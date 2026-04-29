---
title: LMSE for a Continuous Joint PDF (HW7 12.2.4)
type: example
course: [[eee-350]]
tags: [lmse, estimation, joint-pdf, worked-example]
concept: [[linear-mmse-estimation]]
sources: [[homework-2026-04-23-eee-350-hw7]]
created: 2026-04-24
updated: 2026-04-26
---

# LMSE for a Continuous Joint PDF — HW7 Problem 12.2.4

## Problem
$$f_{X,Y}(x,y) = \begin{cases} 2(y + x) & 0 \le x \le y \le 1 \\ 0 & \text{otherwise} \end{cases}$$
Find $\hat X_L(Y)$, the linear MMSE estimate of $X$ given $Y$.

## Support sketch (crucial)
$0 \leq x \leq y \leq 1$ is a **triangle** with corners $(0,0)$, $(0,1)$, $(1,1)$. For a fixed $y$, $x$ ranges over $[0, y]$. For a fixed $x$, $y$ ranges over $[x, 1]$. The triangle's orientation dictates the inner integration limits.

## Step 1 — Marginal of Y
$$f_Y(y) = \int_0^y 2(y + x)\,dx = \bigl[2yx + x^2\bigr]_0^y = 2y^2 + y^2 = 3y^2, \quad 0 \le y \le 1.$$

## Step 2 — Moments of Y
$$E[Y] = \int_0^1 y\cdot 3y^2\,dy = \int_0^1 3y^3\,dy = \tfrac{3}{4}.$$
$$E[Y^2] = \int_0^1 y^2\cdot 3y^2\,dy = \int_0^1 3y^4\,dy = \tfrac{3}{5}.$$
$$\text{Var}(Y) = \tfrac{3}{5} - \tfrac{9}{16} = \tfrac{48}{80} - \tfrac{45}{80} = \tfrac{3}{80}.$$

## Step 3 — Marginal of X
For fixed $x \in [0, 1]$, $y$ ranges over $[x, 1]$:
$$f_X(x) = \int_x^1 2(y + x)\,dy = \bigl[y^2 + 2xy\bigr]_x^1 = (1 + 2x) - (x^2 + 2x^2) = 1 + 2x - 3x^2.$$

## Step 4 — Mean of X
$$E[X] = \int_0^1 x(1 + 2x - 3x^2)\,dx = \int_0^1 (x + 2x^2 - 3x^3)\,dx = \tfrac{1}{2} + \tfrac{2}{3} - \tfrac{3}{4}.$$
Common denominator $12$: $(6 + 8 - 9)/12 = \mathbf{5/12}$.

## Step 5 — E[XY]
$$E[XY] = \int_0^1\!\!\int_0^y xy\cdot 2(y + x)\,dx\,dy = \int_0^1\!\!\int_0^y (2xy^2 + 2x^2 y)\,dx\,dy.$$

Inner integral (in x):
$$\int_0^y (2xy^2 + 2x^2 y)\,dx = \bigl[x^2 y^2 + \tfrac{2}{3}x^3 y\bigr]_0^y = y^4 + \tfrac{2}{3}y^4 = \tfrac{5}{3}y^4.$$

Outer:
$$E[XY] = \int_0^1 \tfrac{5}{3}y^4\,dy = \tfrac{5}{3}\cdot\tfrac{1}{5} = \tfrac{1}{3}.$$

## Step 6 — Covariance
$$\text{Cov}(X,Y) = \tfrac{1}{3} - \tfrac{5}{12}\cdot\tfrac{3}{4} = \tfrac{1}{3} - \tfrac{15}{48} = \tfrac{16}{48} - \tfrac{15}{48} = \tfrac{1}{48}.$$

## Step 7 — LMSE coefficients and estimate

$$a^* = \frac{\text{Cov}(X,Y)}{\text{Var}(Y)} = \frac{1/48}{3/80} = \frac{80}{144} = \tfrac{5}{9}.$$
$$b^* = E[X] - a^*\,E[Y] = \tfrac{5}{12} - \tfrac{5}{9}\cdot\tfrac{3}{4} = \tfrac{5}{12} - \tfrac{15}{36} = \tfrac{15}{36} - \tfrac{15}{36} = 0.$$

$$\boxed{\hat X_L(Y) = \tfrac{5}{9}\,Y.}$$

## Why b* = 0 here
The regression line passes through the origin because of the geometry: both $E[X]$ and $E[Y]$ lie on the line $X = (5/9)\cdot Y$ (since $E[X] = 5/12 = (5/9)\cdot(3/4) = E[X]$). Typical when the support's geometry ties the means by a linear relation.

## Key takeaways
- **Sketch the triangular support first.** Limits depend on which variable you integrate first. Getting this wrong is the #1 error source.
- Notice we're estimating **X from Y** here, so the formula uses Var(Y) in the denominator (not Var(X)).
- LMSE is a 2-D projection — 5 numbers are all you need.

## Related
- [[linear-mmse-estimation]]
- [[lmse-discrete-pmf]] — the discrete version
- [[mmse-vs-lmse-erlang]] — where MMSE and LMSE agree
