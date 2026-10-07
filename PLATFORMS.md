# Platform guide: X, Facebook, YouTube (incl. Shorts), TikTok

Every campaign already has Instagram and LinkedIn kits. This guide maps those assets onto the other four platforms. `tools/platforms.py` renders the few sizes that genuinely differ into `campaigns/<app>/output/platforms/`.

```bash
python3 tools/platforms.py            # all campaigns, or: python3 tools/platforms.py swaad ledgerbook
```

## Which file goes where

| Platform | Placement | Spec | Use this file (in `campaigns/<app>/output/`) |
|---|---|---|---|
| **X** | Image post | 1600×900 (16:9) | `platforms/x/post-NN-1600x900.png` (the LinkedIn link images, re-fit with their own background extended, nothing cropped) |
| X | Video | 16:9, ≤ 2:20 | `linkedin/video-*-16x9.mp4` |
| X | Vertical video | 9:16 | `instagram/reel-*-9x16.mp4` |
| X | Profile header | 1500×500 | `platforms/x-header-1500x500.png`. The left ~420 px is left clear because the avatar overlaps it |
| **Facebook** | Feed image / carousel | 4:5 (1080×1350) | `instagram/posts/*`, `instagram/carousel-*/*`. Facebook shows 4:5 natively |
| Facebook | Reels / Stories | 9:16 | `instagram/reel-*`, `instagram/stories/*` |
| Facebook | Feed video | 16:9 | `linkedin/video-*-16x9.mp4` |
| Facebook | Page cover | 1640×624 | `platforms/facebook-cover-1640x624.png`. The cards sit in the middle so both the desktop and mobile crops keep them |
| **YouTube** | Shorts | 9:16, ≤ 60 s | `instagram/reel-*-9x16.mp4` |
| YouTube | Video + thumbnail | 16:9 + 1280×720 | `linkedin/video-*-16x9.mp4` + `platforms/youtube-thumbnail-1280x720.png` |
| **TikTok** | Video | 9:16 | `instagram/reel-*-9x16.mp4`. Headlines sit in the upper half of every reel, clear of the caption area and the right-hand icon rail. Small footer lines and the bottom of phone mock-ups can sit under the UI, so preview before posting |
| **LinkedIn** (team profiles) | Personal banner | 1584×396 | `platforms/linkedin-banner-1584x396.png`, for founders and team members to add to their own profiles |

**Audio:** every video is silent with all words on screen. Add a licensed track in each app's own music library. TikTok and Shorts reach depends heavily on this, so do it there.

**Captions per platform**
- X: ≤ 280 characters. The copy below is pre-cut to fit.
- Facebook: reuse the Instagram caption from each campaign's `CAMPAIGN.md`, with hashtags trimmed to 3.
- YouTube: title ≤ 70 characters plus a description.
- TikTok: ≤ 150 characters plus 3–5 hashtags.

Every product guardrail in its `CAMPAIGN.md` still applies on every platform. MarketPulse is a paper-trading simulation and not advice. DesiSquare is educational and not advice. EOT-PCS is a pilot. Swaad says no "organic" and no "Made in USA". And no product copy invents figures.

---

## Copy by product

### BigMo (umbrella)
**X**
1. Seven products. One rule: AI does the work, people make the call. Meet LakshyaPrep, AI MarketPulse, DesiSquare, EOT-PCS, Swaad, KPMRentals and Ledger Book. bigmoda.ai
2. In every BigMo product, a person, a checker or deterministic code has the final say, and the record shows who decided what. Get the Big Mo.
3. Classrooms, trading desks, export offices, kitchens, rentals, ledgers. Different industries, same rule. 🔶

**YouTube:** "Seven AI products, one rule: people make the call | BigMo". Description: one line per product plus bigmoda.ai.
**TikTok:** "7 products. 1 rule. AI does the work, people make the call. #AI #startup #buildinpublic #BigMo"

### LakshyaPrep
**X**
1. 1600 is a target, not a vibe. 🎯 Take the free scan and see where your points leak, then lock one goal.
2. Stop studying everything. Scan → Lock → Grind → Land. Goal-based SAT, ACT and MCAT prep with live 1:1 coaching.
3. GoalGap ranks skills by the points they can still give you, not by how often you miss them.

