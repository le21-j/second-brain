---
title: REINFORCE
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - rl
  - policy-gradient
  - monte-carlo
  - phase-3
sources:
  - "[[textbook-sutton-barto-rl]]"
created: 2026-05-01
updated: 2026-05-01
---

# REINFORCE

## In one line
**REINFORCE is the simplest [[policy-gradient]] algorithm: roll out a full episode, compute returns, and weight each step's log-probability gradient by its return.** No critic, no baseline (in vanilla form). Williams 1992.

## Example first

```python
for episode in range(num_episodes):
    states, actions, rewards = rollout(policy)
    returns = compute_returns(rewards, gamma)  # G_t = sum_k gamma^(k-t) r_k
    
    loss = -sum(G * log_prob(s, a) for s, a, G in zip(states, actions, returns))
    loss.backward()
    optimizer.step()
```

Negate because we want gradient *ascent* on return; PyTorch optimizers do gradient *descent*.

## The idea

Direct application of the policy-gradient theorem:
$$\nabla_\theta J(\theta) = \mathbb{E}_\tau\Bigl[\sum_t G_t \nabla_\theta \log \pi_\theta(a_t \mid s_t)\Bigr]$$

REINFORCE just uses **Monte Carlo returns** — full episode, no bootstrapping, no critic.

## With baseline (the practical version)

Subtract a state-dependent baseline $b(s_t)$ — typically a learned value function $V_\phi(s_t)$ — to reduce variance:

$$\nabla_\theta J(\theta) \approx \mathbb{E}\Bigl[\sum_t (G_t - V_\phi(s_t)) \nabla_\theta \log \pi_\theta(a_t \mid s_t)\Bigr]$$

The advantage $A_t = G_t - V_\phi(s_t)$ tells the policy "how much better than expected was this action?" — same expected gradient, lower variance.

## Why it matters / when you use it

- **Sutton-Barto Ch 13** — the introductory policy-gradient algorithm.
- **Pedagogy.** Implementing REINFORCE from scratch teaches the score-function trick and makes [[ppo]] / [[actor-critic]] easier to read.
- **Phase 3 M7 deliverable candidate.**

## Common mistakes

- **No baseline → variance is too high to learn anything.** Always subtract $V_\phi$ in practice.
- **Forgetting to normalize returns.** Many implementations standardize $G_t$ within each batch (`(G - mean) / std`) for stability.
- **Reusing data across updates.** REINFORCE is on-policy; old rollouts have wrong $\pi_\theta$.

## Related
- [[policy-gradient]] — the umbrella.
- [[actor-critic]] — adds the critic.
- [[ppo]] — the modern stable upgrade.
- [[reinforcement-learning]]
- [[textbook-sutton-barto-rl]] — Ch 13.
- [[python-ml-wireless]]
