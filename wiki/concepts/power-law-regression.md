---
title: Power-Law Regression (Log-Log Fit)
type: concept
course:
  - "[[eee-350]]"
tags: [regression, power-law, log-transform, wireless]
sources:
  - "[[slides-46-regression]]"
created: 2026-04-21
updated: 2026-05-06
---

# Power-Law Regression (Log-Log Fit)

## In one line
For data that follows $y = a\cdot x^\alpha$, take logs: $\log y = \log a + \alpha\cdot\log x$ — now it's linear in $(\log x, \log y)$, and standard LS fits $\alpha$ and $\log a$.

## Example first — path-loss exponent in wireless comms
Received power at distance $d$ typically decays as $P_r \propto d^{-\alpha}$, with $\alpha \approx 2$ in free space, 3–5 in urban environments. You measure $P_r$ at distances $d_1, \ldots, d_n$ and want to estimate $\alpha$.

Take logs: $\log P_r = \log K - \alpha\cdot\log d$. Define $y_i = \log(P_{r,i})$ and $x_i = \log(d_i)$; fit $y = \beta_0 + \beta_1\cdot x$ by standard LS. Then:
- $\hat\alpha = -\hat\beta_1$
- $\hat K = \exp(\hat\beta_0)$

With a few noisy measurements you can estimate **path-loss exponent** that drives link-budget calculations.

## The method

Given $y_i = a\cdot x_i^\alpha \cdot \text{multiplicative noise}$:
$$\log y_i = \log a + \alpha \log x_i + \log(\text{noise})$$

Assume $\log(\text{noise}) \sim N(0, \sigma^2)$ (equivalently, multiplicative noise is log-normal). Then standard linear regression in the **log-space** is MLE.

## Key subtlety — noise model matters

**Additive noise in original scale** ($y = a\cdot x^\alpha + \varepsilon$): log transform changes the noise structure, and LS in log-space is **not** MLE. Still often a reasonable heuristic, but don't overinterpret CI's.

**Multiplicative noise** ($y = a\cdot x^\alpha \cdot \eta$ with $\log \eta$ Gaussian): log-LS is exactly MLE. Clean.

## When to log-transform

| Relationship | Transform |
|---|---|
| $y = a\cdot x^\alpha$ (power law) | log both |
| $y = a\cdot e^{bx}$ (exponential) | log $y$ only |
| $y = a\cdot \log(x) + b$ (logarithmic) | log $x$ only |
| $y = a/x + b$ (reciprocal) | $1/x$ |

Always look at a **log-log plot** when you suspect a power law. Straight line $\to$ log-log $\to$ linear fit. Curved line $\to$ not a power law, look elsewhere.

## Common mistakes
- **Forgetting the sign** on $\alpha$ when the relationship is decreasing ($y \propto x^{-\alpha}$).
- **Interpreting confidence intervals in log-space as if they're in original space.** Back-transform carefully (and CIs become asymmetric).
- **Fitting power-law when a line would do.** Don't log-transform for its own sake.

## Related
- [[linear-regression]]
- [[least-squares]]
