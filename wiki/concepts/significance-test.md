---
title: Significance Test
type: concept
course: [[eee-350]]
tags: [hypothesis-testing, significance, frequentist]
sources: [[homework-2026-04-23-eee-350-hw7]]
created: 2026-04-24
updated: 2026-04-26
---

# Significance Test

## In one line
A **decision rule for rejecting a null hypothesis $H$** based on an observed statistic, subject to a fixed cap $\alpha$ on the probability of wrongly rejecting $H$ when $H$ is actually true.

## Example first
A coin is flipped $n = 100$ times. Let $K$ = number of heads. Design a test to decide whether the coin is fair, at significance level $\alpha = 0.05$, with rejection region $R = \{ |K - 50| > c \}$.

1. Under $H$ (fair): $K \sim \text{Binomial}(100, 0.5)$, so $E[K] = 50$, $\sigma_K = 5$.
2. By [[central-limit-theorem|CLT]]: $(K - 50)/5 \approx N(0, 1)$.
3. We want $P(|K - 50| > c \mid H) = 0.05 \to P(|Z| > c/5) = 0.05 \to c/5 = 1.96 \to$ **$c = 9.8$**.
4. **Rule:** reject $H$ (declare coin unfair) if $K \leq 40$ or $K \geq 60$.

The 5% budget has been spent on this rejection region. If $H$ is true, we'll mistakenly say "unfair" in about 5% of hypothetical repetitions of the 100-flip experiment.

## The idea
A significance test has four moving parts:

| Piece | Symbol | Meaning |
|---|---|---|
| Null hypothesis | $H$ | the default belief to be disproved |
| Test statistic | $T(X)$ | a function of the data |
| Rejection region | $R$ | values of $T$ that trigger rejection |
| Significance level | $\alpha$ | max allowed probability of a wrong rejection |

**Design rule.** Pick $R$ so that
$$P(T \in R \mid H) = \alpha.$$
Pick the *smallest* $R$ achieving this (tightest test $\to$ highest power). But you must respect the $\alpha$ budget.

## Two-tailed vs one-tailed

- **Two-tailed:** reject if $T$ is far from $E[T]$ in *either* direction. Split $\alpha$ evenly between tails. Use $z_{\alpha/2}$ (e.g. **1.96** for $\alpha = 0.05$).
- **One-tailed:** reject only on one side. Use $z_\alpha$ (e.g. **1.645** for $\alpha = 0.05$).

The HW coin problem is two-tailed (the coin could be biased high *or* low).

## Common recipe (CLT-based)

1. Under $H$, compute $\mu_0 = E[T \mid H]$ and $\sigma_0 = \sqrt{\text{Var}(T \mid H)}$.
2. If $n$ is large, use [[central-limit-theorem|CLT]]: $(T - \mu_0)/\sigma_0 \approx N(0, 1)$.
3. For two-sided: reject if $|T - \mu_0| > z_{\alpha/2}\cdot\sigma_0$.
4. For one-sided: reject if $T - \mu_0 > z_\alpha\cdot\sigma_0$ (or $< -z_\alpha\cdot\sigma_0$).

$z$-values from [[standard-normal-table]].

## Significance test vs Neyman-Pearson

| | Significance test | [[neyman-pearson-test|Neyman-Pearson]] |
|---|---|---|
| Alternative hypothesis | Implicit or absent | Explicit $H_1$ |
| Output | Reject / fail-to-reject $H$ | Decide $H_0$ or $H_1$ |
| Optimality | Not framed in these terms | **Optimal** power subject to $\alpha$ (by the NP lemma) |
| When to use | "Is the coin fair?" | "Fair vs. biased toward heads?" |

A significance test is essentially a one-sided or two-sided version of the rejection step in Neyman-Pearson, without naming the alternative.

## Common mistakes
- **$\alpha$ is not "probability $H$ is true after rejection."** $\alpha = P(\text{reject } H \mid H \text{ true})$. Reversed conditional. See [[prob-gotchas]].
- **"Fail to reject" $\neq$ "accept $H$."** It only means the data doesn't give enough evidence against $H$ at level $\alpha$.
- **100 flips is ONE experiment, not 100 trials.** $\alpha$ refers to repeated experiments, not to the individual coin flips.
- **Discrete $T$ $\to$ round conservatively.** For Binomial $K$, $c = 9.8$ means reject on $\{K \leq 40, K \geq 60\}$ (integer boundaries). Actual $P(\text{reject} \mid H) \leq \alpha$.

## Related
- [[neyman-pearson-test]] — the "with alternative" upgrade
- [[type-i-error]] — $\alpha$ is its probability
- [[likelihood-ratio-test]]
- [[central-limit-theorem]] — justifies the normal approximation
- [[standard-normal-table]] — where 1.96 comes from

## Examples
- [[fair-coin-significance-test]] — HW7 Problem 11.1.6 worked in full

## Practice
- [[inference-set-01]]
