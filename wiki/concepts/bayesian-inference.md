---
title: Bayesian Inference
type: concept
course: [[eee-350]]
tags: [bayesian, prior, posterior, inference]
sources: [[slides-43.5-bayesian-inference]]
created: 2026-04-21
updated: 2026-04-26
---

# Bayesian Inference

## In one line
Treat the unknown parameter $\theta$ as a **random variable** with a **prior** distribution. After observing data $x$, use Bayes' rule to compute the **posterior** $p(\theta | x)$. All inference flows from the posterior.

## Example first
You're pulling a coin out of a bag. You're told 80% of coins in the bag are fair ($p = 0.5$), 20% are biased ($p = 0.7$). You flip it 10 times and get 8 heads. Is it fair?

**Prior:** $P(\text{fair}) = 0.8$, $P(\text{biased}) = 0.2$.

**Likelihood:** $P(8 \text{ heads in 10} | \text{fair}) = \binom{10}{8} \cdot 0.5^8 \cdot 0.5^2 \approx 0.044$. $P(8 | \text{biased}) = \binom{10}{8} \cdot 0.7^8 \cdot 0.3^2 \approx 0.233$.

**Posterior** by Bayes:
- Numerator (fair) $= 0.044 \cdot 0.8 = 0.0352$.
- Numerator (biased) $= 0.233 \cdot 0.2 = 0.0466$.
- Normalize: $P(\text{fair} | \text{data}) = 0.0352 / (0.0352 + 0.0466) \approx$ **$43\%$**.

Prior said 80% fair; after observing 8 heads, posterior drops to 43%. Evidence updated belief.

## The framework
Three ingredients:
- **Prior** $p(\theta)$: what you believe about $\theta$ before seeing data.
- **Likelihood** $p(x | \theta)$: how data is distributed given $\theta$. ("The model.")
- **Posterior** $p(\theta | x)$: what you believe about $\theta$ after seeing data.

**Bayes' rule:**
$$p(\theta | x) = \frac{p(x | \theta)\, p(\theta)}{p(x)} = \frac{\text{likelihood} \times \text{prior}}{\text{evidence}}$$

The denominator $p(x) = \int p(x | \theta) \cdot p(\theta)\, d\theta$ is a normalization constant ensuring the posterior integrates to 1. Often you just compute the unnormalized posterior $p(x | \theta) \cdot p(\theta)$ and normalize at the end.

## Detection vs Estimation
Two cases depending on the nature of $\theta$:

| $\theta$ type | Framework name | Error metric |
|---|---|---|
| **Discrete** (e.g. $\theta \in \{H_0, H_1\}$) | **Detection / hypothesis testing** | $P(\text{error})$ |
| **Continuous** ($\theta \in \mathbb{R}$) | **Estimation** | MSE, etc. |

See [[detection-vs-estimation]].

## Producing a single answer
The posterior is the whole answer, but sometimes you need one number:

- **MAP estimate:** $\hat\theta_{\text{MAP}} = \arg\max_\theta p(\theta | x)$. The mode of the posterior. In detection, this **minimizes $P(\text{error})$**.
- **Posterior mean (LMS/MMSE):** $\hat\theta_{\text{LMS}} = E[\theta | X]$. Minimizes mean squared error.
- **Median, quantiles:** depending on loss function.

For **jointly Gaussian** $(\theta, X)$, all three coincide and are **linear** in $X$.

## Contrast with classical (frequentist) statistics
| | Bayesian | Classical (MLE) |
|---|---|---|
| Is $\theta$ random? | Yes (prior distribution) | No (fixed but unknown) |
| Key identity | Bayes' rule | Maximize likelihood |
| Output | Posterior distribution | Point estimate / interval |
| Uses prior info? | Yes, explicitly | Not directly (sometimes via regularization) |

See [[maximum-likelihood-estimation]] for the classical counterpart.

## Common mistakes
- **Confusing $p(x | \theta)$ with $p(\theta | x)$.** They're related by Bayes' rule but wildly different in value.
- **Thinking priors "bias" the answer.** They *incorporate* prior information. As data grows, the likelihood dominates and the prior becomes irrelevant.
- **Using "the posterior probability of the data" instead of "posterior of $\theta$".** The posterior is always of the unknown parameter, not the data.

## Related
- [[prior-distribution]]
- [[posterior-distribution]]
- [[map-detection]]
- [[map-estimation]]
- [[lms-estimation]]
- [[detection-vs-estimation]]
- [[maximum-likelihood-estimation]]

## Practice
- [[inference-set-01]]
