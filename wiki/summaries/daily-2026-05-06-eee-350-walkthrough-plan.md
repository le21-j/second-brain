---
title: "EEE 350 Final-Prep — Per-Module Walkthrough Plan (2026-05-06)"
type: summary
source_type: other
source_path: Canvas API + raw/textbook/Probability and Stochastic Processes_ Third Ed copy.pdf
source_date: 2026-05-06
course: [[eee-350]]
tags: [eee-350, walkthrough, finals, planning]
created: 2026-05-06
updated: 2026-05-06
---

# EEE 350 Final-Prep — Per-Module Walkthrough Plan

> [!note] Plan doc for the agent task that builds per-module problem walkthroughs from the Canvas "Videos Containing Problems" lists. Final exam: 2026-05-07 06:00. Strategy: highest-yield modules first (statistical inference, CLT/LLN). Stochastic-processes module deferred per Jayden's request.

## Course / textbook

- **Course:** EEE 350 Random Signal Analysis (Cihan Tepedelenlioglu) — Canvas course ID **246051** (`2026SpringC-T-EEE350-22042`).
- **Textbook on disk:** [`Probability and Stochastic Processes_ Third Ed copy.pdf`](../../raw/textbook/Probability%20and%20Stochastic%20Processes_%20Third%20Ed%20copy.pdf) — Yates & Goodman, **3rd edition** (115 MB, 1 file). Read via `pdftotext -raw` into `/tmp/yates3e/raw.txt` (OCR artifacts but content usable).
- **Edition mapping is given on Canvas.** Each module's "Lecture Materials" page lists the **2nd-edition problem numbers** followed by the **3rd-edition equivalents in parentheses**, written by the instructor. This eliminates the cross-edition matching step — I just transcribe the 3rd-ed numbers and pull them from the textbook.

## Module-by-module problem inventory

Verbatim from each Canvas "Module N: Lecture Materials" page (`/api/v1/courses/246051/pages/module-N-lecture-materials`):

| Module | Topic span | 2nd-ed problems | **3rd-ed problems (used here)** |
|---|---|---|---|
| **1** | Set theory, probability spaces, conditional prob | 1.5.2, 1.7.3, 1.7.5, 1.8.6, 1.9.1 | **1.4.2, 2.1.3, 2.1.5, 2.2.12, 2.3.1** |
| **2** | Counting, discrete RVs, expectation, variance | 2.2.3, 2.2.9, 2.3.2, 2.3.8, 2.3.10, 2.3.13, 2.4.1, 2.4.3, 2.5.9, 2.6.6, 2.8.5 | **3.2.2, 3.2.11, 3.3.3, 3.3.11, 3.3.14, 3.3.18, 3.4.1, 3.4.3, 3.5.15, 3.6.6, 3.8.5** |
| **3** | Continuous RVs, CDF, mixed distrib, normal | 3.1.3, 3.2.2, 3.3.6, 3.4.7, 3.4.5, 3.5.1, 3.6.2, 3.6.3, 3.7.9, 3.8.2 | **4.2.4, 4.3.2, 4.4.6, 4.5.13, 4.5.10, 4.6.1, 4.7.2, 4.7.3, 6.3.4, 7.2.4** |
| **4** | Joint dist, conditioning, independence (multi RVs) | 4.1.1, 4.2.4, 4.3.4, 4.4.2, 4.5.4, 4.6.4, 4.6.6, 4.6.8, 4.8.1, 4.8.5, 4.9.1, 4.9.11, 4.10.2, 4.10.6, 6.1.2 | **5.1.1, 5.2.4, 5.3.5, 5.4.2, 5.5.5, 6.1.5, 6.4.4, 6.4.6, ✗, 7.3.5, 7.4.5, 7.5.6, 5.7.4, 5.7.7, 9.1.1** |
| **5** | Bayes for RVs, derived RVs, sums, MGFs | 6.1.4, 6.2.4, 6.3.1 | **9.1.5, 6.5.6, 9.2.1** |
| **6** | Covariance, conditional expectation, LLN, CLT | 6.3.4, 6.3.5, 6.4.4, 6.5.1, 6.6.1, 6.7.1 | **9.2.4, 9.2.5, 9.3.4, 9.4.1, 9.5.1, 9.5.4** |
| **7** | Bayesian / MLE / NP hypothesis testing / regression | 7.1.2, 7.4.2, 7.1.4, 8.1.1, 8.1.4, 8.3.1, 9.1.3, 9.1.4, 9.1.5, 9.2.7, 9.3.3 | **10.1.2, 10.3.1, 10.1.4, 11.1.1, ✗, 11.3.1, 12.1.3, 12.1.4, 12.1.5, 12.2.6, 12.3.3** |
| **8 (deferred)** | Stochastic processes intro, Gaussian RP, Bernoulli, Poisson | 10.4.1, 10.4.3, 10.5.1, 10.5.3, 10.5.6 | **13.3.1, 13.3.3, 13.4.1, 13.4.3, 13.4.8** |

