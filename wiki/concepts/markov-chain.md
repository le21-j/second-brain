---
title: Markov Chain
type: concept
course: [[eee-350]]
tags: [markov-chain, stochastic-process, state-transitions]
sources: [[slides-47-stochastic-processes]]
created: 2026-04-21
updated: 2026-04-26
---

# Markov Chain

## In one line
A stochastic process with **discrete states** where the next state depends **only on the current state** (not on history). "The future is conditionally independent of the past given the present."

## Example first — "Good/Bad channel" communications model

Two-state Markov chain modeling a noisy channel that has **burst errors**:
- State **G** (good): bit flips with probability $p_G$.
- State **B** (bad): bit flips with probability $p_B \gg p_G$.

Transitions:
- $G \to B$ with probability $P_{GB}$ (small).
- $G \to G$ with probability $1 - P_{GB}$.
- $B \to G$ with probability $P_{BG}$ (small).
- $B \to B$ with probability $1 - P_{BG}$.

"Small $P_{GB}$ and $P_{BG}$" means good times stay good; bad times stay bad $\to$ **burst errors** instead of independent errors. The independent-error model (one bit-flip probability) would miss this structure entirely.

Real example: fading wireless channels, deep-space comms, some memory architectures.

## Formal definition
A sequence of RVs $\{X_0, X_1, X_2, \ldots\}$ on a discrete state space $S$ is a Markov chain if:
$$P(X_{n+1} = j \mid X_n = i, X_{n-1}, \ldots, X_0) = P(X_{n+1} = j \mid X_n = i)$$

The RHS probability $P_{ij}$ is the **transition probability** from $i$ to $j$.

## Transition matrix
$P$ is a $|S| \times |S|$ matrix with rows summing to 1 (each row is a probability distribution over next states).

If $\pi_n$ is the distribution at time $n$ (as a row vector):
$$\pi_{n+1} = \pi_n \cdot P$$
$$\pi_{n+k} = \pi_n \cdot P^k$$

Powers of $P$ tell you long-term behavior.

## Stationary distribution
A distribution $\pi$ is **stationary** if $\pi\cdot P = \pi$. If the chain is irreducible and aperiodic, $\pi$ is unique and $\pi_n \to \pi$ regardless of starting state. Long-term fraction of time in each state $= \pi$.

## Classification of states
- **Recurrent:** you'll eventually return with probability 1.
- **Transient:** positive probability of never returning.
- **Periodic:** returns only at multiples of some period $d > 1$.
- **Aperiodic:** no such period.

## Why it matters
- **Modeling time-dependence** without modeling everything.
- **PageRank** is a Markov chain on web pages.
- **Hidden Markov Models** (HMMs): Markov chain with noisy observations; fundamental in speech recognition.
- **Queuing theory**: many queue models are Markov chains.
- **Physics / chemistry**: random walks, diffusion.

## Common mistakes
- **Assuming independence.** Markov chains have dependence — just limited to one-step memory.
- **Forgetting rows sum to 1.** Transition matrix rows are probabilities, not arbitrary positive numbers.
- **Conflating "stationary" with "initial".** Stationary distribution is a property of the chain; initial distribution is where you start.

## Related
- [[stochastic-process]]
- [[poisson-process]] (continuous-time Markov process)
