"""AI MarketPulse — "Risk control is the product." social campaign (Instagram + LinkedIn).

Brand is taken from the product itself (backend/public/brand/og-midnight.png):
midnight navy ground, white "AI Market" + orange "Pulse", ECG pulse line
fading orange → blue, letter-spaced "AND TRADING AGENT" kicker, Inter type.

Guardrails: paper-trading simulation, not financial advice, no return claims.
Any $ figure visible in a screenshot is simulated demo data and is labelled so.

Run:  python3 campaigns/marketpulse/build.py  [--src ../marketpulse-relay]
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import socialkit as sk  # noqa: E402
from PIL import Image, ImageDraw, ImageFilter  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--src", default=str(HERE.parents[2] / "marketpulse-relay"))
ap.add_argument("--no-video", action="store_true")
args = ap.parse_args()
SRC = Path(args.src)
OUT = HERE / "output"
KIT = SRC / "docs/training-kit/screenshots"

INTER = "/usr/share/fonts/opentype/inter/"
B = sk.Brand(
    name="AI MarketPulse", bg="#0B1020", surface="#141B2E", ink="#F2F4F8", muted="#9AA3B8",
    primary="#FF6A2C", accent="#4F7CFF", highlight="#2BD576", dark_bg="#0B1020", dark_ink="#F2F4F8",
    font_regular=INTER + "Inter-Regular.otf", font_bold=INTER + "InterDisplay-Bold.otf",
    font_italic=INTER + "InterDisplay-Medium.otf", url="big-mo.ai", handle="@bigmo.ai",
    footer="Powered by BigMo · Get the Big Mo.", tracking=-0.025,
)
NAVY, NAVY2 = "#0B1020", "#121A33"
ORANGE, BLUE, GREEN, RED = "#FF6A2C", "#4F7CFF", "#2BD576", "#FF4D5E"
WHITE, MUTED = "#F2F4F8", "#9AA3B8"
DISCLAIMER = "Paper-trading simulation · Not financial advice · Educational use only"


def rgb(h, a=255):
    return sk.hex2rgb(h, a)


# ------------------------------------------------------------- brand pieces

def bg(size, seed=0):
    """Midnight gradient with a faint constellation in the top-right, like the OG image."""
    W, H = size
    g = Image.new("RGBA", size)
    top, bot = rgb(NAVY2), rgb("#070A14")
    d = ImageDraw.Draw(g)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=tuple(int(top[i] * (1 - t) + bot[i] * t) for i in range(3)) + (255,))
    glow = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([W * .45, -H * .3, W * 1.4, H * .5], fill=rgb(BLUE, 34))
    g.alpha_composite(glow.filter(ImageFilter.GaussianBlur(W // 8)))
    import random
    random.seed(seed + W)
    pts = [(W * random.uniform(.68, .97), H * random.uniform(.02, .2)) for _ in range(5)]
    pts.sort()
    lay = Image.new("RGBA", size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    s = W / 1080
    ld.line(pts, fill=rgb(BLUE, 90), width=max(1, int(2 * s)))
    for x, y in pts:
        r = 7 * s
        ld.ellipse([x - r, y - r, x + r, y + r], outline=rgb(BLUE, 140), width=max(1, int(2 * s)))
    g.alpha_composite(lay)
    return g


def pulse(img, x0, x1, y, amp, width=6, beat_at=0.45):
    """ECG pulse line, orange → blue gradient (the product's signature)."""
    W = x1 - x0
    bx = x0 + W * beat_at
    u = amp / 6
    pts = [(x0, y), (bx - 14 * u, y), (bx - 9 * u, y - 1.2 * amp * .25), (bx - 5 * u, y + amp * .12),
           (bx, y - amp), (bx + 5 * u, y + amp * .9), (bx + 10 * u, y - amp * .2), (bx + 14 * u, y + amp * .08),
           (bx + 18 * u, y), (x1, y)]
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).line(pts, fill=255, width=width, joint="curve")
    grad = Image.new("RGBA", img.size)
    gd = ImageDraw.Draw(grad)
    a, b = rgb(ORANGE), rgb(BLUE)
    for x in range(int(x0), int(x1) + 1):
        t = (x - x0) / max(1, W)
        gd.line([(x, 0), (x, img.size[1])], fill=tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3)) + (255,))
    img.paste(grad, (0, 0), mask)


