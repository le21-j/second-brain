---
title: EEE 404 Module 7 — Frequency Domain Concepts (slide deck summary)
type: summary
source_type: slides
source_path: raw/slides/eee-404/m7-freq-1-dtft-and-dft.pdf
source_date: 2026-04-29
course:
  - "[[eee-404]]"
tags: [eee-404, dtft, dft, z-transform, block-diagram, frequency-domain]
created: 2026-04-29
---

# EEE 404 Module 7 — Frequency Domain Concepts

**Source:** 5 PDFs in `raw/slides/eee-404/m7-freq-*.pdf`:

| Slide deck | Path |
|---|---|
| Fourier Transforms: DTFT and DFT | `m7-freq-1-dtft-and-dft.pdf` |
| Fourier Transforms: DFT Examples | `m7-freq-2-dft-examples.pdf` |
| Fourier Transforms: DFT Properties | `m7-freq-3-dft-properties.pdf` |
| Z-Transform | `m7-freq-4-z-transform.pdf` |
| Block Diagram Representations | `m7-freq-5-block-diagram-representations.pdf` |

## TL;DR
Module 7 is the heaviest exam-2 module: it introduces (a) the DTFT and DFT and their relationship, (b) DFT properties (linearity, time/frequency shift, convolution, Parseval, conjugate symmetry), (c) the Z-transform with poles/zeros/ROC, and (d) the five block-diagram realisations of $H(z)$ (DF-I, DF-II, transposed DF-II, cascade, parallel).

## Key takeaways

### DTFT and DFT
- **DTFT analysis:** $X(e^{j\omega}) = \sum_n x[n] e^{-j\omega n}$ — continuous in $\omega$, $2\pi$-periodic.
- **DFT analysis:** $X[k] = \sum_{n=0}^{N-1} x[n] e^{-j 2\pi kn/N}$ — $N$ uniformly-spaced samples of the DTFT around the unit circle.
- **Sampling-in-frequency / aliasing-in-time relation:** $X[k]$ is the DTFT sampled at $\omega_k = 2\pi k/N$, equivalent to periodising $x[n]$ with period $N$ in time. To avoid time-aliasing, $N \geq L$ where $L$ is the support of $x[n]$.
- **Conjugate symmetry for real $x[n]$:** $X[N-k] = X^*[k]$ — only $X[0..N/2]$ are independent.

### DFT properties (full table at [[dft-properties]])
- Linearity, time shift (circular), frequency shift, conjugation, conjugate symmetry, circular convolution, multiplication, **Parseval** ($\sum |x|^2 = \tfrac{1}{N}\sum |X|^2$).

### Z-transform
- $X(z) = \sum_n x[n] z^{-n}$.
- **ROC** is part of the answer; rules at [[region-of-convergence]].
- **Time-shift** $z^{-n_0} \leftrightarrow x[n - n_0]$ — the workhorse for converting $H(z) \leftrightarrow$ difference equation.
- **DTFT exists** ⟺ ROC ⊃ unit circle.
- **Causal stable** ⟺ all poles inside unit circle.

### Block diagrams
- **Direct Form I:** $M + N$ delays; two delay lines. See [[direct-form-i]].
- **Direct Form II:** $\max(M, N)$ delays; shared delay line. See [[direct-form-ii]].
- **Transposed Direct Form II:** reverse all DF-II arrows; same delay count.
- **Cascade:** series of 2nd-order biquads; good for fixed-point.
- **Parallel:** sum of 2nd-order biquads (after partial fractions).

## Concepts introduced
- [[dtft]], [[dft]], [[idft]], [[dft-properties]], [[parseval-theorem]] — Fourier
- [[z-transform]], [[region-of-convergence]] — Z-domain
- [[direct-form-i]], [[direct-form-ii]] — block-diagram realisations
- [[difference-equation]], [[fir-vs-iir]] — time-domain twin of $H(z)$

## Exam tie-in
- **Exam 2 Practice Problem 2** (Z-transform → ROC, difference equation, FIR/IIR, DF-II) is built from this module.
- **Exam 2 Practice Problem 3** uses the rectangular-window DFT structure introduced here.

## Questions raised
- The "transposed DF-II" advantage over plain DF-II — when does it matter? (Answer: numerical conditioning under fixed-point; for floating-point STM32F4 they're equivalent.)
