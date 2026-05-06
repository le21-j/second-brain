---
title: Random Vector
type: concept
course:
  - "[[eee-350]]"
tags: [multivariate, random-vector]
sources:
  - "[[slides-39-multivariate-vectors]]"
created: 2026-04-21
updated: 2026-05-06
---

# Random Vector

## In one line
A **random vector** is just a finite collection of RVs bundled together: $\mathbf{X} = (X_1, X_2, \ldots, X_n)$. Everything you know about joint distributions of pairs generalizes to $n$-tuples.

## Example first
Three-dimensional "measurement" random vector: (temp, pressure, humidity) at a weather station. Each component is a RV; together they have a **joint distribution**.

Joint PDF / PMF describes the probability of any region in $n$-space. Marginals (by integrating/summing out the others) give back individual components.

## The idea
- **Discrete:** joint PMF $p(x_1, \ldots, x_n) = P(X_1 = x_1, \ldots, X_n = x_n)$. Sum over $\mathbb{R}^n$ (well, over the support) is 1.
- **Continuous:** joint PDF $f(x_1, \ldots, x_n) \geq 0$, integrates to 1 over $\mathbb{R}^n$.
- **Marginal:** $f_{X_1}(x_1) = \int \cdots \int f(x_1, x_2, \ldots, x_n)\, dx_2 \ldots dx_n$.
- **Independence:** $X_1, \ldots, X_n$ are independent iff $f(x_1, \ldots, x_n) = f_{X_1}(x_1) \cdot \ldots \cdot f_{X_n}(x_n)$.

## Moments of a random vector
- **Mean vector:** $\boldsymbol\mu = (E[X_1], \ldots, E[X_n])$.
- **Covariance matrix:** $\Sigma$ where $\Sigma_{ij} = \text{Cov}(X_i, X_j) = E[(X_i - \mu_i)(X_j - \mu_j)]$.
  - Diagonal entries are variances.
  - Symmetric. Positive semidefinite.

## Linear transformations
If $\mathbf{Y} = A\mathbf{X} + \mathbf{b}$ ($A$ is $n \times m$, $\mathbf{b} \in \mathbb{R}^n$):
- $E[\mathbf{Y}] = A\boldsymbol\mu + \mathbf{b}$
- $\text{Cov}(\mathbf{Y}) = A\Sigma A^T$

These identities are the backbone of Gaussian-based estimation theory.

## Related
- [[iid-samples]] — special case: components i.i.d.
- [[multivariate-gaussian]] — the most important family
- [[covariance]] — entries of $\Sigma$

## Practice
- [[prob-fundamentals-set-01]]
