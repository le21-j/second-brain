---
title: Slides 44 — MLE and Interval Estimation
type: summary
source_type: slides
source_path: raw/slides/eee-350/44 MLE and Interval Estimation.pptx
course:
  - "[[eee-350]]"
tags: [mle, estimator, confidence-interval, classical-statistics]
created: 2026-04-21
updated: 2026-05-06
---

# Slides 44 — MLE and Interval Estimation

## TL;DR
**Classical statistics** (no prior on $\theta$ — $\theta$ is a fixed but unknown deterministic parameter). **Maximum likelihood** picks $\hat\theta = \arg\max_\theta p(x | \theta)$: "the value of $\theta$ that makes the observed data most likely". Three criteria for a **good estimator**: **unbiased** ($E[\hat\theta] = \theta$), **consistent** ($\hat\theta \to \theta$ in probability), **minimum variance** among unbiased estimators. Introduces **confidence intervals** — instead of a point estimate, report an interval that contains $\theta$ with probability $1 - \alpha$.

## Key takeaways
- **Likelihood function:** $L(\theta) = p(x | \theta)$ viewed as function of $\theta$ for fixed data $x$. Pick $\theta$ that maximizes it.
- **Log-likelihood:** $\ell(\theta) = \log L(\theta)$ — usually easier (products $\to$ sums). $\arg\max$ is the same because log is monotone.
- **MLE for Gaussian mean ($n$ i.i.d. samples):** $\hat\mu_{\text{MLE}} = \bar x$ (the sample mean). Also unbiased and consistent.
- **MLE for Gaussian variance:** $\hat\sigma^2_{\text{MLE}} = (1/n) \sum(x_i - \bar x)^2$ — but this is **biased**. The unbiased sample variance uses $1/(n-1)$.
- **Estimator quality:**
  - **Unbiased:** $E[\hat\theta] = \theta$ exactly.
  - **Consistent:** $\hat\theta_n \to \theta$ in probability.
  - **Efficient:** minimum variance among unbiased estimators (Cramér-Rao bound).
- **Confidence interval for mean** ($\sigma$ known, $n$ large, via CLT):
  $$\bar X_n \pm z_{\alpha/2}\cdot\tfrac{\sigma}{\sqrt{n}}$$
  where $z_{\alpha/2}$ is the standard-normal critical value (e.g. 1.96 for 95%).
- CLT makes this work **even for non-Gaussian data** (for large $n$).
- As $n \to \infty$, interval width shrinks like $1/\sqrt{n}$.

## Concepts introduced or reinforced
- [[maximum-likelihood-estimation]]
- [[unbiased-estimator]], [[consistent-estimator]], [[efficient-estimator]]
- [[confidence-interval]]
- [[sample-mean]] (reinforced — it is the MLE for Gaussian mean)

## Worked examples worth remembering
- MLE of exponential rate $\lambda$ from $n$ i.i.d. observations: $\hat\lambda = n / \sum x_i = 1/\bar x$.
- 95% CI for mean: $\bar x \pm 1.96\cdot\sigma/\sqrt{n}$.
