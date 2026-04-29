---
title: MMSE vs LMSE with Erlang Prior (HW7 12.2.6)
type: example
course: [[eee-350]]
tags: [mmse, lmse, estimation, erlang, worked-example]
concept: [[linear-mmse-estimation]], [[lms-estimation]]
sources: [[homework-2026-04-23-eee-350-hw7]]
created: 2026-04-24
updated: 2026-04-26
---

# MMSE vs LMSE with Erlang Prior — HW7 Problem 12.2.6

## Problem
$X$ has second-order Erlang PDF:
$$f_X(x) = \lambda^2 x e^{-\lambda x}, \quad x \ge 0.$$
Given $X = x$, $Y \sim \text{Uniform}(0, x)$. Find:

- **(a)** $\hat Y_M(x) = E[Y \mid X = x]$ — MMSE of $Y$ given $X$.
- **(b)** $\hat X_M(y) = E[X \mid Y = y]$ — MMSE of $X$ given $Y$.
- **(c)** $\hat Y_L(X)$ — LMSE of $Y$ given $X$.
- **(d)** $\hat X_L(Y)$ — LMSE of $X$ given $Y$.

## The big picture (before computing)

| | MMSE (unrestricted) | LMSE (linear only) |
|---|---|---|
| Form | $E[\cdot \mid \cdot]$ (any function) | $aX + b$ |
| Needs | full conditional distribution | first + second moments |
| Equality condition | LMSE $=$ MMSE iff $E[\cdot \mid \cdot]$ is affine |

**Spoiler:** both conditional means here turn out to be affine, so MMSE = LMSE exactly.

## Erlang $(2, \lambda)$ facts (needed throughout)
$$E[X] = \tfrac{2}{\lambda}, \quad \text{Var}(X) = \tfrac{2}{\lambda^2}, \quad E[X^2] = \tfrac{6}{\lambda^2}.$$

## (a) MMSE of Y given X

Since $Y \mid X = x \sim \text{Uniform}(0, x)$:
$$\boxed{\hat y_M(x) = E[Y \mid X = x] = \tfrac{x}{2}.}$$

No integration needed — conditional distribution given.

## (b) MMSE of X given Y — via Bayes

**Step 1 — Joint PDF.**
$$f_{X,Y}(x,y) = f_{Y|X}(y|x)\,f_X(x) = \tfrac{1}{x}\cdot\lambda^2 x e^{-\lambda x} = \lambda^2 e^{-\lambda x}, \quad 0 \le y \le x.$$

**Step 2 — Marginal of Y.**
$$f_Y(y) = \int_y^\infty \lambda^2 e^{-\lambda x}\,dx = \lambda e^{-\lambda y}, \quad y \ge 0.$$
Pretty: **$Y \sim \text{Exp}(\lambda)$**.

**Step 3 — Conditional of X given Y.**
$$f_{X|Y}(x|y) = \frac{\lambda^2 e^{-\lambda x}}{\lambda e^{-\lambda y}} = \lambda e^{-\lambda(x - y)}, \quad x \ge y.$$
So $(X - y) \mid Y = y \sim \text{Exp}(\lambda)$ — memorylessness in action.

**Step 4 — Conditional mean.**
$$\boxed{\hat x_M(y) = E[X \mid Y = y] = y + \tfrac{1}{\lambda}.}$$

**Linear in y.** So LMSE will match in part (d).

## (c) LMSE of Y given X

**Moments needed:** E[X], Var(X), E[Y], E[XY].

**E[Y]** via tower property (conditioning on X first):
$$E[Y] = E\bigl[E[Y|X]\bigr] = E[\tfrac{X}{2}] = \tfrac{1}{\lambda}.$$

**E[XY]** via tower again:
$$E[XY] = E\bigl[X\cdot E[Y|X]\bigr] = E\bigl[\tfrac{X^2}{2}\bigr] = \tfrac{1}{2}\cdot\tfrac{6}{\lambda^2} = \tfrac{3}{\lambda^2}.$$

**Covariance:**
$$\text{Cov}(X,Y) = \tfrac{3}{\lambda^2} - \tfrac{2}{\lambda}\cdot\tfrac{1}{\lambda} = \tfrac{1}{\lambda^2}.$$

**LMSE coefficients:**
$$a^* = \frac{\text{Cov}(X,Y)}{\text{Var}(X)} = \frac{1/\lambda^2}{2/\lambda^2} = \tfrac{1}{2}.$$
$$b^* = E[Y] - a^*\,E[X] = \tfrac{1}{\lambda} - \tfrac{1}{2}\cdot\tfrac{2}{\lambda} = 0.$$

$$\boxed{\hat Y_L(X) = \tfrac{X}{2}.}$$

Matches (a) exactly. ✓

## (d) LMSE of X given Y

**$\text{Var}(Y)$:** Since $Y \sim \text{Exp}(\lambda)$:
$$\text{Var}(Y) = \tfrac{1}{\lambda^2}.$$

**LMSE coefficients:**
$$a^* = \frac{\text{Cov}(X,Y)}{\text{Var}(Y)} = \frac{1/\lambda^2}{1/\lambda^2} = 1.$$
$$b^* = E[X] - a^*\,E[Y] = \tfrac{2}{\lambda} - \tfrac{1}{\lambda} = \tfrac{1}{\lambda}.$$

$$\boxed{\hat X_L(Y) = Y + \tfrac{1}{\lambda}.}$$

Matches (b) exactly. ✓

## The punchline

Both conditional means were **affine in the observation**:
- $E[Y \mid X] = X/2$ (affine in $X$ with $b = 0$)
- $E[X \mid Y] = Y + 1/\lambda$ (affine in $Y$)

**When $E[\cdot \mid \cdot]$ is affine, LMSE hits MMSE exactly.** That's the theorem, confirmed numerically in parts (c) and (d).

## Key takeaways
- **Tower property is the shortcut** for computing E[Y] and E[XY] when Y | X is simple (here Uniform).
- **Memorylessness of the Exponential** made the posterior of $X$ clean: $(X - y) \mid Y$ is again $\text{Exp}(\lambda)$.
- **Affine conditional mean ⇒ LMSE = MMSE.** A useful diagnostic — if your MMSE comes out linear in the observation, you know LMSE matches it and you've gained nothing by restricting to linear.

## Related
- [[linear-mmse-estimation]] — the linear-only estimator
- [[lms-estimation]] — the unrestricted MMSE (parent)
- [[iterated-expectations]] — the tower property used here
- [[bivariate-gaussian]] — the other famous case where LMSE = MMSE (for structural reasons)
- [[conditional-expectation]]
