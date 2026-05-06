---
title: Slides — FFT IDFT
type: summary
source_type: slides
source_path: raw/slides/eee-404/fft_idft.pdf
course:
  - "[[eee-404]]"
tags: [fft, idft, inverse]
created: 2026-04-21
updated: 2026-05-06
---

# Slides — FFT IDFT

## TL;DR
Shows how to compute the **Inverse DFT** using the *forward* FFT you already have. Trick: take complex conjugate of $X[k]$, run FFT, divide by $N$, conjugate again. Gives $x[n]$. This saves you from writing a separate IFFT routine.

## Key takeaways
- IDFT: $x[n] = (1/N) \sum X[k]\cdot e^{+j2\pi kn/N}$. Note the **$+$** in the exponent — that's what makes it "inverse".
- Algorithm to IDFT via forward FFT:
  1. Take complex conjugate $\to X^*[k]$
  2. Run $N$-point forward FFT on $X^*[k]$
  3. Divide the result by $N$
  4. Take complex conjugate of the result $\to x[n]$

## Concepts introduced or reinforced
- [[idft]] — inverse DFT via the conjugate trick
- [[fft]], [[butterfly]], [[bit-reversed-order]]

## Worked examples worth remembering
- $X[k] = [3, 1-2j, -1, 1+2j] \to x[n] = [1, 2, 0, 0]$. See [[idft-4pt-via-fft]].
- Exercise: $X[k] = [5, 3+2j, -3, 3-2j] \to x[n] = [2, 1, -1, 3]$. Included in same example page.

## Questions this source raised
- The question slide asks about bit-reversing the conjugate — make sure bit-reversal conventions for $N=4$ are solid. See [[bit-reversed-order]].
