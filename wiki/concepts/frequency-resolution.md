---
title: Frequency Resolution
type: concept
course: [[eee-404]]
tags: [fft, resolution]
sources: [[slides-fft-interpretation]], [[slides-fft-real-valued-signal]]
created: 2026-04-21
updated: 2026-04-26
---

# Frequency Resolution

## In one line
$\Delta f = $ **$f_s / N$** — how many Hertz apart adjacent DFT bins are. Also, $f_k = $ **$k \cdot \Delta f$** gives the frequency that bin $k$ represents.

## Example first
- $f_s = 8192$ Hz, $N = 64 \to \Delta f = 128$ Hz. Can resolve tones separated by $\geq 128$ Hz.
- $f_s = 8192$ Hz, $N = 128 \to \Delta f = 64$ Hz. Resolution doubled.
- $f_s = 44100$ Hz, $N = 1024 \to \Delta f \approx 43$ Hz. Fine enough to see a single musical note without smearing into neighbors.

**Trade-off:** doubling $N$ halves $\Delta f$ but doubles the compute cost (and the latency, since you need more samples before you can compute).

## The one-line intuition

> **Bin $k$ tests whether the signal has exactly $k$ complete cycles inside the $N$-sample window.**

Every formula below is a consequence of that single fact.

## Derivation — "cycles per window" route

Collect $N$ samples at sampling rate $f_s$. The window has duration

$$T_{\text{window}} = \frac{N}{f_s}\text{ seconds}$$

If a sinusoid completes **$k$** full cycles inside that window, its frequency is

$$f_k = \frac{\text{cycles}}{\text{seconds}} = \frac{k}{N/f_s} = k\cdot\frac{f_s}{N}$$

**Bin spacing** is the frequency step from $k$ to $k+1$:

$$\Delta f = f_{k+1} - f_k = (k+1)\frac{f_s}{N} - k\frac{f_s}{N} = \boxed{\frac{f_s}{N}}$$

So **$f_k = k \cdot \Delta f$**.

## Derivation — from the DFT definition (algebraic route)

The DFT is:

$$X[k] = \sum_{n=0}^{N-1} x[n]\,e^{-j2\pi kn/N}$$

Each $X[k]$ is the inner product of $x[n]$ against the complex sinusoid $e^{-j2\pi kn/N}$ — a specific test frequency. Pin down that frequency.

The phase at sample $n$ is $\phi(n) = -2\pi k n / N$, so the **digital (rad/sample) angular frequency** is

$$\omega_k = \frac{2\pi k}{N}\text{ rad/sample}$$

Convert to **analog angular frequency** (rad/sec) by multiplying by samples/sec $= f_s$:

$$\Omega_k = \omega_k\cdot f_s = \frac{2\pi k\cdot f_s}{N}\text{ rad/s}$$

Convert rad/s to Hz by dividing by $2\pi$:

$$f_k = \frac{\Omega_k}{2\pi} = \boxed{k\cdot\frac{f_s}{N}}$$

Identical answer. The "cycles-per-window" picture and the DFT algebra describe the same fact.

## Match against a specific sinusoid

Input signal $x(t) = \sin(2\pi\cdot 256\cdot t)$ sampled at $f_s = 8192$ Hz, $N = 128$ samples:

$$x[n] = \sin\!\left(2\pi\cdot 256\cdot\frac{n}{8192}\right) = \sin\!\left(2\pi\cdot\frac{256}{8192}\cdot n\right) = \sin\!\left(\frac{2\pi\cdot 4\cdot n}{128}\right)$$

Compare with bin-$k$ basis $\sin(2\pi k n/N)$ at $N = 128$. Matches when **$k = 4$**. So $X[4]$ is non-zero. Conjugate symmetry (real signal) puts another non-zero bin at $X[128-4] = X[124]$. See [[conjugate-symmetry]].

## The "frequency slot" picture

The DFT splits $[0, f_s)$ into $N$ equal-width slots of size $\Delta f$:

```
 bin:    0      1      2      3      4      5    ...   N-1
         |------|------|------|------|------|--... ----|
  Hz:    0     Δf    2·Δf   3·Δf   4·Δf   ...       (N-1)·Δf
```

With $f_s = 8192$, $N = 128$: each slot is $64$ Hz wide, bin $4$ is at $256$ Hz. Bins $k > N/2$ represent negative frequencies by conjugate symmetry for real inputs.

## The three equivalent forms

$$\text{Digital: } \Delta\omega = \frac{2\pi}{N}\text{ rad/sample}$$

$$\text{Analog angular: } \Delta\Omega = 2\pi\cdot\frac{f_s}{N}\text{ rad/s}$$

$$\text{Analog in Hz: } \Delta f = \frac{f_s}{N}$$

## The two facts you'll actually use

1. **$\Delta f = f_s / N$** — bin-to-bin spacing in Hz.
2. **$f_k = k \cdot \Delta f$** — frequency at bin $k$.

Inverse: which bin does a given $f$ land in? **$k = f / \Delta f = f\cdot N / f_s$.**

## Why it matters
- Designing an FFT size: pick $N$ so $\Delta f$ is fine enough to separate the tones you care about.
- Longer observation window $\to$ finer resolution. Can't get better resolution without waiting longer.
- Zero-padding $x[n]$ to $2N$ before FFT **looks** like double resolution but really just interpolates between bins — doesn't give you new information.

## Common mistakes
- Confusing resolution ($\Delta f$) with Nyquist ($f_s/2$). Nyquist is the highest representable frequency; resolution is the spacing.
- Thinking more samples magically resolves closer tones. It's not $N$ alone — it's the **observation window length** $T = N/f_s$. Two signals closer in frequency than $1/T$ can't be distinguished.
- Forgetting that bins $k > N/2$ mirror back as negative frequencies for real inputs.

## Related
- [[dft-bin-interpretation]]
- [[nyquist-frequency]]
- [[conjugate-symmetry]]
- [[spectral-leakage]]
- [[frequency-bin-256hz]] — worked example using these formulas

## Practice
- [[fft-fundamentals-set-01]]
