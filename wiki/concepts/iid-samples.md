---
title: I.I.D. Samples
type: concept
course:
  - "[[eee-350]]"
tags: [iid, independence, identically-distributed]
sources:
  - "[[slides-39-multivariate-vectors]]"
created: 2026-04-21
updated: 2026-05-06
---

# I.I.D. Samples (Independent and Identically Distributed)

## In one line
$X_1, \ldots, X_n$ are **i.i.d.** if they're (a) **independent** of each other and (b) drawn from the **same** distribution.

## Example first
Roll a fair 6-sided die 100 times. Each roll $X_i$ has the same discrete uniform distribution on $\{1, \ldots, 6\}$. The rolls are independent (one doesn't affect another). So $X_1, \ldots, X_{100}$ are i.i.d. — a textbook i.i.d. sample.

**Not i.i.d.** examples:
- Draw cards from a deck *without* replacement: identically distributed marginally, but NOT independent (the second card is more likely low if the first was high).
- Measure temperature every hour for a day: identically distributed? Maybe (roughly). Independent? No — consecutive hours are correlated.
- Flip a coin whose bias changes each trial: independent, but NOT identical.

## The idea
Two separate conditions stacked together:
- **Independent:** joint PDF factors into product of marginals. $f(x_1, \ldots, x_n) = \prod f(x_i)$.
- **Identically distributed:** each $X_i$ has the same marginal distribution $f$.

Together: $f(x_1, \ldots, x_n) = \prod f(x_i)$, with all $f$'s the same.

## Why it matters
I.i.d. is the foundational assumption of classical statistics:
- **WLLN / CLT** statements assume i.i.d.
- **Maximum likelihood** with $n$ i.i.d. samples factors: $L(\theta) = \prod f(x_i; \theta)$; log-likelihood is a sum $\to$ easy to differentiate.
- **Confidence intervals** and most hypothesis tests derived under this assumption.

## When it fails
Real data is often **not** i.i.d.:
- **Time series:** adjacent observations are correlated.
- **Clustered data:** measurements from the same subject are correlated.
- **Survey data:** respondents in the same household correlate.

These require models that handle dependence (time-series models, mixed-effects models, etc.). LLN/CLT can still hold under weakened conditions (see [[weak-law-of-large-numbers]] notes on dependence).

## Common mistakes
- Treating a **stream of correlated observations** as i.i.d. — common source of underestimated standard errors.
- Forgetting one of the two parts: "independent but different distributions" is not i.i.d.

## Related
- [[random-vector]]
- [[weak-law-of-large-numbers]]
- [[central-limit-theorem]]
- [[sample-mean]]
