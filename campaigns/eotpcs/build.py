"""EOT-PCS — "From PI to paid. One controlled record." B2B social campaign (LinkedIn-led + Instagram).

Brand from the product (src/styles.css + login screen): navy sidebar/login ground,
light slate app surface, mono accent #5980A6, and the BigMo marks — "EOT-" white +
"PCS" orange (#FF6A2C), BigMo blue #2D5BFF. Brand colours only on marks/accents.

Truthfulness: EOT-PCS is a v1 pilot. No customer names, ROI or time-saved claims.
Screens are from a local demo build with fictional demo shipments.

Run:  python3 campaigns/eotpcs/build.py [--src ../eotpcs-export-order-to-payment-control-system] [--no-video]
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import socialkit as sk  # noqa: E402
from PIL import Image, ImageDraw, ImageFilter  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--src", default=str(HERE.parents[2] / "eotpcs-export-order-to-payment-control-system"))
ap.add_argument("--no-video", action="store_true")
args = ap.parse_args()
SRC = Path(args.src)
OUT = HERE / "output"
KIT = SRC / "docs/training-kit/screenshots"

INTER = "/usr/share/fonts/opentype/inter/"
B = sk.Brand(
    name="EOT-PCS", bg="#F1F2F4", surface="#FFFFFF", ink="#1D2329", muted="#5B636E",
    primary="#5980A6", accent="#FF6A2C", font_regular=INTER + "Inter-Regular.otf",
    font_bold=INTER + "InterDisplay-Bold.otf", font_italic=INTER + "InterDisplay-SemiBold.otf",
    url="bigmoda.ai", tracking=-0.028,
)
NAVY, NAVY2, SLATE = "#0E1626", "#1B2537", "#5980A6"
PAPER, WHITE, INK, BODY, DIM = "#F1F2F4", "#FFFFFF", "#1D2329", "#4B535E", "#6B7380"
ORANGE, BLUE, BLUE_SOFT = "#FF6A2C", "#2D5BFF", "#5C82FF"
GREEN, RED, AMBER = "#2F8F5B", "#C2453A", "#B7861F"
FOOT = "EOT-PCS · v1 pilot · Powered by BigMo"


def rgb(h, a=255):
    return sk.hex2rgb(h, a)


# ------------------------------------------------------------- brand pieces

def bg(size, dark=False):
    W, H = size
    if dark:
        g = Image.new("RGBA", size)
        d = ImageDraw.Draw(g)
        a, b = rgb(NAVY2), rgb(NAVY)
        for y in range(H):
            t = y / H
            d.line([(0, y), (W, y)], fill=tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3)) + (255,))
        lay = Image.new("RGBA", size, (0, 0, 0, 0))
        ImageDraw.Draw(lay).ellipse([W * .5, -H * .25, W * 1.3, H * .45], fill=rgb(BLUE, 40))
        g.alpha_composite(lay.filter(ImageFilter.GaussianBlur(W // 9)))
        return g
    g = sk.canvas(size, PAPER)
    # faint route line — the shipment's path, used as a brand motif
    lay = Image.new("RGBA", size, (0, 0, 0, 0))
    route(lay, W * .55, H * .06, W * 1.02, H * .06, rgb(SLATE, 60), max(2, W // 400), dots=4)
    g.alpha_composite(lay)
    return g


def route(img, x0, y0, x1, y1, col, width, dots=7, done=None, labels=None, font=None, lcol=None):
    """A lifecycle 'route': line with milestone dots. done = index up to which dots are filled orange."""
    d = ImageDraw.Draw(img)
    d.line([(x0, y0), (x1, y1)], fill=col, width=width)
    for i in range(dots):
        t = i / max(1, dots - 1)
        x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        r = width * 3.2
        filled = done is not None and i <= done
        d.ellipse([x - r, y - r, x + r, y + r], fill=rgb(ORANGE) if filled else (col if done is None else rgb(PAPER)),
                  outline=rgb(ORANGE) if filled else col, width=width)
        if labels and font:
            lw = font.getlength(labels[i])
            d.text((x - lw / 2, y + r + width * 3), labels[i], font=font, fill=lcol)


def logo(img, x, y, h, dark=True):
    f = B.font(int(h), "bold")
    w1 = sk.draw_text(img, (x, y), "EOT-", f, rgb(WHITE if dark else INK), tracking_px=-h * .02)
    w2 = sk.draw_text(img, (x + w1, y), "PCS", f, rgb(ORANGE), tracking_px=-h * .02)
    return w1 + w2


def bigmo(img, x, y, h, dark=True):
    """'BiGMo' lockup as shipped on the login screen: BiG white/ink, Mo orange, blue chevrons."""
    f = B.font(int(h), "bold")
    w = sk.draw_text(img, (x, y), "BiG", f, rgb(WHITE if dark else INK))
    w += sk.draw_text(img, (x + w, y), "Mo", f, rgb(ORANGE))
    d = ImageDraw.Draw(img)
    cx, cy, s = x + w + h * .3, y + h * .58, h * .32
    for k in range(2):
        ox = cx + k * s * .9
        d.polygon([(ox, cy - s), (ox + s, cy), (ox, cy + s)], fill=rgb(BLUE_SOFT))
    return w + h * 1.3


def lockup(img, x, y, h, dark=True):
    logo(img, x, y, h, dark)
    sk.draw_text(img, (x, y + h * 1.2), "EXPORT ORDER-TO-PAYMENT CONTROL SYSTEM", B.font(max(12, int(h * .22)), "bold"),
                 rgb("#B9C2D0" if dark else DIM), tracking_px=h * .22 * .25)


def kick(img, xy, s, size, col=SLATE):
    sk.draw_text(img, xy, s.upper(), B.font(size, "bold"), rgb(col), tracking_px=size * .16)


def head(img, xy, s, size, max_w, col=INK, lh=1.06, align="left"):
    return sk.block(img, xy, s, B.font(size, "bold"), rgb(col), max_w, line_h=lh, tracking_px=size * B.tracking, align=align)


def head2(img, xy, a, b_, size, max_w, dark=False):
    y = head(img, xy, a, size, max_w, col=WHITE if dark else INK)
    return head(img, (xy[0], y), b_, size, max_w, col=ORANGE if dark else SLATE)


def para(img, xy, s, size, max_w, col=BODY, lh=1.42, align="left"):
    return sk.block(img, xy, s, B.font(size), rgb(col), max_w, line_h=lh, align=align)


def btn(img, x, y, s, size=30):
    return sk.pill(img, (x, y), s, B.font(size, "bold"), WHITE, ORANGE, pad=(int(size * .9), int(size * .55)), radius=6)


def tag(img, x, y, s, col, size=22):
    return sk.pill(img, (x, y), s, B.font(size, "bold"), WHITE, col, pad=(int(size * .6), int(size * .3)), radius=4)


def foot(img, W, H, m, size=20, dark=False, page=None):
    c = "#8D97A6" if dark else DIM
    para(img, (m, H - m * .85), FOOT, size, W - 2 * m, col=c)
    if page:
        f = B.font(size)
        sk.draw_text(img, (W - m - sk.text_width(f, page), H - m * .85), page, f, rgb(c))


SIDEBAR = (232, 0, 1440, 900)


def shot(name, crop=SIDEBAR):
    im = Image.open(KIT / f"{name}.webp").convert("RGB")
    return im.crop(crop) if crop else im


def desk(name, width, max_h=None, crop=SIDEBAR):
    br = sk.browser(shot(name, crop), width, chrome="#DDE1E6", url="eot-pcs", ink=DIM, radius=10)
    return sk.cap(br, max_h) if max_h else br


def panel(name, crop, width):
    """A zoomed-in region of a screen as a floating card (used for vertical formats)."""
    im = shot(name, crop)
    s = width / im.size[0]
    im = im.resize((width, int(im.size[1] * s)), Image.LANCZOS)
    return sk.rounded(im, 10)


def lift(base, im, xy, dark=False):
    sk.shadow_paste(base, im, xy, blur=34, offset=(0, 22), opacity=150 if dark else 55)


LIFECYCLE = ["PI", "Production", "QC", "Dispatch", "Docs", "Approval", "Sent", "Paid"]


# ======================================================================= INSTAGRAM

def ig_carousel():
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    s = bg((W, H), dark=True)
    lockup(s, m, 110, 64)
    y = head2(s, (m, 330), "From PI to paid.", "One controlled record.", 100, W - 2 * m, dark=True)
    para(s, (m, y + 30), "Every export shipment in one place — not a spreadsheet plus an inbox.", 38, W - 2 * m, col="#D7DDE6")
    route(s, m, y + 260, W - m, y + 260, rgb("#55627A"), 5, dots=8, done=7,
          labels=LIFECYCLE, font=B.font(20, "bold"), lcol=rgb("#B9C2D0"))
    kick(s, (m, H - 150), "Swipe · 5 controls", 24, ORANGE)
    foot(s, W, H, m, dark=True)
    out.append(s)

    steps = [
        ("01", "Oracle stays", "the source of truth.", "Customer, order lines and invoice values are pulled read-only. Nothing is re-keyed.", "24-wizard-oracle-pull"),
        ("02", "Checklists that", "write themselves.", "Rules by customer, country, Incoterms, product and transport decide which documents are mandatory.", "33-document-workspace-checklist"),
        ("03", "Missing a document?", "It can't be submitted.", "Submission is blocked until every mandatory document is in and no draft remains.", "34-documents-br004-blocked"),
        ("04", "The maker can never", "be the checker.", "Segregation of duties is enforced by the system, with AI findings flagged before approval.", "46-approvals-br005-blocked"),
        ("05", "Payments chase", "themselves.", "Outstanding balances, due-date reminders and an escalation sweep — every action in the audit log.", "49-payments-queue"),
    ]
    for n, a, b_, line, name in steps:
        s = bg((W, H))
        kick(s, (m, 100), f"Control {n} / 05", 24, DIM)
        y = head2(s, (m, 150), a, b_, 84, W - 2 * m)
        y = para(s, (m, y + 16), line, 34, W - 2 * m)
        br = desk(name, W - m, max_h=H - y - 200)
        lift(s, br, (m // 2, y + 46))
        foot(s, W, H, m, page=f"{int(n) + 1} / 7")
        out.append(s)

    s = bg((W, H), dark=True)
    lockup(s, m, 110, 64)
    y = head2(s, (m, 330), "Every shipment.", "Every document. Logged.", 96, W - 2 * m, dark=True)
    para(s, (m, y + 30), "EOT-PCS is in pilot with BigMo. Exporters ready to retire the tracker spreadsheet — talk to us.", 36, W - 2 * m, col="#D7DDE6")
    btn(s, m, y + 230, "Book a walkthrough", 36)
    bigmo(s, m, H - 200, 48)
    foot(s, W, H, m, dark=True)
    out.append(s)

    for i, s in enumerate(out, 1):
        sk.save(s, OUT / "instagram/carousel-pi-to-paid" / f"slide-{i:02d}.png")


def ig_posts():
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    # 1 spreadsheet vs system
    s = bg((W, H))
    kick(s, (m, 110), "Before / after", 26)
    y = head(s, (m, 160), "Your export tracker", 96, W - 2 * m)
    y = head(s, (m, y), "shouldn't be a spreadsheet.", 96, W - 2 * m, col=SLATE)
    rows = [("Excel tracker", "Email threads", "Who approved this?", "Is it paid yet?"),
            ("One shipment ID", "Rule-based checklist", "Maker-checker approval", "Live outstanding balance")]
    yy = y + 50
    colw = (W - 2 * m - 30) // 2
    for ci, (title, col) in enumerate([("Before", RED), ("With EOT-PCS", GREEN)]):
        x = m + ci * (colw + 30)
        ImageDraw.Draw(s).rounded_rectangle([x, yy, x + colw, yy + 560], 10, fill=rgb(WHITE), outline=rgb("#DDE1E6"), width=2)
        tag(s, x + 30, yy + 30, title, col, 24)
        for ri, t in enumerate(rows[ci]):
            ty = yy + 120 + ri * 105
            sk.draw_text(s, (x + 30, ty), ("–" if ci == 0 else "✓"), B.font(30, "bold"), rgb(col))
            sk.block(s, (x + 80, ty), t, B.font(30), rgb(INK), colw - 110, line_h=1.2)
    foot(s, W, H, m)
    out.append(("post-01-before-after", s))

    # 2 lifecycle
    s = bg((W, H), dark=True)
    kick(s, (m, 110), "Server-enforced state machine", 26, ORANGE)
    y = head2(s, (m, 160), "Eight stages.", "No skipping.", 110, W - 2 * m, dark=True)
    para(s, (m, y + 20), "Each transition is checked on the server and written to an append-only audit log.", 34, W - 2 * m, col="#D7DDE6")
    ys = y + 200
    for i, st in enumerate(["PI received", "Order confirmed", "Production · QC passed", "Dispatched",
                            "Documents prepared & checked", "Approved (maker ≠ checker)", "Sent to customer", "Payment closed"]):
        yy = ys + i * 78
        d = ImageDraw.Draw(s)
        if i < 7:
            d.line([(m + 22, yy + 22), (m + 22, yy + 100)], fill=rgb("#55627A"), width=4)
        d.ellipse([m + 8, yy + 8, m + 36, yy + 36], fill=rgb(ORANGE if i in (0, 7) else SLATE))
        sk.draw_text(s, (m + 66, yy + 4), st, B.font(32, "bold" if i in (0, 7) else "regular"), rgb(WHITE))
    foot(s, W, H, m, dark=True)
    out.append(("post-02-eight-stages", s))

    # 3 maker-checker
    s = bg((W, H))
    kick(s, (m, 110), "Segregation of duties", 26)
    y = head2(s, (m, 160), "You prepared it?", "Someone else approves it.", 92, W - 2 * m)
    para(s, (m, y + 20), "The system refuses self-approval — not a policy PDF, a hard rule.", 34, W - 2 * m)
    p = panel("46-approvals-br005-blocked", (470, 270, 970, 640), W - 2 * m)
    lift(s, p, (m, y + 140))
    foot(s, W, H, m)
    out.append(("post-03-maker-checker", s))

    # 4 audit
    s = bg((W, H))
    kick(s, (m, 110), "Append-only audit log", 26)
    y = head2(s, (m, 160), "Every click", "leaves a receipt.", 104, W - 2 * m)
    para(s, (m, y + 20), "State changes, uploads, approvals, waivers, emails and payments — immutable, filterable, exportable.", 34, W - 2 * m)
    br = desk("61-audit-expanded", W - m, max_h=H - y - 300)
    lift(s, br, (m // 2, y + 200))
    foot(s, W, H, m)
    out.append(("post-04-audit", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/posts" / f"{n}.png")


def story_frame(seed_dark, a, b_, name, crop, line=None):
    W, H = sk.IG_STORY
    m = 90
    s = bg((W, H), dark=seed_dark)
    lockup(s, m, 170, 56, dark=seed_dark)
    y = head2(s, (m, 400), a, b_, 108, W - 2 * m, dark=seed_dark)
    if line:
        y = para(s, (m, y + 20), line, 40, W - 2 * m, col="#D7DDE6" if seed_dark else BODY)
    p = panel(name, crop, W - 2 * m)
    p = sk.cap(p, H - y - 300)
    lift(s, p, (m, y + 70), dark=seed_dark)
    foot(s, W, H, m, 26, dark=seed_dark)
    return s


def ig_stories():
    out = [
        ("story-01-control-board", story_frame(True, "Exceptions first.", "Not reports last.", "03-dashboard-admin", (240, 100, 900, 900),
                                               "The control board shows what's blocked, overdue or waiting — before it's a problem.")),
        ("story-02-checklist", story_frame(False, "The rules decide", "the paperwork.", "16-masters-checklist-preview", (232, 60, 900, 900))),
        ("story-03-customer-portal", story_frame(True, "Customers see", "their shipments.", "62-portal-customer", (232, 0, 900, 900),
                                                 "A read-only portal — no more 'where's my B/L?' emails.")),
    ]
    for n, s in out:
        sk.save(s, OUT / "instagram/stories" / f"{n}.png")


def ig_reel():
    W, H = sk.IG_STORY
    m = 90
    sc = []
    s = bg((W, H), dark=True)
    y = head(s, (m, 600), "Spreadsheets.", 140, W - 2 * m, col=WHITE)
    y = head(s, (m, y), "Email threads.", 140, W - 2 * m, col="#8D97A6")
    head(s, (m, y), "One shipment.", 140, W - 2 * m, col=ORANGE)
    sc.append(sk.Scene(s, 2.6))
    sc.append(sk.Scene(story_frame(False, "Pull from Oracle.", "Never re-key.", "24-wizard-oracle-pull", (232, 60, 900, 900)), 3.0))
    sc.append(sk.Scene(story_frame(True, "Missing a doc?", "Blocked.", "34-documents-br004-blocked", (232, 60, 900, 900)), 3.0))
    sc.append(sk.Scene(story_frame(False, "Self-approval?", "Refused.", "46-approvals-br005-blocked", (470, 270, 970, 640)), 3.0))
    s = bg((W, H), dark=True)
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 150)
    logo(s, (W - lw) / 2, 640, 150)
    route(s, m, 960, W - m, 960, rgb("#55627A"), 6, dots=8, done=7)
    head(s, (m, 1080), "From PI to paid. One controlled record.", 72, W - 2 * m, col=WHITE, align="center")
    bw = bigmo(Image.new("RGBA", (10, 10)), 0, 0, 60)
    bigmo(s, (W - bw) / 2, 1420, 60)
    sc.append(sk.Scene(s, 3.4, move="out", zoom=1.05))
    sk.render_video(sc, (W, H), OUT / "instagram/reel-pi-to-paid-9x16.mp4")
    sk.save(sc[1].frame, OUT / "instagram/reel-cover.png")


# ======================================================================= LINKEDIN

def li_links():
    W, H = sk.LI_LINK
    m = 60
    items = [
        ("link-01-launch", "From PI to paid.", "One controlled record.", "Replace export tracker spreadsheets with one auditable workflow — Oracle stays the source of truth.", "03-dashboard-admin", True),
        ("link-02-documents", "The checklist", "writes itself.", "Document requirements from rules: customer, country, Incoterms, product, payment terms, transport.", "33-document-workspace-checklist", False),
        ("link-03-approvals", "Maker ≠ checker.", "Enforced.", "Document packages need a second person to approve — with AI findings flagged first.", "41-approvals-review-findings", False),
    ]
    for n, a, b_, line, name, dark in items:
        s = bg((W, H), dark=dark)
        logo(s, m, 50, 34, dark=dark)
        y = head2(s, (m, 130), a, b_, 50, 520, dark=dark)
        para(s, (m, y + 16), line, 22, 480, col="#D7DDE6" if dark else BODY)
        para(s, (m, H - 70), FOOT, 16, 500, col="#8D97A6" if dark else DIM)
        br = desk(name, 600, max_h=480)
        lift(s, br, (W - 600 - 30, 70), dark=dark)
        sk.save(s, OUT / "linkedin/images" / f"{n}.png")


def li_document():
    """8-page document: 'The export order-to-payment playbook' — for export ops, finance and CXOs."""
    W, H = sk.LI_SQUARE
    m = 90
    pages = []

    def page(n, k, a, b_, text, name):
        s = bg((W, H))
        kick(s, (m, 80), k, 22)
        y = head2(s, (m, 130), a, b_, 66, W - 2 * m)
        y = para(s, (m, y + 10), text, 30, W - 2 * m)
        br = desk(name, W - 2 * m + 40, max_h=H - y - 190)
        lift(s, br, (m - 20, y + 40))
        logo(s, m, H - 92, 30, dark=False)
        f = B.font(22)
        sk.draw_text(s, (W - m - 50, H - 86), f"{n} / 8", f, rgb(DIM))
        pages.append(s)

    s = bg((W, H), dark=True)
    lockup(s, m, 110, 60)
    y = head2(s, (m, 330), "Seven controls between", "a PI and a payment.", 92, W - 2 * m, dark=True)
    para(s, (m, y + 30), "A playbook for export operations and finance teams moving off spreadsheets and inboxes.", 34, W - 2 * m, col="#D7DDE6")
    route(s, m, y + 240, W - m, y + 240, rgb("#55627A"), 5, dots=8, done=7, labels=LIFECYCLE, font=B.font(20, "bold"), lcol=rgb("#B9C2D0"))
    foot(s, W, H, m, 22, dark=True)
    pages.append(s)
    page(2, "Control 1 · Source of truth", "Pull it from Oracle.", "Don't type it.", "Invoice values and lines are read-only in EOT-PCS — the ERP stays the system of record.", "26-shipment-oracle-overview")
    page(3, "Control 2 · State machine", "One shipment ID,", "one lifecycle.", "PI → production → QC → dispatch → documents → approval → sent → paid. Server-enforced.", "08-shipment-overview")
    page(4, "Control 3 · Rule-based checklists", "The rules decide", "which documents.", "By customer, country, Incoterms, product group, payment terms and transport mode.", "16-masters-checklist-preview")
    page(5, "Control 4 · Completeness gate", "Incomplete packages", "can't move.", "Mandatory documents missing or drafts open? Submission is blocked, with the reason shown.", "34-documents-br004-blocked")
    page(6, "Control 5 · Maker-checker", "Two people, always.", "AI flags first.", "Advisory findings compare documents; a different user must approve or reject.", "41-approvals-review-findings")
    page(7, "Controls 6 & 7 · Payment + audit", "Chase every balance.", "Log every action.", "Reminder rules, an escalation sweep and an append-only audit trail.", "55-escalation-sweep")
    s = bg((W, H), dark=True)
    lockup(s, m, 110, 60)
    y = head2(s, (m, 360), "Retire the tracker", "spreadsheet.", 110, W - 2 * m, dark=True)
    para(s, (m, y + 30), "EOT-PCS is in pilot. If you run export operations and want a walkthrough on your own document rules, talk to BigMo.", 34, W - 2 * m, col="#D7DDE6")
    btn(s, m, y + 230, "Book a walkthrough · bigmoda.ai", 34)
    bigmo(s, m, H - 200, 50)
    pages.append(s)

    sk.pdf(pages, OUT / "linkedin/document-seven-controls-playbook.pdf")
    for i, p in enumerate(pages, 1):
        sk.save(p, OUT / "linkedin/document-pages" / f"page-{i:02d}.png")


def li_video():
    W, H = sk.LI_VIDEO
    m = 120
    sc = []

    def title(a, b_, dark=True):
        s = bg((W, H), dark=dark)
        head2(s, (m, 380), a, b_, 120, W - 2 * m, dark=dark)
        return s

    def feat(k, a, line, name, dark=False):
        s = bg((W, H), dark=dark)
        kick(s, (m, 280), k, 26, ORANGE if dark else SLATE)
        y = head(s, (m, 330), a, 76, 620, col=WHITE if dark else INK)
        para(s, (m, y + 20), line, 34, 600, col="#D7DDE6" if dark else BODY)
        logo(s, m, H - 150, 44, dark=dark)
        br = desk(name, 1040, max_h=880)
        lift(s, br, (W - 1040 - 80, (H - br.size[1]) // 2), dark=dark)
        return s

    sc.append(sk.Scene(title("Every export shipment", "lives in ten places."), 2.8))
    sc.append(sk.Scene(title("What if it lived", "in one?", dark=False), 2.6))
    sc.append(sk.Scene(feat("Control board", "Exceptions first.", "Blocked, overdue, waiting — drill into any number.", "03-dashboard-admin"), 3.6))
    sc.append(sk.Scene(feat("Documents", "Rules write the checklist.", "Incomplete packages are blocked.", "33-document-workspace-checklist"), 3.6))
    sc.append(sk.Scene(feat("Approvals", "Maker ≠ checker.", "AI findings flagged before a second person approves.", "41-approvals-review-findings", dark=True), 3.6))
    sc.append(sk.Scene(feat("Payments", "Balances that chase themselves.", "Reminders and an escalation sweep.", "49-payments-queue"), 3.6))
    s = bg((W, H), dark=True)
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 130)
    logo(s, (W - lw) / 2, 280, 130)
    route(s, 360, 520, W - 360, 520, rgb("#55627A"), 5, dots=8, done=7, labels=LIFECYCLE, font=B.font(22, "bold"), lcol=rgb("#B9C2D0"))
    sk.block(s, (m, 660), "From PI to paid. One controlled record.", B.font(60, "bold"), rgb(WHITE), W - 2 * m, align="center")
    bw = bigmo(Image.new("RGBA", (10, 10)), 0, 0, 52)
    bigmo(s, (W - bw) / 2, 820, 52)
    sk.block(s, (m, H - 100), "v1 pilot · bigmoda.ai", B.font(28), rgb("#8D97A6"), W - 2 * m, align="center")
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
