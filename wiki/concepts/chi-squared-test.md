---
title: Chi-Squared Test (for Variance)
type: concept
course: [[eee-350]]
tags: [chi-squared, hypothesis-testing, variance]
sources: [[slides-45-neyman-pearson]]
created: 2026-04-21
updated: 2026-04-26
---

# Chi-Squared Test (for Variance)

## In one line
To test a hypothesis about a Gaussian **variance**, use the statistic $\sum(x_i - \mu)^2/\sigma^2$ which follows a **chi-squared distribution** with $n$ degrees of freedom under $H_0$.

## The chi-squared distribution ($\chi^2$)
If $Z_1, \ldots, Z_k$ are i.i.d. standard normal, then **$\sum Z_i^2 \sim \chi^2(k)$** — the chi-squared distribution with $k$ degrees of freedom.

- Mean $= k$, variance $= 2k$.
- For even $k$, it's closely related to the Erlang distribution.
- Tables (or numerical software) give $\chi^2_\alpha(k) =$ upper-$\alpha$ quantile.

## Test setup — known mean $\mu$

$H_0: \sigma^2 = \sigma_0^2$ vs $H_1: \sigma^2 > \sigma_0^2$.

Under $H_0$, $Z_i = (X_i - \mu)/\sigma_0 \sim N(0, 1)$, so:
$$T = \sum_{i=1}^n \left(\frac{X_i - \mu}{\sigma_0}\right)^2 \sim \chi^2(n)$$

Reject $H_0$ at level $\alpha$ if $T > \chi^2_\alpha(n)$.

## Test setup — unknown mean

Replace $\mu$ with $\bar x$ (sample mean). The statistic becomes:
$$T = \frac{1}{\sigma_0^2}\sum_{i=1}^n (X_i - \bar X)^2 \sim \chi^2(n-1)$$

One degree of freedom lost because we "used up" one d.f. to estimate $\mu$.

Reject $H_0$ if $T > \chi^2_\alpha(n-1)$.

## Why variance tests matter
- **Quality control:** is the variance of manufactured parts within spec?
- **Signal processing:** is the noise variance consistent with design assumption?
- **Risk management:** is the volatility above acceptable threshold?

## Common mistakes
- Using **$\chi^2(n)$** when the mean is estimated — should be **$\chi^2(n-1)$**.
- Forgetting the test is one-sided by default; if $H_1$ allows $\sigma^2 < \sigma_0^2$ too, use the lower tail or a two-sided version.
- Confusing the "chi-square test" for variance with the "chi-square goodness-of-fit test" — different applications, same distribution.

## Related
- [[neyman-pearson-test]]
- [[likelihood-ratio-test]]
- [[sample-variance]]
