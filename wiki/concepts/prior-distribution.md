---
title: Prior Distribution
type: concept
course:
  - "[[eee-350]]"
tags: [bayesian, prior]
sources:
  - "[[slides-43.5-bayesian-inference]]"
created: 2026-04-21
updated: 2026-05-06
---

# Prior Distribution

## In one line
$p(\theta)$ — your beliefs about the unknown parameter **before** seeing any data.

## Example first
A detector receives antipodal signals $\theta \in \{+1, -1\}$. History says $+1$ is sent 70% of the time, $-1$ sent 30%. So:
$$p(\theta = +1) = 0.7, \quad p(\theta = -1) = 0.3$$
That's the prior. It lives in your head before any measurement arrives.

## The idea
In Bayesian inference, every unknown has a prior. Types:
- **Uniform / flat:** $p(\theta) \propto 1$. "All values equally likely." Common default.
- **Conjugate:** chosen so the posterior has the same family form as the prior (e.g. Beta prior + Binomial likelihood $\to$ Beta posterior).
- **Informative:** encodes strong domain knowledge.
- **Hierarchical:** the prior itself has parameters with their own prior (useful for complex models).

## Effect on posterior
- **Strong prior (narrow):** posterior is heavily influenced by prior, even with moderate data.
- **Weak prior (broad):** data dominates.
- **As $n \to \infty$:** posterior concentrates around the MLE regardless of prior (assuming prior doesn't rule out the truth).

## Common mistakes
- Treating an uninformative prior as "no assumption". Even a flat prior is an assumption — it says "no value is more likely a priori".
- Using the data to pick the prior (double-dipping). Should be chosen before seeing data.

## Related
- [[bayesian-inference]]
- [[posterior-distribution]]
