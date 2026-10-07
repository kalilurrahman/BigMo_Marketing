"""Swaad — month two (post-Deepavali): subscriptions, honest reviews, restock alerts.

Facts from niche-ecommerce-flow: catalog/subscriptions.mjs (Monthly Podi Box — 4 jars,
17-podi rotation; Monthly Millet Box — 3 items, 14 millets), docs/reviews.md (only
customers whose order was delivered can review; publish immediately), docs/back-in-stock.md
(one-shot alert on the real 0 → in-stock change, no account needed), docs/festivals.md.
Still: no "organic", no "Made in USA", no prices, no health claims.

Run:  python3 campaigns/swaad/phase2.py [--no-video]
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--no-video", action="store_true")
a = ap.parse_args()
sys.argv = [sys.argv[0], "--no-video"]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import build as b  # noqa: E402
import phase2  # noqa: E402
import socialkit as sk  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402


def _head(img, xy, s, size, w, dark, accent):
    col = (b.HALDI if dark else b.GREEN) if accent else (b.WHITE if dark else b.INK)
    return b.head(img, xy, s, size, w, col=col, italic=accent)


kit = phase2.Kit(
    bg=lambda size, dark: b.bg(size, "karupatti" if dark else "cream"),
    logo=lambda img, x, y, h, dark: b.logo(img, x, y, h, dark),
    head=_head,
    body=lambda img, xy, s, size, w, dark, col=None: b.para(img, xy, s, size, w, col=col or ("#F2E3CF" if dark else b.BODY)),
    kick=lambda img, xy, s, size, dark: b.kick(img, xy, s, size, b.HALDI if dark else b.KARUPATTI),
    cta=lambda img, x, y, s, size, dark: b.btn(img, x, y, s, size, dark),
    foot=lambda img, W, H, m, dark, page: b.foot(img, W, H, m, 20, dark, page),
    lift=lambda base, im, xy, dark: b.lift(base, im, xy, 110 if dark else 55),
    muted="#A39A8B", muted_dark="#A58C76", accent=b.GREEN, accent_dark=b.HALDI,
    body_font=lambda size: b.B.font(size),
)


def rotation_grid(skus, cols):
    def v(w, max_h):
        gap = 14
        size = min((w - (cols - 1) * gap) // cols, int((max_h - 60) / ((len(skus) + cols - 1) // cols)) - gap)
        rows = (len(skus) + cols - 1) // cols
        im = Image.new("RGBA", (cols * size + (cols - 1) * gap, rows * (size + gap) - gap), (0, 0, 0, 0))
        for i, sku in enumerate(skus):
            im.alpha_composite(b.art(sku, size, radius=12), ((i % cols) * (size + gap), (i // cols) * (size + gap)))
        return im
    return v


def review_card(w, max_h):
    """Illustrates the review RULE — not a review. No customer, no rating, no quote."""
    h = min(max_h, 560)
    c = Image.new("RGBA", (w, h), b.rgb(b.WHITE))
    d = ImageDraw.Draw(c)
    s = w / 900
    f1, f2 = b.fira_like(30 * s, 600), b.fira_like(26 * s)
    d.text((40 * s, 36 * s), "WHO CAN REVIEW", font=b.fira_like(22 * s, 600), fill=b.rgb(b.KARUPATTI))
    rows = [("Bought it", True), ("Order delivered", True), ("Then: review it", True), ("Anyone else", False)]
    for i, (t, ok) in enumerate(rows):
        y = (100 + i * 100) * s
        d.rounded_rectangle([40 * s, y, w - 40 * s, y + 80 * s], 14 * s, fill=b.rgb(b.CREAM if ok else "#F3E6E2"))
        d.text((70 * s, y + 22 * s), ("✓  " if ok else "–  ") + t, font=f1, fill=b.rgb(b.GREEN if ok else b.CHILLI))
    d.text((40 * s, 520 * s), "Publishes immediately. One opinion per customer.", font=f2, fill=b.rgb(b.BODY))
    return sk.rounded(c, int(18 * s))


def restock_card(w, max_h):
    h = min(max_h, 520)
    c = Image.new("RGBA", (w, h), b.rgb(b.WHITE))
    d = ImageDraw.Draw(c)
    s = w / 900
    art = b.art("PIC-MAA-02", int(300 * s), radius=int(16 * s))
    c.alpha_composite(art, (int(40 * s), int(40 * s)))
    x = 380 * s
    d.text((x, 50 * s), "Maavadu (Baby Mango)", font=b.B.font(int(38 * s), "bold"), fill=b.rgb(b.INK))
    d.rounded_rectangle([x, 120 * s, x + 260 * s, 170 * s], 25 * s, fill=b.rgb("#F3E6E2"))
    d.text((x + 24 * s, 128 * s), "Out of stock", font=b.fira_like(26 * s, 600), fill=b.rgb(b.CHILLI))
    d.rounded_rectangle([x, 200 * s, w - 40 * s, 280 * s], 14 * s, fill=b.rgb(b.GREEN))
    d.text((x + 28 * s, 222 * s), "Email me when it's back", font=b.fira_like(30 * s, 600), fill=b.rgb(b.WHITE))
    d.text((40 * s, 380 * s), "No account needed. One email, the moment it's", font=b.fira_like(26 * s), fill=b.rgb(b.BODY))
    d.text((40 * s, 420 * s), "really back in stock — then the alert is done.", font=b.fira_like(26 * s), fill=b.rgb(b.BODY))
    return sk.rounded(c, int(18 * s))


content = {
    "myths": {
        "kicker": "Ordering from home, from abroad", "title_a": "Four things you", "title_b": "probably believe.",
        "sub": "About ordering South Indian sweets and pantry staples in the US.",
        "items": [
            ("You can't know if it'll arrive before the festival.", "Every festival has an order-by date.",
             "Swaad adds each item's kitchen lead time to its delivery window and shows the last day to order."),
            ("Online food reviews are mostly made up.", "Only delivered orders can review.",
             "A review needs a purchase that actually arrived — so 'verified' is true of every single one."),
            ("Sold out means checking back every day.", "One alert, then done.",
             "Ask to be told when an item is back. No account needed — one email the moment it really restocks."),
            ("Bulk buying is only for businesses.", "Six jars is enough.",
             "Buy 6+ of one item for 5% off that line, 12+ for 10%, 24+ for 15% — applied automatically at checkout."),
        ],
        "cta_a": "The whole South", "cta_b": "Indian counter, shipped.",
        "cta_body": "Handmade in small batches in Chennai, shipped across the US.", "cta_button": "Shop all 101 items",
    },
    "posts": [
        {"slug": "podi-box", "kicker": "Monthly Podi Box", "a": "Four jars a month.", "b": "Never the same four.",
         "body": "Starts with the four a Tamil kitchen opens every week, then works through a 17-podi rotation — over a year before a jar comes round again.",
         "visual": rotation_grid(["POD-IDL-01", "POD-PAR-06", "POD-RAS-10", "POD-SAM-11", "POD-MIL-15", "POD-KAR-04", "POD-KOT-05", "POD-PUD-09"], 4)},
        {"slug": "verified-reviews", "kicker": "Reviews", "a": "Every review", "b": "is from a real order.",
         "body": "Only a customer who bought the item and had it delivered can review it. Reviews publish immediately; one opinion per customer.",
         "visual": review_card},
        {"slug": "back-in-stock", "kicker": "Back-in-stock alerts", "a": "Sold out?", "b": "We'll tell you once.",
         "body": "No account, no newsletter — a single email the moment it's really back.", "visual": restock_card, "dark": True},
    ],
    "reel": {"hook_a": "Deepavali's done.", "hook_b": "The podi ran out.",
             "end_a": "Four jars a month.", "end_b": "Never the same four.", "end_sub": "Monthly Podi Box · link in bio"},
}

if __name__ == "__main__":
    phase2.build(kit, content, b.OUT, video=not a.no_video)
    print("phase 2 done →", b.OUT)
