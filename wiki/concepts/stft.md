---
title: Short Time Fourier Transform (STFT)
type: concept
course: [[eee-404]]
tags: [stft, fft, time-frequency]
sources: [[slides-window-functions]]
created: 2026-04-21
updated: 2026-04-26
---

# Short Time Fourier Transform (STFT)

## In one line
Run the DFT on a **moving window** of the signal so you can track **when** different frequencies show up, not just whether they're there.

## Example first
You have $5$ seconds of audio sampled at $8$ kHz ($40{,}000$ samples). A one-shot DFT tells you which frequencies are present *over the whole 5 seconds* — but not whether a note played at second 1 or second 4.

STFT fix: grab a segment of $L = 512$ samples ($64$ ms), multiply it by a window $w[n]$, take the FFT $\to$ one spectrum for that $64$ ms slice. Slide the window forward (e.g. by $256$ samples), repeat. You now have a 2D array (time $\times$ frequency) $= $ a **spectrogram**.

Every audio spectrogram you've ever seen is an STFT.

## The idea
- Pick a window length $L$ (controls [[frequency-resolution]] $\Delta f = f_s/L$ for each slice).
- For each time $t_m = m \cdot \text{hop}$:
  - $s_m[n] = x[t_m + n] \cdot w[n]$ for $n = 0, \ldots, L-1$
  - $S_m[k] = $ DFT of $s_m[n]$
- Stack $S_m$ across $m \to$ spectrogram.

## Why multiply by a window?
Grabbing a hard-edged segment ($= $ multiplying by a rectangular window) introduces **[[spectral-leakage]]**: the abrupt ends in the time segment create artifacts in the spectrum. Smoothly tapering the ends (Hamming, Hann, Bartlett) reduces leakage at the cost of slightly wider main lobes. See [[window-function]].

## The time–frequency trade-off
- **Long window (big $L$):** fine frequency resolution, poor time resolution. You know *which* frequencies are there but not precisely when.
- **Short window (small $L$):** fine time resolution, poor frequency resolution. You know *when* something happened but not precisely what frequency.

This is unavoidable — it's the uncertainty principle for signals.

## Common mistakes
- Using a rectangular window for STFT when you care about spectral cleanness. Default to Hann.
- Picking hop size too small (massive redundancy) or too big (missing events between windows). Typical hop $= L/2$.
- Forgetting that DFT assumes a periodic signal. Windows "fake" periodicity at the segment boundaries.

## Related
- [[window-function]]
- [[spectral-leakage]]
- [[frequency-resolution]]
- [[dft]], [[fft]]
