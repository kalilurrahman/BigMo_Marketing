"""KPMRentals — month two. Live modules only: screens marked "Preview module — actions
simulated" in the app (rent & finance, inspections, renewals) are deliberately NOT marketed.
Facts from the README and screens: time-boxed smart-lock guest passes with an access log;
IoT monitoring that can open a ticket from a sensor alert; unified inbox with AI thread
summaries; owner default-and-confirm memos. Memphis-first, no prices / returns / market stats.

Run:  python3 campaigns/kpm-rentals/phase2.py [--no-video]
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
    col = (b.GOLD if dark else b.EMERALD_M) if accent else (b.CREAM if dark else b.INK)
    return b.head(img, xy, s, size, w, col=col, italic=accent)


kit = phase2.Kit(
    bg=lambda size, dark: b.bg(size, "emerald" if dark else "cream"),
    logo=lambda img, x, y, h, dark: b.logo(img, x, y, h, dark),
    head=_head,
    body=lambda img, xy, s, size, w, dark, col=None: b.para(img, xy, s, size, w, col=col or ("#E6EFE9" if dark else b.BODY)),
    kick=lambda img, xy, s, size, dark: b.kick(img, xy, s, size, b.GOLD if dark else b.GOLD_TEXT),
    cta=lambda img, x, y, s, size, dark: b.btn(img, x, y, s, size, dark),
    foot=lambda img, W, H, m, dark, page: b.foot(img, W, H, m, 20, dark, page),
    lift=lambda base, im, xy, dark: b.lift(base, im, xy, 110 if dark else 60),
    muted="#A9A08A", muted_dark="#8FB5A5", accent=b.EMERALD_M, accent_dark=b.GOLD,
    body_font=lambda size: b.fira(size),
)


def app(name, top=0, h=1500, right=2880):
    def v(w, max_h):
        return b.app(name, w, max_h=max_h, top=top, h=h, right=right)
    return v


content = {
    "myths": {
        "kicker": "Remote-landlord myths", "title_a": "Four things remote", "title_b": "owners put up with.",
        "sub": "You don't have to — even from 13 time zones away.",
        "items": [
            ("Owning from abroad means being on call at 2 a.m.", "Decisions wait for your morning.",
             "Non-urgent decisions are batched into one digest in your local time. Urgent ones are triaged and routed without waiting for you."),
            ("A repair quote is whatever the vendor says.", "Every ticket has a cost band.",
             "Repairs arrive with a P50–P80 band benchmarked against similar Memphis jobs, and outlier quotes are flagged."),
            ("You find out about a leak when the ceiling falls.", "Sensors open the ticket.",
             "Leak, HVAC and smoke sensors raise alerts — a moisture spike can open a plumbing ticket on its own."),
            ("Handing out keys means losing track of who got in.", "Every pass is time-boxed.",
             "Smart-lock guest passes for vendors and showings expire on their own, and every issue and revoke is on the access log."),
        ],
        "cta_a": "Own in Memphis.", "cta_b": "Live anywhere.",
        "cta_body": "Start with a free rental analysis for your Tennessee property.", "cta_button": "Get a free rental analysis",
    },
    "posts": [
        {"slug": "sensors-open-tickets", "kicker": "Intelligent monitoring", "a": "The leak sensor", "b": "calls first.",
         "body": "Connected leak, HVAC, lock and smoke devices across the portfolio — an alert can open a ticket before anyone has to phone.",
         "visual": app("monitoring", h=1300)},
        {"slug": "guest-passes", "kicker": "Keys & guest grants", "a": "A code for the plumber.", "b": "Gone at 4 p.m.",
         "body": "Time-boxed guest passes for vendors and showings, revoked automatically, with every issue and revoke on the access log.",
         "visual": app("access", h=1300, right=2000), "dark": True},
        {"slug": "unified-inbox", "kicker": "Unified inbox", "a": "Every conversation.", "b": "One place.",
         "body": "Residents, owners, vendors and applicants in one inbox, with AI thread summaries so nothing gets missed.",
         "visual": app("inbox", h=1300)},
    ],
    "reel": {"hook_a": "It's 2 a.m.", "hook_b": "The sensor's awake.",
             "end_a": "Your U.S. rentals,", "end_b": "without the 2 a.m. calls.", "end_sub": "Free rental analysis · link in bio"},
}

if __name__ == "__main__":
    phase2.build(kit, content, b.OUT, video=not a.no_video)
    print("phase 2 done →", b.OUT)
