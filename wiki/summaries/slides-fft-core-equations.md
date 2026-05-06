---
title: Slides — FFT Core Equations
type: summary
source_type: slides
source_path: raw/slides/eee-404/fft_core_equations.pdf
course:
  - "[[eee-404]]"
tags: [fft, dft, dit, derivation]
created: 2026-04-21
updated: 2026-05-06
---

# Slides — FFT Core Equations

## TL;DR
Derives the Decimation-In-Time FFT from the DFT by splitting $x[n]$ into even and odd subsequences. Motivation: direct DFT is $O(N^2)$ — 5 minutes of speech at 8 kHz would take ~38 hours on a 168 MHz DSP. FFT drops this to $O(N \log_2 N)$. Ends with the two core butterfly equations that every later slide references.

## Key takeaways
- DFT: $X[k] = \sum x[n]\cdot W_N^{kn}$, $W_N = e^{-j2\pi/N}$ is the **twiddle factor**.
- Direct DFT cost: $N^2$ complex multiplies, $N(N-1)$ complex adds.
- FFT = same DFT, faster. Requires $N = 2^\nu$ (radix 2).
- **DIT** splits $x[n]$ into even ($x[2m]$) and odd ($x[2m+1]$) subsequences $\to$ two $N/2$-point DFTs, glued by a butterfly.
- **Periodicity trick:** $X_e[k+N/2]=X_e[k]$, $X_o[k+N/2]=X_o[k]$, $W_N^{k+N/2} = -W_N^k$.
- Recurse $\log_2 N$ times until each sub-DFT has one sample.

## Concepts introduced or reinforced
- [[dft]] — the starting definition
- [[fft]] — what DIT FFT is at a high level
- [[twiddle-factor]] — $W_N^k$
- [[decimation-in-time]] — even/odd split algorithm
- [[butterfly]] — the atomic op
- [[dft-computation-complexity]] — counting multiplies

## Worked examples worth remembering
- **5-min speech at 8 kHz:** $N = 2.4\cdot 10^6$. Direct DFT $\approx$ 38 hours. See [[dft-computation-burden]].

## Questions this source raised
- What does DIF (Decimation In Frequency) look like? Slides flag it but don't cover it here.
