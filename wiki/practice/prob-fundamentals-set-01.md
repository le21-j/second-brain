---
title: Probability Fundamentals — Practice Set 01
type: practice
course:
  - "[[eee-350]]"
tags: [practice, covariance, multivariate, conditional-expectation]
concept:
  - "[[covariance]]"
  - "[[conditional-expectation]]"
difficulty: mixed
created: 2026-04-21
updated: 2026-05-06
---

# Probability Fundamentals — Practice Set 01

**Scope:** decks 38–40. Moments, correlation, multivariate, conditional expectation. Attempt before peeking. Log your misses in [[prob-gotchas]].

---

### 1. Covariance from definition [easy]
$X$ and $Z$ are independent with $\text{Var}(X) = 4$, $\text{Var}(Z) = 9$. Find $\text{Cov}(X, X + Z)$.

<details><summary>Solution</summary>

$\text{Cov}(X, X + Z) = \text{Cov}(X, X) + \text{Cov}(X, Z) = \text{Var}(X) + 0 =$ **4**.

See [[covariance-of-x-and-x-plus-z]].

</details>

---

### 2. Correlation from covariance [easy]
Same setup: $\text{Var}(X) = 4$, $\text{Var}(Z) = 9$, $X \perp Z$, $Y = X + Z$. Find $\rho_{XY}$.

<details><summary>Solution</summary>

$\sigma_X = 2$, $\sigma_Y = \sqrt{\text{Var}(X) + \text{Var}(Z)} = \sqrt{13}$.
$\rho = \text{Cov}(X, Y) / (\sigma_X\cdot\sigma_Y) = 4 / (2\cdot\sqrt{13}) = 2/\sqrt{13} \approx$ **0.555**.

See [[correlation-coefficient]].

</details>

---

### 3. Variance of a weighted sum [medium]
$X, Y$ have $\text{Var}(X) = 1$, $\text{Var}(Y) = 4$, $\rho_{XY} = 0.5$. Find $\text{Var}(2X + 3Y)$.

<details><summary>Solution</summary>

$\text{Cov}(X, Y) = \rho\cdot\sigma_X\cdot\sigma_Y = 0.5\cdot 1\cdot 2 = 1$.

$\text{Var}(2X + 3Y) = 4\cdot\text{Var}(X) + 9\cdot\text{Var}(Y) + 2\cdot 2\cdot 3\cdot\text{Cov}(X, Y) = 4 + 36 + 12 =$ **52**.

See [[variance-of-a-sum]].

</details>

---

### 4. Uncorrelated $\neq$ independent [medium]
Let $X \sim \text{Uniform}(-1, 1)$. Let $Y = X^2$. Compute $\text{Cov}(X, Y)$ and comment on whether $X, Y$ are independent.

<details><summary>Solution</summary>

- $E[X] = 0$.
- $E[Y] = E[X^2] = 1/3$.
- $E[XY] = E[X^3] = 0$ (by symmetry of $X$).
- $\text{Cov}(X, Y) = E[XY] - E[X]\cdot E[Y] = 0 - 0\cdot(1/3) =$ **0**.

So $X$ and $Y$ are **uncorrelated**. But $Y = X^2$ is a **deterministic function** of $X$, so they are absolutely not independent. Classic counter-example.

See [[independent-vs-uncorrelated]].

</details>

---

### 5. Bivariate Gaussian conditional mean [medium]
$(X, Y)$ is bivariate Gaussian with $\mu_X = 0$, $\mu_Y = 0$, $\sigma_X = 1$, $\sigma_Y = 2$, $\rho = 0.5$. Find $E[Y \mid X = 2]$.

<details><summary>Solution</summary>

$$E[Y | X] = \mu_Y + \rho\frac{\sigma_Y}{\sigma_X}(X - \mu_X) = 0 + 0.5\cdot\frac{2}{1}\cdot(2 - 0) = \boxed{2}$$

See [[bivariate-gaussian]].

</details>

---

### 6. Conditional variance, Gaussian [medium]
Same setup. Find $\text{Var}(Y \mid X = 2)$.

<details><summary>Solution</summary>

For jointly Gaussian: $\text{Var}(Y \mid X) = \sigma_Y^2\cdot(1 - \rho^2) = 4\cdot(1 - 0.25) =$ **3**.

Notice: doesn't depend on the value of $X$. Special to Gaussians.

See [[bivariate-gaussian]], [[conditional-variance]].

</details>

---

### 7. Max of i.i.d. uniforms [medium]
$X_1, \ldots, X_5$ are i.i.d. $\text{Uniform}(0, 1)$. Find $P(\max > 0.9)$ and the PDF of the max.

<details><summary>Solution</summary>

$F(t) = t$ for $t \in [0, 1]$. So $F_{\max}(t) = t^5$ and $f_{\max}(t) = 5t^4$.

$P(\max > 0.9) = 1 - F_{\max}(0.9) = 1 - 0.9^5 \approx 1 - 0.59 =$ **0.41**.

See [[max-of-iid]].

</details>

---

### 8. Iterated expectations, random sum [medium]
$N \sim \text{Geometric}(p)$ with $P(N = k) = (1-p)^{k-1}\cdot p$ for $k = 1, 2, \ldots$ (so $E[N] = 1/p$). Given $N$, $X_1, \ldots, X_N$ are i.i.d. with mean $\mu$, variance $\sigma^2$. Find $E[S]$ where $S = X_1 + \ldots + X_N$.

<details><summary>Solution</summary>

$E[S] = E[N]\cdot\mu =$ **$\mu/p$**.

See [[sum-of-random-number-of-rvs]] and [[iterated-expectations]].

</details>

---

### 9. Variance of a random sum [hard]
Same setup with Geometric $N$. $\text{Var}(N) = (1 - p)/p^2$. Find $\text{Var}(S)$.

<details><summary>Solution</summary>

$$\text{Var}(S) = E[N]\sigma^2 + \mu^2\,\text{Var}(N) = \frac{\sigma^2}{p} + \mu^2\cdot\frac{1 - p}{p^2}$$

Combined: $(\sigma^2 p + \mu^2(1 - p)) / p^2$.

See [[sum-of-random-number-of-rvs]].

</details>

---

### 10. Law of total variance [hard]
Classes A and B have means 80, 60 and **equal** std 5. 50% of students in each class. Find total variance of a random student's score.

<details><summary>Solution</summary>

- $E[\text{Var}(\text{score} \mid \text{class})] = 25$.
- $\text{Var}(E[\text{score} \mid \text{class}]) = \text{Var of } (80 \text{ or } 60, \text{ each } p=0.5) = 100$.
- Total $= 25 + 100 =$ **125**. Std $\approx 11.2$.

See [[law-of-total-variance]].

</details>

---

## Your attempts

_(Log attempts, date, what you missed, pattern to remember.)_
