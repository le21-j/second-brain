---
title: Sample Covariance
type: concept
course: [[eee-350]]
tags: [sample-covariance, descriptive-statistics]
sources: [[slides-46.5-descriptive-stats]]
created: 2026-04-21
updated: 2026-04-26
---

# Sample Covariance

## In one line
$s_{XY} = (1/(n - 1)) \sum (x_i - \bar x)(y_i - \bar y)$ — unbiased estimator of $\text{Cov}(X, Y)$.

## Formula
$$s_{XY} = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar x)(y_i - \bar y)$$

Normalized by **sample standard deviations** gives sample correlation:
$$\hat\rho = \frac{s_{XY}}{s_X \cdot s_Y}$$

## Properties
- **Unbiased:** $E[s_{XY}] = \text{Cov}(X, Y)$.
- **Consistent** by LLN.
- **Used in [[linear-regression|regression]]:** $\hat a = s_{XY} / s_X^2$.

## Note
- $(n-1)$ denominator because we used sample means $\bar x$ and $\bar y$ — again, one degree of freedom "used" for each mean estimate. (It's $n-1$, not $n-2$, despite two means — interesting bookkeeping.)

## Related
- [[covariance]]
- [[correlation-coefficient]]
- [[sample-mean]], [[sample-variance]]
- [[linear-regression]]
