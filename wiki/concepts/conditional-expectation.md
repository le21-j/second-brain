---
title: Conditional Expectation
type: concept
course: [[eee-350]]
tags: [conditional-expectation, moments]
sources: [[slides-40-conditional-expectation]]
created: 2026-04-21
updated: 2026-04-26
---

# Conditional Expectation

## In one line
$E[X | Y]$ is a **random variable** — specifically, a function of $Y$ that gives the best guess of $X$ once you know $Y$.

## Example first
$X$ = height of a random adult, $Y$ = their sex. Then:
- $E[X | Y = \text{male}] \approx 178$ cm — a number
- $E[X | Y = \text{female}] \approx 165$ cm — a number
- $E[X | Y]$ is the **random variable** that equals 178 if $Y =$ male, 165 if $Y =$ female. It takes a value determined by the realization of $Y$.

When you're told $Y$ is male, the conditional expectation is 178. Before you know $Y$, $E[X | Y]$ is itself a random variable that will turn out to be 178 or 165 with the respective probabilities.

## The idea (critical distinction)

| Object | Type | Meaning |
|---|---|---|
| $E[X]$ | a number | marginal mean of $X$ |
| $E[X \| Y = y]$ | a number (given specific $y$) | conditional mean of $X$ when $Y = y$ |
| **$E[X \| Y]$** | a random variable | function $g(Y)$; takes value $E[X \| Y = y]$ when $Y = y$ |

The third one is the subtle thing the slides want you to internalize.

## Formal definition
For $Y$ taking values in some set:
- **Discrete $Y$:** $E[X | Y] = g(Y)$ where $g(y) = E[X | Y = y] = \sum_x x \cdot P(X = x | Y = y)$.
- **Continuous $Y$:** $E[X | Y = y] = \int x \cdot f_{X|Y}(x | y)\, dx$, and $E[X | Y] = g(Y)$.

The function $g$ depends on the joint distribution; $E[X | Y]$ is then just $g$ applied to the random variable $Y$.

## Key identities

### Independence
If $X \perp Y$, then **$E[X | Y] = E[X]$** (a constant).

### Iterated expectations (tower rule)
$$E[E[X | Y]] = E[X]$$

This is a workhorse identity. You often compute $E[X]$ by first conditioning on $Y$, then averaging:
- Step 1: Compute $g(y) = E[X | Y = y]$.
- Step 2: Compute $E[X] = E[g(Y)] = \int g(y) \cdot f_Y(y)\, dy$.

### Gaussian special case
If $(X, Y)$ is jointly Gaussian with correlation $\rho$:
$$E[X | Y] = \mu_X + \rho\frac{\sigma_X}{\sigma_Y}(Y - \mu_Y)$$
Linear in $Y$. See [[bivariate-gaussian]].

## Worked intuition — stick-breaking
Break a unit-length stick at a uniform position $U_1 \in [0, 1]$. Keep the right piece (length $1 - U_1$). Break that at a uniform position $U_2$ along its current length. Remaining length $W$:

$$W = (1 - U_1) \cdot U_2$$

wait, set up is: $W$ is the length of a specific piece. Let's say $W$ = length of the final right piece after two breaks.

$E[W | U_1] = E[(1 - U_1) \cdot U_2 | U_1] = (1 - U_1) \cdot E[U_2] = (1 - U_1) \cdot (1/2)$.

$E[W] = E[E[W | U_1]] = E[(1 - U_1)/2] = (1 - 1/2)/2 =$ **$1/4$**. $\checkmark$ (Two-step iterated expectation.)

## Why it matters
- **Prediction:** $E[X | Y]$ is the **minimum mean-squared-error estimator** of $X$ given $Y$. See [[lms-estimation]].
- **Random sums:** handling $\sum_{i=1}^N X_i$ where $N$ is random uses iterated expectations systematically. See [[sum-of-random-number-of-rvs]].
- **Bayesian inference:** the posterior mean $E[\theta | X]$ is exactly the LMS estimator.
- **Proofs:** iterated expectations is one of the most-used moves in probability proofs.

## Common mistakes
- **Treating $E[X | Y]$ as a number** when it's a random variable. The conditioning variable matters.
- **Conflating $E[X | Y = y]$ with $E[X | Y]$**. The first is a number; the second is a random variable.
- **Forgetting iterated expectations.** When you see a two-stage random experiment, reach for it first.

## Related
- [[iterated-expectations]] — the tower rule in its own page
- [[conditional-variance]]
- [[law-of-total-variance]]
- [[sum-of-random-number-of-rvs]]
- [[lms-estimation]]
- [[bivariate-gaussian]]

## Practice
- [[prob-fundamentals-set-01]]
