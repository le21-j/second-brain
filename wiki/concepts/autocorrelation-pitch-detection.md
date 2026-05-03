---
title: Autocorrelation Pitch Detection
type: concept
course: [[eee-404]]
tags: [eee-404, dsp, fft, autocorrelation, pitch, wiener-khinchin]
sources: [[lab-eee-404-project-2-fft-applications]]
created: 2026-05-02
updated: 2026-05-02
---

# Autocorrelation Pitch Detection

## In one line
The pitch (fundamental frequency $f_0$) of a periodic signal can be read straight off the **first non-trivial peak** of its autocorrelation function — and you can compute autocorrelation for free as $\mathrm{IFFT}(|\mathrm{FFT}(x)|^2)$.

## Example first
Record yourself saying the vowel "a" for one second at $f_s = 8000$ Hz. Take a 512-sample window from the middle. Compute its FFT, square the magnitude, then inverse-FFT — that's the autocorrelation $r[k]$. The plot looks like:

```
r[k]
 |█
 | █
 |  ██     ▄▄
 |    ██▄▄▀  ▀▄▄              ▄▄▄
 |       ▀▀     ▀▄▄▄▄▄▄▄▄▄▄▄▀▀   ▀▄▄
 +-----------------------------------> k
 0    ↑                          
   first peak ≈ k = 73
```

Lag 0 is always the global max (every signal correlates perfectly with itself). The **first peak after lag 0** sits at $k \approx 73$ samples. Convert:

$$f_0 = \frac{f_s}{k} = \frac{8000}{73} \approx 110\ \text{Hz}$$

That's the pitch. The MATLAB reference script `vowel_analysis.m` does exactly this and prints `pitch = 1/((max_index-1)/fs)`.

## The idea
A periodic signal $x[n]$ with period $T$ samples satisfies $x[n] \approx x[n+T]$. So the autocorrelation

$$r[k] = \sum_{n} x[n]\,x[n+k]$$

is large whenever $k$ is a multiple of $T$. Among the integer lags, the **smallest** $k > 0$ that produces a peak gives the period; everything else is a harmonic of it.

## Formal definition
For a wide-sense-stationary real signal, **Wiener–Khinchin** says

$$r[k] = \mathcal{F}^{-1}\!\bigl\{\,|X(\omega)|^2\,\bigr\}$$

i.e., the autocorrelation is the inverse Fourier transform of the **power spectrum**. So given an FFT, you compute autocorrelation in $O(N \log N)$ instead of $O(N^2)$ from the time-domain definition.

The pitch period $T$ in samples is the index of the first local maximum of $r[k]$ for $k > 0$, ignoring the trivial $r[0]$ peak. The fundamental frequency in Hz is

$$f_0 = \frac{f_s}{T}.$$

## Why it matters / when you use it
- **Vowel analysis / speech coding** — pitch detection is foundational for voiced/unvoiced classification, vocoders (LPC, MELP, AMR), and pitch-shifting.
- **Music transcription** — fundamental frequency of a sustained note.
- **Cheap sinusoidal frequency estimator** — when an FFT bin would be too coarse, autocorrelation between zero crossings is finer.
- **Voiced-speech-only.** Unvoiced fricatives ("s", "f", "sh") have no periodicity — autocorrelation has no clear peak. You only run pitch detection on voiced segments.

## Common mistakes
- **Confusing pitch with formants.** Pitch is the periodicity of the **glottal source**; formants are **resonances of the vocal tract**. They are independent. The same pitch can have very different formants. See [[formant]].
- **Picking the lag-0 peak.** $r[0] = \sum x[n]^2$ is always the global max. The pitch period is the **first peak after** $k = 0$.
- **Forgetting to skip the self-correlation peak.** If lag 0 is itself a local maximum (always the case), the algorithm has to ignore index 0 when searching for the first real peak. The starter MATLAB script handles this with `index_offset`; the C version does the same with `peaks_index[0] == 0`.
- **Using too short a window.** If the window length $N$ is shorter than one period $T$, you cannot see periodicity at all. For human speech ($f_0 \in [80, 300]$ Hz at $f_s = 8000$ Hz, $T \in [27, 100]$ samples) a 512-sample window is comfortably long enough.

## Related
- [[fft]] — used to compute autocorrelation efficiently.
- [[real-valued-fft]] — speech is real-valued; CMSIS rFFT applies.
- [[window-function]] — windowing affects the autocorrelation shape; for pitch detection, rectangular is acceptable because we only care about peak **location**, not amplitude.
- [[stft]] — running pitch detection over time = pitch contour.
- [[formant]] — the *other* spectral feature of a vowel.

## Practice
- *(none yet — could generate a synthetic-vowel set: sum of sinusoids at $f_0$ and its harmonics shaped by a vocal-tract envelope, then estimate pitch from autocorrelation.)*
