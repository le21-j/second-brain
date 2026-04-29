---
title: Example — Stick-Breaking via Iterated Expectations
type: example
course: [[eee-350]]
tags: [iterated-expectations, conditional-expectation]
sources: [[slides-40-conditional-expectation]]
created: 2026-04-21
updated: 2026-04-26
---

# Example — Stick-Breaking via Iterated Expectations

## Problem
A unit-length stick is broken at a point uniformly in $[0, 1]$. Call that point $U_1$. You keep the **right piece** (length $1 - U_1$). Now break that right piece at a point chosen uniformly along its length. Call that second break position $U_2$ (where $U_2 \sim \text{Uniform}(0, 1)$, expressed as a fraction along the remaining piece). You keep the right piece of the **second** break.

What is the expected length of the final right piece? What is its variance?

## Setup
Let $W$ = final right piece length.
- After first break, remaining length = $1 - U_1$.
- After second break at a uniform point of that remaining length, final right piece = $(1 - U_1)\cdot(1 - U_2)$.

So $W = (1 - U_1)(1 - U_2)$ with $U_1, U_2$ i.i.d. $\text{Uniform}(0, 1)$.

## Mean — via iterated expectations

$$E[W \mid U_1] = E[(1 - U_1)(1 - U_2) \mid U_1] = (1 - U_1)\cdot E[1 - U_2] = (1 - U_1)\cdot\tfrac{1}{2}$$

Apply the tower rule ([[iterated-expectations]]):
$$E[W] = E\bigl[E[W \mid U_1]\bigr] = \tfrac{1}{2}\cdot E[1 - U_1] = \tfrac{1}{2}\cdot\tfrac{1}{2} = \boxed{\tfrac{1}{4}}$$

## Mean — direct (for comparison)
Since $U_1 \perp U_2$:
$$E[W] = E[1 - U_1]\cdot E[1 - U_2] = \tfrac{1}{2}\cdot\tfrac{1}{2} = \tfrac{1}{4}$$
Same answer, more directly — but the iterated approach generalizes to cases where the second break isn't independent.

## Variance — via law of total variance

Let $V_1 = 1 - U_1$, $V_2 = 1 - U_2$ (both $\text{Uniform}(0, 1)$). $W = V_1\cdot V_2$.

**$E[W \mid V_1] = V_1\cdot(1/2)$, so $\text{Var}\bigl(E[W \mid V_1]\bigr) = (1/4)\cdot\text{Var}(V_1) = (1/4)\cdot(1/12) = 1/48$.**

**$\text{Var}(W \mid V_1) = V_1^2\cdot\text{Var}(V_2) = V_1^2/12$.** Take expectation:
$$E\bigl[\text{Var}(W \mid V_1)\bigr] = \tfrac{1}{12}\cdot E[V_1^2] = \tfrac{1}{12}\cdot\tfrac{1}{3} = \tfrac{1}{36}$$

(Used $E[V_1^2] = \text{Var}(V_1) + E[V_1]^2 = 1/12 + 1/4 = 1/3$.)

Apply the law of total variance:
$$\text{Var}(W) = E\bigl[\text{Var}(W \mid V_1)\bigr] + \text{Var}\bigl(E[W \mid V_1]\bigr) = \tfrac{1}{36} + \tfrac{1}{48} = \tfrac{4 + 3}{144} = \boxed{\tfrac{7}{144}}$$

Std $\approx 0.22$. Roughly, $W$ is usually between $0.03$ and $0.47$ (mean $\pm$ 1 std).

## Pattern to remember
Two-stage random experiments have a natural **"condition on stage 1 first"** structure. [[iterated-expectations]] handles the mean; [[law-of-total-variance]] handles the variance.

## Related
- [[conditional-expectation]]
- [[iterated-expectations]]
- [[law-of-total-variance]]
