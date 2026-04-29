---
title: Slides — Window Functions
type: summary
source_type: slides
source_path: raw/slides/eee-404/window_functions.pdf
course: [[eee-404]]
tags: [dsp, stft, window, leakage]
created: 2026-04-21
updated: 2026-04-26
---

# Slides — Window Functions

## TL;DR
To analyze signals over time (Short Time Fourier Transform), you grab a segment $s[n] = x[n]\cdot w[n]$ where $w[n]$ is a **window**. Different windows trade off **main-lobe width** (frequency resolution) against **side-lobe height** (spectral leakage). Rectangular has the narrowest main lobe but tallest side lobes; Hamming/Hann double the main lobe but kill the side lobes.

## Key takeaways

| Window | $w[n]$ formula ($0 \leq n \leq L-1$) | Main lobe width (radians) | Side lobes |
|---|---|---|---|
| Rectangular | $1$ | **$4\pi/L$** (narrowest) | Highest |
| Hamming | $0.54 - 0.46\cdot\cos(2\pi n/(L-1))$ | $8\pi/L$ | Small, slow decay |
| Hann / Hanning | $0.5 - 0.5\cdot\cos(2\pi n/(L-1))$ | $8\pi/L$ | Small, **fast decay** |
| Bartlett / Triangular | Triangle (ramp up + down) | $\approx 8\pi/(L+1)$ | Small, fast decay |

- Rectangular window spectrum: **aliased sinc**: $W(\Omega) = \sin(\Omega L/2) / \sin(\Omega/2)$. First zero at $\Omega = 2\pi/L$; zero crossings spaced $2\pi/L$.
- Bartlett = convolution of two half-rectangular windows $\to |W_R|^2$ shape.
- **Trade-off:** narrower main lobe = better frequency resolution; smaller side lobes = less leakage from strong tones contaminating weaker ones nearby.

## Concepts introduced or reinforced
- [[stft]] — Short Time Fourier Transform
- [[window-function]] — the general concept
- [[rectangular-window]], [[hamming-window]], [[hann-window]], [[bartlett-window]]
- [[spectral-leakage]] — why windowing exists

## Worked examples worth remembering
- Question: smallest main lobe? Rectangular ($4\pi/L$). Everything else is $8\pi/L$.

## Questions this source raised
- Which window to use *when*? Rule of thumb: Hann for general-purpose spectral analysis (good side-lobe decay), rectangular only when you need the tightest frequency resolution and don't care about leakage.
