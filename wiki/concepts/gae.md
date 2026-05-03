---
title: GAE (Generalized Advantage Estimation)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - rl
  - policy-gradient
  - variance-reduction
  - schulman
  - phase-3
sources:
  - "[[textbook-sutton-barto-rl]]"
created: 2026-05-01
updated: 2026-05-01
---

# GAE (Generalized Advantage Estimation)

## In one line
**GAE is the variance-reduction trick that powers all modern policy-gradient methods (PPO, A2C, A3C, TRPO).** It interpolates between high-variance Monte Carlo returns and high-bias TD-errors via a single hyperparameter $\lambda$. Schulman et al. 2015 (arxiv:1506.02438).

## Example first

**Standard PPO uses GAE-$\lambda$ with $\lambda = 0.95$.** Computing the advantage $\hat A_t$ for each timestep:

```python
# Compute TD-errors first
deltas = [r[t] + gamma * V[t+1] * (1 - done[t]) - V[t] for t in range(T)]

# GAE recursion (computed backward)
gae = 0
advantages = [0] * T
for t in reversed(range(T)):
    gae = deltas[t] + gamma * lam * (1 - done[t]) * gae
    advantages[t] = gae
```

That's it. Replace the raw return $G_t$ in [[reinforce]] / [[actor-critic]] / [[ppo]] with this $\hat A_t^{\text{GAE}}$ — variance plummets, training stabilizes.

## The idea — bias-variance interpolation

Two extremes for advantage estimation:
- **$\lambda = 0$ → TD(0)**: $\hat A_t = \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$. Low variance, high bias (depends entirely on $V$ accuracy).
- **$\lambda = 1$ → Monte Carlo**: $\hat A_t = G_t - V(s_t)$. Unbiased, high variance.

GAE's recursion gives a smooth interpolation:
$$\hat A_t^{\text{GAE}(\lambda)} = \sum_{k=0}^\infty (\gamma\lambda)^k \delta_{t+k}$$

$\lambda \in [0, 1]$ tunes the bias-variance trade. **Typical: $\lambda = 0.95$.** Lower for short-horizon tasks, higher when $V$ is imprecise.

## Why it matters / where it sits in the roadmap

- **Load-bearing for [[ppo]], [[actor-critic]], A2C/A3C.** Without GAE, vanilla policy-gradient barely trains.
- **Phase 3 M8.** [[python-ml-wireless]] M8 ("Spinning Up VPG → PPO") cannot be implemented from scratch without understanding GAE.
- **The defaults are not arbitrary.** $\lambda = 0.95$, $\gamma = 0.99$ are the standard PPO recipe; explaining *why* requires GAE.

## Common mistakes
- **Forgetting episode termination handling.** The `(1 - done[t])` factor zeros propagation across episode boundaries. Skip it and the recursion crosses episodes incorrectly.
- **Computing forward instead of backward.** GAE needs the recursion from $t = T$ backward.
- **Treating $\lambda$ as $\gamma$.** Different roles: $\gamma$ discounts future rewards; $\lambda$ controls bias-variance of the advantage estimate.
- **Normalizing advantages naïvely.** PPO uses `(A - mean) / std` per minibatch — but make sure your minibatches are large enough for this to be stable.

## Related
- [[ppo]] — primary consumer.
- [[actor-critic]] — natural recipe.
- [[reinforce]] — its high-variance ancestor.
- [[policy-gradient]] — umbrella.
- [[reinforcement-learning]]
- [[textbook-sutton-barto-rl]] — Ch 12 (eligibility traces are the close cousin).
- [[python-ml-wireless]]
