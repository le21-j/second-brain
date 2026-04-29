---
title: Max of n i.i.d. RVs
type: concept
course: [[eee-350]]
tags: [order-statistics, iid, cdf]
sources: [[slides-39-multivariate-vectors]]
created: 2026-04-21
updated: 2026-04-26
---

# Max of n i.i.d. RVs

## In one line
If $X_1, \ldots, X_n$ are i.i.d. with CDF $F$, then the maximum $M_n = \max(X_1, \ldots, X_n)$ has CDF **$F(t)^n$**.

## Example first
Draw 10 i.i.d. $\text{Uniform}(0, 1)$ random numbers. What's the probability the max is $\leq 0.8$?

$P(\max \leq 0.8) = P(\text{all 10} \leq 0.8) = (0.8)^{10} \approx 0.107$.

So the max is concentrated near 1: $P(\max > 0.9) = 1 - 0.9^{10} \approx 0.65$.

## The idea
The event "$\max \leq t$" is equivalent to "**every** $X_i \leq t$". By independence:
$$P(M_n \le t) = P(X_1 \le t, \ldots, X_n \le t) = \prod_{i=1}^n P(X_i \le t) = F(t)^n$$

## Derived PDF
Differentiate $F_{\max}(t) = F(t)^n$:
$$f_{M_n}(t) = n \cdot F(t)^{n-1} \cdot f(t)$$

Interpretation: the density is $n$ times the density at $t$ (weighted by the chance everyone else is already below $t$).

## Example: max of n i.i.d. exponentials
$X_i \sim \text{Exp}(\lambda) \to F(t) = 1 - e^{-\lambda t}$ for $t \geq 0$.
$$F_{M_n}(t) = (1 - e^{-\lambda t})^n$$
$$f_{M_n}(t) = n(1 - e^{-\lambda t})^{n-1}\cdot\lambda e^{-\lambda t}$$
Max of exponentials is **not** exponential — the distribution skews right as $n$ grows.

(Contrast: **min** of $n$ exponentials **is** exponential, rate $n\lambda$ — memorylessness trick.)

## Min of n i.i.d. RVs
Symmetric formula: "$\min > t$" means "all $> t$":
$$P(M^{min}_n > t) = (1 - F(t))^n$$
$$f_{M^{min}_n}(t) = n(1 - F(t))^{n-1}\cdot f(t)$$

For exponentials: $\min \sim \text{Exp}(n\lambda)$.

## Why it matters
- **Reliability engineering:** lifetime of a parallel system with $n$ redundant components = max of $n$ component lifetimes.
- **Extreme value theory:** studying floods, stock-market crashes, peak loads — the domain of max-statistics.
- **[[order-statistics]]:** general framework for ranked samples.

## Common mistakes
- Forgetting **independence** — the $F(t)^n$ result needs independence.
- Forgetting **identical distributions** — if $X_i$ have different $F_i$, max has CDF $\prod F_i(t)$, not $F(t)^n$.
- Using min formula where max is needed, or vice versa.

## Related
- [[iid-samples]]
- [[order-statistics]]
- [[poisson-process]] (uses the memoryless min-of-exponentials trick)

## Practice
- [[prob-fundamentals-set-01]]
