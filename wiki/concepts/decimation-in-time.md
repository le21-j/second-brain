---
title: Decimation In Time (DIT)
type: concept
course: [[eee-404]]
tags: [fft, algorithm, dit]
sources: [[slides-fft-core-equations]]
created: 2026-04-21
updated: 2026-04-26
---

# Decimation In Time (DIT)

## In one line
"Split the time-domain signal by even and odd indices, recurse on each half." That's DIT.

## Example first
$x[n] = [a, b, c, d, e, f, g, h]$ ($N=8$). First DIT split:
- Even: $[a, c, e, g] \to$ feeds into a 4-point DFT $\to X_e[k]$
- Odd:  $[b, d, f, h] \to$ feeds into a 4-point DFT $\to X_o[k]$

Then glue with 4 butterflies: $X[k] = X_e[k] + W_8^k \cdot X_o[k]$, $X[k+4] = X_e[k] - W_8^k \cdot X_o[k]$ for $k=0,\ldots,3$.

Split again within each 4-pt DFT:
- $[a, c, e, g] \to$ even $[a, e]$, odd $[c, g]$
- $[b, d, f, h] \to$ even $[b, f]$, odd $[d, h]$

Split once more and you're at pairs; a 2-point DFT is trivial: $X[0]=x[0]+x[1]$, $X[1]=x[0]-x[1]$.

After 3 splits ($\log_2 8 = 3$), the input ordering is $[a, e, c, g, b, f, d, h] = [x[0], x[4], x[2], x[6], x[1], x[5], x[3], x[7]]$. This is **[[bit-reversed-order]]**.

## The idea
Writing the DFT as
$$X[k] = \sum_{n\text{ even}} x[n]\, W_N^{kn} + \sum_{n\text{ odd}} x[n]\, W_N^{kn}$$
and substituting $n = 2m$ (even) and $n = 2m+1$ (odd), and using the identity $(W_N)^2 = W_{N/2}$:

$$X[k] = \underbrace{\sum_{m=0}^{N/2-1} x[2m]\, W_{N/2}^{mk}}_{X_e[k]} + W_N^k \underbrace{\sum_{m=0}^{N/2-1} x[2m+1]\, W_{N/2}^{mk}}_{X_o[k]}$$

Both $X_e$ and $X_o$ are $N/2$-point DFTs. Do it $\log_2 N$ times and you've reduced the whole thing to 2-point DFTs.

The "decimation" name: you're **decimating** (sub-sampling) the time-domain signal by 2 each split. There's a dual called **Decimation In Frequency (DIF)** that does the analogous split on $X[k]$ instead of $x[n]$. This course uses DIT.

## The periodicity / half-circle tricks that make butterflies work
- $X_e$ and $X_o$ are $N/2$-periodic: $X_e[k + N/2] = X_e[k]$.
- $W_N^{k + N/2} = -W_N^k$.

Put those together and:
$$X[k + N/2] = X_e[k] + W_N^{k+N/2}\cdot X_o[k] = X_e[k] - W_N^k\cdot X_o[k]$$

That's the second butterfly equation — the one that gives you the "upper half" of the spectrum for free.

## Why it matters
DIT is the recipe. Every butterfly, every twiddle, every bit-reversal step in the FFT code is a direct consequence of "split by even/odd and recurse". Understanding this makes the three-loop [[butterfly]] structure feel inevitable rather than arbitrary.

## Common mistakes
- Mixing DIT and DIF conventions. DIT has bit-reversed **input**, natural-order output. DIF is the opposite. The lab uses DIT.
- Forgetting that $x[2m+1]\cdot W_N^{k(2m+1)} = x[2m+1]\cdot W_N^k\cdot W_{N/2}^{mk}$ — the $W_N^k$ is the **twiddle** pulled out front; the $W_{N/2}^{mk}$ is what makes $X_o$ an $N/2$-point DFT.

## Related
- [[fft]], [[butterfly]]
- [[bit-reversed-order]] — what the "decimated" input looks like
- [[twiddle-factor]]

## Practice
- [[fft-fundamentals-set-01]]
