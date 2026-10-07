# Email sequences

Each product has an automated sequence in `campaigns/<app>/EMAILS.md`, triggered by that product's real sign-up or lead action:

| Product | Trigger | Goal | Emails / length |
|---|---|---|---|
| [LakshyaPrep](campaigns/lakshyaprep/EMAILS.md) | Free account / free scan started | Scan done → goal locked → 1:1 coaching | 6 over 14 days, plus a parent branch |
| [AI MarketPulse](campaigns/marketpulse/EMAILS.md) | Simulator sign-up | First signal reviewed → risk limits set → paper-trading habit | 5 over 14 days |
| [DesiSquare](campaigns/desisquare/EMAILS.md) | New member | First question / first answer → weekly habit | 5 over 14 days |
| [EOT-PCS](campaigns/eotpcs/EMAILS.md) | Walkthrough request / pilot enquiry | Book the walkthrough → pilot | 5 over 18 days (B2B) |
| [Swaad](campaigns/swaad/EMAILS.md) | Subscriber / first order | Deepavali order before the deadline → review → Podi Box | 4 subscriber emails + 2 post-delivery |
| [KPMRentals](campaigns/kpm-rentals/EMAILS.md) | Free rental-analysis request | Analysis read → owner call → onboarding | 5 over 16 days |
| [Ledger Book](campaigns/ledgerbook/EMAILS.md) | Early-access waitlist | Understand the model → early-access invite | 4 over 21 days |

Each file gives: the trigger, the goal, **exit conditions** (stop as soon as the person does the thing), the cadence, and for every email the send day, a subject line with an A/B alternative, preview text, body, CTA and notes. Merge fields use `{{first_name}}` style. Every email ends with the same footer block (below).

## Rules that apply to every sequence
- **Consent and the law.** Send only to people who opted in. Every email needs a working one-click unsubscribe and the sender's physical postal address (CAN-SPAM; GDPR and CASL where EU or Canadian readers are on the list). Honour unsubscribes across the whole sequence immediately.
- **Product guardrails carry over from `POSTS.md`.**
  - MarketPulse: every email says "Paper-trading simulation · Not financial advice."
  - DesiSquare: every email says "Educational community · Not investment advice". Its emails never ask for, or confirm, a phone number, and WhatsApp is only ever an opt-in inside the product.
  - Swaad: never "organic" or "Made in USA", and no prices.
  - EOT-PCS is a pilot and Ledger Book is in early access.
  - No invented stats, testimonials, guarantees or returns.
- **One CTA per email.** Plain-text-style layouts get the best deliverability and reply rates for product emails. Keep images optional; if you use one, the campaign images in `output/` work.
- **Send times:** students in the afternoon or evening in their own time zone. B2B (EOT-PCS, KPMRentals PMCs, Ledger Book) Tuesday to Thursday, 9–11 a.m. in the recipient's time zone. Swaad in the evening and at weekends.
- **Measure:** open rate is unreliable since Apple Mail Privacy Protection, so judge each email by **click-through and the goal event** (scan finished, simulator signal reviewed, first question posted, walkthrough booked, order placed).

## Footer block (all emails)
```
—
{{product_name}} · a BigMo company · {{postal_address}}
You're getting this because you {{signup_reason}}. Unsubscribe in one click: {{unsubscribe_url}}
{{product_disclaimer}}   ← MarketPulse / DesiSquare only
```
