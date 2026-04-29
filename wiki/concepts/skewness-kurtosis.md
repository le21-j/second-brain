---
title: Skewness and Kurtosis
type: concept
course: [[eee-350]]
tags: [moments, skewness, kurtosis]
sources: [[slides-46.5-descriptive-stats]]
created: 2026-04-21
updated: 2026-04-26
---

# Skewness and Kurtosis

## In one line
Standardized **higher-order** moments that describe distribution shape beyond mean and variance.

## Skewness — asymmetry

$$\text{Skew}(X) = E\!\left[\left(\frac{X - \mu}{\sigma}\right)^3\right]$$

- **Skew $= 0$:** symmetric (e.g. Gaussian, Uniform).
- **Skew $> 0$:** right-tailed (tail extends to right; e.g. Exponential, Log-Normal, income distributions).
- **Skew $< 0$:** left-tailed.

## Kurtosis — tail heaviness

$$\text{Kurt}(X) = E\!\left[\left(\frac{X - \mu}{\sigma}\right)^4\right]$$

- **Gaussian: Kurt $= 3$.** Reference point.
- **Excess kurtosis:** $\text{Kurt} - 3$. $> 0$ means heavier tails than Gaussian; $< 0$ means lighter tails.
- **Uniform:** $\text{Kurt} = 1.8$ (light-tailed).
- **Exponential:** $\text{Kurt} = 9$ (heavy tails).
- **Cauchy:** $\text{Kurt} = \infty$ (no 4th moment).

Financial returns typically have excess kurtosis (fat tails) — reason why Gaussian-based risk models understate rare losses.

## Sample versions
Just replace $\mu, \sigma$ with $\bar x, s$, and expectations with sample averages.

## Related
- [[sample-mean]], [[sample-variance]]
- [[central-limit-theorem]] — sum of $n$ i.i.d. approaches Gaussian kurtosis $\approx 3$ for large $n$ (even if components are skewed/kurtotic)
