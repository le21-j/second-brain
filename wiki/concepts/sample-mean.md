---
title: Sample Mean
type: concept
course: [[eee-350]]
tags: [sample-mean, descriptive-statistics, estimator]
sources: [[slides-42-wlln]], [[slides-44-mle-ci]], [[slides-46.5-descriptive-stats]]
created: 2026-04-21
updated: 2026-04-26
---

# Sample Mean

## In one line
$\bar X_n = (X_1 + X_2 + \ldots + X_n) / n$ — the simple average. **Unbiased, consistent, often efficient** estimator of the true mean $\mu$.

## Properties

- **$E[\bar X_n] = \mu$** — unbiased.
- **$\text{Var}(\bar X_n) = \sigma^2/n$** (for i.i.d. $X_i$) — shrinks with more data.
- **Consistent:** $\bar X_n \to \mu$ in probability by [[weak-law-of-large-numbers|WLLN]].
- **CLT:** $\sqrt{n}(\bar X_n - \mu)/\sigma \to N(0, 1)$.
- **MLE of Gaussian mean.** If $X_i \sim N(\mu, \sigma^2)$, sample mean is the MLE of $\mu$.
- **Efficient** for Gaussian: achieves the Cramér-Rao bound.

## Standard error of the mean
$\text{SE}(\bar X_n) = \sigma/\sqrt{n}$. Pay close attention to the **$1/\sqrt{n}$**:
- Halving SE requires **quadrupling** $n$.
- $10\times$ reduction requires **$100\times$** data.

## Sensitive to outliers
One extreme value can drag $\bar X_n$ arbitrarily. The median is more **robust**.

Example: dataset $[1, 2, 3, 4, 5, 1000]$. Mean $= 169.2$, median $= 3.5$. For small-$n$ datasets with possible outliers, report both.

## Related
- [[weak-law-of-large-numbers]]
- [[central-limit-theorem]]
- [[confidence-interval]] ($\bar x \pm z\cdot\sigma/\sqrt{n}$)
- [[unbiased-estimator]], [[consistent-estimator]]
- [[sample-median]] — the robust alternative
- [[sample-variance]]
