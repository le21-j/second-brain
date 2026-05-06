---
title: Direct Form II
type: concept
course:
  - "[[eee-404]]"
tags: [direct-form, block-diagram, filter-implementation, dsp, eee-404]
sources:
  - "[[summary-eee-404-m7-frequency-domain]]"
created: 2026-04-29
updated: 2026-05-06
---

# Direct Form II (DF-II)

## In one line
A clever rearrangement of [[direct-form-i]] that uses **a single shared delay line** of length $\max(M, N)$ — the minimum possible for a rational $H(z)$ with $M$ feedforward and $N$ feedback taps.

## Example first

For $H(z) = \dfrac{1 + 3 z^{-1}}{1 + \tfrac{3}{10} z^{-1} - \tfrac{1}{10} z^{-2}}$ (the Exam 2 system, $M = 1$, $N = 2$, $\max(M, N) = 2$):

```
 x[n] ──►(+)────────●──►(+)──► y[n]
          ▲          │    ▲
          │         [z⁻¹] │
          │          │    │
          │·(−3/10)──●·1──┤
          │          │    │
          │         [z⁻¹] │·3
          │          │    │
          │·(+1/10)──●────┘
          │          │
          (these feed back to the +)
```

The single chain $w[n], w[n-1], w[n-2]$ holds an **intermediate signal** $w[n] = x[n] - \tfrac{3}{10} w[n-1] + \tfrac{1}{10} w[n-2]$ (the IIR section); the output is $y[n] = w[n] + 3 w[n-1]$ (the FIR section reading from the same chain).

## The idea

**Swap the order** of the two sections in DF-I (do the all-pole IIR first, then the all-zero FIR). After the swap, both sections are reading from the **same intermediate signal** $w[n]$ — so the two delay lines collapse into one. Total storage: $\max(M, N)$.

## Formal definition

DF-I: $H(z) = B(z) \cdot \dfrac{1}{A(z)}$ — first apply $B(z)$, then $1/A(z)$.

DF-II: $H(z) = \dfrac{1}{A(z)} \cdot B(z)$ — first apply $1/A(z)$, then $B(z)$. (LTI cascade is commutative — the answer is the same.)

After the swap, both sections share the intermediate signal $w[n]$:
$$w[n] = x[n] - \sum_{k=1}^{N} a_k w[n - k]$$
$$y[n] = \sum_{k=0}^{M} b_k w[n - k]$$

Total delay elements: $\max(M, N)$.

## Why it matters / when you use it

- **Memory-optimal** — uses the theoretical minimum number of delays for a rational $H(z)$.
- **Exam 2 Problem 2(d)** asks for the DF-II diagram with storage element count.
- **Standard form** for shipped DSP code — `biquad` library functions are usually DF-II implementations.
- **Sketching trick:** see the [study guide](../walkthroughs/eee-404-exam-2-study-guide.md) for the 30-second DF-II drawing recipe.

## How to draw DF-II from a difference equation in 30 seconds

1. Take the difference equation in standard form: $y[n] = \sum b_k x[n-k] - \sum a_k y[n-k]$.
2. Draw a **single vertical delay chain** of length $\max(M, N)$ on the left (each box = $z^{-1}$). Top of chain = $w[n]$; below it $w[n-1]$, $w[n-2]$, ...
3. **Top summing junction** receives $x[n]$ + (each delay node $\times -a_k$). Output of this junction = $w[n]$ → top of delay chain.
4. **Right summing junction** receives each delay node $\times +b_k$ → output = $y[n]$.
5. Done.

## Common mistakes

- **Counting delays as $M + N$** — that's DF-I. DF-II uses $\max(M, N)$.
- **Forgetting the sign flip on feedback** — feedback taps are $\times (-a_k)$, not $\times (+a_k)$.
- **Drawing two delay lines** — that's still DF-I in disguise.
- **Confusing DF-II with Transposed DF-II** — they have the same delay count but the arrows are reversed.

## Comparison

| Form | Storage elements |
|---|---|
| Direct Form I | $M + N$ |
| **Direct Form II** | $\max(M, N)$ ← **the minimum** |
| Transposed DF-II | $\max(M, N)$ |
| Cascade | $\sum 2$ per biquad |
| Parallel | $\sum 2$ per biquad |

## Related

- [[direct-form-i]] — the literal version with $M + N$ delays
- [[difference-equation]] — what gets realised
- [[z-transform]] — where $H(z)$ comes from
- [[fir-vs-iir]] — IIR systems benefit most from DF-II
- [[eee-404-exam-2-walkthrough]] — Problem 2(d) full DF-II walkthrough

## Practice
- Exam 2 Practice Problem 2(d)
