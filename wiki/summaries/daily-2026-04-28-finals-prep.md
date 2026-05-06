---
title: 2026-04-28 — Finals Prep Across All 5 Active Courses
type: summary
source_type: daily
source_path: canvas API + wiki audit
source_date: 2026-04-28
course:
  - "[[eee-404]]"
  - "[[eee-304]]"
  - "[[eee-350]]"
  - "[[eee-341]]"
  - "[[eee-335]]"
tags: [finals, planning, study-guide, prep]
created: 2026-04-28
updated: 2026-05-06
---

# Finals Prep — All 5 Active Courses (2026 Spring C)

> [!warning] **Two confirmed finals in the next 14 days, three more TBD.** EEE 404 Exam 2 (Thu 4/30) is technically a midterm-2 not the final, but it carries 150 pts — treat as one. EEE 304 Final Exam (Wed 5/6) is the headline event at 350 pts. Finals for EEE 341, EEE 350, EEE 335 are likely scheduled the week of 5/4–5/8 but haven't appeared in the upcoming-assignments feed yet.

This page is the master study plan: per-course coverage status, what to study, and which wiki pages to read. Pair with [[daily-2026-04-28-workload]] for the day-by-day calendar.

## Course-by-course status

| Course | Final | Pts | Wiki coverage | Walkthroughs | Confidence |
|:---|:---:|:---:|:---:|:---:|:---:|
| [[eee-404]] | Exam 2 Thu 4/30 (mid-final) | 150 | ✅ strong (FFT module fully covered) | ✅ HW5, Lab 7 | 🟢 high |
| [[eee-304]] | Wed 5/6 | 350 | ✅ AM/PAM/TDM covered | ✅ Lab 4, HW7 | 🟡 medium |
| [[eee-350]] | TBD (Module 8) | ? | ✅ very strong (60+ concept pages) | ✅ HW7 | 🟢 high |
| [[eee-341]] | TBD | ? | ⚠️ stub course page only | ❌ none | 🔴 low |
| [[eee-335]] | TBD | ? | ⚠️ stub course page only | ❌ none | 🔴 low |

==**Bottom line: 3 of 5 courses are well-supported by the wiki; 2 (EEE 341, EEE 335) need raw-source ingest before walkthroughs are useful.**==

---

## EEE 404 Exam 2 — Thu 4/30 11:45 AM (150 pts)

**Likely coverage** (from Canvas modules 1–10): ARM ISA, board peripherals, fixed-point Q15 arithmetic, image processing, ML/MLP, frequency-domain (DTFT/DFT/Z-transform), audio filtering, music synthesis, FFT.

> [!example] **Study plan (2 days, ~6 hours)**
>
> **Wed evening (3 hrs):**
> - Re-read [[eee-404]] roadmap to map out which modules are covered.
> - Run through [[fft-fundamentals-set-01]] (11 problems, mixed difficulty).
> - Skim [[fft-gotchas]] for the canonical mistakes.
> - Re-read [[eee-404-hw5-walkthrough]] (DTFT, windowing, butterflies, real-time budget).
> - Re-read [[eee-404-lab-7-fill-in-walkthrough]] (FFT implementation in C on STM32).
>
> **Thu morning (1 hr):**
> - Quick pass through [[twiddle-factor]], [[butterfly]], [[bit-reversed-order]], [[fft-scaling]], [[real-valued-fft]], [[stft]], [[hamming-window]], [[rectangular-window]].
> - Fixed-point: [[fixed-point-arithmetic]] (Q15 conversion, overflow, scaling).

**Wiki gaps for this exam:** ARM ISA, board peripherals (GPIOs, polling vs. interrupt, timers), neural networks. These weren't in the original 2026-04-21 ingest because the lecture slides are video-only on Canvas. ==**For the exam, fall back on lecture videos** for these topics — wiki coverage is FFT-only.==

---

## EEE 304 Final Exam — Wed 5/6 11:59 PM (350 pts)

**Coverage** (from Canvas modules 1–7): signal/systems fundamentals, filtering, sampling + reconstruction, DT-CT filter equivalence, feedback systems (×2), communication systems / modulation.

