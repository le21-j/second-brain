---
title: PPO (Proximal Policy Optimization)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - rl
  - policy-gradient
  - trust-region
  - on-policy
  - openai
  - phase-3
sources:
  - "[[textbook-sutton-barto-rl]]"
created: 2026-05-01
updated: 2026-05-01
---

# PPO (Proximal Policy Optimization)

## In one line
**PPO is the modern default policy-gradient algorithm: actor-critic with a clipped objective that enforces a "trust region" without the second-order math of TRPO.** Schulman et al. 2017 (OpenAI). The basis of GPT RLHF, Dota OpenAI Five, AlphaStar — and of most wireless RL papers since 2019.

## Example first

```python
for iteration in range(num_iterations):
    # 1. Roll out N steps with current policy θ_old
    states, actions, rewards, old_log_probs, values = rollout(policy, num_steps=2048)
    advantages = gae(rewards, values)
    
    # 2. Compute targets
    returns = advantages + values
    
    # 3. K epochs of minibatch updates
    for epoch in range(K):  # K = 10 typical
        for batch in minibatches:
            new_log_probs = log_prob(policy, batch.states, batch.actions)
            ratio = exp(new_log_probs - batch.old_log_probs)
            
            # The PPO clipped objective
            actor_loss = -min(
                ratio * batch.advantages,
                clip(ratio, 1-eps, 1+eps) * batch.advantages
            ).mean()
            
            critic_loss = (V(batch.states) - batch.returns).pow(2).mean()
            
            optimizer.step(actor_loss + 0.5 * critic_loss)
```

`eps = 0.2` standard. K = 10 epochs reuses each batch — making PPO **more sample-efficient than vanilla policy gradient** while staying on-policy "enough."

## The idea — what's new vs. [[actor-critic]]

The clipped surrogate prevents the policy from moving too far from $\theta_{\text{old}}$ in a single update. The ratio $r_t = \pi_\theta / \pi_{\theta_{\text{old}}}$ is clipped to $[1 - \epsilon, 1 + \epsilon]$ — if the policy tries to make a "good" action much more likely (ratio > 1+ε) and the advantage agrees, the gradient is **zeroed**, preventing collapse.

This sidesteps TRPO's expensive Fisher-information KL constraint while preserving most of the trust-region benefit.

## Standard PPO recipe

| Hyperparameter | Standard value |
|---|---|
| Rollout length | 2048 |
| Minibatch size | 64 |
| K epochs per rollout | 10 |
| Clip $\epsilon$ | 0.2 |
| Discount $\gamma$ | 0.99 |
| [[gae]] $\lambda$ | 0.95 |
| LR | $3 \times 10^{-4}$ |
| Adam | yes |
| Entropy bonus | 0.01 |
| Value-loss coef | 0.5 |

## Why it matters / when you use it

- **Phase 3 M8 deliverable.** [[python-ml-wireless]] lists "Spinning Up VPG → PPO" — PPO is the destination.
- **Default for wireless RL papers** since 2019: power allocation, beam selection, RIS configuration, FedAvg-with-RL.
- **The RL backbone for RLHF** in modern LLMs — same algorithm, different reward.
- **CleanRL** has a single-file ~300-line PPO implementation that's the canonical reproduction reference.

## Common mistakes

- **Skipping GAE.** Plain TD-error gives lower-quality advantages; GAE-$\lambda$ is essential.
- **Wrong K.** Too few epochs: wastes data. Too many: policy drifts too far → clipping degrades training.
- **Reward scaling.** PPO is sensitive — normalize rewards (running mean/std) for stable learning.
- **Sharing weights vs. separate networks.** PPO can do either; separate is usually safer for tabula-rasa wireless tasks.

## Related
- [[policy-gradient]], [[reinforce]], [[actor-critic]] — the parent line.
- [[sac]] — off-policy continuous-action alternative.
- [[gae]] — the variance-reduction trick PPO depends on.
- [[reinforcement-learning]]
- [[textbook-sutton-barto-rl]] — Ch 13 + Spinning Up companion.
- [[python-ml-wireless]]

## Practice
- **TODO (Phase 3 M8)** — **Reproduce CleanRL's PPO reference implementation** as the gate. Match published Cartpole reward at the same step count. Only after parity, port to a wireless task (e.g., link adaptation with ACK/NACK reward, paralleling [[paper-wiesmayr-salad-2025|SALAD]]).
