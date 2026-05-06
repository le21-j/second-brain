---
title: Example — 256 Hz Sinusoid, fs=8192, N=64
type: example
course:
  - "[[eee-404]]"
tags: [fft, interpretation, frequency]
sources:
  - "[[slides-fft-interpretation]]"
created: 2026-04-21
updated: 2026-05-06
---

# Example — Which Bins Contain a 256 Hz Tone?

## Setup
$x(t) = \sin(2\pi \cdot 256 \cdot t)$, sampled at $f_s = 8192$ Hz, $N = 64$.

## Step 1 — Frequency resolution
$\Delta f = f_s / N = 8192 / 64 = $ **$128$ Hz per bin**.

## Step 2 — Which positive bin?
$k = f / \Delta f = 256 / 128 = $ **$2$**. So $X[2]$ has non-zero value.

## Step 3 — Conjugate symmetry
Since $x$ is real, $X[N - k] = X^*[k]$. So $X[N - 2] = X[62]$ is the conjugate of $X[2]$ — **also non-zero** (with the same magnitude).

## Why is it exactly two bins with no leakage?
Because $f = 256$ Hz divides the window exactly: $64$ samples at $8192$ Hz $= 7.8125$ ms $= 2$ full cycles of a $256$ Hz sine. The FFT assumes periodicity; here the assumption is **correct**, so no edge discontinuity $\to$ no [[spectral-leakage]].

If $f$ were $200$ Hz instead (not a bin-aligned frequency), energy would spread into nearby bins.

## Related practice
- $f_s = 8192$, $N = 128$: if $X[4]$ and $X[124]$ are non-zero, what is $f$? $\to \Delta f = 64$, $f = 4\cdot 64 = $ **$256$ Hz**.

## Related
- [[dft-bin-interpretation]]
- [[frequency-resolution]]
- [[conjugate-symmetry]]
- [[spectral-leakage]]
