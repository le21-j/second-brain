---
title: Linear MMSE Estimation (LMSE / LLS)
type: concept
course:
  - "[[eee-350]]"
tags: [estimation, lmse, lls, linear, moments]
sources:
  - "[[homework-2026-04-23-eee-350-hw7]]"
  - "[[slides-43.5-bayesian-inference]]"
created: 2026-04-24
updated: 2026-05-06
---

# Linear MMSE Estimation (LMSE / LLS)

## In one line
The **best linear estimator** of $Y$ from $X$ has the form $\hat Y_L(X) = aX + b$ with
$a^* = \text{Cov}(X,Y)/\text{Var}(X)$ and $b^* = E[Y] - a^*\cdot E[X]$.
Minimum MSE is $\text{Var}(Y)\cdot(1 - \rho^2)$.

## Naming (three names, one concept)
- **LMSE** = Linear Minimum MSE — the modern textbook name.
- **LLS** = Linear Least Squares — Wiley textbook / [[lms-estimation]] page name.
- **Linear MMSE** = the fully spelled-out name.

All three refer to the **same estimator**: the best affine function of $X$. Contrast with the **unrestricted MMSE** estimator $\hat Y_M(X) = E[Y \mid X]$, which allows any function (see [[lms-estimation]]).

## Example first
From HW7 Problem 12.2.3 — discrete joint PMF.

After computing marginals and moments:
- $E[X] = 0$, $\text{Var}(X) = 1/2$
- $E[Y] = -1/16$, $\text{Var}(Y) = 493/768$
- $\text{Cov}(X,Y) = 5/16$

Then
$$a^* = \frac{5/16}{1/2} = \frac{5}{8}, \qquad b^* = -\frac{1}{16} - \frac{5}{8}\cdot 0 = -\frac{1}{16}.$$
$$\boxed{\hat Y_L(X) = \tfrac{5}{8}X - \tfrac{1}{16}}.$$

Minimum MSE:
$$e_L^* = \text{Var}(Y) - \frac{\text{Cov}(X,Y)^2}{\text{Var}(X)} = \tfrac{493}{768} - \tfrac{150}{768} = \tfrac{343}{768} \approx 0.447.$$

Only **five numbers** were used: $E[X]$, $E[Y]$, $\text{Var}(X)$, $\text{Var}(Y)$, $\text{Cov}(X,Y)$. The rest of the joint distribution is irrelevant to linear estimation.

## The formulas (memorize)

**Estimating Y from X:**
$$\hat Y_L(X) = E[Y] + \frac{\text{Cov}(X,Y)}{\text{Var}(X)}\bigl(X - E[X]\bigr).$$

**Coefficient form:**
$$a^* = \frac{\text{Cov}(X,Y)}{\text{Var}(X)}, \qquad b^* = E[Y] - a^*\,E[X].$$

**Minimum MSE:**
$$e_L^* = \text{Var}(Y)(1 - \rho_{XY}^2) = \text{Var}(Y) - \frac{\text{Cov}(X,Y)^2}{\text{Var}(X)},$$
where $\rho_{XY} = \text{Cov}(X,Y) / (\sigma_X \sigma_Y)$ is the [[correlation-coefficient]].

## Why only 5 numbers?
Think of random variables as vectors in a Hilbert space with inner product $\langle U,V\rangle = E[UV]$. The LMSE estimate is the **orthogonal projection** of $Y$ onto the 2-dimensional subspace $\text{span}\{1, X\}$. The residual $Y - \hat Y_L$ is orthogonal to 1 (mean zero) and orthogonal to $X$ (uncorrelated) — exactly two conditions, matching the two coefficients $a, b$.

Projection uses only inner products: $\langle Y,1\rangle = E[Y]$, $\langle Y,X\rangle = E[XY]$, $\langle X,X\rangle = E[X^2]$. The Gram matrix has $\text{Var}(X)$, $\text{Var}(Y)$, $\text{Cov}(X,Y)$ baked in. No other moments needed.

## Continuous example
From HW7 Problem 12.2.4: $f_{X,Y}(x,y) = 2(y + x)$ on $0 \leq x \leq y \leq 1$, else 0.

Estimating $X$ from $Y$:
- $f_Y(y) = 3y^2$ on $[0,1]$ $\to$ $E[Y] = 3/4$, $\text{Var}(Y) = 3/80$.
- $f_X(x) = 1 + 2x - 3x^2$ on $[0,1]$ $\to$ $E[X] = 5/12$.
- $E[XY] = 1/3$ $\to$ $\text{Cov}(X,Y) = 1/48$.

$$a^* = \frac{1/48}{3/80} = \frac{5}{9}, \qquad b^* = \tfrac{5}{12} - \tfrac{5}{9}\cdot\tfrac{3}{4} = 0.$$
$$\boxed{\hat X_L(Y) = \tfrac{5}{9}\,Y.}$$

**$b^* = 0$** here means the regression line passes through the origin — usually geometric (both means tied by the support shape).

## When LMSE = MMSE
**Equality holds iff $E[Y \mid X]$ is an affine function of $X$.**

Two famous sufficient conditions:
1. **$(X, Y)$ is jointly Gaussian** — the canonical case.
2. **The setup yields a linear conditional mean by accident** — HW7 Problem 12.2.6 with $X \sim \text{Erlang}(2,\lambda)$ and $Y \mid X \sim \text{Uniform}(0, X)$. Both $E[Y\mid X] = X/2$ and $E[X\mid Y] = Y + 1/\lambda$ are affine, so LMSE hits MMSE exactly.

When $E[Y \mid X]$ is non-linear, LMSE > MMSE strictly — the gap measures how much nonlinear structure the joint distribution carries.

## Common mistakes
- **Mixing up which variable is being estimated.** $\hat Y_L(X)$ divides by $\text{Var}(X)$; $\hat X_L(Y)$ divides by $\text{Var}(Y)$. Always check the denominator matches the observation.
- **Forgetting the mean shift.** The $+E[Y]$ and $-a^*E[X]$ terms are crucial when means are non-zero; $b^*$ is *not* automatically zero.
- **Getting the support wrong on continuous joints.** Always sketch the region. Inner limits often depend on the outer variable (triangular support).
- **$\rho^2$ as a probability.** It's the **fraction of $\text{Var}(Y)$ explained linearly by $X$** — between 0 and 1, but not a probability.

## Related
- [[lms-estimation]] — the unrestricted MMSE estimator E[Y|X], parent concept
- [[covariance]], [[correlation-coefficient]], [[variance-of-a-sum]]
- [[linear-regression]] — the frequentist / data version
- [[bivariate-gaussian]] — the case where LMSE = MMSE always

## Formulas
- [[inference-formulas]] — collected

## Examples
- [[lmse-discrete-pmf]] — HW7 12.2.3 (discrete)
- [[lmse-continuous-pdf]] — HW7 12.2.4 (continuous)
- [[mmse-vs-lmse-erlang]] — HW7 12.2.6 (all four estimators on one joint)

## Practice
- [[inference-set-01]]
