---
title: Conditional Variance
type: concept
course: [[eee-350]]
tags: [variance, conditional-expectation]
sources: [[slides-40-conditional-expectation]]
created: 2026-04-21
updated: 2026-04-26
---

# Conditional Variance

## In one line
$\text{Var}(X | Y) = E[(X - E[X | Y])^2 | Y]$ — the **random variable** that measures the residual uncertainty about $X$ after knowing $Y$.

## Example first
$(X, Y)$ jointly Gaussian with $\rho = 0.8$, $\sigma_X = 10$, $\sigma_Y = 20$. Given $Y = 30$, what's $\text{Var}(X | Y = 30)$?

For Gaussians: $\text{Var}(X | Y) = \sigma_X^2 \cdot (1 - \rho^2) = 100 \cdot (1 - 0.64) =$ **$36$** — constant in $Y$. Conditional std is $6$. Knowing $Y$ reduced $X$'s std from $10$ to $6$.

Note: $\text{Var}(X | Y)$ for jointly Gaussian **does not depend on the value of $Y$** — unusual; for most other distributions it does.

## The idea
Just like conditional expectation, the conditional variance is a **random variable** (function of $Y$):
$$\text{Var}(X | Y) = E\!\left[\,(X - E[X | Y])^2 \,\big|\, Y\,\right]$$

Equivalent form:
$$\text{Var}(X | Y) = E[X^2 | Y] - (E[X | Y])^2$$

## Law of Total Variance
A beautiful identity decomposing total variance into two pieces:
$$\boxed{\,\text{Var}(X) = E[\text{Var}(X | Y)] + \text{Var}(E[X | Y])\,}$$

**Interpretation:**
- **$E[\text{Var}(X | Y)]$** = "average residual uncertainty" after knowing $Y$. Small if $Y$ is a good predictor.
- **$\text{Var}(E[X | Y])$** = how much the conditional mean **itself varies** as $Y$ varies. Small if the conditional mean doesn't depend much on $Y$.

Total variance = within-group + between-group variance (ANOVA decomposition).

## Derivation sketch
From the definition:
$$\text{Var}(X) = E[(X - E[X])^2]$$
Split $X - E[X]$ as $(X - E[X | Y]) + (E[X | Y] - E[X])$:
$$(X - E[X])^2 = (X - E[X|Y])^2 + 2(X - E[X|Y])(E[X|Y] - E[X]) + (E[X|Y] - E[X])^2$$
Take expectation:
- First term $\to E[\text{Var}(X | Y)]$ by iterated expectations.
- Middle cross term $\to 0$ (by iterated conditioning).
- Third term $\to \text{Var}(E[X | Y])$.

## Worked use — random sums
If $S = \sum_{i=1}^N X_i$ with $N, X_i$ independent:
- $E[S | N] = N \cdot \mu_X \to E[S] = E[N] \cdot \mu_X$.
- $\text{Var}(S | N) = N \cdot \sigma_X^2$.
- Then by law of total variance:
  $$\text{Var}(S) = E[N\sigma_X^2] + \text{Var}(N \cdot \mu_X) = E[N]\sigma_X^2 + \mu_X^2\,\text{Var}(N)$$
- The famous "two-term" variance of a random sum. See [[sum-of-random-number-of-rvs]].

## Common mistakes
- **$\text{Var}(X | Y) = \text{Var}(X) - \text{Var}(Y)$.** Nonsense — variance isn't additive like that.
- Forgetting the **second term** of the law of total variance. Writing $\text{Var}(X) \approx E[\text{Var}(X | Y)]$ understates total variance.
- Treating $\text{Var}(X | Y)$ as a number when $Y$ isn't specified. It's a random variable.

## Related
- [[conditional-expectation]]
- [[law-of-total-variance]] — shares this page but has its own stub
- [[sum-of-random-number-of-rvs]]

## Practice
- [[prob-fundamentals-set-01]]
