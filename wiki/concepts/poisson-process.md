---
title: Poisson Process
type: concept
course: [[eee-350]]
tags: [poisson, counting-process, stochastic-process]
sources: [[slides-47-stochastic-processes]]
created: 2026-04-21
updated: 2026-04-26
---

# Poisson Process

## In one line
A counting process where **arrivals happen at i.i.d. exponential interarrival times**. The number of arrivals in any interval of length $T$ is **$\text{Poisson}(\lambda T)$**.

## Example first
Customers arrive at a coffee shop at rate $\lambda = 20$ per hour.
- Time until first customer: $\text{Exp}(\text{mean } 1/20 = 3 \text{ min})$.
- Time between 5th and 6th customer: also $\text{Exp}(3 \text{ min})$, independent.
- Number of arrivals in a 30-minute window: **$\text{Poisson}(10)$** — mean 10, variance 10.
- Probability of exactly 8 arrivals in 30 minutes: $e^{-10}\cdot 10^8/8! \approx 0.113$.

## Formal definition
$\{N(t) : t \geq 0\}$ is a Poisson process with rate $\lambda > 0$ if:
1. $N(0) = 0$.
2. **Independent increments**: # arrivals in disjoint intervals are independent.
3. **Stationary increments**: distribution of $N(t+s) - N(s)$ depends only on $t$, not $s$.
4. $N(t) - N(s) \sim$ **$\text{Poisson}(\lambda(t - s))$** for $s < t$.

**Equivalent** via interarrivals: let $T_k$ be the time between the $(k-1)$th and $k$-th arrival. Then $T_1, T_2, \ldots$ are **i.i.d. $\text{Exp}(\lambda)$**.

## Key properties
- **Memoryless interarrivals.** $P(T > t + s \mid T > s) = P(T > t)$. No matter how long you've waited, expected remaining wait is still $1/\lambda$.
- **$N(t) \sim \text{Poisson}(\lambda t)$.** Mean $=$ variance $= \lambda t$.
- **Times of events** (conditioned on total count $n$ in $[0, T]$) are **uniformly distributed** over $[0, T]$.
- **Superposition:** sum of independent Poisson processes with rates $\lambda_1, \lambda_2$ is Poisson with rate $\lambda_1 + \lambda_2$.
- **Thinning:** retain each arrival independently with probability $p \to$ new Poisson process with rate $\lambda p$.

## Why it matters
- **Reliability:** time-to-failure often Poisson-like for memoryless components.
- **Queuing theory:** fundamental model for customer arrivals.
- **Communications:** packet arrivals on networks.
- **Physics:** radioactive decay, photon arrivals.

## Intuition — why exponential interarrivals?
The memoryless property forces it. If you want arrivals to be "completely random" (no special times, no memory), the interarrival time MUST be exponential. That's a theorem.

## Common mistakes
- **"Poisson" vs "Poisson process".** Poisson = a discrete distribution on non-negative integers. Poisson process = a stochastic process whose counts follow Poisson distributions.
- Mixing up **mean $1/\lambda$** (interarrival mean) with **rate $\lambda$** (arrivals per unit time).
- Assuming "memoryless = you can predict the next arrival". No — memoryless means you **can't**: your best estimate of the remaining wait is always $1/\lambda$, regardless of past.

## Related
- [[stochastic-process]]
- [[markov-chain]] — Poisson is a special Markov process
- [[sum-of-random-number-of-rvs]] — compound Poisson is a classic example
