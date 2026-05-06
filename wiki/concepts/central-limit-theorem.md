---
title: Central Limit Theorem (CLT)
type: concept
course:
  - "[[eee-350]]"
tags: [clt, asymptotic, gaussian]
sources:
  - "[[slides-43-clt-apps]]"
created: 2026-04-21
updated: 2026-05-06
---

# Central Limit Theorem (CLT)

## In one line
For i.i.d. $X_i$ with finite mean $\mu$ and variance $\sigma^2$, the standardized sum $(S_n - n\mu)/(\sigma\sqrt{n})$ converges in distribution to a standard normal **$N(0, 1)$** — **regardless of the underlying distribution**.

## Example first
Roll $n$ fair dice and sum the results: $S_n = X_1 + \ldots + X_n$. Each $X_i$ has $\mu = 3.5$, $\sigma^2 = 35/12$.
- $E[S_n] = 3.5n$, $\text{Var}(S_n) = 35n/12$.
- **By CLT:** $S_n$ is approximately $N(3.5n, 35n/12)$ for large $n$.
- At $n = 30$: $P(S_n > 125) \approx P(Z > (125 - 105)/\sqrt{35 \cdot 30/12}) = P(Z > 2.08) \approx 0.019$ using a standard-normal table.

The individual $X$'s are discrete uniform, but after summing 30 of them the distribution is **essentially Gaussian**. That's the magic.

## Formal statement
Let $X_1, X_2, \ldots$ be i.i.d. with finite mean $\mu$ and variance $\sigma^2 > 0$. Let $S_n = \sum X_i$. Then:
$$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)$$

"$\xrightarrow{d}$" means convergence in distribution: the CDF of $Z_n$ converges to $\Phi(z)$ (the standard-normal CDF) at every $z$.

Equivalently, the sample mean satisfies:
$$\sqrt{n}\cdot\frac{\bar X_n - \mu}{\sigma} \xrightarrow{d} N(0, 1)$$

## Three scalings of the sum (important)

| Thing | Variance | Behavior |
|---|---|---|
| $S_n$ | $n \cdot \sigma^2$ | Blows up ($\text{Var} \to \infty$) |
| $S_n / n$ (sample mean) | $\sigma^2/n$ | Concentrates at $\mu$ ($\text{Var} \to 0$); this is [[weak-law-of-large-numbers\|WLLN]] |
| **$(S_n - n\mu) / (\sigma\sqrt{n})$** | **$1$** | Converges to $N(0,1)$; this is CLT |

The $\sqrt{n}$ scaling is the unique one that gives a non-trivial limiting distribution.

## When the approximation is good
- **Rough rule:** $n \geq 30$ for most "not too weird" distributions.
- Close-to-symmetric distributions: $n = 10$–$15$ is often plenty.
- Very skewed distributions (e.g. Exponential, Log-Normal): need larger $n$, maybe $50$–$100$.
- **Cauchy distribution:** CLT fails because variance is infinite.

## The "profundity" point
The CLT is why the Gaussian shows up everywhere in nature: whenever a quantity is the sum of many small independent effects (measurement errors, stock returns, population heights), it's approximately Gaussian. **No Gaussian assumptions are needed in the inputs.**

## Continuity correction (for discrete sums)
When approximating a discrete distribution (like Binomial) by CLT, you get sharper answers by shifting the threshold by $0.5$:
$$P(S_n \le k) \approx \Phi\!\left(\frac{k + 0.5 - n\mu}{\sigma\sqrt{n}}\right)$$
See [[continuity-correction]]. Slides' example: changing 21 to 21.5.

## Common applications

### Polling
To estimate a population proportion $p$ within $\varepsilon$ with confidence $1 - \alpha$:
- $\bar X_n \approx p + (1/\sqrt{n}) \cdot N(0, p(1-p)) \cdot \text{scaled}$
- Required $n$: $n \approx (z_{\alpha/2}/\varepsilon)^2 \cdot p(1-p)$. Using worst-case $p(1-p) = 1/4$: **$n \approx (z_{\alpha/2}/\varepsilon)^2 \cdot 0.25$**.
- For 95% ($z = 1.96$) and $\varepsilon = 0.03$: $n \approx 1067$. That's why political polls use $n \approx 1000$.

### Binomial approximation
$\text{Binomial}(n, p) \approx N(np, np(1-p))$ for large $n$, moderate $p$. Lets you use a normal table instead of computing binomial CDFs.

## Common mistakes
- **Using CLT for small $n$ on skewed data.** If $n = 5$ and the $X$'s are Exponential, the sum is nowhere near Gaussian.
- **Forgetting continuity correction** for discrete sums $\to$ off-by-$0.5$ error in tail probabilities.
- **Applying CLT to non-independent or non-identically-distributed data without care.** There are extensions (Lindeberg–Feller, martingale CLTs) — not covered here.
- **Confusing CLT with WLLN.** They scale differently and say different things.

## Related
- [[weak-law-of-large-numbers]]
- [[continuity-correction]]
- [[binomial-via-clt]]
- [[standard-normal-table]]
- [[confidence-interval]]

## Practice
- [[asymptotics-set-01]]
