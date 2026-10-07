# Phase 2: month two, for all seven products

Month one launched each product (`campaigns/<app>/CAMPAIGN.md`). Month two goes deeper. Each product gets:

| Asset | File (in `campaigns/<app>/output/`) | Use |
|---|---|---|
| **Myth vs fact carousel** (6 slides) | `instagram/phase2/carousel-myths/slide-01…06.png` | The most-saved format; a cover, four myths, and a CTA |
| Same, as a LinkedIn document | `linkedin/phase2/document-myths.pdf` | LinkedIn document post (4:5 pages) |
| **Three feature deep-dives** | `instagram/phase2/post-01…03-<slug>.png` | Features month one didn't cover; also post them to LinkedIn and Facebook |
| **Month-two reel** (~12 s) | `instagram/phase2/reel-month2-9x16.mp4` (+ cover) | Hook → two features → end card. Also good for TikTok and Shorts |

All layouts come from one engine, `tools/phase2.py`, filled per product by `campaigns/<app>/phase2.py`. Every fact is traced to the product's own repo (docstring at the top of each file).

```bash
python3 campaigns/<app>/phase2.py          # --no-video for stills only
```

## What each product says in month two

| Product | Myths busted | Deep-dives |
|---|---|---|
| **LakshyaPrep** | More tests ≠ higher score · a scan is a map · every miss comes back · rehearse the clock | Review every miss · Lakshya Coach (AI reply, human confirms) · 1.5× / 2× time accommodation |
| **AI MarketPulse** | The AI only interprets · overrides can't skip the risk core · keyless-first · paper is the gate | Rehearse a rule (in-sample vs held-out) · server-enforced risk limits · research with receipts |
| **DesiSquare** | Percent, never dollars · helpfulness earns standing · flags are private · consent before WhatsApp | NRO alarm tool · FBAR / Form 8938 check · karma is never money |
| **EOT-PCS** | Pull from Oracle, don't type · every version checksummed · approval is a recorded decision · balances chase themselves | Document versions · waivers need a reason · read-only customer portal |
| **Swaad** (post-Deepavali) | Order-by dates · only delivered orders review · one restock alert · bulk tiers from 6 jars | Monthly Podi Box (17-podi rotation) · verified-purchase reviews · back-in-stock alerts |
| **KPMRentals** | Decisions wait for your morning · cost band on every ticket · sensors open the ticket · time-boxed guest passes | Sensor-raised tickets · smart-lock guest passes · unified inbox |
| **Ledger Book** | It proposes, you approve · corrections are reversals · every number is computed · the copilot can only read | Drafted invoice reminders · journal history · 13-week cash view |

**Deliberately left out:**
- KPMRentals' rent & finance, inspections and renewals screens are labelled *"Preview module — actions simulated"* in the app, so they are **not** marketed. Re-check when they go live.
- Swaad's review card illustrates the *rule* (who may review), not a review. The store shows no reviews yet, and no review or rating is invented.

## Month-two calendar (weeks 5–8)

| Week | Instagram | LinkedIn | Also |
|---|---|---|---|
| 5 | Mon myth carousel · Thu deep-dive 1 | Tue myth document (PDF) | Reel → TikTok/Shorts |
| 6 | Mon reel · Thu deep-dive 2 | Tue deep-dive 1 as an image post + founder comment | X: one myth per day as a text post |
| 7 | Mon deep-dive 3 · Thu month-one carousel re-share | Tue deep-dive 2 | Facebook: mirror the Instagram posts |
| 8 | Mon "which myth surprised you?" story + poll · Thu best performer, re-cut | Tue deep-dive 3 · Thu BigMo umbrella re-share | Review metrics; pick month-three angles |

**Caption pattern for a myth carousel:** "Myth: <myth 1>. Fact: <fact 1>. Swipe for three more 👉". Keep each product's guardrail line: MarketPulse "Paper-trading simulation · not financial advice"; DesiSquare "Educational community · not investment advice"; EOT-PCS "v1 pilot".
