---
title: Gambler's Fallacy
type: concept
course: [[eee-350]]
tags: [gotcha, independence, lln]
sources: [[slides-42-wlln]]
created: 2026-04-21
updated: 2026-04-26
---

# Gambler's Fallacy

## In one line
Believing that past independent outcomes make a particular next outcome "due" — e.g. "5 heads in a row, so tails is overdue".

## Example
Roulette table has come up red 10 times in a row. The fallacy says: "black is due!" So you bet heavily on black.

Reality: the wheel has no memory. $P(\text{black next})$ is still whatever it was — independent of history. Your expected loss per spin is the same as ever.

## Why people fall for it
The [[weak-law-of-large-numbers]] says long-run averages stabilize. People misread this as "nature balances things out in the short run". But the long-run balance comes from **dilution** (lots more spins make early anomalies irrelevant), not from **compensation** (future spins correcting past ones).

## Mathematical statement
If $X_1, X_2, \ldots$ are independent:
$$P(X_{n+1} = x \mid X_1, \ldots, X_n) = P(X_{n+1} = x)$$

No matter what happened up to step $n$, the $(n+1)$th outcome follows its marginal distribution. No "overdue" mechanism exists.

## Where it shows up
- Casino / lottery reasoning.
- Stock markets: "stock has fallen 5 days, must bounce back tomorrow." (Maybe, maybe not — depends on whether returns are independent.)
- Drawing without replacement is the one case where "overdue" logic is actually correct — but the trials aren't independent.

## Related
- [[weak-law-of-large-numbers]]
- [[iid-samples]]
- [[prob-gotchas]]
