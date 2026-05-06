---
title: EEE 350 Module 8 — Gaussian RPs, Bernoulli & Poisson Processes (slide deck summary)
type: summary
source_type: slides
source_path: raw/slides/eee-350/47.5 Gaussian Random Processes.pptx
source_date: 2026-04-29
course:
  - "[[eee-350]]"
tags: [eee-350, stochastic-process, gaussian-rp, bernoulli-process, poisson-process, week-15]
created: 2026-04-29
---

# EEE 350 Module 8 — Gaussian, Bernoulli, Poisson Processes

**Source:** Three `.pptx` files (Module 8, Week 15 — final stretch of EEE 350):
- `raw/slides/eee-350/47.5 Gaussian Random Processes.pptx`
- `raw/slides/eee-350/48 Bernoulli Process.pptx`
- `raw/slides/eee-350/49 Poisson Processes.pptx`

## TL;DR
Module 8 is the **stochastic-process zoo** that closes the course. After the Module 7 generic stochastic-process intro ([[stochastic-process]], slide 47), this module fills in the three workhorse process families: **Gaussian RPs** (continuous-time, second-order describes everything), **Bernoulli process** (discrete-time, i.i.d. Bernoulli trials), and **Poisson process** (continuous-time, exponential interarrivals).

## Key takeaways

### Gaussian Random Processes (slide 47.5)
- **Definition:** any finite collection of $X(t_1), \dots, X(t_n)$ has a joint Gaussian distribution.
- **Fully described by mean function $\mu(t)$ and autocovariance $K(s, t)$** — no higher-order moments needed.
- **Special case: Wide-sense stationary (WSS) Gaussian = strict-sense stationary** (because joint Gaussian is determined by mean and covariance).
- **White Gaussian noise (WGN):** zero-mean WSS Gaussian RP with $\text{Cov}(X(s), X(t)) = \sigma^2 \delta(s - t)$. See [[white-gaussian-process]].

### Bernoulli Process (slide 48)
- **Discrete-time** sequence $\{X_n\}_{n \geq 1}$ where each $X_n \sim \text{Bernoulli}(p)$ i.i.d.
- **Number of successes in $n$ trials:** $S_n = \sum X_k \sim \text{Binomial}(n, p)$.
- **Inter-arrival time** (gap until next success): $\sim \text{Geometric}(p)$ — memoryless.
- **Time of $k$-th arrival:** $\sim \text{NegativeBinomial}(k, p)$.

### Poisson Process (slide 49)
- **Continuous-time** counting process $\{N(t), t \geq 0\}$ with i.i.d. **exponential** inter-arrival times of rate $\lambda$.
- $N(t) \sim \text{Poisson}(\lambda t)$ — count in $[0, t]$ is Poisson with mean $\lambda t$.
- $N(t + \tau) - N(t) \sim \text{Poisson}(\lambda \tau)$ — independent increments.
- **Sum of two independent Poisson processes** (rates $\lambda_1, \lambda_2$) is Poisson with rate $\lambda_1 + \lambda_2$. See [[poisson-process]].

## Concepts introduced / reinforced
- [[stochastic-process]] — already exists; this module specialises
- [[white-gaussian-process]] — already exists; reinforced
- [[poisson-process]] — already exists; reinforced
- **Bernoulli process** — could become its own page if Jayden wants one
- **Gaussian RP / WSS Gaussian** — could become its own page

## Exam tie-in
The EEE 350 final is cumulative — all three process types likely appear. Jayden's HW7 already covers significance testing + LMSE; the final will probably push into stochastic-process applications.

## Questions raised
- Will the EEE 350 final include numerical questions about Poisson rates and inter-arrivals? (Likely yes — easy to compute by hand.)
- Markov chains were covered in slide 47 (per existing wiki). This module doesn't add to them.
