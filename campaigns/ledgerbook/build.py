"""Ledger Book — "AI proposes. The ledger disposes." campaign (Instagram + LinkedIn).

Brand from the product (src/styles.css): paper #F4F5F2, panel #FDFDFC, ink #1D232C,
accent blue #2B52C4, ok #1A7146, warn #8A5D09, crit #B3403A; Inter; "L" tile logo.

Screens: the repo ships none, so assets/screens/*.jpg were captured from a local demo
build (no DATABASE_URL → seeded demo ledger, persona "Jordan Blake"), with the
"development environment" banner cropped off. Re-capture with capture.sh.

Claims discipline:
  * AI never posts — it proposes; a person approves; the posting service enforces
    balance. Copilot can read and suggest, never post/send/move money (its own copy).
  * Tax set-aside is "a rule of thumb, not a tax calculation" (the product says so) —
    never call it tax advice or tax-ready.
  * No competitor named, no "replaces your accountant", no time-saved or accuracy figures.
  * All amounts in screenshots are demo data.

Run:  python3 campaigns/ledgerbook/build.py [--no-video]
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import socialkit as sk  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--no-video", action="store_true")
args = ap.parse_args()
OUT = HERE / "output"
SC = HERE / "assets/screens"

INTER = "/usr/share/fonts/opentype/inter/"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
B = sk.Brand(
    name="Ledger Book", bg="#F4F5F2", surface="#FDFDFC", ink="#1D232C", muted="#5D6570",
    primary="#2B52C4", accent="#2B52C4", font_regular=INTER + "Inter-Regular.otf",
    font_bold=INTER + "InterDisplay-Bold.otf", font_italic=INTER + "InterDisplay-SemiBold.otf",
    tracking=-0.03,
)
PAPER, PANEL, INK, SOFT, LINE = "#F4F5F2", "#FDFDFC", "#1D232C", "#5D6570", "#D4D8DC"
BLUE, BLUE_SOFT, OK, OK_SOFT, WARN, CRIT = "#2B52C4", "#E3E9F9", "#1A7146", "#E0F0E7", "#8A5D09", "#B3403A"
NIGHT, NIGHT_INK, NIGHT_BLUE = "#15181D", "#E7E9EC", "#8BA3EF"
FOOT = "Ledger Book by BigMo · the AI bookkeeper"


def rgb(h, a=255):
    return sk.hex2rgb(h, a)


def inter(size, w="Regular"):
    return ImageFont.truetype(INTER + f"Inter-{w}.otf", size)


def mono(size):
    return ImageFont.truetype(MONO, size)


# ------------------------------------------------------------- brand pieces

def bg(size, dark=False):
    """Paper with faint ledger ruling + a margin rule — the book in 'Ledger Book'."""
    W, H = size
    g = sk.canvas(size, NIGHT if dark else PAPER)
    d = ImageDraw.Draw(g)
    step = max(30, W // 28)
    col = rgb("#232830") if dark else rgb("#E6E9E4")
    for y in range(step, H, step):
        d.line([(0, y), (W, y)], fill=col, width=1)
    mx = int(W * .035)
    d.line([(mx, 0), (mx, H)], fill=rgb(NIGHT_BLUE if dark else BLUE, 60), width=max(1, W // 600))
    return g


def logo(img, x, y, h, dark=False):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([x, y, x + h, y + h], int(h * .22), fill=rgb(NIGHT_BLUE if dark else BLUE))
    f = inter(int(h * .6), "Bold")
    d.text((x + (h - f.getlength("L")) / 2, y + h * .14), "L", font=f, fill=rgb(NIGHT if dark else "#FFFFFF"))
    return h * 1.3 + sk.draw_text(img, (x + h * 1.3, y + h * .1), "Ledger Book", inter(int(h * .66), "Bold"),
                                  rgb(NIGHT_INK if dark else INK), tracking_px=-h * .02)


def kick(img, xy, s, size, col=BLUE):
    sk.draw_text(img, xy, s.upper(), inter(size, "SemiBold"), rgb(col), tracking_px=size * .14)


def head(img, xy, s, size, max_w, col=INK, lh=1.04, align="left"):
    return sk.block(img, xy, s, B.font(size, "bold"), rgb(col), max_w, line_h=lh, tracking_px=size * B.tracking, align=align)


def head2(img, xy, a, b_, size, max_w, dark=False, align="left"):
    y = head(img, xy, a, size, max_w, col=NIGHT_INK if dark else INK, align=align)
    return head(img, (xy[0], y), b_, size, max_w, col=NIGHT_BLUE if dark else BLUE, align=align)


def para(img, xy, s, size, max_w, col=SOFT, lh=1.42, align="left"):
    return sk.block(img, xy, s, inter(size), rgb(col), max_w, line_h=lh, align=align)


def btn(img, x, y, s, size=30, dark=False):
    return sk.pill(img, (x, y), s, inter(size, "SemiBold"), NIGHT if dark else "#FFFFFF", NIGHT_BLUE if dark else BLUE,
                   pad=(int(size * .9), int(size * .55)), radius=int(size * .3))


def tag(img, x, y, s, fg, bgc, size=22):
    return sk.pill(img, (x, y), s, inter(size, "SemiBold"), fg, bgc, pad=(int(size * .6), int(size * .3)), radius=int(size))


def foot(img, W, H, m, size=20, dark=False, page=None):
    c = "#8C949E" if dark else "#7A818A"
    para(img, (m, H - m * .9), FOOT, size, W - 2 * m, col=c)
    if page:
        sk.draw_text(img, (W - m - inter(size).getlength(page), H - m * .9), page, inter(size), rgb(c))


def lift(base, im, xy, op=55):
    sk.shadow_paste(base, im, xy, blur=30, offset=(0, 20), opacity=op)


def screen(name, width, max_h=None, frame=True, dark=False):
    im = Image.open(SC / f"{name}.jpg").convert("RGB")
    if frame:
        out = sk.browser(im, width, chrome="#2A2F37" if dark else "#E4E7EA", url="ledger book", ink=SOFT, radius=12)
    else:
        s = width / im.size[0]
        out = sk.rounded(im.resize((width, int(im.size[1] * s)), Image.LANCZOS), 12)
    return sk.cap(out, max_h) if max_h else out


def phone(name, h):
    return sk.phone(Image.open(SC / f"{name}.jpg").convert("RGB"), h, bezel="#1D232C")


def journal_entry(w, scale=1.0, dark=False):
    """A designed balanced journal entry — the double-entry promise, made visible."""
    s = scale
    h = int(400 * s)
    c = Image.new("RGBA", (w, h), rgb("#1D2127" if dark else PANEL))
    d = ImageDraw.Draw(c)
    ink, soft = rgb(NIGHT_INK if dark else INK), rgb("#A3AAB4" if dark else SOFT)
    d.text((36 * s, 30 * s), "JOURNAL ENTRY · Aug 13", font=inter(int(22 * s), "SemiBold"), fill=soft)
    d.text((36 * s, 70 * s), "Workshop facilitation fee", font=inter(int(32 * s), "SemiBold"), fill=ink)
    rows = [("Dr", "1000 Checking", "2,150.00", ""), ("Cr", "4100 Consulting fees", "", "2,150.00")]
    f = mono(int(26 * s))
    y = 140 * s
    d.text((36 * s, y), "", font=f)
    for side, acct, dr, cr in rows:
        d.text((36 * s, y), side, font=f, fill=rgb(NIGHT_BLUE if dark else BLUE))
        d.text((100 * s, y), acct, font=f, fill=ink)
        d.text((w - 330 * s - f.getlength(dr), y), dr, font=f, fill=ink)
        d.text((w - 40 * s - f.getlength(cr), y), cr, font=f, fill=ink)
        y += 52 * s
    d.line([(36 * s, y + 6 * s), (w - 36 * s, y + 6 * s)], fill=rgb(LINE if not dark else "#363C46"), width=2)
    y += 24 * s
    d.text((100 * s, y), "Debits = Credits", font=f, fill=soft)
    for x_end, v in [(w - 330 * s, "2,150.00"), (w - 40 * s, "2,150.00")]:
        d.text((x_end - f.getlength(v), y), v, font=f, fill=ink)
    tag(c, int(36 * s), int(y + 64 * s), "posted · immutable", OK if not dark else "#5CC492", OK_SOFT if not dark else "#1D3529", int(20 * s))
    return sk.rounded(c, int(14 * s))


def confidence_legend(w, scale=1.0):
    """How the review queue routes a suggestion — figures from the product's Today/Review screens."""
    s = scale
    rows = [(OK, "0.95 and above", "posts on its own — still balanced, still reversible"),
            (WARN, "below 0.95", "waits in Review for your Approve or Not mine"),
            (CRIT, "conflicting evidence", "says why, and asks a human")]
    h = int((90 + len(rows) * 96) * s)
    c = Image.new("RGBA", (w, h), rgb(PANEL))
    d = ImageDraw.Draw(c)
    d.text((32 * s, 28 * s), "HOW A SUGGESTION IS ROUTED", font=inter(int(20 * s), "SemiBold"), fill=rgb(SOFT))
    for i, (col, a, b_) in enumerate(rows):
        y = (80 + i * 96) * s
        d.rounded_rectangle([32 * s, y + 12 * s, 112 * s, y + 24 * s], 6 * s, fill=rgb(col))
        d.text((140 * s, y), a, font=inter(int(28 * s), "SemiBold"), fill=rgb(INK))
        d.text((140 * s, y + 40 * s), b_, font=inter(int(24 * s)), fill=rgb(SOFT))
    return sk.rounded(c, int(14 * s))


