---
title: Hann (Hanning) Window
type: concept
course:
  - "[[eee-404]]"
tags: [window, fft]
sources:
  - "[[slides-window-functions]]"
created: 2026-04-21
updated: 2026-05-06
---

# Hann (Hanning) Window

## In one line
A raised-cosine window that tapers **to zero** at the endpoints — the usual default for spectral analysis.

## Example first
For $L = 64$:
- $w[0] = 0.5 - 0.5\cdot\cos(0) = $ **$0$**
- $w[32] = 0.5 - 0.5\cdot\cos(\pi) \approx 1.0$
- $w[63] \approx $ **$0$**

Unlike [[hamming-window]], the endpoints truly hit zero — so the windowed signal has no edge discontinuity whatsoever.

## Formula
$$w[n] = 0.5 - 0.5\cos\!\left(\frac{2\pi n}{L-1}\right), \qquad 0 \le n \le L-1$$

## Key properties
- Main lobe width: **$8\pi/L$** (same as Hamming)
- First side lobe: $\approx 31$ dB below main
- Side-lobe decay: **fast** ($\approx 18$ dB/octave) — later side lobes drop off quickly
- Endpoints exactly zero

## When to use it
The **default choice** for general spectral analysis. Fast side-lobe decay means less distant leakage; makes cleaner spectrograms.

## Naming gotcha
"Hann" (single n) = the window. "Hanning" (with -ing) is common but technically incorrect — the name comes from Julius von Hann. Both names are used interchangeably. Lab slides use "Hanning/Hann" to cover both.

## Related
- [[window-function]]
- [[hamming-window]] — similar form, different side-lobe shape
