---
title: Actor-Critic
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - rl
  - policy-gradient
  - value-function
  - a2c
  - a3c
  - phase-3
sources:
  - "[[textbook-sutton-barto-rl]]"
created: 2026-05-01
updated: 2026-05-01
---

# Actor-Critic

## In one line
**Actor-Critic combines policy gradient (the "actor") with a learned value function (the "critic") that bootstraps the gradient signal — replacing Monte-Carlo returns with TD targets.** Lower variance than [[reinforce]], lower bias than pure value methods.

## Example first

**Two networks, shared backbone.** Actor outputs $\pi_\theta(a \mid s)$; critic outputs $V_\phi(s)$.

```python
for step in range(num_steps):
    a = sample(policy(s))
    s_next, r, done = env.step(a)
    
    td_target = r + gamma * V(s_next) * (1 - done)
    td_error = td_target - V(s)            # this is the "advantage"
    
    critic_loss = td_error ** 2
    actor_loss = -td_error.detach() * log_prob(a, s)
    
    (actor_loss + critic_loss).backward()
    optimizer.step()
```

The TD-error $\delta_t = r_t + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)$ is the **advantage** — replaces $G_t - V$ in [[reinforce]].

## The idea

Actor-Critic is the **online + bootstrap** version of [[reinforce]] with baseline:

| Algorithm | Target | Bias | Variance |
|---|---|---|---|
| REINFORCE | $G_t$ | none | high |
| REINFORCE w/ baseline | $G_t - V_\phi(s_t)$ | none | medium |
| **Actor-Critic** | $\delta_t = r + \gamma V_\phi(s') - V_\phi(s)$ | bootstrap bias | low |

Per-step updates → **online learning**, no need to wait for episode end.

## Variants

- **A2C** (Advantage Actor-Critic, synchronous) — multiple parallel envs, average gradients.
- **A3C** (Asynchronous A-C, 2016) — multiple workers, each updates a shared model asynchronously.
- **[[gae]]** (Generalized Advantage Estimation) — bias-variance interpolation between $G_t$ and TD-error using $\lambda$. **The variance-reduction trick that powers all modern PG methods.**

## Why it matters / when you use it

- **Sutton-Barto Ch 13.5–13.6.**
- **Bridge to [[ppo]].** PPO is essentially A2C + clipped trust region.
- **Phase 3 M8 reading** — Spinning Up's VPG → PPO line goes through Actor-Critic.

## Common mistakes

- **Critic moves while actor learns.** Standard fix: use a separate target critic with delayed weights (DDPG-style) or just tolerate the non-stationarity.
- **Sharing all weights between actor and critic** → competing gradients. Either separate networks or share early layers + split heads.
- **Detaching the wrong thing.** Actor loss must `.detach()` the advantage; critic loss must NOT detach the target.

## Related
- [[policy-gradient]], [[reinforce]] — the parent line.
- [[ppo]] — the modern descendant.
- [[sac]] — off-policy continuous-action cousin.
- [[gae]] — the variance-reduction trick used in practice.
- [[reinforcement-learning]]
- [[textbook-sutton-barto-rl]] — Ch 13.5–13.6.
- [[python-ml-wireless]]
