---
title: Conditional Expectation Identities (Formula)
type: formula
course: [[eee-350]]
tags: [conditional-expectation, iterated-expectations]
sources: [[slides-40-conditional-expectation]]
created: 2026-04-21
updated: 2026-04-26
---

# Conditional Expectation — Formula Sheet

## Tower rule (iterated expectations)

$$E[X] = E[E[X | Y]]$$

$$E[g(X)] = E[E[g(X) | Y]]$$

## Law of total variance

$$\text{Var}(X) = E[\text{Var}(X | Y)] + \text{Var}(E[X | Y])$$

## Bivariate Gaussian conditional (the one to memorize)

For jointly Gaussian $(X, Y)$ with correlation $\rho$:
$$E[X | Y = y] = \mu_X + \rho\,\frac{\sigma_X}{\sigma_Y}(y - \mu_Y)$$
$$\text{Var}(X | Y = y) = \sigma_X^2(1 - \rho^2)$$

Conditional variance doesn't depend on $y$ — unique to Gaussians.

## Random sum ($N$ random, $X_i$ i.i.d. with mean $\mu$, variance $\sigma^2$, and $N \perp$ all $X_i$)

$$E\!\left[\sum_{i=1}^N X_i\right] = E[N]\cdot\mu$$

$$\text{Var}\!\left(\sum_{i=1}^N X_i\right) = E[N]\cdot\sigma^2 + \mu^2\cdot\text{Var}(N)$$

## Compound Poisson ($N \sim \text{Poisson}(\lambda)$)

$$\text{Var}\!\left(\sum_{i=1}^N X_i\right) = \lambda\cdot E[X^2]$$

## Related
- [[conditional-expectation]]
- [[iterated-expectations]]
- [[conditional-variance]]
- [[law-of-total-variance]]
- [[bivariate-gaussian]]
- [[sum-of-random-number-of-rvs]]
