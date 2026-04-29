---
title: Multivariate Gaussian
type: concept
course: [[eee-350]]
tags: [gaussian, multivariate, covariance-matrix]
sources: [[slides-39-multivariate-vectors]]
created: 2026-04-21
updated: 2026-04-26
---

# Multivariate Gaussian

## In one line
The $n$-dimensional Gaussian — parameterized by a **mean vector** $\boldsymbol\mu \in \mathbb{R}^n$ and a **covariance matrix** $\Sigma \in \mathbb{R}^{n \times n}$.

## Example first
You model the height, weight, and age of an adult as a 3-variate Gaussian. Parameters:
- $\boldsymbol\mu = (170, 70, 35)$ — mean height cm, weight kg, age years.
- $\Sigma$ = $3 \times 3$ matrix with diagonals = variances, off-diagonals = covariances.

Sample from this $\to$ a random (height, weight, age) triple. Marginals are 1D Gaussian (each individually Gaussian with its own mean/variance). Pick any pair $\to$ get a 2D Gaussian. Condition on one variable $\to$ the remaining two-dim conditional is Gaussian with shifted mean and reduced covariance.

## The idea
A random vector $\mathbf{X} = (X_1, \ldots, X_n)$ is multivariate Gaussian if every **linear combination** of its components is (1D) Gaussian. Equivalently, its joint PDF has the shape below. It is completely characterized by its **mean vector** and **covariance matrix**.

## Formal PDF

$$f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}} \exp\!\left(-\tfrac{1}{2}(\mathbf{x} - \boldsymbol\mu)^T \Sigma^{-1} (\mathbf{x} - \boldsymbol\mu)\right)$$

- $\boldsymbol\mu \in \mathbb{R}^n$ is the mean vector (component $i = E[X_i]$).
- $\Sigma$ is the $n \times n$ covariance matrix: $\Sigma_{ij} = \text{Cov}(X_i, X_j)$. Symmetric, positive semidefinite.
- $|\Sigma|$ = determinant; $\Sigma^{-1}$ = inverse (needs $\Sigma$ invertible, i.e. positive *definite*).
- Quadratic form in the exponent $\to$ **elliptical level sets**.

## Key properties
- **Marginals are Gaussian.** Any subset of components is a multivariate Gaussian with the corresponding sub-mean-vector and sub-covariance-matrix.
- **Linear transformations stay Gaussian.** If $\mathbf{Y} = A\mathbf{X} + \mathbf{b}$, then $\mathbf{Y} \sim N(A\boldsymbol\mu + \mathbf{b}, A\Sigma A^T)$.
- **Uncorrelated $\Longleftrightarrow$ Independent.** If $\Sigma$ is diagonal, the joint density factors into product of 1D Gaussians.
- **Conditional is Gaussian with reduced covariance.** For $\mathbf{X} = (X_1, X_2)$ partitioned into blocks:
  $$E[X_1 | X_2 = x_2] = \mu_1 + \Sigma_{12}\Sigma_{22}^{-1}(x_2 - \mu_2)$$
  $$\text{Cov}(X_1 | X_2 = x_2) = \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$$
  Mean shifts linearly with observation; conditional covariance is **smaller** than marginal (partial information acquired).

## Why it matters
- **Noise models:** multivariate Gaussian is the default for modeling random errors in many systems (sensor noise, communication channels, financial returns).
- **Optimal linear estimation:** the LMS estimator for jointly Gaussian signals is **linear** and equals the MAP/conditional mean. See [[lms-estimation]].
- **Kalman filter:** maintains a multivariate-Gaussian belief about system state.
- **PCA:** finds the principal axes of the covariance ellipsoid.

## Common mistakes
- "Each $X_i$ is Gaussian $\Rightarrow$ multivariate Gaussian." **False.** Need joint normality, which is stronger.
- $\Sigma$ not positive semidefinite — the PDF isn't valid. $\Sigma$ must come from $\Sigma = \text{Cov}(\mathbf{X})$ for some random vector.
- Forgetting $\Sigma$ must be symmetric. Always write $\Sigma_{ij} = \Sigma_{ji}$.

## Related
- [[bivariate-gaussian]] — $n = 2$ case
- [[covariance]] — entries of $\Sigma$
- [[conditional-expectation]] — Gaussian case gives linear formulas
- [[random-vector]]

## Practice
- [[prob-fundamentals-set-01]]
