# DesiSquare — campaign: "Money questions. Desi answers."

**Product:** DesiSquare ("The Living Square") — a community for desi retail investors across six corridors (US, Canada, UK, UAE, Australia, Singapore), plus 100+ free public money tools.
**Positioning line (from the product):** *Where desi money questions get trusted answers — pseudonymous, percent-only, educational. Never investment advice.*
**Brand:** Porcelain Slate — the client-locked product theme (paper `#F5F6F8`, ink `#16181D`, peacock `#0C637C`), peacock diamond + "DesiSquare" wordmark, clean sans-serif.
**Audiences:** Instagram → desi professionals 24–40 abroad (H-1B, PR, NRI). LinkedIn → the same audience in a professional frame, plus community builders, fintech and CA/CPA/CFA professionals who could join as gurus.
**CTA:** Join free · Try the free tools

> **Product rules that bind this campaign** (from `desisquarev5-product/CLAUDE.md`):
> - **Educational, never investment advice.** "Educational community · Not investment advice" is on every asset; keep it in every caption.
> - **Say "Guru", never "Maven"** in anything member-facing.
> - **Never rank or brag by money.** No "top performers", no return figures in headlines, no leaderboard by returns. Credential-verified guru track records are opt-in and percent-only; they appear inside screenshots only, never as a selling claim.
> - **Privacy:** pseudonymous, percent-only, flags private, WhatsApp only with consent, no phone numbers anywhere.
> - The questions shown are threads from the product's demo community. They are presented as example questions, not as testimonials.
> - "100+ tools" is used deliberately: the product currently shows 102 in one place and 103 in another.

## Asset index (`output/`)

| Platform | File | Format | Use |
|---|---|---|---|
| Instagram | `instagram/carousel-desi-answers/slide-01…07.png` | 1080×1350 carousel | Launch: 5 reasons to join |
| Instagram | `instagram/posts/post-01-you-are-not-alone.png` | 1080×1350 | Question wall |
| Instagram | `instagram/posts/post-02-never-by-money.png` | 1080×1350 | Karma = helpfulness |
| Instagram | `instagram/posts/post-03-privacy.png` | 1080×1350 | Pseudonymous / percent-only |
| Instagram | `instagram/posts/post-04-free-tools.png` | 1080×1350 | "The Three That Matter This Year" tool |
| Instagram | `instagram/posts/post-05-six-corridors.png` | 1080×1350 | Six corridors |
| Instagram | `instagram/stories/story-01…03.png` | 1080×1920 | Ask · FCNR vs T-bills poll · brand |
| Instagram | `instagram/reel-ask-the-desi-9x16.mp4` (+ cover) | 1080×1920, ~14 s | Reel |
| LinkedIn | `linkedin/video-product-film-16x9.mp4` (+ cover) | 1920×1080, ~23 s | Native video |
| LinkedIn | `linkedin/document-six-rules-for-trust.pdf` | 8 pages, 1:1 | Document: "Six rules for a money community people can trust" |
| LinkedIn | `linkedin/images/link-01…03.png` | 1200×627 | Link / image posts |

The videos are silent (all words are on screen); add licensed audio in the app.

---

## Instagram copy

**1 · Carousel — Money questions. Desi answers.**
> NRE or NRO? FBAR due? RSUs vesting in two countries?
> You're not the only one asking.
>
> 01 Real questions, real threads
> 02 Helpfulness earns standing — never money
> 03 Gurus with verified credentials
> 04 Pseudonymous. Percent-only.
> 05 100+ free tools, no sign-in
>
> Join free — link in bio. Educational community · not investment advice.

Hashtags: #NRI #DesiInvestors #H1B #NRIInvesting #PersonalFinance #FBAR #DesiAbroad #IndianDiaspora #MoneyTalk #DesiSquare

**2 · Question wall** — "FCNR at 5.1%? Emergency fund on two visas? Mid-year H-1B tax moves? Someone's already asked — and members have answered. Read the thread, then decide for yourself."
**3 · Never by money** — "Your standing here comes from how helpful your answers are. Not your portfolio. Not your salary. Never."
**4 · Privacy** — "Your name? Optional. Your dollars? Private. Pseudonymous accounts, allocation in percent only, private flags, WhatsApp only if you opt in."
**5 · Free tools** — "Ten questions, none asking for an amount. 'The Three That Matter This Year' puts your NRI money deadlines in the order they actually close. Free, no account."
**6 · Six corridors** — "One square. Six corridors. US · Canada · UK · UAE · Australia · Singapore — each with its own communities and rules."

**Stories** — 1: link sticker "Join free" · 2: poll sticker "FCNR / T-bills / Both" + link to the thread · 3: brand close, no sticker.
**Reel** — "NRE or NRO? FBAR due? RSUs in two countries? Ask the desi who's been there. 🔷 Ranked by help, never by money. Free tools, no sign-in." Pinned comment: "Which money question do you wish someone had answered for you in year one abroad?"

## LinkedIn copy

**Video (launch)**
> Money advice is everywhere. Trusted answers are not — especially if you're a desi professional handling two tax systems, two sets of accounts and a visa.
>
> DesiSquare is a pseudonymous, percent-only community where members answer each other's cross-border money questions. Standing comes from helpfulness, never from wealth. Gurus are credential-verified. And 100+ public tools — FBAR, residency, the NRO alarm, the 60-day clock — are free with no sign-in.
>
> Educational community · not investment advice.
> #NRI #PersonalFinance #CommunityBuilding #FinTech #DesiDiaspora

**Document — "Six rules for a money community people can trust"**
> We built six rules into DesiSquare from day one: rank people by help, never money · keep flags private · percent, not dollars · verify credentials, not identities · consent before WhatsApp · give the tools away. Here's how each one shows up in the product.

**Guru recruitment (text post + link-02)**
> Are you a CFA, CPA, CA or financial planner who already answers NRI money questions for friends? DesiSquare verifies credentials (not identities) and lets you teach in public — percent-only, opt-in, educational. Message us to join as a guru.

**Images** — link-01: launch · link-02: trust/gurus · link-03: "100+ free tools, no sign-in".

## 3-week plan

| Week | Instagram | LinkedIn |
|---|---|---|
| 1 | Mon carousel · Wed reel · Fri question wall · stories daily | Tue video · Thu link-01 |
| 2 | Mon never-by-money · Wed free tools · Fri privacy · poll story | Tue document · Thu guru recruitment |
| 3 | Mon six corridors · Wed reel re-share · Fri carousel re-cut | Tue link-03 (tools) · Thu founder post on "why money never ranks anyone" |

Measure: sign-ups by corridor (`utm_campaign=ds_launch`), tool sessions from `/tools/*`, guru applications, carousel saves.

## Regenerate
```bash
python3 campaigns/desisquare/build.py --src ../desisquarev5-product   # --no-video for stills only
```
Screenshots come from `desisquarev5-product/docs/training-kit/screenshots/*.webp` (local demo build, commit 91ca081, seeded demo data).
