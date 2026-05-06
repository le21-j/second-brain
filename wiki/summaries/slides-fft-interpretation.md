---
title: Slides — FFT Interpretation
type: summary
source_type: slides
source_path: raw/slides/eee-404/FFT_interpretation.pdf
course:
  - "[[eee-404]]"
tags: [fft, interpretation, frequency-resolution, nyquist]
created: 2026-04-21
updated: 2026-05-06
---

# Slides — FFT Interpretation

## TL;DR
How to read a DFT result. Once you've computed $X[k]$, what does bin $k$ *mean*? The bin-to-frequency map is linear: $f_k = k\cdot(f_s/N)$ for $k$ in $[0, N/2]$, negative frequencies live in $[N/2+1, N-1]$. $X[0]$ is DC, $X[N/2]$ is the Nyquist frequency. $\Delta f = f_s/N$ is the frequency resolution.

## Key takeaways
- **Frequency resolution** $\Delta f = f_s / N$ (Hz per bin).
- **Bin meaning:**
  - $k = 0$: DC ($f = 0$)
  - $k = 1, \ldots, N/2 - 1$: positive frequencies $f_k = k\cdot\Delta f$
  - $k = N/2$: Nyquist frequency $f_s/2$
  - $k = N/2 + 1, \ldots, N - 1$: negative frequencies $f_k = (k - N)\cdot\Delta f$
- **Real input trick:** since $x[n]$ is real, $X[N-k] = X^*[k]$ — the "negative frequency" bins are conjugates of positive-frequency bins. For a real cosine/sine at frequency $f$, you get non-zero values at both $k = f/\Delta f$ and $k = N - f/\Delta f$.

## Concepts introduced or reinforced
- [[dft-bin-interpretation]] — the full $k \to f$ mapping
- [[frequency-resolution]] — $\Delta f = f_s/N$
- [[nyquist-frequency]] — $f_s/2$
- [[conjugate-symmetry]] — real input $\Rightarrow X[N-k] = X^*[k]$

## Worked examples worth remembering
- $f = 256$ Hz, $f_s = 8192$ Hz, $N = 64$: $\Delta f = 128$. $X[2]$ (256 Hz) and $X[62]$ ($-256$ Hz) are non-zero. See [[frequency-bin-256hz]].
- Practice: $f_s = 8192$, $N = 128$, $X[4]$ and $X[124]$ nonzero $\to f = ?$ (answer: 256 Hz).

## Questions this source raised
- For complex-valued $x[n]$, the negative bins are *different* info, not mirrored conjugates. We mostly deal with real-valued signals in this course; keep the caveat in mind.
