---
title: Window Function
type: concept
course: [[eee-404]]
tags: [window, stft, spectrum]
sources: [[slides-window-functions]]
created: 2026-04-21
updated: 2026-04-26
---

# Window Function

## In one line
A window $w[n]$ is a weighting sequence you multiply your signal segment by before FFT, to control how the segment's edges affect the spectrum.

## Example first
You want to FFT $64$ samples of audio. If you just grab samples $0,\ldots,63$, you're implicitly using a **rectangular window** ($w[n] = 1$). The sharp edges at $n = 0$ and $n = 63$ create "ringing" artifacts in the spectrum — [[spectral-leakage]].

Try a **Hamming window** instead: $w[n] = 0.54 - 0.46\cdot\cos(2\pi n/63)$. This multiplies the signal so it fades to near-zero at the edges and is maximum in the middle. The spectrum now has smaller side lobes (less leakage) but a wider main lobe (slightly worse resolution).

## The general trade-off

| Property | Drives | Want to |
|---|---|---|
| **Main-lobe width** | Frequency resolution — can you separate two nearby tones? | Minimize |
| **Side-lobe height** | Leakage — does a strong tone bleed into other bins? | Minimize |

You can't win on both. Rectangular has the narrowest main lobe **and** the tallest side lobes. Hamming/Hann/Bartlett swap narrow main lobe for suppressed side lobes.

## The catalog

See individual pages for each:

- **[[rectangular-window]]** — $4\pi/L$ main lobe (narrowest), worst leakage
- **[[hamming-window]]** — $8\pi/L$ main lobe, small side lobes (slow decay)
- **[[hann-window]]** (Hanning) — $8\pi/L$ main lobe, small side lobes (**fast decay**) — good default
- **[[bartlett-window]]** (Triangular) — $\approx 8\pi/(L+1)$ main lobe, fast decay

## In practice
- **Hann** is the usual go-to for general-purpose spectral analysis.
- **Rectangular** only when you need peak frequency resolution and there are no strong interfering tones (or you don't care about leakage).
- **Hamming** when you need the first side lobe suppressed as much as possible (slightly better than Hann on the first side lobe).

## Related
- [[stft]] — the context
- [[spectral-leakage]] — the problem windows solve
- [[rectangular-window]], [[hamming-window]], [[hann-window]], [[bartlett-window]]

## Practice
- [[fft-fundamentals-set-01]]
