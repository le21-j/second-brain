---
title: Least Squares
type: concept
course:
  - "[[eee-350]]"
tags: [regression, optimization, ls]
sources:
  - "[[slides-46-regression]]"
created: 2026-04-21
updated: 2026-05-06
---

# Least Squares

## In one line
Minimize the **sum of squared residuals** $\sum (y_i - \hat y_i)^2$ — the most common curve-fitting criterion.

## Why squared?
Three reasons:
1. **Differentiable** — leads to closed-form normal equations.
2. **Probabilistic:** MLE for Gaussian noise. See [[maximum-likelihood-estimation]].
3. **Geometric:** squared residual = Euclidean distance$^2$ from data to model. Minimizing = projecting onto model space.

## What it's not good for
- Very non-Gaussian noise.
- Data with outliers (a single bad point can dominate via squaring).
- Heavy-tailed residuals (use robust methods).

Alternatives: least **absolute** deviations (median regression, Laplace noise), Huber loss (hybrid), quantile regression.

## Weighted least squares
When errors have different variances: minimize $\sum (y_i - \hat y_i)^2 / \sigma_i^2$. Weights each residual by its expected noise level.

## Related
- [[linear-regression]]
- [[maximum-likelihood-estimation]]
- [[power-law-regression]] (LS on log-log)
