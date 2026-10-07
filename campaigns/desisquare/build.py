"""DesiSquare — "Ask the desi who's been there." social campaign (Instagram + LinkedIn).

Brand: Porcelain Slate, the product's client-locked theme (v4/public/styles.css):
paper #F5F6F8, surface #FFF, ink #16181D, peacock #0C637C, good #2D784C. Logo is
the peacock diamond + "DesiSquare". Sans-serif (Inter here; the app uses system UI).

Product rules carried into marketing (desisquarev5-product/CLAUDE.md):
- educational only, never investment advice — disclaimer on every asset;
- "Guru" is the member-facing word (never "maven");
- recognition ranks helpfulness, never money: no leaderboards / return brag copy;
- pseudonymous and percent-only; WhatsApp is consent-gated.

Run:  python3 campaigns/desisquare/build.py [--src ../desisquarev5-product] [--no-video]
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import socialkit as sk  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--src", default=str(HERE.parents[2] / "desisquarev5-product"))
ap.add_argument("--no-video", action="store_true")
args = ap.parse_args()
SRC = Path(args.src)
OUT = HERE / "output"
KIT = SRC / "docs/training-kit/screenshots"

INTER = "/usr/share/fonts/opentype/inter/"
B = sk.Brand(
    name="DesiSquare", bg="#F5F6F8", surface="#FFFFFF", ink="#16181D", muted="#4A4F58",
    primary="#0C637C", accent="#0C637C", font_regular=INTER + "Inter-Regular.otf",
    font_bold=INTER + "InterDisplay-Bold.otf", font_italic=INTER + "InterDisplay-SemiBold.otf",
    url="desisquare", handle="@desisquare", tracking=-0.03,
)
PAPER, WHITE, INK, BODY, DIM = "#F5F6F8", "#FFFFFF", "#16181D", "#4A4F58", "#575C65"
PEACOCK, PEACOCK_D, TINT, HAIR, GOOD = "#0C637C", "#094F63", "#E3F0F4", "#E3E6EB", "#2D784C"
SAFFRON = "#E8A33D"  # campaign-only warm accent (print/social), used sparingly for the diamond glint
DISCLAIMER = "Educational community · Not investment advice"


def rgb(h, a=255):
    return sk.hex2rgb(h, a)


# ------------------------------------------------------------- brand pieces

def bg(size, dark=False, tint=False):
    W, H = size
    if dark:
        g = sk.canvas(size, PEACOCK_D)
        lay = Image.new("RGBA", size, (0, 0, 0, 0))
        ImageDraw.Draw(lay).polygon(diamond_pts(W * .92, H * .12, W * .5), fill=rgb(PEACOCK, 255))
        g.alpha_composite(lay)
        return g
    g = sk.canvas(size, TINT if tint else PAPER)
    lay = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(lay).polygon(diamond_pts(W * 1.0, H * .02, W * .42), fill=rgb(PEACOCK, 14 if not tint else 22))
    g.alpha_composite(lay)
    return g


def diamond_pts(cx, cy, r):
    return [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]


def diamond(img, cx, cy, r, col=PEACOCK):
    d = ImageDraw.Draw(img)
    d.polygon(diamond_pts(cx, cy, r), fill=rgb(col))
    # small light facet, like a cut stone
    d.polygon([(cx, cy - r), (cx + r * .45, cy - r * .55), (cx, cy - r * .1)], fill=rgb("#FFFFFF", 70))


def logo(img, x, y, h, dark=False):
    diamond(img, x + h * .42, y + h * .55, h * .42, WHITE if dark else PEACOCK)
    f = B.font(int(h * .9), "bold")
    return h * 1.05 + sk.draw_text(img, (x + h * 1.05, y), "DesiSquare", f, rgb(WHITE if dark else INK), tracking_px=-h * .03)


def kick(img, xy, s, size, col=PEACOCK):
    sk.draw_text(img, xy, s.upper(), B.font(size, "bold"), rgb(col), tracking_px=size * .16)


def head(img, xy, s, size, max_w, col=INK, lh=1.06, align="left"):
    return sk.block(img, xy, s, B.font(size, "bold"), rgb(col), max_w, line_h=lh, tracking_px=size * B.tracking, align=align)


def head2(img, xy, a, b_, size, max_w, dark=False):
    y = head(img, xy, a, size, max_w, col=WHITE if dark else INK)
    return head(img, (xy[0], y), b_, size, max_w, col="#9ED3E2" if dark else PEACOCK)


def para(img, xy, s, size, max_w, col=BODY, lh=1.42, align="left"):
    return sk.block(img, xy, s, B.font(size), rgb(col), max_w, line_h=lh, align=align)


def btn(img, x, y, s, size=30, dark=False):
    return sk.pill(img, (x, y), s, B.font(size, "bold"), PEACOCK if dark else WHITE, WHITE if dark else PEACOCK,
                   pad=(int(size * .95), int(size * .55)), radius=int(size * 1.2))


def chip(img, x, y, s, size=24, col=PEACOCK, fill=TINT):
    return sk.pill(img, (x, y), s, B.font(size, "bold"), col, fill, pad=(int(size * .7), int(size * .35)), radius=int(size))


def foot(img, W, H, m, size=20, dark=False, page=None):
    para(img, (m, H - m * .85), DISCLAIMER, size, W - 2 * m, col="#B9D6DE" if dark else DIM)
    if page:
        f = B.font(size)
        sk.draw_text(img, (W - m - sk.text_width(f, page), H - m * .85), page, f, rgb("#B9D6DE" if dark else DIM))


def shot(name, crop=None):
    im = Image.open(KIT / f"{name}.webp").convert("RGB")
    return im.crop(crop) if crop else im


NAV = (232, 0, 1440, 900)  # drop the left nav to zoom into the content
TOOLS = (180, 0, 1260, 760)  # tools directory has wide gutters


def desk(name, width, max_h=None, crop=NAV):
    br = sk.browser(shot(name, crop), width, chrome="#E6E9EE", url="desisquare", ink=DIM, radius=12)
    return sk.cap(br, max_h) if max_h else br


def mob(name, h):
    im = shot(name)
    return sk.phone(im.crop((0, 0, im.size[0], min(im.size[1], 844))), h, bezel="#1F2329")


def lift(base, im, xy):
    sk.shadow_paste(base, im, xy, blur=34, offset=(0, 22), opacity=55)


def quote_card(img, x, y, w, q, who, tag):
    """A member-voice card. Text is a QUESTION from the demo seed, not a testimonial."""
    f, fs = B.font(34, "bold"), B.font(24)
    lines = sk.wrap(f, q, w - 80)
    h = 70 + len(lines) * 44 + 70
    card = Image.new("RGBA", (w, h), rgb(WHITE))
    ImageDraw.Draw(card).rounded_rectangle([0, 0, w - 1, h - 1], 14, outline=rgb(HAIR), width=2)
    yy = 40
    for ln in lines:
        sk.draw_text(card, (40, yy), ln, f, rgb(INK))
        yy += 44
    sk.draw_text(card, (40, yy + 18), who, fs, rgb(DIM))
    tw = sk.text_width(B.font(20, "bold"), tag) + 30
    chip(card, w - 40 - tw, yy + 12, tag, 20)
    lift(img, sk.rounded(card, 14), (x, y))
    return y + h


# ======================================================================= INSTAGRAM

def ig_carousel():
    """7-slide 4:5 carousel: 'Money questions, desi answers.'"""
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    s = bg((W, H))
    logo(s, m, 110, 54)
    y = head2(s, (m, 300), "Money questions.", "Desi answers.", 112, W - 2 * m)
    para(s, (m, y + 30), "FCNR or T-bills? H-1B taxes? RSUs from two countries? Ask the people who've already done it.", 38, W - 2 * m)
    yy, x = y + 240, m
    for i, q in enumerate(["NRE vs NRO?", "FBAR due?", "529 or India?", "RSU vest?"]):
        w, h = chip(s, x, yy, q, 30)
        x += w + 18
        if i == 1:
            x, yy = m, yy + h + 18
    kick(s, (m, H - 140), "Swipe · 5 reasons", 24)
    out.append(s)

    slides = [
        ("01", "Real questions.", "Real threads.", "Members ask in plain words and get answers from people living the same cross-border life.", "11-post-thread"),
        ("02", "Helpfulness", "earns standing.", "Members are ranked by how useful their answers are — never by how much money they have.", "15-discover-people"),
        ("03", "Gurus show", "their credentials.", "Credential-verified gurus. Performance is percent-only, opt-in, and shared as education.", "22-guru-stats"),
        ("04", "Pseudonymous.", "Percent-only.", "No real names required. Public portfolios show weights in percent — dollars stay with their owner.", "25-guru-portfolio"),
        ("05", "Free tools,", "no sign-in.", "100+ calculators for NRI money decisions — FBAR, residency, the 60-day clock — computed in your browser.", "44-tools-directory"),
    ]
    for n, a, b_, line, name in slides:
        s = bg((W, H))
        kick(s, (m, 100), f"{n} / 05", 24, DIM)
        y = head2(s, (m, 150), a, b_, 92, W - 2 * m)
        y = para(s, (m, y + 16), line, 34, W - 2 * m)
        crop = TOOLS if name == "44-tools-directory" else NAV
        br = desk(name, W - m, max_h=H - y - 210, crop=crop)
        lift(s, br, (m // 2, y + 50))
        foot(s, W, H, m, page=f"{int(n) + 1} / 7")
        out.append(s)

    s = bg((W, H), dark=True)
    logo(s, m, 110, 54, dark=True)
    y = head2(s, (m, 320), "Where desi money", "questions get trusted answers.", 92, W - 2 * m, dark=True)
    para(s, (m, y + 30), "Join the community. Ask your first question. Read before you decide.", 38, W - 2 * m, col="#DCEBF0")
    btn(s, m, y + 200, "Join free", 38, dark=True)
    foot(s, W, H, m, 22, dark=True)
    out.append(s)

    for i, s in enumerate(out, 1):
        sk.save(s, OUT / "instagram/carousel-desi-answers" / f"slide-{i:02d}.png")


def ig_posts():
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    # 1 the question wall — questions as seen in the demo community
    s = bg((W, H), tint=True)
    kick(s, (m, 110), "Asked this week", 26)
    y = head(s, (m, 160), "You're not the only one asking.", 84, W - 2 * m)
    y += 40
    qs = [("FCNR deposits at 5.1% — am I missing a catch vs T-bills?", "Taxes & FEMA", "41 replies"),
          ("How much emergency fund when both incomes are visa-linked?", "Insurance & Visas", "Popular"),
          ("Mid-year tax moves for H-1B households", "Taxes & FEMA", "Community Pick")]
    for q, who, tag in qs:
        y = quote_card(s, m, y, W - 2 * m, q, who, tag) + 30
    para(s, (m, H - 170), "Example threads from the DesiSquare demo community.", 22, W - 2 * m, col=DIM)
    foot(s, W, H, m)
    out.append(("post-01-you-are-not-alone", s))

    # 2 never by money
    s = bg((W, H))
    y = head(s, (m, 170), "Ranked by", 120, W - 2 * m)
    y = head(s, (m, y), "helpfulness.", 120, W - 2 * m, col=PEACOCK)
    y = head(s, (m, y + 10), "Never by money.", 120, W - 2 * m, col="#A3AAB5")
    para(s, (m, y + 30), "Karma comes from Helpful, Insightful and Actionable reactions to your answers. Your net worth doesn't enter it.", 34, W - 2 * m)
    yy = y + 250
    x = m
    for t in ["👍 Helpful", "💡 Insightful", "📈 Actionable", "❤️ Like"]:
        w, _ = chip(s, x, yy, t.split(" ", 1)[1], 30, col=INK, fill=WHITE)
        x += w + 16
    foot(s, W, H, m)
    out.append(("post-02-never-by-money", s))

    # 3 privacy
    s = bg((W, H), dark=True)
    kick(s, (m, 110), "Privacy by design", 26, "#9ED3E2")
    y = head2(s, (m, 170), "Your name? Optional.", "Your dollars? Private.", 92, W - 2 * m, dark=True)
    para(s, (m, y + 20), "Pseudonymous accounts. Allocation shown in percent only. Flags are private. WhatsApp only with your consent.", 34, W - 2 * m, col="#DCEBF0")
    ph = mob("69-guru-page-mobile", 700)
    lift(s, ph, ((W - ph.size[0]) // 2, y + 170))
    foot(s, W, H, m, dark=True)
    out.append(("post-03-privacy", s))

    # 4 tools
    s = bg((W, H))
    kick(s, (m, 110), "Free · no account", 26)
    y = head2(s, (m, 160), "The three that", "matter this year.", 100, W - 2 * m)
    para(s, (m, y + 20), "Ten questions, none asking for an amount. It puts your NRI money deadlines in the order they actually close.", 34, W - 2 * m)
    br = desk("46-tools-readiness-results", W - m, max_h=560, crop=(0, 0, 1440, 900))
    lift(s, br, (m // 2, y + 190))
    foot(s, W, H, m)
    out.append(("post-04-free-tools", s))

    # 5 corridors
    s = bg((W, H), tint=True)
    y = head(s, (m, 200), "One square.", 120, W - 2 * m)
    y = head(s, (m, y), "Six corridors.", 120, W - 2 * m, col=PEACOCK)
    para(s, (m, y + 30), "Desis in the US, Canada, UK, UAE, Australia and Singapore — each with their own communities, rules and questions.", 36, W - 2 * m)
    yy, x = y + 260, m
    for i, c in enumerate(["🇺🇸 US", "🇨🇦 Canada", "🇬🇧 UK", "🇦🇪 UAE", "🇦🇺 Australia", "🇸🇬 Singapore"]):
        name = c.split(" ", 1)[1]
        w, h = chip(s, x, yy, name, 34, col=WHITE, fill=PEACOCK)
        x += w + 18
        if i == 2:
            x, yy = m, yy + h + 20
    foot(s, W, H, m)
    out.append(("post-05-six-corridors", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/posts" / f"{n}.png")


def ig_stories():
    W, H = sk.IG_STORY
    m = 90
    out = []

    s = bg((W, H))
    logo(s, m, 200, 64)
    y = head2(s, (m, 420), "Got a money question", "you can't ask at home?", 104, W - 2 * m)
    ph = mob("66-home-mobile", 880)
    lift(s, ph, ((W - ph.size[0]) // 2, y + 70))
    foot(s, W, H, m, 26)
    out.append(("story-01-ask", s))

    s = bg((W, H), tint=True)
    kick(s, (m, 300), "This or that?", 32)
    y = head(s, (m, 370), "FCNR at 5.1%", 120, W - 2 * m)
    y = head(s, (m, y), "or US T-bills?", 120, W - 2 * m, col=PEACOCK)
    para(s, (m, y + 40), "Members are debating it right now. Read the thread — then decide for yourself.", 44, W - 2 * m)
    ph = mob("68-post-thread-mobile", 860)
    lift(s, ph, ((W - ph.size[0]) // 2, y + 280))
    foot(s, W, H, m, 26)
    out.append(("story-02-poll", s))

    s = bg((W, H), dark=True)
    diamond(s, W // 2, 720, 210, WHITE)
    head(s, (m, 1020), "Read before you decide.", 104, W - 2 * m, col=WHITE, align="center")
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 80, dark=True)
    logo(s, (W - lw) / 2, 1320, 80, dark=True)
    foot(s, W, H, m, 26, dark=True)
    out.append(("story-03-brand", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/stories" / f"{n}.png")


def ig_reel():
    W, H = sk.IG_STORY
    m = 90
    sc = []

    def card(a, b_, phone=None, tint=False, size=124):
        s = bg((W, H), tint=tint)
        y = head2(s, (m, 380 if phone else 760), a, b_, size, W - 2 * m)
        if phone:
            ph = mob(phone, 900)
            lift(s, ph, ((W - ph.size[0]) // 2, y + 70))
        foot(s, W, H, m, 26)
        return s

    s = bg((W, H), dark=True)
    y = head(s, (m, 640), "NRE or NRO?", 130, W - 2 * m, col=WHITE)
    y = head(s, (m, y), "FBAR due?", 130, W - 2 * m, col="#9ED3E2")
    head(s, (m, y), "RSUs in two countries?", 110, W - 2 * m, col=WHITE)
    sc.append(sk.Scene(s, 2.6))
    sc.append(sk.Scene(card("Ask the desi", "who's been there.", "68-post-thread-mobile"), 3.0))
    sc.append(sk.Scene(card("Ranked by help,", "never by money.", "70-discover-mobile", tint=True, size=112), 3.0))
    sc.append(sk.Scene(card("Free tools.", "No sign-in.", "71-tools-readiness-mobile"), 3.0))
    s = bg((W, H), dark=True)
    diamond(s, W // 2, 640, 170, WHITE)
    head(s, (m, 900), "Where desi money questions get trusted answers.", 84, W - 2 * m, col=WHITE, align="center")
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 80, dark=True)
    logo(s, (W - lw) / 2, 1280, 80, dark=True)
    foot(s, W, H, m, 26, dark=True)
    sc.append(sk.Scene(s, 3.4, move="out", zoom=1.05))
    sk.render_video(sc, (W, H), OUT / "instagram/reel-ask-the-desi-9x16.mp4")
    sk.save(sc[1].frame, OUT / "instagram/reel-cover.png")


# ======================================================================= LINKEDIN

def li_links():
    W, H = sk.LI_LINK
    m = 60
    items = [
        ("link-01-launch", "Money questions.", "Desi answers.", "A pseudonymous, percent-only community for desi investors across six corridors.", "09-home-annotated", NAV),
        ("link-02-trust", "Trust is earned", "in answers.", "Members are ranked by helpfulness. Gurus are credential-verified. Money never ranks anyone.", "15-discover-people", NAV),
        ("link-03-tools", "100+ free tools.", "No sign-in.", "FBAR, residency, the NRO alarm, the 60-day clock — computed in the browser, every rule sourced.", "44-tools-directory", TOOLS),
    ]
    for n, a, b_, line, name, crop in items:
        s = bg((W, H))
        logo(s, m, 50, 30)
        y = head2(s, (m, 120), a, b_, 52, 520)
        para(s, (m, y + 16), line, 22, 470)
        para(s, (m, H - 70), DISCLAIMER, 16, 500, col=DIM)
        br = desk(name, 600, max_h=480, crop=crop)
        lift(s, br, (W - 600 - 30, 70))
        sk.save(s, OUT / "linkedin/images" / f"{n}.png")


def li_document():
    """8-page 1:1 document: 'Building a money community people can trust' — product/community/fintech audience."""
    W, H = sk.LI_SQUARE
    m = 90
    pages = []

    def page(n, k, a, b_, text, name, crop=NAV):
        s = bg((W, H))
        kick(s, (m, 80), k, 22)
        y = head2(s, (m, 130), a, b_, 68, W - 2 * m)
        y = para(s, (m, y + 10), text, 30, W - 2 * m)
        br = desk(name, W - 2 * m + 40, max_h=H - y - 190, crop=crop)
        lift(s, br, (m - 20, y + 40))
        logo(s, m, H - 92, 30)
        f = B.font(22)
        sk.draw_text(s, (W - m - 50, H - 86), f"{n} / 8", f, rgb(DIM))
        pages.append(s)

    s = bg((W, H))
    logo(s, m, 110, 50)
    y = head2(s, (m, 300), "Six rules for a money", "community people can trust.", 92, W - 2 * m)
    para(s, (m, y + 40), "What we built into DesiSquare so that desi investors can ask honest questions — and get honest answers.", 34, W - 2 * m)
    foot(s, W, H, m, 22)
    pages.append(s)
    page(2, "Rule 1", "Rank people by help,", "never by money.", "Karma comes from reactions to answers. Portfolio data never enters a leaderboard or badge.", "15-discover-people")
    page(3, "Rule 2", "Flags stay", "private.", "Four reasons, one moderator queue. No public flag counts to pile on.", "13-flag-picker")
    page(4, "Rule 3", "Percent,", "not dollars.", "Public pages show allocation in percent. Dollars are visible only to their owner.", "25-guru-portfolio")
    page(5, "Rule 4", "Verify credentials,", "not identities.", "Gurus are credential-checked; members stay pseudonymous. Track records are opt-in.", "22-guru-stats")
    page(6, "Rule 5", "Consent before", "WhatsApp.", "Mirroring and notifications are opt-in. Phone numbers never appear anywhere.", "36-settings-privacy")
    page(7, "Rule 6", "Give away", "the tools.", "100+ public calculators with sourced rules and a date on every figure.", "46-tools-readiness-results", (0, 0, 1440, 900))
    s = bg((W, H), dark=True)
    logo(s, m, 110, 50, dark=True)
    y = head2(s, (m, 320), "Educational,", "never advice.", 110, W - 2 * m, dark=True)
    para(s, (m, y + 40), "Where desi money questions get trusted answers — pseudonymous, percent-only, educational.", 36, W - 2 * m, col="#DCEBF0")
    btn(s, m, y + 220, "Join the community", 36, dark=True)
    foot(s, W, H, m, 22, dark=True)
    pages.append(s)

    sk.pdf(pages, OUT / "linkedin/document-six-rules-for-trust.pdf")
    for i, p in enumerate(pages, 1):
        sk.save(p, OUT / "linkedin/document-pages" / f"page-{i:02d}.png")


def li_video():
    W, H = sk.LI_VIDEO
    m = 120
    sc = []

    def title(a, b_, dark=False):
        s = bg((W, H), dark=dark)
        head2(s, (m, 380), a, b_, 120, W - 2 * m, dark=dark)
        return s

    def feat(k, a, line, name, crop=NAV, tint=False):
        s = bg((W, H), tint=tint)
        kick(s, (m, 280), k, 26)
        y = head(s, (m, 330), a, 80, 620)
        para(s, (m, y + 20), line, 34, 600)
        logo(s, m, H - 150, 44)
        br = desk(name, 1040, max_h=880, crop=crop)
        lift(s, br, (W - 1040 - 80, (H - br.size[1]) // 2))
        return s

    sc.append(sk.Scene(title("Money advice is", "everywhere.", dark=True), 2.8))
    sc.append(sk.Scene(title("Trusted answers", "are not."), 2.6))
    sc.append(sk.Scene(feat("Ask", "Real questions, real threads.", "FCNR, FBAR, H-1B taxes, RSUs across borders.", "11-post-thread"), 4))
    sc.append(sk.Scene(feat("Trust", "Ranked by help. Never by money.", "Karma comes from answers, not net worth.", "15-discover-people", tint=True), 4))
    sc.append(sk.Scene(feat("Learn", "Gurus with verified credentials.", "Percent-only, opt-in, educational.", "22-guru-stats"), 4))
    sc.append(sk.Scene(feat("Decide", "100+ free tools. No sign-in.", "Sourced rules, dated figures.", "44-tools-directory", TOOLS, tint=True), 4))
    s = bg((W, H), dark=True)
    diamond(s, W // 2, 330, 120, WHITE)
    sk.block(s, (m, 510), "Where desi money questions get trusted answers.", B.font(72, "bold"), rgb(WHITE), W - 2 * m, align="center")
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 64, dark=True)
    logo(s, (W - lw) / 2, 700, 64, dark=True)
    sk.block(s, (m, H - 110), DISCLAIMER, B.font(28), rgb("#B9D6DE"), W - 2 * m, align="center")
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
