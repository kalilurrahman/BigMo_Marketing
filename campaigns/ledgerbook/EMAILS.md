# Ledger Book: early-access waitlist sequence

**Trigger:** joins the early-access waitlist (team@bigmoda.ai, LinkedIn or a website form).
**Goal:** understand the "AI proposes, ledger disposes" model → accept an early-access invite.
**Exit:** an invite is sent → move to onboarding. A reply → a person takes over.
**Rules:**
- The AI never posts.
- The tax set-aside is a rule of thumb, not advice.
- No competitor named, no "replaces your accountant", no time-saved or accuracy figures.
**Segments:** ask one question on sign-up ("freelancer / small business / accountant or bookkeeper"). Accountants get the A/B subject marked *(acct)*.

| # | Day | Purpose |
|---|---|---|
| 1 | 0 | Welcome: the one rule |
| 2 | 5 | When it isn't sure, it asks |
| 3 | 12 | Posted means posted |
| 4 | 21 | Your invite / what happens next |

---

### 1 · Day 0: The one rule
**Subject:** AI proposes. You approve. · *A/B (acct):* An AI bookkeeper that can't post
**Preview:** Why our AI never touches the journal directly.
```
Hi {{first_name}},

Thanks for joining the Ledger Book early-access list.

Ledger Book is built on one rule: AI proposes, the ledger disposes. The AI reads your bank and suggests a category with a confidence score and a reason. You approve. A deterministic posting service accepts only balanced entries, and every number on every screen is computed from the journal.

We'll be in touch as invites open.
— The Ledger Book team, BigMo
```

### 2 · Day 5: It asks when it isn't sure
**Subject:** "Needs a human." · *A/B:* Not sure? It asks you.
**Preview:** What happens when the evidence conflicts.
```
Hi {{first_name}},

Here's a real example from the review queue: a $1,200 payment matches one open invoice exactly, but the payer's name matches a different client.

Ledger Book doesn't guess. It says "the amount points one way and the name the other. Needs a human," and shows you both. High-confidence items can post on their own; anything uncertain waits for you.

[See how the review queue works →]
```

### 3 · Day 12: Posted means posted
**Subject:** Don't edit it. Reverse it. · *A/B (acct):* Immutable entries, reversals only
**Preview:** Why the ledger works like a ledger.
```
Hi {{first_name}},

In Ledger Book, posted entries can't be edited. A correction is a second entry that reverses the first, and both stay on the record.

That's how good books have always worked. It's also why you can trust every number: cash, profit, receivables and your 13-week runway are computed from the journal, never stored.

[Read the six rules (PDF) →]
```

### 4 · Day 21: Your invite / next steps
**Subject:** Your early-access spot · *A/B:* Ready to try Ledger Book?
**Preview:** What early access includes, and what we'll ask of you.
```
Hi {{first_name}},

{{#if invite_ready}}
Your early-access invite is ready. [Set up your books →]
{{else}}
Invites are going out in small groups so we can work closely with every early user. You're on the list, and we'll email you the moment your spot opens.
{{/if}}

Early access means: real books, direct access to the team, and your feedback shaping what we build next. Reply anytime with questions.
```
