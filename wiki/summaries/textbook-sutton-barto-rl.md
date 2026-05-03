---
title: "Sutton & Barto — Reinforcement Learning: An Introduction (2nd ed)"
type: summary
source_type: textbook
source_path: raw/textbook/pdfs/sutton-barto-rl-2ed.pdf
source_date: 2018
course:
  - "[[python-ml-wireless]]"
tags:
  - textbook
  - reinforcement-learning
  - sutton-barto
  - canonical
created: 2026-05-01
updated: 2026-05-01
---

# Sutton & Barto — Reinforcement Learning: An Introduction (2nd ed)

**Authors:** Richard S. Sutton (DeepMind / U Alberta) + Andrew G. Barto (UMass Amherst). **MIT Press, 2018**; free PDF (CC BY-NC-ND 2.0) hosted by Sutton at http://incompleteideas.net/book/the-book-2nd.html. 17 chapters, ~525 pages, mirrored locally at `raw/textbook/pdfs/sutton-barto-rl-2ed.pdf`.

## TL;DR
The **RL canon**. Every modern RL paper (PPO, SAC, DQN, AlphaZero) is built on the abstractions in this book — agent-environment loop, value function, Bellman equation, TD learning, policy gradient. The roadmap calls for **Chapters 1–8 (tabular), 9–11 (function approximation), 13 (policy gradient)** for [[python-ml-wireless]] Phase 3 Month 7–8.

## Confirmed table of contents

### Part I — Tabular Solution Methods (Ch 1–8)
| Ch | Title | Roadmap relevance |
|---|---|---|
| 1 | Introduction (Tic-Tac-Toe) | overview, agent-env loop |
| **2** | **Multi-armed Bandits** | exploration vs. exploitation; ε-greedy, UCB |
| **3** | **Finite Markov Decision Processes** | the MDP formalism — agent, state, action, reward, policy, value |
| **4** | **Dynamic Programming** | Bellman equations, policy/value iteration |
| **5** | **Monte Carlo Methods** | learning from sampled returns |
| **6** | **Temporal-Difference Learning** | Sarsa, Q-learning — the workhorse |
| 7 | n-step Bootstrapping | between MC and TD |
| 8 | Planning and Learning with Tabular Methods | model-based + model-free unification |

### Part II — Approximate Solution Methods (Ch 9–13)
| Ch | Title | Roadmap relevance |
|---|---|---|
| 9 | On-policy Prediction with Approximation | function approximation, semi-gradient |
| 10 | On-policy Control with Approximation | semi-gradient Sarsa |
| 11 | Off-policy Methods with Approximation | the deadly triad |
| 12 | Eligibility Traces | TD(λ) — optional |
| **13** | **Policy Gradient Methods** | REINFORCE, Actor-Critic — bridge to DRL |

### Part III — Looking Deeper (Ch 14–17)
| Ch | Title | Roadmap relevance |
|---|---|---|
| 14 | Psychology | optional |
| 15 | Neuroscience | optional |
| 16 | Applications and Case Studies (TD-Gammon, Atari, AlphaGo) | recommended |
| 17 | Frontiers | survey |

## Roadmap reading order

Per [[python-ml-wireless]]:
- **Phase 3 M7 (Nov 2026):** Ch 1–8 (tabular) — paired with David Silver's RL course lectures 1–7.
- **Phase 3 M8 (Dec 2026):** Ch 9–11 + Ch 13 — paired with Hugging Face Deep RL Units 1–4 and Spinning Up VPG → PPO implementation.
- **Phase 3 M9 (Jan 2027):** Ch 16 (case studies) optional — the AlphaGo case study informs how scaled RL works.

## Why it's load-bearing for the roadmap

RL underpins **beam management, power control, and link adaptation** — three of the most active wireless-ML research directions:
- DeepMIMO + RL → beam selection (Phase 3 M9 deliverable).
- Multi-agent DRL for power allocation (Nasir & Guo 2018, [[paper-...]]).
- The [[regretful-learning]] regret-matching algorithm in the AirComp project shares the multi-armed-bandit lineage of Ch 2.

## Concepts grounded by this textbook

**Already exists in the wiki:**
- [[reinforcement-learning]] — will be cross-linked to this summary.

**Created in the 2026-05-01 RL-atoms sprint** (Sutton-Barto chapter → wiki page):
- [[bandit-regret]] — Ch 2 (multi-armed bandits + regret theory)
- [[q-learning]] — Ch 6.5
- [[sarsa]] — Ch 6
- [[policy-gradient]] — Ch 13 (umbrella)
- [[reinforce]] — Ch 13.3
- [[actor-critic]] — Ch 13.5–13.6
- [[gae]] — companion variance-reduction trick (Schulman 2015)
- [[ppo]], [[dqn]], [[sac]] — post-Sutton-Barto, from Spinning Up

**Still deferred (Tier 7+ if needed):** markov-decision-process / bellman-equation / value-iteration / policy-iteration as standalone pages; they're covered inline within the atomic algorithm pages above.

## Companion implementations
- **CleanRL** (https://github.com/vwxyzjn/cleanrl) — single-file PyTorch reference for every algorithm in the book + DRL extensions.
- **OpenAI Spinning Up** (https://spinningup.openai.com/) — algorithm reference with pseudocode + PyTorch.
- **HF Deep RL course** (https://huggingface.co/learn/deep-rl-course/) — hands-on with Stable-Baselines3.

## Worked examples worth remembering
- **Ch 1.5 Tic-Tac-Toe** — the first RL agent in the book; introduces value function via "look up the chance of winning from this position."
- **Ch 2.3 10-armed testbed** — the canonical exploration-vs-exploitation visualization.
- **Ch 6.4 Sarsa vs. Q-learning on cliff-walking** — the classic on-policy vs off-policy contrast.
- **Ch 13.1 REINFORCE** — minimal policy-gradient algorithm, then Actor-Critic.

## Questions this source raises (open)
- The book is **2018-vintage** — modern DRL (PPO, SAC, distributional RL, MARL) is touched but not deep. Pair with Spinning Up for current algorithms.
- Multi-agent RL (essential for [[regretful-learning]]) is barely covered — supplement with the *Multi-Agent Reinforcement Learning* book (Albrecht-Christianos-Schäfer 2024) when needed.

## Related
- [[python-ml-wireless]] — the course page; this textbook is Phase 3 reading.
- [[reinforcement-learning]] — the wiki concept page; will cross-link to this summary.
- [[regretful-learning]] — the AirComp regret-matching algorithm; shares the bandit lineage of Ch 2.
- [[sutton]] — author page.