> [!example] **Study plan (5 days, ~12 hours)**
>
> **Sat–Sun (3 hrs each):**
> - Read [[eee-304]] roadmap top to bottom.
> - Re-read [[eee-304-lab-4-walkthrough]] (AM modulation/demodulation in Simulink) — covers ~30% of likely exam content.
> - Re-read [[eee-304-hw7-walkthrough]] (cascaded AM, TDM-PAM, chopper amplifier) — covers another ~30%.
> - Per-concept refresh: [[amplitude-modulation]], [[modulation-index]], [[coherent-demodulation]], [[envelope-detection]], [[butterworth-filter]], [[pulse-amplitude-modulation]], [[time-division-multiplexing]], [[chopper-amplifier]].
>
> **Mon (3 hrs):**
> - Pull HW1–HW6 solutions from Canvas (`Module N: Homework` + `304_hwN_sol.pdf` files filed in each module). They're available for re-study.
> - Sample exams: Canvas → Module "Final Exam" → "Final Exam Info" page.
>
> **Tue (3 hrs):**
> - Cover gaps: filtering Bode plots, sampling theorem (Nyquist, aliasing, reconstruction), feedback (root locus, stability), DT-CT equivalence (impulse invariance, bilinear).
> - Generate practice problems on weak spots (ask me to make a practice set).
>
> **Wed morning:** light review only.

**Wiki gaps for this exam:** sampling theorem, Bode plots, root locus, feedback stability, DT↔CT mappings — these are Modules 1–6 of EEE 304 and aren't in the wiki yet. The wiki currently only covers the AM (Module 7) arc. ==**Strong recommendation:** ask me to ingest the Module 1–6 lecture materials before the weekend so the wiki carries you through all topics, not just AM.==

---

## EEE 350 Final — TBD (Module 8 has practice exam)

**Coverage** (Canvas Module 1–8): probability fundamentals, multivariate, conditional expectation, asymptotics (LLN/CLT), Bayesian inference, MAP/MMSE, MLE + CIs, hypothesis testing, regression, descriptive stats, intro stochastic processes.

**Wiki coverage is very strong** — see [[eee-350]] roadmap. 60+ concept pages span every topic.

> [!example] **Study plan (when final date is announced)**
>
> 1. [[eee-350]] roadmap — pick the 5–6 weakest arcs.
> 2. [[eee-350-hw7-walkthrough]] — covers significance testing + LMSE (the late-semester focus).
> 3. Practice sets: [[prob-fundamentals-set-01]], [[asymptotics-set-01]], [[inference-set-01]] — three full sets covering moments, asymptotics, inference.
> 4. Worked examples: 10 solo problems in `wiki/examples/` covering specific HW7 problems + canonical exercises.
> 5. [[prob-gotchas]] — running list of mistakes (CLT vs standardization, Var($cX$) = $c^2$Var($X$), Gaussian = Normal, etc.).
> 6. Read Module 8: Practice Final Exam (in Canvas LockDown Browser quiz).

> [!tip] EEE 350 is the **best-prepared** of the 5 courses thanks to the deep ingest done 2026-04-21. The wiki is the strongest study resource.

---

## EEE 341 Final — TBD

**Coverage** (Canvas modules 1–6): Maxwell's equations + free-charge dynamics → plane waves (lossy/lossless) → reflection/transmission at boundaries → transmission lines (Smith chart) → waveguides + cavity resonators → antennas.

**Wiki coverage:** stub course page at [[eee-341]] (created today, contains module roadmap). No concept pages, no walkthroughs.

