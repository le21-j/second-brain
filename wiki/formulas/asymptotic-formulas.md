---
title: Asymptotic Theorems (Formula)
type: formula
course: [[eee-350]]
tags: [chebyshev, lln, clt]
sources: [[slides-41-lln-clt-intro]], [[slides-42-wlln]], [[slides-43-clt-apps]]
created: 2026-04-21
updated: 2026-04-26
---

# Asymptotic Theorems — Formula Sheet

## Markov's inequality ($Y \geq 0$)

$$P(Y \ge a) \le \frac{E[Y]}{a}$$

## Chebyshev's inequality

$$P(|X - \mu| \ge \varepsilon) \le \frac{\sigma^2}{\varepsilon^2}$$

Or equivalently:
$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$

## Weak Law of Large Numbers (WLLN)

$X_i$ i.i.d. with finite mean $\mu$, variance $\sigma^2$:
$$\bar X_n = \frac{1}{n}\sum X_i \xrightarrow{P} \mu$$

Rate (from Chebyshev):
$$P(|\bar X_n - \mu| \ge \varepsilon) \le \frac{\sigma^2}{n\varepsilon^2}$$

## Central Limit Theorem (CLT)

$$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0, 1)$$

Equivalently:
$$\sqrt{n}\cdot\frac{\bar X_n - \mu}{\sigma} \xrightarrow{d} N(0, 1)$$

## CLT application — Gaussian tail probability

$$P(\bar X_n \ge \bar x) \approx 1 - \Phi\!\left(\frac{\bar x - \mu}{\sigma/\sqrt{n}}\right)$$

## Binomial approximation (continuity correction)

$\text{Binomial}(n, p) \approx N(np, np(1-p))$:
$$P(X \le k) \approx \Phi\!\left(\frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right)$$

## Sample size for polling (margin $\varepsilon$, confidence $1 - \alpha$)

$$n \approx \left(\frac{z_{\alpha/2}}{\varepsilon}\right)^2\cdot p(1-p) \;\;\le\;\; \left(\frac{z_{\alpha/2}}{\varepsilon}\right)^2\cdot\tfrac{1}{4}$$

## Related
- [[chebyshev-inequality]]
- [[weak-law-of-large-numbers]]
- [[central-limit-theorem]]
- [[continuity-correction]]
- [[polling-sample-size]]
