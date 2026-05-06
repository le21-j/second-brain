---
title: Sample Variance
type: concept
course:
  - "[[eee-350]]"
tags: [sample-variance, descriptive-statistics, n-minus-1]
sources:
  - "[[slides-46.5-descriptive-stats]]"
  - "[[slides-44-mle-ci]]"
created: 2026-04-21
updated: 2026-05-06
---

# Sample Variance

## In one line
$s^2 = (1/(n - 1)) \sum(x_i - \bar x)^2$ — the **unbiased** sample variance. Using $(1/n)$ gives the MLE, which is **biased**.

## The $1/(n-1)$ vs $1/n$ debate

| Denominator | Name | $E[s^2]$ | Use when |
|---|---|---|---|
| **$n - 1$** | unbiased sample variance | $\sigma^2$ | Classical stats, CI, t-tests |
| **$n$** | MLE estimate | $(n-1)/n \cdot \sigma^2$ (biased low) | Asymptotic or when explicitly doing MLE |

The difference (Bessel's correction): since we used the sample mean $\bar x$ instead of the true $\mu$, we "used up" one degree of freedom. Dividing by $n - 1$ instead of $n$ corrects for it.

For large $n$, the difference is negligible ($n/(n-1) \to 1$).

## Why biased?

$E[\sum(x_i - \bar x)^2] = (n - 1)\cdot\sigma^2$. The expected sum of squared deviations from $\bar x$ is $(n - 1)\sigma^2$, not $n\sigma^2$. So dividing by $n$ gives an expectation of $(n-1)\sigma^2/n < \sigma^2$. Dividing by $(n-1)$ fixes this.

## Sample standard deviation
$s = \sqrt{s^2}$. Note: $s$ is **not** an unbiased estimator of $\sigma$ (the expectation of a square root isn't the square root of the expectation). But the bias of $s$ for $\sigma$ is usually small and ignored in practice.

## Properties of $s^2$
- **Consistent** for $\sigma^2$ by LLN.
- **Distribution under Gaussian data:** $(n-1)s^2/\sigma^2 \sim \chi^2(n-1)$. Used for [[chi-squared-test|tests about variance]] and for **t-intervals** when $\sigma$ is unknown.

## Related
- [[sample-mean]]
- [[maximum-likelihood-estimation]]
- [[unbiased-estimator]]
- [[chi-squared-test]]
- [[confidence-interval]]
