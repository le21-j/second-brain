---
title: Confidence Interval
type: concept
course:
  - "[[eee-350]]"
tags: [confidence-interval, estimation, classical-statistics]
sources:
  - "[[slides-44-mle-ci]]"
created: 2026-04-21
updated: 2026-05-06
---

# Confidence Interval

## In one line
An interval $[L(X), U(X)]$ constructed from data such that $P(L \leq \theta \leq U) = 1 - \alpha$ — i.e. it **covers the true $\theta$ with probability $1 - \alpha$** across repeated experiments.

## Example first
You measure $n = 100$ i.i.d. samples with $\sigma = 2$ (known), sample mean $\bar x = 10.3$. 95% confidence interval for $\mu$:
$$\bar X_n \pm z_{0.025}\cdot\frac{\sigma}{\sqrt{n}} = 10.3 \pm 1.96\cdot\frac{2}{\sqrt{100}} = 10.3 \pm 0.392$$
$\to [9.91, 10.69]$.

Means: "If I repeated this experiment many times, 95% of the intervals I'd construct would contain the true $\mu$."

## The formula (Gaussian mean, $\sigma$ known)

$$\text{CI}_{1-\alpha} = \bar X_n \pm z_{\alpha/2}\cdot\frac{\sigma}{\sqrt{n}}$$

Key pieces:
- **$\bar x$:** your point estimate.
- **$z_{\alpha/2}$:** critical value from standard normal (1.96 for 95%, 2.576 for 99%). See [[standard-normal-table]].
- **$\sigma/\sqrt{n}$:** standard error of the mean. Shrinks as $1/\sqrt{n}$.

## Why this works (CLT route)
- By CLT, $\bar x \approx N(\mu, \sigma^2/n)$ for large $n$.
- So $(\bar x - \mu)/(\sigma/\sqrt{n}) \sim N(0, 1)$.
- $P(|Z| \leq z_{\alpha/2}) = 1 - \alpha \to P(-z_{\alpha/2} \leq (\bar x - \mu)/(\sigma/\sqrt{n}) \leq z_{\alpha/2}) = 1 - \alpha$.
- Rearranging: $P(\bar x - z_{\alpha/2}\cdot\sigma/\sqrt{n} \leq \mu \leq \bar x + z_{\alpha/2}\cdot\sigma/\sqrt{n}) = 1 - \alpha$.

**Because of CLT, this works even when data isn't Gaussian** — as long as $n$ is moderately large.

## When $\sigma$ is unknown
Replace $\sigma$ with sample standard deviation $s$ and use **t-distribution** with $n-1$ degrees of freedom:
$$\bar X_n \pm t_{\alpha/2, n-1}\cdot\frac{s}{\sqrt{n}}$$

For large $n$, $t \approx z$ ($t_{0.025, 100} \approx 1.98$). For small $n$, $t > z$ — interval is wider to account for uncertainty in $\sigma$.

## Interpretation — tricky!
95% CI does **NOT** mean "there is a 95% probability that $\mu$ is in this particular interval". In classical (frequentist) stats, $\mu$ is a **fixed number**, not random. Once the interval is computed, $\mu$ is either in it or not — there's no probability.

Correct interpretation: "95% of the time when I run this procedure, the interval I produce will contain $\mu$." A statement about the **procedure**, not about the specific interval.

(In Bayesian inference, the analog is a **credible interval**, and that one IS a probability statement about $\theta$ given the posterior.)

## How $n$ affects interval width
- Width scales as **$1/\sqrt{n}$** — to halve the interval, need $4\times$ the data.
- For 95% CI width of $\varepsilon$: $n \approx (1.96\cdot\sigma/\varepsilon)^2$.
- Polling for $\pm 3\%$ at 95%: $n \approx 1067$ (with $p(1-p) \leq 1/4$).

## Common mistakes
- **Thinking "95% chance $\mu$ is in $[a, b]$"** — wrong in classical stats. Right in Bayesian credible intervals.
- **Using $z$ when $\sigma$ is unknown** — should use $t$. (For large $n$ they're close; for small $n$ they differ noticeably.)
- **Forgetting CLT dependence.** For very small $n$ on non-Gaussian data, the nominal coverage can be off.

## Related
- [[maximum-likelihood-estimation]]
- [[central-limit-theorem]]
- [[standard-normal-table]]
- [[neyman-pearson-test]] (same z-values show up)

## Practice
- [[inference-set-01]]
