---
title: Standard Normal Table (Φ)
type: concept
course: [[eee-350]]
tags: [gaussian, table, clt]
sources: [[slides-43-clt-apps]], [[slides-44-mle-ci]]
created: 2026-04-21
updated: 2026-04-26
---

# Standard Normal Table ($\Phi$)

## In one line
$\Phi(z) = P(Z \leq z)$ for $Z \sim N(0, 1)$ — tabulated in every stats textbook; you'll use it constantly for CLT-based probabilities and confidence intervals.

## Useful values to memorize

| $z$ | $\Phi(z)$ | $1 - \Phi(z)$ |
|---|---|---|
| $0$ | $0.500$ | $0.500$ |
| $1$ | $0.841$ | $0.159$ |
| $1.645$ | **$0.950$** | $0.050$ |
| $1.96$ | **$0.975$** | $0.025$ |
| $2$ | $0.977$ | $0.023$ |
| $2.326$ | **$0.990$** | $0.010$ |
| $2.576$ | **$0.995$** | $0.005$ |
| $3$ | $0.9987$ | $0.0013$ |

The **bolded** $z$-values are the standard "critical values" for confidence intervals and hypothesis tests:
- **$1.645$** — one-sided 95% (or two-sided 90%)
- **$1.96$** — **two-sided 95%** (the most-used one)
- **$2.326$** — one-sided 99%
- **$2.576$** — two-sided 99%

## Symmetry
$\Phi(-z) = 1 - \Phi(z)$. So you only need the $z \geq 0$ half of the table.

## Computing any normal probability
For $X \sim N(\mu, \sigma^2)$:
$$P(X \le x) = \Phi\!\left(\frac{x - \mu}{\sigma}\right)$$
$$P(a \le X \le b) = \Phi\!\left(\frac{b - \mu}{\sigma}\right) - \Phi\!\left(\frac{a - \mu}{\sigma}\right)$$

## Inverse (quantile function)
$z_\alpha = \Phi^{-1}(1 - \alpha)$ is the **$(1 - \alpha)$-quantile**.
- $z_{0.025} = 1.96$
- $z_{0.05} = 1.645$
- $z_{0.01} = 2.326$

## Common mistakes
- **Reading the wrong tail.** Some tables give $\Phi(z)$; others give $1 - \Phi(z)$ (right-tail). Check what your table is.
- **Confusing one-sided and two-sided CIs.** For 95% two-sided: $1.96$. For 95% one-sided: $1.645$.

## Related
- [[central-limit-theorem]]
- [[confidence-interval]]
- [[neyman-pearson-test]]
