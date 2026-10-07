# Swaad — campaign: "The whole South Indian counter, shipped."

**Product:** Swaad, the storefront built on BigMo's niche-commerce platform (repo `niche-ecommerce-flow`, live at ecommerce-store.big-mo.ai). It sells 101 handmade South Indian sweets, savouries, podis, pickles, millets and gift boxes, made in small batches in a Chennai kitchen and shipped across the US.

**Two tracks**
- **Instagram (consumer, lead track):** desi families in the US, especially Tamil households. Built around the catalog's own product art, Tamil product names and the **Deepavali deadline (Sun 8 Nov 2026)**. The campaign goes out a month before the festival, and the product's festival calendar exists to answer one question: "will it arrive in time?"
- **LinkedIn (B2B):** BigMo's niche-commerce operating flow underneath Swaad: six order stages, catalog-as-code, festival deadlines, per-line quantity pricing, verified-buyer reviews and the read-only AI ops copilot. It's aimed at founders of niche and diaspora food brands and at D2C operators.

**Brand:** brand green `#087B61` with the white "S" tile (from `public/favicon.svg`), on a cream ground with a faint kolam dot grid, plus karupatti brown and haldi gold. Headlines are set in Source Serif 4, body text in Inter, and Tamil in Noto Serif Tamil (with proper shaping).

## Claims discipline — read before editing copy
These come from `src/lib/brand-config.ts` and `catalog/`:
- **Never say "organic" and never say "Made in USA".** Nothing in the catalog is certified organic, and everything is made in Chennai. The repo's screenshots predate that fix and still show "Organic Indian Sweets" in the header and "Made in USA" in the footer. That's why every screenshot here has its header cropped off and the cart/footer screens aren't used. **Recapture the screenshots** (`screenshots/capture.mjs`) once the live site matches the brand config.
- **Prices are admin-editable placeholders**, so no price is quoted in any copy. One LinkedIn page (doc page 6) shows a product screenshot with its placeholder price; swap it once real prices are set.
- **No health claims** (e.g. glycemic index) and **no delivery-speed or free-shipping promises.** Free shipping applies only to the slowest tier, so the copy just says "shipped across the US".
- "No refined sugar", "jaggery sweetened", "vegan" and "gluten-free" are product diet tags from the catalog and are used only on items that carry them.
- Festival dates come from `catalog/festivals.mjs`, where each entry is sourced.
- The 6+/12+/24+ quantity tiers come from `docs/bulk-and-events.md`.

## Asset index (`output/`)

| Platform | File | Format | Use |
|---|---|---|---|
| Instagram | `instagram/carousel-deepavali/slide-01…07.png` | 1080×1350 | **Lead post:** Deepavali sweets, savouries, gifts, order-by dates, quantity tiers |
| Instagram | `instagram/carousel-seven-counters/slide-01…09.png` | 1080×1350 | The seven collections, in English + Tamil |
| Instagram | `instagram/posts/post-01-karupatti-halwa.png` | 1080×1350 | Hero product |
| Instagram | `instagram/posts/post-02-idli-podi.png` | 1080×1350 | Hero product |
| Instagram | `instagram/posts/post-03-avakkai.png` | 1080×1350 | Hero product |
| Instagram | `instagram/posts/post-04-101-things.png` | 1080×1350 | Catalog mosaic |
| Instagram | `instagram/posts/post-05-this-or-that.png` | 1080×1350 | Engagement: Mysore pak or adhirasam? |
| Instagram | `instagram/stories/story-01…03.png` | 1080×1920 | Deepavali deadline · podi poll · missing home |
| Instagram | `instagram/reel-deepavali-counter-9x16.mp4` (+ cover) | 1080×1920, ~12 s | Product-art reel with Tamil names |
| LinkedIn | `linkedin/video-operating-flow-16x9.mp4` (+ cover) | 1920×1080, ~22 s | The operating flow |
| LinkedIn | `linkedin/document-made-to-order-operating-model.pdf` | 8 pages | "Running a made-to-order food brand across two continents" |
| LinkedIn | `linkedin/images/link-01…03.png` | 1200×627 | Storefront · pipeline · AI copilot |

The product art is rendered from `public/product-art/<SKU>.svg` (code-generated, no licensed or scraped images). The videos are silent; add music in the app. Instagram's library has licensed carnatic and Tamil festive tracks.

---

## Instagram copy

