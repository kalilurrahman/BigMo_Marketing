"""Swaad (niche-ecommerce-flow) — "The South Indian counter, shipped." campaign.

Two tracks:
  Instagram  — consumer: Swaad, handmade South Indian sweets, savouries, podis,
               pickles and millets from a Chennai kitchen, shipped across the US.
               Led by the catalog's own generated product art + the Deepavali deadline.
  LinkedIn   — BigMo's niche-commerce operating flow underneath it
               (Order → Demand → Production → Supply → Fulfilment → Delivery, AI ops copilot).

Claims discipline (from src/lib/brand-config.ts and catalog/):
  * never "organic" and never "Made in USA" — nothing is certified organic and
    everything is made in Chennai. The repo's screenshots predate that fix and
    still say "Organic Indian Sweets" in the header, so headers are cropped off.
  * prices are admin-editable placeholders — no price is quoted in copy.
  * no health claims (e.g. glycemic index), no delivery-speed or free-shipping promises.
  * festival dates come from catalog/festivals.mjs (each entry is sourced there).

Product art is rasterised from public/product-art/<SKU>.svg with the bundled
Chromium into .cache/art (git-ignored).

Run:  python3 campaigns/swaad/build.py [--src ../niche-ecommerce-flow] [--no-video]
"""
import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import socialkit as sk  # noqa: E402
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--src", default=str(HERE.parents[2] / "niche-ecommerce-flow"))
ap.add_argument("--no-video", action="store_true")
args = ap.parse_args()
SRC = Path(args.src)
OUT = HERE / "output"
CACHE = HERE / ".cache/art"
SHOTS = SRC / "screenshots/out"
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")

FONTS = HERE.parents[1] / "tools/fonts"
INTER = "/usr/share/fonts/opentype/inter/"
B = sk.Brand(
    name="Swaad", bg="#FBF5EA", surface="#FFFFFF", ink="#22201C", muted="#5E574D",
    primary="#087B61", accent="#8A4A1C", font_regular=INTER + "Inter-Regular.otf",
    font_bold=str(FONTS / "SourceSerif4-600-normal.ttf"), font_italic=str(FONTS / "SourceSerif4-400-italic.ttf"),
    url="ecommerce-store.big-mo.ai", handle="@swaad", tracking=-0.02,
)
CREAM, CREAM2, WHITE, INK, BODY = "#FBF5EA", "#F4EAD8", "#FFFFFF", "#22201C", "#5E574D"
GREEN, GREEN_D, KARUPATTI, HALDI, CHILLI = "#087B61", "#05503F", "#8A4A1C", "#E2A33A", "#A5321A"
TAMIL = str(FONTS / "NotoSerifTamil-600.ttf")

CAT = json.loads((HERE / "assets/catalog.json").read_text())
P = {p["sku"]: p for p in CAT["products"]}
COLL = {c["id"]: c for c in CAT["collections"]}

# Festival dates as in catalog/festivals.mjs (each sourced in that file).
FESTIVALS = [("Navaratri", "9 Oct"), ("Vijayadashami & Ayudha Puja", "20 Oct"), ("Deepavali", "8 Nov"),
             ("Karthigai Deepam", "24 Nov"), ("Thai Pongal", "15 Jan"), ("Tamil Puthandu", "14 Apr")]


def rgb(h, a=255):
    return sk.hex2rgb(h, a)


# ------------------------------------------------------------- art

def ensure_art(skus):
    CACHE.mkdir(parents=True, exist_ok=True)
    todo = [s for s in skus if not (CACHE / f"{s}.png").exists()]

    def one(s):
        svg = SRC / "public/product-art" / f"{s}.svg"
        subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1.5", "--window-size=800,800",
                        f"--user-data-dir=/tmp/sk-chrome-{s}", f"--screenshot={CACHE / (s + '.png')}",
                        svg.as_uri()], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)

    with ThreadPoolExecutor(6) as ex:
        list(ex.map(one, todo))


def art(sku, size, radius=None):
    im = Image.open(CACHE / f"{sku}.png").convert("RGB").resize((size, size), Image.LANCZOS)
    return sk.rounded(im, int(size * .06) if radius is None else radius).convert("RGBA")


def plate(sku, size):
    """Just the round plate from the art (circle crop), for collage use."""
    im = Image.open(CACHE / f"{sku}.png").convert("RGB")
    w = im.size[0]
    m = int(w * .14)
    im = im.crop((m, m, w - m, w - m)).resize((size, size), Image.LANCZOS).convert("RGBA")
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, size - 1, size - 1], fill=255)
    im.putalpha(mask)
    return im


# ------------------------------------------------------------- brand pieces

