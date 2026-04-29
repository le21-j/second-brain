---
title: Sample Mode
type: concept
course: [[eee-350]]
tags: [mode, descriptive-statistics]
sources: [[slides-46.5-descriptive-stats]]
created: 2026-04-21
updated: 2026-04-26
---

# Sample Mode

## In one line
The **most frequently occurring** value in a dataset.

## When useful
- **Discrete / categorical data.** "Most popular car color sold this month" — mode is the right summary.
- Discrete random variables: mode estimates argmax of the PMF.

## When not useful
- **Continuous data.** Every sample value typically appears once, making the mode ill-defined. Bin the data (i.e. make a histogram) and take the mode of the histogram — but that depends on bin choice.
- Multi-modal distributions: a single "mode" hides the multiple peaks. Better to describe the full distribution shape.

## Related
- [[histogram]]
- [[sample-mean]], [[sample-median]]
