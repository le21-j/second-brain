---
title: EEE 404 Module 8 — Difference Equation and Filter Implementation (slide deck summary)
type: summary
source_type: slides
source_path: raw/slides/eee-404/m8-difference-equation-filter-implementation.pdf
source_date: 2026-04-29
course: [[eee-404]]
tags: [eee-404, difference-equation, filter-implementation, fir, iir]
created: 2026-04-29
---

# EEE 404 Module 8 — Difference Equation and Filter Implementation

**Source:** [`raw/slides/eee-404/m8-difference-equation-filter-implementation.pdf`](../../raw/slides/eee-404/m8-difference-equation-filter-implementation.pdf)

## TL;DR
Brief module that picks up where the Module 7 block-diagram slides left off — focuses on practical computation: how to run a difference equation in real time on the STM32 (sample-by-sample loop, manage the delay buffer, choose between DF-I and DF-II), and the FIR-vs-IIR distinction.

## Key takeaways
- **FIR has no feedback** ($a_k = 0$ for $k \geq 1$); IIR has $a_k \neq 0$ → recursive. See [[fir-vs-iir]].
- **Implementation loop pseudocode** for $y[n] = \sum b_k x[n-k] - \sum a_k y[n-k]$:
  ```
  for each sample n:
      shift x_buffer right; x_buffer[0] = new_x;
      acc = 0
      for k in 0..M: acc += b[k] * x_buffer[k]
      for k in 1..N: acc -= a[k] * y_buffer[k]
      shift y_buffer right; y_buffer[0] = acc;
      output(acc)
  ```
- **DF-II** uses a single $w_buffer$ instead of separate $x_buffer$ and $y_buffer$.

## Concepts introduced / reinforced
- [[difference-equation]] — the time-domain form
- [[fir-vs-iir]] — the easy classifier
- [[direct-form-i]], [[direct-form-ii]] — the implementations

## Exam tie-in
**Exam 2 Practice Problem 2** asks for difference-equation derivation, FIR/IIR classification, and DF-II diagram for a 2nd-order IIR.

## Questions raised
- Does the practical implementation use circular buffers or linear shifts? (Answer: STM32 typically uses circular indexing for performance.)
