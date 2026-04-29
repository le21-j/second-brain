---
title: Order Statistics
type: concept
course: [[eee-350]]
tags: [order-statistics, ranks, quantiles]
sources: [[slides-46.5-descriptive-stats]]
created: 2026-04-21
updated: 2026-04-26
---

# Order Statistics

## In one line
Sort your data $x_1, \ldots, x_n$ into $x_{(1)} \leq x_{(2)} \leq \ldots \leq x_{(n)}$. These sorted values are **order statistics**.

## Key special cases
- **$x_{(1)}$** = min of the sample.
- **$x_{(n)}$** = max of the sample — see [[max-of-iid]] for its distribution.
- **$x_{(\lceil n/2\rceil)}$** or average of middle two = [[sample-median|sample median]].
- **$x_{(\lceil nq\rceil)}$** $\approx$ $q$-th sample quantile.

## Distributions
For $X_i$ i.i.d. with CDF $F$:
- $F_{x_{(k)}}(t) = P(\text{at least } k \text{ of } X_i \text{ are } \leq t)$ = sum of binomial tail terms.
- Density: $f_{x_{(k)}}(t) = (n! / ((k-1)!(n-k)!)) \cdot F(t)^{k-1}\cdot(1-F(t))^{n-k}\cdot f(t)$.
- **Max** ($k = n$): $F^n \cdot$ simpler form.
- **Min** ($k = 1$): $1 - (1 - F)^n$.

## Uses
- **Quantile estimation:** sample quantiles.
- **Boxplots:** show $x_{(1)}$, $Q_1$ (25%), median, $Q_3$ (75%), $x_{(n)}$.
- **Robust statistics:** trim extreme order statistics before averaging.
- **Extreme value theory:** max of $n$ i.i.d. as $n \to \infty$ (Gumbel, Weibull, Fréchet limit distributions).

## Related
- [[sample-median]]
- [[max-of-iid]]
- [[histogram]]
