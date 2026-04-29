---
title: Type II Error (Miss)
type: concept
course: [[eee-350]]
tags: [hypothesis-testing, error, miss]
sources: [[slides-45-neyman-pearson]]
created: 2026-04-21
updated: 2026-04-26
---

# Type II Error (Miss)

## In one line
Accepting $H_0$ when $H_1$ is actually true. Probability $\beta$. **Power $= 1 - \beta$** = probability of correctly detecting $H_1$.

## Example
Same drug trial. $H_0$: drug ineffective. A Type II error = concluding the drug doesn't work when it actually does.

- Unlike $\alpha$, you **don't get to pick $\beta$ directly**. $\beta$ depends on the true parameter value under $H_1$, sample size $n$, and the test's $\alpha$.
- Bigger $n$ $\to$ smaller $\beta$ for fixed $\alpha$. More data = better detection.
- Lower $\alpha$ $\to$ higher $\beta$ (for fixed $n$). They trade off.

## Formal

$\beta = P(\text{accept } H_0 \mid H_1 \text{ true}) = P(\text{Type II error})$

Power $= 1 - \beta = P(\text{reject } H_0 \mid H_1 \text{ true})$.

## Trade-off with $\alpha$

|  | $H_0$ true | $H_1$ true |
|---|---|---|
| Reject $H_0$ | $\alpha$ (Type I) | $1 - \beta$ (power) |
| Accept $H_0$ | $1 - \alpha$ | $\beta$ (Type II) |

Reducing $\alpha$ (stricter test) pushes the decision threshold further into the $H_1$ tail $\to$ harder to reject $\to$ more Type II errors. Only way to reduce **both** $\alpha$ and $\beta$ simultaneously: more data.

## Common mistakes
- Not computing $\beta$ when planning an experiment. "Underpowered" studies have high $\beta$ and routinely fail to detect real effects. Common in poorly-designed medical trials.
- Thinking $\beta$ is a property of the test alone. It depends on the **specific alternative value** of $\theta$ under $H_1$. For "$\theta$ close to $\theta_0$" $\beta$ is near $1 - \alpha$ (hard to tell the difference); for "$\theta$ far from $\theta_0$" $\beta$ is near 0.

## Related
- [[type-i-error]]
- [[neyman-pearson-test]]
