---
title: Inverse DFT (IDFT)
type: concept
course: [[eee-404]]
tags: [idft, fft, inverse]
sources: [[slides-fft-idft]]
created: 2026-04-21
updated: 2026-04-26
---

# Inverse DFT (IDFT)

## In one line
Given $X[k]$, recover $x[n] = (1/N) \sum X[k]\cdot e^{+j2\pi kn/N}$. You can compute it **using your existing FFT** with two complex-conjugations.

## Example first
Given $X[k] = [3, 1-2j, -1, 1+2j]$, recover $x[n]$:

1. **Conjugate $X$:** $X^*[k] = [3, 1+2j, -1, 1-2j]$
2. **Bit-reverse** (for $N=4$, positions $0,1,2,3 \to 0,2,1,3$): $[3, -1, 1+2j, 1-2j]$
3. **Run forward FFT** on this sequence $\to [4, 8, 0, 0]$
4. **Divide by $N = 4$:** $[1, 2, 0, 0]$
5. **Conjugate the result:** $[1, 2, 0, 0]$ (real, so no change)

That's $x[n] = [1, 2, 0, 0]$. See [[idft-4pt-via-fft]] for the full butterfly diagram.

## The idea
The IDFT definition has a **$+$** sign in the exponent where the DFT has a minus:
$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k]\, e^{+j2\pi kn/N}$$

Taking the complex conjugate of both sides:
$$x^*[n] = \frac{1}{N}\sum_{k=0}^{N-1} X^*[k]\, e^{-j2\pi kn/N}$$

The right-hand side is **$1/N$ times the forward DFT of $X^*[k]$**. So:

$$x[n] = \frac{1}{N}\bigl(\mathrm{conj} \circ \mathrm{FFT} \circ \mathrm{conj}\bigr)(X[k])$$

Four steps: **conjugate, FFT, divide by $N$, conjugate**. No separate IFFT code needed — your existing forward FFT does the job.

## Formal definition

$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k]\cdot W_N^{-kn}, \qquad n = 0, 1, \ldots, N-1$$

where $W_N^{-1} = e^{+j2\pi/N}$ is the conjugate of the forward [[twiddle-factor]].

## Why it matters
Anywhere you transform *to* the frequency domain and want to come back — filtering, convolution via frequency domain, MP3 decoding, OFDM demodulation — you need the IDFT. And you almost never implement it separately; you reuse the forward FFT.

## Common mistakes
- Forgetting the divide-by-$N$ step. Without it the magnitudes are off by a factor of $N$.
- Skipping the second conjugation when the result is complex. For real $x$, the second conj is identity, but in general it matters.
- Confusing sign conventions with other textbooks. Some put the $1/N$ on the **forward** transform; Dr. Wang's slides put it on the inverse. Stay consistent within the course.

## Related
- [[dft]], [[fft]]
- [[twiddle-factor]]
- [[bit-reversed-order]]

## Practice
- [[fft-fundamentals-set-01]] — includes the IDFT-via-FFT exercise
- Worked example: [[idft-4pt-via-fft]]
