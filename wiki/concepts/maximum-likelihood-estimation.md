---
title: Maximum Likelihood Estimation (MLE)
type: concept
course: [[eee-350]]
tags: [mle, estimator, classical-statistics]
sources: [[slides-44-mle-ci]], [[slides-46-regression]]
created: 2026-04-21
updated: 2026-04-26
---

# Maximum Likelihood Estimation (MLE)

## In one line
Pick $\hat\theta$ that **maximizes the likelihood** $p(x \mid \theta)$ — "the parameter value that makes the observed data most probable".

## Example first — MLE for Gaussian mean
Observe $X_1, \ldots, X_n$ i.i.d. $\sim N(\mu, \sigma^2)$ with $\sigma^2$ known. Find MLE of $\mu$.

Likelihood:
$$L(\mu) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\tfrac{1}{2\sigma^2}(x_i - \mu)^2\right)$$

Log-likelihood (easier to work with):
$$\ell(\mu) = -\tfrac{n}{2}\log(2\pi\sigma^2) - \tfrac{1}{2\sigma^2}\sum_i (x_i - \mu)^2$$

Differentiate w.r.t. $\mu$ and set to zero:
$$\frac{\partial\ell}{\partial\mu} = \frac{1}{\sigma^2}\sum_i (x_i - \mu) = 0$$

Solve: **$\hat\mu = \bar x$** = sample mean. Clean result: MLE of Gaussian mean is the sample mean.

## The framework
- **Likelihood:** $L(\theta) = p(x \mid \theta)$ viewed as a function of $\theta$ for **fixed** $x$.
- **Log-likelihood:** $\ell(\theta) = \log L(\theta)$. Easier to differentiate (products $\to$ sums).
- **MLE:** $\hat\theta = \arg\max \ell(\theta)$.

For i.i.d. data:
$$\ell(\theta) = \sum_{i=1}^n \log p(x_i | \theta)$$

## MLE of common distributions

| Distribution | Parameter | MLE |
|---|---|---|
| $N(\mu, \sigma^2)$ | $\mu$ | $\bar x$ (sample mean) |
| $N(\mu, \sigma^2)$ | $\sigma^2$ | $(1/n) \sum(x_i - \bar x)^2$ — biased! |
| $\text{Exp}(\lambda)$ | $\lambda$ | $1/\bar x$ |
| $\text{Bernoulli}(p)$ | $p$ | $\bar x$ (sample proportion) |
| $\text{Uniform}(0, \theta)$ | $\theta$ | $\max(x_i)$ |
| $\text{Poisson}(\lambda)$ | $\lambda$ | $\bar x$ |

## Important note on Gaussian $\sigma^2$ MLE
MLE of variance is $(1/n) \sum(x_i - \bar x)^2$. This is **biased**: $E[\hat\sigma^2_{MLE}] = ((n-1)/n)\cdot\sigma^2 < \sigma^2$. Using $(n-1)$ instead of $n$ gives the **unbiased** sample variance. When $n$ is large, the difference is negligible.

This is one of the classic MLE quirks: MLE isn't automatically unbiased.

## Properties of MLE (asymptotic)

For well-behaved models as $n \to \infty$:
- **Consistent:** $\hat\theta_{MLE} \to \theta$ in probability (correct value in the limit).
- **Asymptotically normal:** $\sqrt{n}(\hat\theta_{MLE} - \theta) \to N(0, I(\theta)^{-1})$ where $I(\theta)$ is the **Fisher information**.
- **Asymptotically efficient:** achieves the Cramér-Rao lower bound — no unbiased estimator has smaller asymptotic variance.

## Contrast with MAP
| | MLE | MAP |
|---|---|---|
| Uses prior? | No | Yes |
| Maximizes | $p(x \mid \theta)$ | $p(\theta \mid x) = p(x \mid \theta)\cdot p(\theta) / p(x)$ |
| Limit of large $n$ | Converges to true $\theta$ | Converges to MLE (prior washed out) |
| Flat prior | — | = MLE |

## Common mistakes
- **Forgetting to take logs.** Products of many probabilities underflow; log-likelihood is the computational workhorse.
- **Assuming MLE is unbiased.** Often it isn't. Gaussian $\sigma^2$ MLE is a classic example.
- **Using MLE without checking the critical point is a maximum** (could be a minimum or saddle). Check the second derivative.
- **Boundary issues.** MLE might be on the boundary (e.g. $\text{Uniform}(0, \theta)$ MLE is $\max(x_i)$, not an interior critical point).

## Related
- [[bayesian-inference]] — the alternative framework
- [[map-estimation]]
- [[unbiased-estimator]]
- [[consistent-estimator]]
- [[efficient-estimator]]
- [[confidence-interval]]
- [[linear-regression]] (least-squares is MLE under Gaussian noise)

## Practice
- [[inference-set-01]]
