---
title: Independent vs Uncorrelated
type: concept
course: [[eee-350]]
tags: [independence, covariance, gotcha]
sources: [[slides-38-covariance]]
created: 2026-04-21
updated: 2026-04-26
---

# Independent vs Uncorrelated

## In one line
**Independent $\Rightarrow$ uncorrelated**, but **uncorrelated $\not\Rightarrow$ independent** in general. Only for jointly Gaussian RVs do the two imply each other.

## Example first (the classic counter-example)
Let $X \sim \text{Uniform}(-1, +1)$ and $Y = X^2$. Then:
- $E[X] = 0$.
- $E[XY] = E[X \cdot X^2] = E[X^3]$. By symmetry ($X$'s density is even), $E[X^3] = 0$.
- $\text{Cov}(X, Y) = E[XY] - E[X] \cdot E[Y] = 0 - 0 =$ **$0$**. So $\rho = 0$ — uncorrelated.

But $Y$ is a **deterministic function** of $X$ — knowing $X$ tells you $Y$ exactly. That's the opposite of independence.

So: **$\text{Cov}(X, Y) = 0$ and $Y$ is completely determined by $X$, simultaneously.** Uncorrelated $\neq$ independent.

## The idea

**Independence** is strong: for all $(x, y)$,
$$f_{X,Y}(x, y) = f_X(x)\cdot f_Y(y)$$
Every joint statistic factors.

**Uncorrelated** is much weaker: just
$$E[XY] = E[X]\cdot E[Y]$$
Only **linear** comovement is zero. Non-linear relationships (like $Y = X^2$) can make $\text{Cov} = 0$ while leaving massive dependence.

## Implication ladder
- Independence $\Rightarrow$ uncorrelated $\checkmark$
- Independence $\Rightarrow \text{Cov}(X, Y) = 0$ $\checkmark$
- Independence $\Rightarrow$ all $E[g(X) \cdot h(Y)] = E[g(X)] \cdot E[h(Y)]$ for any $g, h$ $\checkmark$
- Uncorrelated $\Rightarrow$ independence $\times$
- Uncorrelated $\Rightarrow E[X^2 Y^2] = E[X^2] \cdot E[Y^2]$ $\times$ (only linear moment factors)

## The Gaussian exception
If $(X, Y)$ are **jointly Gaussian**, then uncorrelated ($\rho = 0$) $\Rightarrow$ independent. This is a **special property of the Gaussian family** — their joint density decomposes as $f(x) \cdot f(y)$ exactly when $\Sigma$ is diagonal. Do not generalize to other distributions.

**Common trap:** $X$ and $Y$ both Gaussian **individually** (marginally) does NOT mean they're jointly Gaussian. Two marginal-Gaussian RVs can have $\rho = 0$ without being independent. The joint distribution must be multivariate Gaussian.

## Why the distinction matters
- **CLT/LLN for sums of random vectors:** variance of sum uses covariance, so "uncorrelated" is enough — full independence isn't required. Many theorems weaken "i.i.d." to "uncorrelated, identical variance".
- **Regression:** the least-squares coefficient uses $\text{Cov}(X, Y)$. Knowing $X$ and $Y$ are uncorrelated tells you the **linear** relationship is zero — but there could still be perfect non-linear dependence you'd miss.
- **Feature engineering in ML:** two features can have $\rho \approx 0$ yet contain redundant information; need dependence measures (mutual information) to detect non-linear relationships.

## Common mistakes
- Using $\text{Cov} = 0$ (or $\rho = 0$) to claim independence. Only safe under joint Gaussianity.
- Using "$X$ and $Y$ are both Gaussian" as a shortcut for "jointly Gaussian". The joint must be Gaussian.
- Forgetting the counter-example exists. When in doubt, think of $Y = X^2$ on symmetric $X$.

## Related
- [[covariance]]
- [[correlation-coefficient]]
- [[bivariate-gaussian]]
- [[prob-gotchas]] — where this gets a permanent mistake entry
