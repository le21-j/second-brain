---
title: Slides 41 — LLN/CLT Intro, Convergence
type: summary
source_type: slides
source_path: raw/slides/eee-350/41 LLN CLT Intro, Convergence.pptx
course:
  - "[[eee-350]]"
tags: [asymptotic, chebyshev, convergence]
created: 2026-04-21
updated: 2026-05-06
---

# Slides 41 — LLN/CLT Intro, Convergence

## TL;DR
Preview slide for the whole asymptotics arc. Both LLN and CLT describe what happens to a sum of many RVs — LLN about the *average*, CLT about the *scaled sum* (with a $\sqrt{n}$ normalization). Before stating them, revisits **Chebyshev's inequality** (the bound that powers most LLN proofs) and defines **convergence in probability**.

## Key takeaways
- **Chebyshev's inequality:** for any RV $X$ with finite mean $\mu$ and variance $\sigma^2$,
  $$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$
  Or equivalently, $P(|X - \mu| \geq \varepsilon) \leq \sigma^2/\varepsilon^2$. Only needs finite variance — no distribution shape.
- **Deterministic limit** (review): $a_n \to a$ means for every $\varepsilon > 0$, eventually $|a_n - a| < \varepsilon$.
- **Convergence in probability:** $X_n \to X$ in probability if for every $\varepsilon > 0$, $P(|X_n - X| \geq \varepsilon) \to 0$ as $n \to \infty$. Different from convergence of deterministic sequences.
- Example: if $\text{Var}(X_n) \to 0$ while mean stays at $\mu$, Chebyshev $\Rightarrow X_n \to \mu$ in probability.

## Concepts introduced or reinforced
- [[chebyshev-inequality]]
- [[convergence-in-probability]]
- [[deterministic-limit]] (review)

## Worked examples worth remembering
- $X_n$ with $E[X_n] = \mu$ and $\text{Var}(X_n) = \sigma^2/n \to X_n \to \mu$ in probability.
