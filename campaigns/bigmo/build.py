"""BigMo — umbrella brand campaign: seven products, one rule.

Brand: the BiGMo lockup as the products ship it (eotpcs bigmo-logo.tsx, MarketPulse
terminal.css): Archivo 900, "BiG" in ink, orange "M" #FF6A2C, blue-soft "o" #5C82FF,
blue double chevron #2D5BFF. Sign-off "Get the Big Mo." (LakshyaPrep PoweredByBigMo).

Product cards reuse each campaign's own output (campaigns/<app>/output), so every
product keeps its own look inside the portfolio. Build the product campaigns first.

Claims: "seven products we build" — not "seven launched products"; EOT-PCS is a pilot,
Ledger Book is early access. No user counts, revenue or growth figures.

Run:  python3 campaigns/bigmo/build.py [--no-video]
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAMP = HERE.parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import socialkit as sk  # noqa: E402
from PIL import Image, ImageDraw, ImageFilter, ImageFont  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--no-video", action="store_true")
args = ap.parse_args()
OUT = HERE / "output"
FONTS = HERE.parents[1] / "tools/fonts"

NAVY, NAVY2, INK, WHITE, MUTED = "#0A0F1F", "#141C33", "#11151F", "#F4F6FA", "#9AA3B8"
ORANGE, BLUE, BLUE_SOFT, PAPER = "#FF6A2C", "#2D5BFF", "#5C82FF", "#F3F4F7"
TAGLINE = "Get the Big Mo."
RULE_A, RULE_B = "AI does the work.", "People make the call."

PRODUCTS = [
    dict(key="lakshyaprep", name="LakshyaPrep", cat="EdTech", line="Goal-based SAT, ACT and MCAT prep. Pick one score; the route is built and re-planned until you land it.",
         rule="AI scans and plans. A 1:1 coach leads.", tag="Lock the goal. Own the score.", card="instagram/posts/post-01-main-character-score.png", col="#0088B0"),
    dict(key="marketpulse", name="AI MarketPulse", cat="FinTech", line="AI-assisted market research with a deterministic risk core and a full audit trail. Paper-trading first.",
         rule="AI interprets. Code decides.", tag="Risk control is the product.", card="instagram/carousel-signal-to-trade/slide-01.png", col="#FF6A2C"),
    dict(key="desisquare", name="DesiSquare", cat="Community", line="A pseudonymous, percent-only community where desi investors abroad answer each other's money questions.",
         rule="People answer. Helpfulness earns standing.", tag="Money questions. Desi answers.", card="instagram/carousel-desi-answers/slide-01.png", col="#0C637C"),
    dict(key="eotpcs", name="EOT-PCS", cat="Trade ops · pilot", line="One controlled record for every export shipment, from proforma invoice to payment closure.",
         rule="AI flags. Maker and checker approve.", tag="From PI to paid.", card="instagram/carousel-pi-to-paid/slide-01.png", col="#5980A6"),
    dict(key="swaad", name="Swaad", cat="Niche commerce", line="101 handmade South Indian foods from a Chennai kitchen, run on BigMo's six-stage order flow.",
         rule="AI briefs the shop floor. Staff decide.", tag="The whole South Indian counter, shipped.", card="instagram/posts/post-04-101-things.png", col="#087B61"),
    dict(key="kpm-rentals", name="KPMRentals", cat="PropTech", line="AI-native property management for single-family rentals — Memphis-first, built for remote owners.",
         rule="AI triages and prices. Owners approve.", tag="Without the 2 a.m. calls.", card="instagram/carousel-remote-owners/slide-01.png", col="#064E3B"),
    dict(key="ledgerbook", name="Ledger Book", cat="Accounting · early access", line="The AI bookkeeper on a real double-entry engine: only balanced, approved entries ever post.",
         rule="AI proposes. The ledger disposes.", tag="AI proposes. You approve.", card="instagram/carousel-ai-proposes/slide-01.png", col="#2B52C4"),
]


def rgb(h, a=255):
    return sk.hex2rgb(h, a)


def arch(size, w=900):
    return ImageFont.truetype(str(FONTS / f"Archivo-{w}.ttf"), size)


def inter(size, w="Regular"):
    return ImageFont.truetype(f"/usr/share/fonts/opentype/inter/Inter-{w}.otf", size)


# ------------------------------------------------------------- brand pieces

def bg(size, light=False, seed=0):
    W, H = size
    if light:
        g = sk.canvas(size, PAPER)
    else:
        g = Image.new("RGBA", size)
        d = ImageDraw.Draw(g)
        a, b = rgb(NAVY2), rgb(NAVY)
        for y in range(H):
            t = y / H
            d.line([(0, y), (W, y)], fill=tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3)) + (255,))
    # momentum chevrons, huge and faint, bottom-right
    lay = Image.new("RGBA", size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    s = max(W, H) * .55
    x0, y0 = W - s * .95, H - s * .62
    for k, col in enumerate([ORANGE, BLUE]):
        ox = x0 + k * s * .36
        ld.polygon([(ox, y0), (ox + s * .36, y0 + s * .3), (ox, y0 + s * .6)], fill=rgb(col, 20 if not light else 16))
    g.alpha_composite(lay)
    return g


def lockup(img, x, y, h, dark=True):
    """BiG(ink) M(orange) o(blue-soft) + blue double chevron. Returns width."""
    f = arch(int(h), 900)
    ink = WHITE if dark else INK
    w = sk.draw_text(img, (x, y), "BiG", f, rgb(ink), tracking_px=-h * .02)
    w += sk.draw_text(img, (x + w, y), "M", f, rgb(ORANGE), tracking_px=-h * .02)
    w += sk.draw_text(img, (x + w, y), "o", f, rgb(BLUE_SOFT), tracking_px=-h * .02)
    d = ImageDraw.Draw(img)
    cy = y + h * .62
    ch = h * .56
    cw = ch * 26 / 15 / 2
    cx = x + w + h * .2
    for k in range(2):
        ox = cx + k * cw
        d.polygon([(ox, cy - ch / 2), (ox + cw, cy), (ox, cy + ch / 2)], fill=rgb(BLUE))
    return w + h * .2 + cw * 2


def lockup_w(h):
    return lockup(Image.new("RGBA", (10, 10)), 0, 0, h)


def kick(img, xy, s, size, col=ORANGE):
    sk.draw_text(img, xy, s.upper(), inter(size, "SemiBold"), rgb(col), tracking_px=size * .18)


def head(img, xy, s, size, max_w, col=WHITE, lh=1.0, align="left"):
    return sk.block(img, xy, s, arch(size, 900), rgb(col), max_w, line_h=lh, tracking_px=-size * .025, align=align)


def para(img, xy, s, size, max_w, col=MUTED, lh=1.42, align="left"):
    return sk.block(img, xy, s, inter(size), rgb(col), max_w, line_h=lh, align=align)


def btn(img, x, y, s, size=30):
    return sk.pill(img, (x, y), s, inter(size, "SemiBold"), "#FFFFFF", ORANGE, pad=(int(size * .9), int(size * .55)), radius=int(size * .3))


def foot(img, W, H, m, size=20, light=False, page=None):
    c = "#6B748A" if not light else "#6B7280"
    para(img, (m, H - m * .9), "BigMo · " + TAGLINE + " · bigmoda.ai", size, W - 2 * m, col=c)
    if page:
        sk.draw_text(img, (W - m - inter(size).getlength(page), H - m * .9), page, inter(size), rgb(c))


def card(p, h):
    """The product's own campaign cover, as a portfolio card."""
    im = Image.open(CAMP / p["key"] / "output" / p["card"]).convert("RGB")
    w = int(h * im.size[0] / im.size[1])
    return sk.rounded(im.resize((w, h), Image.LANCZOS), int(h * .03))


