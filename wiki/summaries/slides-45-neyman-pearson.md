---
title: Slides 45 — Neyman-Pearson Hypothesis Testing
type: summary
source_type: slides
source_path: raw/slides/eee-350/45 Neyman-Pearson Hypothesis Testing.pptx
course:
  - "[[eee-350]]"
tags: [hypothesis-testing, neyman-pearson, lrt, type-i, type-ii, chi-squared]
created: 2026-04-21
updated: 2026-05-06
---

# Slides 45 — Neyman-Pearson Hypothesis Testing

## TL;DR
**Classical** (no prior) binary hypothesis testing. Two hypotheses: **$H_0$** (null, "status quo") vs **$H_1$** (alternative). Can make two kinds of errors: **Type I** (reject $H_0$ when true — "false alarm") and **Type II** (accept $H_0$ when false — "missed detection"). Neyman-Pearson strategy: fix Type I probability (significance level $\alpha$, often small like 0.05), then minimize Type II. Uses the **Likelihood Ratio Test** (LRT): accept $H_1$ if $L(x; H_1)/L(x; H_0) >$ threshold $\gamma$, with $\gamma$ chosen to hit the target $\alpha$. Examples: testing a mean (uses CLT) and testing a variance (uses **chi-squared** distribution).

## Key takeaways
- **No prior** on which hypothesis is "more likely" — unlike Bayesian.
- **Null = status quo / presumed innocent**; alternative = "something new".
- **Type I ($\alpha$):** false alarm — reject $H_0$ when it's actually true. Also called "significance level".
- **Type II ($\beta$):** missed detection — fail to reject $H_0$ when $H_1$ is actually true.
- **Power:** $1 - \beta$ = probability of correctly rejecting $H_0$ when $H_1$ is true.
- **LRT:** decide $H_1$ iff $\Lambda(x) = p(x | H_1) / p(x | H_0) > \gamma$. $\gamma$ chosen so that $P(\Lambda > \gamma | H_0) = \alpha$.
- Often thresholding $\Lambda$ is equivalent to thresholding a **sufficient statistic** (e.g. the sum of observations, the sample variance).
- **Testing a mean (Gaussian known variance):** threshold the sample mean at $\bar x_{\text{thresh}} = \mu_0 + z_\alpha\cdot\sigma/\sqrt{n}$. Uses CLT for non-Gaussian data with large $n$.
- **Testing a variance:** statistic is $\sum(x_i - \mu)^2/\sigma^2$ which follows a **$\chi^2$** distribution with $n$ degrees of freedom. Use a $\chi^2$ table.

## Concepts introduced or reinforced
- [[neyman-pearson-test]]
- [[type-i-error]], [[type-ii-error]]
- [[likelihood-ratio-test]]
- [[chi-squared-test]]
- [[sufficient-statistic]] (mentioned implicitly)

## Worked examples worth remembering
- **Testing mean:** detect shift from $\mu_0$ to $\mu_1$ under Gaussian noise. Threshold on $\bar x$.
- **Testing variance:** check if $\sigma^2 > \sigma_0^2$ using $\sum(x_i - \mu)^2$ vs. $\chi^2$ threshold.

## Questions this source raised
- Difference between one-sided and two-sided tests. Slides focus on one-sided; two-sided just splits $\alpha$ between both tails.
