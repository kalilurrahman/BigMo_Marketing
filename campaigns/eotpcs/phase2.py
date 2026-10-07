"""EOT-PCS — month two. Facts from the README (BR codes) and training-kit screens:
Oracle values read-only (BR-003); SHA-256 checksums + version history; a replaced
document needs a reason; waivers and approvals are recorded; escalation sweep for
payments; customer portal is read-only. Pilot framing kept.

Run:  python3 campaigns/eotpcs/phase2.py [--no-video]
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
    col = (b.ORANGE if dark else b.SLATE) if accent else (b.WHITE if dark else b.INK)
    return b.head(img, xy, s, size, w, col=col)


kit = phase2.Kit(
    bg=lambda size, dark: b.bg(size, dark=dark),
    logo=lambda img, x, y, h, dark: b.logo(img, x, y, h, dark),
    head=_head,
    body=lambda img, xy, s, size, w, dark, col=None: b.para(img, xy, s, size, w, col=col or ("#D7DDE6" if dark else b.BODY)),
    kick=lambda img, xy, s, size, dark: b.kick(img, xy, s, size, b.ORANGE if dark else b.SLATE),
    cta=lambda img, x, y, s, size, dark: b.btn(img, x, y, s, size),
    foot=lambda img, W, H, m, dark, page: b.foot(img, W, H, m, 20, dark, page),
    lift=lambda base, im, xy, dark: b.lift(base, im, xy, dark),
    muted="#9AA1AB", muted_dark="#6F7B8F", accent=b.SLATE, accent_dark=b.ORANGE,
    body_font=lambda size: b.B.font(size),
)


def screen(name, crop=b.SIDEBAR):
    def v(w, max_h):
        return b.desk(name, w, max_h=max_h, crop=crop)
    return v


content = {
    "myths": {
        "kicker": "Export-ops myths", "title_a": "Four things exporters", "title_b": "accept as normal.",
        "sub": "They aren't. Here's what a controlled workflow does instead.",
        "items": [
            ("Re-keying invoice values from the ERP is just part of the job.", "Pull it. Don't type it.",
             "Customer, order lines and invoice values come from Oracle read-only — the number on the document is the number in the ERP."),
            ("The latest version is whichever file was emailed last.", "Every version, checksummed.",
             "Uploads carry a SHA-256 checksum and a version history. Replacing a document asks why — and keeps the old one."),
            ("Approval means someone replied 'ok' to an email.", "Approval is a recorded decision.",
             "A different person approves, rejects or waives — with the reason captured in an append-only audit trail."),
            ("Chasing payments is someone's spreadsheet.", "Balances chase themselves.",
             "Outstanding balances come from invoices and receipts; reminder rules and an escalation sweep do the follow-up."),
        ],
        "cta_a": "Retire the", "cta_b": "tracker spreadsheet.",
        "cta_body": "EOT-PCS is in pilot. Book a walkthrough on your own document rules.", "cta_button": "Book a walkthrough",
    },
    "posts": [
        {"slug": "document-versions", "kicker": "Document workspace", "a": "Which version", "b": "did we send?",
         "body": "Every upload is checksummed and versioned. Replacing one requires a reason, and the previous file stays on record.",
         "visual": screen("38-documents-versions")},
        {"slug": "waivers-recorded", "kicker": "Approvals", "a": "Waived? Fine.", "b": "Say why.",
         "body": "AI findings can be waived — by a checker, with a reason, on the record. Nothing disappears quietly.",
         "visual": screen("42-approvals-waive-dialog"), "dark": True},
        {"slug": "customer-portal", "kicker": "Customer portal", "a": "Fewer 'where's", "b": "my B/L?' emails.",
         "body": "Customers see their own shipments and released documents in a read-only portal.",
         "visual": screen("62-portal-customer")},
    ],
    "reel": {"hook_a": "Which version", "hook_b": "did we send?",
             "end_a": "From PI to paid.", "end_b": "One controlled record.", "end_sub": "EOT-PCS · v1 pilot · bigmoda.ai"},
}

if __name__ == "__main__":
    phase2.build(kit, content, b.OUT, video=not a.no_video)
    print("phase 2 done →", b.OUT)
