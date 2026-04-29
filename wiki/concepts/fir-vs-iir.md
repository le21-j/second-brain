---
title: FIR vs IIR
type: concept
course: [[eee-404]]
tags: [fir, iir, filter, lti-system, dsp, eee-404]
sources: [[summary-eee-404-m8-difference-equation]]
created: 2026-04-29
updated: 2026-04-29
---

# FIR vs IIR

## In one line
**FIR** (Finite Impulse Response) filters have no feedback — output depends only on inputs. **IIR** (Infinite Impulse Response) filters have feedback — output depends on past outputs too.

## Example first

**FIR (3-tap moving average):**
$$y[n] = \tfrac{1}{3}\bigl(x[n] + x[n-1] + x[n-2]\bigr) \quad\Rightarrow\quad H(z) = \tfrac{1}{3}(1 + z^{-1} + z^{-2})$$
Denominator is constant ($1$). Impulse response $h[n] = \{1/3, 1/3, 1/3, 0, 0, \dots\}$ — finite. ✓ FIR.

**IIR (1st-order leaky integrator):**
$$y[n] = x[n] + 0.9\,y[n-1] \quad\Rightarrow\quad H(z) = \frac{1}{1 - 0.9 z^{-1}}$$
Denominator has $z^{-1}$ term → feedback. Impulse response $h[n] = (0.9)^n u[n]$ — infinite. ✓ IIR.

## The idea

A 30-second test:

> **Look at the denominator of $H(z)$ (or look for $y[n-k]$ terms in the difference equation).**
> - If the denominator is a constant (or there are no $y[n-k]$ terms), it's **FIR**.
> - If the denominator has any $z^{-k}$ for $k \geq 1$, it's **IIR**.

## Formal definition

| | FIR | IIR |
|---|---|---|
| Difference equation | $y[n] = \sum_{k=0}^M b_k x[n-k]$ | $y[n] = \sum_{k=0}^M b_k x[n-k] - \sum_{k=1}^N a_k y[n-k]$ |
| Transfer function $H(z)$ | $\sum_{k=0}^M b_k z^{-k}$ (polynomial) | $\dfrac{\sum b_k z^{-k}}{1 + \sum a_k z^{-k}}$ (rational) |
| Impulse response $h[n]$ | finite length $M+1$ | infinite length |
| Poles | only at $z = 0$ | nonzero poles |
| Stability | always stable (no poles outside circle) | stable iff all poles inside unit circle |
| Implementation cost | high # taps for sharp cutoff | low # taps for sharp cutoff |
| Phase response | can be exactly linear | generally nonlinear |

## Why it matters / when you use it

- **Exam 2 Problem 2(c):** "FIR or IIR? Why?" — the easy classifier above.
- **Choice in real-time DSP:** IIR is computationally cheaper for the same selectivity, but FIR is unconditionally stable and can have linear phase (no group delay distortion).
- **STM32 / embedded:** FIR is straightforward; IIR needs careful fixed-point coefficient quantisation to stay stable.

## Common mistakes

- **Reading FIR/IIR off the numerator.** Numerator structure matters for zeros, not for FIR/IIR. **Look at the denominator.**
- **Saying "no $z^{-1}$ term anywhere = FIR".** Wrong — there can be $z^{-1}, z^{-2}, \dots$ in the numerator and it's still FIR.
- **Saying "$y[n-1]$ term in equation = FIR".** Backwards — that's a feedback term, so it's IIR.

## Related

- [[difference-equation]] — the time-domain form
- [[z-transform]], [[region-of-convergence]] — the freq-domain side
- [[direct-form-i]], [[direct-form-ii]] — both forms work for FIR or IIR
- [[eee-404-exam-2-walkthrough]] — Problem 2(c)

## Practice
- Exam 2 Practice Problem 2(c)