**1 · Carousel — Deepavali sweets, sorted early (post this week)**
> Deepavali is Sunday 8 Nov. 🪔 The sweet box, the karam box, the gift boxes for everyone you forgot — sorted, made to order in our Chennai kitchen and shipped across the US.
> Every product page shows when it ships; the festival calendar shows the last day to order.
> Buying for the whole family? 6+ of one item is 5% off, 12+ is 10%, 24+ is 15%.
> Link in bio.

Hashtags: #Deepavali #Diwali2026 #TamilInUSA #SouthIndianSweets #MysorePak #Adhirasam #Murukku #DesiInUSA #Chennai #Swaad

**2 · Carousel — Seven counters, one Chennai kitchen**
> Karupatti specials. Traditional sweets. Savouries. Podis. Pickles & thokkus. Millets. Gift boxes. 101 items, all in one place. Which counter are you starting with? 👇

**Posts**
- **Karupatti Halwa:** "Palm jaggery, slow-stirred in ghee until it holds a clean cut. கருப்பட்டி அல்வா — no refined sugar."
- **Idli Podi:** "A spoon of podi and some sesame oil turn idli, dosa or plain rice into dinner. Stone-ground, roasted to order."
- **Avakkai:** "The jar that goes back in your suitcase. Raw mango in mustard, chilli and gingelly oil."
- **101 things:** "101 things you miss from home. Which one is yours?"
- **This or that:** "Mysore pak or adhirasam? Settle it in the comments. MP or AD."

**Stories:** 1 is the Deepavali deadline (link sticker "Order by the deadline"), 2 is "Podi on idli: oil or ghee?" (poll sticker in the marked space), 3 is "Missing home? We ship the counter."
**Reel:** "POV: Deepavali, half a world from Chennai. → Mysore pak, karupatti halwa, butter murukku, idli podi, avakkai. The whole counter, shipped." Pinned comment: "Tag the person who always brings the murukku."

**Timing:** Navaratri is 9 Oct and Vijayadashami / Ayudha Puja is 20 Oct, so the Deepavali push should run **now through about 1 Nov**. Check each product's order-by date on the store before boosting any post.

## LinkedIn copy

**Video**
> A Chennai kitchen. Customers across the US. 101 made-to-order products.
>
> Swaad runs on BigMo's niche-commerce flow. Every order moves Order → Demand → Production → Supply → Fulfilment → Delivery on one record, with a board per role. The catalog is code (storefront, database seed and generated product art from one file). A festival calendar tells customers the last day to order. And an AI ops copilot answers staff questions using six read-only tools, with a SQL fallback when no model is configured.
>
> #DTC #Ecommerce #FoodBusiness #DiasporaBrands #AIinOperations #SupplyChain

**Document — "Running a made-to-order food brand across two continents"**
> Eight pages on the operating model behind Swaad: the six-stage flow, catalog-as-code, festival deadlines, quantity pricing customers can predict, trust signals (verified-buyer reviews, back-in-stock alerts that fire once) and an AI copilot that can read but never write.

**Images:** link-01 is the storefront ("a niche brand, fully operated"), link-02 the six-stage pipeline, link-03 the AI copilot ("ask the shop floor a question").
**CTA:** "Got a niche brand that needs to run like this? team@bigmoda.ai"

## 3-week plan

| Week | Instagram (lead) | LinkedIn |
|---|---|---|
| 1 (now) | Mon Deepavali carousel · Wed reel · Fri this-or-that · deadline story daily | Tue video |
| 2 | Mon seven counters · Wed karupatti halwa · Fri 101 things · podi poll | Tue document · Thu link-03 copilot |
| 3 (last order week) | Mon idli podi · Wed avakkai · Fri reel re-share + "last days to order" story | Tue link-02 pipeline · Thu link-01 |

**Measure:** sessions and orders from `utm_campaign=swaad_deepavali26`, saves on both carousels, comment volume on the this-or-that post, and LinkedIn enquiries to team@bigmoda.ai.

## Regenerate
```bash
python3 campaigns/swaad/build.py --src ../niche-ecommerce-flow   # --no-video for stills only
```
Product art is rasterised from the repo's SVGs with the bundled Chromium (`CHROME=` to override) into `.cache/art/` (git-ignored). Catalog facts are read from `assets/catalog.json`, which was exported from `catalog/*.mjs`. Re-export it if the catalog changes.
