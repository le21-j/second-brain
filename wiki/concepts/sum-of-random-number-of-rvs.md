---
title: Sum of a Random Number of RVs
type: concept
course:
  - "[[eee-350]]"
tags: [random-sum, compound, iterated-expectations]
sources:
  - "[[slides-40-conditional-expectation]]"
created: 2026-04-21
updated: 2026-05-06
---

# Sum of a Random Number of RVs

## In one line
$S = X_1 + X_2 + \ldots + X_N$ where **$N$ itself is random**. Mean: $E[S] = E[N] \cdot E[X]$. Variance has **two** terms: $E[N] \cdot \text{Var}(X) + \text{Var}(N) \cdot (E[X])^2$.

## Example first
A call center receives $N \sim \text{Poisson}(100)$ calls per hour. Each call takes a random time $X \sim \text{Exponential}(\text{mean 2 minutes})$, independent of $N$ and of other calls. What's the mean and variance of total call time $S$?

- $E[X] = 2$, $\text{Var}(X) = 4$.
- $E[N] = \text{Var}(N) = 100$ (Poisson).
- **$E[S] = E[N] \cdot E[X] = 100 \cdot 2 =$ $200$ minutes**.
- **$\text{Var}(S) = E[N] \cdot \text{Var}(X) + \text{Var}(N) \cdot E[X]^2 = 100 \cdot 4 + 100 \cdot 4 =$ $800$ minutes$^2$**.
- $\text{Std}(S) \approx 28$ min.

## The idea
Two sources of randomness:
1. How many $X$'s are we summing? (That's $N$.)
2. How big is each $X$?

You can't just "sum the variances" — you have to account for the fact that $N$ is random too. The elegant derivation uses [[iterated-expectations]] and the [[law-of-total-variance]].

## Assumptions (standard setup)
- $N$ is a non-negative integer RV.
- $X_1, X_2, \ldots$ are i.i.d. with mean $\mu_X$ and variance $\sigma_X^2$.
- $N$ is **independent** of all the $X_i$.

## The mean (one-liner with iterated expectations)
$$E[S | N = n] = n\cdot\mu_X$$
so $E[S | N] = N \cdot \mu_X$, and
$$E[S] = E[N \cdot \mu_X] = \mu_X \cdot E[N]$$

## The variance (law of total variance)
First get the conditional:
$$\text{Var}(S | N = n) = n\cdot\sigma_X^2$$
so $\text{Var}(S | N) = N \cdot \sigma_X^2$. And $E[S | N] = N \cdot \mu_X$, whose variance is $\mu_X^2 \cdot \text{Var}(N)$.

Plug into $\text{Var}(S) = E[\text{Var}(S | N)] + \text{Var}(E[S | N])$:
$$\boxed{\,\text{Var}(S) = E[N]\cdot\sigma_X^2 + \mu_X^2\cdot\text{Var}(N)\,}$$

## Interpreting the two terms
- **$E[N] \cdot \sigma_X^2$:** variance you'd expect from summing $E[N]$ terms of variance $\sigma_X^2$ each. The "per-term noise" contribution.
- **$\mu_X^2 \cdot \text{Var}(N)$:** extra variance because the number of terms is itself uncertain. Each extra (or missing) term contributes about $\mu_X$, so spread in $N$ gets squared.

## Special case: Poisson N
If $N \sim \text{Poisson}(\lambda)$, then $E[N] = \text{Var}(N) = \lambda$, so
$$\text{Var}(S) = \lambda(\sigma_X^2 + \mu_X^2) = \lambda\cdot E[X^2]$$
(Used the identity $\sigma^2 + \mu^2 = E[X^2]$.)

Nice clean form — recurring in queuing theory and point processes. Poisson-based random sums are called **compound Poisson** processes.

## Common mistakes
- Using $\text{Var}(S) = N \cdot \sigma_X^2$ (with $N$ random, as if it weren't). This is only the conditional variance; you also need the $\text{Var}(N)$ term.
- Forgetting the independence of $N$ from the $X_i$. If $N$ is correlated with $X$ (e.g. "long calls today $\Rightarrow$ fewer calls"), the simple formula doesn't apply.
- Mixing up $\text{Var}(N)$ with $E[N]$ — both appear in the final formula, and they're different things (only equal for Poisson).

## Related
- [[iterated-expectations]]
- [[law-of-total-variance]]
- [[poisson-process]] — context for compound-Poisson random sums
- [[conditional-expectation]]

## Practice
- [[prob-fundamentals-set-01]]
