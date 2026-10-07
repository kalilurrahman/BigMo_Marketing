# Ledger Book — campaign: "AI proposes. You approve. The ledger posts."

**Product:** Ledger Book (repo `LedgerBookPilot`), the AI bookkeeper from BigMo. It runs on a real double-entry engine (integer cents, balanced entries, immutable posted entries, corrections by reversal only) and has nineteen screens derived live from the journal. Its one rule: **AI proposes, ledger disposes.** The model never posts. A person approves, and a deterministic posting service validates every entry.

**Audiences**
- **Instagram:** freelancers, consultants and small-business owners. That's the product's first rollout lens: the demo persona is a consultancy, Jordan Blake at BigMo Consulting Services.
- **LinkedIn:** founders, accountants and bookkeepers, finance leads and fintech builders. The message is the trust architecture: how you let an AI near the books without letting it touch them.

**Brand:** taken from `src/styles.css`. Paper `#F4F5F2`, ink `#1D232C`, accent blue `#2B52C4`, with the ok/warn/crit greens, ambers and reds for confidence. The type is Inter. The logo is the blue "L" tile plus "Ledger Book". The background carries faint ledger ruling and a blue margin rule, the "book" in Ledger Book.

## Where the visuals came from
The repo had **no screenshots** (only a v0.1 wireframe that is marked historical), so I **ran the real app locally** in demo mode. With no `DATABASE_URL`, the server serves its seeded demo ledger. I captured the screens with headless Chromium (`capture.sh`) and cropped off the yellow "development environment" banner. The crops are committed in `assets/screens/` so the build is reproducible without running the app.

## Claims discipline
- **AI never posts.** Every line keeps the human approval step. The copilot line ("it can read and suggest, but cannot change anything" / "no tool exists that can post, send, or move money") is the product's own UI copy.
- **The tax set-aside is not tax advice.** The product calls it "a rule of thumb … not a tax calculation". The copy only says "a tax set-aside check".
- **No competitor is named.** The README pitches against QuickBooks, but comparative ads need substantiation, so the copy leaves the comparison out. There's also no "replaces your accountant" line and no time-saved or accuracy figures.
- The 0.95 auto-post threshold comes from the Today screen ("auto-posted without you (≥ 0.95 confidence)").
- All amounts, clients and transactions are **demo data**.
- No availability or pricing is claimed. The CTA is "See Ledger Book" or "Want an early look? team@bigmoda.ai". Swap in the real URL once there's a public one.

## Asset index (`output/`)

| Platform | File | Format | Use |
|---|---|---|---|
| Instagram | `instagram/carousel-ai-proposes/slide-01…07.png` | 1080×1350 | Lead: how it works in five steps |
| Instagram | `instagram/posts/post-01-debits-equal-credits.png` | 1080×1350 | Double-entry, enforced |
| Instagram | `instagram/posts/post-02-shows-its-work.png` | 1080×1350 | Review queue with reasons |
| Instagram | `instagram/posts/post-03-copilot-read-only.png` | 1080×1350 | "It can read. It can't touch." |
| Instagram | `instagram/posts/post-04-today.png` | 1080×1350 | "Are my books done?" |
| Instagram | `instagram/posts/post-05-close.png` | 1080×1350 | Month-end close checklist |
| Instagram | `instagram/stories/story-01…03.png` | 1080×1920 | Approve over coffee · reconcile poll · ask your books |
| Instagram | `instagram/reel-ai-proposes-9x16.mp4` (+ cover) | 1080×1920, ~13 s | Reel |
| LinkedIn | `linkedin/video-ai-proposes-16x9.mp4` (+ cover) | 1920×1080, ~22 s | "Would you let an AI post to your books?" |
| LinkedIn | `linkedin/document-six-rules-ai-bookkeeping.pdf` | 8 pages | "Six rules for an AI you can trust with your books" |
| LinkedIn | `linkedin/images/link-01…03.png` | 1200×627 | Launch · review queue · live reports |

The videos are silent; add audio in the app.

---

## Instagram copy

**1 · Carousel — how it works**
> AI proposes. You approve. The ledger posts. 📒
> 01 It reads the bank: a category, a confidence score and a reason for every line
> 02 Not sure? It asks you instead of guessing
> 03 Only balanced entries post, and posted entries can't be edited
> 04 Every number is computed live from the journal
> 05 Ask your books anything; the copilot can read but never move money
> Bookkeeping for freelancers and small businesses. Link in bio.

Hashtags: #Bookkeeping #SmallBusiness #Freelancer #Accounting #AIforBusiness #Solopreneur #FinanceTips #LedgerBook #BigMo

**Posts**
- **Debits = Credits:** "Debits = Credits. Always. Integer cents, balanced entries, posted entries immutable. Mistakes get reversed, on the record."
- **Shows its work:** "Every suggestion shows its work: a confidence score and a plain-English reason. Low confidence? It asks you."
- **Copilot:** "It can read. It can't touch. Ask about profit, who owes you or your runway, with no tool that can post, send or move money."
- **Today:** "'Are my books done?' One screen answers: cash, who owes you, what you owe, a tax set-aside check, and the next 13 weeks."
- **Close:** "Close the month with a checklist. Only real blockers hold it up."

**Stories:** 1 is "6 items waiting. Approve over coffee." (link sticker), 2 is the poll "When did you last reconcile your books? This week / This quarter / Don't ask", 3 is "Ask your books a question" (question sticker).
**Reel:** "Shoebox of receipts. Twelve bank tabs. Sound familiar? → AI proposes, with a reason → you approve, the ledger balances → every number always current." Pinned comment: "What's the one bookkeeping task you'd hand off first?"

## LinkedIn copy

**Video**
> Would you let an AI post to your books? Neither would we, so in Ledger Book it doesn't.
>
> The model proposes a category with a confidence score and a reason. Below the threshold, a person decides. A deterministic posting service accepts only balanced entries, posted entries are immutable, and corrections are reversals. Every balance and report is computed from the journal, never stored. The copilot has twelve read-only tools and nothing that can post, send or move money.
>
> AI proposes. The ledger disposes.
> #Accounting #AI #FinTech #Bookkeeping #SmallBusiness #AIGovernance

**Document — "Six rules for an AI you can trust with your books"**
> The model proposes and never posts · show the reason, not just the answer · debits equal credits, enforced not hoped · posted means posted · store nothing you can compute · give the copilot read-only tools. One page each, with the screen that implements it.

**Images:** link-01 is the launch line, link-02 the review queue (aimed at accountants and bookkeepers), link-03 "Reports computed, never stored" (finance leads).

## 3-week plan

| Week | Instagram | LinkedIn |
|---|---|---|
| 1 | Mon carousel · Wed reel · Fri debits=credits · review story | Tue video · Thu link-01 |
| 2 | Mon shows-its-work · Wed copilot · Fri today · poll story | Tue document · Thu founder post: "why our AI can't post" |
| 3 | Mon close · Wed reel re-share · Fri carousel re-cut | Tue link-02 · Thu link-03 |

**Measure:** early-access sign-ups (`utm_campaign=ledgerbook_launch`), document dwell and completion, accountant and bookkeeper enquiries, carousel saves.

## Regenerate
```bash
python3 campaigns/ledgerbook/build.py            # uses assets/screens/*.jpg
# fresh screens: run the app in demo mode (see capture.sh header), then
bash campaigns/ledgerbook/capture.sh             # raw PNGs → .cache/raw, then re-crop
```
