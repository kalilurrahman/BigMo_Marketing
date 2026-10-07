"""Phase 2 (month two) template engine, shared by every campaign.

A campaign supplies a `Kit` — its own brand functions (usually thin wrappers over the
helpers already in its build.py) — and a `content` dict. The engine lays out:

  instagram/phase2/carousel-myths/slide-NN.png   myth-vs-fact carousel (cover, 4 myths, CTA)
  instagram/phase2/post-0N-<slug>.png            three feature deep-dives (4:5)
  instagram/phase2/reel-month2-9x16.mp4          ~12 s reel (hook, 2 features, end card)
  linkedin/phase2/document-myths.pdf             the carousel as a LinkedIn document (4:5)

content = {
  "myths": {"kicker", "title_a", "title_b", "sub",
            "items": [(myth, fact_headline, fact_body), ...4],
            "cta_a", "cta_b", "cta_body", "cta_button"},
  "posts": [{"slug", "kicker", "a", "b", "body", "visual": callable(width, max_h) -> RGBA,
             "dark": bool}, ...3],
  "reel":  {"hook_a", "hook_b", "end_a", "end_b", "end_sub"},
}
"""
from dataclasses import dataclass
from typing import Callable

from PIL import ImageDraw

import socialkit as sk


@dataclass
class Kit:
    bg: Callable            # (size, dark) -> RGBA
    logo: Callable          # (img, x, y, h, dark) -> width
    head: Callable          # (img, xy, text, size, max_w, dark, accent) -> bottom y
    body: Callable          # (img, xy, text, size, max_w, dark) -> bottom y
    kick: Callable          # (img, xy, text, size, dark)
    cta: Callable           # (img, x, y, text, size, dark)
    foot: Callable          # (img, W, H, m, dark, page)
    lift: Callable          # (base, im, xy, dark)
    muted: str              # strike/secondary colour on light
    muted_dark: str         # on dark
    accent: str             # "FACT" label colour on light
    accent_dark: str
    body_font: Callable = None  # (size) -> ImageFont used by kit.body (for exact strike widths)


