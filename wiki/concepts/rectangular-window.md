---
title: Rectangular Window
type: concept
course: [[eee-404]]
tags: [window, fft]
sources: [[slides-window-functions]]
created: 2026-04-21
updated: 2026-04-26
---

# Rectangular Window

## In one line
$w[n] = 1$ for $n = 0, \ldots, L-1$, zero outside — the "do nothing" window you get by default.

## Example first
If you just grab $L = 64$ samples of a signal and FFT them, you've used a rectangular window. Its frequency response is an **aliased sinc**:

$$W(\Omega) = \frac{\sin(\Omega L / 2)}{\sin(\Omega / 2)}$$

- Main lobe width: **$4\pi/L$** (narrowest of all standard windows)
- First zero crossing: $\Omega = 2\pi/L$
- First side lobe: only $\approx 13$ dB below main lobe $\to$ **tall side lobes $= $ worst leakage**

## When to use it
- When you need peak [[frequency-resolution]] and there are no strong interfering tones nearby.
- When the signal is already "close to periodic" over the window and you don't expect edge discontinuities.
- Otherwise, reach for [[hann-window]] or [[hamming-window]] instead.

## Formula
Causal form (starts at n = 0):

$$w[n] = \begin{cases} 1, & 0 \le n \le L-1 \\ 0, & \text{otherwise}\end{cases}$$

## Related
- [[window-function]] — overview
- [[spectral-leakage]] — why this window is often bad
