---
title: Discrete Fourier Transform (DFT)
type: concept
course: [[eee-404]]
tags: [dft, fft, fundamentals]
sources: [[slides-fft-core-equations]]
created: 2026-04-21
updated: 2026-04-26
---

# Discrete Fourier Transform (DFT)

## In one line
The DFT takes $N$ time-domain samples $x[0], \ldots, x[N-1]$ and returns $N$ frequency-domain samples $X[0], \ldots, X[N-1]$, each $X[k]$ being a weighted sum of the $x[n]$ tagged by a complex phase.

## Example first
Take $x[n] = [1, 2, 0, 0]$ (a 4-point signal). Compute $X[0]$:

$$X[0] = \sum_{n=0}^{3} x[n]\cdot W_4^{0 \cdot n} = x[0] + x[1] + x[2] + x[3] = 1+2+0+0 = 3$$

$X[0]$ is just the **sum** of all samples — i.e. the DC component. Now $X[1]$:

$$X[1] = x[0]\cdot W_4^0 + x[1]\cdot W_4^1 + x[2]\cdot W_4^2 + x[3]\cdot W_4^3$$
$$= 1 + 2\cdot(-j) + 0 + 0 = 1 - 2j$$

Continuing: $X[2] = -1$, $X[3] = 1+2j$. So $X[k] = [3, 1-2j, -1, 1+2j]$. This is exactly the example used in [[idft-4pt-via-fft]].

## The idea
$X[k]$ measures **how much of frequency bin $k$ is present in the signal**. You correlate $x[n]$ against a complex sinusoid spinning at digital frequency $2\pi k/N$. A big $|X[k]|$ means the signal has strong energy at that frequency; a small one means it doesn't. The full $X$ is the signal re-expressed as a sum of $N$ complex sinusoids.

## Formal definition

$$X[k] = \sum_{n=0}^{N-1} x[n]\, W_N^{kn}, \qquad k = 0, 1, \ldots, N-1$$

where $W_N = e^{-j2\pi/N}$ is the [[twiddle-factor]].

## Why it matters / when you use it
- Spectrum analysis: what frequencies are in this signal?
- Filtering in frequency domain (multiply $X$ by filter, inverse transform).
- Foundation for [[fft]], [[stft]], OFDM modulation, MP3/JPEG, almost all DSP.

## Complexity
Direct computation: **$N^2$ complex multiplies**, $N(N-1)$ complex adds. Prohibitively expensive for large $N$ — see [[dft-computation-burden]] for the 5-min-speech "38 hours" calculation. That's why [[fft]] exists.

## Common mistakes
- Forgetting the **minus sign** in the exponent: DFT has $e^{-j2\pi kn/N}$; IDFT has $e^{+j2\pi kn/N}$. See [[idft]].
- Assuming $X$ is real. It's **complex** in general, even if $x$ is real. For real $x$, conjugate symmetry $X[N-k] = X^*[k]$ holds — see [[conjugate-symmetry]].
- Confusing $k$ (bin index) with frequency in Hz. Bin $k$ corresponds to $f_k = k\cdot f_s/N$. See [[dft-bin-interpretation]].

## Related
- [[fft]] — same thing, fast
- [[idft]] — inverse
- [[twiddle-factor]] — the $W_N^{kn}$ term
- [[frequency-resolution]] — $\Delta f = f_s/N$ per bin

## Practice
- [[fft-fundamentals-set-01]] — multiple problems on DFT mechanics
