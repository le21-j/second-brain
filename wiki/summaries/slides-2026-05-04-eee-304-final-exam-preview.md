---
title: EEE 304 Final Exam Preview Slides (8 pp, 4/23/2026)
type: summary
source_type: slides
source_path: raw/slides/eee-304/Final_slides.pdf
source_date: 2026-04-23
course: [[eee-304]]
tags: [eee-304, final, exam, preview, slides, transfer-function, butterworth, roc, euler, tustin, pam, tdm, fdm, feedback, sampled-data]
created: 2026-05-04
---

# EEE 304 Final Exam Preview — Source Summary

## TL;DR

8-page deck previewing the **EEE 304 Final Exam** (online, **May 4 10 AM → May 6 11:59 PM**, **150 min**, open-book, **350 pts**, **8 problems**). One slide per exam problem, each pointing back to the originating module + homework + lab. The slides give a worked **example** of each problem type (not the actual exam problem) — these examples are the same ones from Module 1/2/4 lectures and HW1/HW4/HW7.

## Key takeaways

- **The exam mirrors the 8 modules of the course** — there's no surprise topic. If you've done HW1, HW4, HW7, Module 2 filter design, Lab 3 control design, you've seen everything.
- **Open-book ≠ unlimited time.** $\sim 18$ min/problem. Don't lose time looking up basics — keep a one-page formula sheet in front of you.
- **Modules + sources to revisit:** Module 1 (steady-state, ROC), Module 2 (filtering), Module 4 (Euler/Tustin), HW1 (steady-state), HW4 (sampling), HW7 (PAM/TDM), Lab 3 (feedback control).

## Concepts introduced or reinforced

- [[steady-state-response]] (NEW) — Problem 1's topic. Sinusoidal steady-state via $H(j\omega)$.
- [[butterworth-filter]] — Problem 2/3's prototype. First-order $H(s) = 1/(\tau s + 1)$, $\tau = 1/\omega_c$.
- [[region-of-convergence]] — Problem 4. Causal/anticausal/two-sided ROC + stability test.
- [[forward-euler-discretization]] (NEW) — Problem 5. $z = 1 + sT$; can destabilize.
- [[tustin-bilinear]] (NEW) — Problem 5/8. $z = (1+sT/2)/(1-sT/2)$; stability-preserving.
- [[pulse-amplitude-modulation]], [[time-division-multiplexing]] — Problem 6 (slide example: 4 voice signals, 4 kHz BW each → TDM = 40 kHz, FDM = 16 kHz).
- [[feedback-control-loop]] (NEW) — Problem 7. Closed-loop TFs: $T_{ry} = CP/(1+CP)$, $T_{dy} = P/(1+CP)$.
- [[sampled-data-system]] (NEW) — Problem 8. AAF → sample → DT filter → reconstruct; reverse-engineer CT equivalent via FE or Tustin.

## Worked examples worth remembering

- **Slide 3 (Problem 1):** $h(t) = e^{-t}u(t-1) - e^{-2t}u(t)$ → $H(s) = (1/e)\,e^{-s}/(s+1) - 1/(s+2)$. Walks the time-shift Laplace property.
- **Slide 4 (Problem 2/3):** Separate $1$ Hz signal from $100$ Hz noise with DT filter at $f_s = 2$ kHz. CT corner $\omega_c = 62.8$ rad/s; FE-equivalent DT pole $z = 0.969$; $H(z) = (0.01547\,z + 0.01547)/(z - 0.9691)$.
- **Slide 6 (Problem 6):** 4 voice signals @ $4$ kHz BW each. TDM with $5$ slots (4+sync) at $8$ kHz frame rate → $T_{\text{slot}} = 25\,\mu\text{s}$, $B_{TDM} = 40$ kHz. FDM → $B_{FDM} = 16$ kHz.
- **Slide 8 (Problem 8):** $H_{DT}(z) = 0.1/(z-0.95)$ at $1$ kHz. FE → $H(s) = 100/(s+50)$. Tustin → $H(s) = (-0.05128 s + 102.6)/(s + 51.28)$.

## Questions this source raised

- **None about content.** The slides are a roadmap, not a test bank — every actual exam problem will use *different* numbers from the worked examples, but the technique is the same.
- **Strategy question:** open-book means you can bring formula references — make sure the [[eee-304-final-walkthrough]] cheat-sheet table is handy during the exam.

## Filed alongside

- [[eee-304-final-walkthrough]] — the full per-problem walkthrough built from this deck.
