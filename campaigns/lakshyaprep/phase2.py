"""LakshyaPrep — month two: myths vs facts, three deep-dives, a new reel.

Facts used here are on the product's own screens (docs/master/assets, docs/evidence):
practice test 1 free with an account; Standard / 1.5x / 2x time accommodation; review
shows your answer, the key, time spent and why; Lakshya Coach labels every reply as
AI-generated and says a human confirms before anything is booked.

Run:  python3 campaigns/lakshyaprep/phase2.py [--src ../academy-kpm-spark] [--no-video]
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--src")
ap.add_argument("--no-video", action="store_true")
a = ap.parse_args()
sys.argv = [sys.argv[0]] + (["--src", a.src] if a.src else [])
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import build as b  # noqa: E402
import phase2  # noqa: E402
import socialkit as sk  # noqa: E402

DOCS = b.SRC / "docs"


def _head(img, xy, s, size, w, dark, accent):
    if accent:
        return b.display(img, xy, s, size, w, colour=b.NIGHT_MAG if dark else b.B.accent, style="italic", dark=dark, misreg=False)
    return b.display(img, xy, s, size, w, dark=dark)


kit = phase2.Kit(
    bg=lambda size, dark: b.bg(size, dark=dark),
    logo=lambda img, x, y, h, dark: b.logo(img, x, y, h, dark),
    head=_head,
    body=lambda img, xy, s, size, w, dark, col=None: b.body(img, xy, s, size, w, dark=dark, colour=col),
    kick=lambda img, xy, s, size, dark: sk.kicker(img, xy, s, b.B, size, b.NIGHT_MAG if dark else b.B.accent),
    cta=lambda img, x, y, s, size, dark: b.cta(img, x, y, s, size, dark=dark),
    foot=lambda img, W, H, m, dark, page: b.footer(img, W, H, dark=dark, m=m, page=page),
    lift=lambda base, im, xy, dark: sk.shadow_paste(base, im, xy, opacity=120 if dark else 70),
    muted="#8F8B8B", muted_dark="#7D7880", accent=b.B.accent, accent_dark=b.NIGHT_MAG,
    body_font=lambda size: b.B.font(size, "regular"),
)


def shot(path, crop, frame=True, url="lakshyaprep.com"):
    def v(w, max_h):
        im = sk.load_shot(path, crop=crop)
        out = sk.browser(im, w, url=url) if frame else sk.rounded(im.resize((w, int(im.size[1] * w / im.size[0]))), 4)
        if out.size[1] > max_h:  # narrow card: fit height instead
            s = max_h / out.size[1]
            out = out.resize((int(out.size[0] * s), max_h))
        return out
    return v


content = {
    "myths": {
        "kicker": "Test-prep myths", "title_a": "Four things", "title_b": "nobody should tell you.",
        "sub": "Busting the advice that keeps students busy instead of improving.",
        "items": [
            ("More practice tests will raise my score.", "Practise what pays.",
             "GoalGap ranks your weak skills by the points they can still give you — so the next hour goes where the score can move."),
            ("A diagnostic is just another test.", "A scan is a map.",
             "It shows where points leak, by skill and by section — before you spend a single hour."),
            ("A missed question is just a missed question.", "Every miss comes back.",
             "Misses flow into a review log and spaced repetition, so the same trap gets fewer chances."),
            ("Pacing is something you figure out on test day.", "Rehearse the clock.",
             "Timed full-length mocks, with Standard, 1.5× or 2× time accommodation, and the time spent on every question."),
        ],
        "cta_a": "Lock the goal.", "cta_b": "Own the score.",
        "cta_body": "Practice test 1 of each exam is free with an account.", "cta_button": "Take the free scan",
    },
    "posts": [
        {"slug": "review-every-miss", "kicker": "Review", "a": "See why", "b": "you missed it.",
         "body": "Your answer, the key, the time you spent and the reason — then filter to just the ones you got wrong.",
         "visual": shot(DOCS / "evidence/quick-wins-2026-10-06/05-review-missed-filter.png", (0, 70, 1200, 900))},
        {"slug": "lakshya-coach", "kicker": "Lakshya Coach", "a": "Ask anything.", "b": "A human confirms.",
         "body": "Tell Lakshya Coach the grade, the exam and the date — it suggests a route. Every reply is labelled AI-generated, and a person confirms before anything is booked.",
         "visual": shot(DOCS / "master/assets/mobile/coach-open-1280.png", (898, 218, 1262, 770), frame=False), "dark": True},
        {"slug": "time-accommodation", "kicker": "Full-length tests", "a": "Real sections.", "b": "Real timing.",
         "body": "One sitting at a time, with Standard, 1.5× or 2× extended time. Practice test 1 is free on your account.",
         "visual": shot(DOCS / "master/assets/mobile/test-timing-1280.png", (0, 220, 1280, 780))},
    ],
    "reel": {"hook_a": "Studying hard?", "hook_b": "Or studying right?",
             "end_a": "One goal.", "end_b": "Zero noise.", "end_sub": "Take the free scan · lakshyaprep.com"},
}

if __name__ == "__main__":
    phase2.build(kit, content, b.OUT, video=not a.no_video)
    print("phase 2 done →", b.OUT)
