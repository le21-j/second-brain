---
title: Q-learning
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - rl
  - off-policy
  - tabular
  - bellman
  - phase-3
sources:
  - "[[textbook-sutton-barto-rl]]"
created: 2026-05-01
updated: 2026-05-01
---

# Q-learning

## In one line
**Q-learning is an off-policy temporal-difference algorithm that learns the optimal action-value function $Q^*(s,a)$ — directly, without ever needing to know the environment dynamics.**

## Example first

**FrozenLake $4 \times 4$ — the canonical RL toy.** A 16-state grid; agent starts top-left, must reach bottom-right; some squares are holes (terminal -1 reward), the goal gives +1.

Initialize $Q(s,a) = 0$ for all $s, a$. Run episodes:
1. From state $s$, pick action $a$ via $\epsilon$-greedy: random with probability $\epsilon$, else $\arg\max_a Q(s,a)$.
2. Step environment → get $(r, s')$.
3. **Q-learning update:**
   $$Q(s,a) \leftarrow Q(s,a) + \alpha\bigl[r + \gamma \max_{a'} Q(s', a') - Q(s,a)\bigr]$$
4. Move to $s'$, repeat.

After a few thousand episodes with $\alpha = 0.1$, $\gamma = 0.95$, $\epsilon$ decaying from 1.0 → 0.01: $Q$ converges, and $\pi^*(s) = \arg\max_a Q(s,a)$ solves the lake. **No model of the environment was needed.**

## The idea

Q-learning is **bootstrapping** — every update uses the current (imperfect) $Q$ estimate as the target. The learning target is the **Bellman optimality equation**:

$$Q^*(s,a) = \mathbb{E}\bigl[r + \gamma \max_{a'} Q^*(s', a')\bigr]$$

The TD update **shifts $Q(s,a)$ toward this target by step size $\alpha$**.

**Off-policy** because the update uses $\max_{a'} Q(s', a')$ — the **optimal** action — regardless of which action the behavior policy actually picked. This is what distinguishes Q-learning from [[sarsa]] (on-policy: uses the behavior-policy's $a'$, not the optimal one).

## Why it matters / when you use it

- **Sutton-Barto Ch 6** — the foundational TD-control algorithm. **Phase 3 M7 reading** in [[python-ml-wireless]].
- **Foundation for [[dqn]]** — Q-learning + neural network for $Q$-function = DQN, the bridge to deep RL.
- **Wireless applications** — RL for power allocation, beam selection, scheduling. The "tabular vs deep" distinction matters: tabular Q-learning works for small state spaces; DQN/PPO needed for continuous-state wireless problems.

## Common mistakes

- **Confusing Q-learning with SARSA.** Q uses $\max_{a'}$ (off-policy); SARSA uses the actual $a'$ from the behavior policy (on-policy). Q is greedier but can over-estimate; SARSA is safer but lower-reward.
- **Forgetting $\epsilon$-decay.** Without exploration decay you keep wasting actions on random exploration; without sufficient initial exploration you never find the optimal policy.
- **Tabular Q-learning on continuous state.** Won't work — $Q$ table grows infinite. Use [[dqn]] or function approximation.

## Related
- [[sarsa]] — on-policy cousin.
- [[dqn]] — Q-learning with deep nets.
- [[reinforcement-learning]] — umbrella concept.
- [[textbook-sutton-barto-rl]] — Ch 6 (TD), Ch 7 (n-step).
- [[python-ml-wireless]]

## Practice
- **TODO (Phase 3 M7)** — Reproduce the **CleanRL DQN reference** first to verify your environment + plotting pipeline. Then implement tabular Q-learning on FrozenLake from scratch in NumPy. Then port to a wireless task (e.g., simple beam-selection bandit).
