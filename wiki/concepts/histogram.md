---
title: Histogram
type: concept
course: [[eee-350]]
tags: [histogram, pdf-estimate, visualization]
sources: [[slides-46.5-descriptive-stats]]
created: 2026-04-21
updated: 2026-04-26
---

# Histogram

## In one line
A bar graph where bar height = count (or density) of data points in each bin — a coarse estimator of the PDF or PMF.

## Construction
1. Pick a number of bins $k$ (or bin width $h$).
2. For each bin, count how many data points fall into it.
3. Plot bar heights.
4. For **density histograms**: divide counts by (total samples $\times$ bin width). Then bars have area (not height) representing probability; the total area $= 1$.

## As a PDF/PMF estimator
- As $n \to \infty$ and bin width $h \to 0$ at the right rate, density histogram converges to the true PDF.
- Bin choice matters: too few bins $\to$ over-smooth; too many $\to$ noisy. Rules of thumb:
  - Sturges: $k = \lceil\log_2 n\rceil + 1$.
  - Scott: $h = 3.5\cdot\sigma/n^{1/3}$.
  - Freedman-Diaconis: $h = 2\cdot\text{IQR}/n^{1/3}$. Robust to outliers.

## MATLAB
`hist(data, nbins)` — plot. `histogram(data, nbins)` in newer MATLAB.

## Why it matters
- First look at **shape** of a distribution: symmetric? skewed? bimodal?
- Goodness-of-fit visual check.
- Estimate of PDF when no parametric form is known.

## Limitations
- Sensitive to bin choice.
- Discontinuous by construction (bar edges).
- For better (smoother) estimates, use **kernel density estimation (KDE)** — not covered here.

## Related
- [[sample-mean]], [[sample-median]], [[sample-mode]]
- [[order-statistics]]
