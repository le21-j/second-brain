---
title: Real-Valued FFT (N-pt via N/2-pt Complex)
type: concept
course: [[eee-404]]
tags: [fft, real-valued, optimization]
sources: [[slides-fft-real-valued-signal]]
created: 2026-04-21
updated: 2026-04-26
---

# Real-Valued FFT

## In one line
Pack a real $N$-point signal into a complex $N/2$-point signal, run an $N/2$-point FFT, then unpack — half the work of an $N$-point complex FFT.

## Example first
Real $x[n] = [1, 2, 0, 0]$ ($N = 4$).

**Pack:**
- $x_e[n] = x[2n] = [x[0], x[2]] = [1, 0]$
- $x_o[n] = x[2n+1] = [x[1], x[3]] = [2, 0]$
- $z[n] = x_e[n] + j\cdot x_o[n] = [$**$1+2j$**$, 0]$

**Run 2-point FFT of $z[n]$:** $Z[0] = z[0] + z[1] = 1+2j$. $Z[1] = z[0] - z[1] = 1+2j$.
So $Z = [1+2j, 1+2j]$.

**Extract $X_e$ and $X_o$ via conjugate symmetry:**
- $X_e[0] = (Z[0] + Z^*[0]) / 2 = ((1+2j) + (1-2j)) / 2 = $ **$1$**
- $X_e[1] = (Z[1] + Z^*[1]) / 2 = 1$
- $X_o[0] = (Z[0] - Z^*[0]) / (2j) = (4j) / (2j) = $ **$2$**
- $X_o[1] = (Z[1] - Z^*[1]) / (2j) = 2$

**Combine (last butterfly stage) with $W_4^0 = 1$, $W_4^1 = -j$:**
- $X[0] = X_e[0] + W_4^0\cdot X_o[0] = 1 + 2 = $ **$3$**
- $X[2] = X_e[0] - W_4^0\cdot X_o[0] = 1 - 2 = $ **$-1$**
- $X[1] = X_e[1] + W_4^1\cdot X_o[1] = 1 + (-j)(2) = $ **$1 - 2j$**
- $X[3] = X_e[1] - W_4^1\cdot X_o[1] = 1 - (-j)(2) = $ **$1 + 2j$**

$X[k] = [3, 1-2j, -1, 1+2j]$ $\checkmark$ matches direct DFT. See [[real-valued-fft-4pt]].

## The idea

**Step 1 — Pack** the $N$ real samples into $N/2$ complex samples by alternating even/odd into real/imag:
$$z[n] = x_e[n] + j\,x_o[n], \quad x_e[n] = x[2n], \quad x_o[n] = x[2n+1]$$

**Step 2 — FFT** $z[n]$ (size $N/2$ complex) to get $Z[k]$.

**Step 3 — Unpack.** Since $x_e$ and $x_o$ are real, their $N/2$-point DFTs $X_e$ and $X_o$ each satisfy conjugate symmetry. Using $Z[k] = X_e[k] + j\cdot X_o[k]$, you can algebraically separate:

$$X_e[k] = \frac{Z[k] + Z^*[(-k)_{N/2}]}{2}, \qquad X_o[k] = \frac{Z[k] - Z^*[(-k)_{N/2}]}{2j}$$

(where $(-k)_{N/2}$ means $-k$ modulo $N/2$).

**Step 4 — Combine** via one $N$-point butterfly stage:
$$X[k] = X_e[k] + W_N^k\cdot X_o[k], \qquad X[k+N/2] = X_e[k] - W_N^k\cdot X_o[k]$$

for $k = 0, 1, \ldots, N/2 - 1$.

## Why it matters
- **Complexity:** $(\log_2(N/2)\cdot N + 2N)$ real MULTs, vs. $2N\cdot\log_2(N)$ for a native $N$-point FFT. Roughly half.
- Real input is the common case in audio/DSP. Using this scheme is free performance.
- For **two** real signals $x_1, x_2$, there's an even tighter trick: stuff $z[n] = x_1[n] + j\cdot x_2[n]$, do a single $N$-point complex FFT, then unpack — one FFT for two real transforms.

## Complexity comparison ($N = 4$)

| Method | Real MULTs |
|---|---|
| Direct DFT | $4\cdot N^2 = $ **$64$** |
| $N$-point FFT | $2N\cdot\log_2 N = $ **$16$** |
| Real-input via $N/2$-pt complex FFT | $\log_2(N/2)\cdot N + 2N = $ **$12$** |

For $N = 64$ via complex 32-pt FFT: $\log_2(32)\cdot 64 + 128 = $ **$448$** real MULTs — that's the practice-question answer.

## Common mistakes
- Forgetting the $(-k) \bmod N/2$ when indexing $Z^*[\ldots]$. For $k = 0$, $(-0) \bmod N/2 = 0$, so $X_e[0] = \mathrm{Re}\{Z[0]\}$, $X_o[0] = \mathrm{Im}\{Z[0]\} / 1$. For $k > 0$, you wrap around.
- Using $W_{N/2}$ instead of $W_N$ in the combine step. The final butterfly is at the **$N$-point** level.

## Related
- [[conjugate-symmetry]]
- [[fft]], [[butterfly]]
- [[dft-computation-complexity]]

## Practice
- [[fft-fundamentals-set-01]]
- Worked example: [[real-valued-fft-4pt]]
