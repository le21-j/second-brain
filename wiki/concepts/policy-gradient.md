---
title: Policy gradient
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - rl
  - policy-based
  - on-policy
  - phase-3
sources:
  - "[[textbook-sutton-barto-rl]]"
created: 2026-05-01
updated: 2026-05-01
---

# Policy gradient

## In one line
**Policy-gradient methods directly parameterize the policy $\pi_\theta(a \mid s)$ and improve it by gradient ascent on expected return.** No $Q$-table, no value function required (though one often helps as a baseline).

## Example first

**See [[reinforce]]** for the canonical Cartpole-with-policy-net worked example — this page intentionally defers the per-algorithm derivation. The umbrella concept here is the **family** (theorem + variants table); the per-algorithm details (REINFORCE / actor-critic / PPO / SAC) live on their own pages.

## The idea — why this works

The **policy-gradient theorem** says:

$$\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}\Bigl[\sum_t G_t \nabla_\theta \log \pi_\theta(a_t \mid s_t)\Bigr]$$

i.e. the gradient of expected return with respect to policy parameters equals the expectation of return × log-probability gradient. The **score function** $\nabla_\theta \log \pi_\theta$ is computable; the return $G_t$ is observed; their product is an unbiased gradient estimator.

**Why is this useful?** Direct: **no need to estimate $Q$** at all (though baselines help variance). Works in **continuous action spaces** trivially (just parameterize $\pi_\theta$ as a Gaussian over actions). Handles **stochastic policies** naturally.

## Variants

| Variant | Reduces variance with… |
|---|---|
| **REINFORCE** ([[reinforce]]) | Nothing (use $G_t$ raw) |
| **REINFORCE w/ baseline** | Subtract a state-dependent baseline $b(s_t)$ |
| **Actor-Critic** ([[actor-critic]]) | Replace $G_t$ with TD-error $\delta_t$ |
| **A2C / A3C** | Synchronous / asynchronous actor-critic |
| **TRPO / PPO** ([[ppo]]) | Trust-region constraint on $\theta$ updates |

## Why it matters / when you use it

- **Sutton-Barto Ch 13.**
- **Wireless beam selection** — beam choice is discrete; cartpole-scale state + actions → REINFORCE works.
- **Wireless resource allocation** — power-allocation is continuous → policy gradient is the natural family.
- **Phase 3 M7–M8 reading.** [[python-ml-wireless]] explicitly lists Sutton-Barto + David Silver + HF Deep RL + Spinning Up VPG→PPO.

## Common mistakes

- **No baseline → high variance.** Raw REINFORCE is too noisy for serious problems.
- **Forgetting log-likelihood numerical stability.** $\log \pi_\theta(a \mid s)$ for tiny probabilities can underflow; softmax-cross-entropy is the safe form.
- **Off-policy data with on-policy gradient.** Vanilla policy gradient assumes data is sampled from the current $\pi_\theta$; using stale rollouts is biased — use [[ppo]] or importance sampling.

## Related
- [[reinforce]] — the simplest policy-gradient algorithm.
- [[actor-critic]] — adds value baseline.
- [[ppo]] — modern stable variant.
- [[reinforcement-learning]]
- [[textbook-sutton-barto-rl]] — Ch 13.
- [[python-ml-wireless]]
