---
title: Example — MLE for Exponential Rate
type: example
course: [[eee-350]]
tags: [mle, exponential, example]
sources: [[slides-44-mle-ci]]
created: 2026-04-21
updated: 2026-04-26
---

# Example — MLE of Exponential Rate $\lambda$

## Problem
You observe $n$ i.i.d. samples $X_1, \dots, X_n$ from $\text{Exp}(\lambda)$ — the Exponential distribution with rate parameter $\lambda$. Find the MLE of $\lambda$.

## Setup
PDF of $\text{Exp}(\lambda)$: $f(x; \lambda) = \lambda\, e^{-\lambda x}$ for $x \geq 0$.

Likelihood:
$$L(\lambda) = \prod_{i=1}^n \lambda\, e^{-\lambda x_i} = \lambda^n \exp\!\left(-\lambda\sum x_i\right)$$

## Log-likelihood
$$\ell(\lambda) = n\log\lambda - \lambda\sum_{i=1}^n x_i$$

## Differentiate
$$\frac{d\ell}{d\lambda} = \frac{n}{\lambda} - \sum x_i = 0 \implies \lambda = \frac{n}{\sum x_i} = \frac{1}{\bar x}$$

**MLE: $\hat\lambda = 1/\bar x$.**

## Check it's a maximum
$$\frac{d^2\ell}{d\lambda^2} = -\frac{n}{\lambda^2} < 0 \quad \text{always}$$
Concave $\to$ critical point is a global max. Good.

## Sanity check
- As $\lambda \to 0$: $e^{-\lambda x} \to 1$, $\lambda\cdot e^{-\lambda x} \to 0$. $L \to 0$.
- As $\lambda \to \infty$: pushes mass to $x = 0$, so for $x_i > 0$, $f$ drops to $0$. $L \to 0$.
- So $L$ is maximized at an interior point — namely $\hat\lambda = n/\sum x_i$.

## Small-sample behavior
- Is $\hat\lambda = 1/\bar x$ unbiased? **No.**
  - $\bar X_n$ is unbiased for $E[X] = 1/\lambda$.
  - But $1/\bar X_n$ is **not** unbiased for $\lambda$ — by Jensen's inequality, $E[1/\bar X] > 1/E[\bar X] = \lambda$. So $\hat\lambda$ is biased **high**.
- Is it consistent? **Yes.** By LLN, $\bar X \to 1/\lambda$ in probability, so $1/\bar X \to \lambda$.

## Numerical example
Observations: $[0.5, 1.2, 2.8, 0.7, 1.5]$. Sum $= 6.7$. $\bar x = 1.34$.

$\hat\lambda = 1/1.34 \approx \mathbf{0.746}$.

Expected time between events: $1/\hat\lambda = 1.34$ (which is just $\bar x$, by construction).

## Related
- [[maximum-likelihood-estimation]]
- [[unbiased-estimator]]
- [[consistent-estimator]]
- [[poisson-process]] (interarrival times are Exp)
