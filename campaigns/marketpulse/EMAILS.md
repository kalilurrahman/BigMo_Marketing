# AI MarketPulse: simulator onboarding sequence

**Trigger:** simulator account created. New accounts start with a virtual $100,000 and must acknowledge that it's a paper-trading simulation for education.
**Goal:** first signal reviewed → risk limits set → a regular paper-trading habit.
**Exit:** leave the sequence if they unsubscribe or stop logging in after email 5 (move them to a monthly digest instead).
**Every email ends with:** `Paper-trading simulation · Not financial advice · Educational use only.`
**Never:** claim returns, win rates or performance, or suggest that a specific trade is a good idea.

| # | Day | Purpose |
|---|---|---|
| 1 | 0 | Welcome: how it works |
| 2 | 1 | Read your first signal, and why it fired |
| 3 | 3 | Set your risk limits and find the kill switch |
| 4 | 7 | Rehearse a rule before it runs |
| 5 | 14 | The trace ID and the audit trail |

---

### 1 · Day 0: Welcome
**Subject:** The AI interprets. Code decides. · *A/B:* Your $100,000 simulator is ready
**Preview:** How a headline becomes a trade, or gets stopped.
```
Hi {{first_name}},

Your simulator account is live, with a virtual $100,000 and no real money involved.

Here's the one idea behind AI MarketPulse:
The AI reads the market (news, filings, messages) and proposes a structured signal.
Deterministic code decides, through 17 pre-trade checks.
Everything is logged.

[Open your dashboard →]

Paper-trading simulation · Not financial advice · Educational use only.
```

### 2 · Day 1: Your first signal
**Subject:** Why did this signal fire? · *A/B:* Every signal shows its work
**Preview:** Open one signal and read the "why" panel.
```
Hi {{first_name}},

Pick any signal on your Trade Signals page and open it. The "why" panel shows the rule that triggered it, the sources it read and the confidence.

You don't have to act on anything. Reading a few is the best way to see how the system thinks.

[Open Trade Signals →]

Paper-trading simulation · Not financial advice · Educational use only.
```

### 3 · Day 3: Set your limits
**Subject:** Set your brakes first · *A/B:* Where's the kill switch?
**Preview:** Daily loss, drawdown and position limits, all enforced by the server.
```
Hi {{first_name}},

Before you place a paper trade, set your limits in the Risk Cockpit: max daily loss, weekly drawdown, position size, sector concentration and trades per day.

They're enforced server-side. No order can bypass them, and a human override can skip advisory checks but never the risk core. The kill switch is one click away.

[Set my limits →]

Paper-trading simulation · Not financial advice · Educational use only.
```

### 4 · Day 7: Rehearse a rule
**Subject:** Test a rule before it runs · *A/B:* In-sample vs held-out, side by side
**Preview:** And why the gap between them matters.
```
Hi {{first_name}},

In the no-code Rule Builder you can rehearse a rule set on history before it ever runs. The results are split into in-sample and held-out, with the gap between them shown, and the page says plainly that it's not a promise about the future.

[Open the Rule Builder →]

Paper-trading simulation · Not financial advice · Educational use only.
```

### 5 · Day 14: Every trade has a receipt
**Subject:** One trace ID, headline to order · *A/B:* "Why did this happen?" has an answer
**Preview:** Follow one decision end to end.
```
Hi {{first_name}},

Every decision in AI MarketPulse carries a trace ID: trigger → research → bull/bear debate → signed guardrail report → verdict → order.

Open any TradeOS verdict and follow its lineage. That's what "auditable" means here.

[Open TradeOS →]

Paper-trading simulation · Not financial advice · Educational use only.
```
