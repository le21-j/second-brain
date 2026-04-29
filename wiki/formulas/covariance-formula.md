---
title: Covariance / Correlation (Formula)
type: formula
course: [[eee-350]]
tags: [covariance, correlation, moments]
sources: [[slides-38-covariance]]
created: 2026-04-21
updated: 2026-04-26
---

# Covariance & Correlation — Formula Sheet

## Definitions

$$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - \mu_X\mu_Y$$

$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X\,\sigma_Y} \in [-1, +1]$$

## Bilinearity

$$\text{Cov}(aX + bY, Z) = a\cdot\text{Cov}(X, Z) + b\cdot\text{Cov}(Y, Z)$$

## Variance of sum

$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X, Y)$$

$$\text{Var}(aX + bY) = a^2\text{Var}(X) + b^2\text{Var}(Y) + 2ab\,\text{Cov}(X, Y)$$

## Sample versions

$$\hat\sigma_{XY}^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar x)(y_i - \bar y)$$

$$\hat\rho = \frac{\hat\sigma_{XY}^2}{\hat\sigma_X\hat\sigma_Y}$$

## Key facts

- $X \perp Y \Rightarrow \text{Cov} = 0$ (converse false in general).
- Jointly Gaussian: $\text{Cov} = 0 \iff X \perp Y$.
- $\text{Cov}(X, X) = \text{Var}(X)$.

## Related
- [[covariance]]
- [[correlation-coefficient]]
- [[variance-of-a-sum]]