# ======================================================================= INSTAGRAM

def ig_carousel():
    W, H = sk.IG_PORTRAIT
    m = 90
    out = []

    s = bg((W, H))
    logo(s, m, 90, 56)
    y = head2(s, (m, 300), "AI proposes.", "You approve.", 128, W - 2 * m)
    y = head(s, (m, y), "The ledger posts.", 128, W - 2 * m, col=SOFT)
    para(s, (m, y + 30), "Bookkeeping for freelancers and small businesses, where nothing reaches your books without a reason and a yes.", 36, W - 2 * m)
    kick(s, (m, H - 150), "Swipe · how it works", 22)
    out.append(s)

    steps = [
        ("01", "It reads the bank.", "Each transaction gets a suggested category, a confidence score and a plain-English reason.", "review-queue", None),
        ("02", "Not sure? It asks you.", "Low confidence means a person decides — here, the amount points one way and the payer's name the other.", "review-needs-human", None),
        ("03", "Only balanced entries post.", "Debits equal credits, every time. Posted entries can't be edited — mistakes are reversed, on the record.", None, "journal"),
        ("04", "Every number is live.", "Cash, profit, what you're owed and the 13-week runway are computed from the journal — never stored.", "today-top", None),
        ("05", "Ask it anything.", "The copilot can read your books and suggest. It has no tool that can post, send or move money.", "copilot", None),
    ]
    for n, t, line, name, special in steps:
        s = bg((W, H))
        kick(s, (m, 100), f"{n} / 05", 22, SOFT)
        y = head(s, (m, 150), t, 90, W - 2 * m)
        y = para(s, (m, y + 16), line, 32, W - 2 * m)
        if special == "journal":
            je = journal_entry(W - 2 * m, 1.0)
            lift(s, je, (m, y + 60))
        elif name == "review-needs-human":
            br = screen(name, W - 2 * m, frame=False)
            lift(s, br, (m, y + 50))
            lg = confidence_legend(W - 2 * m)
            lift(s, lg, (m, y + 50 + br.size[1] + 40), 40)
        else:
            br = screen(name, W - m, max_h=H - y - 210)
            lift(s, br, (m // 2, y + 50))
        foot(s, W, H, m, page=f"{int(n) + 1} / 7")
        out.append(s)

    s = bg((W, H), dark=True)
    logo(s, m, 90, 56, dark=True)
    y = head2(s, (m, 340), "Books that close", "themselves. Almost.", 112, W - 2 * m, dark=True)
    para(s, (m, y + 30), "The AI does the sorting. You make the calls. The ledger keeps everyone honest.", 38, W - 2 * m, col="#C3C9D1")
    btn(s, m, y + 210, "See Ledger Book", 36, dark=True)
    foot(s, W, H, m, dark=True)
    out.append(s)

    for i, s in enumerate(out, 1):
        sk.save(s, OUT / "instagram/carousel-ai-proposes" / f"slide-{i:02d}.png")


def ig_posts():
    W, H = sk.IG_PORTRAIT
    m = 90
    out = []

    s = bg((W, H))
    kick(s, (m, 110), "Double-entry, enforced", 24)
    y = head(s, (m, 160), "Debits = Credits.", 120, W - 2 * m)
    y = head(s, (m, y), "Always.", 120, W - 2 * m, col=BLUE)
    je = journal_entry(W - 2 * m, 1.05)
    lift(s, je, (m, y + 70))
    para(s, (m, y + 70 + je.size[1] + 50), "Integer cents. Balanced entries. Posted entries are immutable — corrections are reversals.", 32, W - 2 * m)
    foot(s, W, H, m)
    out.append(("post-01-debits-equal-credits", s))

    s = bg((W, H))
    kick(s, (m, 110), "Review queue", 24)
    y = head2(s, (m, 160), "Every suggestion", "shows its work.", 100, W - 2 * m)
    y = para(s, (m, y + 16), "A confidence score and a reason on every line. Low confidence? It asks you instead of guessing.", 32, W - 2 * m)
    br = screen("review-queue", W - m, max_h=H - y - 210, frame=False)
    lift(s, br, (m // 2, y + 50))
    foot(s, W, H, m)
    out.append(("post-02-shows-its-work", s))

    s = bg((W, H), dark=True)
    kick(s, (m, 110), "Copilot", 24, NIGHT_BLUE)
    y = head2(s, (m, 160), "It can read.", "It can't touch.", 120, W - 2 * m, dark=True)
    para(s, (m, y + 20), "Ask about profit, who owes you or your runway. Every figure comes from a lookup against your ledger — and no tool exists that can post, send or move money.", 32, W - 2 * m, col="#C3C9D1")
    br = screen("copilot", W - m, dark=True)
    lift(s, br, (m // 2, y + 260), 150)
    foot(s, W, H, m, dark=True)
    out.append(("post-03-copilot-read-only", s))

    s = bg((W, H))
    kick(s, (m, 110), "Today", 24)
    y = head2(s, (m, 160), "“Are my books done?”", "One screen answers.", 92, W - 2 * m)
    y = para(s, (m, y + 16), "Cash on hand, who owes you, what you owe, a tax set-aside check and the next 13 weeks.", 32, W - 2 * m)
    br = screen("today-top", W - m, max_h=H - y - 210)
    lift(s, br, (m // 2, y + 50))
    foot(s, W, H, m)
    out.append(("post-04-today", s))

    s = bg((W, H))
    kick(s, (m, 110), "Month-end close", 24)
    y = head2(s, (m, 160), "Close the month", "with a checklist.", 100, W - 2 * m)
    y = para(s, (m, y + 16), "Only real blockers hold up a close. Lock it hard, or leave room for your accountant.", 32, W - 2 * m)
    br = screen("close", W - 2 * m, max_h=H - y - 210, frame=False)
    lift(s, br, (m, y + 50))
    foot(s, W, H, m)
    out.append(("post-05-close", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/posts" / f"{n}.png")


def ig_stories():
    W, H = sk.IG_STORY
    m = 90
    out = []
    s = bg((W, H))
    logo(s, m, 150, 66)
    y = head2(s, (m, 360), "6 items waiting.", "Approve over coffee.", 112, W - 2 * m)
    ph = phone("m-today", 1000)
    lift(s, ph, ((W - ph.size[0]) // 2, y + 60), 70)
    foot(s, W, H, m, 26)
    out.append(("story-01-review", s))

    s = bg((W, H), dark=True)
    kick(s, (m, 300), "Poll", 32, NIGHT_BLUE)
    y = head(s, (m, 360), "When did you last reconcile your books?", 104, W - 2 * m, col=NIGHT_INK)
    para(s, (m, y + 40), "(Poll sticker: This week / This quarter / Don't ask)", 32, W - 2 * m, col="#8C949E")
    logo(s, m, H - 240, 66, dark=True)
    out.append(("story-02-poll", s))

    s = bg((W, H))
    logo(s, m, 150, 66)
    y = head2(s, (m, 360), "Ask your books", "a question.", 120, W - 2 * m)
    ph = phone("m-copilot", 1000)
    lift(s, ph, ((W - ph.size[0]) // 2, y + 60), 70)
    foot(s, W, H, m, 26)
    out.append(("story-03-today", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/stories" / f"{n}.png")


def ig_reel():
    W, H = sk.IG_STORY
    m = 90
    sc = []
    s = bg((W, H), dark=True)
    y = head(s, (m, 640), "Shoebox of receipts.", 112, W - 2 * m, col="#8C949E")
    y = head(s, (m, y), "Twelve bank tabs.", 112, W - 2 * m, col="#8C949E")
    head(s, (m, y), "Sound familiar?", 112, W - 2 * m, col=NIGHT_INK)
    sc.append(sk.Scene(s, 2.6))

    def card(a, b_, ph_name=None, je=False, shot=None):
        s = bg((W, H))
        y = head2(s, (m, 300), a, b_, 112, W - 2 * m)
        if shot:
            im = screen(shot, W - 2 * m, frame=False)
            lift(s, im, (m, y + 120), 60)
        if ph_name:
            ph = phone(ph_name, 1000)
            lift(s, ph, ((W - ph.size[0]) // 2, y + 70), 70)
        if je:
            e = journal_entry(W - 2 * m, 1.05)
            lift(s, e, (m, y + 160))
        foot(s, W, H, m, 26)
        return s

    sc.append(sk.Scene(card("AI proposes.", "With a reason.", shot="review-needs-human"), 2.8))
    sc.append(sk.Scene(card("You approve.", "The ledger balances.", je=True), 2.8))
    sc.append(sk.Scene(card("Every number,", "always current.", "m-today"), 2.8))
    s = bg((W, H), dark=True)
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 100, dark=True)
    logo(s, (W - lw) / 2, 680, 100, dark=True)
    head(s, (m, 900), "AI proposes. You approve. The ledger posts.", 84, W - 2 * m, col=NIGHT_INK, align="center")
    para(s, (m, 1260), "The AI bookkeeper · by BigMo", 40, W - 2 * m, col=NIGHT_BLUE, align="center")
    sc.append(sk.Scene(s, 3.2, move="out", zoom=1.05))
    sk.render_video(sc, (W, H), OUT / "instagram/reel-ai-proposes-9x16.mp4")
    sk.save(sc[1].frame, OUT / "instagram/reel-cover.png")


# ======================================================================= LINKEDIN

def li_links():
    W, H = sk.LI_LINK
    m = 60
    items = [
        ("link-01-launch", "AI proposes.", "The ledger disposes.", "An AI bookkeeper on a real double-entry engine: model output never posts directly.", "today-top", False),
        ("link-02-review", "Every suggestion", "shows its work.", "Confidence, a reason, and a person's approval before anything reaches the journal.", "review-queue", True),
        ("link-03-reports", "Reports computed,", "never stored.", "P&L, balance sheet, cash flow and more — derived live from the journal.", "reports", False),
    ]
    for n, a, b_, line, name, bare in items:
        s = bg((W, H))
        logo(s, m, 50, 32)
        y = head2(s, (m, 130), a, b_, 50, 500)
        para(s, (m, y + 14), line, 20, 470)
        br = screen(name, 610, max_h=490, frame=not bare)
        lift(s, br, (W - 610 - 30, 70))
        sk.save(s, OUT / "linkedin/images" / f"{n}.png")


def li_document():
    W, H = sk.LI_SQUARE
    m = 90
    pages = []

    def page(n, k, a_, b_, text, visual):
        s = bg((W, H))
        kick(s, (m, 90), k, 22)
        y = head2(s, (m, 136), a_, b_, 66, W - 2 * m)
        y = para(s, (m, y + 10), text, 28, W - 2 * m)
        im, xy = visual(y)
        lift(s, im, xy)
        logo(s, m, H - 100, 36)
        sk.draw_text(s, (W - m - 50, H - 92), f"{n} / 8", inter(22), rgb("#7A818A"))
        pages.append(s)

    s = bg((W, H), dark=True)
    logo(s, m, 100, 56, dark=True)
    y = head2(s, (m, 360), "Six rules for an AI", "you can trust with your books.", 88, W - 2 * m, dark=True)
    para(s, (m, y + 30), "How Ledger Book keeps a language model useful — and out of the journal.", 34, W - 2 * m, col="#C3C9D1")
    pages.append(s)
    page(2, "Rule 1", "The model proposes.", "It never posts.", "AI output is a proposal. A deterministic posting service validates every entry before it reaches the journal.",
         lambda y: (screen("review-queue", W - 2 * m, max_h=H - y - 200, frame=False), (m, y + 40)))
    page(3, "Rule 2", "Show the reason,", "not just the answer.", "Every suggestion carries a confidence score and a plain-English why. Below the threshold, a person decides.",
         lambda y: (screen("review-needs-human", W - 2 * m, frame=False), (m, y + 60)))
    lg = confidence_legend(W - 2 * m, .75)
    lift(pages[-1], lg, (m, 785), 40)
    page(4, "Rule 3", "Debits equal credits.", "Enforced, not hoped.", "Integer cents, balanced entries across two or more lines — checked by the engine, not by a prompt.",
         lambda y: (journal_entry(W - 2 * m), (m, y + 60)))
    page(5, "Rule 4", "Posted means posted.", "", "Entries are immutable. Corrections are reversals — both stay on the record.",
         lambda y: (screen("journal", W - 2 * m, max_h=H - y - 200), (m, y + 40)))
    page(6, "Rule 5", "Store nothing", "you can compute.", "Balances and reports are derived from the journal on demand, so every screen agrees.",
         lambda y: (screen("reports", W - 2 * m, max_h=H - y - 200), (m, y + 40)))
    page(7, "Rule 6", "Give the copilot", "read-only tools.", "It can look up profit, invoices, runway and unusual activity. No tool exists that can post, send or move money.",
         lambda y: (screen("copilot", W - 2 * m), (m, y + 50)))
    s = bg((W, H), dark=True)
    logo(s, m, 100, 56, dark=True)
    y = head2(s, (m, 380), "AI proposes.", "The ledger disposes.", 112, W - 2 * m, dark=True)
    para(s, (m, y + 30), "Ledger Book is the AI bookkeeper from BigMo. Want an early look? Talk to us.", 34, W - 2 * m, col="#C3C9D1")
    btn(s, m, y + 200, "team@bigmoda.ai", 34, dark=True)
    pages.append(s)
    sk.pdf(pages, OUT / "linkedin/document-six-rules-ai-bookkeeping.pdf")
    for i, p in enumerate(pages, 1):
        sk.save(p, OUT / "linkedin/document-pages" / f"page-{i:02d}.png")


def li_video():
    W, H = sk.LI_VIDEO
    m = 140
    sc = []
    s = bg((W, H), dark=True)
    head2(s, (m, 400), "Would you let an AI", "post to your books?", 116, W - 2 * m, dark=True)
    sc.append(sk.Scene(s, 3.0))
    s = bg((W, H))
    head2(s, (m, 400), "Neither would we.", "So it doesn't.", 116, W - 2 * m)
    sc.append(sk.Scene(s, 2.6))

    def feat(k, a_, line, visual, dark=False):
        s = bg((W, H), dark=dark)
        kick(s, (m, 300), k, 26, NIGHT_BLUE if dark else BLUE)
        y = head(s, (m, 350), a_, 74, 620, col=NIGHT_INK if dark else INK)
        para(s, (m, y + 20), line, 32, 600, col="#C3C9D1" if dark else SOFT)
        logo(s, m, H - 150, 48, dark=dark)
        lift(s, visual, (W - visual.size[0] - 90, (H - visual.size[1]) // 2), 120 if dark else 60)
        return s

    sc.append(sk.Scene(feat("AI proposes", "A category, a confidence, a reason.", "Below the threshold, it asks you.", screen("review-queue", 1000, max_h=880, frame=False)), 3.8))
    sc.append(sk.Scene(feat("The ledger disposes", "Only balanced entries post.", "Immutable. Corrections are reversals.", journal_entry(900, 1.1)), 3.6))
    sc.append(sk.Scene(feat("Live numbers", "Computed from the journal.", "Cash, profit, receivables, runway.", screen("today-top", 1040, max_h=880)), 3.6))
    sc.append(sk.Scene(feat("Copilot", "It can read. It can't touch.", "No tool that posts, sends or moves money.", screen("copilot", 1040, dark=True), dark=True), 3.6))
    s = bg((W, H), dark=True)
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 100, dark=True)
    logo(s, (W - lw) / 2, 330, 100, dark=True)
    sk.block(s, (m, 520), "AI proposes. You approve. The ledger posts.", B.font(76, "bold"), rgb(NIGHT_INK), W - 2 * m, align="center")
    sk.block(s, (m, 680), "Ledger Book — the AI bookkeeper by BigMo · team@bigmoda.ai", inter(34), rgb(NIGHT_BLUE), W - 2 * m, align="center")
    sc.append(sk.Scene(s, 4, move="out", zoom=1.04))
    sk.render_video(sc, (W, H), OUT / "linkedin/video-ai-proposes-16x9.mp4")
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
