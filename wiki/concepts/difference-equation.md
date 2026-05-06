---
title: Difference Equation
type: concept
course:
  - "[[eee-404]]"
tags: [difference-equation, lti-system, dsp, eee-404]
sources:
  - "[[summary-eee-404-m8-difference-equation]]"
created: 2026-04-29
updated: 2026-05-06
---

# Difference Equation

## In one line
A **difference equation** describes a discrete-time LTI system in the time domain: $y[n]$ as a linear combination of past inputs $x[n-k]$ and past outputs $y[n-k]$.

## Example first

$$y[n] = x[n] + 3 x[n-1] - \tfrac{3}{10} y[n-1] + \tfrac{1}{10} y[n-2]$$

This is Exam 2 Problem 2(b). Reading it left-to-right:

- Current output $y[n]$ depends on current input $x[n]$, the input one step ago $x[n-1]$ (with weight 3), and the **past two outputs** $y[n-1], y[n-2]$ (the **feedback** terms).
- The feedback makes it an **IIR** system — see [[fir-vs-iir]].

## The idea

The difference equation is the time-domain twin of $H(z)$. They are interconvertible:
- **From $H(z)$ to difference equation:** cross-multiply $H(z) = Y(z)/X(z)$, then apply the time-shift property $z^{-l} \leftrightarrow x[n-l]$ to each term.
- **From difference equation to $H(z)$:** Z-transform both sides, solve for $Y(z)/X(z)$.

The difference equation is what you actually **implement on hardware** (or in code) — it's a recursive update rule.

## Formal definition

**Standard form** (with $a_0 = 1$):
$$\sum_{k=0}^{N} a_k\,y[n - k] = \sum_{k=0}^{M} b_k\,x[n - k]$$

**Solved for $y[n]$:**
$$y[n] = \sum_{k=0}^{M} b_k\,x[n - k] - \sum_{k=1}^{N} a_k\,y[n - k]$$

**Corresponding transfer function:**
$$H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_{k=0}^{M} b_k z^{-k}}{1 + \sum_{k=1}^{N} a_k z^{-k}}$$

**$M$ = order of the FIR (numerator) part. $N$ = order of the IIR (denominator) part.**

## Why it matters / when you use it

- **Exam 2 Problem 2(b)** — given $H(z)$, derive the difference equation.
- **Implementation.** When you write a real-time filter on the STM32, you literally code the difference equation in a loop.
- **Calculate the impulse response** $h[n]$ by setting $x[n] = \delta[n]$ and iterating. (Easier than inverse Z-transform for short responses.)
- **Calculate the output** for a specific input by direct iteration.

## How to derive the difference equation from $H(z)$ (template)

1. **Write $H(z) = Y(z)/X(z)$.**
2. **Cross-multiply** so all $Y(z)$ are on LHS, all $X(z)$ on RHS.
3. **Apply $z^{-l} X(z) \leftrightarrow x[n-l]$** to each term.
4. **Solve for $y[n]$** (move feedback terms to RHS — flip their sign).

**Worked:** $H(z) = \dfrac{1 + 3 z^{-1}}{1 + \tfrac{3}{10} z^{-1} - \tfrac{1}{10} z^{-2}}$
- Cross-multiply: $\bigl(1 + \tfrac{3}{10} z^{-1} - \tfrac{1}{10} z^{-2}\bigr) Y(z) = \bigl(1 + 3 z^{-1}\bigr) X(z)$
- Time-shift: $y[n] + \tfrac{3}{10} y[n-1] - \tfrac{1}{10} y[n-2] = x[n] + 3 x[n-1]$
- Solve: $y[n] = x[n] + 3 x[n-1] - \tfrac{3}{10} y[n-1] + \tfrac{1}{10} y[n-2]$ ✓

## Common mistakes

- **Sign errors when moving feedback to RHS.** $+\tfrac{3}{10} y[n-1]$ on LHS becomes $-\tfrac{3}{10} y[n-1]$ on RHS.
- **Mixing up which side gets $X$ vs $Y$.** $H(z) = Y/X$ → numerator multiplies $X$, denominator multiplies $Y$.
- **Forgetting $a_0 = 1$ convention.** If $a_0 \neq 1$, divide everything by $a_0$ to normalise.

## Related

- [[z-transform]] — the freq-domain twin
- [[fir-vs-iir]] — classify by inspecting the equation
- [[direct-form-i]], [[direct-form-ii]] — block-diagram realisations of the equation
- [[eee-404-exam-2-walkthrough]] — Problem 2(b)

## Practice
- Exam 2 Practice Problem 2(b)
