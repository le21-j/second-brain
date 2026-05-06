---
title: Slides 40 — Conditional Expectation of One RV Given Another
type: summary
source_type: slides
source_path: raw/slides/eee-350/40 Conditional Expectation of one RV given another.pptx
course:
  - "[[eee-350]]"
tags: [conditional-expectation, iterated-expectations, law-of-total-variance]
created: 2026-04-21
updated: 2026-05-06
---

# Slides 40 — Conditional Expectation

## TL;DR
**$E[X|Y]$ is a random variable** (a function of $Y$), not a number. This is the slide's central idea. Once you accept that, you get a toolkit: **iterated expectations** $E[E[X|Y]] = E[X]$, **conditional variance** $\text{Var}(X|Y)$, the **law of total variance** $\text{Var}(X) = E[\text{Var}(X|Y)] + \text{Var}(E[X|Y])$, and two powerful applications — Gaussian conditionals (linear in $Y$) and **random sums** $\sum_{i=1}^N X_i$ where $N$ is itself a RV.

## Key takeaways
- **$E[X|Y]$ is a function of $Y \to$ it's a random variable.** $E[X|Y = y]$ for specific $y$ is a number (the regression function).
- If $X \perp Y$: $E[X|Y] = E[X]$ (a constant).
- **Iterated expectations (tower rule):** $E[E[X|Y]] = E[X]$. One of the most-used identities.
- **Conditional variance:** $\text{Var}(X|Y) = E[(X - E[X|Y])^2 | Y]$. Also a RV (function of $Y$).
- **Law of total variance:**
  $$\text{Var}(X) = E[\text{Var}(X|Y)] + \text{Var}(E[X|Y])$$
- **Gaussian conditional:** if $(X, Y)$ is bivariate Gaussian, then $E[X|Y]$ is **linear** in $Y$:
  $$E[X|Y] = \mu_X + \rho\tfrac{\sigma_X}{\sigma_Y}(Y - \mu_Y)$$
- **Random sum** $S = X_1 + \ldots + X_N$ where $N$ is a RV independent of $X$'s:
  - $E[S] = E[N]\cdot E[X]$
  - $\text{Var}(S) = E[N]\cdot\text{Var}(X) + \text{Var}(N)\cdot E[X]^2$ (the "two-term" variance formula, derived via law of total variance)
  - Example in slides: Poisson $N$, Gaussian $X$.

## Concepts introduced or reinforced
- [[conditional-expectation]]
- [[iterated-expectations]]
- [[conditional-variance]]
- [[law-of-total-variance]]
- [[sum-of-random-number-of-rvs]]

## Worked examples worth remembering
- **Stick-breaking example** (slides 8–10): break a stick at uniform position, break the remaining piece uniformly again $\to$ compute $E[\text{length after second break}]$ and Var using iterated expectations.
- **Poisson–Gaussian random sum** — direct application of the two variance-of-random-sum terms.

## Questions this source raised
- Why is the Gaussian conditional linear? Works out algebraically from the bivariate Gaussian PDF; covered in [[bivariate-gaussian]].