def lift(base, im, xy, op=150):
    sk.shadow_paste(base, im, xy, blur=36, offset=(0, 24), opacity=op)


def rule_chip(img, x, y, s, col, size=24):
    return sk.pill(img, (x, y), s, inter(size, "SemiBold"), "#FFFFFF", col, pad=(int(size * .7), int(size * .4)), radius=int(size * .35))


# ======================================================================= INSTAGRAM

def ig_portfolio():
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []
    s = bg((W, H))
    lockup(s, m, 90, 64)
    kick(s, (m, 300), "The BigMo portfolio", 26)
    y = head(s, (m, 350), "Seven products.", 118, W - 2 * m)
    y = head(s, (m, y), "One rule.", 118, W - 2 * m, col=ORANGE)
    y = para(s, (m, y + 30), f"{RULE_A} {RULE_B}", 44, W - 2 * m, col=WHITE)
    # fan of mini cards
    x = m
    for i, p in enumerate(PRODUCTS):
        c = card(p, 250)
        s.alpha_composite(c.rotate(0), (int(x), int(H - 420 + (i % 2) * 30)))
        x += (W - 2 * m - c.size[0]) / 6
    kick(s, (m, H - 120), "Swipe · meet all seven", 22, MUTED)
    out.append(s)

    for i, p in enumerate(PRODUCTS, 1):
        s = bg((W, H), seed=i)
        kick(s, (m, 90), f"{i:02d} / 07 · {p['cat']}", 22, MUTED)
        y = head(s, (m, 140), p["name"], 96, W - 2 * m)
        y = para(s, (m, y + 14), p["line"], 30, W - 2 * m, col="#D7DCE6")
        rule_chip(s, m, int(y + 18), p["rule"], p["col"], 24)
        c = card(p, H - int(y) - 260)
        lift(s, c, ((W - c.size[0]) // 2, int(y) + 100))
        foot(s, W, H, m, page=f"{i + 1} / 9")
        out.append(s)

    s = bg((W, H))
    lockup(s, m, 90, 64)
    y = head(s, (m, 330), RULE_A, 112, W - 2 * m)
    y = head(s, (m, y), RULE_B, 112, W - 2 * m, col=ORANGE)
    para(s, (m, y + 40), "That's the line every BigMo product holds — in classrooms, trading desks, export offices, kitchens, rentals and ledgers.", 36, W - 2 * m, col="#D7DCE6")
    btn(s, m, y + 290, TAGLINE + "  bigmoda.ai", 34)
    foot(s, W, H, m, page="9 / 9")
    out.append(s)
    for i, s in enumerate(out, 1):
        sk.save(s, OUT / "instagram/carousel-portfolio" / f"slide-{i:02d}.png")


def ig_posts():
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    s = bg((W, H))
    lockup(s, m, 90, 56)
    y = head(s, (m, 420), RULE_A, 128, W - 2 * m)
    head(s, (m, y), RULE_B, 128, W - 2 * m, col=ORANGE)
    foot(s, W, H, m)
    out.append(("post-01-manifesto", s))

    s = bg((W, H))
    kick(s, (m, 90), "The BigMo portfolio", 24)
    head(s, (m, 130), "Seven products. One rule.", 76, W - 2 * m)
    cols, gap = 4, 22
    cw = (W - 2 * m - (cols - 1) * gap) // cols
    for i, p in enumerate(PRODUCTS):
        c = card(p, int(cw * 1.25))
        x = m + (i % cols) * (cw + gap) + (cw - c.size[0]) // 2
        yy = 300 + (i // cols) * (c.size[1] + 90)
        lift(s, c, (x, yy), 120)
        f = inter(22, "SemiBold")
        sk.draw_text(s, (x, yy + c.size[1] + 16), p["name"], f, rgb(WHITE))
    # 8th tile: the rule
    x, yy = m + 3 * (cw + gap), 300 + int(cw * 1.25) + 90
    ImageDraw.Draw(s).rounded_rectangle([x, yy, x + cw, yy + int(cw * 1.25)], 12, outline=rgb(ORANGE), width=3)
    sk.block(s, (x + 20, yy + 40), "AI does the work. People make the call.", arch(30, 800), rgb(WHITE), cw - 40, line_h=1.1)
    foot(s, W, H, m)
    out.append(("post-02-seven-products", s))

    s = bg((W, H), light=True)
    lw = lockup_w(170)
    lockup(s, (W - lw) / 2, 470, 170, dark=False)
    head(s, (m, 760), TAGLINE, 90, W - 2 * m, col=INK, align="center")
    para(s, (m, 900), "Momentum, built into every product.", 36, W - 2 * m, col="#4B5563", align="center")
    foot(s, W, H, m, light=True)
    out.append(("post-03-get-the-big-mo", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/posts" / f"{n}.png")


def ig_stories():
    W, H = sk.IG_STORY
    m = 90
    s = bg((W, H))
    lockup(s, m, 160, 70)
    y = head(s, (m, 520), "Which BigMo product should you try first?", 104, W - 2 * m)
    para(s, (m, y + 40), "(Quiz sticker: Students · Investors · Exporters · Landlords · Small business)", 32, W - 2 * m, col="#6B748A")
    sk.save(s, OUT / "instagram/stories/story-01-quiz.png")
    s = bg((W, H))
    lockup(s, m, 160, 70)
    y = head(s, (m, 420), RULE_A, 120, W - 2 * m)
    y = head(s, (m, y), RULE_B, 120, W - 2 * m, col=ORANGE)
    x, yy = m, y + 100
    for i, p in enumerate(PRODUCTS[:6]):
        c = card(p, 355)
        s.alpha_composite(c, (int(m + (i % 3) * (c.size[0] + 20)), int(yy + (i // 3) * 385)))
    foot(s, W, H, m, 26)
    sk.save(s, OUT / "instagram/stories/story-02-manifesto.png")


def sizzle(size, out_path, secs=2.3):
    """Hard-hitting sizzle: rule → each product (card + name + its rule) → lockup."""
    W, H = size
    vertical = H > W
    m = 90 if vertical else 140
    sc = []
    s = bg(size)
    if vertical:
        y = head(s, (m, 700), RULE_A, 130, W - 2 * m)
        head(s, (m, y), RULE_B, 130, W - 2 * m, col=ORANGE)
    else:
        y = head(s, (m, 380), RULE_A, 130, W - 2 * m)
        head(s, (m, y), RULE_B, 130, W - 2 * m, col=ORANGE)
    sc.append(sk.Scene(s, 2.8))
    for p in PRODUCTS:
        s = bg(size)
        if vertical:
            kick(s, (m, 260), p["cat"], 30, MUTED)
            y = head(s, (m, 310), p["name"], 120, W - 2 * m)
            rule_chip(s, m, int(y + 20), p["rule"], p["col"], 32)
            c = card(p, H - int(y) - 330)
            lift(s, c, ((W - c.size[0]) // 2, int(y) + 130))
        else:
            kick(s, (m, 330), p["cat"], 28, MUTED)
            y = head(s, (m, 380), p["name"], 110, 820)
            y = para(s, (m, y + 20), p["tag"], 40, 820, col="#D7DCE6")
            rule_chip(s, m, int(y + 30), p["rule"], p["col"], 30)
            c = card(p, 900)
            lift(s, c, (W - c.size[0] - 160, (H - 900) // 2))
        sc.append(sk.Scene(s, secs, zoom=1.05))
    s = bg(size)
    lw = lockup_w(200 if vertical else 180)
    lockup(s, (W - lw) / 2, H * .36, 200 if vertical else 180)
    sk.block(s, (m, H * .36 + (330 if vertical else 290)), TAGLINE, arch(80, 900), rgb(ORANGE), W - 2 * m, align="center")
    sk.block(s, (m, H * .36 + (460 if vertical else 410)), "Seven products. One rule. · bigmoda.ai", inter(40), rgb(WHITE), W - 2 * m, align="center")
    sc.append(sk.Scene(s, 3.4, move="out", zoom=1.04))
    sk.render_video(sc, size, out_path)
    return sc


# ======================================================================= LINKEDIN

def li_brand():
    """Company page banner (1128x191) and logo (400x400), plus link images."""
    W, H = 1128, 191
    s = bg((W, H))
    lockup(s, 180, 40, 44)  # left ~170px is covered by the page's logo on desktop
    sk.draw_text(s, (180, 100), RULE_A, inter(18, "SemiBold"), rgb(WHITE))
    sk.draw_text(s, (180, 126), RULE_B, inter(18, "SemiBold"), rgb(ORANGE))
    x = W - 24
    for p in reversed(PRODUCTS):
        c = card(p, 112)
        x -= c.size[0] + 8
        s.alpha_composite(c, (int(x), 40))
    sk.save(s, OUT / "linkedin/company-banner-1128x191.png")
    s = bg((400, 400))
    lw = lockup_w(84)
    lockup(s, (400 - lw) / 2, 150, 84)
    sk.save(s, OUT / "linkedin/company-logo-400x400.png")

    W, H = sk.LI_LINK
    m = 60
    s = bg((W, H))
    lockup(s, m, 60, 56)
    y = head(s, (m, 200), RULE_A, 64, 560)
    head(s, (m, y), RULE_B, 64, 560, col=ORANGE)
    x = 640
    for i, p in enumerate(PRODUCTS[:4]):
        c = card(p, 240)
        s.alpha_composite(c, (x + (i % 2) * (c.size[0] + 18), 50 + (i // 2) * 270))
    sk.save(s, OUT / "linkedin/images/link-01-portfolio.png")


def li_document():
    W, H = sk.LI_SQUARE
    m = 90
    pages = []
    s = bg((W, H))
    lockup(s, m, 100, 64)
    y = head(s, (m, 380), "Seven products.", 110, W - 2 * m)
    y = head(s, (m, y), "One rule.", 110, W - 2 * m, col=ORANGE)
    para(s, (m, y + 40), "How BigMo builds AI products people can trust — in education, markets, community, trade, commerce, property and accounting.", 34, W - 2 * m, col="#D7DCE6")
    pages.append(s)
    for i, p in enumerate(PRODUCTS, 2):
        s = bg((W, H), seed=i)
        kick(s, (m, 90), p["cat"], 22, MUTED)
        y = head(s, (m, 136), p["name"], 72, 500)
        y = para(s, (m, y + 16), p["line"], 28, 480, col="#D7DCE6")
        rule_chip(s, m, int(y + 26), p["rule"], p["col"], 22)
        c = card(p, 600)
        lift(s, c, (W - c.size[0] - m, (H - 600) // 2 - 20))
        lockup(s, m, H - 110, 36)
        sk.draw_text(s, (m + 200, H - 104), f"{i} / 9", inter(22), rgb("#6B748A"))
        pages.append(s)
    s = bg((W, H))
    lockup(s, m, 100, 64)
    y = head(s, (m, 360), RULE_A, 100, W - 2 * m)
    y = head(s, (m, y), RULE_B, 100, W - 2 * m, col=ORANGE)
    para(s, (m, y + 40), "Building in one of these spaces, or want early access? team@bigmoda.ai", 36, W - 2 * m, col="#D7DCE6")
    btn(s, m, y + 200, TAGLINE, 36)
    pages.append(s)
    sk.pdf(pages, OUT / "linkedin/document-seven-products-one-rule.pdf")
    for i, p in enumerate(pages, 1):
        sk.save(p, OUT / "linkedin/document-pages" / f"page-{i:02d}.png")


if __name__ == "__main__":
    ig_portfolio()
    ig_posts()
    ig_stories()
    li_brand()
    li_document()
    if not args.no_video:
        sc = sizzle(sk.IG_STORY, OUT / "instagram/reel-seven-products-9x16.mp4")
        sk.save(sc[0].frame, OUT / "instagram/reel-cover.png")
        sc = sizzle(sk.LI_VIDEO, OUT / "linkedin/video-sizzle-16x9.mp4", secs=3.0)
        sk.save(sc[1].frame, OUT / "linkedin/video-cover.png")
    print("done →", OUT)
