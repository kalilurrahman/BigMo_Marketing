# BigMo — umbrella campaign: "Seven products. One rule."

**What it is:** the parent-brand campaign. It introduces BigMo and shows all seven products as one portfolio, held together by the line every product actually enforces:

> **AI does the work. People make the call.**

Each product has its own version of that rule, taken from its own product docs:

| Product | Its version of the rule |
|---|---|
| LakshyaPrep | AI scans and plans; a 1:1 coach leads |
| AI MarketPulse | The AI interprets; deterministic code decides |
| DesiSquare | People answer; helpfulness earns standing |
| EOT-PCS | AI flags anomalies; maker and checker approve |
| Swaad | The AI copilot briefs the shop floor (read-only); staff decide |
| KPMRentals | AI triages and prices; owners and coordinators approve |
| Ledger Book | AI proposes; the ledger disposes |

**Brand:** the BiGMo lockup exactly as the products ship it (`eotpcs …/bigmo-logo.tsx`, MarketPulse `terminal.css`). It's Archivo 900: "BiG" in ink, an orange **M** `#FF6A2C`, a blue-soft **o** `#5C82FF`, and the blue double chevron `#2D5BFF`. The ground is midnight navy with oversized faint chevrons for momentum. The sign-off **"Get the Big Mo."** comes from the products' "Powered by BigMo" footer. Archivo is bundled (SIL OFL).

**Product cards** are each product's own campaign cover, read from `campaigns/<app>/output`, so every product keeps its own identity inside the portfolio. Build the seven product campaigns first, then this one.

## Claims discipline
- Say "seven products we build", **not** "seven launched products". EOT-PCS is labelled **pilot** and Ledger Book **early access**.
- No user counts, revenue, growth or customer logos.
- Each product's guardrails still apply wherever it is described. MarketPulse is paper-trading and not advice; DesiSquare is educational and not advice.

## Asset index (`output/`)

| Platform | File | Format | Use |
|---|---|---|---|
| Instagram | `instagram/carousel-portfolio/slide-01…09.png` | 1080×1350 | Launch: meet all seven |
| Instagram | `instagram/posts/post-01-manifesto.png` | 1080×1350 | The rule |
| Instagram | `instagram/posts/post-02-seven-products.png` | 1080×1350 | Portfolio grid |
| Instagram | `instagram/posts/post-03-get-the-big-mo.png` | 1080×1350 | Brand sign-off (light) |
| Instagram | `instagram/stories/story-01-quiz.png`, `story-02-manifesto.png` | 1080×1920 | Quiz sticker · manifesto |
| Instagram | `instagram/reel-seven-products-9x16.mp4` (+ cover) | 1080×1920, ~20 s | Sizzle reel |
| LinkedIn | `linkedin/video-sizzle-16x9.mp4` (+ cover) | 1920×1080, ~26 s | Company-page launch video |
| LinkedIn | `linkedin/document-seven-products-one-rule.pdf` | 9 pages | One page per product |
| LinkedIn | `linkedin/company-banner-1128x191.png` | 1128×191 | Company page cover (the left ~170 px is kept clear for the page logo) |
| LinkedIn | `linkedin/company-logo-400x400.png` | 400×400 | Company page logo |
| LinkedIn | `linkedin/images/link-01-portfolio.png` | 1200×627 | Link / image post |

## Copy

**LinkedIn company-page launch (with the sizzle video)**
> BigMo builds AI products for people who can't afford an AI that guesses.
>
> Students preparing for the SAT, ACT and MCAT. Retail investors and the desi diaspora. Exporters, small food brands, landlords and small businesses. Seven products so far: LakshyaPrep, AI MarketPulse, DesiSquare, EOT-PCS, Swaad, KPMRentals and Ledger Book.
>
> Different industries, one rule: AI does the work, people make the call. In every product, a person, a checker or deterministic code has the final say, and the record shows who decided what.
>
> Get the Big Mo. → bigmoda.ai
> #AI #ResponsibleAI #Startups #ProductStudio #EdTech #FinTech #PropTech

**LinkedIn document — "Seven products. One rule."**
> One page per product: what it does, who it's for, and exactly where the human stays in the loop.

**Instagram carousel**
> Seven products. One rule. 🔶 AI does the work. People make the call. Swipe to meet LakshyaPrep, AI MarketPulse, DesiSquare, EOT-PCS, Swaad, KPMRentals and Ledger Book. Which one is for you? 👇
> #BigMo #GetTheBigMo #AIStartup #BuildInPublic

**Story quiz:** "Which BigMo product should you try first?" with the options Students → LakshyaPrep, Investors → MarketPulse / DesiSquare, Exporters → EOT-PCS, Landlords → KPMRentals, Small business → Ledger Book.

## How it fits with the product campaigns
Post the umbrella launch **first** (LinkedIn company page + Instagram carousel). Then run each product's own 3-week plan. Every product post can end with "A BigMo company" or "Powered by BigMo", and the umbrella carousel gets a re-share each month.

## Regenerate
```bash
python3 campaigns/bigmo/build.py      # needs the seven product campaigns' output/ first
```
