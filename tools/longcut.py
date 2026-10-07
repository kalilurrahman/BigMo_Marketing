"""Video upgrade: 45–60 s narrated explainers with burned-in captions, for every campaign.

Each product gets a voiceover script (one line per scene). The scene shows one of the
campaign's own slides; the line is burned in as a caption and exported as .srt/.vtt, and
a read-aloud script with timings is written for whoever records the voiceover.

Per campaign, writes campaigns/<app>/output/video/:
  explainer-9x16.mp4    1080x1920 — Reels (≤90 s), TikTok, YouTube Shorts (≤60 s)
  explainer-1x1.mp4     1080x1080 — LinkedIn / Facebook feed
  explainer.srt, explainer.vtt   caption files (upload as captions too — LinkedIn autoplays muted)
  voiceover-script.md   lines + timecodes + delivery notes

Scene length follows the line: ~2.7 words/s + 0.9 s breathing room, min 3.6 s, so a
voiceover recorded at a natural pace drops straight in.

Run:  python3 tools/longcut.py [app ...]     (default: all)
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

import socialkit as sk

ROOT = Path(__file__).resolve().parents[1] / "campaigns"
INTER = "/usr/share/fonts/opentype/inter/"


def F(size, w="SemiBold"):
    return ImageFont.truetype(INTER + f"Inter-{w}.otf", size)


C = "instagram/carousel-"
P = "instagram/posts/"
P2 = "instagram/phase2/"

# (slide, voiceover line). Every line is a fact from the campaign's CAMPAIGN.md / phase2.py.
SCRIPTS = {
    "lakshyaprep": dict(title="LakshyaPrep — the Lakshya Method in 50 seconds", voice="Warm, upbeat coach. Smile on 'one goal'.", lines=[
        (C + "method/slide-01.png", "Everyone tells you to do more. More tests, more tabs, more noise."),
        (C + "method/slide-01.png", "LakshyaPrep does the opposite. One goal. Zero noise."),
        (C + "method/slide-02.png", "Scan. A short adaptive diagnostic shows where your points leak."),
        (C + "method/slide-03.png", "Lock. Put in your goal score and test date, and get a week-by-week route."),
        (C + "method/slide-04.png", "Grind. Live one-to-one sessions, drills and timed full-length mocks, re-planned every week."),
        (C + "method/slide-06.png", "GoalGap ranks your weak skills by the points they can still give you, not by how often you miss them."),
        (P2 + "post-01-review-every-miss.png", "Every miss comes back with your answer, the key, your time and the reason why."),
        (P2 + "post-03-time-accommodation.png", "Practice tests run on real timing, with standard, one-and-a-half or double time."),
        (C + "method/slide-05.png", "Land. Walk into test day with a pacing plan you've already rehearsed."),
        (C + "method/slide-07.png", "Practice test one is free with an account. Take the free scan at lakshyaprep dot com."),
    ]),
    "marketpulse": dict(title="AI MarketPulse — how a headline becomes a trade (or doesn't)", voice="Calm, precise, trustworthy. Never hype returns.", lines=[
        (C + "signal-to-trade/slide-01.png", "Markets talk all day. Most of it is noise."),
        (C + "signal-to-trade/slide-02.png", "AI MarketPulse reads RSS, email, Telegram, Reddit and SEC filings into one scored queue."),
        (C + "signal-to-trade/slide-03.png", "The AI turns each item into a structured signal, and shows why it fired."),
        (C + "signal-to-trade/slide-04.png", "TradeOS runs research and a bull-versus-bear debate before reaching a verdict."),
        (C + "signal-to-trade/slide-05.png", "Then seventeen deterministic pre-trade checks decide. Overrides can't bypass the risk core."),
        (P + "post-01-kill-switch.png", "Loss limits, drawdown caps, and a kill switch you can actually reach."),
        (P + "post-03-paper-first.png", "Everything starts on paper. Going live means meeting a published five-step ladder."),
        (C + "signal-to-trade/slide-06.png", "Every decision carries one trace ID, from headline to order."),
        (C + "signal-to-trade/slide-07.png", "The AI interprets. Code decides. Everything is logged."),
        (C + "signal-to-trade/slide-07.png", "Paper-trading simulation. Not financial advice. Educational use only."),
    ]),
    "desisquare": dict(title="DesiSquare — money questions, desi answers", voice="Friendly, peer-to-peer, unhurried. Light Indian-English warmth welcome.", lines=[
        (C + "desi-answers/slide-01.png", "NRE or NRO? Is FBAR due? RSUs vesting in two countries?"),
        (P + "post-01-you-are-not-alone.png", "You're not the only one asking. On DesiSquare, desi investors abroad answer each other."),
        (C + "desi-answers/slide-03.png", "Standing comes from how helpful your answers are. Never from how much money you have."),
        (C + "desi-answers/slide-04.png", "Gurus are credential-verified, and their track records are opt-in and percent-only."),
        (P + "post-03-privacy.png", "Your name is optional. Public pages show percent, never dollars. Flags stay private."),
        (P2 + "post-01-nro-alarm.png", "Moved abroad? The free NRO tool tells you which accounts should have changed."),
        (P2 + "post-02-fbar-check.png", "Not sure about FBAR or Form 8938? One free check covers both, with no sign-in."),
        (P + "post-05-six-corridors.png", "One square, six corridors: US, Canada, UK, UAE, Australia and Singapore."),
        (C + "desi-answers/slide-07.png", "DesiSquare. Read before you decide."),
        (C + "desi-answers/slide-07.png", "Educational community. Not investment advice."),
    ]),
    "eotpcs": dict(title="EOT-PCS — from proforma invoice to payment, one controlled record", voice="Confident, operational, B2B. Medium pace.", lines=[
        (C + "pi-to-paid/slide-01.png", "Every export shipment lives in ten places: a spreadsheet, the ERP, a shared drive and a dozen inboxes."),
        (C + "pi-to-paid/slide-01.png", "EOT-PCS puts it in one controlled record, from proforma invoice to payment."),
        (C + "pi-to-paid/slide-02.png", "Customer, order and invoice values come from Oracle, read-only. Nothing is re-keyed."),
        (C + "pi-to-paid/slide-03.png", "Rules decide which documents each shipment needs: customer, country, Incoterms and transport."),
        (C + "pi-to-paid/slide-04.png", "If a mandatory document is missing, the package simply can't be submitted."),
        (C + "pi-to-paid/slide-05.png", "The person who prepared it can never approve it. AI findings are flagged first."),
        (P2 + "post-01-document-versions.png", "Every upload is checksummed and versioned, and replacing one needs a reason."),
        (C + "pi-to-paid/slide-06.png", "Balances, reminders and escalations run themselves, and every action is in the audit log."),
        (C + "pi-to-paid/slide-07.png", "EOT-PCS is in pilot with BigMo. Book a walkthrough on your own document rules."),
    ]),
    "swaad": dict(title="Swaad — the South Indian counter, shipped", voice="Warm, homely, a little nostalgic. Tamil names pronounced properly.", lines=[
        (C + "deepavali/slide-01.png", "Deepavali, half a world away from Chennai."),
        (C + "deepavali/slide-02.png", "Swaad makes Mysore pak, adhirasam and the whole sweet counter, in small batches in Chennai."),
        (C + "deepavali/slide-03.png", "Murukku twisted by hand, ribbon pakoda, and the mixture that disappears first."),
        (P + "post-01-karupatti-halwa.png", "Karupatti halwa: palm jaggery, slow-stirred in ghee until it holds a clean cut."),
        (C + "deepavali/slide-05.png", "Every festival has an order-by date, worked out from each item's kitchen lead time."),
        (C + "deepavali/slide-06.png", "Buying for the family? Six or more of one item takes five percent off that line, up to fifteen."),
        (P2 + "post-01-podi-box.png", "And the Monthly Podi Box: four jars a month, never the same four."),
        (P + "post-04-101-things.png", "One hundred and one things you miss from home, shipped across the US."),
        (C + "deepavali/slide-07.png", "Swaad. The whole South Indian counter, shipped."),
    ]),
    "kpm-rentals": dict(title="KPMRentals — your U.S. rentals, without the 2 a.m. calls", voice="Reassuring, composed. Slow on the 2 a.m. line.", lines=[
        (C + "remote-owners/slide-01.png", "Own a rental in Memphis but live thirteen time zones away?"),
        (C + "remote-owners/slide-01.png", "It's two a.m. The kitchen faucet is leaking. You don't need to be awake."),
        (C + "remote-owners/slide-02.png", "Every repair arrives with a cost band benchmarked against similar Memphis jobs."),
        (C + "remote-owners/slide-03.png", "Non-urgent decisions are batched into one morning digest, in your own time zone."),
        (C + "remote-owners/slide-04.png", "Each memo proposes a default. Approve in seconds, or simply let it stand."),
        (P + "post-04-humans-in-the-middle.png", "AI triages and prices. A coordinator or owner approves. Every step is logged."),
        (P2 + "post-01-sensors-open-tickets.png", "Leak and HVAC sensors can open a ticket before anyone has to phone."),
        (P + "post-02-residents.png", "Residents pay rent and report repairs with a photo, all from one app."),
        (C + "remote-owners/slide-07.png", "Own in Memphis, live anywhere. Start with a free rental analysis."),
    ]),
    "ledgerbook": dict(title="Ledger Book — AI proposes, you approve, the ledger posts", voice="Clear, dry, quietly confident. Like a good accountant.", lines=[
        (C + "ai-proposes/slide-01.png", "Would you let an AI post to your books? Neither would we. So in Ledger Book, it doesn't."),
        (C + "ai-proposes/slide-02.png", "It reads your bank, and every line gets a suggested category, a confidence score and a reason."),
        (C + "ai-proposes/slide-03.png", "When it isn't sure, it asks you instead of guessing."),
        (C + "ai-proposes/slide-04.png", "Only balanced entries post. Debits equal credits, every time."),
        (P2 + "post-02-journal-history.png", "Posted entries can't be edited. Mistakes are reversed, and both stay on the record."),
        (C + "ai-proposes/slide-05.png", "Cash, profit and your thirteen-week runway are computed live from the journal."),
        (C + "ai-proposes/slide-06.png", "The copilot can read your books and suggest. It has no tool that can post, send or move money."),
        (P2 + "post-01-invoice-reminders.png", "Invoice reminders are drafted for you. Nothing goes out until you send it."),
        (C + "ai-proposes/slide-07.png", "Ledger Book. AI proposes. The ledger disposes."),
    ]),
    "bigmo": dict(title="BigMo — seven products, one rule", voice="Founder voice. Measured, proud, no hype.", lines=[
        (C + "portfolio/slide-01.png", "BigMo builds AI products for people who can't afford an AI that guesses."),
        (C + "portfolio/slide-02.png", "LakshyaPrep: AI scans and plans your SAT, ACT or MCAT route. A one-to-one coach leads."),
        (C + "portfolio/slide-03.png", "AI MarketPulse: the AI interprets the market. Deterministic code decides."),
        (C + "portfolio/slide-04.png", "DesiSquare: desi investors abroad answer each other, ranked by helpfulness, never money."),
        (C + "portfolio/slide-05.png", "EOT-PCS: AI flags the export paperwork. A maker and a checker approve."),
        (C + "portfolio/slide-06.png", "Swaad: an AI copilot briefs the shop floor. The staff decide."),
        (C + "portfolio/slide-07.png", "KPMRentals: AI triages and prices the repair. The owner approves."),
        (C + "portfolio/slide-08.png", "Ledger Book: AI proposes. The ledger disposes."),
        (C + "portfolio/slide-09.png", "Seven products. One rule. AI does the work. People make the call."),
        (C + "portfolio/slide-09.png", "Get the Big Mo, at bigmoda dot ai."),
    ]),
}


def dur(line):
    return max(3.6, len(line.split()) / 2.7 + 0.9)


def contain(im, box_w, box_h):
    s = min(box_w / im.size[0], box_h / im.size[1])
    return im.resize((int(im.size[0] * s), int(im.size[1] * s)), Image.LANCZOS)


def caption(img, text, cx, y, max_w, size):
    """Subtitle style: white semibold on a translucent dark box, centred, max 2 lines."""
    f = F(size)
    lines = sk.wrap(f, text, max_w - 2 * int(size * .7))
    while len(lines) > 3 and size > 26:
        size -= 2
        f = F(size)
        lines = sk.wrap(f, text, max_w - 2 * int(size * .7))
    lh = int(size * 1.32)
    bw = int(max(f.getlength(l) for l in lines)) + 2 * int(size * .7)
    bh = lh * len(lines) + int(size * .8)
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    x0 = int(cx - bw / 2)
    d.rounded_rectangle([x0, y, x0 + bw, y + bh], int(size * .4), fill=(10, 12, 18, 205))
    for i, l in enumerate(lines):
        d.text((cx - f.getlength(l) / 2, y + int(size * .4) + i * lh), l, font=f, fill=(255, 255, 255, 255))
    img.alpha_composite(lay)


def frame(slide_path, text, size):
    W, H = size
    im = Image.open(slide_path).convert("RGB")
    # background: the slide itself, blurred and darkened (keeps every product on-brand)
    s = max(W / im.size[0], H / im.size[1])
    bgim = im.resize((int(im.size[0] * s) + 1, int(im.size[1] * s) + 1)).crop((0, 0, W, H))
    bgim = bgim.filter(ImageFilter.GaussianBlur(W // 25)).convert("RGBA")
    bgim.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 140)))
    if H > W:   # 9:16 — slide high, caption in the middle band, bottom ~20% clear for app UI
        fg = contain(im, W - 120, int(H * .62))
        top = int(H * .07)
        cap_y, cap_size = top + fg.size[1] + 50, 46
    else:       # 1:1 — slide left-of-centre top, caption under it
        fg = contain(im, W - 200, int(H * .70))
        top = int(H * .04)
        cap_y, cap_size = top + fg.size[1] + 28, 38
    sk.shadow_paste(bgim, sk.rounded(fg, 14), ((W - fg.size[0]) // 2, top), blur=30, opacity=140)
    caption(bgim, text, W // 2, cap_y, W - 120, cap_size)
    return bgim


def tc(t, sep=","):
    t = round(t, 3)
    h, m, s = int(t // 3600), int(t % 3600 // 60), t % 60
    return f"{h:02d}:{m:02d}:{int(s):02d}{sep}{int(round((s - int(s)) * 1000)):03d}"


def run(app, video=True):
    spec = SCRIPTS[app]
    o = ROOT / app / "output"
    out = o / "video"
    out.mkdir(parents=True, exist_ok=True)
    for p, _ in spec["lines"]:
        if not (o / p).exists():
            raise SystemExit(f"{app}: missing {p} — build the campaign (and its phase2) first")
    # captions + script (timings account for the 0.4 s cross-fade overlap)
    t, srt, vtt, md = 0.0, [], ["WEBVTT", ""], [f"# Voiceover script — {spec['title']}", "",
                                                     f"**Delivery:** {spec['voice']}", "",
                                                     "Record each line to roughly its slot; the video holds each slide for the line's length. "
                                                     "Leave ~0.4 s between lines (the cross-fade).", "",
                                                     "| # | In | Out | Line | On screen |", "|---|---|---|---|---|"]
    xf = 0.4
    for i, (p, line) in enumerate(spec["lines"], 1):
        d = dur(line)
        a, z = t, t + d - (xf if i < len(spec["lines"]) else 0)
        srt += [str(i), f"{tc(a)} --> {tc(z)}", line, ""]
        vtt += [f"{tc(a, '.')} --> {tc(z, '.')}", line, ""]
        md.append(f"| {i} | {tc(a)[3:8]} | {tc(z)[3:8]} | {line} | `{p.split('/')[-2]}/{p.split('/')[-1]}` |")
        t += d - xf
    total = t + xf
    md += ["", f"**Total:** {total:.0f} s · fits Reels (≤ 90 s), TikTok, Shorts (≤ 60 s) and LinkedIn.", "",
           "Captions are burned into both videos; also upload `explainer.srt` (LinkedIn, Facebook, YouTube) so the platform's own captions work for accessibility."]
    (out / "explainer.srt").write_text("\n".join(srt))
    (out / "explainer.vtt").write_text("\n".join(vtt))
    (out / "voiceover-script.md").write_text("\n".join(md) + "\n")
    if video:
        for size, name in [(sk.IG_STORY, "explainer-9x16.mp4"), ((1080, 1080), "explainer-1x1.mp4")]:
            scenes = [sk.Scene(frame(o / p, line, size), dur(line), move="in", zoom=1.035) for p, line in spec["lines"]]
            sk.render_video(scenes, size, out / name, xfade=xf)
        sk.save(frame(o / spec["lines"][0][0], spec["lines"][0][1], sk.IG_STORY), out / "explainer-cover-9x16.png")
    return total


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    video = "--no-video" not in sys.argv
    for a in args or list(SCRIPTS):
        print(a, f"{run(a, video):.1f}s")
