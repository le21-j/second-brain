---
title: Hamming Window
type: concept
course:
  - "[[eee-404]]"
tags: [window, fft]
sources:
  - "[[slides-window-functions]]"
created: 2026-04-21
updated: 2026-05-06
---

# Hamming Window

## In one line
A raised-cosine window with coefficients $0.54 / 0.46$, tuned to push down the first side lobe as much as possible.

## Example first
For $L = 64$:
- $w[0] = 0.54 - 0.46\cdot\cos(0) = 0.08$ (not exactly zero at endpoints — a Hamming "fingerprint")
- $w[32] \approx 0.54 - 0.46\cdot\cos(\pi) = 1.0$ (peak in the middle)
- $w[63] \approx 0.08$ (near-zero at end)

Compared to [[rectangular-window]]: first side lobe now $\approx 43$ dB down (vs. $\approx 13$ dB), at the cost of twice as wide a main lobe.

## Formula
$$w[n] = 0.54 - 0.46 \cos\!\left(\frac{2\pi n}{L-1}\right), \qquad 0 \le n \le L-1$$

## Key properties
- Main lobe width: **$8\pi/L$** (twice rectangular)
- Side-lobe decay: **slow** ($\approx 6$ dB/octave) — first side lobe is suppressed but later ones decrease slowly
- Endpoint values $\approx 0.08$ (not zero, unlike [[hann-window]])

## When to use it
Use Hamming when you specifically want to **maximize attenuation of the first side lobe** — e.g. a strong tone adjacent in frequency to a weak one. For general broadband clean-up, [[hann-window]] has faster side-lobe decay.

## Related
- [[window-function]]
- [[hann-window]] — similar shape, different coefficients
