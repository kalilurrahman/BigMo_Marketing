"""LakshyaPrep — launch social campaign (Instagram + LinkedIn).

Source of truth for copy/visuals: academy-kpm-spark/brand/01-brand-guidelines.md
(Broadsheet newsprint system, Source Serif 4, misregistration on display type,
cyan = CTA, magenta = reward/emphasis, yellow print/social only).

Run:  python3 campaigns/lakshyaprep/build.py  [--src ../academy-kpm-spark]
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import socialkit as sk  # noqa: E402
from PIL import ImageDraw  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--src", default=str(HERE.parents[2] / "academy-kpm-spark"))
args = ap.parse_args()
SRC = Path(args.src)
OUT = HERE / "output"
SHOTS = SRC / "docs/master/assets/mobile"
FULL = SRC / "docs/evidence/full-tests"

B = sk.Brand(
    name="LakshyaPrep", bg="#F3F2F2", surface="#EAE9E9", ink="#201E1D", muted="#605D5D",
    primary="#0088B0", accent="#D6006C", highlight="#EDBB00", dark_bg="#17151A",
    dark_ink="#F3F2F2", misreg=True, url="lakshyaprep.com", handle="@lakshyaprep",
    footer="LakshyaPrep is a BigMo company.", tracking=-0.045,
)
CYAN_TEXT, NIGHT_CYAN, NIGHT_MAG = "#006786", "#38A6CF", "#FF458E"
RISO_BG = "#FFDEE6"
ink = sk.hex2rgb(B.ink, 255)
paper = sk.hex2rgb(B.bg, 255)


# ------------------------------------------------------------- brand pieces

def mark(img, cx, cy, r, dark=False):
    """L1 off-register bullseye: cyan + magenta rings offset, yellow inner ring, ink dot."""
    lay = sk.Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    w = max(3, int(r * 0.26))
    o = max(1, int(r * 0.06))
    d.ellipse([cx - r - o, cy - r, cx + r - o, cy + r], outline=sk.hex2rgb(B.primary, 230), width=w)
    d.ellipse([cx - r + o, cy - r + o, cx + r + o, cy + r + o], outline=sk.hex2rgb(B.accent, 200), width=w)
    ri = r * 0.55
    d.ellipse([cx - ri, cy - ri, cx + ri, cy + ri], outline=sk.hex2rgb(B.highlight, 255), width=max(2, int(r * 0.12)))
    rd = r * 0.26
    d.ellipse([cx - rd, cy - rd, cx + rd, cy + rd], fill=sk.hex2rgb(B.dark_ink if dark else B.ink, 255))
    img.alpha_composite(lay)


def logo(img, x, y, h, dark=False):
    """Mark + 'Lakshya' (600) + 'Prep' (italic). Returns width."""
    col = sk.hex2rgb(B.dark_ink if dark else B.ink, 255)
    r = h * 0.42
    mark(img, int(x + r), int(y + h / 2), int(r), dark)
    fb, fi = B.font(int(h * 0.78), "bold"), B.font(int(h * 0.78), "italic")
    tx = x + r * 2 + h * 0.28
    ty = y + h * 0.02
    w1 = sk.draw_text(img, (tx, ty), "Lakshya", fb, col, tracking_px=-h * 0.02)
    w2 = sk.draw_text(img, (tx + w1, ty), "Prep", fi, col)
    return tx + w1 + w2 - x


def display(img, xy, s, size, max_w, colour=None, style="bold", dark=False, misreg=True, lh=0.98, align="left"):
    f = B.font(size, style)
    col = sk.hex2rgb(colour, 255) if colour else sk.hex2rgb(B.dark_ink if dark else B.ink, 255)
    sh = sk.misreg_shadow(B, size / 90) if misreg else None
    if sh and dark:
        sh = [((-max(2, size // 30), 0), sk.hex2rgb(NIGHT_CYAN, 200)), ((max(2, size // 30), size // 60), sk.hex2rgb(NIGHT_MAG, 190))]
    return sk.block(img, xy, s, f, col, max_w, line_h=lh, tracking_px=size * B.tracking, shadow=sh, align=align)


def body(img, xy, s, size, max_w, dark=False, colour=None, style="regular", lh=1.38, align="left"):
    col = sk.hex2rgb(colour or (B.dark_ink if dark else B.muted), 255)
    return sk.block(img, xy, s, B.font(size, style), col, max_w, line_h=lh, align=align)


def cta(img, x, y, s, size=34, dark=False, outline=False):
    f = B.font(size, "bold")
    if outline:
        c = B.dark_ink if dark else B.ink
        return sk.pill(img, (x, y), s, f, c, None, pad=(int(size * .8), int(size * .5)), radius=3, outline=c)
    return sk.pill(img, (x, y), s, f, "#FFFFFF", NIGHT_CYAN if dark else B.primary,
                   pad=(int(size * .8), int(size * .5)), radius=3)


def masthead(img, W, y, left="SAT · ACT · MCAT", mid="GOAL-BASED PREP", right="LIVE 1:1 + GOALGAP", dark=False, m=72, scale=1.0):
    c = sk.hex2rgb(B.dark_ink if dark else B.ink, 255)
    sk.double_rule(img, m, W - m, y, c, scale)
    f = B.font(int(20 * scale), "bold")
    ty = y + int(26 * scale)
    tr = 20 * scale * 0.12
    sk.draw_text(img, (m, ty), left, f, c, tr)
    mw = sk.text_width(f, mid, tr)
    sk.draw_text(img, ((W - mw) / 2, ty), mid, f, c, tr)
    rw = sk.text_width(f, right, tr)
    sk.draw_text(img, (W - m - rw, ty), right, f, c, tr)
    ImageDraw.Draw(img).rectangle([m, ty + int(36 * scale), W - m, ty + int(37.5 * scale)], fill=c)


def footer(img, W, H, dark=False, m=72, page=None, size=22):
    c = sk.hex2rgb(B.dark_ink if dark else B.muted, 255)
    f = B.font(size, "regular")
    y = H - m + 4
    sk.draw_text(img, (m, y), B.url, f, c)
    s = page or B.handle
    sk.draw_text(img, (W - m - sk.text_width(f, s), y), s, f, c)


def hype(img, xy, s, size, max_w, dark=False):
    return sk.block(img, xy, s, B.font(size, "italic"), sk.hex2rgb(NIGHT_MAG if dark else B.accent, 255), max_w, line_h=1.05)


# screenshots (crop the "payments in test mode" banner + floating widgets)
def desk(name, folder=SHOTS, bottom=0):
    return sk.load_shot(folder / name, crop_top=37, crop_bottom=bottom)


def mob(name, bottom=120):
    return sk.load_shot(SHOTS / name, crop_top=58, crop_bottom=bottom)


def phone_shot(name, h, bottom=120):
    return sk.phone(mob(name, bottom), h)


def bg(size, dark=False, colour=None):
    return sk.grain(sk.canvas(size, colour or (B.dark_bg if dark else B.bg)), seed=size[1])


def goal_meter(img, x, y, w, scale=1.0, dark=False, frm="1180", to="1450", progress=0.42, note=True):
    """The hero 'points to goal' meter. Example numbers are always labelled as such."""
    c_ink = B.dark_ink if dark else B.ink
    c_mut = "#BAB6B6" if dark else B.muted
    sk.kicker(img, (x, y), "Goal locked · SAT", B, int(22 * scale), c_mut)
    lv = B.font(int(24 * scale), "regular")
    s = "Lv 2 Archer"
    sk.draw_text(img, (x + w - sk.text_width(lv, s), y), s, lv, sk.hex2rgb(NIGHT_MAG if dark else B.accent, 255))
    yy = y + int(60 * scale)
    f1 = B.font(int(80 * scale), "regular")
    a = sk.draw_text(img, (x, yy + int(40 * scale)), frm, f1, sk.hex2rgb(c_mut, 255))
    sk.draw_text(img, (x + a + int(26 * scale), yy + int(48 * scale)), "→", sk.ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", int(56 * scale)), sk.hex2rgb(c_ink, 255))
    display(img, (x + a + int(110 * scale), yy), to, int(150 * scale), w, colour=c_ink, dark=dark)
    by = yy + int(190 * scale)
    d = ImageDraw.Draw(img)
    d.rectangle([x, by, x + w, by + int(16 * scale)], fill="#3A363D" if dark else "#D7D3D3")
    d.rectangle([x, by, x + int(w * progress), by + int(16 * scale)], fill=NIGHT_CYAN if dark else B.primary)
    fs = B.font(int(28 * scale))
    ty = by + int(40 * scale)
    sk.draw_text(img, (x, ty), "156 to go", B.font(int(28 * scale), "bold"), sk.hex2rgb(c_ink, 255))
    s2 = "Week 5 of 12"
    sk.draw_text(img, (x + (w - sk.text_width(fs, s2)) / 2, ty), s2, fs, sk.hex2rgb(c_ink, 255))
    s3 = "12-day streak"
    sk.draw_text(img, (x + w - sk.text_width(fs, s3), ty), s3, fs, sk.hex2rgb(NIGHT_MAG if dark else B.accent, 255))
    if note:
        sk.draw_text(img, (x, ty + int(60 * scale)), "Example numbers for illustration only.",
                     B.font(int(20 * scale), "italic"), sk.hex2rgb(c_mut, 255))
    return ty + int(90 * scale)


# ======================================================================= INSTAGRAM

def ig_carousel_method():
    """7-slide 4:5 carousel: The Lakshya Method."""
    W, H = sk.IG_PORTRAIT
    m = 80
    slides = []

    s = bg((W, H))
    masthead(s, W, 70, mid="THE LAKSHYA METHOD", right="No. 01")
    sk.kicker(s, (m, 250), "Swipe · 4 steps", B, 26, B.accent)
    y = display(s, (m, 320), "One goal.", 190, W - 2 * m)
    y = display(s, (m, y), "Zero noise.", 190, W - 2 * m, colour=B.accent, style="italic", misreg=False)
    body(s, (m, y + 50), "Stop studying everything. Study what moves your score.", 40, W - 2 * m - 80)
    mark(s, W - m - 90, H - 260, 90)
    logo(s, m, H - 170, 58)
    slides.append(s)

    steps = [
        ("01", "Scan", "A 20-question adaptive scan finds where your points leak.", "scoregap-diagnostic-390.png", "scan"),
        ("02", "Lock", "Goal score + test date in. Week-by-week route out.", "scoregap-start-390.png", "lock"),
        ("03", "Grind", "1:1 sessions, drills and timed mocks. Re-planned weekly.", "test-run-390.png", "grind"),
        ("04", "Land", "Test day with a rehearsed pacing plan. Go land it.", "tests-free-390.png", "land"),
    ]
    for n, word, line, shot, _ in steps:
        s = bg((W, H))
        masthead(s, W, 70, mid="THE LAKSHYA METHOD", right=f"STEP {n} / 04")
        display(s, (m, 200), n, 110, 300, colour=B.primary, misreg=False)
        display(s, (m + 170, 200), word + ".", 150, W - 2 * m)
        body(s, (m, 390), line, 40, W - 2 * m, colour=B.ink)
        ph = phone_shot(shot, 700, bottom=140 if shot != "scoregap-diagnostic-390.png" else 300)
        sk.shadow_paste(s, ph, ((W - ph.size[0]) // 2, 520), opacity=80)
        footer(s, W, H, page=f"{int(n) + 1} / 7")
        slides.append(s)

    s = bg((W, H))
    masthead(s, W, 70, mid="GOALGAP", right="WHY IT WORKS")
    y = display(s, (m, 220), "Points, not percent.", 110, W - 2 * m)
    body(s, (m, y + 30), "GoalGap ranks your weak skills by the score points they can still give you — not by how often you miss them. So every hour goes where the points are.", 36, W - 2 * m)
    br = sk.cap(sk.browser(desk("practice-skill-1280.png"), W - 2 * m + 40, url="lakshyaprep.com/scoregap"), 520)
    sk.shadow_paste(s, br, (m - 20, 680), radius=14)
    footer(s, W, H, page="6 / 7")
    slides.append(s)

    s = bg((W, H), dark=True)
    masthead(s, W, 70, dark=True, mid="YOUR MOVE", right="FREE")
    y = display(s, (m, 260), "Lock the goal.", 140, W - 2 * m, dark=True)
    y = display(s, (m, y), "Own the score.", 140, W - 2 * m, colour=NIGHT_MAG, style="italic", dark=True, misreg=False)
    body(s, (m, y + 50), "Take the free scan. Pick one number. We build the route and re-plan it after every session.", 38, W - 2 * m, dark=True)
    cta(s, m, y + 300, "Lock my goal", 40, dark=True)
    cta(s, m + 360, y + 300, "Take the free scan", 40, dark=True, outline=True)
    logo(s, m, H - 180, 60, dark=True)
    sk.draw_text(s, (m, H - 100), "Link in bio · " + B.url, B.font(26), sk.hex2rgb("#BAB6B6", 255))
    slides.append(s)

    for i, s in enumerate(slides, 1):
        sk.save(s, OUT / "instagram/carousel-method" / f"slide-{i:02d}.png")
    return slides


def ig_posts():
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    # 1 hero meter
    s = bg((W, H))
    masthead(s, W, 70)
    display(s, (m, 200), "Main character score.", 120, W - 2 * m)
    goal_meter(s, m, 560, W - 2 * m, scale=1.25)
    hype(s, (m, 1040), "Every point, tracked. Re-planned until you land it.", 40, W - 2 * m)
    logo(s, m, H - 150, 54)
    out.append(("post-01-main-character-score", s))

    # 2-4 exam taglines
    exams = [
        ("sat", "1600 is a target,", "not a vibe.", "SAT", FULL / "sat-04-report.png", "Digital SAT · Reading & Writing + Math"),
        ("act", "36,", "locked in.", "ACT", FULL / "act-04-report.png", "English · Math · Reading · Science"),
        ("mcat", "Aim for the", "white coat.", "MCAT", FULL / "mcat-04-report.png", "Full-length mocks · section-level estimates"),
    ]
    for key, l1, l2, ex, shot, sub in exams:
        s = bg((W, H), colour=RISO_BG if key == "act" else None)
        masthead(s, W, 70, left=ex, mid="GOAL-BASED PREP", right="LAKSHYAPREP")
        y = display(s, (m, 210), l1, 128, W - 2 * m)
        y = display(s, (m, y), l2, 128, W - 2 * m, colour=B.accent, style="italic", misreg=False)
        body(s, (m, y + 24), sub, 32, W - 2 * m)
        br = sk.browser(sk.load_shot(shot, crop_top=40, crop_bottom=60), W - 2 * m + 60, url="lakshyaprep.com/scoregap/tests")
        sk.shadow_paste(s, sk.cap(br, H - 230 - (y + 110)), (m - 30, y + 90))
        cta(s, m, H - 170, "Take the free scan", 32)
        mark(s, W - m - 50, H - 135, 46)
        out.append((f"post-0{len(out) + 1}-{key}", s))

    # 5 parents — exam hall feel
    s = bg((W, H), colour="#F8F4F4")
    sk.kicker(s, (m, 110), "For parents", B, 26, CYAN_TEXT)
    y = display(s, (m, 170), "See the plan. Not just the bill.", 104, W - 2 * m, misreg=False)
    body(s, (m, y + 30), "One dashboard for every child: goals, sessions, progress reports and invoices. Sibling discounts apply automatically.", 34, W - 2 * m, colour=B.ink)
    br = sk.browser(desk("parent-dashboard-1280.png"), W - 2 * m + 60, url="lakshyaprep.com/parent")
    sk.shadow_paste(s, sk.cap(br, 430), (m - 30, 640))
    logo(s, m, H - 140, 54)
    out.append(("post-05-parents", s))

    for name, s in out:
        sk.save(s, OUT / "instagram/posts" / f"{name}.png")
    return out


def ig_stories():
    W, H = sk.IG_STORY
    m = 90
    out = []

    s = bg((W, H), dark=True)
    masthead(s, W, 160, dark=True, m=m)
    sk.kicker(s, (m, 330), "POV", B, 34, NIGHT_MAG)
    y = display(s, (m, 390), "You stopped studying everything.", 140, W - 2 * m, dark=True)
    ph = phone_shot("home-390.png", 780)
    sk.shadow_paste(s, ph, ((W - ph.size[0]) // 2, y + 60), opacity=120)
    cta(s, m, H - 200, "Take the free scan", 40, dark=True)
    out.append(("story-01-pov", s))

    s = bg((W, H))
    masthead(s, W, 160, m=m)
    y = display(s, (m, 330), "20 questions.", 150, W - 2 * m)
    y = display(s, (m, y), "Your whole map.", 130, W - 2 * m, colour=B.accent, style="italic", misreg=False)
    body(s, (m, y + 30), "The free scan shows where your points leak — before you spend a single hour.", 42, W - 2 * m)
    ph = phone_shot("test-run-390.png", 760)
    sk.shadow_paste(s, ph, ((W - ph.size[0]) // 2, y + 190), opacity=90)
    cta(s, m, H - 190, "Take the free scan", 40)
    out.append(("story-02-free-scan", s))

    s = bg((W, H), colour=RISO_BG)
    masthead(s, W, 160, m=m, mid="TEST EVE", right="No. 04")
    y = display(s, (m, 420), "You've done the reps.", 140, W - 2 * m)
    y = display(s, (m, y + 10), "Go land it.", 170, W - 2 * m, colour=B.accent, style="italic", misreg=False)
    mark(s, W // 2, y + 420, 230)
    logo(s, m, H - 300, 70)
    sk.draw_text(s, (m, H - 200), "Lock the goal. Own the score.", B.font(40, "italic"), ink)
    out.append(("story-03-test-eve", s))

    for name, s in out:
        sk.save(s, OUT / "instagram/stories" / f"{name}.png")
    return out


def ig_reel():
    """15s 9:16 reel, per brand kit §9 reel script."""
    W, H = sk.IG_STORY
    m = 90
    sc = []

    def card(lines, dark=True, sub=None, shot=None, sizes=(170,)):
        s = bg((W, H), dark=dark)
        masthead(s, W, 160, dark=dark, m=m)
        y = 420 if shot else 640
        for i, (t, style, col) in enumerate(lines):
            y = display(s, (m, y), t, sizes[min(i, len(sizes) - 1)], W - 2 * m, dark=dark, style=style,
                        colour=col, misreg=style == "bold")
        if sub:
            y = body(s, (m, y + 20), sub, 44, W - 2 * m, dark=dark)
        if shot:
            ph = phone_shot(shot, 900)
            sk.shadow_paste(s, ph, ((W - ph.size[0]) // 2, y + 60), opacity=120)
        return s

    sc.append(sk.Scene(card([("POV:", "italic", NIGHT_MAG), ("you stopped studying everything.", "bold", None)], sizes=(120, 140)), 2.4))
    sc.append(sk.Scene(card([("Scan:", "italic", NIGHT_MAG), ("20 Qs.", "bold", None)], shot="scoregap-diagnostic-390.png", sizes=(110, 170)), 2.6))
    sc.append(sk.Scene(card([("Lock:", "italic", NIGHT_MAG), ("1450 by March.", "bold", None)], shot="scoregap-start-390.png", sizes=(110, 150)), 2.8))
    s = bg((W, H), dark=True)
    masthead(s, W, 160, dark=True, m=m)
    sk.kicker(s, (m, 520), "Grind + Land", B, 34, NIGHT_MAG)
    goal_meter(s, m, 640, W - 2 * m, scale=1.4, dark=True)
    sc.append(sk.Scene(s, 3.4, zoom=1.08))
    s = bg((W, H))
    mark(s, W // 2, 560, 190)
    y = display(s, (m, 840), "Lock the goal.", 140, W - 2 * m, align="center")
    y = display(s, (m, y), "Own the score.", 140, W - 2 * m, colour=B.accent, style="italic", misreg=False, align="center")
    lw = logo(sk.canvas((10, 10), B.bg), 0, 0, 80)
    logo(s, (W - lw) / 2, y + 120, 80)
    sk.block(s, (m, y + 260), "Take the free scan · " + B.url, B.font(40), ink, W - 2 * m, align="center")
    sc.append(sk.Scene(s, 3.6, move="out", zoom=1.05))
    sk.render_video(sc, (W, H), OUT / "instagram/reel-lock-the-goal-9x16.mp4")
    sk.save(sc[0].frame, OUT / "instagram/reel-cover.png")


# ======================================================================= LINKEDIN

def li_links():
    W, H = sk.LI_LINK
    m = 64
    out = []
    s = bg((W, H))
    y = display(s, (m, 90), "Lock the goal.", 92, 560)
    y = display(s, (m, y), "Own the score.", 92, 560, colour=B.accent, style="italic", misreg=False)
    body(s, (m, y + 24), "Goal-based SAT, ACT and MCAT prep: live 1:1 coaching + GoalGap diagnostics.", 26, 520)
    logo(s, m, H - 100, 44)
    br = sk.browser(desk("home-1280.png", bottom=70), 560, url="lakshyaprep.com")
    sk.shadow_paste(s, br, (W - 560 - 40, 110))
    out.append(("link-01-launch", s))

    s = bg((W, H), colour="#F8F4F4")
    sk.kicker(s, (m, 70), "How GoalGap prioritises", B, 20, CYAN_TEXT)
    y = display(s, (m, 110), "Rank skills by points available.", 66, 520, misreg=False)
    body(s, (m, y + 20), "Not by percentage wrong. Every study hour goes where the score can still move.", 26, 500, colour=B.ink)
    logo(s, m, H - 100, 44)
    br = sk.browser(desk("practice-skill-1280.png"), 580, url="lakshyaprep.com/scoregap")
    sk.shadow_paste(s, br, (W - 580 - 40, 100))
    out.append(("link-02-goalgap", s))

    s = bg((W, H), dark=True)
    sk.kicker(s, (m, 70), "Full-length mocks · SAT · ACT · MCAT", B, 20, NIGHT_MAG)
    y = display(s, (m, 110), "Real timing. Honest ranges.", 70, 520, dark=True)
    body(s, (m, y + 20), "Section-level score estimates as a range, a review of every miss, and timing by question type.", 26, 500, dark=True)
    logo(s, m, H - 100, 44, dark=True)
    br = sk.browser(sk.load_shot(FULL / "sat-04-report.png", 40, 60), 580, url="lakshyaprep.com/scoregap/tests", chrome="#2A272D")
    sk.shadow_paste(s, br, (W - 580 - 40, 100), opacity=140)
    out.append(("link-03-mocks", s))

    for n, s in out:
        sk.save(s, OUT / "linkedin/images" / f"{n}.png")


def li_document():
    """8-page 1:1 document carousel (upload as PDF) for parents & counselors."""
    W, H = sk.LI_SQUARE
    m = 90
    pages = []
    exam_bg = "#F8F4F4"

    def page(title, text, shot=None, k="", n=0, dark=False, shot_kind="desk"):
        s = bg((W, H), dark=dark, colour=None if dark else exam_bg)
        sk.kicker(s, (m, 90), k, B, 22, NIGHT_MAG if dark else CYAN_TEXT)
        y = display(s, (m, 140), title, 74, W - 2 * m, dark=dark, misreg=False)
        y = body(s, (m, y + 16), text, 30, W - 2 * m, dark=dark, colour=None if dark else B.ink)
        if shot is not None:
            if shot_kind == "desk":
                br = sk.browser(shot, W - 2 * m, url="lakshyaprep.com")
                sk.shadow_paste(s, br, (m, max(y + 40, H - br.size[1] - 130)))
            else:
                sk.shadow_paste(s, shot, ((W - shot.size[0]) // 2, y + 40))
        logo(s, m, H - 90, 36, dark=dark)
        f = B.font(22)
        pn = f"{n} / 8"
        sk.draw_text(s, (W - m - sk.text_width(f, pn), H - 84), pn, f, sk.hex2rgb(B.dark_ink if dark else B.muted, 255))
        pages.append(s)

    s = bg((W, H))
    masthead(s, W, 90, m=m, mid="A GUIDE FOR FAMILIES", right="2026")
    y = display(s, (m, 260), "SAT, ACT, MCAT:", 110, W - 2 * m)
    y = display(s, (m, y), "prep that starts with one number.", 96, W - 2 * m, colour=B.accent, style="italic", misreg=False)
    body(s, (m, y + 40), "How goal-based preparation works — in 7 pages.", 36, W - 2 * m)
    logo(s, m, H - 150, 60)
    pages.append(s)
    page("The problem: too much, aimed at nothing.", "More practice books, more tabs, more tips. Students work hard on skills that barely move their score.", k="01 · The noise", n=2, shot=desk("tests-free-1280.png", bottom=80))
    page("Step 1 — Scan.", "A short adaptive diagnostic shows where points are leaking, by skill and by section.", k="02 · Scan", n=3, shot=desk("scoregap-diagnostic-1280.png", bottom=120))
    page("Step 2 — Lock.", "The student sets a goal score and test date. GoalGap turns that into a week-by-week route.", k="03 · Lock", n=4, shot=desk("scoregap-start-1280.png", bottom=120))
    page("Step 3 — Grind.", "Live 1:1 sessions, targeted drills, timed full-length mocks. The plan is re-built weekly from real results.", k="04 · Grind", n=5, shot=sk.load_shot(FULL / "sat-02-question.png", 40, 0))
    page("Step 4 — Land.", "Every miss flows into a review log and spaced repetition. Test day comes with a rehearsed pacing plan.", k="05 · Land", n=6, shot=sk.load_shot(FULL / "sat-04-report.png", 40, 60))
    page("Parents see the whole picture.", "Goals, sessions, progress reports and billing for every child in one place. AI support stays a starting point — a human coach reviews it.", k="06 · For parents", n=7, shot=desk("parent-dashboard-1280.png", bottom=100))
    s = bg((W, H), dark=True)
    y = display(s, (m, 240), "Lock the goal.", 120, W - 2 * m, dark=True)
    y = display(s, (m, y), "Own the score.", 120, W - 2 * m, colour=NIGHT_MAG, style="italic", dark=True, misreg=False)
    body(s, (m, y + 40), "Start with the free scan at " + B.url, 38, W - 2 * m, dark=True)
    cta(s, m, y + 170, "Take the free scan", 40, dark=True)
    logo(s, m, H - 150, 56, dark=True)
    sk.draw_text(s, (m, H - 70), B.footer, B.font(22, "italic"), sk.hex2rgb("#BAB6B6", 255))
    pages.append(s)

    sk.pdf(pages, OUT / "linkedin/document-carousel-families.pdf")
    for i, p in enumerate(pages, 1):
        sk.save(p, OUT / "linkedin/document-pages" / f"page-{i:02d}.png")


def li_video():
    """~30s 16:9 product film for LinkedIn feed."""
    W, H = sk.LI_VIDEO
    m = 120
    sc = []

    def title(lines, dark=False, k=None):
        s = bg((W, H), dark=dark)
        masthead(s, W, 90, dark=dark, m=m, scale=1.3)
        y = 360
        if k:
            sk.kicker(s, (m, y - 70), k, B, 30, NIGHT_MAG if dark else B.accent)
        for t, style in lines:
            y = display(s, (m, y), t, 150, W - 2 * m, dark=dark, style=style,
                        colour=(NIGHT_MAG if dark else B.accent) if style == "italic" else None, misreg=style == "bold")
        return s

    def feature(k, t, line, shot, dark=False):
        s = bg((W, H), dark=dark)
        sk.kicker(s, (m, 200), k, B, 28, NIGHT_MAG if dark else B.accent)
        y = display(s, (m, 250), t, 96, 640, dark=dark)
        body(s, (m, y + 30), line, 38, 620, dark=dark)
        br = sk.browser(shot, 1000, url="lakshyaprep.com", chrome="#2A272D" if dark else "#E4E2E2")
        sk.shadow_paste(s, br, (W - 1000 - 90, (H - br.size[1]) // 2 + 20), opacity=120 if dark else 70)
        logo(s, m, H - 150, 52, dark=dark)
        return s

    sc.append(sk.Scene(title([("Everyone tells you", "bold"), ("to do more.", "italic")], dark=True), 3.0))
    sc.append(sk.Scene(title([("We do the opposite.", "bold"), ("One goal.", "italic")]), 3.0))
    sc.append(sk.Scene(feature("01 · Scan", "Find the leak.", "An adaptive scan shows where points are lost.", desk("home-1280.png", bottom=70)), 4.0))
    sc.append(sk.Scene(feature("02 · Lock", "Set the number.", "Goal score + date in. A week-by-week route out.", desk("scoregap-start-1280.png", bottom=120)), 4.0))
    sc.append(sk.Scene(feature("03 · Grind", "Practise what pays.", "Live 1:1 sessions and timed, full-length mocks.", sk.load_shot(FULL / "sat-02-question.png", 40, 0)), 4.0))
    sc.append(sk.Scene(feature("04 · Land", "Review every miss.", "Score ranges by section and a log of every wrong answer.", sk.load_shot(FULL / "sat-04-report.png", 40, 60), dark=True), 4.0))
    s = bg((W, H))
    goal_meter(s, 480, 330, 960, scale=1.5)
    sc.append(sk.Scene(s, 3.5, zoom=1.08))
    s = bg((W, H), dark=True)
    mark(s, W // 2, 300, 120, dark=True)
    y = display(s, (m, 470), "Lock the goal. Own the score.", 110, W - 2 * m, dark=True, align="center")
    sk.block(s, (m, y + 40), "SAT · ACT · MCAT   —   Take the free scan at " + B.url, B.font(42), sk.hex2rgb(B.dark_ink, 255), W - 2 * m, align="center")
    sk.block(s, (m, H - 120), B.footer, B.font(28, "italic"), sk.hex2rgb("#BAB6B6", 255), W - 2 * m, align="center")
    sc.append(sk.Scene(s, 4.0, move="out", zoom=1.04))
    sk.render_video(sc, (W, H), OUT / "linkedin/video-product-film-16x9.mp4")
    sk.save(sc[2].frame, OUT / "linkedin/video-cover.png")


if __name__ == "__main__":
    ig_carousel_method()
    ig_posts()
    ig_stories()
    li_links()
    li_document()
    ig_reel()
    li_video()
    print("done →", OUT)
