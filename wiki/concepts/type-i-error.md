---
title: Type I Error (False Alarm)
type: concept
course:
  - "[[eee-350]]"
tags: [hypothesis-testing, error, false-alarm]
sources:
  - "[[slides-45-neyman-pearson]]"
created: 2026-04-21
updated: 2026-05-06
---

# Type I Error (False Alarm)

## In one line
Rejecting $H_0$ when $H_0$ is actually true. Probability $\alpha =$ **significance level** = **false alarm rate**.

## Example
Drug trial. $H_0$: drug ineffective. $H_1$: drug effective. A Type I error = concluding the drug works when it actually doesn't.

- Common choices: $\alpha = 0.05$ (5% false alarm), $\alpha = 0.01$ (1%), $\alpha = 0.001$ (very strict).
- Lower $\alpha$ = stricter test = **harder to reject $H_0$**, so more misses (more Type II error).

## Formal

$\alpha = P(\text{reject } H_0 \mid H_0 \text{ true}) = P(\text{Type I error})$

By construction (Neyman-Pearson): **you choose $\alpha$** as a design parameter. The test is built so that no matter what, Type I probability doesn't exceed $\alpha$.

## Common mistakes
- Interpreting $\alpha$ as "probability $H_0$ is true given we rejected it". Not the same thing. For that you'd need Bayes' theorem with priors.
- Setting $\alpha$ based on sample size rather than problem cost. Choose $\alpha$ based on how bad a false alarm is (e.g. cost of an unnecessary treatment) — not based on data.

## Related
- [[type-ii-error]] — the other error
- [[neyman-pearson-test]]
