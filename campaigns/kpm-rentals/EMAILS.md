# KPMRentals: rental-analysis lead nurture

**Trigger:** a free rental analysis is requested for a Tennessee property.
**Goal:** analysis delivered and read → owner call → owner onboarding.
**Exit:** as soon as a call is booked or onboarding starts, stop. Replies go to a person.
**Rules:**
- Memphis-first and Tennessee only.
- No rent figures or returns in the emails (the analysis itself carries the property-specific benchmark).
- No market statistics.
- Never describe stock photos as listings.
- AI recommends; a person approves.
**Timing:** owners abroad. Send at 8 a.m. in the **owner's** time zone, and capture it on the form (`{{owner_tz}}`).

| # | Day | Purpose |
|---|---|---|
| 1 | 0 | Analysis received / delivered |
| 2 | 2 | Decisions in your time zone |
| 3 | 5 | Every repair has a cost band |
| 4 | 9 | Humans in the middle (how AI is used) |
| 5 | 16 | Book a call |

---

### 1 · Day 0: Your rental analysis
**Subject:** Your rental analysis for {{property_address_short}} · *A/B:* What your Tennessee rental could earn
**Preview:** Market rent benchmark, days-to-lease estimate, onboarding plan.
```
Hi {{first_name}},

Thanks for requesting a rental analysis. Here's what's inside:
· a market rent benchmark for your property
· an estimated days-to-lease
· an onboarding plan if you'd like us to manage it

[Read your analysis →]

Questions? Just reply. A person on our Memphis team reads every one.
```

### 2 · Day 2: Decisions in your time zone
**Subject:** No more 2 a.m. calls · *A/B:* Decisions, in your morning
**Preview:** One digest, in your local time.
```
Hi {{first_name}},

Owning a rental from far away usually means late-night calls.

With KPMRentals, non-urgent decisions are batched into one morning digest in your own time zone. Each memo proposes a default ("we'll proceed with vendor B unless you object by 10:00") so you can approve in seconds or simply let it stand.

[See how owners approve →]
```

### 3 · Day 5: Every repair has a cost band
**Subject:** Is that repair quote fair? · *A/B:* Every ticket, priced against similar jobs
**Preview:** Outlier quotes are flagged.
```
Hi {{first_name}},

Every repair ticket arrives with a P50–P80 cost band benchmarked against similar Memphis jobs, and quotes outside the band are flagged. Vendors are scored on rework and cost variance, so underperformers are easy to spot and replace.

[See a sample ticket →]
```

### 4 · Day 9: Humans in the middle
**Subject:** How we use AI (and where we don't) · *A/B:* AI drafts it. A person decides.
**Preview:** Every step is logged and exportable.
```
Hi {{first_name}},

A fair question from remote owners: who's actually deciding?

At KPMRentals, AI triages each ticket, estimates the cost and suggests a vendor. A coordinator, or you, approves. Every AI suggestion and every human override is timestamped and exportable, so you can always see who decided what.

[Read how it works →]
```

### 5 · Day 16: Book a call
**Subject:** 20 minutes about your property? · *A/B:* Own in Memphis. Live anywhere.
**Preview:** We'll walk through the onboarding plan with you.
```
Hi {{first_name}},

If you're considering professional management for your Tennessee rental, let's walk through your onboarding plan together. It takes 20 minutes, at a time that suits your time zone.

[Book a call →]

If now isn't the right time, no problem. Your analysis stays in your inbox.
```
