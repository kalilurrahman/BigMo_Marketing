# KPMRentals — campaign: "Your U.S. rentals, without the 2 a.m. calls."

**Product:** KPMRentals (repo `kpm-rentals`, live at kpm-rentals.lovable.app) is AI-native, full-service property management for single-family rentals. It's Memphis-first and Tennessee-headquartered. One platform carries seven portals: public site, staff console, operations console, owner portal, resident portal, vendor portal and technician PWA.

**Audiences**
- **Instagram:** (1) **remote and NRI owners** of US rentals, the product's own "For remote owners" positioning ("a console designed for owners 13 time zones away"); (2) **residents**, who use one app for rent and repairs.
- **LinkedIn:** owners and investors in Memphis single-family rentals, plus **property-management companies** for the white-label offer ("Memphis property management, on your label").

**Brand:** taken from the product's `src/styles.css` and app icon. The palette is deep emerald `#064E3B`, warm cream `#F5F0E0` and brushed gold `#C9A84C` (used for frames and fills), with gold text on cream darkened to `#8A6D1E`. Headlines are DM Serif Display and body text is Fira Sans (both bundled, SIL OFL). Logo: the house-outline app icon plus "KPM" + "Rentals". Cream slides carry the gold hairline frame.

## Claims discipline
- The copy says **Memphis-first** and **Tennessee**, never "nationwide" as a present fact.
- **No prices, fees, returns, occupancy or market statistics** appear in the copy. The pricing page shows tiers, so confirm those with the business before using them.
- **The property photos** (`src/assets/hero/`) are the site's own hero imagery and look illustrative or generated. They're used as **mood imagery only**: no caption, address or "available now" claim is attached to any photo.
- **AI recommends, a person approves.** Every AI line keeps the human in the loop, matching the product's own "multi-agent loop with humans in the middle".
- Owner-feature copy ("AI-priced repairs", "Decisions, batched", "Default-and-confirm", "Vendor scoring", "Full audit trail") is lifted from `src/routes/owners.tsx`. That includes the "10:00 IST" example memo.
- The screens show demo data ("Dana", sample Memphis addresses). The dollar figures in the screenshots are demo values.
- Time zones were checked: 2 a.m. in Memphis is midday in India, so the story says "you don't need to be awake" rather than claiming the owner is asleep.

## Asset index (`output/`)

| Platform | File | Format | Use |
|---|---|---|---|
| Instagram | `instagram/carousel-remote-owners/slide-01…07.png` | 1080×1350 | Lead: five things that change for remote owners |
| Instagram | `instagram/posts/post-01-your-property.png` | 1080×1350 | Brand: "Your property. Our priority." |
| Instagram | `instagram/posts/post-02-residents.png` | 1080×1350 | Resident + technician apps |
| Instagram | `instagram/posts/post-03-dispatch.png` | 1080×1350 | Live dispatch |
| Instagram | `instagram/posts/post-04-humans-in-the-middle.png` | 1080×1350 | AI drafts, a person decides |
| Instagram | `instagram/posts/post-05-rental-analysis.png` | 1080×1350 | Lead gen: free rental analysis |
| Instagram | `instagram/stories/story-01…03.png` | 1080×1920 | 2 a.m. · residents · poll |
| Instagram | `instagram/reel-2am-calls-9x16.mp4` (+ cover) | 1080×1920, ~13 s | The 2 a.m. leak story |
| LinkedIn | `linkedin/video-remote-owners-16x9.mp4` (+ cover) | 1920×1080, ~20 s | Native video |
| LinkedIn | `linkedin/document-seven-portals.pdf` | 8 pages | "One platform, seven portals" |
| LinkedIn | `linkedin/images/link-01…03.png` | 1200×627 | Remote owners · AI loop · PMC white-label |

The videos are silent; add a licensed track in the app.

---

## Instagram copy

**1 · Carousel — For remote owners**
> Own a rental in Memphis but live 13 time zones away? 🏡
> 01 AI-priced repairs: a cost band on every ticket, outlier quotes flagged
> 02 Decisions batched into one morning digest, in your time zone
> 03 Default-and-confirm: silence is a valid answer
> 04 Vendors scored on rework and cost variance
> 05 Every AI suggestion and human override, on the record
> Free rental analysis — link in bio.

Hashtags: #NRI #NRIInvestors #RentalProperty #PropertyManagement #Memphis #Tennessee #RealEstateInvesting #Landlord #KPMRentals

**Posts**
- **Your property:** "Your property. Our priority. Tennessee-headquartered, full-service property management."
- **Residents:** "Rent, repairs, one app. Pay by ACH or card, report a repair with a photo, follow it live."
- **Dispatch:** "A technician, already on the way. Routes are planned each morning and technicians share their location while on a job."
- **Humans in the middle:** "AI drafts it. A person decides. Ticket in → AI triage and cost band → coordinator or owner approves → vendor dispatched → logged."
- **Rental analysis:** "What could your Tennessee rental earn? Free rental analysis: a market rent benchmark, days-to-lease estimate and onboarding plan."

**Stories:** 1 is "It's 2 a.m. in Memphis. You don't need to be awake." (link sticker "Free rental analysis"), 2 is the resident app, 3 is the poll "Do you own a rental back home, or here?"
**Reel:** "2:07 a.m. Kitchen faucet leaking. → AI triages it and prices it → dispatch routes a technician → you approve over breakfast." Pinned comment: "What's the worst 2 a.m. call you've had as a landlord?"

## LinkedIn copy

**Video (remote owners)**
> Owning a rental from far away usually means late-night calls, vague quotes and no record of who decided what.
>
> KPMRentals batches non-urgent decisions into one digest in the owner's time zone. Every repair arrives with a cost band benchmarked against similar Memphis jobs, and each memo proposes a default action the owner can approve in seconds or simply let stand. AI recommends; a coordinator or owner approves; everything is logged and exportable.
>
> Memphis-first. Free rental analysis at kpm-rentals.lovable.app
> #PropertyManagement #RealEstate #SFR #PropTech #NRI #Memphis

**Document — "One platform, seven portals"**
> How KPMRentals runs single-family rentals: owners approve in ten seconds, staff see every ticket in one pipeline, AI triage is a recommendation not a decision, dispatch routes technicians, sensors catch leaks before the call, and residents pay, report and track in one portal.

**Images:** link-01 is remote owners, link-02 the multi-agent loop with humans in the middle (PropTech and AI audience), link-03 the PMC white-label pitch.

## 3-week plan

| Week | Instagram | LinkedIn |
|---|---|---|
| 1 | Mon remote-owners carousel · Wed reel · Fri your-property · 2 a.m. story | Tue video · Thu link-01 |
| 2 | Mon humans-in-the-middle · Wed residents · Fri rental analysis · poll story | Tue document · Thu link-02 |
| 3 | Mon dispatch · Wed reel re-share · Fri carousel re-cut | Tue link-03 (PMC) · Thu founder post on "default-and-confirm" |

**Measure:** rental-analysis submissions (`utm_campaign=kpm_remote_owners`), owner sign-ups by country, carousel saves and PMC enquiries.

## Regenerate
```bash
(cd ../kpm-rentals && git lfs pull)     # screenshots are Git LFS objects
python3 campaigns/kpm-rentals/build.py --src ../kpm-rentals   # --no-video for stills only
```
