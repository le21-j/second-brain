---
title: Stochastic (Random) Process
type: concept
course:
  - "[[eee-350]]"
tags: [stochastic-process, random-process]
sources:
  - "[[slides-47-stochastic-processes]]"
created: 2026-04-21
updated: 2026-05-06
---

# Stochastic (Random) Process

## In one line
A collection of random variables indexed by time (or space): $\{X_t : t \in T\}$. One realization is an entire **function** (or sequence), not just a number.

## Example first — stock price
Stock price $S_t$ at each time $t$ is a RV. The **process** $\{S_t : t \geq 0\}$ describes all times at once. A single "experiment" (one day of trading) produces an entire path $S_0, S_1, S_2, \ldots$ — one realization of the process.

Other examples:
- **Queue length** at a post office vs. time.
- **Voltage noise** in a receiver vs. time.
- **Rainfall** at latitude/longitude (space-indexed).

## Dimensions
- **Index set $T$:** time, space, or abstract index.
  - Discrete (integers): a **sequence** of RVs.
  - Continuous (real numbers): a **function-valued** RV.
- **State space:** what $X_t$ can take.
  - Discrete states (integer counts, letters): e.g. Markov chains, counting processes.
  - Continuous states (real): e.g. Brownian motion, Gaussian noise.

Four combos: discrete/discrete, discrete/continuous, continuous/discrete, continuous/continuous.

## Applications
- Finance: stock prices, interest rates.
- Communications: noise, fading, multipath.
- Queuing: arrivals and service times.
- Biology: birth-death, genetic drift.
- Signal processing: random signals needing detection/estimation.

## What characterizes a process
- **Finite-dimensional distributions:** joint distribution of $(X_{t_1}, X_{t_2}, \ldots, X_{t_n})$ for any finite set of times. Kolmogorov's extension theorem says these determine the process.
- **Stationarity:** whether finite-dim distributions are time-invariant. See [[stationary-process]].
- **Independence structure:** are $X_t$ independent across times? Markov? General dependence?

## Realization vs. process

> You can plot a **realization** (one sample path), but not "the process itself".

A process is a distribution over paths. A plot shows one path drawn from that distribution.

## Related
- [[stationary-process]]
- [[white-gaussian-process]]
- [[poisson-process]]
- [[markov-chain]]
- [[iid-samples]] — the simplest process: i.i.d. in time
