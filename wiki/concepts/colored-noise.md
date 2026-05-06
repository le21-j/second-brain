---
title: Colored Noise
type: concept
course:
  - "[[eee-350]]"
tags: [noise, filter, spectrum]
sources:
  - "[[slides-47-stochastic-processes]]"
created: 2026-04-21
updated: 2026-05-06
---

# Colored Noise

## In one line
Any noise whose power spectrum is **not flat**. Typically constructed by filtering [[white-gaussian-process|white noise]] through a linear system.

## Example
Pass WGN through a moving-average filter $h[n] = 1/\sqrt{50}$ for $0 \leq n < 50$:
- Output = convolution of WGN with $h$.
- Samples are now **correlated** (smoothed) — each output averages 50 input samples.
- Still Gaussian (sum of Gaussians), but no longer white.
- Visually: WGN looks jagged; colored noise looks smoother/low-pass.

## Color terminology (borrowed from light)
| Name | Shape of PSD | Pattern |
|---|---|---|
| **White** | Flat | All frequencies equal |
| **Pink** | $1/f$ | 3 dB/octave rolloff; common in audio |
| **Red / Brown** | $1/f^2$ | 6 dB/octave rolloff; random walk's increments |
| **Blue** | $f$ | 3 dB/octave rise |

## Creating a colored noise from white

Given desired PSD $S_Y(\omega)$, find filter $H(\omega)$ with $|H(\omega)|^2 = S_Y(\omega) / S_W(\omega)$. Pass white noise $W[n]$ through $H \to$ output $Y[n]$ has the desired spectrum.

This is the principle behind many noise generators and the inverse problem (**whitening**): filter colored noise to get white.

## Why it matters
- **Real-world noise** (receiver 1/f noise, flicker noise, modeled interference) is usually colored.
- **Detection/estimation** optimal rules under colored noise involve prewhitening filters (e.g. matched filter after whitening).

## Related
- [[white-gaussian-process]]
- [[stationary-process]]
