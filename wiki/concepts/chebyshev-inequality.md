---
title: Chebyshev's Inequality
type: concept
course: [[eee-350]]
tags: [chebyshev, inequalities, tail-bound]
sources: [[slides-41-lln-clt-intro]]
created: 2026-04-21
updated: 2026-04-26
---

# Chebyshev's Inequality

## In one line
For any RV with finite mean $\mu$ and variance $\sigma^2$:
$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$

## Example first
A factory's widget lengths have $\mu = 10$ cm, $\sigma = 0.2$ cm. What fraction of widgets are more than 1 cm away from 10?

$1$ cm $= 5\sigma$. So $P(|X - 10| \geq 5\sigma) \leq 1/25 =$ **$4\%$**. Whatever the shape of the distribution — Gaussian, uniform, bimodal, you name it — no more than 4% of the mass is more than 5 std away from the mean.

That's the power of Chebyshev: **no distribution shape required**.

## The idea
Only requires the variance exists. Trades precision for generality — the bound is usually loose (e.g. for Gaussians the probability at $3\sigma$ is 0.27% but Chebyshev only says $\leq 11\%$), but it's universal.

## Formal statement

$$\boxed{\,P(|X - \mu| \ge \varepsilon) \le \frac{\sigma^2}{\varepsilon^2}\,}$$

Equivalent form (substituting $\varepsilon = k\sigma$):
$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$

## Derivation sketch
Start from Markov's inequality: for a non-negative RV $Y$, $P(Y \geq a) \leq E[Y]/a$. Apply it to $Y = (X - \mu)^2$:
$$P((X - \mu)^2 \ge \varepsilon^2) \le \frac{E[(X - \mu)^2]}{\varepsilon^2} = \frac{\sigma^2}{\varepsilon^2}$$
The event $(X - \mu)^2 \geq \varepsilon^2$ is the same as $|X - \mu| \geq \varepsilon$. Done.

## Why it matters
- **Proof of WLLN:** the one-line argument. If $\text{Var}(\bar X_n) = \sigma^2/n \to 0$, then $P(|\bar X_n - \mu| \geq \varepsilon) \leq \sigma^2/(n\varepsilon^2) \to 0$. That's convergence in probability. See [[weak-law-of-large-numbers]].
- **Crude confidence intervals** when only variance (not distribution) is known. "Within $k$ std of the mean, at least $1 - 1/k^2$ of the mass."
- **Sanity check in experiments:** outliers more than $5\sigma$ away are guaranteed rare ($\leq 4\%$) by Chebyshev alone.

## Looseness of the bound
| $k$ | Chebyshev upper bound | Gaussian actual |
|---|---|---|
| 1 | $\leq 1.00$ | $0.317$ |
| 2 | $\leq 0.25$ | $0.046$ |
| 3 | $\leq 0.111$ | $0.0027$ |
| 5 | $\leq 0.04$ | $6 \times 10^{-7}$ |

Chebyshev is usually **orders of magnitude loose** for well-behaved distributions. Its virtue is robustness (requires only 2nd moment), not tightness.

## Common mistakes
- **Needs finite variance.** If $\text{Var}(X) = \infty$ (Cauchy distribution, for instance), Chebyshev doesn't apply.
- **One-sided misuse:** Chebyshev is two-sided. For one-sided $P(X - \mu \geq \varepsilon)$, there's a different bound (Cantelli's).
- **Using Chebyshev when the distribution is known** — you get much tighter bounds from the actual CDF.

## Related
- [[weak-law-of-large-numbers]]
- [[convergence-in-probability]]
- [[markov-inequality]]

## Practice
- [[asymptotics-set-01]]
