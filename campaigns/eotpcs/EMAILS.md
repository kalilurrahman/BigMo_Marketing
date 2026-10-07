# EOT-PCS: walkthrough / pilot nurture (B2B)

**Trigger:** a walkthrough request or pilot enquiry (website form, LinkedIn comment "walkthrough", or an event lead).
**Goal:** book a walkthrough on the prospect's own document rules → start a pilot.
**Exit:** as soon as a walkthrough is booked, stop and hand over to sales. If someone replies, a human takes over.
**Style:** plain text, from a named person (`{{sender_name}}, BigMo`). Send Tuesday to Thursday, 9–11 a.m. in the recipient's time zone.
**Rules:** call it a **pilot**. No customer names, ROI or time-saved figures.

| # | Day | Purpose |
|---|---|---|
| 1 | 0 | Thanks + book a slot |
| 2 | 3 | The seven controls (playbook PDF) |
| 3 | 7 | Maker ≠ checker, and why it matters |
| 4 | 12 | Oracle stays the source of truth |
| 5 | 18 | Close the loop |

---

### 1 · Day 0: Book the walkthrough
**Subject:** Your EOT-PCS walkthrough · *A/B:* From PI to paid, on your own rules
**Preview:** 30 minutes, using your document requirements.
```
Hi {{first_name}},

Thanks for your interest in EOT-PCS.

The most useful walkthrough uses your own rules: which documents your customers, countries and Incoterms require, and who approves what. If you can share one recent shipment's document list (anonymised is fine), we'll set it up in the pilot before we meet.

[Pick a 30-minute slot →]

{{sender_name}}
EOT-PCS · BigMo
```

### 2 · Day 3: The seven controls
**Subject:** 7 controls between a PI and a payment · *A/B:* Where export delays actually come from
**Preview:** One page each.
```
Hi {{first_name}},

Most export delays and payment leaks come from the same gaps: re-keyed numbers, a missing certificate, a package approved by the person who made it, a balance nobody chased.

I've attached a short playbook: the seven controls we built into EOT-PCS to close them, one page each.

[Read the playbook (PDF) →]

Worth 30 minutes to see them on your shipments? [Book a slot →]

{{sender_name}}
```

### 3 · Day 7: Maker ≠ checker
**Subject:** Who approved this package? · *A/B:* Maker ≠ checker, enforced
**Preview:** Segregation of duties by the system, not a policy PDF.
```
Hi {{first_name}},

In most export teams, "approved" means someone replied "ok" to an email.

In EOT-PCS, the person who prepared a document package can never approve it. AI advisory findings compare the documents first, then a different person approves, rejects or waives, with the reason recorded in an append-only audit log.

Happy to show it on one of your shipments. [Book a slot →]

{{sender_name}}
```

### 4 · Day 12: Oracle stays the source of truth
**Subject:** Nothing re-keyed · *A/B:* Keep Oracle. Lose the spreadsheet.
**Preview:** The ERP owns the numbers. EOT-PCS owns the process.
```
Hi {{first_name}},

One design decision you should know about: EOT-PCS doesn't replace your ERP.

Customer, order-line and invoice values are pulled from Oracle read-only, so the number on the document is the number in the ERP. EOT-PCS runs the process around it: checklists, approvals, release, payment follow-up and the audit trail.

[Book a walkthrough →]

{{sender_name}}
```

### 5 · Day 18: Close the loop
**Subject:** Should I close your request? · *A/B:* Last note from me
**Preview:** No problem if the timing isn't right.
```
Hi {{first_name}},

I haven't heard back, so I'll assume the timing isn't right and close your request for now.

If export documentation or payment follow-up becomes a priority, reply to this email and we'll set up a walkthrough on your own rules. EOT-PCS is in pilot, so it's a good time to shape it.

{{sender_name}}
```
