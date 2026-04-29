---
title: Variance Scaling Rule — Var(cX) = c²Var(X)
type: concept
course: [[eee-350]]
tags: [variance, linearity, gotcha, transformation]
sources: [[homework-2026-04-23-eee-350-hw7]]
created: 2026-04-24
updated: 2026-04-26
---

# Variance Scaling Rule — $\text{Var}(cX) = c^2 \text{Var}(X)$

## In one line
Multiplying a random variable by a constant $c$ multiplies its **variance** by $c^2$ (not $c$). The standard deviation scales by $|c|$.

## Example first
$X$ has $\text{Var}(X) = 25$, so $\text{SD}(X) = 5$. Let $Y = X/5$.

| Quantity | Expression | Value |
|---|---|:---:|
| $\text{Var}(X)$ | $25$ | $25$ |
| $\text{Var}(X/5)$ | $(1/5)^2 \cdot 25$ | **$1$** |
| $\text{SD}(X)$ | $5$ | $5$ |
| $\text{SD}(X/5)$ | $(1/5) \cdot 5$ | **$1$** |

The $5$ in the denominator **becomes $25$ when it acts on variance** — that's what kills the original variance of $25$.

## Why it's quadratic
Variance is defined as $E[(X - \mu)^2]$. The squared term absorbs any constant $c$ as $c^2$:
$$\text{Var}(cX) = E[(cX - c\mu)^2] = E[c^2(X - \mu)^2] = c^2\,\text{Var}(X).$$

## The full linear-transformation table

| Operation | Mean | Variance | Std Dev |
|---|:---:|:---:|:---:|
| $X + c$ | $\mu + c$ | unchanged | unchanged |
| $X - c$ | $\mu - c$ | unchanged | unchanged |
| $cX$ | $c \cdot \mu$ | $c^2 \cdot \text{Var}(X)$ | $\|c\| \cdot \text{SD}(X)$ |
| $X / c$ | $\mu/c$ | $\text{Var}(X)/c^2$ | $\text{SD}(X)/\|c\|$ |
| $aX + b$ | $a\mu + b$ | $a^2 \cdot \text{Var}(X)$ | $\|a\| \cdot \text{SD}(X)$ |

**Shift does nothing** to spread. **Scale** multiplies variance quadratically and std dev linearly.

## Why [[standardization]] works
Standardization divides by $\sigma$:
$$\text{Var}\!\left(\frac{X - \mu}{\sigma}\right) = \frac{1}{\sigma^2}\text{Var}(X) = \frac{\sigma^2}{\sigma^2} = 1.$$
The $\sigma^2$ in the denominator is **engineered** to cancel the $\sigma^2$ of $X$. Divide by anything else and you don't get unit variance.

## Think in SD if variance confuses you
SD scales linearly, so the arithmetic often feels more natural:
- $\text{SD}(K) = 5 \to \text{SD}(K/5) = 1 \to \text{Var}(K/5) = 1^2$. $\checkmark$

## Common mistakes
- **Scaling variance linearly.** Most common slip: writing $\text{Var}(X/5) = \text{Var}(X)/5 = 5$ instead of $1$. Always remember the square.
- **Applying to a sum instead of a scalar multiple.** $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y)$. Different rule. See [[variance-of-a-sum]].
- **Forgetting $|\cdot|$ on std dev.** $\text{SD}(-X) = \text{SD}(X)$, not $-\text{SD}(X)$. Std dev is non-negative.

## Related
- [[variance-of-a-sum]] — the companion rule for sums
- [[standardization]] — the canonical use case
- [[covariance]] — bilinearity with the same squaring pattern, $\text{Cov}(aX, bY) = ab \cdot \text{Cov}(X, Y)$
- [[central-limit-theorem]] — scales variance by $n$ for $S_n$ and by $1/n$ for $\bar X_n$
