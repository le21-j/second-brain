---
title: Example — How Many Voters to Poll?
type: example
course:
  - "[[eee-350]]"
tags: [polling, clt, chebyshev, sample-size]
sources:
  - "[[slides-42-wlln]]"
  - "[[slides-43-clt-apps]]"
created: 2026-04-21
updated: 2026-05-06
---

# Example — Sample Size for Polling

## Problem
You want to estimate the true fraction $p$ of voters supporting candidate A. You'll poll $n$ random voters and use the sample proportion $\hat p = \bar X_n$ as your estimate. How large must $n$ be so that $P(|\hat p - p| < 0.03) \geq 0.95$ (i.e. within 3 percentage points, 95% of the time)?

## Setup
Each $X_i \in \{0, 1\}$ i.i.d. with $P(X_i = 1) = p$. Then:
- $E[X_i] = p$.
- $\text{Var}(X_i) = p(1 - p)$.
- $\text{Var}(\bar X_n) = p(1 - p)/n$.
- $\sigma_X = \sqrt{p(1 - p)}$.

The worst case variance (to guarantee for any $p$): $p(1 - p) \leq 1/4$ at $p = 1/2$. We'll use this for a distribution-free bound.

## Method 1 — Chebyshev (loose)

$$P(|\hat p - p| \ge 0.03) \le \frac{\text{Var}(\hat p)}{(0.03)^2} \le \frac{1/(4n)}{0.0009} = \frac{1}{0.0036\,n}$$

Set $\leq 0.05$:
$$n \ge \frac{1}{0.0036 \cdot 0.05} = \frac{1}{0.00018} \approx 5556$$

Chebyshev says **~5600 voters** suffice.

## Method 2 — CLT (tight)

By CLT, $(\hat p - p)/\sqrt{p(1-p)/n} \approx \mathcal{N}(0, 1)$. So:
$$P(|\hat p - p| < 0.03) \approx P\!\left(|Z| < 0.03\sqrt{n/(p(1-p))}\right) = 2\Phi\!\left(0.03\sqrt{n/(p(1-p))}\right) - 1$$

Set $= 0.95$: $2\Phi(\cdot) - 1 = 0.95 \implies \Phi(\cdot) = 0.975 \implies$ argument $= 1.96$.

$$0.03\sqrt{n/(p(1-p))} = 1.96 \implies n = \frac{(1.96)^2\cdot p(1-p)}{(0.03)^2}$$

Worst case $p(1 - p) = 1/4$:
$$n = \frac{3.8416 \cdot 0.25}{0.0009} \approx \boxed{1067}$$

CLT says **~1068 voters** suffice. That's why real political polls use ~1000 — CLT, not Chebyshev.

## Why the huge gap?
Chebyshev makes **no distributional assumption**; CLT **exploits** the shape of the Bernoulli sum (approximately Gaussian). Gaussian tails drop much faster than $1/k^2$.

## The formula for general margin $\varepsilon$ and confidence $1 - \alpha$

$$n \approx \left(\frac{z_{\alpha/2}}{\varepsilon}\right)^2 \cdot p(1-p) \;\;\le\;\; \left(\frac{z_{\alpha/2}}{\varepsilon}\right)^2 \cdot \tfrac{1}{4}$$

| Margin $\varepsilon$ | Confidence | $z$ | $n_{\min}$ (worst-case) |
|---|---|---|---|
| 3% | 95% | 1.96 | 1067 |
| 1% | 95% | 1.96 | 9604 |
| 3% | 99% | 2.576 | 1843 |
| 5% | 95% | 1.96 | 385 |

Doubling precision needs 4× the data (inverse-square law of sample size).

## Related
- [[weak-law-of-large-numbers]]
- [[chebyshev-inequality]]
- [[central-limit-theorem]]
- [[confidence-interval]]
- [[standard-normal-table]]
