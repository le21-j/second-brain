---
title: Reinforcement learning
type: concept
course:
  - "[[python-ml-wireless]]"
tags: [rl, dqn, ppo, sutton, barto, mdp, beam-management, power-control]
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-04-23
updated: 2026-05-06
---

# Reinforcement learning

## In one line
An agent interacts with an environment by taking **actions**, observes **states** and **rewards**, and learns a policy that maximizes **cumulative reward over time** — no supervised labels, just trial-and-error in an environment.

## Example first

**Bandit (simplest case).** A single state, $K$ arms, each arm gives a random reward. You want to figure out which arm has the highest mean and play it.

**$\varepsilon$-greedy policy:**
```python
if np.random.rand() < eps:
    action = np.random.randint(K)        # explore
else:
    action = np.argmax(Q)                # exploit best-so-far
reward = pull_arm(action)
Q[action] += (reward - Q[action]) / (n[action] + 1)
n[action] += 1
```

That's RL in 5 lines. It's literally what [[regretful-learning]] generalizes for AirComp power control. Sutton & Barto Ch 2 is this exercise.

**Full RL** adds: a state that changes based on your action (Markov decision process), so actions have long-term consequences beyond this step. Algorithms: Q-learning, SARSA, policy gradient, actor-critic.

## The idea

Classical setup is a **Markov decision process** (MDP):
- States $s \in \mathcal{S}$.
- Actions $a \in \mathcal{A}$.
- Transition $p(s' | s, a)$.
- Reward $r(s, a, s')$.
- Discount factor $\gamma \in [0, 1]$.

Goal: find a policy $\pi: \mathcal{S} \to \mathcal{A}$ that maximizes:

$$
V^\pi(s) = \mathbb{E}_\pi\!\left[\sum_{t=0}^{\infty} \gamma^t r_t \;\middle|\; s_0 = s\right]
$$

### Two families of algorithms

- **Value-based (Q-learning, DQN).** Learn $Q^\pi(s, a) = \mathbb{E}[\text{return} \mid s, a]$. Policy is argmax. Classic for discrete actions.
- **Policy-based (REINFORCE, PPO, SAC).** Learn $\pi_\theta(a | s)$ directly by gradient ascent on expected return. Natural for continuous actions.

### Algorithms, in the order the roadmap teaches

1. **[[q-learning]]** (Sutton & Barto Ch 6) — tabular off-policy TD; small state spaces. Cousin: [[sarsa]] (on-policy).
2. **[[dqn]]** (Mnih 2015) — deep Q-network; replay buffer + target network; Atari breakthrough.
3. **[[policy-gradient]]** umbrella — directly parameterize $\pi_\theta$.
4. **[[reinforce]]** (Williams 1992) — the simplest policy-gradient algorithm.
5. **[[actor-critic]]** — adds a learned value baseline (A2C / A3C).
6. **[[ppo]]** (Schulman 2017) — current workhorse; clipped trust region.
7. **[[sac]]** (Haarnoja 2018) — off-policy actor-critic with entropy regularization; **the standard for continuous-control wireless deliverables.**

### Wireless applications

- **Beam management** — state $=$ UE position/prior beams, action $=$ which beam, reward $=$ SINR. See [[beam-prediction]] for the supervised version; RL handles the sequential/exploration case.
- **Power control** — state $=$ channel $+$ queue, action $=$ power level, reward $=$ throughput $-$ cost. Classical Nasir & Guo 2018 (arxiv:1808.00490). Connects to [[regretful-learning]].
- **Link adaptation** — MCS selection. [[link-adaptation]] concept page; SALAD (Wiesmayr et al. 2025, [[paper-wiesmayr-salad-2025]]) is the NVIDIA take.
- **Resource allocation over unlicensed spectrum** — Challita, Dong, Saad 2018 (IEEE TWC).

## Formal definition (Q-learning update)

After observing transition $(s, a, r, s')$:

$$
Q(s, a) \leftarrow Q(s, a) + \alpha\!\left[r + \gamma \max_{a'} Q(s', a') - Q(s, a)\right]
$$

With function approximation (DQN), $Q_\theta(s, a)$ is a neural network; use a **target network** $Q_{\theta^-}$ for the bootstrap to stabilize training.

## Why it matters / when you use it

- **Sequential / exploration wireless problems.** Anywhere you have actions whose consequences unfold over time, RL is the tool.
- **Connection to [[regretful-learning]].** Regret-matching is a game-theoretic cousin of the bandit methods in Ch 2 of Sutton & Barto. Understanding both illuminates both.
- **Phase 3 roadmap focus.** Month 7–8 of the roadmap is RL depth — tabular Q, DQN, REINFORCE, PPO, SAC.

## Common mistakes

- **Too little exploration.** Deterministic policy with $\varepsilon=0$ gets stuck on bad local optima.
- **Reward shaping that game-breaks.** A misaligned reward produces clever but wrong policies (paperclip optimizers).
- **No stability tricks.** DQN without target networks $+$ experience replay doesn't converge.
- **Sample inefficiency.** RL often needs $10^6+$ samples; wireless environments are expensive to sample. Use offline RL or imitation learning when you can.

## Reading order (per roadmap)

1. [[textbook-sutton-barto-rl]] — Chapters 1–8 (tabular), 9–11 (approximate), 13 (policy gradient).
2. David Silver's RL course on YouTube.
3. OpenAI Spinning Up — https://spinningup.openai.com/ — algorithm reference.
4. Hugging Face Deep RL Course — https://huggingface.co/learn/deep-rl-course/.
5. **CleanRL** — https://github.com/vwxyzjn/cleanrl — single-file reference implementations.

## Related
- [[bandit-regret]] — the stateless special case (Sutton-Barto Ch 2 first chapter).
- [[regretful-learning]] — multi-agent regret-matching (Jayden's existing AirComp work).
- **Atomic algorithm pages:** [[q-learning]], [[sarsa]], [[policy-gradient]], [[reinforce]], [[actor-critic]], [[ppo]], [[sac]], [[dqn]].
- [[gae]] — the variance-reduction trick across modern PG methods.
- [[link-adaptation]] — wireless application; [[paper-wiesmayr-salad-2025|SALAD]] is a Bayesian-RL approach.
- [[textbook-sutton-barto-rl]]
- [[beam-prediction]]
- [[python-ml-wireless]]