def bg(size, kind="cream"):
    """Cream ground with a faint kolam dot grid; 'green' for brand slides; 'warm' for festival."""
    W, H = size
    base = {"cream": CREAM, "green": GREEN_D, "warm": "#F7E3C3", "karupatti": "#3B2416"}[kind]
    g = sk.canvas(size, base)
    lay = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    step = max(28, W // 30)
    dot = rgb(WHITE, 26) if kind in ("green", "karupatti") else rgb(KARUPATTI, 26)
    r = max(1.5, W / 700)
    for yy in range(step // 2, H, step):
        for xx in range(step // 2 + (step // 2 if (yy // step) % 2 else 0), W, step):
            d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=dot)
    g.alpha_composite(lay)
    return g


def logo(img, x, y, h, dark=False):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([x, y, x + h, y + h], int(h * .2), fill=rgb(WHITE if dark else GREEN))
    f = B.font(int(h * .62), "bold")
    sw = f.getlength("S")
    d.text((x + (h - sw) / 2, y + h * .1), "S", font=f, fill=rgb(GREEN if dark else WHITE))
    fw = B.font(int(h * .62), "bold")
    w = sk.draw_text(img, (x + h * 1.25, y - h * .04), "Swaad", fw, rgb(WHITE if dark else INK))
    sk.draw_text(img, (x + h * 1.27, y + h * .64), "South Indian Sweets", ImageFont.truetype(INTER + "Inter-Medium.otf", max(10, int(h * .26))),
                 rgb("#CFE5DD" if dark else BODY))
    return h * 1.25 + w


def tamil(img, xy, s, size, col=KARUPATTI):
    f = ImageFont.truetype(TAMIL, size)
    ImageDraw.Draw(img).text(xy, s, font=f, fill=rgb(col))
    return f.getlength(s)


def kick(img, xy, s, size, col=GREEN):
    f = ImageFont.truetype(INTER + "Inter-SemiBold.otf", size)
    sk.draw_text(img, xy, s.upper(), f, rgb(col), tracking_px=size * .16)


def head(img, xy, s, size, max_w, col=INK, lh=1.08, align="left", italic=False):
    f = B.font(size, "italic" if italic else "bold")
    return sk.block(img, xy, s, f, rgb(col), max_w, line_h=lh, tracking_px=size * B.tracking, align=align)


def head2(img, xy, a, b_, size, max_w, dark=False, align="left"):
    y = head(img, xy, a, size, max_w, col=WHITE if dark else INK, align=align)
    return head(img, (xy[0], y), b_, size, max_w, col=HALDI if dark else GREEN, align=align, italic=True)


def para(img, xy, s, size, max_w, col=BODY, lh=1.45, align="left"):
    return sk.block(img, xy, s, B.font(size), rgb(col), max_w, line_h=lh, align=align)


def btn(img, x, y, s, size=30, dark=False):
    f = ImageFont.truetype(INTER + "Inter-SemiBold.otf", size)
    return sk.pill(img, (x, y), s, f, GREEN if dark else WHITE, WHITE if dark else GREEN, pad=(int(size * .95), int(size * .55)), radius=int(size * .3))


def chip(img, x, y, s, size=22, fg=GREEN, fill="#E3F1EC"):
    f = ImageFont.truetype(INTER + "Inter-SemiBold.otf", size)
    return sk.pill(img, (x, y), s, f, fg, fill, pad=(int(size * .7), int(size * .35)), radius=int(size))


def foot(img, W, H, m, size=20, dark=False, page=None, text="Handmade in small batches in Chennai · shipped across the US"):
    c = "#CFE5DD" if dark else "#7A7266"
    para(img, (m, H - m * .85), text, size, W - 2 * m, col=c)
    if page:
        f = B.font(size)
        sk.draw_text(img, (W - m - sk.text_width(f, page), H - m * .85), page, f, rgb(c))


def lift(base, im, xy, op=60):
    sk.shadow_paste(base, im, xy, blur=30, offset=(0, 20), opacity=op)


DIET_LABEL = {"no-refined-sugar": "No refined sugar", "jaggery": "Jaggery sweetened", "vegan": "Vegan",
              "gluten-free": "Gluten-free", "millet": "Millet", "high-protein": "High protein", "high-fibre": "High fibre"}


def card(sku, w, show_tamil=True):
    """Product card: art + name + Tamil name, no price (prices are placeholders)."""
    p = P[sku]
    a = art(sku, w, radius=0)
    h = w + int(w * .40)
    c = Image.new("RGBA", (w, h), rgb(WHITE))
    c.alpha_composite(a, (0, 0))
    f = B.font(max(14, int(w * .08)), "bold")
    lines = sk.wrap(f, p["name"], int(w * .86))[:2]
    yy = w + int(w * .05)
    for ln in lines:
        sk.draw_text(c, (int(w * .07), yy), ln, f, rgb(INK))
        yy += int(f.size * 1.1)
    if show_tamil and p.get("tamil"):
        tamil(c, (int(w * .07), yy + int(w * .01)), p["tamil"], max(12, int(w * .055)))
    return sk.rounded(c, int(w * .05))


def shot(name, crop):
    return Image.open(SHOTS / f"{name}.png").convert("RGB").crop(crop)


NO_HEADER = (0, 66, 1440, 900)  # drop the stale "Organic Indian Sweets" header


def desk(name, width, crop=NO_HEADER, max_h=None):
    br = sk.browser(shot(name, crop), width, chrome="#EDE4D3", url="swaad", ink=BODY, radius=12)
    return sk.cap(br, max_h) if max_h else br


# ======================================================================= INSTAGRAM

def ig_carousel_deepavali():
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    s = bg((W, H), "karupatti")
    logo(s, m, 90, 64, dark=True)
    kick(s, (m, 250), "Deepavali · 8 Nov", 28, HALDI)
    y = head2(s, (m, 300), "Deepavali sweets,", "sorted early.", 110, W - 2 * m, dark=True)
    y = para(s, (m, y + 24), "Made to order in Chennai, shipped across the US. Order before the deadline and it's on the table on the day.", 34, W - 2 * m, col="#F2E3CF")
    a = art("CMB-FES-01", 560)
    lift(s, a, (W - 560 - m, y + 40), 140)
    kick(s, (m, H - 150), "Swipe · 5 slides", 22, HALDI)
    foot(s, W, H, m, dark=True)
    out.append(s)

    def grid_slide(n, k, a_, b_, line, skus):
        s = bg((W, H))
        kick(s, (m, 100), f"{n} / 05 · {k}", 22, KARUPATTI)
        y = head2(s, (m, 150), a_, b_, 84, W - 2 * m)
        y = para(s, (m, y + 14), line, 32, W - 2 * m)
        avail = H - (y + 40) - 130
        cw = min((W - 2 * m - 30) // 2, int((avail - 26) / 2 / 1.40))
        ox = (W - (2 * cw + 30)) // 2
        for i, sku in enumerate(skus):
            c = card(sku, cw)
            lift(s, c, (ox + (i % 2) * (cw + 30), y + 40 + (i // 2) * (c.size[1] + 26)), 45)
        foot(s, W, H, m, page=f"{n + 1} / 7")
        return s

    out.append(grid_slide(1, "The sweet counter", "Mysore pak to", "adhirasam.", "Ghee, cane jaggery or palm jaggery — the counter you'd queue for in Chennai.",
                          ["SWT-MYS-01", "SWT-ADH-02", "SWT-JAN-03", "SWT-BOO-04"]))
    out.append(grid_slide(2, "The karam side", "Something salty", "for every guest.", "Hand-twisted murukku, ribbon pakoda and the mixture that disappears first.",
                          ["SAV-MIX-01", "SAV-BUT-06", "SAV-RIB-03", "SAV-THA-10"]))
    out.append(grid_slide(3, "Gifting", "Boxes that say", "you remembered.", "Curated hampers and combos for family, friends and the office.",
                          ["CMB-FES-01", "CMB-SWK-07", "CMB-KAR-04", "CMB-POD-02"]))

    # festival calendar slide
    s = bg((W, H), "warm")
    kick(s, (m, 100), "4 / 05 · Will it arrive in time?", 22, KARUPATTI)
    y = head2(s, (m, 150), "Every festival,", "an order-by date.", 90, W - 2 * m)
    y = para(s, (m, y + 14), "Swaad adds each sweet's kitchen lead time to your delivery window and tells you the last day to order.", 32, W - 2 * m)
    yy = y + 40
    for name, date in FESTIVALS[:4]:
        hl = name == "Deepavali"
        ImageDraw.Draw(s).rounded_rectangle([m, yy, W - m, yy + 110], 14, fill=rgb(GREEN if hl else WHITE))
        sk.draw_text(s, (m + 36, yy + 32), name, B.font(38, "bold"), rgb(WHITE if hl else INK))
        f = ImageFont.truetype(INTER + "Inter-SemiBold.otf", 32)
        sk.draw_text(s, (W - m - 36 - f.getlength(date), yy + 36), date, f, rgb(HALDI if hl else KARUPATTI))
        yy += 130
    para(s, (m, yy + 10), "2026–27 dates from the store's festival calendar. Check the order-by date on each product.", 24, W - 2 * m, col="#7A7266")
    foot(s, W, H, m, page="5 / 7")
    out.append(s)

    # bulk tiers slide
    s = bg((W, H))
    kick(s, (m, 100), "5 / 05 · Buying for the whole family?", 22, KARUPATTI)
    y = head2(s, (m, 150), "More boxes,", "less per box.", 96, W - 2 * m)
    y = para(s, (m, y + 14), "Quantity pricing applies to each item line, automatically at checkout.", 32, W - 2 * m)
    yy = y + 50
    for q, off in [("6+", "5%"), ("12+", "10%"), ("24+", "15%")]:
        ImageDraw.Draw(s).rounded_rectangle([m, yy, W - m, yy + 150], 16, fill=rgb(WHITE))
        sk.draw_text(s, (m + 40, yy + 30), q, B.font(80, "bold"), rgb(GREEN))
        sk.draw_text(s, (m + 260, yy + 52), "of one item", B.font(34), rgb(BODY))
        f = B.font(80, "bold")
        t = off + " off"
        sk.draw_text(s, (W - m - 40 - f.getlength(t), yy + 30), t, f, rgb(KARUPATTI))
        yy += 175
    para(s, (m, yy + 10), "Planning a wedding, puja or function? Send an event enquiry from the store.", 28, W - 2 * m)
    foot(s, W, H, m, page="6 / 7")
    out.append(s)

    s = bg((W, H), "green")
    logo(s, m, 90, 64, dark=True)
    y = head2(s, (m, 330), "The whole South Indian", "counter, shipped.", 96, W - 2 * m, dark=True)
    para(s, (m, y + 30), "101 sweets, savouries, podis, pickles and millets — made in small batches in Chennai.", 36, W - 2 * m, col="#DDEFE8")
    btn(s, m, y + 220, "Shop the Deepavali counter", 34, dark=True)
    x = m
    for sku in ["SWT-MYS-01", "KAR-HAL-01", "SAV-BUT-06", "POD-IDL-01"]:
        p = plate(sku, 200)
        s.alpha_composite(p, (x, H - 360))
        x += 225
    foot(s, W, H, m, dark=True, text="Link in bio · ecommerce-store.big-mo.ai")
    out.append(s)

    for i, s in enumerate(out, 1):
        sk.save(s, OUT / "instagram/carousel-deepavali" / f"slide-{i:02d}.png")


def ig_carousel_collections():
    W, H = sk.IG_PORTRAIT
    m = 80
    picks = {
        "karupatti": ["KAR-HAL-01", "KAR-BUR-02", "KAR-ELL-03"],
        "sweets": ["SWT-MYS-01", "SWT-KAJ-07", "SWT-TIR-08"],
        "savouries": ["SAV-MIX-01", "SAV-KAI-09", "SAV-BAN-19"],
        "podis": ["POD-IDL-01", "POD-MUR-02", "POD-RAS-10"],
        "pickles": ["PIC-AVA-01", "PIC-MAA-02", "PIC-THO-03"],
        "millets": ["MIL-RAG-01", "MIL-MUR-04", "MIL-SAT-06"],
        "combos": ["CMB-FES-01", "CMB-POD-02", "CMB-PIC-03"],
    }
    out = []
    s = bg((W, H))
    logo(s, m, 90, 60)
    y = head2(s, (m, 300), "Seven counters.", "One Chennai kitchen.", 104, W - 2 * m)
    para(s, (m, y + 24), "Swipe through everything we make — in English and Tamil.", 36, W - 2 * m)
    x, yy = m, y + 170
    for i, c in enumerate(CAT["collections"]):
        w, h = chip(s, x, yy, c["name"], 26)
        x += w + 14
        if x > W - m - 260:
            x, yy = m, yy + h + 14
    foot(s, W, H, m)
    out.append(s)

    for i, c in enumerate(CAT["collections"], 1):
        s = bg((W, H))
        kick(s, (m, 100), f"Counter {i} / 7", 22, KARUPATTI)
        y = head(s, (m, 145), c["name"], 92, W - 2 * m)
        tamil(s, (m, y + 4), c["tamil"], 46, c["accent"])
        y = para(s, (m, y + 90), c["tagline"] + ".", 34, W - 2 * m, col=INK)
        sk_list = picks[c["id"]]
        big = art(sk_list[0], 560)
        lift(s, big, (m, y + 40), 55)
        sw = W - 2 * m - 560 - 30
        for j, sku in enumerate(sk_list[1:]):
            a = art(sku, sw)
            lift(s, a, (m + 560 + 30, y + 40 + j * (sw + 30)), 45)
        ny = y + 40 + 560 + 24
        sk.draw_text(s, (m, ny), P[sk_list[0]]["name"], B.font(34, "bold"), rgb(INK))
        tamil(s, (m, ny + 46), P[sk_list[0]]["tamil"] or "", 28)
        foot(s, W, H, m, page=f"{i + 1} / 9")
        out.append(s)

    s = bg((W, H), "green")
    logo(s, m, 90, 60, dark=True)
    y = head2(s, (m, 330), "Which counter", "are you starting with?", 100, W - 2 * m, dark=True)
    para(s, (m, y + 30), "Tell us in the comments. Shop all 101 items — link in bio.", 36, W - 2 * m, col="#DDEFE8")
    btn(s, m, y + 200, "Shop all 101 items", 34, dark=True)
    foot(s, W, H, m, dark=True)
    out.append(s)

    for i, s in enumerate(out, 1):
        sk.save(s, OUT / "instagram/carousel-seven-counters" / f"slide-{i:02d}.png")


def ig_posts():
    W, H = sk.IG_PORTRAIT
    m = 80
    out = []

    def hero(name, sku, kind, k, a_, b_, line, tags):
        s = bg((W, H), kind)
        dark = kind in ("green", "karupatti")
        kick(s, (m, 100), k, 24, HALDI if dark else KARUPATTI)
        y = head2(s, (m, 145), a_, b_, 90, W - 2 * m, dark=dark)
        a = art(sku, 560)
        lift(s, a, ((W - 560) // 2, y + 36), 120 if dark else 60)
        ny = y + 36 + 560 + 30
        sk.draw_text(s, (m, ny), P[sku]["name"], B.font(40, "bold"), rgb(WHITE if dark else INK))
        tamil(s, (m, ny + 52), P[sku]["tamil"] or "", 30, HALDI if dark else KARUPATTI)
        ey = para(s, (m, ny + 104), line, 28, W - 2 * m, col="#F2E3CF" if dark else BODY)
        x = m
        for t in tags:
            w, _ = chip(s, x, int(ey + 14), t, 22, fg=GREEN_D if not dark else WHITE, fill="#E3F1EC" if not dark else "#2E6B5A")
            x += w + 12
        foot(s, W, H, m, dark=dark)
        out.append((name, s))

    hero("post-01-karupatti-halwa", "KAR-HAL-01", "karupatti", "Karupatti Specials", "Palm jaggery.", "Slow-stirred in ghee.",
         P["KAR-HAL-01"]["blurb"], ["No refined sugar", "Jaggery sweetened", "Bestseller"])
    hero("post-02-idli-podi", "POD-IDL-01", "cream", "Podis & Spice Blends", "A spoon of podi.", "A whole meal.",
         "Stone-ground, roasted to order. With sesame oil, it turns idli, dosa or plain rice into dinner.", ["Vegan", "Gluten-free"])
    hero("post-03-avakkai", "PIC-AVA-01", "warm", "Pickles & Thokkus", "The jar that", "goes back with you.",
         P["PIC-AVA-01"]["blurb"], ["Vegan", "Gluten-free"])

    # mosaic
    s = bg((W, H), "green")
    skus = [p["sku"] for p in CAT["products"]]
    cols, size, gap = 6, 150, 12
    ox = (W - (cols * size + (cols - 1) * gap)) // 2
    sel = skus[8:8 + 30]
    for i, sku in enumerate(sel):
        a = art(sku, size, radius=14)
        s.alpha_composite(a, (ox + (i % cols) * (size + gap), 330 + (i // cols) * (size + gap)))
    head2(s, (m, 90), "101 things", "you miss from home.", 84, W - 2 * m, dark=True)
    foot(s, W, H, m, dark=True, text="Every item made in small batches in Chennai · shipped across the US")
    out.append(("post-04-101-things", s))

    # this-or-that
    s = bg((W, H))
    kick(s, (m, 100), "Settle it in the comments", 24, KARUPATTI)
    head(s, (m, 145), "Mysore pak or adhirasam?", 84, W - 2 * m)
    cw = (W - 2 * m - 40) // 2
    for i, sku in enumerate(["SWT-MYS-01", "SWT-ADH-02"]):
        c = card(sku, cw)
        lift(s, c, (m + i * (cw + 40), 400), 50)
    f = B.font(70, "bold")
    ImageDraw.Draw(s).ellipse([W // 2 - 60, 560, W // 2 + 60, 680], fill=rgb(GREEN))
    sk.draw_text(s, (W // 2 - f.getlength("or") / 2, 575), "or", f, rgb(WHITE))
    para(s, (m, 400 + cw + int(cw * .34) + 50), "Comment MP for Mysore pak, AD for adhirasam.", 32, W - 2 * m)
    foot(s, W, H, m)
    out.append(("post-05-this-or-that", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/posts" / f"{n}.png")


def ig_stories():
    W, H = sk.IG_STORY
    m = 90
    out = []

    s = bg((W, H), "karupatti")
    logo(s, m, 160, 66, dark=True)
    kick(s, (m, 380), "Deepavali · Sunday 8 Nov", 32, HALDI)
    y = head2(s, (m, 440), "Will your sweets", "make it in time?", 112, W - 2 * m, dark=True)
    para(s, (m, y + 30), "Every product page shows when it ships. The festival calendar shows the last day to order.", 42, W - 2 * m, col="#F2E3CF")
    a = art("SWT-JAN-03", 760)
    lift(s, a, ((W - 760) // 2, y + 280), 150)
    foot(s, W, H, m, 26, dark=True, text="Tap the link · ecommerce-store.big-mo.ai")
    out.append(("story-01-deepavali-deadline", s))

    s = bg((W, H))
    kick(s, (m, 260), "Poll", 32, KARUPATTI)
    head(s, (m, 320), "Podi on idli: oil or ghee?", 104, W - 2 * m)
    a = art("POD-IDL-01", 820)
    lift(s, a, ((W - 820) // 2, 700), 60)
    para(s, (m, 1580), "(Leave space here for the poll sticker.)", 30, W - 2 * m, col="#B0A796")
    foot(s, W, H, m, 26)
    out.append(("story-02-podi-poll", s))

    s = bg((W, H), "green")
    y = head2(s, (m, 360), "Missing home?", "We ship the counter.", 116, W - 2 * m, dark=True)
    x, yy = m, y + 120
    for i, sku in enumerate(["KAR-HAL-01", "SWT-MYS-01", "SAV-BUT-06", "POD-IDL-01"]):
        p = plate(sku, 360)
        s.alpha_composite(p, (int((W - 780) // 2 + (i % 2) * 420), int(yy + (i // 2) * 400)))
    logo(s, m, H - 190, 66, dark=True)
    out.append(("story-03-missing-home", s))

    for n, s in out:
        sk.save(s, OUT / "instagram/stories" / f"{n}.png")


def ig_reel():
    W, H = sk.IG_STORY
    m = 90
    sc = []
    s = bg((W, H), "karupatti")
    y = head2(s, (m, 700), "POV: Deepavali,", "half a world from Chennai.", 110, W - 2 * m, dark=True)
    sc.append(sk.Scene(s, 2.4))
    for sku, kind in [("SWT-MYS-01", "warm"), ("KAR-HAL-01", "cream"), ("SAV-BUT-06", "warm"), ("POD-IDL-01", "cream"), ("PIC-AVA-01", "warm")]:
        s = bg((W, H), kind)
        a = art(sku, 900)
        lift(s, a, ((W - 900) // 2, 420), 70)
        ty = head(s, (m, 1390), P[sku]["name"], 96, W - 2 * m, align="center")
        f = ImageFont.truetype(TAMIL, 56)
        t = P[sku]["tamil"] or ""
        ImageDraw.Draw(s).text(((W - f.getlength(t)) / 2, ty + 14), t, font=f, fill=rgb(KARUPATTI))
        sc.append(sk.Scene(s, 1.6, zoom=1.04))
    s = bg((W, H), "green")
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 110, dark=True)
    logo(s, (W - lw) / 2, 620, 110, dark=True)
    head(s, (m, 880), "The whole South Indian counter, shipped.", 92, W - 2 * m, col=WHITE, align="center")
    para(s, (m, 1240), "Order before the festival deadline · link in bio", 40, W - 2 * m, col="#DDEFE8", align="center")
    sc.append(sk.Scene(s, 3.2, move="out", zoom=1.05))
    sk.render_video(sc, (W, H), OUT / "instagram/reel-deepavali-counter-9x16.mp4")
    sk.save(sc[0].frame, OUT / "instagram/reel-cover.png")


# ======================================================================= LINKEDIN (BigMo platform)

STAGES = ["Order", "Demand", "Production", "Supply", "Fulfilment", "Delivery"]


def pipeline(img, x0, y, x1, size=26, active=None, dark=False):
    d = ImageDraw.Draw(img)
    n = len(STAGES)
    d.line([(x0, y), (x1, y)], fill=rgb("#CFE5DD" if dark else "#D8CDB8"), width=max(3, size // 6))
    f = ImageFont.truetype(INTER + "Inter-SemiBold.otf", size)
    for i, st in enumerate(STAGES):
        x = x0 + (x1 - x0) * i / (n - 1)
        r = size * .7
        on = active is None or i <= active
        d.ellipse([x - r, y - r, x + r, y + r], fill=rgb(GREEN if on else (WHITE if not dark else GREEN_D)),
                  outline=rgb(HALDI if dark else GREEN), width=3)
        w = f.getlength(st)
        d.text((x - w / 2, y + r + size * .5), st, font=f, fill=rgb(WHITE if dark else INK))


def copilot_card(w):
    """Designed illustration of the ops copilot — tool names are the real read-only tools."""
    h = int(w * .86)
    c = Image.new("RGBA", (w, h), rgb(WHITE))
    d = ImageDraw.Draw(c)
    s = w / 900
    f1 = ImageFont.truetype(INTER + "Inter-SemiBold.otf", int(30 * s))
    f2 = ImageFont.truetype(INTER + "Inter-Regular.otf", int(26 * s))
    fm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", int(22 * s))
    d.text((40 * s, 36 * s), "Ops copilot · morning briefing", font=f1, fill=rgb(INK))
    d.rounded_rectangle([40 * s, 100 * s, w - 40 * s, 200 * s], 16 * s, fill=rgb("#EEF6F3"))
    d.text((64 * s, 122 * s), "“What's stuck in production today?”", font=f2, fill=rgb(GREEN_D))
    d.text((40 * s, 236 * s), "Read-only tools it can call", font=f1, fill=rgb(INK))
    tools = ["list_orders", "get_order", "check_inventory", "search_catalog", "demand_summary", "pipeline_snapshot"]
    for i, t in enumerate(tools):
        x = 40 * s + (i % 2) * (w / 2 - 20 * s)
        yy = 296 * s + (i // 2) * 74 * s
        d.rounded_rectangle([x, yy, x + w / 2 - 60 * s, yy + 56 * s], 10 * s, fill=rgb(CREAM2))
        d.text((x + 20 * s, yy + 14 * s), t + "()", font=fm, fill=rgb(KARUPATTI))
    d.text((40 * s, 540 * s), "No writes. No keys? Falls back to SQL rules.", font=f2, fill=rgb(BODY))
    d.text((40 * s, 590 * s), "Purchase plans are clamped and validated.", font=f2, fill=rgb(BODY))
    d.text((40 * s, 640 * s), "Briefing cached for 15 minutes.", font=f2, fill=rgb(BODY))
    return sk.rounded(c, int(18 * s))


def li_links():
    W, H = sk.LI_LINK
    m = 60
    # 1 storefront
    s = bg((W, H))
    logo(s, m, 50, 40)
    y = head2(s, (m, 140), "A niche brand,", "fully operated.", 54, 500)
    para(s, (m, y + 16), "Swaad's storefront and its six-stage order flow — built by BigMo on one platform.", 22, 470)
    br = desk("01-home", 610, max_h=480)
    lift(s, br, (W - 610 - 30, 70))
    sk.save(s, OUT / "linkedin/images/link-01-storefront.png")
    # 2 pipeline
    s = bg((W, H), "green")
    kick(s, (m, 60), "BigMo niche-commerce flow", 18, HALDI)
    head2(s, (m, 100), "From a customer order", "to a doorstep delivery.", 52, W - 2 * m, dark=True)
    pipeline(s, m + 40, 400, W - m - 40, 24, dark=True)
    para(s, (m, H - 90), "Demand evaluation · batch production · material supply · carrier dispatch · tracking", 20, W - 2 * m, col="#DDEFE8")
    sk.save(s, OUT / "linkedin/images/link-02-pipeline.png")
    # 3 copilot
    s = bg((W, H))
    kick(s, (m, 60), "AI ops copilot", 18, KARUPATTI)
    y = head2(s, (m, 100), "Ask the shop floor", "a question.", 52, 500)
    para(s, (m, y + 16), "Staff ask about orders, stock and demand in plain language. The model only gets read-only tools.", 22, 470)
    c = copilot_card(560)
    lift(s, c, (W - 560 - 40, (H - c.size[1]) // 2))
    sk.save(s, OUT / "linkedin/images/link-03-copilot.png")


def li_document():
    W, H = sk.LI_SQUARE
    m = 90
    pages = []

    def page(n, k, a_, b_, text, visual=None, kind="cream"):
        s = bg((W, H), kind)
        dark = kind == "green"
        kick(s, (m, 80), k, 22, HALDI if dark else KARUPATTI)
        y = head2(s, (m, 128), a_, b_, 68, W - 2 * m, dark=dark)
        y = para(s, (m, y + 10), text, 30, W - 2 * m, col="#DDEFE8" if dark else BODY)
        if visual is not None:
            v = visual(y)
            if v is not None:
                lift(s, v[0], v[1], 70)
        logo(s, m, H - 100, 40, dark=dark)
        f = B.font(22)
        sk.draw_text(s, (W - m - 50, H - 86), f"{n} / 8", f, rgb("#DDEFE8" if dark else "#7A7266"))
        pages.append(s)
        return s

    s = bg((W, H), "karupatti")
    logo(s, m, 100, 56, dark=True)
    y = head2(s, (m, 320), "Running a made-to-order", "food brand across two continents.", 82, W - 2 * m, dark=True)
    para(s, (m, y + 30), "How BigMo's niche-commerce flow runs Swaad — a Chennai kitchen shipping 101 items across the US.", 32, W - 2 * m, col="#F2E3CF")
    for i, sku in enumerate(["SWT-MYS-01", "KAR-HAL-01", "SAV-BUT-06", "POD-IDL-01"]):
        s.alpha_composite(plate(sku, 220), (m + i * 255, H - 340))
    pages.append(s)

    page(2, "01 · The flow", "Six stages,", "one order record.", "Every order moves Order → Demand → Production → Supply → Fulfilment → Delivery, with a board per role.",
         lambda y: None)
    pipeline(pages[-1], m + 50, 760, W - m - 50, 26)
    page(3, "02 · Catalog as code", "101 products,", "zero licensed images.", "One catalog file feeds the storefront, the database seed and the product art — every image is generated from code.",
         lambda y: (sk.rounded(mosaic(5, 3, 190, 12), 16), (m, y + 40)))
    page(4, "03 · Festival deadlines", "“Will it arrive", "before Deepavali?”", "Per-product kitchen lead time + delivery window = the last day to order, for six festivals a year.",
         lambda y: (festival_card(W - 2 * m), (m, y + 40)))
    page(5, "04 · Pricing people can predict", "Quantity tiers", "per line.", "6+ of one item: 5% off · 12+: 10% · 24+: 15%. Cents are floored in the customer's favour.",
         lambda y: (tiers_card(W - 2 * m), (m, y + 40)))
    page(6, "05 · Trust signals", "Verified-buyer reviews.", "Restock alerts.", "Only customers whose order was delivered can review. Back-in-stock alerts fire once, on the real 0 → in-stock change.",
         lambda y: (desk("03-product-detail", W - 2 * m, max_h=H - y - 200), (m, y + 40)))
    page(7, "06 · AI ops copilot", "Plain-language questions,", "read-only answers.", "Six read-only tools, a cached morning briefing, and a SQL fallback when no model is configured.",
         lambda y: (copilot_card(W - 2 * m - 300), (m + 150, y + 40)))
    s = bg((W, H), "green")
    logo(s, m, 100, 56, dark=True)
    y = head2(s, (m, 340), "Got a niche brand", "that needs to run like this?", 86, W - 2 * m, dark=True)
    para(s, (m, y + 30), "BigMo builds and operates the storefront, the order flow and the ops copilot. Talk to us.", 34, W - 2 * m, col="#DDEFE8")
    btn(s, m, y + 210, "team@bigmoda.ai", 34, dark=True)
    pages.append(s)

    sk.pdf(pages, OUT / "linkedin/document-made-to-order-operating-model.pdf")
    for i, p in enumerate(pages, 1):
        sk.save(p, OUT / "linkedin/document-pages" / f"page-{i:02d}.png")


def mosaic(cols, rows, size, gap):
    skus = [p["sku"] for p in CAT["products"]][40:40 + cols * rows]
    im = Image.new("RGBA", (cols * size + (cols - 1) * gap, rows * size + (rows - 1) * gap), rgb(CREAM2))
    for i, sku in enumerate(skus):
        im.alpha_composite(art(sku, size, radius=12), ((i % cols) * (size + gap), (i // cols) * (size + gap)))
    return im


def tiers_card(w):
    c = Image.new("RGBA", (w, 520), rgb(WHITE))
    d = ImageDraw.Draw(c)
    f1 = ImageFont.truetype(INTER + "Inter-SemiBold.otf", 26)
    d.text((40, 30), "Quantity pricing · per item line", font=f1, fill=rgb(KARUPATTI))
    for i, (q, off) in enumerate([("6+", "5% off"), ("12+", "10% off"), ("24+", "15% off")]):
        yy = 100 + i * 130
        d.rounded_rectangle([24, yy, w - 24, yy + 110], 14, fill=rgb(CREAM))
        f = B.font(64, "bold")
        d.text((60, yy + 16), q, font=f, fill=rgb(GREEN))
        d.text((250, yy + 38), "of one item", font=B.font(30), fill=rgb(BODY))
        d.text((w - 60 - f.getlength(off), yy + 16), off, font=f, fill=rgb(KARUPATTI))
    return sk.rounded(c, 16)


def festival_card(w):
    rows = FESTIVALS
    h = 90 + len(rows) * 80
    c = Image.new("RGBA", (w, h), rgb(WHITE))
    d = ImageDraw.Draw(c)
    f1 = ImageFont.truetype(INTER + "Inter-SemiBold.otf", 26)
    f2 = B.font(32, "bold")
    d.text((36, 30), "Festival calendar · 2026–27", font=f1, fill=rgb(KARUPATTI))
    for i, (n, dt) in enumerate(rows):
        yy = 90 + i * 80
        if n == "Deepavali":
            d.rounded_rectangle([20, yy - 6, w - 20, yy + 66], 12, fill=rgb("#E3F1EC"))
        d.text((36, yy + 10), n, font=f2, fill=rgb(INK))
        d.text((w - 36 - f1.getlength(dt), yy + 16), dt, font=f1, fill=rgb(GREEN))
    return sk.rounded(c, 16)


def li_video():
    W, H = sk.LI_VIDEO
    m = 120
    sc = []
    s = bg((W, H), "karupatti")
    head2(s, (m, 380), "A Chennai kitchen.", "Customers across the US.", 110, W - 2 * m, dark=True)
    sc.append(sk.Scene(s, 2.8))

    def feat(k, a_, line, visual, kind="cream"):
        s = bg((W, H), kind)
        dark = kind == "green"
        kick(s, (m, 280), k, 26, HALDI if dark else KARUPATTI)
        y = head(s, (m, 330), a_, 76, 620, col=WHITE if dark else INK)
        para(s, (m, y + 20), line, 34, 600, col="#DDEFE8" if dark else BODY)
        logo(s, m, H - 160, 52, dark=dark)
        v = visual
        lift(s, v, (W - v.size[0] - 90, (H - v.size[1]) // 2), 80)
        return s

    sc.append(sk.Scene(feat("Storefront", "101 items, all generated art.", "Search in Tamil or English, filter by diet and spice.", desk("01-home", 1040, max_h=860)), 3.6))
    s = bg((W, H), "green")
    kick(s, (m, 260), "Operations", 26, HALDI)
    head(s, (m, 310), "Six stages, one order record.", 84, W - 2 * m, col=WHITE)
    pipeline(s, m + 80, 640, W - m - 80, 34, dark=True)
    sc.append(sk.Scene(s, 3.6))
    sc.append(sk.Scene(feat("Festivals", "“Will it arrive in time?”", "Lead time + delivery window = order-by date.", festival_card(760)), 3.6))
    sc.append(sk.Scene(feat("AI ops copilot", "Ask the shop floor.", "Read-only tools. Cached briefing. SQL fallback.", copilot_card(820)), 3.6))
    sc.append(sk.Scene(feat("Tracking", "Every order, visible.", "From new order to delivered.", desk("06-track", 1040, crop=(0, 66, 1440, 640))), 3.2))
    s = bg((W, H), "green")
    lw = logo(Image.new("RGBA", (10, 10)), 0, 0, 100, dark=True)
    logo(s, (W - lw) / 2, 300, 100, dark=True)
    sk.block(s, (m, 480), "The whole South Indian counter, shipped.", B.font(70, "bold"), rgb(WHITE), W - 2 * m, align="center")
    sk.block(s, (m, 620), "Built and operated on BigMo's niche-commerce flow · bigmoda.ai", B.font(36), rgb("#DDEFE8"), W - 2 * m, align="center")
    x = (W - 4 * 200 - 3 * 30) // 2
    for i, sku in enumerate(["SWT-MYS-01", "KAR-HAL-01", "SAV-BUT-06", "POD-IDL-01"]):
        s.alpha_composite(plate(sku, 200), (x + i * 230, 760))
    sc.append(sk.Scene(s, 4, move="out", zoom=1.04))
    sk.render_video(sc, (W, H), OUT / "linkedin/video-operating-flow-16x9.mp4")
    sk.save(sc[1].frame, OUT / "linkedin/video-cover.png")


if __name__ == "__main__":
    ensure_art([p["sku"] for p in CAT["products"]])
    ig_carousel_deepavali()
    ig_carousel_collections()
    ig_posts()
    ig_stories()
    li_links()
    li_document()
    if not args.no_video:
        ig_reel()
        li_video()
    print("done →", OUT)
