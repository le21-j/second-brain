---
title: Inference (Formula)
type: formula
course: [[eee-350]]
tags: [inference, bayesian, mle, hypothesis-testing]
sources: [[slides-43.5-bayesian-inference]], [[slides-44-mle-ci]], [[slides-45-neyman-pearson]]
created: 2026-04-21
updated: 2026-04-26
---

# Inference — Formula Sheet

## Bayes' rule (core identity)

$$p(\theta | x) = \frac{p(x | \theta)\, p(\theta)}{p(x)}$$

## MAP detection / estimation

$$\hat\theta_{MAP} = \arg\max_\theta\, p(\theta | x) = \arg\max_\theta\, p(x | \theta)\, p(\theta)$$

**MAP detection minimizes $P(\text{error})$** for discrete $\theta$.

### Antipodal signaling MAP threshold
For $\theta \in \{+1, -1\}$ with priors $\pi_0, \pi_1$, observation $X = \theta + N$ where $N \sim N(0, \sigma^2)$:
$$\tau = \frac{\sigma^2}{2}\ln\frac{\pi_1}{\pi_0}$$
Decide $+1$ if $X > \tau$.

## LMS (MMSE) estimation

$$\hat\theta_{LMS} = E[\theta | X]$$

**MSE of LMS:** $E[\text{Var}(\theta | X)]$.

### Gaussian LMS (linear in $X$)
$$\hat\theta_{LMS}(X) = \mu_\theta + \rho\,\frac{\sigma_\theta}{\sigma_X}(X - \mu_X)$$
$$\text{MSE} = \sigma_\theta^2(1 - \rho^2)$$

## Maximum Likelihood

$$\hat\theta_{MLE} = \arg\max_\theta\, p(x | \theta) = \arg\max_\theta\, \sum_i \log p(x_i | \theta)$$

Common MLEs:
- Gaussian mean ($\sigma$ known): $\bar x$
- Gaussian variance ($\mu$ known): $(1/n) \sum(x_i - \mu)^2$ — biased!
- Gaussian variance ($\mu$ unknown): $(1/n) \sum(x_i - \bar x)^2$ — biased; use $1/(n-1)$ for unbiased
- $\text{Exp}(\lambda)$: $1/\bar x$
- $\text{Bernoulli}(p)$: $\bar x$ (sample proportion)
- $\text{Poisson}(\lambda)$: $\bar x$

## Confidence interval (Gaussian mean, $\sigma$ known)

$$\bar X_n \pm z_{\alpha/2}\cdot\frac{\sigma}{\sqrt{n}}$$

## Critical values

| Confidence | Two-sided $z$ | One-sided $z$ |
|---|---|---|
| 90% | 1.645 | 1.282 |
| 95% | 1.96 | 1.645 |
| 99% | 2.576 | 2.326 |

## Neyman-Pearson LRT

$$\Lambda(x) = \frac{p(x | H_1)}{p(x | H_0)} > \gamma \implies \text{reject } H_0$$

$\gamma$ set so $P(\Lambda > \gamma | H_0) = \alpha$ (significance level).

### Test of Gaussian mean (one-sided $H_0: \mu = \mu_0$ vs $H_1: \mu > \mu_0$)
Reject $H_0$ if:
$$\bar x > \mu_0 + z_\alpha\cdot\frac{\sigma}{\sqrt{n}}$$

### Test of variance ($\chi^2$ test)
Under $H_0$ ($\sigma^2 = \sigma_0^2$, mean $\mu$ known):
$$T = \sum_i \frac{(x_i - \mu)^2}{\sigma_0^2} \sim \chi^2(n)$$
If mean is estimated, d.f. $= n - 1$.

## Linear regression LS

$$\hat a = \frac{\sum(x_i - \bar x)(y_i - \bar y)}{\sum(x_i - \bar x)^2} = \frac{s_{XY}}{s_X^2}$$
$$\hat b = \bar y - \hat a\,\bar x$$

## Related
- [[bayesian-inference]]
- [[maximum-likelihood-estimation]]
- [[confidence-interval]]
- [[neyman-pearson-test]]
- [[standard-normal-table]]
