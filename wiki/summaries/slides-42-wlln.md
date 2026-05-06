---
title: Slides 42 — Weak Law of Large Numbers
type: summary
source_type: slides
source_path: raw/slides/eee-350/42 WLLN.pptx
course:
  - "[[eee-350]]"
tags: [wlln, sample-mean, convergence]
created: 2026-04-21
updated: 2026-05-06
---

# Slides 42 — Weak Law of Large Numbers (WLLN)

## TL;DR
If $X_1, X_2, \ldots$ are i.i.d. with finite mean $\mu$ and variance $\sigma^2$, then the **sample mean** $\bar X_n = (X_1+\ldots+X_n)/n$ converges to $\mu$ **in probability**. Proof is a one-line Chebyshev argument. The slides caution about the Gambler's Fallacy, mention the Strong LLN briefly (different convergence type), relax the independence assumption (works with bounded covariance), and apply the result to **polling** — "how many people should we poll for an election?".

## Key takeaways
- **WLLN:** $\bar X_n \to \mu$ in probability, i.e. $P(|\bar X_n - \mu| \geq \varepsilon) \to 0$.
- **Proof sketch (1 line):** $\text{Var}(\bar X_n) = \sigma^2/n \to 0$; apply Chebyshev.
- **Gambler's Fallacy:** LLN does **not** mean "if I got heads five times in a row, tails is due next". Each toss is independent; LLN is about the long-run *average*, not short-run compensation.
- **SLLN** (Strong): same limit but almost-sure convergence, stronger concept — not covered here.
- LLN doesn't need strict independence: bounded pairwise covariances (e.g. moving-average of independent Gaussians) also work, as long as $\text{Var}(\bar X_n) \to 0$.
- **Extreme failure case:** if all $X_i = X$ (perfectly correlated), $\bar X_n = X$ forever — no convergence to $\mu$.
- **Polling application:** to estimate true fraction $p = P(\text{vote for A})$ within $\varepsilon$ with probability $\geq 1 - \delta$, you need $n$ on the order of $\sigma^2/(\varepsilon^2\cdot\delta)$ samples by Chebyshev. CLT gives a tighter $n$ (covered in deck 43).

## Concepts introduced or reinforced
- [[weak-law-of-large-numbers]]
- [[sample-mean]] (briefly — gets deeper treatment in slides 46.5)
- [[gamblers-fallacy]]

## Worked examples worth remembering
- Dice roll average (cartoon in slides) — the average roll of a fair die stabilizes around 3.5.
- Polling: "how many voters to poll for 1% accuracy with 95% confidence?"
