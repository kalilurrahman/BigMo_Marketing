# AI MarketPulse — campaign: "Risk control is the product."

**Product:** AI MarketPulse (repo `marketpulse-relay`) — AI-assisted market research and agentic trading with a deterministic risk core. Powered by BigMo.
**Core message (from the README):** *The AI interprets. Deterministic code decides. The broker executes. Everything is logged.*
**Brand:** taken from the product's own OG image — midnight navy, white "AI Market" + orange "Pulse", ECG pulse line orange → blue, Inter type.
**Audiences:** Instagram → self-directed retail investors and finance-curious 20–35s. LinkedIn → fintech builders, CTOs, risk/compliance and ops leaders.
**CTA:** Try the simulator · big-mo.ai

> **Compliance guardrails — keep on every post.** The product is a research and education tool running a paper-trading simulator. Every asset carries "Paper-trading simulation · Not financial advice · Educational use only". Never claim returns, win rates or performance. Any $ figure in a screenshot is **simulated demo data** (labelled where it is prominent). Don't call it "advice", "guaranteed", or "beat the market". Have compliance review the copy before paid promotion.

## Asset index (`output/`)

| Platform | File | Format | Use |
|---|---|---|---|
| Instagram | `instagram/carousel-signal-to-trade/slide-01…07.png` | 1080×1350 carousel | Launch: Ingest → Interpret → Debate → Gate → Log |
| Instagram | `instagram/posts/post-01-kill-switch.png` | 1080×1350 | Risk Cockpit, mobile |
| Instagram | `instagram/posts/post-02-17-gates.png` | 1080×1350 | The 17 pre-trade checks (typographic) |
| Instagram | `instagram/posts/post-03-paper-first.png` | 1080×1350 | Paper → live graduation |
| Instagram | `instagram/posts/post-04-trace-id.png` | 1080×1350 | TradeOS verdict "receipt" |
| Instagram | `instagram/stories/story-01…03.png` | 1080×1920 | Not-to-trade · paper contests · manifesto |
| Instagram | `instagram/reel-risk-control-9x16.mp4` (+ cover) | 1080×1920, ~14 s | Reel |
| LinkedIn | `linkedin/video-product-film-16x9.mp4` (+ cover) | 1920×1080, ~25 s | Native video |
| LinkedIn | `linkedin/document-agentic-trading-with-brakes.pdf` | 8 pages, 1:1 | Document post / field guide |
| LinkedIn | `linkedin/images/link-01…03.png` | 1200×627 | Link / image posts |

Videos are silent (on-screen type carries the message); add a licensed track in-app.

---

## Instagram copy

**1 · Carousel — signal to trade**
> The AI interprets. Code decides. 📈
> 01 Ingest — every source, one scored queue
> 02 Interpret — signals that show why they fired
> 03 Debate — bull vs bear, then a verdict
> 04 Gate — 17 deterministic checks, no bypass
> 05 Log — one trace ID from headline to order
> Start in the simulator. Link in bio.
> Paper-trading simulation · Not financial advice.

Hashtags: #AItrading #FinTech #RiskManagement #PaperTrading #StockMarket #AlgoTrading #Investing101 #MarketPulse #BigMo

**2 · Kill switch** — "One button. Everything stops. Loss budgets, drawdown caps and a kill switch you can actually reach. Paper-trading simulation · Not financial advice."
**3 · 17 gates** — "17 pre-trade checks. Zero exceptions. Overrides can skip advisory checks — never the risk core."
**4 · Paper first** — "Prove it on paper. Then earn live. A 5-criterion graduation ladder per asset class, with automatic demotion back to paper. (Demo account shown — simulated.)"
**5 · Trace ID** — "Every trade has a receipt. Trigger → research → debate → signed guardrail report → verdict → order."
**Stories** — 1: link sticker "Try the simulator" · 2: poll "Would you trade in a paper contest first? Yes / Already do" · 3: manifesto, no sticker.
**Reel** — "Headlines move fast. Your risk rules shouldn't. 🔁 AI reads every signal, 17 checks decide, paper first, always logged." Pinned comment: "What's the one rule you'd never let an AI override?"

## LinkedIn copy

**Video (launch)**
> Everyone is building AI agents that trade. Very few are building the brakes.
>
> In AI MarketPulse the language model never decides. It reads RSS, email, chat channels, Reddit and SEC filings and proposes a structured signal. A deterministic risk core — 17 pure-arithmetic pre-trade gates in a <50 ms budget — decides. Human overrides can skip advisory checks, never the risk core. Every verdict carries a trace ID from trigger to order.
>
> The AI interprets. Code decides. The broker executes. Everything is logged.
> #FinTech #AIagents #RiskManagement #TradingTechnology #Compliance

**Document — "Agentic trading, with brakes"**
> An 8-page field guide to separating what AI is good at (reading) from what code must own (deciding): five planes, explainable signals, bull/bear debate, 17 gates, and compliance postures that decide which features are even loaded.

**Images** — link-01: "AI-assisted research. Deterministic risk." · link-02: "Every trade has a trace ID — here's what's in the receipt." · link-03: "Risk control is the product: kill switch, loss budgets, paper → live graduation."

## 3-week plan

| Week | Instagram | LinkedIn |
|---|---|---|
| 1 | Mon carousel · Wed reel · Fri 17 gates · stories | Tue video · Thu document |
| 2 | Mon kill switch · Wed trace ID · Fri paper first · stories | Tue link-02 · Thu founder post: "why the LLM never decides" |
| 3 | Mon reel re-share · Wed carousel re-cut · Fri manifesto story | Tue link-03 · Thu link-01 |

Measure: simulator sign-ups (`utm_campaign=mp_launch`), carousel saves, document dwell/click-through, video completion.

## Regenerate
```bash
python3 campaigns/marketpulse/build.py --src ../marketpulse-relay   # add --no-video for stills only
```
Screenshots come from `marketpulse-relay/docs/training-kit/screenshots/*.webp` (captured with seeded demo data, commit 6232757).
