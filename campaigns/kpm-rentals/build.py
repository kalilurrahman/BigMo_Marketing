"""KPMRentals — "Your U.S. rentals, without the 2 a.m. calls." campaign (Instagram + LinkedIn).

Brand from the product (src/styles.css, public/icons/icon.svg): deep emerald #064E3B,
warm cream #F5F0E0, brushed gold #C9A84C (borders/fills only), mid emerald #0D7A5F;
DM Serif Display headlines, Fira Sans body; house-outline app icon.

Claims discipline:
  * Memphis-first, Tennessee operator — never "nationwide" as a present fact.
  * No prices, fees, returns, occupancy or market stats in copy.
  * The property photographs in src/assets/hero are the site's own hero imagery and
    read as illustrative; they are used as mood images, never captioned as a real
    available listing or address.
  * AI recommends, humans approve: every AI line keeps the human in the loop.
  * Screens show demo data (e.g. "Dana", sample Memphis addresses).

Screenshots: docs/media/screenshots/*.jpg are Git LFS objects — run
`git lfs pull` in the kpm-rentals repo first.

Run:  python3 campaigns/kpm-rentals/build.py [--src ../kpm-rentals] [--no-video]
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import socialkit as sk  # noqa: E402
from PIL import Image, ImageDraw, ImageFilter, ImageFont  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--src", default=str(HERE.parents[2] / "kpm-rentals"))
ap.add_argument("--no-video", action="store_true")
args = ap.parse_args()
SRC = Path(args.src)
OUT = HERE / "output"
SHOTS = SRC / "docs/media/screenshots"
PHOTOS = SRC / "src/assets"

FONTS = HERE.parents[1] / "tools/fonts"
B = sk.Brand(
    name="KPMRentals", bg="#F5F0E0", surface="#FFFDF7", ink="#13231D", muted="#4E5B55",
    primary="#064E3B", accent="#C9A84C", font_regular=str(FONTS / "FiraSans-400.ttf"),
    font_bold=str(FONTS / "DMSerifDisplay-400.ttf"), font_italic=str(FONTS / "DMSerifDisplay-400-italic.ttf"),
    url="kpm-rentals.lovable.app", tracking=-0.01,
)
CREAM, PAPER, INK, BODY = "#F5F0E0", "#FFFDF7", "#13231D", "#4E5B55"
EMERALD, EMERALD_M, MINT, GOLD = "#064E3B", "#0D7A5F", "#8FC7A3", "#C9A84C"
GOLD_TEXT = "#8A6D1E"  # gold readable on cream


def rgb(h, a=255):
    return sk.hex2rgb(h, a)


def fira(size, w=400):
    return ImageFont.truetype(str(FONTS / f"FiraSans-{w}.ttf"), size)


if not (SHOTS / "home.jpg").exists() or (SHOTS / "home.jpg").stat().st_size < 1000:
    sys.exit("Screenshots are Git LFS pointers — run `git lfs pull` in the kpm-rentals repo first.")


# ------------------------------------------------------------- brand pieces

def bg(size, kind="cream"):
    W, H = size
    if kind == "emerald":
        g = Image.new("RGBA", size)
        d = ImageDraw.Draw(g)
        a, b = rgb("#0A5C47"), rgb("#04362A")
        for y in range(H):
            t = y / H
            d.line([(0, y), (W, y)], fill=tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3)) + (255,))
        return g
    g = sk.canvas(size, CREAM if kind == "cream" else PAPER)
    # gold hairline frame — the brand's "brushed gold borders"
    d = ImageDraw.Draw(g)
    inset = max(18, W // 45)
    d.rectangle([inset, inset, W - inset, H - inset], outline=rgb(GOLD, 150), width=max(1, W // 700))
    return g


def icon(img, x, y, h, dark=False):
    """App icon: house outline on an emerald tile with a mint dot (public/icons/icon.svg)."""
    s = h / 512
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([x, y, x + h, y + h], int(112 * s), fill=rgb(CREAM if dark else EMERALD))
    ink = EMERALD if dark else "#F4EFE4"
    w = max(2, int(28 * s))
    pts = [(256, 118), (400, 232), (400, 394), (112, 394), (112, 232), (256, 118)]
    d.line([(x + px * s, y + py * s) for px, py in pts], fill=rgb(ink), width=w, joint="curve")
    door = [(196, 394), (196, 300), (316, 300), (316, 394)]
    d.line([(x + px * s, y + py * s) for px, py in door], fill=rgb(ink), width=max(2, int(24 * s)), joint="curve")
    r = 26 * s
    d.ellipse([x + 256 * s - r, y + 222 * s - r, x + 256 * s + r, y + 222 * s + r], fill=rgb(MINT))


def logo(img, x, y, h, dark=False):
    icon(img, x, y, h, dark)
    f = B.font(int(h * .78), "bold")
    w1 = sk.draw_text(img, (x + h * 1.25, y + h * .02), "KPM", f, rgb(CREAM if dark else EMERALD))
    w2 = sk.draw_text(img, (x + h * 1.25 + w1, y + h * .02), "Rentals", f, rgb(GOLD if dark else INK))
    return h * 1.25 + w1 + w2


def kick(img, xy, s, size, col=GOLD_TEXT):
    sk.draw_text(img, xy, s.upper(), fira(size, 600), rgb(col), tracking_px=size * .18)


def head(img, xy, s, size, max_w, col=INK, lh=1.05, align="left", italic=False):
    return sk.block(img, xy, s, B.font(size, "italic" if italic else "bold"), rgb(col), max_w, line_h=lh, align=align)


def head2(img, xy, a, b_, size, max_w, dark=False, align="left"):
    y = head(img, xy, a, size, max_w, col=CREAM if dark else INK, align=align)
    return head(img, (xy[0], y), b_, size, max_w, col=GOLD if dark else EMERALD_M, align=align, italic=True)


def para(img, xy, s, size, max_w, col=BODY, lh=1.45, align="left"):
    return sk.block(img, xy, s, fira(size), rgb(col), max_w, line_h=lh, align=align)


def btn(img, x, y, s, size=30, dark=False):
    return sk.pill(img, (x, y), s, fira(size, 600), EMERALD if dark else CREAM, GOLD if dark else EMERALD,
                   pad=(int(size * .95), int(size * .55)), radius=int(size * .25))


def foot(img, W, H, m, size=20, dark=False, page=None, text="KPMRentals · Memphis-first property management"):
    c = "#C9D9CF" if dark else "#6B756F"
    para(img, (m, H - m * .95), text, size, W - 2 * m, col=c)
    if page:
        sk.draw_text(img, (W - m - fira(size).getlength(page), H - m * .95), page, fira(size), rgb(c))


def lift(base, im, xy, op=60):
    sk.shadow_paste(base, im, xy, blur=32, offset=(0, 22), opacity=op)


def photo(name, size):
    """Cover-crop a hero photo to size."""
    im = Image.open(PHOTOS / name).convert("RGB")
    W, H = size
    s = max(W / im.size[0], H / im.size[1])
    im = im.resize((int(im.size[0] * s) + 1, int(im.size[1] * s) + 1), Image.LANCZOS)
    x, y = (im.size[0] - W) // 2, (im.size[1] - H) // 2
    return im.crop((x, y, x + W, y + H)).convert("RGBA")


def shade(img, top=0.0, bottom=0.85, col="#04362A"):
    """Vertical emerald gradient over a photo for legible type."""
    W, H = img.size
    lay = Image.new("RGBA", img.size)
    d = ImageDraw.Draw(lay)
    c = rgb(col)
    for y in range(H):
        t = y / H
        a = int(255 * (top + (bottom - top) * (t ** 1.6)))
        if t < .2:  # top scrim so the logo reads on bright skies
            a = max(a, int(255 * .6 * (1 - t / .2)))
        d.line([(0, y), (W, y)], fill=c[:3] + (a,))
    out = img.copy()
    out.alpha_composite(lay)
    return out


SIDEBAR = 400  # app pages: 200 css px sidebar at 2x


def shot(name, crop=None):
    im = Image.open(SHOTS / f"{name}.jpg").convert("RGB")
    return im.crop(crop) if crop else im


def app(name, width, max_h=None, top=0, h=1800, left=SIDEBAR, right=2880):
    br = sk.browser(shot(name, (left, top, right, top + h)), width, chrome="#E9E1C9", url="kpm-rentals", ink=BODY, radius=12)
    return sk.cap(br, max_h) if max_h else br


def mob(name, h, top=0, crop_h=1792):
    im = shot(name)
    im = im.crop((0, top, im.size[0], min(im.size[1], top + crop_h)))
    return sk.phone(im, h, bezel="#13231D")


# ======================================================================= INSTAGRAM

def ig_carousel_owners():
    """Remote/NRI owners: 7 slides."""
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    s = shade(photo("hero/tn-01.jpg", (W, H)), .25, .92)
    logo(s, m, 80, 60, dark=True)
    y = head2(s, (m, 720), "Your U.S. rentals,", "without the 2 a.m. calls.", 100, W - 2 * m, dark=True)
    para(s, (m, y + 24), "Property management for owners who live 13 time zones away.", 36, W - 2 * m, col="#E6EFE9")
    kick(s, (m, H - 120), "Swipe · 5 things that change", 22, GOLD)
    out.append(s)

    feats = [
        ("01", "AI-priced repairs.", "Every ticket arrives with a cost band benchmarked against similar Memphis jobs. Outlier quotes get flagged.", ("ticket-detail", 0, 1500)),
        ("02", "Decisions in your morning.", "Non-urgent decisions are batched into one digest in your local time. One screen, ten seconds.", ("dashboard", 0, 1500)),
        ("03", "Silence is a valid answer.", "Each memo proposes a default — 'we'll proceed with vendor B unless you object by 10:00 IST.'", ("pipeline", 0, 1500)),
        ("04", "Vendors, scored.", "See each vendor's score, rework rate and cost variance. Switch away from underperformers in one place.", ("vendors", 0, 1500)),
        ("05", "Every decision, on the record.", "Every AI suggestion, human override, photo and quote — timestamped and exportable.", ("ai-decisions", 0, 1500)),
    ]
    for n, t, line, (name, top, h) in feats:
        s = bg((W, H))
        kick(s, (m, 100), f"For remote owners · {n} / 05", 22)
        y = head(s, (m, 150), t, 84, W - 2 * m)
        y = para(s, (m, y + 16), line, 32, W - 2 * m)
        br = app(name, W - m, max_h=H - y - 200, top=top, h=h)
        lift(s, br, (m // 2, y + 46))
        foot(s, W, H, m, page=f"{int(n) + 1} / 7")
        out.append(s)

    s = bg((W, H), "emerald")
    logo(s, m, 90, 60, dark=True)
    y = head2(s, (m, 330), "Own in Memphis.", "Live anywhere.", 116, W - 2 * m, dark=True)
    para(s, (m, y + 30), "Get a free rental analysis for your Tennessee property — market rent benchmark, days-to-lease estimate and an onboarding plan.", 36, W - 2 * m, col="#E6EFE9")
    btn(s, m, y + 260, "Get a free rental analysis", 34, dark=True)
    foot(s, W, H, m, dark=True, text="Link in bio · kpm-rentals.lovable.app")
    out.append(s)

    for i, s in enumerate(out, 1):
        sk.save(s, OUT / "instagram/carousel-remote-owners" / f"slide-{i:02d}.png")


def ig_posts():
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    s = shade(photo("hero-home.jpg", (W, H)), .15, .9)
    logo(s, m, 80, 56, dark=True)
    y = head2(s, (m, 860), "Your property.", "Our priority.", 120, W - 2 * m, dark=True)
    para(s, (m, y + 20), "Tennessee-headquartered, full-service property management.", 34, W - 2 * m, col="#E6EFE9")
    out.append(("post-01-your-property", s))

    s = bg((W, H))
    kick(s, (m, 100), "For residents", 24)
    y = head2(s, (m, 150), "Rent, repairs,", "one app.", 108, W - 2 * m)
    para(s, (m, y + 16), "Pay by ACH or card, report a repair with a photo and follow it live — from your phone.", 32, W - 2 * m)
    p1, p2 = mob("tenant-mobile", 680), mob("technician-mobile", 680)
    lift(s, p1, (W // 2 - p1.size[0] - 20, y + 170), 80)
    lift(s, p2, (W // 2 + 20, y + 230), 80)
    foot(s, W, H, m)
    out.append(("post-02-residents", s))

    s = bg((W, H), "emerald")
    kick(s, (m, 100), "Live dispatch", 24, GOLD)
    y = head2(s, (m, 150), "A technician,", "already on the way.", 100, W - 2 * m, dark=True)
    para(s, (m, y + 16), "Routes are planned each morning and technicians share their location while on a job.", 32, W - 2 * m, col="#E6EFE9")
    br = app("dispatch", W - m, max_h=H - y - 230, h=1500)
    lift(s, br, (m // 2, y + 160), 140)
    foot(s, W, H, m, dark=True)
    out.append(("post-03-dispatch", s))

    s = bg((W, H))
    kick(s, (m, 100), "Humans in the middle", 24)
    y = head2(s, (m, 150), "AI drafts it.", "A person decides.", 108, W - 2 * m)
    para(s, (m, y + 16), "Triage, cost estimates and vendor picks are proposed by AI and approved by a coordinator or the owner — and every step is logged.", 32, W - 2 * m)
    yy = y + 200
    for i, (t, c) in enumerate([("Ticket in", BODY), ("AI triage + cost band", EMERALD_M), ("Coordinator / owner approves", GOLD_TEXT), ("Vendor dispatched", EMERALD_M), ("Logged & exportable", BODY)]):
        ImageDraw.Draw(s).rounded_rectangle([m, yy, W - m, yy + 92], 12, fill=rgb(PAPER), outline=rgb(GOLD, 160), width=2)
        sk.draw_text(s, (m + 30, yy + 24), f"{i + 1}", B.font(44, "bold"), rgb(GOLD_TEXT))
        sk.draw_text(s, (m + 100, yy + 28), t, fira(34, 500), rgb(INK if c == BODY else c))
        yy += 110
    foot(s, W, H, m)
    out.append(("post-04-humans-in-the-middle", s))

    s = shade(photo("hero/tn-int-02.jpg", (W, H)), .3, .97)
    kick(s, (m, 840), "Free rental analysis", 26, GOLD)
    y = head2(s, (m, 890), "What could your", "Tennessee rental earn?", 96, W - 2 * m, dark=True)
    para(s, (m, y + 20), "Free rental analysis: a market rent benchmark, days-to-lease estimate and onboarding plan.", 32, W - 2 * m, col="#E6EFE9")
    out.append(("post-05-rental-analysis", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/posts" / f"{n}.png")


def ig_stories():
    W, H = sk.IG_STORY
    m = 90
    out = []
    s = shade(photo("hero/tn-05.jpg", (W, H)), .2, .92)
    logo(s, m, 140, 70, dark=True)
    y = head2(s, (m, 1080), "It's 2 a.m. in Memphis.", "You don't need to be awake.", 104, W - 2 * m, dark=True)
    para(s, (m, y + 30), "The leak gets triaged, priced and routed. The decision waits for your morning digest, in your time zone.", 44, W - 2 * m, col="#E6EFE9")
    out.append(("story-01-2am", s))

    s = bg((W, H))
    logo(s, m, 140, 70)
    y = head2(s, (m, 380), "Report it.", "Track it.", 130, W - 2 * m)
    ph = mob("tenant-mobile", 1040, top=0)
    lift(s, ph, ((W - ph.size[0]) // 2, y + 70), 80)
    foot(s, W, H, m, 26)
    out.append(("story-02-residents", s))

    s = bg((W, H), "emerald")
    kick(s, (m, 520), "Poll", 32, GOLD)
    y = head(s, (m, 590), "Do you own a rental back home — or here?", 104, W - 2 * m, col=CREAM)
    para(s, (m, 1500), "(Poll sticker space)", 30, W - 2 * m, col="#9FBFAF")
    logo(s, m, H - 220, 70, dark=True)
    out.append(("story-03-poll", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/stories" / f"{n}.png")


def ig_reel():
    W, H = sk.IG_STORY
    m = 90
    sc = []

    def ph_scene(photo_name, a, b_):
        s = shade(photo(photo_name, (W, H)), .15, .92)
        head2(s, (m, 1180), a, b_, 112, W - 2 * m, dark=True)
        return s

    sc.append(sk.Scene(ph_scene("hero/tn-02.jpg", "2:07 a.m.", "Kitchen faucet leaking."), 2.6, zoom=1.08))

    def ui(a, b_, name, top=0, h=1780):
        s = bg((W, H))
        y = head2(s, (m, 260), a, b_, 104, W - 2 * m)
        br = app(name, W - 2 * m + 40, top=top, h=h, right=2000)
        lift(s, br, (m - 20, y + 80), 70)
        foot(s, W, H, m, 26)
        return s

    sc.append(sk.Scene(ui("AI triages it.", "Prices it.", "ticket-detail"), 2.8))
    sc.append(sk.Scene(ui("Dispatch routes", "a technician.", "dispatch"), 2.8))
    sc.append(sk.Scene(ui("You approve", "over breakfast.", "dashboard"), 2.8))
    s = bg((W, H), "emerald")
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 110, dark=True)
    logo(s, (W - lw) / 2, 640, 110, dark=True)
    head(s, (m, 880), "Your U.S. rentals, without the 2 a.m. calls.", 88, W - 2 * m, col=CREAM, align="center")
    para(s, (m, 1240), "Free rental analysis · link in bio", 40, W - 2 * m, col=GOLD, align="center")
    sc.append(sk.Scene(s, 3.2, move="out", zoom=1.05))
    sk.render_video(sc, (W, H), OUT / "instagram/reel-2am-calls-9x16.mp4")
    sk.save(sc[0].frame, OUT / "instagram/reel-cover.png")


# ======================================================================= LINKEDIN

def li_links():
    W, H = sk.LI_LINK
    m = 60
    items = [
        ("link-01-remote-owners", "Your U.S. rentals,", "without the 2 a.m. calls.", "Time-zone-aligned decisions, AI-priced repairs and a full audit trail — for remote and NRI owners.", "dashboard"),
        ("link-02-ai-native", "A multi-agent loop,", "humans in the middle.", "Intake, triage, cost, vendor, dispatch, close — each step proposed by AI and approved by a person.", "ai-decisions"),
        ("link-03-pmc", "Memphis property management,", "on your label.", "One platform for PMCs: staff console, owner and resident portals, vendors and technicians.", "pipeline"),
    ]
    for n, a, b_, line, name in items:
        s = bg((W, H))
        logo(s, m, 50, 34)
        y = head2(s, (m, 130), a, b_, 46, 500)
        para(s, (m, y + 14), line, 20, 470)
        br = app(name, 620, max_h=490, h=1500)
        lift(s, br, (W - 620 - 30, 70), 60)
        sk.save(s, OUT / "linkedin/images" / f"{n}.png")


def li_document():
    W, H = sk.LI_SQUARE
    m = 90
    pages = []

    def page(n, k, a_, b_, text, name, top=0, h=1500, left=SIDEBAR, right=2880):
        s = bg((W, H))
        kick(s, (m, 90), k, 22)
        y = head2(s, (m, 136), a_, b_, 66, W - 2 * m)
        y = para(s, (m, y + 10), text, 28, W - 2 * m)
        br = app(name, W - 2 * m + 40, max_h=H - y - 200, top=top, h=h, left=left, right=right)
        lift(s, br, (m - 20, y + 40))
        logo(s, m, H - 100, 38)
        sk.draw_text(s, (W - m - 50, H - 92), f"{n} / 8", fira(22), rgb("#6B756F"))
        pages.append(s)

    s = shade(photo("hero/tn-15.jpg", (W, H)), .2, .93)
    logo(s, m, 90, 56, dark=True)
    y = head2(s, (m, 640), "One platform,", "seven portals.", 100, W - 2 * m, dark=True)
    para(s, (m, y + 24), "How KPMRentals runs single-family rentals in Memphis — for owners, residents, vendors, technicians and the team in between.", 32, W - 2 * m, col="#E6EFE9")
    pages.append(s)
    page(2, "Owners", "Approve in", "ten seconds.", "Batched decisions in the owner's time zone, each with a default action and a cost band.", "dashboard")
    page(3, "Staff console", "Every ticket,", "one pipeline.", "New, triaged, awaiting owner, dispatched, completed — with AI recommendations attached.", "pipeline")
    page(4, "AI triage", "A recommendation,", "not a decision.", "Severity, trade, cost band and suggested vendor — approved or rejected by a person.", "ticket-detail")
    page(5, "Operations", "Live dispatch", "and routing.", "Technician routes planned each morning; positions shared while on a job.", "dispatch")
    page(6, "Monitoring", "Catch the leak", "before the call.", "Connected sensors and devices raise alerts that can open a ticket on their own.", "monitoring")
    page(7, "Residents", "Pay, report,", "track.", "A resident portal for rent, maintenance requests with photos, notices and lease details.", "tenant-home", h=1700)
    s = bg((W, H), "emerald")
    logo(s, m, 90, 56, dark=True)
    y = head2(s, (m, 360), "Own in Memphis?", "Run a PMC?", 110, W - 2 * m, dark=True)
    para(s, (m, y + 30), "Start with a free rental analysis — or ask about running KPMRentals on your own label.", 34, W - 2 * m, col="#E6EFE9")
    btn(s, m, y + 210, "kpm-rentals.lovable.app", 34, dark=True)
    pages.append(s)
    sk.pdf(pages, OUT / "linkedin/document-seven-portals.pdf")
    for i, p in enumerate(pages, 1):
        sk.save(p, OUT / "linkedin/document-pages" / f"page-{i:02d}.png")


def li_video():
    W, H = sk.LI_VIDEO
    m = 120
    sc = []
    s = shade(photo("hero/tn-01.jpg", (W, H)), .25, .9)
    head2(s, (m, 640), "Owning a rental from far away", "shouldn't feel like this.", 92, W - 2 * m, dark=True)
    sc.append(sk.Scene(s, 3.0, zoom=1.06))

    def feat(k, a_, line, name, h=1500, dark=False):
        s = bg((W, H), "emerald" if dark else "cream")
        kick(s, (m, 300), k, 26, GOLD if dark else GOLD_TEXT)
        y = head(s, (m, 350), a_, 76, 620, col=CREAM if dark else INK)
        para(s, (m, y + 20), line, 32, 600, col="#E6EFE9" if dark else BODY)
        logo(s, m, H - 160, 52, dark=dark)
        br = app(name, 1060, max_h=900, h=h)
        lift(s, br, (W - 1060 - 80, (H - br.size[1]) // 2), 120 if dark else 70)
        return s

    sc.append(sk.Scene(feat("Owners", "Decisions in your time zone.", "A default action and a cost band on every memo.", "dashboard"), 3.6))
    sc.append(sk.Scene(feat("AI triage", "A recommendation, not a decision.", "Severity, trade, cost band, vendor — approved by a person.", "ticket-detail"), 3.6))
    sc.append(sk.Scene(feat("Dispatch", "A technician, already routed.", "Daily routes and live job status.", "dispatch", dark=True), 3.6))
    sc.append(sk.Scene(feat("Residents", "Pay, report, track.", "Rent and repairs from one portal.", "tenant-home", h=1700), 3.6))
    s = bg((W, H), "emerald")
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 100, dark=True)
    logo(s, (W - lw) / 2, 330, 100, dark=True)
    sk.block(s, (m, 520), "Your U.S. rentals, without the 2 a.m. calls.", B.font(76, "bold"), rgb(CREAM), W - 2 * m, align="center")
    sk.block(s, (m, 680), "Memphis-first property management · free rental analysis at kpm-rentals.lovable.app", fira(34), rgb(GOLD), W - 2 * m, align="center")
    sc.append(sk.Scene(s, 4, move="out", zoom=1.04))
    sk.render_video(sc, (W, H), OUT / "linkedin/video-remote-owners-16x9.mp4")
    sk.save(sc[1].frame, OUT / "linkedin/video-cover.png")


if __name__ == "__main__":
    ig_carousel_owners()
    ig_posts()
    ig_stories()
    li_links()
    li_document()
    if not args.no_video:
        ig_reel()
        li_video()
    print("done →", OUT)
