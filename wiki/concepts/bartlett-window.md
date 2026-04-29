---
title: Bartlett (Triangular) Window
type: concept
course: [[eee-404]]
tags: [window, fft]
sources: [[slides-window-functions]]
created: 2026-04-21
updated: 2026-04-26
---

# Bartlett (Triangular) Window

## In one line
A triangular ramp — zero at the endpoints, peaks in the middle. Mathematically, the convolution of two half-rectangular windows.

## Example first
For $L = 63$ (odd length typical for triangular):
- $w[0] = 0$
- $w[31] = 1$ (peak)
- $w[62] = 0$

The window rises linearly from $0$ to $1$, then falls linearly back to $0$.

## Why it matters
Because Bartlett is the convolution of two rectangular windows of length $(L+1)/2$:
- Its frequency response is the **square** of the rectangular window's: $|W_R(\Omega)|^2$.
- Squaring a sinc makes it **always non-negative** and **decays faster** than a plain sinc.

## Key properties
- Main lobe width: $\approx $ **$8\pi/(L+1)$** (essentially twice the rectangular's $4\pi/L$)
- Side lobes: fast decay, all non-negative
- First side lobe: $\approx 26$ dB below main

## When to use it
Less common than Hann/Hamming in practice. Used when you want:
- Non-negative spectral window (useful in power spectral density estimation).
- A window cheap to compute (just a ramp — no trig).

## Formula
$$w[n] = w_R[n] * w_R[n]$$
where $w_R$ has length $(L+1)/2$. Equivalently ($L$ odd):

$$w[n] = 1 - \left|\frac{n - (L-1)/2}{(L-1)/2}\right|, \qquad 0 \le n \le L-1$$

## Related
- [[window-function]]
- [[rectangular-window]] — Bartlett = rect convolved with rect
