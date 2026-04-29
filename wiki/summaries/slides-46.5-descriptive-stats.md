---
title: Slides 46.5 — Sample Mean, Median, Mode, Histogram
type: summary
source_type: slides
source_path: raw/slides/eee-350/46.5 Sample Mean Median Mode Histogram.pptx
course: [[eee-350]]
tags: [descriptive-statistics, sample-mean, median, histogram]
created: 2026-04-21
updated: 2026-04-26
---

# Slides 46.5 — Descriptive Statistics

## TL;DR
Once you have data, you can summarize it two ways: (a) compute "sample" versions of expectations (sample mean, variance, covariance — all approximate the true expectations via LLN) or (b) use order-based stats (median, quantiles) and graphical summaries (histogram). Mean is sensitive to outliers; median is not. Histogram is a coarse estimate of the PDF/PMF.

## Key takeaways

### Moment-based (estimators for theoretical moments)
- **Sample mean:** $\bar x = (1/n) \sum x_i$. By LLN $\to E[X]$. Also MLE/MAP for mean in many models (e.g. Gaussian).
- **Sample variance:** $s^2 = (1/(n-1)) \sum(x_i - \bar x)^2$. ($1/n$ is the MLE but biased; $1/(n-1)$ is unbiased.)
- **Sample covariance:** $(1/(n-1)) \sum(x_i - \bar x)(y_i - \bar y)$. Normalize by sample $\sigma_x\cdot\sigma_y \to$ sample correlation coefficient.
- **Sample moments** (general $n$th): $(1/n) \sum x_i^n$ — approximate $E[X^n]$ by LLN.
- Higher-order moments $\to$ **cumulants**, **skewness**, **kurtosis** (mentioned, not computed).

### Order-based
- **Mode:** most frequent value. Useful for discrete / categorical; fuzzy for continuous data.
- **Order statistics:** sorted data $x_{(1)} \leq x_{(2)} \leq \ldots \leq x_{(n)}$.
- **Median:** middle value. 50% above, 50% below. Robust to outliers — adding one huge outlier doesn't change median, but shifts the mean.
- **Quantiles:** generalize median to any fraction. Boxplots use the quartiles.

### Graphical
- **Histogram:** bar graph of frequencies across bins. Approximate PDF/PMF (after normalization by total count $\cdot$ bin width).
- MATLAB: `hist(data, nbins)`.

## Concepts introduced or reinforced
- [[sample-mean]]
- [[sample-variance]]
- [[sample-covariance]]
- [[sample-median]]
- [[sample-mode]]
- [[order-statistics]]
- [[histogram]]
- [[skewness-kurtosis]] (briefly mentioned)

## Worked examples worth remembering
- **Outlier sensitivity thought-experiment:** a dataset of incomes has a few billionaires — mean is huge, median is close to the "typical person". Why the median filtering trick works against salt-and-pepper noise.
- Adding one extra sample with very large value: what happens to mean (shifts) vs median (barely moves).
