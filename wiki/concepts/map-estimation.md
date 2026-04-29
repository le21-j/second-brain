---
title: MAP Estimation
type: concept
course: [[eee-350]]
tags: [bayesian, estimation, map]
sources: [[slides-43.5-bayesian-inference]]
created: 2026-04-21
updated: 2026-04-26
---

# MAP Estimation (Maximum A Posteriori)

## In one line
For a continuous unknown $\theta$, pick $\hat\theta = \arg\max_\theta p(\theta \mid x)$ — the **mode of the posterior**.

## Example first
$\theta$ is the underlying mean of Gaussian samples; observation $X \sim N(\theta, \sigma^2)$ with **prior** $\theta \sim N(\mu_0, \tau^2)$.

Posterior is Gaussian (nice property of the Gaussian–Gaussian combination):
$$p(\theta | X) \propto \exp\!\left(-\tfrac{1}{2\sigma^2}(X-\theta)^2\right) \cdot \exp\!\left(-\tfrac{1}{2\tau^2}(\theta - \mu_0)^2\right)$$

Completing the square, the posterior is $N(\mu_{post}, \sigma_{post}^2)$ with
$$\mu_{post} = \frac{\tau^2}{\sigma^2 + \tau^2}X + \frac{\sigma^2}{\sigma^2 + \tau^2}\mu_0$$

The MAP estimate (mode = mean for Gaussian) is this weighted average: data (weighted by prior variance $\tau^2$) plus prior mean (weighted by observation variance $\sigma^2$). When data is precise ($\sigma^2$ small), data dominates. When prior is strong ($\tau^2$ small), prior dominates.

## The rule

$$\hat\theta_{MAP}(x) = \arg\max_\theta p(\theta | x) = \arg\max_\theta p(x | \theta)\, p(\theta)$$

Equivalently (taking log): $\arg\max [\log\text{-likelihood} + \log\text{-prior}]$.

## vs. MLE
- **MLE:** $\arg\max \log p(x \mid \theta)$. No prior.
- **MAP:** $\arg\max [\log p(x \mid \theta) + \log p(\theta)]$. Adds the prior term.

If the prior is flat ($p(\theta) = \text{const}$), MAP = MLE. The prior acts as a **regularizer**, pulling the estimate toward regions of high prior.

This is why in ML:
- L2 regularization (weight decay) $\leftrightarrow$ Gaussian prior on weights $\to$ MAP estimate with Gaussian prior.
- L1 regularization (Lasso) $\leftrightarrow$ Laplace prior.

## vs. LMS / Posterior Mean
- **MAP:** mode of posterior.
- **LMS:** mean of posterior = $E[\theta \mid X]$.

For **symmetric unimodal** posteriors (like Gaussians), they coincide. For **skewed** posteriors, they differ.

## Connection to loss functions
- MAP minimizes **0–1 loss** (binary "are you exactly right"). Silly for continuous, but that's the formal relationship.
- **LMS** minimizes squared error. Usually the more useful metric.
- **Posterior median** minimizes absolute error.

So pick your estimator based on what kind of error you care about.

## Common mistakes
- **"MAP is optimal for estimation."** Only under 0–1 loss. Under MSE, LMS is optimal.
- **Using MAP when the posterior is multimodal.** You get just one mode — may miss the other. Reporting the full posterior is safer.

## Related
- [[bayesian-inference]]
- [[map-detection]]
- [[lms-estimation]]
- [[maximum-likelihood-estimation]]
