# Swaad: Deepavali subscriber sequence + post-delivery

**Rules:**
- Never "organic" or "Made in USA". Everything is made in small batches in Chennai and shipped across the US.
- **No prices** (placeholders).
- No health claims, and no delivery-speed or free-shipping promises.
- Product descriptions come from the catalog.
- Before each send, **check the order-by dates** on the store (the festival calendar works them out per product) and quote the store's date, not a guess.

## A · Deepavali subscriber sequence
**Trigger:** joins the email list (pop-up, back-in-stock sign-up opt-in, or an Instagram link). **Window:** now → Deepavali (Sun 8 Nov).
**Goal:** place a Deepavali order before the last order-by date.
**Exit:** an order is placed → move to sequence B.

| # | When | Purpose |
|---|---|---|
| A1 | Day 0 | Welcome + the seven counters |
| A2 | +3 days | Deepavali order-by dates |
| A3 | +6 days | Gifting + quantity tiers |
| A4 | ~2 days before the last order-by date | Last call |

### A1 · Welcome
**Subject:** The whole South Indian counter, shipped · *A/B:* Vanakkam from Chennai 🪔
**Preview:** 101 sweets, savouries, podis, pickles and millets.
```
Hi {{first_name}},

Welcome to Swaad.

We make South Indian sweets, savouries, podis, pickles and millets in small batches in Chennai, and ship them across the US. Seven counters, 101 items, every name in English and Tamil.

[Browse the counters →]
```

### A2 · Order-by dates
**Subject:** Will your sweets make it for Deepavali? · *A/B:* Deepavali is Sunday 8 Nov
**Preview:** Every product shows its last day to order.
```
Hi {{first_name}},

Deepavali is Sunday 8 November. 🪔

Everything is made to order, so each product page shows its kitchen lead time and the festival calendar shows the last day to order for Deepavali. Mysore pak, adhirasam, murukku, mixture: check the date, then relax.

[See the festival calendar →]
```

### A3 · Gifting + quantity tiers
**Subject:** Boxes that say you remembered · *A/B:* Buying for the whole family?
**Preview:** Gift boxes, plus up to 15% off when you buy more of one item.
```
Hi {{first_name}},

The Grand Festival Hamper has eight items across sweets and savouries in one ribboned box. There's also the Sweet & Karam Box, the Karupatti Discovery Box and more.

Buying for family or the office? Quantity pricing is automatic on each item line: 6+ of one item is 5% off, 12+ is 10%, 24+ is 15%.

[Shop gift boxes →]
```

### A4 · Last call
**Subject:** Last days to order for Deepavali · *A/B:* {{last_order_date}} is the cut-off
**Preview:** After this, we can't promise it arrives in time.
```
Hi {{first_name}},

Quick one: {{last_order_date}} is the last day to order for Deepavali on most items (each product page shows its own date).

[Order now →]

Wishing you a bright Deepavali. 🪔
```

## B · Post-delivery
**Trigger:** order status is **Delivered**.

### B1 · 3 days after delivery: Review
**Subject:** How was the {{product_name}}? · *A/B:* One honest line helps
**Preview:** Only delivered orders can review, so yours counts.
```
Hi {{first_name}},

We hope the {{product_name}} tasted like home.

On Swaad, only customers whose order was delivered can review, so every review is from a real order. One honest line helps the next family choose.

[Write a review →]
```

### B2 · 10 days after delivery: Monthly Podi Box
**Subject:** Four jars a month. Never the same four. · *A/B:* Your podi shelf, sorted
**Preview:** A 17-podi rotation, starting with the everyday four.
```
Hi {{first_name}},

The Monthly Podi Box starts with the four podis a Tamil kitchen opens every week (idli podi, paruppu podi, rasam and sambar), then works outward through a 17-podi rotation. It's over a year before the same jar comes round again.

[See the Podi Box →]
```