> [!example] **Study plan**
>
> ==**Pre-requisite step:** ingest course material before walkthroughs are useful.== Drop these into `raw/`:
> - The textbook chapters (Ulaby/Ravaioli or whatever the syllabus specifies).
> - Sample exams (Canvas → "Sample Exams" page in Exam Information module).
> - Recent labs (Lab 5 PDF — also imminent for the 4/30 deadline).
>
> Once those are in `raw/`, ask me to ingest them and create concept pages for the major topics. Recommended priority order:
> 1. Plane waves (most likely heavy on the final): [[helmholtz-equation]], [[plane-wave-polarization]], [[poynting-vector]], [[wave-impedance]].
> 2. Reflection/transmission: [[fresnel-coefficients]], [[snells-law]], [[brewster-angle]], [[total-internal-reflection]].
> 3. Transmission lines: [[characteristic-impedance]], [[reflection-coefficient-line]], [[smith-chart]], [[stub-matching]].
> 4. Waveguides: [[guided-modes-tem-te-tm]], [[waveguide-cutoff]].
> 5. Antennas: [[hertzian-dipole]], [[antenna-gain-directivity]].
>
> Then build a single [[eee-341-final-walkthrough]] page covering sample-exam problems with collapsible derivations.

> [!warning] **The 5 ABET exams + Quiz 6 are due Friday — those are short and don't need finals-level prep.** Focus finals study on plane-waves + transmission lines (the two big topic areas of the course).

---

## EEE 335 Final — TBD

**Coverage** (Canvas Units 1–6): MOSFET physics → CMOS logic gates → memory → IC amplifiers → frequency response → multi-transistor + differential amps.

**Wiki coverage:** stub course page at [[eee-335]] (created today). No concept pages, no walkthroughs.

> [!example] **Study plan**
>
> ==**Pre-requisite step:** drop Sedra/Smith chapters or course-pack PDFs into `raw/textbook/` so I can ingest them.==
>
> 1. Frequency response (Unit 5 — most recent material, likely heavily tested): Miller's theorem, OCTC method, CS amplifier high-freq response.
> 2. Differential amplifiers (Unit 6 — the current unit): differential pair, CMRR, active loads.
> 3. IC amplifiers (Unit 4): small-signal model, basic configs, current mirrors.
> 4. Memory + CMOS (Units 2–3): SRAM cell, CMOS inverter VTC, transistor sizing.
> 5. MOSFET basics (Unit 1): $I$–$V$ in triode/saturation, biasing.
>
> Then build [[eee-335-final-walkthrough]] using Sedra/Smith chapter problems as anchors.

**This week's open items** are not finals-prep: Lab 5 (Wed) + HW8 (Thu) + course eval (Wed). After those clear, **Saturday 5/2 onwards is finals-prep window**.

---

## What I need from you to fill the EEE 341 / EEE 335 gaps

Drop any of these into `raw/`:
- **Lecture slides** (PDF or pptx) → `raw/slides/eee-341/` or `raw/slides/eee-335/`
- **Textbook chapters** → `raw/textbook/`
- **Past exams / sample exams** → `raw/other/eee-341-sample-exams/` etc.
- **Lab PDFs** that are due before finals → `raw/labs/`
- **Past homework problems with solutions** → `raw/homework/`

Once I see them, I'll do the same ingest pattern as EEE 304/350/404 (concept pages + walkthroughs + course-page roadmap update).

## Friday 5/1 ABET cliff (separate from finals)

5 ABET exams + Quiz 6 due Friday. Coverage from EEE 341 module letters:
- **A1, A2, A3** — Knowledge / Application / Analysis ABET dimensions (likely conceptual quiz questions).
- **B2** — Communication-style assessment.
- **K** — Specific subject-knowledge area.

These are short conceptual quizzes — block 90 minutes Friday afternoon, knock all 5 out back-to-back.

## Cross-references
- [[daily-2026-04-28-workload]] — day-by-day calendar for the same window
- [[eee-304]], [[eee-350]], [[eee-404]], [[eee-341]], [[eee-335]] — course pages
- All existing walkthroughs: [[eee-304-lab-4-walkthrough]], [[eee-304-hw7-walkthrough]], [[eee-350-hw7-walkthrough]], [[eee-404-hw5-walkthrough]], [[eee-404-lab-7-fill-in-walkthrough]]

## Source data
Canvas modules + syllabus pulled 2026-04-28 via API. Cached at `/tmp/canvas_*.json` for re-reads in the session.
