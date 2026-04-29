---
title: Variance of a Sum
type: concept
course: [[eee-350]]
tags: [variance, covariance, moments]
sources: [[slides-38-covariance]]
created: 2026-04-21
updated: 2026-04-26
---

# Variance of a Sum

## In one line
$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) +$ **$2 \cdot \text{Cov}(X, Y)$**. The covariance term is the whole reason this isn't just "add the variances".

## Example first
Two fair 6-sided dice, independent. $X, Y$ each have $\text{Var} = 35/12$.
- **Independent sum:** $\text{Var}(X + Y) = 35/12 + 35/12 + 0 = 70/12$. $\checkmark$
- **Perfectly correlated sum ($Y = X$):** $\text{Var}(X + X) = \text{Var}(2X) = 4 \cdot \text{Var}(X) = 140/12$ — twice as big.
- **Perfectly anti-correlated ($Y = 7 - X$):** $\text{Var}(X + (7 - X)) = \text{Var}(7) = 0$ — sum is constant!

So the same "sum of two dice" has Var ranging from 0 to $140/12$ depending on the covariance.

## The idea
Variance is a **quadratic** functional, so expanding $(X + Y - \mu_X - \mu_Y)^2$ gives
$$\text{Var}(X + Y) = E[(X - \mu_X)^2] + E[(Y - \mu_Y)^2] + 2\,E[(X - \mu_X)(Y - \mu_Y)]$$
The first two terms are the individual variances; the third is **$2 \cdot \text{Cov}(X, Y)$**.

## Formula

$$\boxed{\,\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X, Y)\,}$$

## General n-term version

$$\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_i \text{Var}(X_i) + 2\sum_{i < j} \text{Cov}(X_i, X_j)$$

Or more symmetrically, with $\Sigma$ = covariance matrix of the random vector:
$$\text{Var}(\mathbf{1}^T \mathbf{X}) = \mathbf{1}^T \Sigma \mathbf{1}$$

## Weighted version
$$\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y) + 2ab\,\text{Cov}(X, Y)$$

## Why it matters
- **Sample mean variance:** $\text{Var}(\bar X_n) = \sigma^2/n$ **only when samples are independent**. Correlated samples $\Rightarrow$ the covariance terms don't vanish.
- **Portfolio variance:** a weighted sum of asset returns; covariances drive diversification.
- **Proof of WLLN:** needs $\text{Var}(\bar X_n) \to 0$, which uses the n-term formula above.

## Common mistakes
- **"Variance of sum = sum of variances."** Only if covariances are all zero (e.g. independent). Otherwise you need the cross terms.
- **Dropping the factor of 2** in front of the covariance. Easy to miss.
- For **$\text{Var}(X - Y)$** people sometimes write "$= \text{Var}(X) - \text{Var}(Y) + \ldots$". Wrong: $\text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y) - 2 \cdot \text{Cov}(X, Y)$. The minus is only on the covariance.

## Related
- [[covariance]]
- [[correlation-coefficient]]
- [[weak-law-of-large-numbers]] (uses n-term formula)
- [[sum-of-random-number-of-rvs]]

## Practice
- [[prob-fundamentals-set-01]]
