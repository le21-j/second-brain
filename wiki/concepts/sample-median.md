---
title: Sample Median
type: concept
course:
  - "[[eee-350]]"
tags: [median, robust-statistics, order-statistics]
sources:
  - "[[slides-46.5-descriptive-stats]]"
created: 2026-04-21
updated: 2026-05-06
---

# Sample Median

## In one line
The middle value after sorting — or the average of the two middles for even $n$.

## Why use it
- **Robust to outliers.** A single huge value barely moves the median (shifts by one position), whereas the [[sample-mean|mean]] can be dragged arbitrarily.
- **Matches "typical" for skewed distributions.** Income, home prices, queue lengths — median describes the typical experience better than mean (the mean is pulled up by the right tail).

## Example
Dataset: $[1, 2, 3, 4, 1000]$.
- Mean $= 202$ — dominated by the outlier.
- Median $= 3$ — the typical value.

Add another sample: $[1, 2, 3, 4, 1000, 10^6]$.
- Mean $= 167{,}001.7$ — moved even further.
- Median $= 3.5$ — moved slightly.

## Outlier sensitivity — "breakdown point"
- Mean: breakdown point $= 0$ (one outlier can ruin it).
- Median: breakdown point $= 50\%$ (you'd need more than half the data to be outliers).

## Where used
- **Median filtering** in image processing: removes "salt-and-pepper" noise (isolated bright/dark pixels) without blurring edges.
- **Robust regression:** minimize $\sum|y_i - \hat y_i|$ instead of squared errors.
- **Non-parametric tests:** sign test, Wilcoxon, etc. rely on median-type statistics.

## Relation to quantiles
Median $=$ 50th percentile. Generalizes to quantiles: $x_{(nq)}$ is the $q$-th quantile (roughly — precise definitions vary). See [[order-statistics]].

## Related
- [[sample-mean]] — the non-robust alternative
- [[order-statistics]]
