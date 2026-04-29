---
title: Markov's Inequality
type: concept
course: [[eee-350]]
tags: [inequalities, tail-bound]
sources: [[slides-41-lln-clt-intro]]
created: 2026-04-21
updated: 2026-04-26
---

# Markov's Inequality

## In one line
For any **non-negative** RV $Y$ with finite mean:
$$P(Y \ge a) \le \frac{E[Y]}{a}$$

## Example first
Average household income is \$80,000. By Markov, at most 10% of households have income $\geq$ \$800,000. (The bound is loose — actual number is way smaller — but you didn't need any distribution info, just the mean.)

## The idea
If $Y$ is positive and has mean $E[Y]$, it can't have too much mass **above** any given threshold, because the threshold $\times$ (probability above it) contributes at least that much to the mean.

## Derivation (2 lines)
$E[Y] = \int y \cdot f(y)\, dy \geq \int_{y \geq a} y \cdot f(y)\, dy \geq a \cdot \int_{y \geq a} f(y)\, dy = a \cdot P(Y \geq a)$. Rearrange.

## Why it's the parent of Chebyshev
Apply Markov to $Y = (X - \mu)^2$ (which is non-negative) with threshold $\varepsilon^2$:
$$P((X - \mu)^2 \ge \varepsilon^2) \le \frac{E[(X - \mu)^2]}{\varepsilon^2} = \frac{\sigma^2}{\varepsilon^2}$$
That's Chebyshev. So every Chebyshev proof secretly uses Markov.

## Common mistakes
- Applying Markov to RVs that **can be negative**. The bound assumes $Y \geq 0$.
- Reading $E[Y]/a > 1$ as "probability $> 1$" — Markov still says the probability is $\leq 1$, just that the bound becomes trivial.

## Related
- [[chebyshev-inequality]] — special case via squaring trick
- [[convergence-in-probability]]
