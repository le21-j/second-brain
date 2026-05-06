---
title: Z-Transform
type: concept
course:
  - "[[eee-404]]"
tags: [z-transform, discrete-time, lti-system, transfer-function, dsp, eee-404]
sources:
  - "[[summary-eee-404-m7-frequency-domain]]"
created: 2026-04-29
updated: 2026-05-06
---

# Z-Transform

## In one line
The **Z-transform** maps a discrete-time signal $x[n]$ to a function of a complex variable $z$, generalising the [[dtft]] (which is the Z-transform restricted to the unit circle $|z| = 1$).

## Example first

Take the unit pulse $x[n] = a^n u[n]$ (geometric sequence, $|a| < 1$):
$$X(z) = \sum_{n=0}^{\infty} a^n z^{-n} = \sum_{n=0}^{\infty} (a z^{-1})^n = \frac{1}{1 - a z^{-1}}$$

This converges only when $|a z^{-1}| < 1$, i.e. $|z| > |a|$. So the **ROC** (region of convergence) is $\{|z| > |a|\}$.

For $a = 0.5$: $X(z) = 1 / (1 - 0.5 z^{-1})$, ROC $|z| > 0.5$. The single pole sits at $z = 0.5$ inside the unit circle, so the DTFT exists and the system is causal+stable.

## The idea

The Z-transform replaces $e^{j\omega}$ in the DTFT with a free complex variable $z$, generalising "frequency" to a 2D complex plane. Most discrete-time LTI systems can be cleanly described by a **rational** $H(z)$ — a ratio of polynomials in $z^{-1}$. The roots of the numerator are **zeros**; the roots of the denominator are **poles**. The pole-zero plot tells you everything about the system: stability, causality, frequency response, transient behavior.

## Formal definition

**Bilateral Z-transform:**
$$X(z) = \sum_{n=-\infty}^{\infty} x[n]\,z^{-n}$$

**Region of convergence (ROC):** the set of $z$ for which the sum converges. ROC is part of the answer — same $X(z)$ formula, different ROC, can mean different signals.

**Time-shift property** (the workhorse):
$$x[n - n_0]\ \xleftrightarrow{\mathcal{Z}}\ z^{-n_0} X(z)$$

This is what lets you go from $H(z)$ → difference equation. See [[difference-equation]].

**Convolution property:**
$$y[n] = h[n] * x[n]\ \xleftrightarrow{\mathcal{Z}}\ Y(z) = H(z) X(z)$$

**ROC rules:**
| Sequence type | ROC |
|---|---|
| Right-sided / causal | $\{|z| > r_{\max}\}$ — outside outermost pole |
| Left-sided / anti-causal | $\{|z| < r_{\min}\}$ — inside innermost pole |
| Two-sided | annulus between two pole rings |
| **DTFT exists** | ROC includes the unit circle $|z| = 1$ |
| **Causal AND stable** | all poles **strictly inside** the unit circle |

## Why it matters / when you use it

- **Transfer function** $H(z) = Y(z)/X(z)$ is the cleanest way to describe an LTI system.
- **Stability test** by inspecting pole locations.
- **Filter design** — pole-zero placement gives intuitive control over frequency response.
- **Going from $H(z) \leftrightarrow$ difference equation $\leftrightarrow$ block diagram** is THE Exam 2 Problem 2 skill.
- **Z-transform = discrete-time analog of the Laplace transform** (which generalises Fourier in continuous time).

## Common mistakes

- **Forgetting the ROC.** $X(z) = 1/(1 - 0.5 z^{-1})$ with ROC $|z| > 0.5$ is the causal $0.5^n u[n]$. With ROC $|z| < 0.5$ it's the anti-causal $-0.5^n u[-n-1]$. Same algebra, different signal.
- **Reading FIR/IIR off the numerator.** The denominator tells you FIR vs IIR. See [[fir-vs-iir]].
- **Mixing up "ROC includes unit circle" (DTFT exists) with "all poles inside unit circle" (causal+stable).** The first is necessary; the second is the additional condition for causal stable.
- **Sign error in time-shift.** $x[n-1] \leftrightarrow z^{-1} X(z)$ (negative exponent), not $z^{+1}$.

## Related

- [[dtft]] — restriction of Z-transform to $|z| = 1$
- [[region-of-convergence]] — the "where does it converge" detail
- [[difference-equation]] — get from $H(z)$ to time domain
- [[direct-form-i]], [[direct-form-ii]] — block-diagram realisations
- [[fir-vs-iir]] — quick classifier from $H(z)$
- [[eee-404-exam-2-walkthrough]] — Problem 2 walks through ROC, difference equation, DF-II for a 2nd-order IIR

## Practice
- Exam 2 Practice Problem 2
