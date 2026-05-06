---
title: Example — Real-Input 4-pt FFT via Complex 2-pt FFT
type: example
course:
  - "[[eee-404]]"
tags: [fft, real-valued]
sources:
  - "[[slides-fft-real-valued-signal]]"
created: 2026-04-21
updated: 2026-05-06
---

# Example — Real-Input 4-pt FFT via Complex 2-pt FFT

Compute $X[k]$ for the real signal $x[n] = [1, 2, 0, 0]$ using the $N/2$-point complex FFT trick. See [[real-valued-fft]] for the theory.

## Step 1 — Pack
- $x_e[n] = x[2n] = [1, 0]$
- $x_o[n] = x[2n+1] = [2, 0]$
- $z[n] = x_e[n] + j\cdot x_o[n] = $ **$[1 + 2j, 0]$**

## Step 2 — 2-point complex FFT of $z[n]$
Two-point DFT: $Z[0] = z[0] + z[1]$, $Z[1] = z[0] - z[1]$.
- $Z[0] = (1+2j) + 0 = $ **$1 + 2j$**
- $Z[1] = (1+2j) - 0 = $ **$1 + 2j$**

## Step 3 — Extract $X_e, X_o$

Using:
- $X_e[k] = (Z[k] + Z^*[(-k) \bmod N/2]) / 2$
- $X_o[k] = (Z[k] - Z^*[(-k) \bmod N/2]) / (2j)$

For $N/2 = 2$, so $(-0) \bmod 2 = 0$ and $(-1) \bmod 2 = 1$:

- $X_e[0] = (Z[0] + Z^*[0])/2 = ((1+2j) + (1-2j))/2 = $ **$1$**
- $X_e[1] = (Z[1] + Z^*[1])/2 = ((1+2j) + (1-2j))/2 = $ **$1$**
- $X_o[0] = (Z[0] - Z^*[0])/(2j) = ((1+2j) - (1-2j))/(2j) = (4j)/(2j) = $ **$2$**
- $X_o[1] = (Z[1] - Z^*[1])/(2j) = 2$ (same calculation)

## Step 4 — Combine with final butterfly ($W_4^0 = 1, W_4^1 = -j$)
- $X[0] = X_e[0] + W_4^0\cdot X_o[0] = 1 + 2 = $ **$3$**
- $X[2] = X_e[0] - W_4^0\cdot X_o[0] = 1 - 2 = $ **$-1$**
- $X[1] = X_e[1] + W_4^1\cdot X_o[1] = 1 + (-j)(2) = $ **$1 - 2j$**
- $X[3] = X_e[1] - W_4^1\cdot X_o[1] = 1 - (-j)(2) = $ **$1 + 2j$**

**$X[k] = [3, 1 - 2j, -1, 1 + 2j]$** $\checkmark$ matches a direct 4-pt DFT of $[1, 2, 0, 0]$.

## Exercise
Same process for $x[n] = [2, 1, -1, 3]$. Expected: **$X[k] = [5, 3 + 2j, -3, 3 - 2j]$**.

<details><summary>Hint</summary>

$z[n] = [2 + j, -1 + 3j]$. After 2-pt FFT: $Z[0] = 1 + 4j$, $Z[1] = 3 - 2j$. Extract $X_e = [1, 4]$, $X_o = [3, -2]$. Final combine gives the answer.

</details>

## Operation count check
- 4-pt direct DFT: $4N^2 = $ **$64$** real MULTs
- 4-pt FFT (native): $2N\cdot\log_2 N = $ **$16$** real MULTs
- Real-input via 2-pt complex FFT: $\log_2(N/2)\cdot N + 2N = $ **$12$** real MULTs $\leftarrow$ best

## Related
- [[real-valued-fft]]
- [[conjugate-symmetry]]
- [[dft-computation-complexity]]
