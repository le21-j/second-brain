---
title: Likelihood Ratio Test (LRT)
type: concept
course: [[eee-350]]
tags: [hypothesis-testing, lrt]
sources: [[slides-45-neyman-pearson]]
created: 2026-04-21
updated: 2026-04-26
---

# Likelihood Ratio Test (LRT)

## In one line
Decide **$H_1$** if
$$\Lambda(x) = \frac{p(x | H_1)}{p(x | H_0)} > \gamma$$
where threshold $\gamma$ is chosen to hit your target false-alarm rate $\alpha$.

## Why it's optimal
**Neyman-Pearson lemma:** among all tests with Type I rate $\leq \alpha$, the LRT has **maximum power** (minimum Type II rate). No other test is uniformly better for simple-vs-simple hypotheses.

## Typical simplification
For many distributions, $\Lambda(x) > \gamma$ is equivalent to a threshold on a simpler **sufficient statistic**. Examples:

| Model | $H_0$ vs $H_1$ | $\Lambda$ reduces to |
|---|---|---|
| $N(\mu, \sigma^2)$ known $\sigma$ | $\mu = 0$ vs $\mu = 1$ | $\sum x_i > \tau$ (sum test) |
| $N(0, \sigma^2)$ test variance | $\sigma^2 = \sigma_0^2$ vs $\sigma^2 = \sigma_1^2$ (with $\sigma_1 > \sigma_0$) | $\sum x_i^2 > \tau$ (chi-square test) |
| $\text{Exp}(\lambda)$ | $\lambda = \lambda_0$ vs $\lambda = \lambda_1$ (with $\lambda_1 < \lambda_0$) | $\bar x > \tau$ |

The algebra: take log of $\Lambda$, expand with the specific PDF, group terms. Usually the "hard" statistic ($\Lambda$ itself) becomes a **simple linear or quadratic function** of the data plus constants that fold into $\gamma$.

## Worked example — Gaussian test of mean

$H_0: X \sim N(0, \sigma^2)$, $H_1: X \sim N(\mu_1, \sigma^2)$, with $\mu_1 > 0$ known.

$$\Lambda(x) = \frac{\exp(-(x-\mu_1)^2/(2\sigma^2))}{\exp(-x^2/(2\sigma^2))} = \exp\!\left(\frac{2\mu_1 x - \mu_1^2}{2\sigma^2}\right)$$

$\Lambda(x) > \gamma \iff 2\mu_1 x/(2\sigma^2) > \log \gamma + \mu_1^2/(2\sigma^2) \iff$ **$x > \tau$** for some $\tau$.

So LRT is "decide $H_1$ if $x > \tau$". Simpler form.

## Extension to composite hypotheses
When $H_0$ and/or $H_1$ are **composite** (parameter range, not single point), use:
$$\Lambda(x) = \frac{\max_{\theta \in H_1} p(x | \theta)}{\max_{\theta \in H_0} p(x | \theta)}$$
called the **generalized LRT**. Not always optimal, but widely used.

## Common mistakes
- Using **natural log ratio** vs **log-ratio in some other base** — pick one and stick to it. Threshold values differ, but decision rule doesn't.
- Forgetting to solve for the threshold on the **simplified statistic** — don't keep computing $\Lambda$ when a sample-mean threshold gives the same result.

## Related
- [[neyman-pearson-test]]
- [[map-detection]] — the Bayesian cousin (adds prior)
