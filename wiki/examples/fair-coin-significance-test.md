---
title: Fair-Coin Significance Test (HW7 11.1.6)
type: example
course:
  - "[[eee-350]]"
tags: [significance-test, clt, binomial, worked-example]
concept:
  - "[[significance-test]]"
sources:
  - "[[homework-2026-04-23-eee-350-hw7]]"
created: 2026-04-24
updated: 2026-05-06
---

# Fair-Coin Significance Test — HW7 Problem 11.1.6

## Problem
$K$ = number of heads in $n = 100$ flips. Devise a significance test for
$$H: p = 0.5 \quad (\text{coin is fair})$$
with level $\alpha = 0.05$ and rejection region $R = \{\, |K - E[K]| > c \,\}$.

## Setup under $H$
If $H$ is true, $K \sim \text{Binomial}(100, 0.5)$:
- $E[K] = np = 50$
- $\text{Var}(K) = np(1 - p) = 25$
- $\sigma_K = 5$

## Step 1 — Write the constraint
$$P(|K - 50| > c \mid H) \le 0.05.$$

## Step 2 — Apply CLT
$n = 100$ is large and $p = 0.5$ is symmetric $\to$ the [[central-limit-theorem|CLT]] approximation is excellent. [[standardization|Standardize]]:
$$Z = \frac{K - 50}{5} \approx \mathcal{N}(0, 1).$$

So
$$P(|K - 50| > c) \;\approx\; P\!\left(|Z| > \tfrac{c}{5}\right) \;=\; 2\bigl(1 - \Phi(c/5)\bigr).$$

## Step 3 — Solve for $c$
$$2\bigl(1 - \Phi(c/5)\bigr) = 0.05 \;\Longrightarrow\; \Phi(c/5) = 0.975.$$
From [[standard-normal-table]]: $\Phi^{-1}(0.975) = 1.96$. Therefore
$$\frac{c}{5} = 1.96 \;\Longrightarrow\; \boxed{c = 9.8}.$$

## Step 4 — State the rule
> **Reject $H$** if $|K - 50| > 9.8$, i.e. if $K \leq 40$ or $K \geq 60$.

Integer boundaries chosen because $K$ is discrete — this is conservative (actual $P(\text{reject} \mid H) \leq 0.05$).

## Sanity check on the rule
$P(K \leq 40 \text{ or } K \geq 60 \mid H)$ by normal approximation $\approx 2\cdot(1 - \Phi(10/5)) = 2\cdot(1 - \Phi(2)) \approx 0.0455$. ✓ (under budget, thanks to the integer snap).

## Key takeaways
- **1.96** is the two-sided z-score for $\alpha = 0.05$. Memorize it. See [[standard-normal-table]].
- **Two separate steps**: CLT gives $\mathcal{N}(50, 25)$; [[standardization]] gives $\mathcal{N}(0, 1)$. They are not the same operation — see [[prob-gotchas]].
- **$\alpha$ refers to experiments, not flips.** The 5% describes what happens if we repeated the *entire* 100-flip experiment many times under a fair coin.

## Related
- [[significance-test]] — the concept
- [[central-limit-theorem]], [[standardization]], [[standard-normal-table]]
- [[binomial-via-clt]] — normal approximation to Binomial
- [[type-i-error]] — the $\alpha$ probability
