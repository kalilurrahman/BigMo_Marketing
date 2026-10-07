"""Platform pack: re-cut every campaign for X, Facebook, YouTube (incl. Shorts) and TikTok.

Only sizes that genuinely differ are rendered; everything else is mapped to an existing
file in PLATFORMS.md (Facebook takes the 4:5 posts and 9:16 reels as-is, TikTok/Shorts
take the reels, X takes the 16:9 film).

Per campaign, writes campaigns/<app>/output/platforms/:
  x/post-NN-1600x900.png        LinkedIn link images re-fit to 16:9 (edge-extended, no crop)
  x-header-1500x500.png         card strip, left third kept clear for the avatar
  facebook-cover-1640x624.png   card strip, safe for desktop + mobile crops
  linkedin-banner-1584x396.png  personal-profile banner (team members' profiles)
  youtube-thumbnail-1280x720.png  from the 16:9 film cover

Run:  python3 tools/platforms.py [app ...]      (default: every campaign with an output/)
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

import socialkit as sk

ROOT = Path(__file__).resolve().parents[1] / "campaigns"

# Which of each campaign's own images to show in banners (most on-brand first).
STRIP = {
    "lakshyaprep": ["instagram/carousel-method/slide-01.png", "instagram/posts/post-01-main-character-score.png",
                    "instagram/posts/post-02-sat.png", "instagram/posts/post-03-act.png", "instagram/posts/post-04-mcat.png"],
    "marketpulse": ["instagram/carousel-signal-to-trade/slide-01.png", "instagram/posts/post-02-17-gates.png",
                    "instagram/posts/post-01-kill-switch.png", "instagram/posts/post-04-trace-id.png", "instagram/posts/post-03-paper-first.png"],
    "desisquare": ["instagram/carousel-desi-answers/slide-01.png", "instagram/posts/post-02-never-by-money.png",
                   "instagram/posts/post-01-you-are-not-alone.png", "instagram/posts/post-03-privacy.png", "instagram/posts/post-05-six-corridors.png"],
    "eotpcs": ["instagram/carousel-pi-to-paid/slide-01.png", "instagram/posts/post-02-eight-stages.png",
               "instagram/posts/post-01-before-after.png", "instagram/posts/post-03-maker-checker.png", "instagram/posts/post-04-audit.png"],
    "swaad": ["instagram/carousel-seven-counters/slide-01.png", "instagram/posts/post-01-karupatti-halwa.png",
              "instagram/posts/post-04-101-things.png", "instagram/posts/post-02-idli-podi.png", "instagram/posts/post-03-avakkai.png"],
    "kpm-rentals": ["instagram/carousel-remote-owners/slide-01.png", "instagram/posts/post-01-your-property.png",
                    "instagram/posts/post-04-humans-in-the-middle.png", "instagram/posts/post-02-residents.png", "instagram/posts/post-05-rental-analysis.png"],
    "ledgerbook": ["instagram/carousel-ai-proposes/slide-01.png", "instagram/posts/post-01-debits-equal-credits.png",
                   "instagram/posts/post-03-copilot-read-only.png", "instagram/posts/post-02-shows-its-work.png", "instagram/posts/post-04-today.png"],
    "bigmo": ["instagram/posts/post-01-manifesto.png", "instagram/carousel-portfolio/slide-02.png", "instagram/carousel-portfolio/slide-03.png",
              "instagram/carousel-portfolio/slide-05.png", "instagram/carousel-portfolio/slide-08.png"],
}


def ground(src_paths):
    """Banner ground: the cover image blown up, blurred and darkened — always on-brand."""
    im = Image.open(src_paths[0]).convert("RGB")
    return im


def banner(out_dir, size, paths, clear_left, name, card_h_ratio=.78):
    W, H = size
    base = ground(paths)
    s = max(W / base.size[0], H / base.size[1])
    g = base.resize((int(base.size[0] * s) + 1, int(base.size[1] * s) + 1), Image.LANCZOS)
    g = g.crop(((g.size[0] - W) // 2, (g.size[1] - H) // 2, (g.size[0] - W) // 2 + W, (g.size[1] - H) // 2 + H))
    g = g.filter(ImageFilter.GaussianBlur(max(W, H) // 40)).convert("RGBA")
    shade = Image.new("RGBA", (W, H), (0, 0, 0, 90))
    g.alpha_composite(shade)
    ch = int(H * card_h_ratio)
    cards = []
    for p in paths:
        im = Image.open(p).convert("RGB")
        cw = int(ch * im.size[0] / im.size[1])
        cards.append(sk.rounded(im.resize((cw, ch), Image.LANCZOS), max(4, ch // 40)))
    gap = max(8, W // 120)
    avail = W - clear_left - gap
    while cards and sum(c.size[0] for c in cards) + gap * (len(cards) - 1) > avail:
        cards.pop()
    total = sum(c.size[0] for c in cards) + gap * (len(cards) - 1)
    x = clear_left + (avail - total) // 2
    y = (H - ch) // 2
    for c in cards:
        sk.shadow_paste(g, c, (x, y), blur=max(6, H // 30), offset=(0, max(4, H // 60)), opacity=120)
        x += c.size[0] + gap
    sk.save(g, out_dir / name)


def edge_extend(im, size):
    """Fit `im` into `size` by scaling to width and extending its own top/bottom rows."""
    W, H = size
    s = W / im.size[0]
    im = im.resize((W, int(im.size[1] * s)), Image.LANCZOS)
    if im.size[1] >= H:
        top = (im.size[1] - H) // 2
        return im.crop((0, top, W, top + H))
    pad = H - im.size[1]
    t = pad // 2
    out = Image.new("RGB", size)
    out.paste(im, (0, t))
    top_row = im.crop((0, 0, W, 1)).resize((W, t))
    bot_row = im.crop((0, im.size[1] - 1, W, im.size[1])).resize((W, pad - t))
    out.paste(top_row, (0, 0))
    out.paste(bot_row, (0, t + im.size[1]))
    return out


def run(app):
    o = ROOT / app / "output"
    if not o.exists():
        return False
    pdir = o / "platforms"
    (pdir / "x").mkdir(parents=True, exist_ok=True)
    paths = [o / p for p in STRIP.get(app, []) if (o / p).exists()]
    if not paths:
        paths = sorted((o / "instagram/posts").glob("*.png"))[:5]
    banner(pdir, (1500, 500), paths, clear_left=420, name="x-header-1500x500.png")
    banner(pdir, (1640, 624), paths, clear_left=380, name="facebook-cover-1640x624.png", card_h_ratio=.72)
    banner(pdir, (1584, 396), paths, clear_left=440, name="linkedin-banner-1584x396.png")
    for i, li in enumerate(sorted((o / "linkedin/images").glob("*.png")), 1):
        sk.save(edge_extend(Image.open(li).convert("RGB"), (1600, 900)), pdir / "x" / f"post-{i:02d}-1600x900.png")
    cov = o / "linkedin/video-cover.png"
    if cov.exists():
        sk.save(Image.open(cov).convert("RGB").resize((1280, 720), Image.LANCZOS), pdir / "youtube-thumbnail-1280x720.png")
    return True


if __name__ == "__main__":
    apps = sys.argv[1:] or sorted(p.name for p in ROOT.iterdir() if (p / "output").exists())
    for a in apps:
        print(a, "ok" if run(a) else "skipped (no output/)")
