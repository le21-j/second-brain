---
title: LMS / MMSE Estimation
type: concept
course: [[eee-350]]
tags: [bayesian, estimation, lms, mmse]
sources: [[slides-43.5-bayesian-inference]], [[homework-2026-04-23-eee-350-hw7]]
created: 2026-04-21
updated: 2026-04-26
---

# LMS / MMSE Estimation (Least Mean Squares)

## In one line
**$\hat\theta = E[\theta \mid X]$** is the estimator that **minimizes the mean squared error** $E[(\theta - \hat\theta(X))^2]$. Also called MMSE (Minimum Mean Square Error).

## Naming (heads up — three things, different conventions)

| This page / Wiley / MIT 6.041 | HW7 / modern textbooks | What it is |
|---|---|---|
| **LMS** (Least Mean Squares) | **MMSE** (Minimum MSE) | $E[Y \mid X]$ — unrestricted |
| **LLS** (Linear Least Squares) — see below | **LMSE** (Linear MMSE) — see [[linear-mmse-estimation]] | $aX + b$ — linear-restricted |

Same two estimators, different abbreviations depending on which book you open. Both conventions are fine — just know which one you're in.

## Example first
$(\theta, X)$ are jointly Gaussian with $\theta \sim N(\mu_\theta, \sigma_\theta^2)$, $X \sim N(\mu_X, \sigma_X^2)$, correlation $\rho$. The LMS estimator:
$$\hat\theta_{LMS}(X) = E[\theta | X] = \mu_\theta + \rho\,\frac{\sigma_\theta}{\sigma_X}(X - \mu_X)$$

Linear in $X$! This is the regression line. For jointly Gaussian, LMS is **both linear and equal to MAP**.

MSE of this estimator = $\sigma_\theta^2\cdot(1 - \rho^2)$ — the conditional variance. Shrinks with $|\rho|$.

## The theorem

**Orthogonality principle / tower rule proof:** For any estimator $g(X)$,
$$E[(\theta - g(X))^2] = E[\text{Var}(\theta | X)] + E[(E[\theta | X] - g(X))^2]$$
The first term is fixed (can't be reduced). The second term is minimized when $g(X) = E[\theta \mid X]$. QED.

So **$g^*(X) = E[\theta \mid X]$ minimizes MSE** — no other function of $X$ does better on mean-squared-error terms.

## Minimum MSE achieved
$$\text{MSE}^* = E[\text{Var}(\theta | X)]$$

This is the "unavoidable" error — the part of $\theta$'s variance that $X$ can't explain. See [[law-of-total-variance]].

## LLS / LMSE (Linear Least Squares) — the simpler cousin
If you restrict estimators to **linear** functions $g(X) = aX + b$ (even when $E[\theta \mid X]$ isn't linear), the best such estimator is:
$$\hat\theta_{LLS}(X) = E[\theta] + \frac{\text{Cov}(\theta, X)}{\text{Var}(X)}(X - E[X])$$

**For jointly Gaussian:** LMS = LLS (both are linear). For other distributions: LLS is the best **linear** estimator but not the overall best.

See [[linear-mmse-estimation]] for the full treatment (HW7-compatible naming: LMSE), including the projection view and minimum MSE formula $e_L^* = \text{Var}(Y)(1 - \rho^2)$.

## Why LMS is THE default
- Squared error is a natural loss (penalizes big mistakes more).
- The solution $E[\theta \mid X]$ is elegant.
- In Gaussian settings (common!), it's linear and computable.
- Has Kalman-filter, Wiener-filter, LMS-adaptive-filter all as special cases.

## Common mistakes
- Confusing LMS (conditional mean) with MAP (mode). They coincide for symmetric unimodal posteriors, not always.
- Using LMS when an absolute-error criterion is more appropriate (e.g., robust estimation in presence of outliers — median is better there).

## Related
- [[bayesian-inference]]
- [[conditional-expectation]]
- [[law-of-total-variance]]
- [[map-estimation]]
- [[linear-regression]] — the frequentist version of LLS
- [[linear-mmse-estimation]] — the LLS case, worked out at HW7 depth (LMSE naming)

## Examples
- [[mmse-vs-lmse-erlang]] — HW7 12.2.6: MMSE and LMSE of X|Y and Y|X when X is Erlang, Y|X uniform; both conditional means are linear so MMSE = LMSE
- [[map-detection-antipodal]] — related inference example
