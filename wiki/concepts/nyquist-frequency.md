---
title: Nyquist Frequency
type: concept
course: [[eee-404]]
tags: [sampling, dsp]
sources: [[slides-fft-interpretation]]
created: 2026-04-21
updated: 2026-04-26
---

# Nyquist Frequency

## In one line
The highest frequency that can be uniquely represented at sampling rate $f_s$ is **$f_s/2$**.

## Example first
- Sampling at $f_s = 8192$ Hz $\to$ Nyquist $= 4096$ Hz. Any analog tone above $4096$ Hz gets **aliased** into $0$–$4096$ Hz and is indistinguishable from a different, lower tone.
- In an $N = 64$ DFT at $f_s = 8192$, bin **$k = N/2 = 32$** is exactly the Nyquist frequency $4096$ Hz.

## The idea
A sinusoid is only "trackable" by samples if there are at least two samples per cycle. Less than that, and a high-frequency signal looks (to the samples) exactly like a lower-frequency one — aliasing.

In DFT terms, bin $N/2$ is the only self-conjugate bin (besides DC): $X[N/2] = X^*[N - N/2] = X^*[N/2]$, so it must be **real**.

## Why it matters
- Any analog signal should be low-pass filtered before sampling so nothing above $f_s/2$ exists.
- In the DFT output, bin $N/2$ is the "last" positive frequency. Bins above it loop back as negative frequencies — see [[dft-bin-interpretation]].

## Common mistakes
- Calling $f_s$ the Nyquist rate — **$f_s/2$** is the Nyquist frequency; $f_s$ (or $2\cdot f_{\max}$) is sometimes called the Nyquist *rate*. The slides call $f_s/2$ the Nyquist frequency.
- Forgetting that there's only **one** bin at Nyquist (no conjugate pair), unlike other positive frequencies.

## Related
- [[dft-bin-interpretation]]
- [[frequency-resolution]]
