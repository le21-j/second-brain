---
title: Detection vs Estimation
type: concept
course: [[eee-350]]
tags: [inference, detection, estimation]
sources: [[slides-43.5-bayesian-inference]]
created: 2026-04-21
updated: 2026-04-26
---

# Detection vs Estimation

## In one line
**Detection** = infer a discrete-valued $\theta$ (hypothesis testing). **Estimation** = infer a continuous-valued $\theta$. Same tools, different performance metrics.

## Example
- **Detection:** receiver decides whether a radar pulse is present ($\theta = 1$) or absent ($\theta = 0$). Error is binary: right or wrong.
- **Estimation:** same receiver estimates the precise range $\theta \in [0, 1000]$ meters. Error has **magnitude** — being off by 50 m is worse than being off by 5 m.

The math (Bayes' rule, MAP, etc.) is identical. What changes is **how you measure success**.

## Detection (discrete $\theta$)

- $\theta \in \{H_0, H_1, \ldots\}$ (finite or countable).
- Metric: **probability of error** $P(\hat\theta \neq \theta)$.
- Optimal rule (Bayesian): **MAP detector** $\hat\theta_{MAP} = \arg\max p(\theta \mid x)$. See [[map-detection]].
- Often reduced to a binary decision: **[[likelihood-ratio-test]]** or MAP thresholding.
- Classical (no prior) version: **[[neyman-pearson-test]]**.

## Estimation (continuous $\theta$)

- $\theta \in \mathbb{R}$ (or $\mathbb{R}^n$).
- Metric: **mean squared error** (MSE) $E[(\hat\theta - \theta)^2]$ is the most common, but could be MAE ($|\hat\theta - \theta|$) or anything else.
- Optimal rules (Bayesian):
  - MSE-optimal: **posterior mean** $\hat\theta = E[\theta \mid X]$. The [[lms-estimation|LMS / MMSE]] estimator.
  - MAE-optimal: posterior median.
  - 0/1-loss optimal: **[[map-estimation|MAP estimate]]** (posterior mode).
- Classical version: **[[maximum-likelihood-estimation|MLE]]**.

## Why the distinction matters
- **Error metrics differ.** "Probability of being wrong" makes sense only for discrete. For continuous, you're always wrong by some amount; "magnitude of wrong" is the question.
- **Optimal rules differ.** MAP detection is best for discrete; conditional mean (LMS) is best for continuous under MSE.
- **Information-theoretic capacity** in communications is split the same way: detection capacity for digital bits, estimation capacity (Cramér–Rao bound) for analog parameters.

## Hybrid cases
Real systems often mix:
- Estimate a continuous channel gain (estimation), then detect a transmitted bit (detection).
- ML problems: classification = detection; regression = estimation.

## Common mistakes
- **Using MSE for detection.** Doesn't make sense if $\theta$ is categorical (what's $(H_0 - H_1)^2$ mean?).
- **Using probability of error for estimation.** $P(\hat\theta = \theta)$ is 0 for continuous — you need magnitude.

## Related
- [[bayesian-inference]]
- [[map-detection]] — MAP for discrete case
- [[lms-estimation]] — MMSE for continuous case
- [[neyman-pearson-test]] — classical detection
- [[maximum-likelihood-estimation]] — classical estimation
