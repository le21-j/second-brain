---
title: Convergence in Probability
type: concept
course:
  - "[[eee-350]]"
tags: [convergence, asymptotic]
sources:
  - "[[slides-41-lln-clt-intro]]"
created: 2026-04-21
updated: 2026-05-06
---

# Convergence in Probability

## In one line
A sequence of RVs $X_n$ converges to $X$ "in probability" if the chance that $X_n$ is far from $X$ **vanishes** as $n \to \infty$.

## Example first
Let $X_n$ = sample mean of $n$ i.i.d. fair dice rolls. We suspect $X_n \to 3.5$ as $n \to \infty$. In what sense?

- $X_n$ **doesn't** equal $3.5$ at any finite $n$.
- $X_n$ doesn't even "always get close" — occasionally it has a bad run.
- But $P(|X_n - 3.5| \geq 0.01) \to 0$ as $n$ grows. That's convergence in probability.

This is the [[weak-law-of-large-numbers]] in action.

## Formal definition
$X_n \to X$ in probability if for every $\varepsilon > 0$:
$$\lim_{n \to \infty} P(|X_n - X| \ge \varepsilon) = 0$$

Notation: $X_n \xrightarrow{p} X$, or $X_n \xrightarrow{P} X$, or "$\text{plim } X_n = X$".

## Contrast with deterministic convergence
A deterministic sequence $a_n$ converges to $a$ if for every $\varepsilon > 0$, eventually $|a_n - a| < \varepsilon$ for **all** $n$ large enough. No randomness.

Convergence in probability allows $X_n$ to occasionally be far from $X$ — just ever more rarely.

## Related convergence modes (mention only)
Probability theory has **several** notions of convergence, strictly comparable:
1. **Almost surely (a.s.):** $P(\lim X_n = X) = 1$. Every realization's sequence converges.
2. **In probability:** defined above.
3. **In $L^p$** (e.g. mean-square): $E[|X_n - X|^p] \to 0$.
4. **In distribution (in law):** $F_{X_n}(t) \to F_X(t)$ at continuity points.

Hierarchy: **a.s. $\Rightarrow$ in probability $\Rightarrow$ in distribution** (and similar for $L^p$). The reverse implications generally fail.

- **WLLN** = convergence of sample mean **in probability**.
- **SLLN** = convergence **almost surely** (stronger).
- **CLT** = convergence **in distribution** (a completely different thing — it's about the shape of the distribution, not the value converging to a constant).

## Useful shortcut (Chebyshev lemma)
If **$E[X_n] \to \mu$** (a constant) and **$\text{Var}(X_n) \to 0$**, then $X_n \xrightarrow{p} \mu$.

Proof: by Chebyshev, $P(|X_n - \mu| \geq \varepsilon) \leq (E[X_n] - \mu)^2$ term $+ \text{Var}(X_n)/\varepsilon^2 \to 0$. This is exactly how WLLN gets proved.

## Common mistakes
- Thinking convergence in probability means $X_n = X$ eventually. It doesn't — just that "far from $X$" has shrinking probability.
- Mixing "in probability" with "in distribution". Completely different. $X_n \xrightarrow{d} X$ only says the CDFs converge; $X_n$ itself might be jumping around.
- Assuming "in probability" guarantees convergence of moments. It doesn't — $X_n$ could converge in probability but $E[X_n]$ oscillates.

## Related
- [[chebyshev-inequality]]
- [[weak-law-of-large-numbers]]
- [[central-limit-theorem]] (uses a different convergence — in distribution)

## Practice
- [[asymptotics-set-01]]