def _strike(img, xy, text, kit, size, max_w, dark):
    """Myth line: muted, with a rule struck through each rendered line (measured, not guessed)."""
    col = kit.muted_dark if dark else kit.muted
    y0 = xy[1]
    y1 = kit.body(img, xy, text, size, max_w, dark, col)
    d = ImageDraw.Draw(img)
    f = kit.body_font(size) if kit.body_font else None
    lines = sk.wrap(f, text, max_w) if f else [text]
    step = (y1 - y0) / max(1, len(lines))
    for i, ln in enumerate(lines):
        w = f.getlength(ln) if f else max_w * .9
        ly = y0 + i * step + size * .62
        d.line([(xy[0] - 6, ly), (xy[0] + w + 6, ly)], fill=sk.hex2rgb(col), width=max(2, size // 12))
    return y1


def _centred(img, H, draw, top=150, bottom=160):
    """Run draw(img, y0)->bottom on a scratch copy to measure it, then draw it vertically centred."""
    scratch = img.copy()
    h = draw(scratch, 0)
    y0 = max(top, top + (H - top - bottom - h) // 2)
    return draw(img, y0)


def myths(kit, c, out_ig, out_li):
    W, H = sk.IG_PORTRAIT
    m = 84
    pages = []
    s = kit.bg((W, H), True)
    kit.logo(s, m, 96, 58, True)
    kit.kick(s, (m, 330), c["kicker"], 26, True)
    y = kit.head(s, (m, 380), c["title_a"], 112, W - 2 * m, True, False)
    y = kit.head(s, (m, y), c["title_b"], 112, W - 2 * m, True, True)
    kit.body(s, (m, y + 50), c["sub"], 38, W - 2 * m, True)
    kit.kick(s, (m, H - 150), "Swipe · 4 myths", 22, True)
    kit.foot(s, W, H, m, True, None)
    pages.append(s)
    n = len(c["items"])
    for i, (myth, fh, fb) in enumerate(c["items"], 1):
        s = kit.bg((W, H), False)
        kit.kick(s, (m, 100), f"Myth {i} / {n}", 24, False)

        def draw(img, y0, myth=myth, fh=fh, fb=fb):
            y = _strike(img, (m, y0), myth, kit, 50, W - 2 * m, False)
            kit.kick(img, (m, y + 80), "Fact", 28, False)
            y = kit.head(img, (m, y + 134), fh, 104, W - 2 * m, False, True)
            return kit.body(img, (m, y + 30), fb, 40, W - 2 * m, False)

        _centred(s, H, draw)
        kit.foot(s, W, H, m, False, f"{i + 1} / {n + 2}")
        pages.append(s)
    s = kit.bg((W, H), True)
    kit.logo(s, m, 96, 58, True)
    y = kit.head(s, (m, 360), c["cta_a"], 100, W - 2 * m, True, False)
    y = kit.head(s, (m, y), c["cta_b"], 100, W - 2 * m, True, True)
    y = kit.body(s, (m, y + 30), c["cta_body"], 36, W - 2 * m, True)
    kit.cta(s, m, int(y + 60), c["cta_button"], 34, True)
    kit.foot(s, W, H, m, True, f"{n + 2} / {n + 2}")
    pages.append(s)
    for i, p in enumerate(pages, 1):
        sk.save(p, out_ig / "carousel-myths" / f"slide-{i:02d}.png")
    sk.pdf(pages, out_li / "document-myths.pdf")
    return pages


def posts(kit, items, out_ig):
    W, H = sk.IG_PORTRAIT
    m = 84
    out = []
    for i, p in enumerate(items, 1):
        dark = p.get("dark", False)
        s = kit.bg((W, H), dark)
        kit.kick(s, (m, 100), p["kicker"], 24, dark)
        y = kit.head(s, (m, 150), p["a"], 90, W - 2 * m, dark, False)
        y = kit.head(s, (m, y), p["b"], 90, W - 2 * m, dark, True)
        y = kit.body(s, (m, y + 18), p["body"], 32, W - 2 * m, dark)
        v = p["visual"](W - 2 * m, int(H - y - 190))
        kit.lift(s, v, ((W - v.size[0]) // 2, int(y + 46)), dark)
        kit.foot(s, W, H, m, dark, None)
        sk.save(s, out_ig / f"post-0{i}-{p['slug']}.png")
        out.append(s)
    return out


def reel(kit, c, items, out_ig):
    W, H = sk.IG_STORY
    m = 90
    sc = []
    s = kit.bg((W, H), True)
    y = kit.head(s, (m, 700), c["hook_a"], 120, W - 2 * m, True, False)
    kit.head(s, (m, y), c["hook_b"], 120, W - 2 * m, True, True)
    kit.foot(s, W, H, m, True, None)
    sc.append(sk.Scene(s, 2.6))
    for p in items[:2]:
        s = kit.bg((W, H), False)
        y = kit.head(s, (m, 260), p["a"], 100, W - 2 * m, False, False)
        y = kit.head(s, (m, y), p["b"], 100, W - 2 * m, False, True)
        v = p["visual"](W - 2 * m, int(H - y - 260))
        kit.lift(s, v, ((W - v.size[0]) // 2, int(y + 70)), False)
        kit.foot(s, W, H, m, False, None)
        sc.append(sk.Scene(s, 3.2))
    s = kit.bg((W, H), True)
    kit.logo(s, m, 560, 90, True)
    y = kit.head(s, (m, 800), c["end_a"], 100, W - 2 * m, True, False)
    y = kit.head(s, (m, y), c["end_b"], 100, W - 2 * m, True, True)
    kit.body(s, (m, y + 40), c["end_sub"], 40, W - 2 * m, True)
    kit.foot(s, W, H, m, True, None)
    sc.append(sk.Scene(s, 3.2, move="out", zoom=1.05))
    sk.render_video(sc, (W, H), out_ig / "reel-month2-9x16.mp4")
    sk.save(sc[0].frame, out_ig / "reel-month2-cover.png")


def build(kit, content, out_root, video=True):
    out_ig = out_root / "instagram/phase2"
    out_li = out_root / "linkedin/phase2"
    out_ig.mkdir(parents=True, exist_ok=True)
    out_li.mkdir(parents=True, exist_ok=True)
    myths(kit, content["myths"], out_ig, out_li)
    posts(kit, content["posts"], out_ig)
    if video:
        reel(kit, content["reel"], content["posts"], out_ig)
