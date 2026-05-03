---
title: SAC (Soft Actor-Critic)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - rl
  - off-policy
  - continuous-control
  - entropy-regularization
  - haarnoja
  - phase-3
sources:
  - "[[textbook-sutton-barto-rl]]"
created: 2026-05-01
updated: 2026-05-01
---

# SAC (Soft Actor-Critic)

## In one line
**SAC is the off-policy actor-critic algorithm of choice for continuous-action problems** — it adds an **entropy regularizer** to the reward, pushing the policy to be as random as possible while still maximizing return. Sample-efficient (off-policy with replay), stable, the modern default for wireless RL deliverables (power allocation, beamforming, RIS phase).

## Example first

**Pendulum-v1 — continuous torque control.** Action $\in [-2, 2]$. SAC trains 2 critics ($Q_1, Q_2$) + 1 actor ($\pi_\phi$) + 1 temperature $\alpha$.

Per training step:
1. Sample batch from replay buffer.
2. **Critic update:** TD target with **soft Q** = $r + \gamma (\min_i Q_i(s', a') - \alpha \log \pi_\phi(a' \mid s'))$.
3. **Actor update:** $\nabla_\phi \mathbb{E}_{a \sim \pi_\phi}[\alpha \log \pi_\phi(a \mid s) - \min_i Q_i(s, a)]$.
4. **Temperature update:** auto-tune $\alpha$ to track a target entropy.

Converges in ~50K steps on Pendulum, beats PPO by ~3× sample efficiency. Same recipe works for wireless tasks with continuous power/phase actions.

## The idea — entropy regularization

Standard RL maximizes $\mathbb{E}\bigl[\sum_t \gamma^t r_t\bigr]$.
SAC maximizes $\mathbb{E}\bigl[\sum_t \gamma^t (r_t + \alpha \mathcal{H}(\pi(\cdot \mid s_t)))\bigr]$.

Adding policy entropy $\mathcal{H}$ to the objective gives:
- **Better exploration** — policy stays stochastic instead of collapsing to a single action.
- **Robust to local optima** — entropy bonus prevents premature convergence.
- **Multimodal behavior** captured — if two actions are equally good, both stay sampled.

The temperature $\alpha$ controls the trade-off — auto-tuned in modern SAC to target a fixed entropy.

## Two critics — addressing Q-function overestimation

Like TD3, SAC uses **twin critics** $(Q_1, Q_2)$ and takes the **minimum** in the TD target. Stops the systematic positive-bias of single-Q DDPG / DQN.

## SAC vs PPO vs DDPG (when to use which)

| Algorithm | Action space | On/off policy | Sample eff. | Stability |
|---|---|---|---|---|
| [[ppo]] | continuous or discrete | on | low | very stable |
| [[dqn]] | discrete | off | medium | moderate |
| **DDPG** | continuous | off | high | unstable (overestimation) |
| **SAC** | continuous | off | **highest** | **stable** |

For continuous wireless control (power, phase, beamforming weights), **SAC is the default**.

## Why it matters / where it sits in the roadmap

- **Phase 3 M8 reading priority.** [[python-ml-wireless]] M8 lists "Spinning Up VPG → PPO" — but most wireless RL papers since 2019 use SAC for continuous control. The umbrella [[reinforcement-learning]] page calls SAC out as "standard for continuous control."
- **Wireless deliverables.** Power-allocation RL ([[paper-osman-ris-oran-2025]]'s mobility-management algorithm could be reframed as SAC), beamforming, RIS phase optimization — all continuous-action.
- **Connects to [[paper-wiesmayr-salad-2025|SALAD]].** SALAD is a specialized Bayesian-RL algorithm; a from-scratch SAC implementation gives the comparison baseline.

## Common mistakes
- **Forgetting auto-temperature tuning.** Fixed $\alpha$ can over-explore (poor performance) or under-explore (premature convergence). Auto-tune $\alpha$ to a target entropy.
- **Single critic.** Without the twin-critic minimum, Q-function overestimation creeps in.
- **Replay buffer size too small.** SAC's sample efficiency depends on a large replay buffer (1M+ for Atari-scale).
- **Confusing with TD3.** Both use twin critics. **TD3** layers in delayed policy updates + target-policy smoothing; **SAC** layers in entropy regularization. The features are independent — modern variants combine both.

## Related
- [[reinforcement-learning]], [[actor-critic]] — parent algorithms.
- [[ppo]] — on-policy alternative.
- [[dqn]] — discrete-action cousin.
- [[policy-gradient]] — theoretical backbone.
- [[textbook-sutton-barto-rl]] — Ch 13 + Spinning Up.
- [[python-ml-wireless]]

## Practice
- **TODO (Phase 3 M8)** — Reproduce CleanRL's SAC reference on Pendulum-v1; match published 50K-step convergence. Then port to a continuous-power wireless task and compare to PPO.
