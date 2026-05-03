---
title: DQN (Deep Q-Network)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - rl
  - deep-rl
  - q-learning
  - off-policy
  - replay-buffer
  - phase-3
sources:
  - "[[textbook-sutton-barto-rl]]"
created: 2026-05-01
updated: 2026-05-01
---

# DQN (Deep Q-Network)

## In one line
**DQN replaces tabular [[q-learning]]'s $Q$-table with a neural network — and uses two tricks (experience replay + target network) to make TD-learning stable in deep nets.** Mnih et al. 2013 / 2015 (DeepMind, Atari). The bridge from tabular RL to deep RL.

## Example first

**Atari from raw pixels.** State $s$ = stack of 4 most-recent 84×84 grayscale frames (210M raw pixels per game).

Architecture: 3 conv layers + 2 FC layers; output $Q(s, \cdot) \in \mathbb{R}^{|\mathcal{A}|}$ — one $Q$-value per discrete action.

Training loop:
```python
for step in range(num_steps):
    a = epsilon_greedy(Q_net(s))
    s_next, r, done = env.step(a)
    replay_buffer.add(s, a, r, s_next, done)
    
    # Sample minibatch
    batch = replay_buffer.sample(64)
    target = batch.r + gamma * Q_target(batch.s_next).max(dim=-1) * (1 - batch.done)
    loss = (Q_net(batch.s).gather(a) - target.detach()).pow(2).mean()
    loss.backward()
    optimizer.step()
    
    if step % update_freq == 0:
        Q_target.load_state_dict(Q_net.state_dict())  # hard update
```

After 50M frames, DQN reaches superhuman performance on most Atari games.

## The idea — the two stability tricks

**Trick 1: Experience replay.** Store transitions $(s, a, r, s', d)$ in a buffer; sample minibatches uniformly. Breaks the temporal correlation between consecutive samples (critical for SGD assumptions). Also enables data reuse.

**Trick 2: Target network.** Compute the TD target $r + \gamma \max_{a'} Q_{\text{target}}(s', a')$ using a **frozen copy** of the Q-network. Update this target every $C$ steps. Without this, the moving target makes training unstable (chasing a moving target).

Both tricks address the **non-IID, non-stationary target** problems that arise when combining function approximation + TD + bootstrap.

## Variants

- **Double DQN** — fix Q-learning's overestimation bias via two networks.
- **Dueling DQN** — separate $V(s)$ + $A(s,a)$ heads.
- **Prioritized Experience Replay** — sample high-TD-error transitions more.
- **Rainbow DQN** — combines all of the above + multi-step + noisy nets + distributional.

## Why it matters / when you use it

- **The ImageNet moment for RL** — 2013/2015 Atari paper made deep RL respectable.
- **Phase 3 M7 reading** — paired with PPO + actor-critic in any RL course.
- **Wireless DQN apps** — power allocation, beam selection, scheduling. Common when action space is **discrete** (PPO better for continuous).
- **Reproduce target.** CleanRL has a single-file DQN reference implementation.

## Common mistakes

- **No target network.** Single-network DQN diverges almost always.
- **No replay buffer.** Online DQN with corrupted IID assumption diverges.
- **Wrong target update frequency.** $C = 1$ (always sync) defeats the purpose; $C = 10000$ (Atari default) lags too much for fast-changing dynamics.
- **Continuous actions.** DQN needs discrete actions; for continuous use [[ppo]] or DDPG.

## Related
- [[q-learning]] — the tabular ancestor.
- [[ppo]] — the modern continuous-action default.
- [[reinforcement-learning]]
- [[textbook-sutton-barto-rl]] — Ch 16 (deep RL).
- [[python-ml-wireless]]
