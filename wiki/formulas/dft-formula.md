---
title: DFT (Formula)
type: formula
course: [[eee-404]]
tags: [dft, fft]
sources: [[slides-fft-core-equations]]
created: 2026-04-21
updated: 2026-04-26
---

# DFT — Formula

## Forward

$$X[k] = \sum_{n=0}^{N-1} x[n]\, W_N^{kn}, \qquad k = 0, 1, \ldots, N-1$$

with [[twiddle-factor]] $W_N = e^{-j2\pi/N}$.

## Expanded

$$X[k] = \sum_{n=0}^{N-1} x[n] \left[\cos\!\tfrac{2\pi kn}{N} - j\sin\!\tfrac{2\pi kn}{N}\right]$$

For real $x[n]$, real and imaginary parts of $X[k]$ are:
- $\mathrm{Re}\{X[k]\} = \sum x[n]\cdot\cos(2\pi kn/N)$
- $\mathrm{Im}\{X[k]\} = -\sum x[n]\cdot\sin(2\pi kn/N)$

## Inverse (see [[idft]])

$$x[n] = \tfrac{1}{N}\sum_{k=0}^{N-1} X[k]\, W_N^{-kn}$$

## Complexity
- Direct: **$N^2$ complex MULTs**, $N(N-1)$ complex ADDs.
- FFT (radix-2): **$(N/2)\cdot\log_2 N$** complex MULTs.
- One complex MULT $= 4$ real MULTs $+ 2$ real ADDs.

## Related
- [[dft]] — conceptual page
- [[fft]]
- [[twiddle-factor]]
