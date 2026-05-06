---
title: Unbiased Estimator
type: concept
course:
  - "[[eee-350]]"
tags: [estimator, bias]
sources:
  - "[[slides-44-mle-ci]]"
created: 2026-04-21
updated: 2026-05-06
---

# Unbiased Estimator

## In one line
$\hat\theta$ is **unbiased** for $\theta$ if $E[\hat\theta] = \theta$ for every possible value of $\theta$.

## Example
- Sample mean $\bar X_n$ **is unbiased** for $\mu$: $E[\bar X_n] = \mu$ always.
- Sample variance with $(n-1)$ denominator is unbiased for $\sigma^2$. With $(n)$ denominator, it's biased (systematically too small by factor $(n-1)/n$).

## Why care
- **Interpretation:** on average across many experiments, $\hat\theta$ gives the right answer.
- **Common benchmark:** many theoretical results (Cramér-Rao bound, UMVUE) are stated for unbiased estimators.

## Bias $\neq$ error
- **Bias** = $E[\hat\theta - \theta]$. Systematic offset.
- **Variance** = $\text{Var}(\hat\theta)$. Random scatter.
- **MSE** = $\text{Bias}^2 + \text{Variance}$. The true "how wrong are you on average" metric.

A **biased estimator** can beat an unbiased one on MSE. Classic example: for Gaussian variance with small $n$, the MLE (biased, divided by $n$) has smaller MSE than the unbiased (divided by $n-1$). Bias-variance tradeoff in machine learning is the same idea.

## Consistency is different
An unbiased estimator might not be consistent (not converge to $\theta$), and a biased one might be consistent (bias shrinks to 0). See [[consistent-estimator]].

## Common mistakes
- Assuming **MLE is always unbiased.** Often it isn't.
- Preferring **unbiased over biased** on principle. MSE is what usually matters.

## Related
- [[consistent-estimator]]
- [[efficient-estimator]]
- [[maximum-likelihood-estimation]]
- [[sample-mean]]
- [[sample-variance]]
