---
title: Neyman-Pearson Test
type: concept
course:
  - "[[eee-350]]"
tags: [hypothesis-testing, neyman-pearson, lrt]
sources:
  - "[[slides-45-neyman-pearson]]"
created: 2026-04-21
updated: 2026-05-06
---

# Neyman-Pearson Test

## In one line
Classical (no-prior) binary hypothesis testing: fix the **false-alarm rate** $\alpha$, then find the test that **maximizes power** (= minimizes miss rate) subject to that constraint. The answer is the **likelihood ratio test (LRT)**.

## Example first
Testing if a signal has mean 0 ($H_0$) vs. mean 1 ($H_1$). Data: single sample $X$ with $X \mid H_i \sim N(i, 1)$.

**Set significance level** $\alpha = 0.05$. Find threshold $\tau$ on $X$ such that $P(X > \tau \mid H_0) = 0.05$.
- Under $H_0$, $X \sim N(0, 1)$. $P(X > \tau) = 0.05 \to \tau = 1.645$ (from [[standard-normal-table]]).
- **Rule:** declare $H_1$ if $X > 1.645$, else $H_0$.
- Type II error (miss) probability: $P(X \leq 1.645 \mid H_1) = \Phi(1.645 - 1) = \Phi(0.645) \approx 0.74$. (Lousy with $n = 1$; get better with more data.)

**Power** (probability of correctly detecting $H_1$) = $1 - 0.74 = 0.26$.

## The framework

Two hypotheses:
- **$H_0$** (null): "status quo", presumed until evidence contradicts.
- **$H_1$** (alternative): "something new".

Two error types:

| Truth | Decision | Error |
|---|---|---|
| $H_0$ true | Reject $H_0$ | **Type I** (false alarm) |
| $H_1$ true | Accept $H_0$ | **Type II** (miss) |

**Terminology:**
- $\alpha = P(\text{Type I}) = P(\text{reject } H_0 \mid H_0 \text{ true}) =$ **significance level** / **false alarm rate**.
- $\beta = P(\text{Type II}) = P(\text{accept } H_0 \mid H_1 \text{ true})$.
- $1 - \beta =$ **power** of the test.

Neyman-Pearson: **fix $\alpha$**, minimize $\beta$.

## The LRT (Likelihood Ratio Test)

**Decide $H_1$ iff**
$$\Lambda(x) = \frac{p(x | H_1)}{p(x | H_0)} > \gamma$$

Threshold $\gamma$ chosen so that $P(\Lambda(X) > \gamma \mid H_0) = \alpha$.

**Neyman-Pearson Lemma:** among all tests with false-alarm rate $\leq \alpha$, the LRT has the **highest power**. The optimal test.

Often, $\Lambda(x) > \gamma$ simplifies to a threshold on some **sufficient statistic** (e.g. sample mean, sum of squares).

## Example — testing Gaussian mean (known $\sigma$)

$n$ i.i.d. samples $X_i$. $H_0: \mu = \mu_0$ vs. $H_1: \mu = \mu_1 > \mu_0$.

Likelihood ratio simplifies (after log) to:
$$\sum x_i > \tau$$
i.e. **reject $H_0$ if the sum is large enough**. Threshold $\tau$ chosen so $P(\sum x_i > \tau \mid \mu = \mu_0) = \alpha$.

Under $H_0$, $\sum x_i \sim N(n\mu_0, n\sigma^2)$. Threshold:
$$\tau = n\mu_0 + z_\alpha\cdot\sigma\sqrt{n}$$

Or equivalently on the sample mean:
$$\bar x > \mu_0 + z_\alpha\cdot\sigma/\sqrt{n}$$

Looks **exactly like a one-sided confidence-interval check**.

## Example — testing variance ($\chi^2$ test)

$H_0: \sigma^2 = \sigma_0^2$ vs. $H_1: \sigma^2 > \sigma_0^2$. Assume known mean $\mu$.

Statistic: $T = \sum(x_i - \mu)^2/\sigma_0^2 \sim$ **$\chi^2(n)$** under $H_0$. Reject $H_0$ if $T > \chi^2_\alpha(n)$ (upper $\alpha$ quantile of $\chi^2$ with $n$ df, from a chi-square table).

If $\mu$ is unknown, use $(x_i - \bar x)$ with $n-1$ df.

## Neyman-Pearson vs. Bayesian

| | Bayesian | Neyman-Pearson |
|---|---|---|
| Prior on $H_0, H_1$? | Required | None |
| What's minimized? | Total $P(\text{error})$ | $\beta$ for fixed $\alpha$ |
| When to use | Priors are meaningful | No priors, or asymmetric error costs |

## Common mistakes
- **Calling $\alpha$ "probability that $H_0$ is true".** No. $\alpha$ is $P(\text{reject } H_0 \text{ given } H_0 \text{ is true})$. $H_0$ being true isn't a probability event in classical stats.
- **Confusing one-sided with two-sided tests.** One-sided ($H_1: \mu > \mu_0$): use $z_\alpha = 1.645$ for $\alpha = 0.05$. Two-sided ($H_1: \mu \neq \mu_0$): split $\alpha$ in two, use $z_{\alpha/2} = 1.96$.
- **Interpreting low p-value as "$H_1$ is true".** A low p-value means the data is unlikely under $H_0$, not that $H_1$ is "probably true".

## Related
- [[type-i-error]], [[type-ii-error]]
- [[likelihood-ratio-test]]
- [[chi-squared-test]]
- [[bayesian-inference]] — the alternative
- [[standard-normal-table]]

## Practice
- [[inference-set-01]]
