---
title: MAP Detection
type: concept
course: [[eee-350]]
tags: [bayesian, detection, map]
sources: [[slides-43.5-bayesian-inference]]
created: 2026-04-21
updated: 2026-04-26
---

# MAP Detection (Maximum A Posteriori)

## In one line
For a discrete unknown $\theta \in \{H_0, H_1, \ldots\}$, pick $\hat\theta = \arg\max_\theta p(\theta \mid x)$. Provably **minimizes the probability of error**.

## Example first — antipodal signaling over AWGN
Send $\theta \in \{+1, -1\}$. Receiver sees $X = \theta + N$ where $N \sim N(0, \sigma^2)$. Priors: $P(+1) = \pi_0$, $P(-1) = \pi_1$ (need not be equal).

Posterior ratio (likelihood $\times$ prior):
$$\frac{p(X | +1)\pi_0}{p(X | -1)\pi_1} = \frac{\exp(-(X - 1)^2/(2\sigma^2))\,\pi_0}{\exp(-(X + 1)^2/(2\sigma^2))\,\pi_1} \;\overset{H_0}{\underset{H_1}{\gtrless}}\; 1$$

Taking log and simplifying:
$$X \;\overset{H_0}{\underset{H_1}{\gtrless}}\; \frac{\sigma^2}{2}\ln\frac{\pi_1}{\pi_0}$$

So the MAP decision rule is: **threshold $X$ at $\tau = (\sigma^2/2)\cdot\ln(\pi_1/\pi_0)$** and declare $+1$ if $X > \tau$.

**Symmetric priors ($\pi_0 = \pi_1 = 0.5$):** $\tau = 0$ $\to$ threshold at zero. The classic "sign detector". When priors are uneven, the threshold **shifts toward the less-likely hypothesis** (harder to declare it).

## The rule
Given observation $X = x$:
$$\hat\theta_{MAP}(x) = \arg\max_\theta p(\theta | x) = \arg\max_\theta p(x | \theta)\, p(\theta)$$

(The denominator $p(x)$ doesn't depend on $\theta$, so it drops out of the argmax.)

## Why MAP minimizes P(error)

$P(\text{error} \mid X = x) = 1 - P(\text{correct} \mid x) = 1 - p(\hat\theta \mid x)$.

Maximizing $p(\hat\theta \mid x)$ over $\hat\theta$ = minimizing $P(\text{error} \mid x)$ pointwise for every $x$. Pointwise optimal $\to$ optimal overall.

$$P(\text{error}) = E_X[P(\text{error} | X)]$$

Since MAP is best for every $x$, averaging (integration over $x$) preserves optimality.

## Relation to MLE
- MAP: $\arg\max p(x \mid \theta)\cdot p(\theta)$. Uses likelihood **and** prior.
- MLE: $\arg\max p(x \mid \theta)$. Uses likelihood only.
- **Equal priors** (e.g. $P(H_0) = P(H_1) = 0.5$) $\to$ MAP reduces to **ML detection**, which maximizes the likelihood.

## Common mistakes
- **Forgetting the prior** — using MLE when MAP is called for. If priors differ, MAP's threshold shift can change answers a lot.
- **Taking argmax of the likelihood $\times$ prior without normalizing...** wait, actually that's fine. You can argmax the unnormalized posterior; normalization doesn't change the argmax.
- **Computing $p(\text{error})$ by integrating over $\theta$ instead of $x$.** The data integration is what matters for frequency-of-error.

## Related
- [[bayesian-inference]]
- [[detection-vs-estimation]]
- [[likelihood-ratio-test]]
- [[map-estimation]] — same idea for continuous $\theta$
- [[neyman-pearson-test]] — the no-prior cousin

## Practice
- [[inference-set-01]]
