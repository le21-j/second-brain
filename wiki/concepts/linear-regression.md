---
title: Linear Regression
type: concept
course:
  - "[[eee-350]]"
tags: [regression, least-squares, mle]
sources:
  - "[[slides-46-regression]]"
created: 2026-04-21
updated: 2026-05-06
---

# Linear Regression

## In one line
Fit a line $y = a\cdot x + b$ to noisy $(x_i, y_i)$ data by minimizing the sum of squared vertical residuals — which turns out to be the **MLE** under Gaussian noise.

## Example first
You have 5 $(x, y)$ data points: $(1, 2), (2, 3.9), (3, 6.1), (4, 7.8), (5, 10.3)$.

Compute $\bar x = 3$, $\bar y = 6.02$, $\sum(x_i - \bar x)^2 = 10$, $\sum(x_i - \bar x)(y_i - \bar y) = 20.8$.

$$\hat a = \frac{20.8}{10} = 2.08, \quad \hat b = 6.02 - 2.08\cdot3 = -0.22$$

Best-fit line: $y \approx$ **$2.08\cdot x - 0.22$**. Plug in $x = 6$ to predict $y \approx 12.26$.

## The model
$$y_i = a\cdot x_i + b + \varepsilon_i, \quad \varepsilon_i \overset{\text{iid}}{\sim} N(0, \sigma^2)$$

Unknowns to estimate: $a$ (slope), $b$ (intercept), and optionally $\sigma^2$ (noise variance).

## Least-squares as MLE

Likelihood:
$$L(a, b) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\tfrac{(y_i - ax_i - b)^2}{2\sigma^2}\right)$$

Log-likelihood:
$$\ell(a, b) = -\tfrac{n}{2}\log(2\pi\sigma^2) - \tfrac{1}{2\sigma^2}\sum (y_i - ax_i - b)^2$$

Maximizing $\ell \iff$ minimizing $\sum(y_i - ax_i - b)^2$. That's **least squares**.

So LS isn't arbitrary — it's what **Gaussian-noise MLE** gives you. If noise were Laplace-distributed, you'd minimize $\sum|y_i - ax_i - b|$ instead.

## Closed-form solution

Setting $\partial\ell/\partial a = 0$ and $\partial\ell/\partial b = 0$:

$$\hat a = \frac{\sum (x_i - \bar x)(y_i - \bar y)}{\sum (x_i - \bar x)^2} = \frac{\text{sample Cov}(X, Y)}{\text{sample Var}(X)}$$

$$\hat b = \bar y - \hat a\,\bar x$$

**Note the numerator**: sample covariance. Slope = covariance / variance.

Connection to correlation: if you **standardize** $x$ and $y$ (subtract mean, divide by sample std), the slope equals **$\hat\rho$** (sample correlation).

## Multi-variable (multiple regression)

Generalizing to $p$ predictors: $y = X\cdot\beta + \varepsilon$. Matrix solution:
$$\hat\beta = (X^T X)^{-1} X^T y$$

(That's a whole topic — not in the slide set, but essential if you move to ML/real data.)

## $R^2$ — proportion of variance explained

$$R^2 = 1 - \frac{\sum (y_i - \hat y_i)^2}{\sum (y_i - \bar y)^2}$$

$R^2 = 0$: model no better than just predicting $\bar y$. $R^2 = 1$: perfect fit. Equals $\rho^2$ for simple linear regression.

Connection to [[law-of-total-variance]]: $\text{Var}(Y) = \text{Var}(E[Y \mid X]) + E[\text{Var}(Y \mid X)]$. $R^2 = \text{Var}(\hat Y)/\text{Var}(Y) =$ "fraction of variance explained by $X$".

## Common mistakes
- **Extrapolating.** Fitting on $x \in [0, 10]$ and predicting at $x = 100$. The linear assumption can fail badly outside the training range.
- **Ignoring heteroskedasticity.** Noise variance constant? If not ($\sigma$ depends on $x$), LS is no longer optimal.
- **Outliers dominating.** Squared loss is very sensitive to extreme points. Consider robust regression (e.g. Huber loss) if you have outliers.
- **$R^2$ comparison across models.** Higher-dimensional models always have higher $R^2$ — use adjusted $R^2$ to penalize extra parameters.

## Related
- [[maximum-likelihood-estimation]] — LS is MLE under Gaussian noise
- [[least-squares]]
- [[covariance]] / [[correlation-coefficient]]
- [[power-law-regression]]
- [[bivariate-gaussian]] — regression line = conditional mean
- [[lms-estimation]]

## Practice
- [[inference-set-01]]
