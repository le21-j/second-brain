---
title: EEE 404 Module 10 (FFT) — Butterfly Structure (slide deck summary, fill-in)
type: summary
source_type: slides
source_path: raw/slides/eee-404/m10-fft-2-butterfly-structure.pdf
source_date: 2026-04-29
course:
  - "[[eee-404]]"
tags: [eee-404, fft, butterfly, decimation-in-time, dit]
created: 2026-04-29
---

# EEE 404 Module 10 — FFT Butterfly Structure (fill-in)

**Source:** [`raw/slides/eee-404/m10-fft-2-butterfly-structure.pdf`](../../raw/slides/eee-404/m10-fft-2-butterfly-structure.pdf)

## TL;DR
Companion slide deck to the rest of Module 10 (which we already had). Walks through the **butterfly structure** of the radix-2 DIT FFT: how a single butterfly takes two inputs $X_e$ and $X_o$ with twiddle $W_N^k$ and produces two outputs $X_e + W_N^k X_o$ and $X_e - W_N^k X_o$. Shows how $N/2$ butterflies per stage × $\log_2 N$ stages = $\frac{N}{2} \log_2 N$ butterflies total.

## Key takeaways
- **One butterfly = 1 complex multiply + 2 complex adds** (subtraction is addition of negative).
- **Convert to real ops:** 1 complex mult = 4 real mults + 2 real adds.
- **Per stage:** $N/2$ butterflies; total $\log_2 N$ stages.
- **Stage $s$ (1-indexed) twiddles:** $W_N^k$ for $k = 0, 1, \dots, N/2^s - 1$. Stage 1 has only $W_N^0 = 1$ — those are "trivial" butterflies (no actual multiplication). Stage 2 introduces $W_N^{N/4} = -j$. Stage $\log_2 N$ uses all $N/2$ twiddles.
- **In-place computation:** since each butterfly only reads two values and writes two values back, the FFT can be done with no extra memory beyond the input array.

## Concepts introduced / reinforced
- [[butterfly]] — already exists; this slide deck is the canonical visual
- [[fft]], [[decimation-in-time]] — the parent algorithm
- [[twiddle-factor]] — the $W_N^k$ multipliers
- [[bit-reversed-order]] — DIT requires bit-reversed input

## Exam tie-in
**Exam 2 Practice Problem 4** asks you to draw a 4-pt butterfly flow graph from scratch and label every node. The walkthrough has the full diagram + labels.

## Questions raised
- DIF vs DIT? (DIT = decimation in time = split inputs by even/odd index. DIF = decimation in frequency = split outputs by even/odd index. Same complexity; mirror images.)
