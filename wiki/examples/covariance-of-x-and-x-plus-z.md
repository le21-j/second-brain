---
title: Example — Cov(X, X + Z) when X and Z are independent
type: example
course:
  - "[[eee-350]]"
tags: [covariance, bilinearity]
sources:
  - "[[slides-38-covariance]]"
created: 2026-04-21
updated: 2026-05-06
---

# Example — $\text{Cov}(X, X+Z)$ when $X$ and $Z$ are independent

## Problem
$X$ and $Z$ are independent random variables. Find $\text{Cov}(X, Y)$ where $Y = X + Z$.

## Approach 1 — bilinearity of covariance
$$\text{Cov}(X, Y) = \text{Cov}(X, X + Z) = \text{Cov}(X, X) + \text{Cov}(X, Z)$$

- $\text{Cov}(X, X) = \text{Var}(X)$ by definition.
- $\text{Cov}(X, Z) = 0$ by independence.

**So $\text{Cov}(X, Y) = \text{Var}(X)$.**

## Approach 2 — from definition
$$\text{Cov}(X, X + Z) = E[(X - \mu_X)(X + Z - \mu_X - \mu_Z)]$$

Expand:
$$= E[(X - \mu_X)^2] + E[(X - \mu_X)(Z - \mu_Z)] = \text{Var}(X) + \text{Cov}(X, Z)$$

Same answer.

## Intuition
$Y = X + Z$ moves with $X$ (by the $X$ term) and with an independent random kick $Z$. The **part of $Y$'s variation that's aligned with $X$** is just $X$'s own variation. That's $\text{Var}(X)$.

## Correlation coefficient
$$\rho_{XY} = \frac{\text{Var}(X)}{\sigma_X\cdot\sigma_Y}$$
- $\sigma_Y = \sqrt{\text{Var}(X) + \text{Var}(Z)}$ (since $X \perp Z$, variance of sum = sum of variances).
- So $\rho = \sigma_X / \sqrt{\sigma_X^2 + \sigma_Z^2}$.

**Limits:**
- $Z = 0$: $\rho = 1$ ($Y = X$ exactly).
- $\text{Var}(Z) \to \infty$: $\rho \to 0$ ($Y$ dominated by noise, loses connection to $X$).

## Related
- [[covariance]]
- [[correlation-coefficient]]
- [[variance-of-a-sum]]
