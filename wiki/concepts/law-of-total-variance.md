---
title: Law of Total Variance
type: concept
course:
  - "[[eee-350]]"
tags: [variance, conditional-expectation, anova]
sources:
  - "[[slides-40-conditional-expectation]]"
created: 2026-04-21
updated: 2026-05-06
---

# Law of Total Variance

## In one line
$$\text{Var}(X) = E[\text{Var}(X | Y)] + \text{Var}(E[X | Y])$$
Total variance = expected conditional variance + variance of the conditional mean.

## Example first
Students in two classes take a test. Class A has mean 80, std 5. Class B has mean 60, std 5. Half the students are in each class.

- Conditional variance: $\text{Var}(\text{score} | \text{class}) = 25$ in both classes.
- **$E[\text{Var}(\text{score} | \text{class})] = 25$.** (Expected within-class variance.)
- Conditional mean $E[\text{score} | \text{class}]$ is 80 or 60 with equal prob.
- **$\text{Var}(E[\text{score} | \text{class}]) = ((80 - 70)^2 + (60 - 70)^2)/2 = 100$.** (Between-class variance.)

Total variance: $25 + 100 =$ **$125$**. (Std $\approx 11.2$.)

So the total variance has two sources:
- **Within-class** (residual noise within each class)
- **Between-class** (the classes themselves have different means)

## Geometric / ANOVA view
The decomposition is the **probability-theory version of ANOVA**:
- Total sum of squares = within-group sum of squares + between-group sum of squares
- Total variance = within-group (residual) variance + between-group variance (of group means)

## Why it matters
- **Building intuition for regression:** $R^2 = \text{Var}(\hat Y) / \text{Var}(Y) = 1 - \text{Var}(\text{residual})/\text{Var}(Y)$. The two terms in total-variance-law correspond to "explained by $Y$" and "unexplained" variance of $X$.
- **Random sums:** direct computation of $\text{Var}(S)$ where $S = \sum_{i=1}^N X_i$ with random $N$. See [[sum-of-random-number-of-rvs]].
- **LMS estimation:** MSE of the LMS estimator $E[X | Y]$ is exactly the first term $E[\text{Var}(X | Y)]$ — the unavoidable residual.

## Extreme cases
- **$Y$ is independent of $X$:** $E[X | Y] = E[X]$ constant $\to \text{Var}(E[X | Y]) = 0$. All variance is within-group. Makes sense — $Y$ tells you nothing.
- **$X$ is a deterministic function of $Y$:** $\text{Var}(X | Y) = 0$. All variance is between-group. Makes sense — knowing $Y$ pins $X$ down.
- **Generic intermediate case:** both terms are non-zero.

## Common mistakes
- Only using one of the two terms.
- Writing $\text{Var}(X) = \text{Var}(X | Y) + \text{Var}(Y)$ — that's not it. The first term is $E[\text{Var}(X | Y)]$ (an expectation), the second is $\text{Var}(E[X | Y])$ (a variance).

## Related
- [[conditional-expectation]]
- [[conditional-variance]]
- [[iterated-expectations]]
- [[sum-of-random-number-of-rvs]]
