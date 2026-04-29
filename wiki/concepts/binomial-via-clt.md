---
title: Binomial via CLT
type: concept
course: [[eee-350]]
tags: [clt, binomial, approximation]
sources: [[slides-43-clt-apps]]
created: 2026-04-21
updated: 2026-04-26
---

# Binomial via CLT

## In one line
For large $n$, $\text{Binomial}(n, p) \approx N(np, np(1-p))$ — use a standard-normal table instead of summing 50 binomial terms.

## Example first
Flip a fair coin 100 times. $P(\geq 60 \text{ heads})$?

$\text{Binomial}(100, 0.5)$: $\mu = 50$, $\sigma^2 = 25$, $\sigma = 5$. With [[continuity-correction|continuity correction]]:
$$P(X \ge 60) \approx P\!\left(Z \ge \frac{59.5 - 50}{5}\right) = P(Z \ge 1.9) \approx 0.029$$

(Exact binomial: $0.0284$. Near-perfect.)

## The idea
$\text{Binomial}(n, p)$ = sum of $n$ i.i.d. $\text{Bernoulli}(p)$ trials. Each Bernoulli has $\mu = p$ and $\sigma^2 = p(1-p)$. Apply CLT to the sum:
$$S_n = \sum_{i=1}^n X_i \approx N(np, np(1-p))$$

Standardize:
$$Z = \frac{S_n - np}{\sqrt{np(1-p)}} \sim N(0, 1)$$

## When does it work well?
Rule of thumb: **$np \geq 10$ and $n(1-p) \geq 10$**. This keeps both tails of the binomial far enough from $0$ and $n$ that the Gaussian shape is a good match.

- $n = 100$, $p = 0.5$: $np = 50$, $n(1-p) = 50$ — great approximation.
- $n = 100$, $p = 0.05$: $np = 5$ — **bad**. Here use Poisson approximation ($\text{Binomial}(n, p) \approx \text{Poisson}(np)$ when $p$ is small).

## With continuity correction
Always include the $\pm 0.5$ shift when approximating a discrete quantity. See [[continuity-correction]] for the full rule table.

| Question | Calculation |
|---|---|
| $P(X \leq 59)$ | $\Phi((59.5 - 50)/5) = \Phi(1.9)$ |
| $P(X \geq 60)$ | $1 - \Phi((59.5 - 50)/5) = 1 - \Phi(1.9)$ |
| $P(X = 60)$ | $\Phi(2.1) - \Phi(1.9)$ |

## Common mistakes
- Using Normal approximation when $p$ is near $0$ or $1$ and $n$ is small — use Poisson.
- Skipping the continuity correction — $1$–$5\%$ error.
- Forgetting that the standardization uses $np(1 - p)$, **not** $np$.

## Related
- [[central-limit-theorem]]
- [[continuity-correction]]
- [[binomial-distribution]] _(not yet written — TBD)_
