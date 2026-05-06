---
title: Slides 43.5 — Bayesian Inference
type: summary
source_type: slides
source_path: raw/slides/eee-350/43.5 Bayesian Inference.pptx
course:
  - "[[eee-350]]"
tags: [bayesian, map, lms, estimation, detection]
created: 2026-04-21
updated: 2026-05-06
---

# Slides 43.5 — Bayesian Inference

## TL;DR
In Bayesian inference, the unknown parameter $\theta$ is treated as a **random variable** with a **prior** distribution. Observe data $X$; compute the **posterior** $p(\theta | x)$ by Bayes' rule. Two cases: **$\theta$ discrete** $\to$ "detection" / hypothesis testing (**MAP detector** minimizes error probability); **$\theta$ continuous** $\to$ "estimation" (**MAP** or **LMS** = conditional mean). In the Gaussian case, LMS is **linear** in the observation and equals MAP.

## Key takeaways
- **Bayes' rule** (the backbone):
  $$p(\theta | x) = \frac{p(x | \theta)\, p(\theta)}{p(x)}$$
  Prior $\times$ likelihood / evidence.
- **Detection vs Estimation:**
  - $\theta$ discrete $\to$ detection / hypothesis testing. Success metric: $P(\text{error})$.
  - $\theta$ continuous $\to$ estimation. Success metric: MSE, or $P(|\hat\theta - \theta| > \varepsilon)$.
- **MAP detection / estimation:** $\hat\theta_{\text{MAP}} = \arg\max_\theta p(\theta | x)$. Equivalently $\arg\max_\theta p(x | \theta)\cdot p(\theta)$.
- **MAP minimizes probability of error** in the discrete case — the key theorem.
- **LMS estimation** (aka MMSE): $\hat\theta = E[\theta | X]$. Minimizes expected squared error.
- **Gaussian miracle:** if $(\theta, X)$ is jointly Gaussian, $E[\theta | X]$ is **linear in $X$** — and equals the MAP estimate. The slides' favorite example: antipodal signaling $X = \theta + \text{noise}$, where $\theta \in \{+1, -1\}$ under unequal priors.
- **AWGN antipodal example:** MAP detector thresholds $X$ at a point determined by noise variance and prior ratio.

## Concepts introduced or reinforced
- [[bayesian-inference]]
- [[prior-distribution]] / [[posterior-distribution]]
- [[detection-vs-estimation]]
- [[map-detection]] / [[map-estimation]]
- [[lms-estimation]]
- [[antipodal-signaling]] (communications-flavored example)

## Worked examples worth remembering
- **MAP detection of antipodal signal under AWGN with unequal priors:** derive the threshold on $X$ that decides $\theta = +1$ vs $-1$.
- **LMS for jointly Gaussian $(\theta, X)$:** $\hat\theta = \mu_\theta + (\sigma_{\theta X}/\sigma_X^2)(X - \mu_X)$ — exactly the regression line.
