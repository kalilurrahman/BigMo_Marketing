"""DesiSquare — month two. Facts from desisquarev5-product/CLAUDE.md and the training-kit
screens: percent-only public pages (dollars owner-only); karma "measures community
engagement — never money"; flags are private (four reasons, one moderator queue);
WhatsApp is consent-gated and numbers never appear; the NRO and FBAR tools.
"Guru", never "maven". Educational, never investment advice — on every asset.

Run:  python3 campaigns/desisquare/phase2.py [--no-video]
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
    col = ("#9ED3E2" if dark else b.PEACOCK) if accent else (b.WHITE if dark else b.INK)
    return b.head(img, xy, s, size, w, col=col)


kit = phase2.Kit(
    bg=lambda size, dark: b.bg(size, dark=dark),
    logo=lambda img, x, y, h, dark: b.logo(img, x, y, h, dark),
    head=_head,
    body=lambda img, xy, s, size, w, dark, col=None: b.para(img, xy, s, size, w, col=col or ("#DCEBF0" if dark else b.BODY)),
    kick=lambda img, xy, s, size, dark: b.kick(img, xy, s, size, "#9ED3E2" if dark else b.PEACOCK),
    cta=lambda img, x, y, s, size, dark: b.btn(img, x, y, s, size, dark),
    foot=lambda img, W, H, m, dark, page: b.foot(img, W, H, m, 20, dark, page),
    lift=lambda base, im, xy, dark: b.lift(base, im, xy),
    muted="#9AA0AB", muted_dark="#7FA9B5", accent=b.PEACOCK, accent_dark="#9ED3E2",
    body_font=lambda size: b.B.font(size),
)


def screen(name, crop):
    def v(w, max_h):
        return b.desk(name, w, max_h=max_h, crop=crop)
    return v


content = {
    "myths": {
        "kicker": "Money-community myths", "title_a": "Four reasons people", "title_b": "don't ask online.",
        "sub": "And how DesiSquare is built so you can.",
        "items": [
            ("To get good answers, you have to share your portfolio.", "Percent, never dollars.",
             "Public pages show allocation in percent only. The dollar view is visible to its owner and nobody else."),
            ("The loudest, richest account is the most trusted.", "Helpfulness earns standing.",
             "Karma comes from Actionable, Insightful and Helpful reactions to your answers. Portfolio value and returns can never affect it."),
            ("Reporting a post shames the author in public.", "Flags are private.",
             "Four reasons, one moderator queue — and no public flag counts for anyone to pile on to."),
            ("Joining means your phone number ends up in a group.", "Consent first. Numbers never shown.",
             "WhatsApp mirroring and notifications are opt-in, and phone numbers never appear anywhere on DesiSquare."),
        ],
        "cta_a": "Read before", "cta_b": "you decide.",
        "cta_body": "Pseudonymous, percent-only, educational. Ask your first question.", "cta_button": "Join the community",
    },
    "posts": [
        {"slug": "nro-alarm", "kicker": "Free tool · no sign-in", "a": "Moved abroad?", "b": "Your accounts noticed.",
         "body": "Enter the month you left and what you still hold in India. The NRO tool says what should have changed — and what to ask your bank.",
         "visual": screen("47-tools-nro", (350, 20, 1100, 800))},
        {"slug": "fbar-check", "kicker": "Free tool · no sign-in", "a": "FBAR, Form 8938,", "b": "or both?",
         "body": "Two thresholds that don't agree — the tool checks both and explains why, without sending your numbers to any server.",
         "visual": screen("48-tools-fbar", (350, 20, 1100, 800))},
        {"slug": "karma-never-money", "kicker": "Karma guide", "a": "Engagement,", "b": "never money.",
         "body": "Every point is published: what earns it, what costs it. Portfolio value and percent returns can never move it.",
         "visual": screen("37-karma-guide", (460, 60, 1200, 800)), "dark": True},
    ],
    "reel": {"hook_a": "Asked a money question", "hook_b": "and got judged?",
             "end_a": "Money questions.", "end_b": "Desi answers.", "end_sub": "Educational community · not investment advice"},
}

if __name__ == "__main__":
    phase2.build(kit, content, b.OUT, video=not a.no_video)
    print("phase 2 done →", b.OUT)
