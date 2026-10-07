"""AI MarketPulse — month two. Facts from the README and docs/training-kit/TRAINING-GUIDE.md:
overrides skip advisory gates, never the Risk Core; keyless-first data; the 5-criterion
paper→live ladder; rule rehearsal reports in-sample and held-out separately ("not a promise
about the future"); risk limits are enforced server-side. Disclaimer on every asset.

Run:  python3 campaigns/marketpulse/phase2.py [--no-video]
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


def _logo(img, x, y, h, dark):
    b.mini_logo(img, x, y, int(h * 1.1))
    return h * 6


def _head(img, xy, s, size, w, dark, accent):
    return b.head(img, xy, s, size, w, col=b.ORANGE if accent else b.WHITE)


kit = phase2.Kit(
    bg=lambda size, dark: b.bg(size, seed=7 if dark else 3),
    logo=_logo,
    head=_head,
    body=lambda img, xy, s, size, w, dark, col=None: b.para(img, xy, s, size, w, col=col or "#D7DCE6"),
    kick=lambda img, xy, s, size, dark: b.kick(img, xy, s, size),
    cta=lambda img, x, y, s, size, dark: b.btn(img, x, y, s, size),
    foot=lambda img, W, H, m, dark, page: b.disclaimer(img, W, H, m, 20),
    lift=lambda base, im, xy, dark: b.glow_paste(base, im, xy),
    muted="#6B748A", muted_dark="#6B748A", accent=b.ORANGE, accent_dark=b.ORANGE,
    body_font=lambda size: b.B.font(size),
)


def screen(name, crop=(200, 0, 1440, 900)):
    def v(w, max_h):
        return b.desk(name, w, max_h=max_h, crop=crop)
    return v


content = {
    "myths": {
        "kicker": "AI trading myths", "title_a": "Four things people", "title_b": "get wrong about AI agents.",
        "sub": "What an AI should and shouldn't be allowed to do with a trade.",
        "items": [
            ("The AI agent decides what to buy.", "The AI only interprets.",
             "It turns headlines and messages into a structured signal. Deterministic code decides; the broker executes; everything is logged."),
            ("A human override can skip any check.", "Not the risk core.",
             "An override can skip advisory gates. Cash, buying power, daily-loss and position limits still apply — and the override is stamped in the audit trail."),
            ("You need paid data feeds to start.", "Keyless-first.",
             "The platform stays fully functional with zero API keys configured, degrading across data providers."),
            ("Paper trading is just a toy.", "Paper is the gate.",
             "Live activation needs 20+ paper trades, 14+ days of history, a reconciled ledger and acknowledged disclosures — and it names whatever is unmet."),
        ],
        "cta_a": "Risk control", "cta_b": "is the product.",
        "cta_body": "Start in the simulator — a virtual $100,000 and no real money.", "cta_button": "Try the simulator",
    },
    "posts": [
        {"slug": "rehearse-a-rule", "kicker": "No-code rule builder", "a": "Rehearse a rule", "b": "before it runs.",
         "body": "In-sample and held-out results are shown separately, with the gap between them — and the page says plainly that it's not a promise about the future.",
         "visual": screen("37-rule-builder-rehearsal")},
        {"slug": "risk-limits", "kicker": "Risk limits", "a": "Limits the server", "b": "actually enforces.",
         "body": "Daily loss, drawdown, position size, sector concentration, trades per day — enforced server-side in the execution path. No order can bypass them.",
         "visual": screen("28-risk-limits", (200, 0, 1440, 760))},
        {"slug": "knowledge-with-sources", "kicker": "Knowledge base", "a": "Research", "b": "with receipts.",
         "body": "Retrieval shows which playbook or framework an answer came from, and how closely it matched.",
         "visual": screen("43-knowledge-rag")},
    ],
    "reel": {"hook_a": "Would you let an AI", "hook_b": "trade for you?",
             "end_a": "We'd let it read.", "end_b": "Code decides.", "end_sub": "Paper-trading simulation · not financial advice"},
}

if __name__ == "__main__":
    phase2.build(kit, content, b.OUT, video=not a.no_video)
    print("phase 2 done →", b.OUT)
