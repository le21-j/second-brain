---
title: Slides 39 — Multivariate Random Vectors
type: summary
source_type: slides
source_path: raw/slides/eee-350/39 Multivariate Random Vectors.pptx
course: [[eee-350]]
tags: [multivariate, random-vector, iid, gaussian]
created: 2026-04-21
updated: 2026-04-26
---

# Slides 39 — Multivariate Random Vectors

## TL;DR
Generalizes from two RVs to **$n$** — a random vector $\mathbf{X} = (X_1, \ldots, X_n)$. Covers discrete vs continuous joint distributions, **i.i.d. samples** (all components have the same distribution and are mutually independent), the **distribution of the max** of $n$ i.i.d. RVs ($F_{\max}(t) = F(t)^n$), and the **multivariate Gaussian** (quadratic form in the exponent, parameters: mean vector $\boldsymbol\mu$ and covariance matrix $\Sigma$).

## Key takeaways
- **Joint PMF / PDF** extended to $n$ dimensions.
- **i.i.d.** = independent *and* identically distributed — the assumption behind most of classical statistics.
- **Max of $n$ i.i.d.** RVs: $F_{\max}(t) = P(\text{all} \leq t) = F(t)^n$. Differentiate $\to f_{\max}(t) = n\cdot F(t)^{n-1}\cdot f(t)$.
  - Example in slides: max of $n$ i.i.d. exponentials.
- **Multivariate Gaussian PDF:**
  $$f(\mathbf{x}) = \frac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}} \exp\!\left(-\tfrac{1}{2}(\mathbf{x}-\boldsymbol\mu)^T \Sigma^{-1} (\mathbf{x}-\boldsymbol\mu)\right)$$
- **Marginals of a multivariate Gaussian are Gaussian.**
- If $\Sigma$ is diagonal, components are **independent** (special to Gaussians).

## Concepts introduced or reinforced
- [[random-vector]]
- [[iid-samples]]
- [[max-of-iid]]
- [[multivariate-gaussian]] (builds on [[bivariate-gaussian]])

## Worked examples worth remembering
- PDF of max of $n$ i.i.d. $\text{Exp}(\lambda)$ — the textbook derivation.
