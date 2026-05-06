---
title: EEE 404 Exam 2 Review (Practice Exam)
type: summary
source_type: other
source_path: raw/other/eee-404-exam-2-review.pdf
source_date: 2026-04-29
course:
  - "[[eee-404]]"
tags: [eee-404, exam, practice-exam, review-handout]
created: 2026-04-29
---

# EEE 404 Exam 2 Review

**Source:** [`raw/other/eee-404-exam-2-review.pdf`](../../raw/other/eee-404-exam-2-review.pdf) (7 pages, posted by Dr. Wang)

## TL;DR
Practice exam for EEE 404 Exam 2 (Thursday 2026-04-30): 4 problems covering MLP forward-pass, Z-transform → ROC + difference equation + DF-II, sampling/DTFT/DFT/FFT sizing + multiplication count, and 4-pt DFT direct + FFT butterfly + IFFT. Closed-book except one 8.5×11 sheet, calculator allowed, 150 pts. Topics: Modules 6, 7, 10, 11. HW3, HW4, HW5 also fair game.

## Key takeaways
- **Module coverage:** 6 (NN), 7 (DTFT/DFT/Z-transform/block diagrams), 10 (FFT), 11 (windows / time-frequency).
- **4 practice problems** map 1:1 to 4 conceptual buckets.
- **Answer key included** (pages 4–7) — ground truth for the walkthrough.
- **Hardest gotcha:** Problem 1 Y₂ is **0** because ReLU clips a $-0.049$ pre-activation. Problem 4(d) requires the IFFT-via-FFT trick with the conjugate-divide-conjugate ritual.

## Concepts introduced or reinforced
- [[mlp]], [[neuron]], [[relu]], [[forward-propagation]] — Module 6
- [[dtft]], [[dft]], [[idft]], [[dft-properties]], [[parseval-theorem]] — Module 7
- [[z-transform]], [[region-of-convergence]], [[difference-equation]], [[fir-vs-iir]], [[direct-form-i]], [[direct-form-ii]] — Modules 7 + 8
- [[fft]], [[butterfly]], [[bit-reversed-order]], [[twiddle-factor]] — Module 10
- [[window-resolution-criterion]], [[frequency-resolution]], [[spectral-leakage]] — Module 11

## Walkthrough produced
[[eee-404-exam-2-walkthrough]] (per-problem deep dive) and [[eee-404-exam-2-study-guide]] (formula-sheet skeleton).

## Questions this source raised
- Will the actual exam keep the same 4-bucket structure? (Best guess from past exam patterns: yes.)
- Will window functions other than rectangular be tested? (HW5 implies Hamming will appear.)
