---
title: Direct Form I
type: concept
course:
  - "[[eee-404]]"
tags: [direct-form, block-diagram, filter-implementation, dsp, eee-404]
sources:
  - "[[summary-eee-404-m7-frequency-domain]]"
created: 2026-04-29
updated: 2026-05-06
---

# Direct Form I (DF-I)

## In one line
The most literal block-diagram realisation of a difference equation: a feedforward (zero) section followed by a feedback (pole) section, with **two separate delay lines** of lengths $M$ and $N$.

## Example first

For $y[n] = x[n] + 3 x[n-1] - \tfrac{3}{10} y[n-1] + \tfrac{1}{10} y[n-2]$ (the Exam 2 system, $M = 1$, $N = 2$):

```
 x[n] ──●──────────►(+)─────┬──► y[n]
        │           ▲        │
       [z⁻¹]        │       [z⁻¹]
        │           │        │
        │·3        ─┤       y[n−1]
        │           │        │
        ▼           │       (×−3/10)─→
       (+)──────────┘        │
                            [z⁻¹]
                             │
                            y[n−2]
                             │
                           (×+1/10)─→
```

(Read: input goes through a length-$M$ delay line summed with weights $b_k$ to produce an intermediate signal; that intermediate sum then goes through a length-$N$ delay line whose past outputs are summed back with weights $-a_k$.)

## The idea

Two delay lines, two summing junctions.

1. **Feedforward section (FIR):** delay $x$ a max of $M$ times, sum with weights $b_0, b_1, \dots, b_M$ to make $\sum b_k x[n-k]$.
2. **Feedback section (IIR):** take the running output, delay it a max of $N$ times, sum with weights $-a_1, -a_2, \dots, -a_N$ and **add to the feedforward result** to make $y[n]$.

Total delay elements: $M + N$.

## Formal definition

For $H(z) = \dfrac{B(z)}{A(z)} = \dfrac{\sum b_k z^{-k}}{1 + \sum a_k z^{-k}}$, DF-I is the cascade:
$$x[n] \xrightarrow{B(z)\text{ section}} v[n] \xrightarrow{1/A(z)\text{ section}} y[n]$$

The intermediate signal $v[n] = \sum b_k x[n-k]$ is computed first; then $y[n] = v[n] - \sum a_k y[n-k]$.

## Why it matters / when you use it

- **Most intuitive** — directly mirrors the difference equation.
- **Easy to code** — explicit delay buffers for $x$ and $y$.
- **Drawback:** uses $M + N$ storage elements, more than necessary. Use [[direct-form-ii]] when memory matters.
- **Better numerical behavior than DF-II** for some fixed-point cases — the intermediate signal $v[n]$ has the same dynamic range as $x[n]$ scaled by $\sum |b_k|$.

## Comparison vs other forms

| Form | Storage elements | Notes |
|---|---|---|
| **Direct Form I** | $M + N$ | Two delay lines |
| **Direct Form II** | $\max(M, N)$ | Shared delay line — saves memory |
| **Transposed DF-II** | $\max(M, N)$ | Reverses DF-II arrows; often better numerics |
| **Cascade** | $\sum 2$ per biquad | Series of 2nd-order sections |
| **Parallel** | $\sum 2$ per biquad | Sum of 2nd-order sections |

## Common mistakes

- **Forgetting the sign flip on feedback.** Difference equation has $- a_k y[n-k]$ on RHS → diagram has $\times (-a_k)$ on the feedback taps.
- **Drawing only one delay line** — that's DF-II, not DF-I.
- **Counting delays as $M$ or $N$** — they're $M + N$ for DF-I.

## Related

- [[direct-form-ii]] — the memory-efficient alternative
- [[difference-equation]] — what gets implemented
- [[fir-vs-iir]] — which sections you need
- [[eee-404-exam-2-walkthrough]] — Problem 2(d) sketches DF-I and DF-II for the same system

## Practice
- Exam 2 Practice Problem 2(d)
