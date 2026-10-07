# LakshyaPrep — Launch campaign: "Lock the goal. Own the score."

**Product:** goal-based SAT / ACT / MCAT prep (live 1:1 coaching + GoalGap diagnostics) · **A BigMo company**
**Brand source:** `academy-kpm-spark/brand/01-brand-guidelines.md` (Broadsheet newsprint system, Source Serif 4, misregistration on display type only, cyan = CTA, magenta = reward).
**Audiences:** Instagram → students 15–22 (Gen Z, voice: hype coach with receipts). LinkedIn → parents, school counselors, educators (Exam Hall tone: calm, specific).
**Primary CTA:** Lock my goal · **Secondary:** Take the free scan · **Link:** lakshyaprep.com

> Guardrails (from the brand kit): no score or admission guarantees, no invented stats or testimonials. Any example score (1180 → 1450) is labelled "Example numbers for illustration only." Emoji only 🎯 🔥 ✅. At most one slang phrase per piece.

## Asset index (`output/`)

| Platform | File | Format | Use |
|---|---|---|---|
| Instagram | `instagram/carousel-method/slide-01…07.png` | 1080×1350 carousel | Launch post — The Lakshya Method |
| Instagram | `instagram/posts/post-01-main-character-score.png` | 1080×1350 | Goal meter hero |
| Instagram | `instagram/posts/post-02-sat.png` / `03-act` / `04-mcat` | 1080×1350 | Exam series |
| Instagram | `instagram/posts/post-05-parents.png` | 1080×1350 | Parent dashboard |
| Instagram | `instagram/stories/story-01…03.png` | 1080×1920 | Stories (add link sticker in the empty lower third) |
| Instagram | `instagram/reel-lock-the-goal-9x16.mp4` (+ `reel-cover.png`) | 1080×1920, 13.5 s | Reel — brand-kit §9 script |
| LinkedIn | `linkedin/video-product-film-16x9.mp4` (+ `video-cover.png`) | 1920×1080, 27 s | Native video post |
| LinkedIn | `linkedin/document-carousel-families.pdf` | 8 pages, 1:1 | Document post ("A guide for families") |
| LinkedIn | `linkedin/images/link-01…03.png` | 1200×627 | Single-image / link posts |

Videos are silent by design (captions are on-screen). Add a licensed track in-app: Instagram's audio library for the reel; LinkedIn plays muted by default.

---

## Instagram copy

### 1 · Carousel — The Lakshya Method (launch)
**Caption**
> One goal. Zero noise. 🎯
>
> Stop studying everything. Study what moves your score.
> 01 Scan — 20 questions find where your points leak.
> 02 Lock — goal score + test date in. Week-by-week route out.
> 03 Grind — 1:1 sessions, drills, timed mocks. Re-planned weekly.
> 04 Land — test day with a rehearsed pacing plan.
>
> Take the free scan. Link in bio.

**Hashtags:** #SAT #DigitalSAT #ACT #MCAT #SATprep #StudyTok #StudyWithMe #CollegeAdmissions #PreMed #LakshyaPrep
**Alt text:** Seven slides in newspaper style explaining the four-step Lakshya Method (Scan, Lock, Grind, Land), each with a phone screenshot of the LakshyaPrep app.

### 2 · Post — Main character score
> Pick one number. Watch the gap close. 🔥
> Points-to-goal, weekly route, streaks earned on-plan. Example numbers shown — yours start with the free scan.

### 3–5 · Exam series (post one per week)
- **SAT:** "1600 is a target, not a vibe. Full-length Digital SAT mocks with section ranges and a review of every miss. 🎯"
- **ACT:** "36, locked in. English, Math, Reading, Science — timed like the real thing."
- **MCAT:** "Aim for the white coat. Full-length MCAT mocks with section-level estimates and a miss-by-miss review."

### 6 · Post — Parents
> See the plan. Not just the bill. Goals, sessions, progress reports and invoices for every child in one place. Sibling discounts apply automatically.

### Stories
1. **POV** → link sticker "Free scan". 2. **20 questions** → poll sticker "Which test? SAT / ACT". 3. **Test eve** → post the night before major test dates (no link; pure brand).

### Reel — "POV: you stopped studying everything."
> POV: you stopped studying everything. 🎯 Scan. Lock. Grind. Land. Take the free scan — link in bio.
Pin a comment: "Which test are you locking — SAT, ACT or MCAT?"

---

## LinkedIn copy

### 1 · Native video (launch)
> Most test-prep advice says: do more. More books, more tabs, more practice sets.
>
> We built LakshyaPrep to do the opposite. A student picks one goal score. An adaptive scan shows where points are being lost. GoalGap ranks skills by the points they can still give — not by percentage wrong — and a live 1:1 coach turns that into a week-by-week route that is re-planned from real results.
>
> SAT · ACT · MCAT. Start with the free scan: lakshyaprep.com
>
> #EdTech #SAT #ACT #MCAT #CollegeAdmissions #Parenting #Education

### 2 · Document post — "SAT, ACT, MCAT: prep that starts with one number"
> A 7-page guide for families and counselors on how goal-based preparation works — Scan, Lock, Grind, Land — and what parents can see along the way. Free to share with your school community.

### 3 · Image posts (rotate)
- **link-01-launch:** "Goal-based SAT, ACT and MCAT prep: live 1:1 coaching + GoalGap diagnostics. Lock the goal. Own the score."
- **link-02-goalgap:** "Where should the next study hour go? GoalGap ranks skills by points available, not percentage wrong. Here's why that matters…" (write 3 short paragraphs from the founder's voice)
- **link-03-mocks:** "Full-length mocks with real timing and honest score ranges. Every miss flows into a review log and spaced repetition."

---

## 3-week posting plan

| Week | Instagram | LinkedIn |
|---|---|---|
| 1 | Mon carousel · Wed reel · Fri post-01 · stories daily | Tue video · Thu link-01 |
| 2 | Mon SAT · Wed parents · Fri ACT · stories ×3 | Tue document PDF · Thu link-02 |
| 3 | Mon MCAT · Wed reel (re-share) · Fri carousel re-cut | Tue link-03 · Thu founder text post + video cover |

**Measure:** free-scan starts (UTM `utm_source=instagram|linkedin&utm_campaign=lp_launch&utm_content=<file name>`), saves/shares on the carousel, video completion rate.

## Regenerate
```bash
python3 campaigns/lakshyaprep/build.py --src ../academy-kpm-spark
```
Screenshots are read from `academy-kpm-spark/docs/master/assets/mobile` and `docs/evidence/full-tests`; the "payments in test mode" banner is cropped out automatically.
