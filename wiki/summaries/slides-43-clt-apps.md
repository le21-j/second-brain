---
title: Slides 43 — Central Limit Theorem and Applications
type: summary
source_type: slides
source_path: raw/slides/eee-350/43 CLT and Apps.pptx
course:
  - "[[eee-350]]"
tags: [clt, binomial, continuity-correction, asymptotic]
created: 2026-04-21
updated: 2026-05-06
---

# Slides 43 — Central Limit Theorem

## TL;DR
The **Central Limit Theorem:** for i.i.d. $X_i$ with finite mean $\mu$ and variance $\sigma^2$, the **standardized sum** $Z_n = (S_n - n\mu)/(\sigma\sqrt{n})$ converges in distribution to a standard normal $N(0, 1)$ — **regardless** of the shape of the original distribution. Profoundly useful: lets you compute tail probabilities for almost any sum using a table of $\Phi$. Applied to polling (tighter than Chebyshev), binomial approximation (with **continuity correction** $\pm 0.5$).

## Key takeaways
- **CLT:** for i.i.d. $X_i$ with finite $\mu, \sigma^2$,
  $$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)$$
- "Different scalings of the sum":
  - Just $S_n$: blows up with $n$ (variance $= n\sigma^2$).
  - $S_n/n$ (sample mean): concentrates at $\mu$ (variance $\to 0$). This is WLLN.
  - $(S_n - n\mu)/(\sigma\sqrt{n})$: stays a "unit-variance fluctuation" — this is the CLT scaling.
- **Polling via CLT:** $P(|\bar X_n - p| < \varepsilon) \approx 2\Phi(\varepsilon\sqrt{n}/\sigma) - 1$. Invert to get required $n$ for confidence $1 - \delta$. Much tighter than Chebyshev's bound.
- **Binomial$(n, p) \approx N(np, np(1-p))$** for moderate-to-large $n$.
- **Continuity correction:** when approximating $P(X \leq k)$ for discrete $X$ by CLT, use $P(X \leq k + 0.5)$ instead. Small shift, meaningful accuracy gain.
  - Slides' example: "change 21 to 21.5".

## Concepts introduced or reinforced
- [[central-limit-theorem]]
- [[binomial-via-clt]]
- [[continuity-correction]]
- [[standard-normal-table]]

## Worked examples worth remembering
- Polling with CLT: "how many voters needed for $\pm 1\%$ at 95%" $\to n \approx (1.96/0.01)^2 \cdot \sigma^2$ using $\sigma^2 \leq 1/4$ (max of $p(1-p)$).
- Binomial approximation with continuity correction — the recurring "21 $\to$ 21.5" pattern.