def logo(img, x, y, h, kicker=True):
    """'AI Market' white + 'Pulse' orange, optional AND TRADING AGENT kicker. Returns width."""
    f = B.font(int(h), "bold")
    w1 = sk.draw_text(img, (x, y), "AI Market ", f, rgb(WHITE), tracking_px=-h * .02)
    w2 = sk.draw_text(img, (x + w1, y), "Pulse", f, rgb(ORANGE), tracking_px=-h * .02)
    if kicker:
        k = B.font(int(h * .3), "bold")
        sk.draw_text(img, (x + 2, y + h * 1.18), "AND TRADING AGENT", k, rgb(MUTED), tracking_px=h * .3 * .35)
    return w1 + w2


def mini_logo(img, x, y, h):
    """Small pulse glyph + wordmark for footers."""
    pulse(img, x, x + h * 1.6, y + h * .55, h * .5, width=max(2, int(h * .12)), beat_at=.5)
    f = B.font(int(h * .62), "bold")
    w = sk.draw_text(img, (x + h * 1.9, y + h * .12), "AI Market ", f, rgb(WHITE))
    sk.draw_text(img, (x + h * 1.9 + w, y + h * .12), "Pulse", f, rgb(ORANGE))


def kick(img, xy, s, size, col=ORANGE):
    sk.draw_text(img, xy, s.upper(), B.font(size, "bold"), rgb(col), tracking_px=size * .22)


def head(img, xy, s, size, max_w, col=WHITE, lh=1.04, align="left"):
    return sk.block(img, xy, s, B.font(size, "bold"), rgb(col), max_w, line_h=lh, tracking_px=size * B.tracking, align=align)


def head2(img, xy, a, b_, size, max_w, lh=1.04):
    """Two-tone headline: line a white, line b orange."""
    y = head(img, xy, a, size, max_w)
    return head(img, (xy[0], y), b_, size, max_w, col=ORANGE, lh=lh)


def para(img, xy, s, size, max_w, col=MUTED, lh=1.4, align="left"):
    return sk.block(img, xy, s, B.font(size), rgb(col), max_w, line_h=lh, align=align)


def btn(img, x, y, s, size=30, col=ORANGE, fg="#FFFFFF"):
    return sk.pill(img, (x, y), s, B.font(size, "bold"), fg, col, pad=(int(size * .9), int(size * .55)), radius=int(size * .35))


def chip(img, x, y, s, col, size=22):
    f = B.font(size, "bold")
    return sk.pill(img, (x, y), s, f, NAVY, col, pad=(int(size * .6), int(size * .3)), radius=4)


def disclaimer(img, W, H, m, size=20):
    para(img, (m, H - m * .9), DISCLAIMER, size, W - 2 * m, col="#6B748A")


def shot(name, crop=None, max_h=None):
    im = Image.open(KIT / f"{name}.webp").convert("RGB")
    if crop:
        im = im.crop(crop)
    return im


def desk(name, width, max_h=None, crop=None, url="app.big-mo.ai"):
    br = sk.browser(shot(name, crop), width, chrome="#1C2338", url=url, ink=MUTED, radius=12)
    # browser() draws the URL pill light; recolour for dark chrome
    return sk.cap(br, max_h) if max_h else br


def mob(name, h, bottom=56):
    im = shot(name)
    return sk.phone(im.crop((0, 0, im.size[0], im.size[1] - bottom)), h, bezel="#2A3350")


def glow_paste(base, im, xy, col=BLUE):
    sk.shadow_paste(base, im, xy, blur=40, offset=(0, 24), opacity=170)


# ======================================================================= INSTAGRAM

