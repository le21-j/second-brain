---
title: LMSE from a Discrete Joint PMF (HW7 12.2.3)
type: example
course: [[eee-350]]
tags: [lmse, estimation, joint-pmf, worked-example]
concept: [[linear-mmse-estimation]]
sources: [[homework-2026-04-23-eee-350-hw7]]
created: 2026-04-24
updated: 2026-04-26
---

# LMSE from a Discrete Joint PMF — HW7 Problem 12.2.3

## Problem
Random variables $X, Y$ with joint PMF:

| $P_{X,Y}(x,y)$ | $y = -1$ | $y = 0$ | $y = 1$ |
|:---:|:---:|:---:|:---:|
| $\mathbf{x = -1}$ | $3/16$ | $1/16$ | $0$ |
| $\mathbf{x = 0}$  | $1/6$  | $1/6$  | $1/6$ |
| $\mathbf{x = 1}$  | $0$    | $1/8$  | $1/8$ |

Find $\hat Y_L(X) = aX + b$ minimizing MSE, and the resulting minimum MSE $e_L^*$.

## Step 1 — Marginals

**$P_X$** (row sums):
- $P_X(-1) = 3/16 + 1/16 + 0 = 4/16 = 1/4$
- $P_X(0) = 1/6 + 1/6 + 1/6 = 1/2$
- $P_X(1) = 0 + 1/8 + 1/8 = 1/4$

**$P_Y$** (column sums), common denominator $48$:
- $P_Y(-1) = 3/16 + 1/6 + 0 = 9/48 + 8/48 = 17/48$
- $P_Y(0) = 1/16 + 1/6 + 1/8 = 3/48 + 8/48 + 6/48 = 17/48$
- $P_Y(1) = 0 + 1/6 + 1/8 = 8/48 + 6/48 = 14/48$

## Step 2 — First and second moments of $X$

$$E[X] = -\tfrac{1}{4} + 0 + \tfrac{1}{4} = 0.$$
$$E[X^2] = \tfrac{1}{4} + 0 + \tfrac{1}{4} = \tfrac{1}{2}.$$
$$\text{Var}(X) = \tfrac{1}{2} - 0^2 = \tfrac{1}{2}.$$

## Step 3 — First and second moments of $Y$

$$E[Y] = -\tfrac{17}{48} + 0 + \tfrac{14}{48} = -\tfrac{3}{48} = -\tfrac{1}{16}.$$
$$E[Y^2] = \tfrac{17}{48} + 0 + \tfrac{14}{48} = \tfrac{31}{48}.$$
$$\text{Var}(Y) = \tfrac{31}{48} - \tfrac{1}{256} = \tfrac{496}{768} - \tfrac{3}{768} = \tfrac{493}{768}.$$

## Step 4 — $E[XY]$
Only cells with both $x \neq 0$ and $y \neq 0$ contribute:
$$E[XY] = (-1)(-1)\tfrac{3}{16} + (-1)(1)\cdot 0 + (1)(-1)\cdot 0 + (1)(1)\tfrac{1}{8} = \tfrac{3}{16} + \tfrac{2}{16} = \tfrac{5}{16}.$$

$$\text{Cov}(X,Y) = \tfrac{5}{16} - 0\cdot(-\tfrac{1}{16}) = \tfrac{5}{16}.$$

## Step 5 — LMSE coefficients

$$a^* = \frac{\text{Cov}(X,Y)}{\text{Var}(X)} = \frac{5/16}{1/2} = \boxed{\tfrac{5}{8}}.$$
$$b^* = E[Y] - a^*\,E[X] = -\tfrac{1}{16} - \tfrac{5}{8}\cdot 0 = \boxed{-\tfrac{1}{16}}.$$

$$\boxed{\hat Y_L(X) = \tfrac{5}{8}X - \tfrac{1}{16}}.$$

## Step 6 — Minimum MSE

$$e_L^* = \text{Var}(Y) - \frac{\text{Cov}(X,Y)^2}{\text{Var}(X)} = \tfrac{493}{768} - \frac{(5/16)^2}{1/2}.$$
$$\frac{(5/16)^2}{1/2} = \frac{25/256}{1/2} = \tfrac{50}{256} = \tfrac{150}{768}.$$
$$e_L^* = \tfrac{493}{768} - \tfrac{150}{768} = \boxed{\tfrac{343}{768} \approx 0.447}.$$

## Sanity check: how much variance does $X$ explain?

$$\rho^2 = \frac{\text{Cov}(X,Y)^2}{\text{Var}(X)\text{Var}(Y)} = \frac{(5/16)^2}{(1/2)(493/768)} = \frac{25/256}{493/1536} = \frac{150}{493} \approx 0.30.$$

So $X$ explains about 30% of $\text{Var}(Y)$ linearly. The remaining 70% is unexplainable by any linear function of $X$. That's consistent with $e_L^* / \text{Var}(Y) = 343/493 \approx 0.70$.

## Key takeaways
- LMSE needed only **5 numbers**: $E[X]$, $E[Y]$, $\text{Var}(X)$, $\text{Var}(Y)$, $\text{Cov}(X,Y)$. The rest of the PMF was irrelevant to the linear estimator.
- A diagonal-heavy joint (cells $(-1,-1)$ and $(1,1)$ carrying mass) gives positive $\text{Cov}(X,Y)$ $\to$ positive $a^*$.
- $E[X] = 0$ made $b^* = E[Y]$ — a lucky simplification.

## Related
- [[linear-mmse-estimation]]
- [[covariance]], [[correlation-coefficient]]
- [[lmse-continuous-pdf]] — the continuous-PDF analog
- [[mmse-vs-lmse-erlang]] — contrasts LMSE with unrestricted MMSE
