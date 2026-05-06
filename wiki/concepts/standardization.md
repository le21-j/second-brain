---
title: Standardization (Z-Score)
type: concept
course:
  - "[[eee-350]]"
tags: [gaussian, z-score, standardization, transformation]
sources:
  - "[[homework-2026-04-23-eee-350-hw7]]"
created: 2026-04-24
updated: 2026-05-06
---

# Standardization (Z-Score)

## In one line
For any random variable $X$ with mean $\mu$ and std dev $\sigma > 0$, the transformation
$$Z = \frac{X - \mu}{\sigma}$$
produces a random variable with $E[Z] = 0$ and $\text{Var}(Z) = 1$. If $X$ is Normal, then $Z \sim N(0, 1)$.

## Example first
$K \sim \text{Binomial}(100, 0.5)$: $E[K] = 50$, $\sigma_K = 5$.

By [[central-limit-theorem|CLT]], $K$ is approximately $N(50, 25)$. Standardize:
$$Z = \frac{K - 50}{5}.$$

| Quantity | Mean | Variance |
|---|:---:|:---:|
| $K$ | $50$ | $25$ |
| $K - 50$ | $0$ | $25$ |
| $(K - 50) / 5$ | $0$ | $25/25 = 1$ |

The variance becomes 1 because the **5 in the denominator squares to 25** when it acts on variance (see [[variance-scaling-rule]]). That 25 exactly kills the 25 variance of $K - 50$.

**Use case:** $P(K > 60) = P(Z > (60 - 50)/5) = P(Z > 2) = 1 - \Phi(2) \approx 0.023$ — read from [[standard-normal-table]].

## The two algebra rules used

1. **Mean shifts linearly.** $E[X - \mu] = E[X] - \mu = 0$. Subtracting a constant does not change the variance.
2. **Variance scales quadratically.** $\text{Var}(cX) = c^2 \cdot \text{Var}(X)$. Dividing by $\sigma$ scales variance by $1/\sigma^2$. See [[variance-scaling-rule]].

Combined:
$$\text{Var}\!\left(\frac{X - \mu}{\sigma}\right) = \frac{1}{\sigma^2}\text{Var}(X) = 1.$$

## Why divide by $\sigma$ specifically?
Not arbitrary — **reverse-engineered so the variance equals 1**. Dividing by anything else gives the wrong scale.

## Standardization is not CLT

| CLT | Standardization |
|---|---|
| *Shape* theorem: sum/avg becomes Gaussian | *Rescaling* operation: changes mean/variance |
| Result: $N(n\mu, n\sigma^2)$ or $N(\mu, \sigma^2/n)$ | Result: $N(0, 1)$ **if** input was Normal |
| Input distribution can be anything (i.i.d., finite variance) | Only meaningful for $\mu$ known and $\sigma$ known (or estimated) |

Textbooks often apply CLT and standardize in one breath, making them look like the same step. They are **two distinct operations** — the Q4 gotcha in [[homework-2026-04-23-eee-350-hw7]] spells this out carefully.

## Three forms of "CLT" (same theorem, different scalings)

| Form | Expression | Approx distribution |
|---|---|---|
| Raw sum | $S_n = \sum X_i$ | $N(n\mu, n\sigma^2)$ |
| Sample mean | $\bar X_n = S_n / n$ | $N(\mu, \sigma^2/n)$ |
| **Standardized sum** | $Z_n = (S_n - n\mu)/(\sigma\sqrt{n})$ | **$N(0, 1)$** |

Only Form 3 is standard Normal — because standardization was applied.

## The "Gaussian = Normal" vocabulary

They're the same distribution.
- **Gaussian** honors Carl Friedrich Gauss (astronomy, 1800s).
- **Normal** is the name Galton/Pearson later popularized.
- $\mathcal{N}$ covers both.

The *standard* Normal is the specific member $N(0, 1)$. Every Normal is a shifted, stretched copy, recoverable by standardization.

## Inverse (un-standardizing)
$X = \mu + \sigma \cdot Z$. If you have a z-score and need to return to the original scale, multiply by $\sigma$ and add $\mu$.

## Common mistakes
- **Linear std dev vs quadratic variance.** $\text{SD}(cX) = |c| \cdot \text{SD}(X)$; $\text{Var}(cX) = c^2 \cdot \text{Var}(X)$. Don't forget the square on variance. See [[variance-scaling-rule]].
- **Standardizing the wrong random variable.** Use the $\mu$ and $\sigma$ of the RV you're working with, not of a related one.
- **Forgetting $n$ in the sample mean case.** For $\bar X_n$: $\mu$ stays $\mu$, but $\sigma$ shrinks to $\sigma/\sqrt{n}$. So standardize using $\sigma/\sqrt{n}$, not $\sigma$.

## Related
- [[central-limit-theorem]] — provides the Normal shape that standardization then scales
- [[standard-normal-table]] — the table you consult after standardizing
- [[variance-scaling-rule]] — the $\text{Var}(cX) = c^2\text{Var}(X)$ rule
- [[confidence-interval]] — uses z-scores to build bounds

## Examples
- [[fair-coin-significance-test]] — standardization applied in HW7 11.1.6
