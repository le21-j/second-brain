---
title: Inference — Practice Set 01
type: practice
course: [[eee-350]]
tags: [practice, bayesian, mle, hypothesis-testing]
concept: [[bayesian-inference]], [[maximum-likelihood-estimation]], [[neyman-pearson-test]]
difficulty: mixed
created: 2026-04-21
updated: 2026-04-26
---

# Inference — Practice Set 01

**Scope:** decks 43.5–45. Bayesian inference, MAP, LMS, MLE, confidence intervals, Neyman-Pearson, LRT. Attempt before peeking.

---

### 1. Bayes rule [easy]
A coin is drawn from a bag where 90% are fair ($p = 0.5$) and 10% are biased ($p = 0.8$). You flip 3 times and get 3 heads. What's the posterior probability the coin is biased?

<details><summary>Solution</summary>

- $P(3H \mid \text{fair}) = 0.5^3 = 0.125$.
- $P(3H \mid \text{biased}) = 0.8^3 = 0.512$.
- Numerator (biased) $= 0.512\cdot 0.1 = 0.0512$.
- Numerator (fair) $= 0.125\cdot 0.9 = 0.1125$.
- $P(\text{biased} \mid \text{data}) = 0.0512 / (0.0512 + 0.1125) = 0.0512/0.1637 \approx$ **0.313**.

Data shifted belief from 10% $\to$ 31%.

See [[bayesian-inference]].

</details>

---

### 2. MLE for Bernoulli [easy]
$n$ i.i.d. $\text{Bernoulli}(p)$ observations with sum $k$. Show the MLE of $p$ is $k/n$.

<details><summary>Solution</summary>

$L(p) = p^k (1-p)^{n-k}$. Log-likelihood: $k\cdot\log p + (n-k)\cdot\log(1-p)$.
Differentiate: $k/p - (n-k)/(1-p) = 0 \Rightarrow k(1-p) = (n-k)p \Rightarrow$ **$\hat p = k/n$**.

See [[maximum-likelihood-estimation]].

</details>

---

### 3. Confidence interval for mean [medium]
You collect $n = 64$ samples from a Gaussian with known $\sigma = 8$. Sample mean is $\bar x = 25$. Construct a 95% CI for $\mu$.

<details><summary>Solution</summary>

$\text{CI} = \bar x \pm z_{0.025}\cdot\sigma/\sqrt{n} = 25 \pm 1.96\cdot(8/8) = 25 \pm 1.96 \to$ **$[23.04, 26.96]$**.

See [[confidence-interval]].

</details>

---

### 4. MAP detection with unequal priors [medium]
Signal $\theta \in \{+1, -1\}$, priors $P(+1) = 0.8$, $P(-1) = 0.2$. Observation $X = \theta + N$, $N \sim N(0, 1)$. Where's the MAP threshold?

<details><summary>Solution</summary>

$$\tau = \frac{\sigma^2}{2}\ln\frac{\pi_-}{\pi_+} = \frac{1}{2}\ln\frac{0.2}{0.8} = \frac{1}{2}\ln(0.25) = \tfrac{-1.386}{2} = \boxed{-0.693}$$

Decide $+1$ if $X > -0.693$. Threshold pushed toward $-1$ because $+1$ is a priori more likely.

See [[map-detection]], [[map-detection-antipodal]].

</details>

---

### 5. Power of a test [medium]
$H_0: \mu = 0$, $H_1: \mu = 1$. $\sigma = 1$, $n = 9$. Test rejects if $\bar x > 0.5$. Find $\alpha$ and power ($1 - \beta$).

<details><summary>Solution</summary>

$\bar x \sim N(\mu, 1/9)$, so $\sigma_{\bar x} = 1/3$.

- $\alpha = P(\bar x > 0.5 \mid \mu = 0) = P(Z > (0.5 - 0)/(1/3)) = P(Z > 1.5) \approx$ **0.067**.
- Power $= P(\bar x > 0.5 \mid \mu = 1) = P(Z > (0.5 - 1)/(1/3)) = P(Z > -1.5) \approx$ **0.933**.
- $\beta \approx 0.067$.

Symmetric here because threshold is halfway between means.

See [[neyman-pearson-test]], [[type-i-error]], [[type-ii-error]].

</details>

---

### 6. LRT threshold [hard]
Testing $H_0: X \sim N(0, 1)$ vs $H_1: X \sim N(2, 1)$ with a single sample. Find the LRT threshold on $X$ for $\alpha = 0.05$.

<details><summary>Solution</summary>

$\Lambda(x) = \exp((x-2)^2/2 - \ldots$ wait, compute $p_1/p_0$):
$\Lambda(x) = \exp(-(x-2)^2/2)/\exp(-x^2/2) = \exp(2x - 2)$.

$\Lambda > \gamma \iff 2x - 2 > \log \gamma \iff$ **$x > \tau$** for threshold $\tau$ related to $\gamma$.

Under $H_0$, $X \sim N(0, 1)$. $\alpha = P(X > \tau \mid H_0) = 1 - \Phi(\tau) = 0.05 \Rightarrow$ **$\tau = 1.645$**.

Decision rule: reject $H_0$ if $X > 1.645$.

See [[likelihood-ratio-test]].

</details>

---

### 7. Testing variance [hard]
25 i.i.d. Gaussian samples with **unknown** mean. Sample statistic: $\sum(x_i - \bar x)^2 = 85$. Test $H_0: \sigma^2 = 4$ at $\alpha = 0.05$ (one-sided, $H_1: \sigma^2 > 4$).

<details><summary>Solution</summary>

Test statistic $T = \sum(x_i - \bar x)^2 / \sigma_0^2 = 85/4 = 21.25$.
Under $H_0$: $T \sim \chi^2(n - 1) = \chi^2(24)$.

Look up $\chi^2_{0.05}(24) \approx 36.42$.

$T = 21.25 < 36.42 \to$ **fail to reject $H_0$**. No evidence $\sigma^2 > 4$.

See [[chi-squared-test]].

</details>

---

### 8. LMS for jointly Gaussian [medium]
$(\theta, X)$ jointly Gaussian with $\mu_\theta = 2$, $\mu_X = 0$, $\sigma_\theta = 1$, $\sigma_X = 2$, $\rho = 0.6$. Find the LMS estimator of $\theta$ given $X = 1$.

<details><summary>Solution</summary>

$$\hat\theta_{LMS}(X) = \mu_\theta + \rho\,\frac{\sigma_\theta}{\sigma_X}(X - \mu_X) = 2 + 0.6\cdot\frac{1}{2}\cdot(1 - 0) = 2 + 0.3 = \boxed{2.3}$$

MSE $= \sigma_\theta^2(1 - \rho^2) = 1\cdot(1 - 0.36) =$ **0.64**.

See [[lms-estimation]], [[bivariate-gaussian]].

</details>

---

## Your attempts

_(Log attempts, date, what you missed, pattern to remember.)_
