---
title: Slides 46 — Regression
type: summary
source_type: slides
source_path: raw/slides/eee-350/46 Regression.pptx
course: [[eee-350]]
tags: [regression, least-squares, power-law, mle]
created: 2026-04-21
updated: 2026-04-26
---

# Slides 46 — Regression

## TL;DR
Linear regression models data as **$y_i = a\cdot x_i + b + \varepsilon_i$** with i.i.d. Gaussian noise $\varepsilon_i$. Taking the log-likelihood under Gaussian noise yields the **least-squares** criterion — so LS isn't arbitrary, it's the MLE under Gaussian noise. Covers non-linear extensions by basis change or log-transforming variables. Concrete wireless-comms application: estimating the **path-loss exponent** in a power-law model $y = a\cdot x^{-\alpha}$ by taking logs.

## Key takeaways
- **Model:** $y_i = a\cdot x_i + b + \varepsilon_i$, $\varepsilon_i$ i.i.d. $\sim N(0, \sigma^2)$. Parameters: $a, b$.
- **Likelihood:** $\prod (1/\sqrt{2\pi\sigma^2}) \exp(-(y_i - a\cdot x_i - b)^2/(2\sigma^2))$.
- **Log-likelihood:** $-(1/(2\sigma^2))\cdot \sum (y_i - a\cdot x_i - b)^2 + \text{const}$.
- Maximizing log-likelihood $\iff$ **minimizing $\sum (y_i - a\cdot x_i - b)^2$** = least-squares objective.
- LS also comes from "common sense" (penalize errors) — Gaussian noise is the probabilistic justification.
- **Closed-form LS solution:**
  $$\hat a = \frac{\sum(x_i - \bar x)(y_i - \bar y)}{\sum(x_i - \bar x)^2}, \quad \hat b = \bar y - \hat a\,\bar x$$
  i.e. $\hat a$ = sample covariance / sample variance of $x$.
- **Variations:** non-linear basis functions (polynomial regression), log-transforming $x$ or $y$.
- **Power law:** $y = a\cdot x^\alpha$ with multiplicative noise. Take logs $\to \log y = \log a + \alpha\cdot \log x + \varepsilon_{\log}$, which is linear in log-coordinates. Fit $\alpha, a$ by LS on $(\log x, \log y)$.
- **Path-loss exponent:** wireless received power falls as $P_r \propto d^{-\alpha}$; estimating $\alpha$ from noisy measurements at known distances is exactly this log-log fit.

## Concepts introduced or reinforced
- [[linear-regression]]
- [[least-squares]]
- [[power-law-regression]]
- [[maximum-likelihood-estimation]] (reinforced — LS = MLE under Gaussian noise)

## Worked examples worth remembering
- Fit a line to $(x_i, y_i)$ data — closed-form $\hat a, \hat b$.
- Path-loss: estimate $\alpha$ from received-power measurements at varying distances.
