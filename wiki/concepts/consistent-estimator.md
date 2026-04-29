---
title: Consistent Estimator
type: concept
course: [[eee-350]]
tags: [estimator, consistency, asymptotic]
sources: [[slides-44-mle-ci]]
created: 2026-04-21
updated: 2026-04-26
---

# Consistent Estimator

## In one line
$\hat\theta_n$ is **consistent** for $\theta$ if $\hat\theta_n \to \theta$ **in probability** as $n \to \infty$.

## Example
- Sample mean is consistent for $\mu$ by [[weak-law-of-large-numbers|WLLN]].
- Both the biased ($1/n$) and unbiased ($1/(n-1)$) sample variance are consistent: as $n \to \infty$, they both converge to $\sigma^2$.

## The idea
You can be biased at finite $n$ but still get arbitrarily close to the truth as data accumulates. "Consistent" = no asymptotic bias + variance shrinks to 0.

Equivalent condition: if **bias $\to 0$ AND variance $\to 0$** as $n \to \infty$, estimator is consistent. Proof via Markov: $P(|\hat\theta_n - \theta| \geq \varepsilon) \leq \text{MSE}(\hat\theta_n)/\varepsilon^2 = (\text{bias}^2 + \text{var})/\varepsilon^2 \to 0$.

## Unbiased vs consistent

| | Unbiased | Biased but consistent | Biased and inconsistent |
|---|---|---|---|
| $E[\hat\theta_n]$ | $= \theta$ always | $\to \theta$ as $n \to \infty$ | stays off |
| Converges to $\theta$? | Not guaranteed | Yes | No |

You want **consistent** — an estimator that converges to the truth with enough data. Unbiasedness is nice-to-have but not essential.

## Common mistakes
- **Confusing consistency with unbiasedness.** They're different asymptotic properties. An estimator can be:
  - Unbiased but inconsistent (rare, but possible if variance doesn't shrink).
  - Biased but consistent (most MLEs after tiny bias correction).
  - Both (ideal).

## Related
- [[unbiased-estimator]]
- [[maximum-likelihood-estimation]]
- [[weak-law-of-large-numbers]]
- [[convergence-in-probability]]
