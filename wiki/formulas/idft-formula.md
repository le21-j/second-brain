---
title: IDFT (Formula)
type: formula
course:
  - "[[eee-404]]"
tags: [idft, fft]
sources:
  - "[[slides-fft-idft]]"
created: 2026-04-21
updated: 2026-05-06
---

# IDFT — Formula

## Definition

$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k]\, W_N^{-kn}, \qquad n = 0, 1, \ldots, N-1$$

where $W_N^{-1} = e^{+j2\pi/N}$.

## Via forward FFT (implementation recipe)

$$x[n] = \frac{1}{N}\left(\text{FFT}(X^*[k])\right)^*$$

Four steps in code:
1. $X^*[k]$ — conjugate.
2. $Y[k] = \text{FFT}\{X^*[k]\}$ — forward FFT (use bit-reversal convention your FFT expects).
3. Divide by $N$.
4. $x[n] = Y^*[n]$ — conjugate.

## Related
- [[idft]]
- [[dft]]
- [[twiddle-factor]]
