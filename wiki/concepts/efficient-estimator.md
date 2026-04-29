---
title: Efficient Estimator
type: concept
course: [[eee-350]]
tags: [estimator, cramer-rao]
sources: [[slides-44-mle-ci]]
created: 2026-04-21
updated: 2026-04-26
---

# Efficient Estimator

## In one line
Among **unbiased** estimators, the one with the **smallest variance** is called efficient. Lower bound on variance is the **Cramér-Rao Bound** (CRB).

## The Cramér-Rao Bound

For any unbiased estimator $\hat\theta$ of $\theta$:
$$\text{Var}(\hat\theta) \ge \frac{1}{I(\theta)}$$

where $I(\theta)$ is the **Fisher information**:
$$I(\theta) = E\!\left[\left(\frac{\partial}{\partial\theta}\log p(X | \theta)\right)^2\right] = -E\!\left[\frac{\partial^2}{\partial\theta^2}\log p(X | \theta)\right]$$

(Equivalence of the two formulas holds under regularity.)

- For $n$ i.i.d. samples: $I_n(\theta) = n\cdot I_1(\theta)$. CRB: $\text{Var}(\hat\theta) \geq 1/(n\cdot I_1(\theta))$.

## Example — Gaussian mean
$X_i$ i.i.d. $\sim N(\mu, \sigma^2)$. Fisher info per sample: $I_1(\mu) = 1/\sigma^2$. So CRB for $n$ samples:
$$\text{Var}(\hat\mu) \ge \frac{\sigma^2}{n}$$
Sample mean achieves this ($\text{Var}(\bar x) = \sigma^2/n$). So **$\bar x$ is efficient** for Gaussian mean.

## Why this matters
- Efficiency sets an **absolute limit** on how well you can estimate: no unbiased method does better.
- **MLE is asymptotically efficient:** for large $n$, $\text{Var}(\text{MLE}) \approx \text{CRB}$. That's why MLE is the default.
- In communications: **Cramér-Rao** bounds the precision of time-of-arrival, carrier phase, etc. estimators.

## Common mistakes
- Applying CRB to biased estimators. The standard CRB is for unbiased only (there's a more general biased CRB).
- Forgetting to **multiply $I_1$ by $n$** for i.i.d. samples.

## Related
- [[unbiased-estimator]]
- [[maximum-likelihood-estimation]]
