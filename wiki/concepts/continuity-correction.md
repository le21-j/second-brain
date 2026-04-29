---
title: Continuity Correction
type: concept
course: [[eee-350]]
tags: [clt, discrete, approximation]
sources: [[slides-43-clt-apps]]
created: 2026-04-21
updated: 2026-04-26
---

# Continuity Correction

## In one line
When approximating a **discrete** distribution (like Binomial) with a **continuous** one (Normal) via CLT, shift integer thresholds by $\pm 0.5$ to hit the boundary between integer buckets.

## Example first
$X \sim \text{Binomial}(n = 36, p = 0.5)$. Approximate $P(X \leq 21)$ via CLT.

Without correction: $Z = (21 - 18)/3 = 1$. $P(Z \leq 1) = \Phi(1) =$ **$0.841$**.

With correction: the discrete event "$X \leq 21$" corresponds to the continuous event "$X \leq 21.5$". So $Z = (21.5 - 18)/3 =$ **$1.167$**. $P(Z \leq 1.167) = \Phi(1.167) \approx$ **$0.878$**.

Exact Binomial: $P(X \leq 21) = 0.878$. **Continuity correction nails it; uncorrected is off by 4 percentage points.**

(The slides give this exact example — "changing 21 to 21.5".)

## The idea
Integer-valued $X$ has probability mass at each integer. Normal approximation has probability density — a continuous curve. To map between them:
- "$X \leq 21$" (integer $\leq 21$, discrete) $\approx$ "continuous $X \leq 21.5$" (include all of the "21 mass").
- "$X \geq 22$" (integer $\geq 22$, discrete) $\approx$ "continuous $X \geq 21.5$".
- "$X = 21$" (exactly) $\approx$ "$21.5 - 0.5 \leq$ continuous $X \leq 21.5 + 0.5$" = "$20.5 \leq X \leq 21.5$".

The $0.5$ is half the gap between consecutive integers.

## Rules of thumb

| Discrete event | Continuous approximation |
|---|---|
| $P(X \leq k)$ | $P(X_N \leq k + 0.5)$ |
| $P(X < k)$ | $P(X_N \leq k - 0.5)$ |
| $P(X \geq k)$ | $P(X_N \geq k - 0.5)$ |
| $P(X > k)$ | $P(X_N \geq k + 0.5)$ |
| $P(X = k)$ | $P(k - 0.5 \leq X_N \leq k + 0.5)$ |
| $P(a \leq X \leq b)$ | $P(a - 0.5 \leq X_N \leq b + 0.5)$ |

## When is it worth doing?
- Small-ish $n$ (say $n < 50$): **definitely**. Error can be several percentage points.
- Large $n$ ($n > 500$): matters less, but still $1\%$ or so.
- In exams: always do it — free accuracy, tiny cognitive cost.

## Common mistakes
- **Sign direction.** For "$X \leq k$" you add $0.5$; for "$X \geq k$" you subtract $0.5$. Easy to flip.
- **Using it for already-continuous approximations.** Doesn't apply if your $X$ is continuous (e.g. Uniform) — only for integer-valued $X$.

## Related
- [[central-limit-theorem]]
- [[binomial-via-clt]]
