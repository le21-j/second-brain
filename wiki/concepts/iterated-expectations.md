---
title: Iterated Expectations (Tower Rule)
type: concept
course:
  - "[[eee-350]]"
tags: [tower-rule, conditional-expectation]
sources:
  - "[[slides-40-conditional-expectation]]"
created: 2026-04-21
updated: 2026-05-06
---

# Iterated Expectations (Tower Rule)

## In one line
$$E[X] = E[E[X | Y]]$$
Compute $E[X]$ by first conditioning on $Y$, then averaging out $Y$.

## Example first
You want $E[X]$ where $X$ = number of heads in $N$ tosses, and **$N$ itself is a random variable** — say $N \sim \text{Poisson}(10)$, and each toss is independent fair.

Direct computation: hard ($X$ has a compound distribution).

Iterated: condition on $N$ first.
- $E[X | N = n] = n/2$ (binomial mean).
- So $E[X | N] = N/2$.
- $E[X] = E[E[X | N]] = E[N/2] = E[N]/2 =$ **$10/2 = 5$**.

Clean. Two-step.

## The idea
When a probability model has a natural "inner" random variable $Y$, computing $E[X]$ directly might be hard. But **conditioning on $Y$** often simplifies things because you can freeze $Y$ and compute a conditional mean easily. Then average out $Y$.

## Statement
For any RVs $X, Y$ (with $E[|X|] < \infty$):
$$E[X] = E[E[X | Y]]$$

Also known as the **tower rule** or the **law of total expectation**.

## Generalizations
- **Nested conditioning:** $E[X | Y] = E[E[X | Y, Z] | Y]$. Coarser $\sigma$-algebra on the outside.
- **Functions of $X$:** $E[g(X)] = E[E[g(X) | Y]]$ for any $g$.

## Why it works (intuition)
Think of it discretely. If $Y$ takes values $y_1, \ldots, y_k$:
$$E[X] = \sum_x x \cdot P(X = x) = \sum_x x \sum_j P(X = x | Y = y_j) P(Y = y_j)$$
Switch order of summation:
$$= \sum_j P(Y = y_j) \sum_x x \cdot P(X = x | Y = y_j) = \sum_j P(Y = y_j) \cdot E[X | Y = y_j] = E[E[X | Y]]$$

## Common uses
- **Two-stage experiments:** probability of something happening in step 2 depends on outcome of step 1. Condition on step 1 first.
- **Random sums:** $E[\sum X_i]$ with random $N$. See [[sum-of-random-number-of-rvs]].
- **Bayesian** computations: $E_X[g(X)]$ often $= E_\theta[E_X[g(X) | \theta]]$.
- **Proofs:** simplifying $E[\text{something}]$ by finding a conditioning variable that makes the inner expectation easy.

## Common mistakes
- **Forgetting it's an identity** — people sometimes think "condition on $Y$" is throwing away information. It's not; $E[E[X | Y]] = E[X]$ exactly.
- **Confusing "tower rule" with "total probability".** Related but different:
  - Total probability: $P(A) = \sum_j P(A | Y = y_j) \cdot P(Y = y_j)$. For events.
  - Iterated expectations: $E[X] = E[E[X | Y]]$. For expectations.

## Related
- [[conditional-expectation]]
- [[law-of-total-variance]]
- [[sum-of-random-number-of-rvs]]

## Practice
- [[prob-fundamentals-set-01]]
