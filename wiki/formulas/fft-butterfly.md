---
title: FFT Butterfly (Formula)
type: formula
course:
  - "[[eee-404]]"
tags: [fft, butterfly]
sources:
  - "[[slides-fft-core-equations]]"
  - "[[slides-fft-implementation]]"
created: 2026-04-21
updated: 2026-05-06
---

# FFT Butterfly — Formula

## Equations

$$X[k]         = X_e[k] + W_N^k\, X_o[k], \qquad k = 0, 1, \ldots, \tfrac{N}{2}-1$$
$$X[k + N/2]   = X_e[k] - W_N^k\, X_o[k], \qquad k = 0, 1, \ldots, \tfrac{N}{2}-1$$

## Why the minus sign in the second line
From the half-circle identity $W_N^{k+N/2} = -W_N^k$, combined with the periodicity $X_e[k+N/2] = X_e[k]$ and $X_o[k+N/2] = X_o[k]$:

$$X[k+N/2] = X_e[k+N/2] + W_N^{k+N/2}X_o[k+N/2] = X_e[k] + (-W_N^k)X_o[k]$$

## Complex-multiply expansion
If $U = U_r + jU_i$ and $X[k] = A + jB$, then $\text{temp} = U\cdot X[k]$:
- $\text{temp}_r = U_r\cdot A - U_i\cdot B$
- $\text{temp}_i = U_r\cdot B + U_i\cdot A$

## Scaled variant (with overflow scaling; see [[fft-scaling]])

$$X[k]         = s\,(X_e[k] + W_N^k\, X_o[k])$$
$$X[k + N/2]   = s\,(X_e[k] - W_N^k\, X_o[k])$$

Typically $s = 0.5$ per stage, with final output multiplied by $N$.

## Related
- [[butterfly]] — conceptual page
- [[twiddle-factor]]
- [[fft-scaling]]
