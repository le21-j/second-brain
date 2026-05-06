---
title: Weak Law of Large Numbers (WLLN)
type: concept
course:
  - "[[eee-350]]"
tags: [wlln, lln, sample-mean, asymptotic]
sources:
  - "[[slides-42-wlln]]"
created: 2026-04-21
updated: 2026-05-06
---

# Weak Law of Large Numbers (WLLN)

## In one line
If $X_1, X_2, \ldots$ are i.i.d. with finite mean $\mu$ and variance $\sigma^2$, the sample mean $\bar X_n = (X_1 + \ldots + X_n)/n \to \mu$ **in probability** as $n \to \infty$.

## Example first
Roll a fair die infinite times. Let $\bar X_n$ be the average of the first $n$ rolls. Intuition says $\bar X_n$ should stabilize around $3.5$.

WLLN makes this precise: **for any tolerance $\varepsilon > 0$**, the probability that $|\bar X_n - 3.5| \geq \varepsilon$ **goes to zero** as $n$ grows. At $n = 100$, maybe there's a 5% chance $\bar X_{100}$ is more than $0.1$ away from $3.5$. At $n = 10{,}000$, that probability is well under 1%. It never hits 0 for finite $n$, but it shrinks to 0 in the limit.

## Formal statement

Let $X_1, X_2, \ldots$ be i.i.d. with finite mean $\mu$. Then for every $\varepsilon > 0$:
$$P(|\bar X_n - \mu| \ge \varepsilon) \longrightarrow 0 \quad \text{as } n \to \infty$$

i.e. $\bar X_n \xrightarrow{p} \mu$.

(Slides' version assumes finite variance $\sigma^2$ — that's enough for a simple Chebyshev proof. The "real" WLLN needs only finite mean.)

## One-line proof (assuming finite variance)
- $E[\bar X_n] = \mu$ (linearity of expectation).
- $\text{Var}(\bar X_n) = \sigma^2/n$ (i.i.d. $\to$ independent $\to$ no cross-covariances).
- Apply [[chebyshev-inequality]]:
$$P(|\bar X_n - \mu| \ge \varepsilon) \le \frac{\sigma^2 / n}{\varepsilon^2} \to 0$$

Done. One line.

## "Weak" vs "Strong"
- **Weak LLN:** convergence in probability (what this page covers).
- **Strong LLN (SLLN):** convergence **almost surely** — for almost every realization, the sequence $\bar X_1(\omega), \bar X_2(\omega), \ldots$ has a limit equal to $\mu$. Much stronger statement. Beyond EEE 350 scope.

Both say "sample mean $\to$ expectation". WLLN is easier to prove (Chebyshev); SLLN needs more work.

## Gambler's Fallacy (the classic misinterpretation)
"I flipped 5 heads in a row; tails is due."

**WRONG.** WLLN says **averages** stabilize. It says nothing about **short-run** compensation. Each flip is still 50/50, independent. The long-run mean moves toward $0.5$ because the effect of those 5 heads gets diluted in a sea of subsequent i.i.d. flips — not because tails becomes more likely.

## Failure cases
WLLN **fails** when:
- **Dependence is too strong.** Extreme: all $X_i = X$ (perfectly correlated). Then $\bar X_n = X$ forever.
- **Variance is infinite** (e.g. Cauchy distribution). Sample mean doesn't stabilize.
- **Identical distribution fails in a bad way** (e.g. distributions drift).

WLLN **holds under some dependence**: bounded covariances can make $\text{Var}(\bar X_n) \to 0$ anyway. Slides' example: a moving-average of independent Gaussians (adjacent samples correlated, but covariance dies off).

## Typical application — polling
You poll $n$ random voters. Each $X_i \in \{0, 1\}$ with mean $p$ (the true fraction supporting candidate A). Your estimate $\hat p = \bar X_n$.
- By WLLN, $\hat p \to p$ in probability as $n \to \infty$.
- By Chebyshev, $P(|\hat p - p| \geq \varepsilon) \leq p(1-p)/(n\varepsilon^2) \leq 1/(4n\varepsilon^2)$ (using $p(1-p) \leq 1/4$).
- To get within $1\%$ ($\varepsilon = 0.01$) with $95\%$ confidence ($\leq 5\%$ miss prob): $1/(4n \cdot 0.0001) \leq 0.05 \Rightarrow n \geq 50{,}000$.

[[central-limit-theorem|CLT]] gives a sharper $n \approx 10{,}000$. That's why pollsters use CLT, not Chebyshev.

## Common mistakes
- **Thinking WLLN says "eventually $\bar X_n = \mu$".** No — it's a probability statement.
- **Invoking WLLN for non-independent data.** Double-check independence or at least bounded covariances.
- **Confusing WLLN with CLT.** WLLN: $\bar X_n \to \mu$ (a constant). CLT: $(\bar X_n - \mu)\sqrt{n} \to N(0, \sigma^2)$ (a distribution). Different scalings, different conclusions.

## Related
- [[chebyshev-inequality]]
- [[convergence-in-probability]]
- [[central-limit-theorem]]
- [[sample-mean]]
- [[gamblers-fallacy]]

## Practice
- [[asymptotics-set-01]]
