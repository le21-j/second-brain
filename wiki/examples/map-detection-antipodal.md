---
title: Example — MAP Detection of Antipodal Signal
type: example
course: [[eee-350]]
tags: [map-detection, awgn, communications]
sources: [[slides-43.5-bayesian-inference]]
created: 2026-04-21
updated: 2026-04-26
---

# Example — MAP Detection of Antipodal Signal under AWGN

## Problem
Transmitter sends $\theta \in \{+1, -1\}$ with prior $P(+1) = 0.7$, $P(-1) = 0.3$. Receiver observes $X = \theta + N$ where $N \sim \mathcal{N}(0, \sigma^2)$ with $\sigma = 1$. Find:
1. The MAP decision rule.
2. The probability of error.

## Step 1 — Likelihood ratio

$$p(X \mid +1) = \frac{1}{\sqrt{2\pi}}\exp\!\left(-\tfrac{(X - 1)^2}{2}\right), \quad p(X \mid -1) = \frac{1}{\sqrt{2\pi}}\exp\!\left(-\tfrac{(X + 1)^2}{2}\right)$$

MAP: decide $+1$ iff $p(X \mid +1)\cdot \pi_0 > p(X \mid -1)\cdot \pi_1$ with $\pi_0 = 0.7$, $\pi_1 = 0.3$.

$$\frac{p(X \mid +1)\cdot 0.7}{p(X \mid -1)\cdot 0.3} = \frac{0.7}{0.3}\exp\!\left(-\tfrac{(X-1)^2}{2} + \tfrac{(X+1)^2}{2}\right) = \frac{0.7}{0.3}\exp(2X) > 1$$

Take log: $2X > -\log(7/3) = -0.847$. So $\mathbf{X > -0.4236}$.

**Decision rule: declare $\hat\theta = +1$ if $X > \tau = -0.4236$, else $\hat\theta = -1$.**

## Step 2 — Verify with formula
General formula from [[map-detection]]:
$$\tau = \frac{\sigma^2}{2}\ln\frac{\pi_1}{\pi_0} = \frac{1}{2}\ln\frac{0.3}{0.7} = \tfrac{1}{2}\cdot(-0.847) = -0.4236 \;\;\checkmark$$

## Step 3 — Probability of error

$P(\text{error}) = P(\text{error} \mid +1)\cdot \pi_0 + P(\text{error} \mid -1)\cdot \pi_1$.

- **$P(\text{error} \mid +1)$:** declared $-1$ when truth is $+1$ $\to$ $X \leq \tau$.
  $X \mid +1 \sim \mathcal{N}(1, 1)$, so $P(X \leq -0.4236 \mid +1) = \Phi(-0.4236 - 1) = \Phi(-1.424) \approx \mathbf{0.0772}$.
- **$P(\text{error} \mid -1)$:** declared $+1$ when truth is $-1$ $\to$ $X > \tau$.
  $X \mid -1 \sim \mathcal{N}(-1, 1)$, so $P(X > -0.4236 \mid -1) = 1 - \Phi(-0.4236 - (-1)) = 1 - \Phi(0.576) \approx \mathbf{0.2822}$.

**$P(\text{error}) = 0.0772\cdot 0.7 + 0.2822\cdot 0.3 = 0.0540 + 0.0847 = 0.1387$.**

Compare with **equal-prior MAP** ($\tau = 0$), which has symmetric errors of $\Phi(-1) \approx 0.1587$ each way, total $P(\text{error}) = 0.1587$. The unequal-prior MAP has LOWER error because it moves the threshold toward the less-likely hypothesis.

## Why the threshold shifts toward $-1$

When $P(+1) = 0.7 > P(-1) = 0.3$, we should be **biased toward declaring $+1$** — it's the more common answer. That means we decide $+1$ even for slightly negative $X$. Threshold moves **down** to $\tau < 0$.

If priors were flipped ($P(-1) = 0.7$), threshold would move up ($\tau > 0$).

## Related
- [[map-detection]]
- [[antipodal-signaling]]
- [[bayesian-inference]]
- [[standard-normal-table]]
