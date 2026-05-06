---
title: Posterior Distribution
type: concept
course:
  - "[[eee-350]]"
tags: [bayesian, posterior]
sources:
  - "[[slides-43.5-bayesian-inference]]"
created: 2026-04-21
updated: 2026-05-06
---

# Posterior Distribution

## In one line
$p(\theta | x)$ — your updated beliefs about $\theta$ **after** observing data $x$. Computed via Bayes' rule.

## Formula

$$p(\theta | x) = \frac{p(x | \theta) \, p(\theta)}{p(x)} = \frac{\text{likelihood} \times \text{prior}}{\text{evidence}}$$

The denominator $p(x) = \int p(x | \theta) \cdot p(\theta)\, d\theta$ is a normalizing constant.

In practice, you often work with the **unnormalized posterior** $p(x | \theta) \cdot p(\theta)$, then normalize at the end (or don't — for maximization, the constant doesn't matter).

## What you can extract from the posterior

- **Point estimates:**
  - **MAP:** $\hat\theta = \arg\max p(\theta | x)$. See [[map-detection]] / [[map-estimation]].
  - **Posterior mean:** $\hat\theta = E[\theta | X] = \int \theta \cdot p(\theta | x)\, d\theta$. See [[lms-estimation]].
  - **Posterior median:** the 50th percentile.
- **Interval estimates:**
  - **Credible interval:** interval $[a, b]$ with posterior mass $\geq 1 - \alpha$. Bayesian analog of [[confidence-interval]].
- **Predictions** for future data:
  - $p(x_{\text{new}} | x) = \int p(x_{\text{new}} | \theta) \cdot p(\theta | x)\, d\theta$. "Posterior predictive distribution."

## Relation to MLE
Bayesian posterior maximizer:
- $\text{MAP} = \arg\max [p(x | \theta) \cdot p(\theta)]$
- $\text{MLE} = \arg\max p(x | \theta)$

When the prior is **flat** (uniform), MAP = MLE. That's the connection: MLE is MAP with an uninformative prior.

## Common mistakes
- **Using posterior probabilities for testing without a prior.** Can't — need a prior to even have a posterior. Classical (non-Bayesian) hypothesis testing avoids this by using [[neyman-pearson-test]].
- **Interpreting MLE as a posterior.** MLE is not a posterior probability even under flat priors — it's a point where the likelihood is maximized.

## Related
- [[bayesian-inference]]
- [[prior-distribution]]
- [[map-detection]] / [[map-estimation]]
- [[lms-estimation]]
