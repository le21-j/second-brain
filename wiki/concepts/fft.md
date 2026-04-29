---
title: Fast Fourier Transform (FFT)
type: concept
course: [[eee-404]]
tags: [fft, dft, algorithm]
sources: [[slides-fft-core-equations]], [[slides-fft-implementation]]
created: 2026-04-21
updated: 2026-04-26
---

# Fast Fourier Transform (FFT)

## In one line
The FFT is **not a new transform** — it's the DFT computed faster, by cleverly reusing partial sums instead of redoing them.

## Example first
For $N = 8$, direct DFT costs $N^2 = 64$ complex multiplies. An 8-point FFT costs roughly $(N/2)\cdot\log_2 N = 12$ complex multiplies — **over 5x speedup**. For $N = 1024$, FFT is $\approx 200\times$ faster. For $N = 2.4$ million (5 minutes of 8 kHz speech), the difference is 38 hours vs. a couple seconds. See [[dft-computation-burden]].

## The idea
Split $x[n]$ into even-indexed and odd-indexed subsequences:

$$X[k] = \underbrace{\sum_{m=0}^{N/2-1} x[2m]\, W_{N/2}^{mk}}_{X_e[k]} + W_N^k \cdot \underbrace{\sum_{m=0}^{N/2-1} x[2m+1]\, W_{N/2}^{mk}}_{X_o[k]}$$

Now you have **two $N/2$-point DFTs** ($X_e$ and $X_o$), glued by a twiddle factor $W_N^k$. Each of those $N/2$-point DFTs can be split the same way $\to$ recurse. After $\log_2 N$ splits, each sub-DFT is a single sample, which is trivial.

The glue between $X_e$ and $X_o$ is the **[[butterfly]]**:
- $X[k] = X_e[k] + W_N^k \cdot X_o[k]$
- $X[k + N/2] = X_e[k] - W_N^k \cdot X_o[k]$

(Those two equations come from the periodicity identity $W_N^{k+N/2} = -W_N^k$ — halving the work of the second half.)

## Formal definition
For $N = 2^\nu$ (radix 2, decimation in time), the FFT is the DFT of $x[n]$ computed by $\log_2 N$ stages of butterflies, $N/2$ butterflies per stage, using precomputed [[twiddle-factor|twiddle factors]].

## Why it matters
Turns an $O(N^2)$ algorithm into an **$O(N \log N)$** one. Without it, spectral analysis on anything larger than a few hundred samples would be impractical — no real-time audio, no OFDM, no image compression.

## Common mistakes
- Thinking FFT and DFT are different transforms. They give **identical outputs**. FFT is just the algorithm.
- Forgetting the input must be in **bit-reversed order** before a [[decimation-in-time]] FFT (or the output comes back in bit-reversed order, depending on convention). See [[bit-reversed-order]].
- $N$ must be a power of 2 (for radix-2). If $N$ isn't, zero-pad or use a different-radix FFT.

## Related
- [[dft]] — same output, slow
- [[butterfly]] — the atomic operation
- [[decimation-in-time]] — the even/odd split algorithm
- [[twiddle-factor]] — the $W_N^k$ weights
- [[bit-reversed-order]] — required input ordering
- [[fft-scaling]] — overflow prevention
- [[real-valued-fft]] — optimization for real inputs

## Practice
- [[fft-fundamentals-set-01]]