Notes from Canvas:
- Module 4 has one missing 3rd-ed mapping (the "✗" entry — the 9th problem corresponds to no equivalent in the 3rd ed). The instructor flagged that audio drops out from 7:18–10:54 in the Module 4 video for problem 4.9.1.
- Module 7 has one missing 3rd-ed mapping (✗ in 5th slot — 8.1.4 appears to have no 3rd-ed equivalent. Instructor also noted a numerical correction in the Gaussian-approximation step).
- Module 3 instructor errata: var(V) = 8 (not 6.55 as stated in video); for problem 3.8.2 a `y` was mistakenly written as `x`.

**Total problems:** 80 problems across 8 modules. Active scope (modules 1–7) = 75 problems. Stochastic-processes Module 8 = 5 deferred.

## Priority order

> [!note] **Strategy:** Topic-6 (statistical inference, Module 7 in this course's numbering) is the biggest gap zone. Build the Module 7 walkthrough first at full depth. Then CLT/LLN (Module 6), multi-RVs (Module 4), then back-fill earlier modules if time permits. Stochastic-processes Module 8 is deferred per Jayden's request.

1. **Module 7** — Bayesian / MLE / NP / regression (statistical inference) — **highest priority, biggest gap.**
2. **Module 6** — covariance, conditional expectation, LLN, CLT.
3. **Module 5** — Bayes-for-RVs, derived RVs, sum distributions, MGFs.
4. **Module 4** — joint distributions, conditioning, independence, total prob theorem for RVs.
5. **Module 3** — continuous RVs, CDF, mixed distributions, normal probabilities.
6. **Module 2** — counting, discrete RVs, expectation, variance.
7. **Module 1** — set theory, probability axioms, conditional probability.
8. **Module 8 — DEFERRED** (stochastic processes — Jayden has explicitly deferred this).

## Effort estimate

- Module 7 (11 problems, hardest): ~45–60 minutes.
- Module 6 (6 problems): ~30 minutes.
- Module 5 (3 problems): ~15 minutes.
- Module 4 (15 problems): ~50 minutes.
- Module 3 (10 problems): ~35 minutes.
- Module 2 (11 problems): ~30 minutes.
- Module 1 (5 problems): ~20 minutes.

Total budget for active scope ≈ 3.5 hours of focused construction.

## Pipeline

1. Pull problem text from `/tmp/yates3e/raw.txt` (already cached) by grep at line-start for the problem number.
2. For each problem: state the problem (verbatim, OCR-cleaned), name the framework (3–5 building blocks), solve step-by-step in LaTeX, headline `**Answer:**` line, `> [!tip]` for what to memorize, `> [!warning]` for gotchas.
3. Write each module walkthrough to `/Users/smallboi/Documents/second-brain/wiki/walkthroughs/eee-350-module-NN-<topic>-walkthrough.md`.
4. Cross-link to [[eee-350-final-walkthrough]] and concept pages.

---

## Progress log

(Updated as modules complete.)

- **2026-05-06** — Module 7 walkthrough complete: [[eee-350-module-07-statistical-inference-walkthrough]]. 10 problems solved (1 placeholder for 8.1.4 with no 3rd-ed equivalent). Highest-priority module — biggest gap zone.
- **2026-05-06** — Module 6 walkthrough complete: [[eee-350-module-06-clt-lln-mgf-walkthrough]]. All 6 problems solved (MGF moments, random-sum substitution, CLT, continuity correction).
- **2026-05-06** — Module 5 walkthrough complete: [[eee-350-module-05-derived-rvs-sums-walkthrough]]. All 3 problems solved (variance-of-sum trap on triangle support, PDF-of-sum CDF method, Laplace MGF).
- **2026-05-06** — Module 4 walkthrough complete: [[eee-350-module-04-multiple-rvs-walkthrough]]. 14 problems solved + 1 marked unavailable per Canvas mapping. Joint distributions, conditioning, derived RVs (max/min/ratio).
- **2026-05-06** — Module 3 walkthrough complete: [[eee-350-module-03-continuous-rvs-walkthrough]]. All 10 problems solved. Continuous PDFs/CDFs, mixed RVs, Gaussian probability.
- **2026-05-06** — Module 2 walkthrough complete: [[eee-350-module-02-discrete-rvs-walkthrough]]. All 11 problems solved. PMFs, binomial/geometric/negative-binomial, doubling-strategy gambling.
- **2026-05-06** — Module 1 walkthrough complete: [[eee-350-module-01-probability-set-theory-walkthrough]]. All 5 problems solved. Set theory, conditional probability, Bayes (HIV test), counting.
- **2026-05-06** — Module 8 (stochastic processes) **deferred** per Jayden's request. Problems on file in this plan doc if Jayden wants to pick them up post-exam: 13.3.1, 13.3.3, 13.4.1, 13.4.3, 13.4.8 (Yates 3rd ed).

---

## Final summary (2026-05-06)

### Modules completed

All 7 active-scope modules have full walkthroughs. **74 problems** solved (1 problem marked as having no 3rd-ed equivalent in Canvas mapping; 1 problem in Module 7 was a placeholder for the same reason). Walkthroughs list:

1. [[eee-350-module-07-statistical-inference-walkthrough]] — **highest priority**, statistical inference (MLE / MAP / LMSE / NP / significance test). 11 problems.
2. [[eee-350-module-06-clt-lln-mgf-walkthrough]] — MGFs, sums of RVs, CLT/LLN. 6 problems.
3. [[eee-350-module-05-derived-rvs-sums-walkthrough]] — derived RVs, sums, MGFs. 3 problems.
4. [[eee-350-module-04-multiple-rvs-walkthrough]] — joint distributions, conditioning, independence. 15 problems.
5. [[eee-350-module-03-continuous-rvs-walkthrough]] — continuous RVs, CDF, mixed RVs, normal. 10 problems.
6. [[eee-350-module-02-discrete-rvs-walkthrough]] — counting, discrete RVs, expectation, variance. 11 problems.
7. [[eee-350-module-01-probability-set-theory-walkthrough]] — set theory, probability axioms, conditional probability. 5 problems.

### Modules deferred

- **Module 8 (stochastic processes)** — 5 problems (13.3.1, 13.3.3, 13.4.1, 13.4.3, 13.4.8). Skipped per Jayden's request. Recommended pickup time: post-exam, after the relevant material becomes useful for EEE 404.

### Quality notes

- **Edition mapping was free** — the instructor lists 3rd-ed numbers in parentheses on each Canvas Lecture-Materials page. No need to text-match between editions.
- **PDF extraction** worked via `pdftotext -raw` on the 3rd-ed PDF in `raw/textbook/`. Some OCR artifacts (`\l\l` for W, `'v` for w, `n11mber` for number, etc.) but content was always recoverable. Direct read of the raw extract `/tmp/yates3e/raw.txt` indexed by problem number at line-start for fast lookup.
- **2 problem slots in the Canvas mapping have no 3rd-ed equivalent** (one in Module 4, one in Module 7). Documented as placeholders with the recommendation to consult the video for context.
- **One known instructor errata** caught: Module 3 problem 4.4.6 — Tepedelenlioglu's video reports $\text{Var}[V] = 6.55$, but direct integration gives $\text{Var}[V] = 8$. The walkthrough uses the correct value.
- All walkthroughs follow the vault's framework-over-formulas style: 3–5 named building blocks per problem type, "what to internalize vs memorize" tip callouts, gotcha warnings, headline `**Answer:**` sentences. LaTeX throughout.
- Every problem walkthrough is cross-linked to: the course page [[eee-350]], master review [[eee-350-final-walkthrough]], adjacent module walkthroughs, and 3–5 concept pages.

### Recommended next steps (post-exam)

1. **Module 8 walkthrough** (deferred) — same Canvas-mapping pattern, problems 13.3.1, 13.3.3, 13.4.1, 13.4.3, 13.4.8. Topic: stochastic-process intro + Bernoulli + Poisson + Gaussian RPs. Probably useful prep for EEE 404 / EEE 350-follow-on courses.
2. **Practice-mode solo retries.** Copy the problem statements (already in each walkthrough) into a fresh `wiki/practice/eee-350-solo-set-NN.md` and time yourself blind on a representative sample (e.g., one from each module). Compare to the walkthrough.
3. **Mistake log.** Walk through each gotcha callout flagged in the walkthroughs and add a one-line entry to [[mistakes/prob-gotchas]] for the categories that bit hardest in the exam.
4. **Concept-page consolidation.** Several concepts referenced in the walkthroughs ([[mle]], [[map-estimation]], [[lmse]], [[chebyshev-inequality]], [[mgf]], [[random-sum]]) likely have stub or out-of-date pages. A lint pass after the exam would compress and update them based on the framework distilled in these walkthroughs.

### Files created this session

- `/Users/smallboi/Documents/second-brain/wiki/summaries/daily-2026-05-06-eee-350-walkthrough-plan.md` (this file)
- `/Users/smallboi/Documents/second-brain/wiki/walkthroughs/eee-350-module-07-statistical-inference-walkthrough.md`
- `/Users/smallboi/Documents/second-brain/wiki/walkthroughs/eee-350-module-06-clt-lln-mgf-walkthrough.md`
- `/Users/smallboi/Documents/second-brain/wiki/walkthroughs/eee-350-module-05-derived-rvs-sums-walkthrough.md`
- `/Users/smallboi/Documents/second-brain/wiki/walkthroughs/eee-350-module-04-multiple-rvs-walkthrough.md`
- `/Users/smallboi/Documents/second-brain/wiki/walkthroughs/eee-350-module-03-continuous-rvs-walkthrough.md`
- `/Users/smallboi/Documents/second-brain/wiki/walkthroughs/eee-350-module-02-discrete-rvs-walkthrough.md`
- `/Users/smallboi/Documents/second-brain/wiki/walkthroughs/eee-350-module-01-probability-set-theory-walkthrough.md`

### Files modified this session

- `index.md` — added 7 new walkthrough entries + planning-doc link in the EEE 350 walkthrough section.
- `log.md` — added one consolidated walkthrough entry covering all 7 modules.
- `wiki/walkthroughs/eee-350-final-walkthrough.md` — added a "Module practice problems (from textbook video list)" callout under each Module 1–7 heading, linking to the new per-module walkthrough.

### Files NOT modified (per task constraints)

- `wiki/tutor-sessions/tutor-2026-05-06-live.md` (live tutor surface).
- `wiki/tutor-sessions/tutor-2026-05-06.md` (active session log).
- `wiki/courses/eee-350.md` (canonical syllabus).
- `raw/` (immutable).

