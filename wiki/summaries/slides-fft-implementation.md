---
title: Slides — FFT Implementation
type: summary
source_type: slides
source_path: raw/slides/eee-404/fft_implementation.pdf
course: [[eee-404]]
tags: [fft, implementation, butterfly, scaling, embedded]
created: 2026-04-21
updated: 2026-04-26
---

# Slides — FFT Implementation

## TL;DR
The concrete "how to code an FFT" slides. Three nested loops: **stage $L$**, **butterfly index $j$**, **butterfly pair $i$**. Each stage's sub-DFT size is $D = 2^L$, with $B = D/2$ butterflies. Precompute $\log_2 N$ twiddle factors $W = [W_N^{N/4}, W_N^{N/8}, \ldots, W_N^1]$; update $U$ in place inside the $j$ loop. Finishes with overflow prevention: scale each stage output by 0.5, multiply final result by $N$ to recover.

## Key takeaways
- Loops:
  ```
  for L = 1 .. log2(N):                 // stage
      D = 1 << L;   B = D >> 1;
      U = 1 + 0j;                       // reset twiddle
      for j = 0 .. B-1:                 // butterfly index within sub-DFT
          for i = j; i < N; i += D:     // butterfly pairs across N
              k = i + B;
              temp = U * X[k];
              P = X[i] + temp;          // possibly * 0.5
              Q = X[i] - temp;          // possibly * 0.5
              X[i] = P;  X[k] = Q;
          U = U * W[L-1];               // advance twiddle
  ```
- **Twiddle table layout:** $W[L-1] = W_N^{N/D}$ so $W[0] = W_N^{N/2} = -1$ (kind of; actually $W$ for stage 1 has $D=2$ so we reset; carefully: $W[L-1] = e^{-j\cdot\pi/B}$, i.e. $\cos(\pi/B) - j\cdot\sin(\pi/B)$).
- **Overflow risk:** $P = X[i] + U\cdot X[k]$ can grow. Preventive fix: scale both $P$ and $Q$ by 0.5 per stage. After all $\log_2 N$ stages, overall scale is $1/N$ — multiply output by $N$ to get correct DFT.
- **Complex multiply:** $\text{temp.re} = U_{\text{re}}\cdot X[k]_{\text{re}} - U_{\text{im}}\cdot X[k]_{\text{im}}$; $\text{temp.im} = U_{\text{re}}\cdot X[k]_{\text{im}} + U_{\text{im}}\cdot X[k]_{\text{re}}$.

## Concepts introduced or reinforced
- [[butterfly]] — inner equations
- [[twiddle-factor]] — precomputed table `W[]`
- [[fft-scaling]] — per-stage 0.5 to prevent overflow
- [[complex-multiplication]] — the four-multiply-two-add identity

## Worked examples worth remembering
- $N=8$ trace: $D$ goes $2 \to 4 \to 8$, $B$ goes $1 \to 2 \to 4$ across stages. Walk through the twiddle updates in [[butterfly]].

## Questions this source raised
- 1024-point FFT question: if scaling 0.5 every stage, recover by multiplying by **1024** ($= 2^{10}$). Pattern: multiply by $N$ to undo.