def ig_carousel():
    """7-slide 4:5 carousel: how a signal becomes (or doesn't become) a trade."""
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    s = bg((W, H))
    kick(s, (m, 120), "Swipe · 5 steps", 26)
    y = head(s, (m, 200), "The AI interprets.", 104, W - 2 * m)
    y = head(s, (m, y), "Code decides.", 104, W - 2 * m, col=ORANGE)
    pulse(s, 0, W, y + 140, 120, width=8, beat_at=.55)
    para(s, (m, y + 280), "How a market headline becomes a trade — or gets stopped — inside AI MarketPulse.", 38, W - 2 * m, col=WHITE)
    mini_logo(s, m, H - 150, 56)
    out.append(s)

    steps = [
        ("01", "Ingest", "RSS, email, Telegram, Reddit, SEC EDGAR and more land in one review queue, scored.", "09-review-queue"),
        ("02", "Interpret", "LLMs turn raw text into a structured signal — and show why it fired.", "15-signal-why-panel"),
        ("03", "Debate", "TradeOS runs analysts, a bull/bear debate and guardrails into one verdict.", "20-annotated-tradeos-verdict"),
        ("04", "Gate", "17 deterministic pre-trade checks. Overrides can't bypass the risk core.", "26-annotated-risk-cockpit"),
        ("05", "Log", "Every decision carries a trace ID — trigger to verdict to order.", "21-tradeos-lineage"),
    ]
    for n, word, line, name in steps:
        s = bg((W, H), seed=int(n))
        kick(s, (m, 110), f"Step {n} / 05", 24, MUTED)
        y = head(s, (m, 160), word + ".", 120, W - 2 * m, col=ORANGE)
        para(s, (m, y + 20), line, 38, W - 2 * m, col=WHITE)
        br = desk(name, W - m, max_h=H - y - 260, crop=(200, 0, 1440, 900))
        glow_paste(s, br, (m // 2, y + 190))
        sk.draw_text(s, (W - m - 70, H - 80), f"{int(n) + 1} / 7", B.font(22), rgb(MUTED))
        para(s, (m, H - 80), "big-mo.ai", 22, 300)
        out.append(s)

    s = bg((W, H), seed=9)
    y = head(s, (m, 260), "Risk control", 120, W - 2 * m)
    y = head(s, (m, y), "is the product.", 120, W - 2 * m, col=ORANGE)
    para(s, (m, y + 40), "Kill switch. Paper → live graduation. A full audit trail. Start in the simulator — no keys, no real money.", 38, W - 2 * m, col=WHITE)
    btn(s, m, y + 300, "Try the simulator", 36)
    mini_logo(s, m, H - 190, 56)
    disclaimer(s, W, H, m, 22)
    out.append(s)

    for i, s in enumerate(out, 1):
        sk.save(s, OUT / "instagram/carousel-signal-to-trade" / f"slide-{i:02d}.png")
    return out


def ig_posts():
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    # 1 kill switch
    s = bg((W, H), 1)
    kick(s, (m, 110), "Risk Cockpit", 26)
    y = head2(s, (m, 170), "One button.", "Everything stops.", 104, W - 2 * m)
    para(s, (m, y + 20), "Server-enforced loss limits, drawdown caps and a kill switch you can actually reach.", 34, W - 2 * m, col=WHITE)
    ph = mob("75-risk-cockpit-mobile", 760)
    glow_paste(s, ph, ((W - ph.size[0]) // 2, y + 150))
    disclaimer(s, W, H, m)
    out.append(("post-01-kill-switch", s))

    # 2 17 gates
    s = bg((W, H), 2)
    sk.block(s, (m, 120), "17", B.font(360, "bold"), rgb(ORANGE), W, line_h=1, tracking_px=-18)
    y = head(s, (m, 520), "pre-trade checks.", 88, W - 2 * m)
    y = head(s, (m, y), "Zero exceptions.", 88, W - 2 * m, col=MUTED)
    gates = [("Daily loss budget", GREEN, "PASS"), ("Sector exposure", ORANGE, "WARN"), ("Account state", RED, "BLOCK"), ("Position size", GREEN, "PASS")]
    yy = y + 50
    for label, col, v in gates:
        ImageDraw.Draw(s).rounded_rectangle([m, yy, W - m, yy + 84], 10, fill=rgb("#141B2E"), outline=rgb("#26304A"), width=2)
        sk.draw_text(s, (m + 30, yy + 24), label, B.font(32), rgb(WHITE))
        cw = sk.text_width(B.font(24, "bold"), v) + 30
        chip(s, W - m - 30 - cw, yy + 20, v, col, 24)
        yy += 100
    disclaimer(s, W, H, m)
    out.append(("post-02-17-gates", s))

    # 3 paper first
    s = bg((W, H), 3)
    kick(s, (m, 110), "Paper → Live graduation", 26)
    y = head2(s, (m, 170), "Prove it on paper.", "Then earn live.", 96, W - 2 * m)
    para(s, (m, y + 20), "A published 5-criterion ladder per asset class — with automatic demotion back to paper if things regress.", 34, W - 2 * m, col=WHITE)
    br = desk("29-portfolio-summary", W - m, max_h=560)
    glow_paste(s, br, (m // 2, y + 190))
    para(s, (m, H - 140), "Simulated demo account shown.", 22, W - 2 * m, col=MUTED)
    disclaimer(s, W, H, m)
    out.append(("post-03-paper-first", s))

    # 4 trace id
    s = bg((W, H), 4)
    kick(s, (m, 110), "TradeOS", 26)
    y = head2(s, (m, 170), "Every trade", "has a receipt.", 104, W - 2 * m)
    para(s, (m, y + 20), "Trigger → research → bull/bear debate → signed guardrail report → verdict → order. One trace ID.", 34, W - 2 * m, col=WHITE)
    br = desk("19-tradeos-run-verdict", W - m, max_h=580)
    glow_paste(s, br, (m // 2, y + 190))
    disclaimer(s, W, H, m)
    out.append(("post-04-trace-id", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/posts" / f"{n}.png")


def ig_stories():
    W, H = sk.IG_STORY
    m = 90
    out = []

    s = bg((W, H), 11)
    pulse(s, 0, W, 300, 180, width=10)
    y = head(s, (m, 480), "AI that knows when", 104, W - 2 * m)
    y = head(s, (m, y), "not to trade.", 104, W - 2 * m, col=ORANGE)
    ph = mob("70-dashboard-mobile", 860)
    glow_paste(s, ph, ((W - ph.size[0]) // 2, y + 70))
    disclaimer(s, W, H, m, 24)
    out.append(("story-01-not-to-trade", s))

    s = bg((W, H), 12)
    kick(s, (m, 300), "Paper-only contests", 30)
    y = head2(s, (m, 360), "Compete.", "No real money at risk.", 120, W - 2 * m)
    ph = mob("73-competition-mobile", 980)
    glow_paste(s, ph, ((W - ph.size[0]) // 2, y + 80))
    disclaimer(s, W, H, m, 24)
    out.append(("story-02-competition", s))

    s = bg((W, H), 13)
    logo(s, m, 700, 130)
    pulse(s, 0, W, 1100, 160, width=10, beat_at=.5)
    para(s, (m, 1300), "The AI interprets. Deterministic code decides. The broker executes. Everything is logged.", 46, W - 2 * m, col=WHITE)
    btn(s, m, 1600, "big-mo.ai", 40)
    out.append(("story-03-manifesto", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/stories" / f"{n}.png")


def ig_reel():
    """15s 9:16 reel: four hard statements, then the end card."""
    W, H = sk.IG_STORY
    m = 90
    sc = []

    def card(a, b_, phone_name=None, seed=0, sz=140):
        s = bg((W, H), seed)
        y = 560 if phone_name else 760
        y = head(s, (m, y), a, sz, W - 2 * m)
        y = head(s, (m, y), b_, sz, W - 2 * m, col=ORANGE)
        if phone_name:
            ph = mob(phone_name, 900)
            glow_paste(s, ph, ((W - ph.size[0]) // 2, y + 60))
        return s

    s = bg((W, H), 1)
    pulse(s, 0, W, 900, 260, width=12)
    head(s, (m, 1180), "Headlines move fast.", 110, W - 2 * m)
    sc.append(sk.Scene(s, 2.2))
    sc.append(sk.Scene(card("AI reads", "every signal.", "70-dashboard-mobile", 2, 130), 2.8))
    sc.append(sk.Scene(card("17 checks", "decide.", "75-risk-cockpit-mobile", 3, 140), 2.8))
    sc.append(sk.Scene(card("Paper first.", "Always logged.", "74-portfolio-mobile", 4, 130), 2.8))
    s = bg((W, H), 5)
    logo(s, m, 760, 130)
    pulse(s, 0, W, 1150, 160, width=10, beat_at=.5)
    para(s, (m, 1320), "Risk control is the product.", 56, W - 2 * m, col=WHITE)
    para(s, (m, 1420), "big-mo.ai", 48, W - 2 * m, col=ORANGE)
    disclaimer(s, W, H, m, 26)
    sc.append(sk.Scene(s, 3.4, move="out", zoom=1.05))
    sk.render_video(sc, (W, H), OUT / "instagram/reel-risk-control-9x16.mp4")
    sk.save(sc[0].frame, OUT / "instagram/reel-cover.png")


# ======================================================================= LINKEDIN

def li_links():
    W, H = sk.LI_LINK
    m = 60
    items = [
        ("link-01-launch", "AI-assisted research.", "Deterministic risk.", "Signals from RSS, email, Telegram, Reddit and SEC EDGAR — interpreted by AI, gated by 17 code-enforced checks.", "03-dashboard-home"),
        ("link-02-tradeos", "Every trade", "has a trace ID.", "Multi-analyst research, bull/bear debate and an HMAC-signed guardrail report behind each verdict.", "20-annotated-tradeos-verdict"),
        ("link-03-risk", "Risk control", "is the product.", "Kill switch, loss budgets, drawdown caps and a paper → live graduation ladder.", "25-risk-cockpit"),
    ]
    for n, a, b_, line, name in items:
        s = bg((W, H), len(n))
        kick(s, (m, 60), "AI MarketPulse", 18)
        y = head(s, (m, 100), a, 54, 520)
        y = head(s, (m, y), b_, 54, 520, col=ORANGE)
        para(s, (m, y + 16), line, 22, 470, col=WHITE)
        mini_logo(s, m, H - 80, 36)
        br = desk(name, 600, max_h=470)
        glow_paste(s, br, (W - 600 - 30, 80))
        sk.save(s, OUT / "linkedin/images" / f"{n}.png")


def li_document():
    """8-page 1:1 document: 'Agentic trading, with brakes' — for fintech / ops / CTO audiences."""
    W, H = sk.LI_SQUARE
    m = 90
    pages = []

    def page(n, k, a, b_, text, name, max_h=560):
        s = bg((W, H), n)
        kick(s, (m, 80), k, 22)
        y = head(s, (m, 130), a, 72, W - 2 * m)
        if b_:
            y = head(s, (m, y), b_, 72, W - 2 * m, col=ORANGE)
        y = para(s, (m, y + 10), text, 30, W - 2 * m, col=WHITE)
        br = desk(name, W - 2 * m + 40, max_h=min(max_h, H - y - 180), crop=(200, 0, 1440, 900))
        glow_paste(s, br, (m - 20, y + 40))
        mini_logo(s, m, H - 90, 36)
        sk.draw_text(s, (W - m - 60, H - 80), f"{n} / 8", B.font(22), rgb(MUTED))
        pages.append(s)

    s = bg((W, H), 0)
    kick(s, (m, 120), "A field guide · 2026", 24)
    y = head(s, (m, 200), "Agentic trading,", 110, W - 2 * m)
    y = head(s, (m, y), "with brakes.", 110, W - 2 * m, col=ORANGE)
    pulse(s, 0, W, y + 140, 130, width=8)
    para(s, (m, y + 300), "How AI MarketPulse separates what AI is good at (reading) from what code must own (deciding).", 34, W - 2 * m, col=WHITE)
    logo(s, m, H - 220, 64)
    pages.append(s)
    page(2, "01 · Five planes", "Ingest. Understand.", "Gate. Execute. Observe.", "Each plane has one job, and the risk plane sits between AI and the broker.", "04-annotated-dashboard-layout")
    page(3, "02 · Ingestion", "Every source,", "one queue.", "RSS, Gmail, Outlook, IMAP, WhatsApp, Telegram, Reddit, SEC EDGAR — scored and de-duplicated.", "06-sources-feeds")
    page(4, "03 · Understanding", "Signals that", "explain themselves.", "Each AI signal shows the rule that triggered it, the citations and the confidence.", "15-signal-why-panel")
    page(5, "04 · TradeOS", "Research, debate,", "verdict.", "Analysts argue bull and bear; a signed guardrail report records which rules passed, warned or blocked.", "22-tradeos-guardrails")
    page(6, "05 · Policy", "17 gates.", "No bypass.", "Pure-arithmetic pre-trade checks in a <50 ms budget. Human overrides skip advisory checks — never the risk core.", "26-annotated-risk-cockpit")
    page(7, "06 · Compliance posture", "Features that", "aren't allowed aren't loaded.", "EDUCATIONAL and SELF_DIRECTED postures decide what is even mounted in the router.", "65-educational-posture-nav")
    s = bg((W, H), 8)
    y = head(s, (m, 300), "The AI interprets.", 84, W - 2 * m)
    y = head(s, (m, y), "Code decides.", 84, W - 2 * m, col=ORANGE)
    y = head(s, (m, y), "The broker executes.", 84, W - 2 * m)
    y = head(s, (m, y), "Everything is logged.", 84, W - 2 * m, col=ORANGE)
    btn(s, m, y + 60, "See it at big-mo.ai", 36)
    mini_logo(s, m, H - 160, 48)
    disclaimer(s, W, H, m, 22)
    pages.append(s)

    sk.pdf(pages, OUT / "linkedin/document-agentic-trading-with-brakes.pdf")
    for i, p in enumerate(pages, 1):
        sk.save(p, OUT / "linkedin/document-pages" / f"page-{i:02d}.png")


def li_video():
    W, H = sk.LI_VIDEO
    m = 120
    sc = []

    def title(a, b_, seed, beat=True):
        s = bg((W, H), seed)
        if beat:
            pulse(s, 0, W, 300, 150, width=8)
        y = head(s, (m, 480), a, 120, W - 2 * m)
        head(s, (m, y), b_, 120, W - 2 * m, col=ORANGE)
        return s

    def feat(k, a, line, name, seed):
        s = bg((W, H), seed)
        kick(s, (m, 260), k, 26)
        y = head(s, (m, 310), a, 84, 620)
        para(s, (m, y + 20), line, 34, 600, col=WHITE)
        mini_logo(s, m, H - 150, 44)
        br = desk(name, 1040)
        glow_paste(s, br, (W - 1040 - 80, (H - br.size[1]) // 2))
        return s

    sc.append(sk.Scene(title("Markets talk", "all day.", 1), 2.8))
    sc.append(sk.Scene(title("Most of it", "is noise.", 2, beat=False), 2.6))
    sc.append(sk.Scene(feat("01 · Ingest", "One queue for every source.", "RSS, email, chat apps, Reddit, SEC filings — scored.", "09-review-queue", 3), 4))
    sc.append(sk.Scene(feat("02 · Interpret", "Signals that show their work.", "Why it fired, with citations.", "14-signals", 4), 4))
    sc.append(sk.Scene(feat("03 · TradeOS", "A verdict with a receipt.", "Bull/bear debate + signed guardrails.", "19-tradeos-run-verdict", 5), 4))
    sc.append(sk.Scene(feat("04 · Gate", "17 checks. No bypass.", "Kill switch, loss budgets, paper → live.", "25-risk-cockpit", 6), 4))
    s = bg((W, H), 7)
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 120, kicker=False)
    logo(s, (W - lw) / 2, 330, 120)
    pulse(s, 0, W, 620, 140, width=8, beat_at=.5)
    sk.block(s, (m, 740), "The AI interprets. Code decides. Everything is logged.", B.font(48), rgb(WHITE), W - 2 * m, align="center")
    sk.block(s, (m, 830), "big-mo.ai", B.font(48, "bold"), rgb(ORANGE), W - 2 * m, align="center")
    sk.block(s, (m, H - 110), DISCLAIMER, B.font(26), rgb("#6B748A"), W - 2 * m, align="center")
    sc.append(sk.Scene(s, 4, move="out", zoom=1.04))
    sk.render_video(sc, (W, H), OUT / "linkedin/video-product-film-16x9.mp4")
    sk.save(sc[2].frame, OUT / "linkedin/video-cover.png")


if __name__ == "__main__":
    ig_carousel()
    ig_posts()
    ig_stories()
    li_links()
    li_document()
    if not args.no_video:
        ig_reel()
        li_video()
    print("done →", OUT)
