---
title: Slides 38 — Covariance and Correlation Coefficient
type: summary
source_type: slides
source_path: raw/slides/eee-350/38 Covariance and Correlation Coeff.pptx
course:
  - "[[eee-350]]"
tags: [covariance, correlation, bivariate]
created: 2026-04-21
updated: 2026-05-06
---

# Slides 38 — Covariance & Correlation Coefficient

## TL;DR
Introduces **covariance** $\text{Cov}(X,Y) = E[(X-\mu_X)(Y-\mu_Y)]$ as a measure of linear dependence between two RVs, and shows how it appears in $\text{Var}(X+Y)$. Defines the **correlation coefficient** $\rho = \text{Cov}(X,Y)/(\sigma_X \sigma_Y)$ as the normalized, dimensionless version. Closes with independence $\Rightarrow$ $\text{Cov} = 0$ (but **not** vice versa in general) and covariance between jointly Gaussian RVs.

## Key takeaways
- **$\text{Cov}(X, Y) = E[XY] - E[X]\cdot E[Y]$** (useful computational form).
- **$\text{Var}(X + Y) = \text{Var}\, X + \text{Var}\, Y + 2\cdot\text{Cov}(X, Y)$** — this is where covariance "naturally appears".
  - $\text{Cov} > 0$: sum has more variance than uncorrelated case (co-move up).
  - $\text{Cov} < 0$: less (hedge each other).
  - $\text{Cov} = 0$: Var of sum = sum of Vars (uncorrelated case).
- **$\rho \in [-1, +1]$** (by Cauchy–Schwarz); dimensionless.
- **$X \perp Y \Rightarrow \text{Cov}(X, Y) = 0$**. The converse is **false** in general — uncorrelated $\neq$ independent.
- **Jointly Gaussian** case: uncorrelated $\Rightarrow$ independent. (Special property of Gaussians.)
- Bivariate Gaussian: 5 parameters ($\mu_X, \mu_Y, \sigma_X, \sigma_Y, \rho$).

## Concepts introduced or reinforced
- [[covariance]] — full treatment
- [[correlation-coefficient]] — $\rho$ properties
- [[variance-of-a-sum]]
- [[bivariate-gaussian]]
- [[independent-vs-uncorrelated]] — the classic gotcha

## Worked examples worth remembering
- $\text{Cov}(X, X + Z)$ where $X \perp Z \to \text{Cov} = \text{Var}(X)$.
- Finding $\text{Var}(aX + bY)$ using the bilinearity.

## Questions this source raised
- Counter-example: $X$ and $Y$ with $\text{Cov} = 0$ but not independent. Typical one: $X$ uniform on $[-1, 1]$, $Y = X^2$. Covered in [[independent-vs-uncorrelated]].
