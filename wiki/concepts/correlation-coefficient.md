---
title: Correlation Coefficient
type: concept
course: [[eee-350]]
tags: [correlation, moments, normalized]
sources: [[slides-38-covariance]]
created: 2026-04-21
updated: 2026-04-26
---

# Correlation Coefficient

## In one line
$\rho_{XY} = \text{Cov}(X, Y) / (\sigma_X \cdot \sigma_Y)$ — a **dimensionless** number in $[-1, +1]$ that measures linear dependence, normalized so scale doesn't affect it.

## Example first
Measure heights (cm) and weights (kg) of 1000 adults. You get $\text{Cov}(H, W) \approx 450$ cm$\cdot$kg — a weird-units number. Is that "big" or "small"?

Compute $\rho$: $\sigma_H \approx 10$ cm, $\sigma_W \approx 15$ kg. $\rho = 450 / (10 \cdot 15) =$ **$+0.75$**. Now it's meaningful — strongly positive, but not perfect.

Switch $H$ to meters: $\text{Cov}(H, W)$ becomes $4.5$ m$\cdot$kg ($1/100$ the value), but $\rho$ stays $0.75$. **That invariance is the whole point.**

## The idea
Covariance has a dimensional issue: $\text{Cov}(X, Y)$ is measured in $X$-units $\times$ $Y$-units. Multiply $X$ by 100 and Cov multiplies by 100 even though nothing really changed. Correlation fixes this by dividing by the standard deviations so scale cancels out.

## Formal definition
$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \, \sigma_Y}$$

## Bounds ($|\rho| \leq 1$)
By Cauchy–Schwarz: $|E[(X - \mu_X)(Y - \mu_Y)]| \leq \sqrt{E[(X - \mu_X)^2] \cdot E[(Y - \mu_Y)^2]} = \sigma_X \sigma_Y$. Divide by $\sigma_X \sigma_Y$:
$$-1 \le \rho_{XY} \le +1$$

**Extremes:**
- $\rho = +1 \Longleftrightarrow Y = aX + b$ with $a > 0$ (perfect positive linear relationship).
- $\rho = -1 \Longleftrightarrow Y = aX + b$ with $a < 0$ (perfect negative).
- $\rho = 0 \Longleftrightarrow$ uncorrelated (no **linear** trend — may still be dependent).

## Rules of thumb
- $|\rho| \approx 0.0$–$0.1$: essentially no linear relation.
- $|\rho| \approx 0.3$: weak.
- $|\rho| \approx 0.5$: moderate.
- $|\rho| \approx 0.7$: strong.
- $|\rho| \approx 0.9+$: very strong, almost linear.

These are heuristics — interpret in context.

## Why it matters
- **Regression slope** in standardized form: if you standardize $X$ and $Y$ to mean 0 std 1, the least-squares slope equals $\rho$.
- **Portfolio risk diversification:** assets with $\rho < 1$ reduce portfolio variance even if individual variances are the same.
- **PCA / dimensionality reduction:** highly-correlated variables carry redundant information.

## Common mistakes
- **"Correlation = causation."** No. A high $|\rho|$ could reflect a common cause, coincidence, or direct causation in either direction.
- **$\rho = 0$ means independent.** No, unless the variables are jointly Gaussian. Same counter-example as covariance: $X \sim \text{Uniform}(-1, 1)$, $Y = X^2 \to \rho = 0$ but $Y$ is a deterministic function of $X$.
- **Using $\rho$ for non-linear relationships.** $\rho$ only captures linear trends. A perfect parabolic relationship can have $\rho = 0$.
- **Extrapolating $\rho$.** Correlation on one range of $X$ doesn't imply the same relationship outside that range.

## Related
- [[covariance]] — the numerator
- [[independent-vs-uncorrelated]]
- [[bivariate-gaussian]] ($\rho$ is the 5th parameter)
- [[linear-regression]]

## Practice
- [[prob-fundamentals-set-01]]
