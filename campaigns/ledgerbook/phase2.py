"""Ledger Book — month two. Facts from the README and the demo screens: posted entries are
immutable and corrected by reversal; balances are computed from the journal, never stored;
invoices carry a reminder ladder that drafts notes for you to send; the copilot has twelve
read-only tools; Today's 13-week view. Tax set-aside is a rule of thumb, never advice.
No competitor named.

Run:  python3 campaigns/ledgerbook/phase2.py [--no-video]
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


def _head(img, xy, s, size, w, dark, accent):
    col = (b.NIGHT_BLUE if dark else b.BLUE) if accent else (b.NIGHT_INK if dark else b.INK)
    return b.head(img, xy, s, size, w, col=col)


kit = phase2.Kit(
    bg=lambda size, dark: b.bg(size, dark=dark),
    logo=lambda img, x, y, h, dark: b.logo(img, x, y, h, dark),
    head=_head,
    body=lambda img, xy, s, size, w, dark, col=None: b.para(img, xy, s, size, w, col=col or ("#C3C9D1" if dark else b.SOFT)),
    kick=lambda img, xy, s, size, dark: b.kick(img, xy, s, size, b.NIGHT_BLUE if dark else b.BLUE),
    cta=lambda img, x, y, s, size, dark: b.btn(img, x, y, s, size, dark),
    foot=lambda img, W, H, m, dark, page: b.foot(img, W, H, m, 20, dark, page),
    lift=lambda base, im, xy, dark: b.lift(base, im, xy, 120 if dark else 55),
    muted="#9AA1AA", muted_dark="#6E7682", accent=b.BLUE, accent_dark=b.NIGHT_BLUE,
    body_font=lambda size: b.inter(size),
)


def screen(name, frame=True, dark=False):
    def v(w, max_h):
        return b.screen(name, w, max_h=max_h, frame=frame, dark=dark)
    return v


content = {
    "myths": {
        "kicker": "Bookkeeping myths", "title_a": "Four things you've", "title_b": "been told about AI books.",
        "sub": "What an AI should and shouldn't do with your ledger.",
        "items": [
            ("An AI bookkeeper just posts whatever it guesses.", "It proposes. You approve.",
             "Every suggestion carries a confidence score and a reason. A deterministic posting service accepts only balanced entries."),
            ("Fixing a mistake means editing the old entry.", "Corrections are reversals.",
             "Posted entries are immutable. A correction is a second entry that reverses the first — both stay on the record."),
            ("Your balance is a number someone saved.", "Every number is computed.",
             "Cash, profit, receivables and reports are derived from the journal on demand, so every screen agrees."),
            ("An AI copilot can move your money.", "It can only read.",
             "Twelve read-only tools — profit, invoices, runway, unusual activity. No tool exists that can post, send or move money."),
        ],
        "cta_a": "AI proposes.", "cta_b": "The ledger disposes.",
        "cta_body": "Ledger Book is the AI bookkeeper from BigMo. Early access: team@bigmoda.ai", "cta_button": "Ask for early access",
    },
    "posts": [
        {"slug": "invoice-reminders", "kicker": "Invoices", "a": "Reminders drafted.", "b": "You hit send.",
         "body": "A collections ladder decides when each client should hear from you and writes the note. Nothing goes out until you send it.",
         "visual": screen("invoices")},
        {"slug": "journal-history", "kicker": "Journal", "a": "Nothing edited.", "b": "Everything explained.",
         "body": "Every posted entry, what it did and where it came from — corrections show as reversals, never as quiet edits.",
         "visual": screen("journal")},
        {"slug": "thirteen-weeks", "kicker": "Today", "a": "Will cash dip?", "b": "See 13 weeks out.",
         "body": "A projection built from the commitments your books already show — and it says in words whether it ever goes below today.",
         "visual": screen("today-top", dark=True), "dark": True},
    ],
    "reel": {"hook_a": "Made a mistake", "hook_b": "in your books?",
             "end_a": "Don't edit it.", "end_b": "Reverse it.", "end_sub": "Ledger Book · the AI bookkeeper by BigMo"},
}

if __name__ == "__main__":
    phase2.build(kit, content, b.OUT, video=not a.no_video)
    print("phase 2 done →", b.OUT)
