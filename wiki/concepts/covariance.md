---
title: Covariance
type: concept
course: [[eee-350]]
tags: [covariance, moments, dependence]
sources: [[slides-38-covariance]]
created: 2026-04-21
updated: 2026-04-26
---

# Covariance

## In one line
$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]$ — a signed measure of how $X$ and $Y$ vary together.

## Example first
Let $X$ = roll of a die, $Y = X + U$ where $U$ is another independent die roll. Intuitively $X$ and $Y$ should **move together** — bigger $X$ tends to mean bigger $Y$.

Compute: $\text{Cov}(X, Y) = \text{Cov}(X, X + U)$ where $U$ is the second die.
$= \text{Cov}(X, X) + \text{Cov}(X, U)$ (bilinearity)
$= \text{Var}(X) + 0$ (independent)
$= 35/12 \approx 2.92$

Contrast: if $Y = 7 - X$ ($X$ and $Y$ anti-correlated, as in "if $X$ is 1, $Y$ is 6"), then $\text{Cov}(X, Y) = \text{Cov}(X, -X) = -\text{Var}(X) \approx -2.92$. Negative covariance $\to$ they move opposite.

## The idea
**Covariance measures linear comovement.**
- Positive: when $X$ is above its mean, $Y$ tends to be above its mean too.
- Negative: when $X$ is above its mean, $Y$ tends to be below its mean.
- Zero: no **linear** trend in the comovement (doesn't mean no relationship — see [[independent-vs-uncorrelated]]).

## Formal definition
$$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - \mu_X \mu_Y$$

The second form is the **computational shortcut** — usually easier.

## Key properties
- **Symmetry:** $\text{Cov}(X, Y) = \text{Cov}(Y, X)$.
- **$\text{Cov}(X, X) = \text{Var}(X)$** — variance is a special case.
- **Bilinearity:**
  $$\text{Cov}(aX + b, cY + d) = ac\,\text{Cov}(X, Y)$$
  $$\text{Cov}(X + Z, Y) = \text{Cov}(X, Y) + \text{Cov}(Z, Y)$$
- **Independence $\Rightarrow \text{Cov} = 0$.** The converse is **false** (see [[independent-vs-uncorrelated]]).
- Dimensional: $\text{Cov}(X, Y)$ has units of ($X$ units)$\cdot$($Y$ units). The normalized version is the [[correlation-coefficient]].

## Computing covariance

### From joint PMF/PDF
$$\text{Cov}(X, Y) = \int\int (x - \mu_X)(y - \mu_Y)\, f_{X,Y}(x, y)\, dx\, dy$$
Or use the shortcut $E[XY] - E[X]E[Y]$, where $E[XY] = \int\int xy \cdot f(x,y)\, dx\, dy$.

### Example: from independence
If $X \perp Z$ and $Y = X + Z$:
- $E[XY] = E[X \cdot (X + Z)] = E[X^2] + E[X]E[Z] = E[X^2] + \mu_X \cdot \mu_Z$.
- $E[X]E[Y] = \mu_X \cdot (\mu_X + \mu_Z) = \mu_X^2 + \mu_X \cdot \mu_Z$.
- $\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = E[X^2] - \mu_X^2 =$ **$\text{Var}(X)$**.

## Why it matters
Covariance appears everywhere:
- **[[variance-of-a-sum]]:** $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X, Y)$.
- **[[correlation-coefficient]]:** normalized covariance, dimensionless.
- **Regression:** slope of the best-fit line $= \text{Cov}(X, Y) / \text{Var}(X)$.
- **Portfolio theory:** Var of a weighted sum of assets is a quadratic form in their covariance matrix.

## Common mistakes
- **$\text{Cov} = 0 \Longrightarrow$ independence.** **False.** Only true for jointly Gaussian. Classic counter: $X \sim \text{Uniform}(-1, 1)$, $Y = X^2$. $\text{Cov} = 0$ but $Y$ is a deterministic function of $X$.
- **Adding covariance when variables are independent of each other but not independent of $X$.** Always check independence carefully; in $\text{Cov}(X + Z, Y)$ the cross terms $\text{Cov}(X, Y)$ and $\text{Cov}(Z, Y)$ matter even if $X \perp Z$.
- **Forgetting the dimensional issue.** You can't compare $\text{Cov}(\text{height, weight})$ with $\text{Cov}(\text{height, age})$ directly — scales differ. Always normalize if comparing.

## Related
- [[correlation-coefficient]] — normalized version
- [[variance-of-a-sum]]
- [[independent-vs-uncorrelated]]
- [[bivariate-gaussian]]

## Practice
- [[prob-fundamentals-set-01]]
