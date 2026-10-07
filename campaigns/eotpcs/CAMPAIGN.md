# EOT-PCS — campaign: "From PI to paid. One controlled record."

**Product:** EOT-PCS, the Export Order-to-Payment Control System by BigMo. It replaces Excel export trackers and email threads with one auditable workflow: proforma invoice → production & QC → dispatch → documents → maker-checker approval → customer release → payment closure. Oracle ERP stays the read-only system of record.
**Stage:** v1 pilot. **This is a B2B campaign, so LinkedIn leads** and Instagram supports it (exporters, MSME owners, trade-ops people).
**Brand:** taken from the product's own screens. The ground is navy (login screen and sidebar) and the app surface is light slate. "EOT-" is white or ink and "PCS" is orange (`#FF6A2C`). The BigMo lockup keeps its blue chevrons. The faint dotted "route" line on light slides stands for a shipment's path.
**Audiences:** export operations managers, export finance / receivables, CFOs and owners of manufacturing exporters, and ERP (Oracle) teams.
**CTA:** Book a walkthrough · bigmoda.ai

> **Truthfulness guardrails:** No customer names, time-saved figures or ROI claims. The product is in pilot, and the copy says so. All shipments, customers and amounts in the screenshots are demo data (DEMO-SHP-…, "Demo Customer One"). Business-rule codes (BR-004, BR-005) are product facts and can be quoted.

## Asset index (`output/`)

| Platform | File | Format | Use |
|---|---|---|---|
| LinkedIn | `linkedin/video-product-film-16x9.mp4` (+ cover) | 1920×1080, ~23 s | Native video, launch |
| LinkedIn | `linkedin/document-seven-controls-playbook.pdf` | 8 pages, 1:1 | Document post: "Seven controls between a PI and a payment" |
| LinkedIn | `linkedin/images/link-01-launch.png` / `02-documents` / `03-approvals` | 1200×627 | Image / link posts |
| Instagram | `instagram/carousel-pi-to-paid/slide-01…07.png` | 1080×1350 carousel | Five controls |
| Instagram | `instagram/posts/post-01-before-after.png` | 1080×1350 | Spreadsheet vs. system |
| Instagram | `instagram/posts/post-02-eight-stages.png` | 1080×1350 | Lifecycle state machine |
| Instagram | `instagram/posts/post-03-maker-checker.png` | 1080×1350 | Self-approval refused (BR-005) |
| Instagram | `instagram/posts/post-04-audit.png` | 1080×1350 | Append-only audit log |
| Instagram | `instagram/stories/story-01…03.png` | 1080×1920 | Control board · rule checklist · customer portal |
| Instagram | `instagram/reel-pi-to-paid-9x16.mp4` (+ cover) | 1080×1920, ~14 s | Reel |

The videos are silent, with all the words on screen. Add a licensed track in the app before posting.

---

## LinkedIn copy

**1 · Video (launch)**
> Every export shipment lives in ten places: a tracker spreadsheet, the ERP, a shared drive, three inboxes and someone's memory.
>
> EOT-PCS puts it in one. One shipment ID from proforma invoice to payment. Oracle stays the read-only source of truth. Document checklists come from rules (customer, country, Incoterms, product, payment terms, transport). Incomplete packages can't be submitted. The person who prepared a package can never approve it. Payments are tracked against invoices and escalate on their own, and every action lands in an append-only audit log.
>
> We're running EOT-PCS as a pilot with BigMo. If you run export operations and want to see it on your own document rules, comment "walkthrough" or message me.
> #ExportManagement #TradeOperations #OracleERP #Exporters #FinanceOps #Compliance #DigitalTransformation

**2 · Document: "Seven controls between a PI and a payment"**
> Most export delays and payment leaks come from the same gaps: re-keyed numbers, a missing certificate, a package approved by the person who made it, a balance nobody chased. Here are the seven controls we built into EOT-PCS to close them, one page each.

**3 · Image posts**
- **link-02-documents:** "Which documents does this shipment need? In most export teams, that answer lives in one person's head. In EOT-PCS, the rules decide, and submission is blocked until the package is complete."
- **link-03-approvals:** "Maker ≠ checker, enforced by the system rather than a policy PDF. Plus AI advisory findings that compare documents (e.g. a consignee mismatch between the packing list and the PI) before a second person approves."
- **link-01-launch:** recap or re-share with the walkthrough CTA.

**4 · Founder text post (no image)**
> Why we kept Oracle as the system of record instead of replacing it: ERP owns the numbers; EOT-PCS owns the process. Nothing financial is re-keyed, and nothing about the process lives in email.

## Instagram copy

**Carousel — From PI to paid**
> Your export tracker shouldn't be a spreadsheet. 5 controls that keep every shipment moving, from PI to payment:
> 01 Oracle stays the source of truth
> 02 Checklists that write themselves
> 03 Missing a document? It can't be submitted
> 04 The maker can never be the checker
> 05 Payments chase themselves
> Pilot open, link in bio.

Hashtags: #Exporters #ExportBusiness #TradeOps #MSME #SupplyChain #Logistics #B2B #BigMo

**Posts**
- **Before / after:** "Excel tracker → one shipment ID. Email threads → rule-based checklist. 'Who approved this?' → maker-checker. 'Is it paid yet?' → live balance."
- **Eight stages:** "Eight stages. No skipping. Every transition is checked on the server and logged."
- **Maker-checker:** "You prepared it? Someone else approves it. The system refuses self-approval."
- **Audit:** "Every click leaves a receipt."

**Stories:** 1 is the control board (link sticker "Book a walkthrough"), 2 is the rules checklist (poll: "How do you track export docs today? Excel / ERP / Email"), 3 is the customer portal.
**Reel:** "Spreadsheets. Email threads. One shipment. → EOT-PCS: from PI to paid, one controlled record."

## 3-week plan

| Week | LinkedIn (lead) | Instagram |
|---|---|---|
| 1 | Tue video · Thu document | Mon carousel · Thu reel |
| 2 | Tue link-02 documents · Thu founder post (Oracle as system of record) | Mon before/after · Thu maker-checker · stories |
| 3 | Tue link-03 approvals · Thu link-01 recap + walkthrough CTA | Mon eight stages · Thu audit |

**Measure:** walkthrough requests (`utm_campaign=eotpcs_pilot`), document-post completion rate, comments asking "walkthrough", and profile visits from export-industry titles.

## Regenerate
```bash
python3 campaigns/eotpcs/build.py --src ../eotpcs-export-order-to-payment-control-system   # --no-video for stills
```
Screenshots come from `docs/training-kit/screenshots/*.webp` (a local demo build). The mobile captures aren't used because the sidebar crowds the content at 390 px, so vertical formats use zoomed desktop crops instead.
