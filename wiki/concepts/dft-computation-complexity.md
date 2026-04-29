---
title: DFT/FFT Computation Complexity
type: concept
course: [[eee-404]]
tags: [fft, complexity]
sources: [[slides-fft-core-equations]], [[slides-fft-real-valued-signal]]
created: 2026-04-21
updated: 2026-04-26
---

# DFT/FFT Computation Complexity

## In one line
Direct DFT: **$O(N^2)$**. FFT: **$O(N \log N)$**. Real-input FFT (via $N/2$-pt complex): still **$O(N \log N)$** but with smaller constant.

## Example first
$N = 64$:

| Method | Complex MULTs | Real MULTs |
|---|---|---|
| Direct DFT | $N^2 = 4096$ | $4\cdot N^2 = $ **$16384$** |
| $N$-pt FFT | $(N/2)\cdot\log_2 N = 192$ | $2N\cdot\log_2 N = $ **$768$** |
| Real-input via $N/2$-pt complex FFT | — | $\log_2(N/2)\cdot N + 2N = $ **$448$** |

So for a 64-pt real signal: $16384$ vs. $768$ vs. $448$. Real-input trick wins by $\approx 35\%$ over standard FFT.

## The formulas

### Direct DFT
- $N^2$ complex MULTs
- $N(N-1)$ complex ADDs
- Real MULT count: **$4N^2$**

### Radix-2 FFT (complex input)
- $\log_2 N$ stages, $N/2$ butterflies per stage
- $(N/2)\cdot\log_2 N$ complex MULTs
- Real MULT count: **$2N\cdot\log_2 N$**

### Real-input FFT ($N$-pt real via $N/2$-pt complex FFT)
- $N/2$-pt FFT: $\log_2(N/2)\cdot N/4$ complex butterflies
- $N/2$ butterflies to extract $X_e, X_o$ from $Z$
- $N/2$ butterflies for final combine
- Real MULT count: **$\log_2(N/2)\cdot N + 2N$**

## Why it matters
This is the single biggest reason FFT exists. For large $N$ (speech, audio, images), the difference is literally **compute-in-minutes vs. compute-in-hours**. Every MC question about complexity in this course is arithmetic with these three formulas.

## The 5-minute speech example
From the slides: $5$ min of $8$ kHz speech $\to N = 2.4\cdot 10^6$. Direct DFT on a $168$ MHz DSP (1 instruction/cycle) at 4 MULTs per CMULT $\approx $ **$38$ hours**. With FFT: a few seconds. See [[dft-computation-burden]].

## Related
- [[dft]], [[fft]], [[real-valued-fft]]
- [[complex-multiplication]] — the "$1$ CMULT $= 4$ MULTs" identity

## Practice
- [[fft-fundamentals-set-01]] — complexity questions