**YouTube Shorts:** "POV: you stopped studying everything (SAT/ACT/MCAT) #shorts"
**TikTok:** "POV: you stopped studying everything 🎯 one goal, zero noise #SAT #ACT #MCAT #studytok #LakshyaPrep"

### AI MarketPulse
**X**
1. The AI interprets. Deterministic code decides. The broker executes. Everything is logged. Paper-trading simulation · not financial advice.
2. 17 pre-trade checks. Overrides can skip advisory checks, never the risk core. (Simulation · not advice)
3. Every trade has a receipt: trigger → research → bull/bear debate → signed guardrail report → verdict. One trace ID.

**YouTube:** "An AI trading agent with brakes: how the risk core decides | AI MarketPulse". Description must include: "Paper-trading simulation. Not financial advice. Educational use only."
**TikTok:** "AI that knows when NOT to trade. Paper-trading sim · not financial advice #fintech #AI #papertrading"

### DesiSquare
**X**
1. NRE or NRO? FBAR due? RSUs vesting in two countries? Ask the desi who's been there. Educational community · not investment advice.
2. Ranked by helpfulness. Never by money. Your standing comes from your answers, not your portfolio.
3. 100+ free NRI money tools, no sign-in: FBAR, residency, the NRO alarm, the 60-day clock.

**YouTube Shorts:** "NRE vs NRO? FBAR? Ask the desi who's been there #shorts" + the disclaimer in the description.
**TikTok:** "Money questions. Desi answers. Educational, not advice #NRI #desi #H1B #personalfinance"

### EOT-PCS (pilot)
**X**
1. Your export tracker shouldn't be a spreadsheet. One controlled record from proforma invoice to payment closure. Pilot open.
2. Missing a document? The package can't be submitted. Prepared it yourself? Someone else approves it. Enforced by the system.
3. Oracle stays the source of truth: invoice values are pulled read-only, never re-keyed.

**YouTube:** "From PI to paid: seven controls for export operations | EOT-PCS (pilot)"
**TikTok:** (lower priority for B2B) "Spreadsheets. Email threads. One shipment. #exporters #tradeops #MSME"

### Swaad
**X**
1. Deepavali is Sunday 8 Nov. 🪔 Mysore pak, adhirasam, murukku and gift boxes, made to order in Chennai and shipped across the US. Check each item's order-by date.
2. Karupatti halwa (கருப்பட்டி அல்வா): palm jaggery, slow-stirred in ghee until it holds a clean cut.
3. Mysore pak or adhirasam? Settle it below. 👇

**YouTube Shorts:** "Deepavali, half a world from Chennai 🪔 #shorts"
**TikTok:** "POV: Deepavali, half a world from Chennai 🪔 #Deepavali #Diwali #TamilInUSA #southindianfood #Swaad"

### KPMRentals
**X**
1. Own a rental in Memphis but live 13 time zones away? Decisions batched into one digest in your time zone, each with a cost band and a default action.
2. AI triages and prices the repair. A person approves. Every step is logged and exportable.
3. Free rental analysis for your Tennessee property: market rent benchmark, days-to-lease estimate, onboarding plan.

**YouTube:** "Your U.S. rentals, without the 2 a.m. calls | KPMRentals"
**TikTok:** "2:07 a.m. Kitchen faucet leaking. You don't need to be awake. #landlord #NRI #realestate #Memphis"

### Ledger Book (early access)
**X**
1. AI proposes. You approve. The ledger posts. An AI bookkeeper on a real double-entry engine, where model output never posts directly.
2. Debits = Credits. Always. Posted entries are immutable; mistakes are reversed, on the record.
3. The copilot can read your books and suggest. No tool exists that can post, send or move money.

**YouTube:** "Would you let an AI post to your books? | Ledger Book"
**TikTok:** "AI proposes. You approve. 📒 #bookkeeping #smallbusiness #freelancer #accounting"

---

## Posting order across platforms
1. **Week 0:** BigMo umbrella on LinkedIn (company page), X and Facebook. Update the profile headers and banners on X, Facebook and LinkedIn.
2. **Weeks 1–3:** each product follows its own `CAMPAIGN.md` plan on Instagram and LinkedIn. Mirror the same day's asset to Facebook (no rework), and the reel to TikTok and Shorts within 24 h.
3. **X:** post 1 of the three daily in week 1, then the other two in weeks 2 and 3. Pin the umbrella post.
