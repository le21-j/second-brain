---
title: Example — 4-pt IDFT via Forward FFT
type: example
course: [[eee-404]]
tags: [idft, fft]
sources: [[slides-fft-idft]]
created: 2026-04-21
updated: 2026-04-26
---

# Example — 4-point IDFT via Forward FFT

Recover $x[n]$ from $X[k] = [3, 1-2j, -1, 1+2j]$ using the forward-FFT-with-conjugation recipe from [[idft]].

## Twiddle values ($N = 4$)
- $W_4^0 = 1$
- $W_4^1 = -j$
- $W_2^0 = 1$ (used in the first butterfly stage when splitting)

## Step 1 — Conjugate $X[k]$
$X^*[k] = [3, $ **$1+2j$**$, -1, $ **$1-2j$**$]$

## Step 2 — Bit-reverse for $N = 4$
Positions $(0,1,2,3)$ become $(0,2,1,3)$. See [[bit-reversed-order]].

Reordered: $[3, -1, 1+2j, 1-2j]$

## Step 3 — Two stages of butterflies (forward FFT)

### Stage 1 ($D = 2$, pairs)
- Pair (indices $0, 1$): $X_e[0] = 3 + (-1)\cdot W_2^0 = 3 - 1 = $ **$2$**. $X_e[1] = 3 - (-1)\cdot 1 = $ **$4$**.
- Pair (indices $2, 3$): $X_o[0] = (1+2j) + (1-2j)\cdot 1 = $ **$2$**. $X_o[1] = (1+2j) - (1-2j) = $ **$4j$**.

Working array after stage 1: $[2, 4, 2, 4j]$.

### Stage 2 ($D = 4$, final butterfly)
- $k=0$: $X[0] = X_e[0] + W_4^0\cdot X_o[0] = 2 + 1\cdot 2 = $ **$4$**. $X[2] = 2 - 2 = $ **$0$**.
- $k=1$: $X[1] = X_e[1] + W_4^1\cdot X_o[1] = 4 + (-j)\cdot(4j) = 4 + 4 = $ **$8$**. $X[3] = 4 - 4 = $ **$0$**.

FFT output: $[4, 8, 0, 0]$.

## Step 4 — Divide by $N$ and conjugate
- Divide by $4$: $[1, 2, 0, 0]$
- Conjugate: $[1, 2, 0, 0]$ (already real, no change)

**$x[n] = [1, 2, 0, 0]$** $\checkmark$ matches the textbook answer.

## Exercise (from the slides)
Do the same for $X[k] = [5, 3+2j, -3, 3-2j]$. Expected result: **$x[n] = [2, 1, -1, 3]$**.

<details><summary>Worked solution</summary>

1. Conjugate: $[5, 3-2j, -3, 3+2j]$
2. Bit-reverse: $[5, -3, 3-2j, 3+2j]$
3. Stage 1: $X_e = [5-3, 5+3] = [2, 8]$; $X_o = [(3-2j)+(3+2j), (3-2j)-(3+2j)] = [6, -4j]$.
4. Stage 2: $X[0] = 2 + 6 = $ **$8$**. $X[2] = 2 - 6 = $ **$-4$**. $X[1] = 8 + (-j)(-4j) = 8 - 4 = $ **$4$**. $X[3] = 8 + 4 = $ **$12$**.
5. Output $[8, 4, -4, 12]$, divide by $4 \to [2, 1, -1, 3]$. Conjugate (real): **$[2, 1, -1, 3]$** $\checkmark$

</details>

## Related
- [[idft]], [[fft]]
- [[bit-reversed-order]]
- [[butterfly]]
