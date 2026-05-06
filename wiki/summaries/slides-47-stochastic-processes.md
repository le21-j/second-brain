---
title: Slides 47 — Stochastic (Random) Processes Intro
type: summary
source_type: slides
source_path: raw/slides/eee-350/47 Stochastic (Random) Processes Intro.pptx
course:
  - "[[eee-350]]"
tags: [stochastic-process, random-process, markov-chain, poisson, white-noise]
created: 2026-04-21
updated: 2026-05-06
---

# Slides 47 — Stochastic Processes Intro

## TL;DR
A **random (stochastic) process** is a collection of RVs indexed by time (or space). Instead of a single number, one experiment produces a whole function/sequence. Course gives a *flavor* of three types: **white Gaussian process** (stationary, independent across time), **Poisson process** (integer-valued counter that jumps at exponential interarrival times), and **Markov chain** (discrete-state process where next state depends only on current).

## Key takeaways

### What's a random process
- Collection $\{X_t : t \in T\}$ where $t$ can be continuous (real) or discrete (integer).
- One "experiment" produces a **realization** — a function of time (or a sequence).
- Applications: finance, communications noise, queuing, biometrics, signal processing.

### White Gaussian process (WGN)
- **Discrete time** for simplicity: $X[n] \sim N(0, \sigma^2)$, independent across $n$.
- Each sample has the **same distribution** (identical) and samples at different times are **independent**.
- Classic example of a **stationary process** — joint distribution of any finite collection depends only on *relative* times, not absolute.
- Filtered WGN $\to$ **colored noise** (still Gaussian, but samples correlated). E.g. moving-average filter.

### Stationary vs non-stationary
- Stationary: statistics don't depend on when you look.
- Non-stationary: mean or variance drifts with time.

### Poisson process
- Counts arrivals in time.
- **Interarrival times are i.i.d. $\text{Exp}(\lambda)$**.
- **Number of arrivals in any interval of length $T \sim \text{Poisson}(\lambda T)$**.
- Plot: staircase that jumps by 1 at each arrival.
- Memoryless property (from Exp): $P(\text{wait} > t + s \mid \text{wait} > s) = P(\text{wait} > t)$.

### Markov chain
- Discrete state space, discrete time.
- **Markov property:** future depends only on current state, not on history.
- State transitions defined by transition probabilities $P(s_{t+1} = j \mid s_t = i)$.
- Slides' example: two-state "good/bad" channel for modeling **burst errors** in communications. Independent-error model fails; Markov chain captures "good times stay good, bad times stay bad".

## Concepts introduced or reinforced
- [[stochastic-process]]
- [[stationary-process]]
- [[white-gaussian-process]]
- [[colored-noise]]
- [[poisson-process]]
- [[markov-chain]]

## Worked examples worth remembering
- **Good/Bad channel Markov model** (burst errors): 2 states, transition probabilities $P_{GB}, P_{BG}$.
- **Poisson process** with different $\lambda$: compare realizations.
