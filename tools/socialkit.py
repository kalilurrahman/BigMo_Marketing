"""socialkit — tiny, dependency-light generator for BigMo social campaign assets.

Pillow draws every frame; ffmpeg stitches frames into MP4s. Each campaign
(campaigns/<app>/build.py) supplies a Brand and its own copy + screenshots;
this module owns layout primitives so all campaigns share one craft level.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
FONTS = ROOT / "fonts"

# Platform sizes (px)
IG_SQUARE = (1080, 1080)
IG_PORTRAIT = (1080, 1350)   # feed post / carousel slide
IG_STORY = (1080, 1920)      # story / reel
LI_LINK = (1200, 627)        # link / single-image share
LI_SQUARE = (1200, 1200)     # document carousel page
LI_VIDEO = (1920, 1080)


def hex2rgb(h: str, a: int | None = None):
    h = h.lstrip("#")
    t = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    return t + (a,) if a is not None else t


@dataclass
class Brand:
    name: str
    bg: str
    surface: str
    ink: str
    muted: str
    primary: str          # CTA colour
    accent: str           # emphasis colour
    highlight: str = "#EDBB00"
    dark_bg: str = "#17151A"
    dark_ink: str = "#F3F2F2"
    font_regular: str = str(FONTS / "SourceSerif4-400-normal.ttf")
    font_bold: str = str(FONTS / "SourceSerif4-600-normal.ttf")
    font_italic: str = str(FONTS / "SourceSerif4-400-italic.ttf")
    misreg: bool = False  # cyan/magenta offset shadow on display type
    misreg_a: str = "#0088B0"
    misreg_b: str = "#D6006C"
    radius: int = 2
    url: str = ""
    handle: str = ""
    footer: str = ""
    logo_fn: object = None  # callable(draw_img, xy, height, dark) -> width
    tracking: float = -0.03  # display letter-spacing (em)

    def font(self, size: int, style: str = "regular"):
        path = {"regular": self.font_regular, "bold": self.font_bold, "italic": self.font_italic}[style]
        return ImageFont.truetype(path, size)


# ---------------------------------------------------------------- text

def text_width(font, s: str, tracking_px: float = 0.0) -> float:
    if not s:
        return 0
    return font.getlength(s) + tracking_px * (len(s) - 1)


def draw_text(img, xy, s, font, fill, tracking_px=0.0, shadow=None):
    """Draw a single line with optional letter-spacing and misreg shadow pair."""
    d = ImageDraw.Draw(img)
    x, y = xy
    passes = []
    if shadow:
        passes += shadow  # list of ((dx,dy), rgba)
    passes.append(((0, 0), fill))
    for (dx, dy), col in passes:
        if col is None:
            continue
        if tracking_px == 0:
            if len(col) == 4 and col[3] < 255:
                layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
                ImageDraw.Draw(layer).text((x + dx, y + dy), s, font=font, fill=col)
                img.alpha_composite(layer) if img.mode == "RGBA" else img.paste(layer, (0, 0), layer)
            else:
                d.text((x + dx, y + dy), s, font=font, fill=col)
            continue
        cx = x
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        for ch in s:
            ld.text((cx + dx, y + dy), ch, font=font, fill=col)
            cx += font.getlength(ch) + tracking_px
        if img.mode == "RGBA":
            img.alpha_composite(layer)
        else:
            img.paste(layer, (0, 0), layer)
    return text_width(font, s, tracking_px)


def wrap(font, s: str, max_w: int, tracking_px=0.0):
    lines = []
    for para in s.split("\n"):
        words, cur = para.split(" "), ""
        for w in words:
            t = (cur + " " + w).strip()
            if text_width(font, t, tracking_px) <= max_w or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def block(img, xy, s, font, fill, max_w, line_h=1.15, tracking_px=0.0, shadow=None, align="left"):
    """Wrapped paragraph. Returns bottom y."""
    x, y = xy
    asc = font.size
    for ln in wrap(font, s, max_w, tracking_px):
        lx = x
        if align == "center":
            lx = x + (max_w - text_width(font, ln, tracking_px)) / 2
        draw_text(img, (lx, y), ln, font, fill, tracking_px, shadow)
        y += asc * line_h
    return y


def fit_font(brand, s, max_w, max_size, style="bold", min_size=24, max_lines=3, tracking=None):
    tr = brand.tracking if tracking is None else tracking
    size = max_size
    while size > min_size:
        f = brand.font(size, style)
        if len(wrap(f, s, max_w, tr * size)) <= max_lines:
            return f
        size -= 4
    return brand.font(min_size, style)


def misreg_shadow(brand, scale=1.0):
    if not brand.misreg:
        return None
    o = max(2, round(3 * scale))
    return [((-o, 0), hex2rgb(brand.misreg_a, 180)), ((o, o // 2), hex2rgb(brand.misreg_b, 165))]


# ---------------------------------------------------------------- canvas + furniture

def canvas(size, colour):
    return Image.new("RGBA", size, hex2rgb(colour, 255))


def grain(img, amount=10, seed=7):
    """Subtle risograph/paper grain."""
    import random
    random.seed(seed)
    w, h = img.size
    noise = Image.effect_noise((w // 2, h // 2), amount).resize((w, h)).convert("L")
    layer = Image.merge("RGBA", (noise, noise, noise, noise.point(lambda v: 14)))
    out = img.copy()
    out.alpha_composite(layer)
    return out


def rounded(im, r):
    if r <= 0:
        return im
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.size[0] - 1, im.size[1] - 1], r, fill=255)
    out = im.convert("RGBA")
    out.putalpha(mask)
    return out


def shadow_paste(base, im, xy, blur=28, offset=(0, 18), opacity=70, radius=0):
    x, y = xy
    sh = Image.new("RGBA", (im.size[0] + blur * 4, im.size[1] + blur * 4), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle(
        [blur * 2, blur * 2, blur * 2 + im.size[0], blur * 2 + im.size[1]], radius, fill=(0, 0, 0, opacity))
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(sh, (int(x - blur * 2 + offset[0]), int(y - blur * 2 + offset[1])))
    base.alpha_composite(im.convert("RGBA"), (int(x), int(y)))


def cap(im, max_h):
    """Crop a framed screenshot to max_h (keeps the top, where the content is)."""
    return im if im.size[1] <= max_h else im.crop((0, 0, im.size[0], int(max_h)))


def load_shot(path, crop_top=0, crop_bottom=0, crop=None):
    im = Image.open(path).convert("RGB")
    if crop:
        im = im.crop(crop)
    w, h = im.size
    return im.crop((0, crop_top, w, h - crop_bottom))


def browser(shot, width, chrome="#E4E2E2", dot=True, url="", radius=14, ink="#605D5D"):
    """Wrap a desktop screenshot in a minimal browser frame, scaled to width."""
    s = width / shot.size[0]
    body = shot.resize((width, int(shot.size[1] * s)), Image.LANCZOS)
    bar = max(28, int(44 * width / 1280))
    out = Image.new("RGBA", (width, body.size[1] + bar), hex2rgb(chrome, 255))
    d = ImageDraw.Draw(out)
    if dot:
        for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
            cx = int(bar * 0.6 + i * bar * 0.45)
            r = int(bar * 0.13)
            d.ellipse([cx - r, bar // 2 - r, cx + r, bar // 2 + r], fill=c)
    if url:
        f = ImageFont.truetype(str(FONTS / "SourceSerif4-400-normal.ttf"), int(bar * 0.38))
        uw = int(width * 0.42)
        ux = (width - uw) // 2
        d.rounded_rectangle([ux, int(bar * 0.2), ux + uw, int(bar * 0.8)], int(bar * 0.2), fill="#F6F5F5")
        tw = f.getlength(url)
        d.text((ux + (uw - tw) / 2, int(bar * 0.27)), url, font=f, fill=ink)
    out.paste(body, (0, bar))
    return rounded(out, radius)


def phone(shot, height, bezel="#1B1A1C"):
    """Wrap a mobile screenshot in a simple phone body, scaled to height."""
    pad = int(height * 0.022)
    inner_h = height - pad * 2
    s = inner_h / shot.size[1]
    scr = shot.resize((int(shot.size[0] * s), inner_h), Image.LANCZOS)
    r_out, r_in = int(height * 0.075), int(height * 0.06)
    out = Image.new("RGBA", (scr.size[0] + pad * 2, height), (0, 0, 0, 0))
    ImageDraw.Draw(out).rounded_rectangle([0, 0, out.size[0] - 1, height - 1], r_out, fill=bezel)
    out.alpha_composite(rounded(scr, r_in), (pad, pad))
    d = ImageDraw.Draw(out)
    nw = int(out.size[0] * 0.28)
    d.rounded_rectangle([(out.size[0] - nw) // 2, pad + int(height * 0.012), (out.size[0] + nw) // 2,
                         pad + int(height * 0.034)], int(height * 0.012), fill=bezel)
    return out


def pill(img, xy, s, font, fg, bg, pad=(18, 9), radius=None, outline=None):
    d = ImageDraw.Draw(img)
    x, y = xy
    w = text_width(font, s) + pad[0] * 2
    h = font.size + pad[1] * 2
    r = h // 2 if radius is None else radius
    d.rounded_rectangle([x, y, x + w, y + h], r, fill=bg, outline=outline, width=2 if outline else 0)
    d.text((x + pad[0], y + pad[1] - font.size * 0.08), s, font=font, fill=fg)
    return w, h


def kicker(img, xy, s, brand, size=26, colour=None, dark=False):
    f = brand.font(size, "bold")
    col = hex2rgb(colour or (brand.dark_ink if dark else brand.muted), 255)
    draw_text(img, xy, s.upper(), f, col, tracking_px=size * 0.12)


def double_rule(img, x0, x1, y, ink, scale=1.0):
    d = ImageDraw.Draw(img)
    d.rectangle([x0, y, x1, y + int(6 * scale)], fill=ink)
    d.rectangle([x0, y + int(10 * scale), x1, y + int(11.5 * scale)], fill=ink)


def save(img, path, fmt=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    im = img.convert("RGB")
    if str(path).endswith(".jpg"):
        im.save(path, quality=92, optimize=True, progressive=True)
    else:
        im.save(path, optimize=True)
    return path


def pdf(pages, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    ims = [p.convert("RGB") for p in pages]
    ims[0].save(path, save_all=True, append_images=ims[1:], resolution=150)
    return path


# ---------------------------------------------------------------- video

@dataclass
class Scene:
    """One video scene: a still frame plus a camera move.

    frame: PIL image at the output size (or larger for zoom headroom).
    secs: duration. move: 'in' (slow push-in), 'out', 'up' (pan down a tall
    image), 'none'.
    """
    frame: Image.Image
    secs: float = 3.0
    move: str = "in"
    zoom: float = 1.06


def _ease(t):
    return 1 - (1 - t) ** 3 if t < 1 else 1.0


def _frame(sc, i, total, size):
    W, H = size
    fr = sc._rgb
    t = _ease(i / max(1, total - 1))
    if sc.move == "up" and fr.size[1] > H:
        sw = W / fr.size[0]
        big = fr if sw == 1 else fr.resize((W, int(fr.size[1] * sw)))
        y = int((big.size[1] - H) * t)
        return big.crop((0, y, W, y + H))
    if sc.move in ("in", "out"):
        z = 1 + (sc.zoom - 1) * (t if sc.move == "in" else 1 - t)
        cw, ch = fr.size[0] / z, fr.size[1] / z
        x0, y0 = (fr.size[0] - cw) / 2, (fr.size[1] - ch) / 2
        return fr.resize(size, Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch))
    return fr if fr.size == size else fr.resize(size)


def render_video(scenes, size, out_path, fps=30, xfade=0.35, crf=20):
    """Rasterise every frame with Pillow (eased push-in/out, cross-fades) and stream it to ffmpeg.

    Frames are generated and written one at a time, so memory stays flat however long
    the video is (the previous version held every frame in memory).
    """
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # write to a git-ignored .partial.mp4 and rename when complete, so a half-written
    # video never shows up as a finished file (or gets committed)
    part = out_path.with_name(out_path.stem + ".partial.mp4")
    proc = subprocess.Popen([
        "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{size[0]}x{size[1]}", "-r", str(fps), "-i", "-",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", str(crf), "-preset", "medium",
        "-movflags", "+faststart", str(part)], stdin=subprocess.PIPE)
    xf = int(xfade * fps)
    for sc in scenes:
        sc._rgb = sc.frame.convert("RGB")
    try:
        for si, sc in enumerate(scenes):
            total = max(1, int(sc.secs * fps))
            nxt = scenes[si + 1] if si + 1 < len(scenes) else None
            ntotal = max(1, int(nxt.secs * fps)) if nxt else 0
            start = xf if si > 0 else 0  # these frames were emitted inside the previous cross-fade
            for i in range(start, total):
                f = _frame(sc, i, total, size)
                k = i - (total - xf)
                if nxt is not None and k >= 0:
                    f = Image.blend(f, _frame(nxt, k, ntotal, size), (k + 1) / (xf + 1))
                proc.stdin.write(f.tobytes())
    finally:
        proc.stdin.close()
        for sc in scenes:
            sc.__dict__.pop("_rgb", None)
    if proc.wait() != 0:
        part.unlink(missing_ok=True)
        raise RuntimeError("ffmpeg failed")
    part.replace(out_path)
    return out_path


def gif_from(images, path, ms=1600, width=540):
    path = Path(path)
    fr = [im.convert("RGB").resize((width, int(im.size[1] * width / im.size[0])), Image.LANCZOS) for im in images]
    fr[0].save(path, save_all=True, append_images=fr[1:], duration=ms, loop=0, optimize=True)
    return path
