---
title: Multi-armed bandits and regret
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - rl
  - bandit
  - regret
  - exploration-exploitation
  - phase-3
  - aircomp
sources:
  - "[[textbook-sutton-barto-rl]]"
  - "[[regretful-learning]]"
created: 2026-05-01
updated: 2026-05-01
---

# Multi-armed bandits and regret

## In one line
**A bandit is a stateless RL problem: $K$ arms, each gives a stochastic reward, and you must trade off exploration vs. exploitation to minimize cumulative regret** — the gap between your reward and the oracle (always-pick-best-arm) reward. **The simplest RL setting and the one that connects directly to Jayden's existing AirComp [[regretful-learning]] work.**

## Example first

**$K = 5$ arm Bernoulli bandit.** Arms have hidden success probabilities $p_1, \ldots, p_5$. At each step $t$:
1. Pick an arm $a_t$.
2. Observe reward $r_t \in \{0, 1\}$.
3. Update your estimate $\hat p_a$.

Three classical algorithms:
- **$\epsilon$-greedy:** with prob $\epsilon$ pick random; else pick $\arg\max_a \hat p_a$. Simple; sub-optimal.
- **UCB1:** pick $\arg\max_a [\hat p_a + \sqrt{2 \ln t / n_a}]$ — optimism in the face of uncertainty. **Logarithmic regret bound** — provably $O(\log T)$.
- **Thompson sampling:** maintain a Beta posterior on each $p_a$; sample, pick the max. Bayes-optimal in the limit.

Run each for $10^4$ steps; UCB1 and Thompson roughly match; $\epsilon$-greedy is ~5× worse.

## The idea — regret as the metric

**Regret** $R_T = T \cdot p_* - \mathbb{E}\bigl[\sum_t r_t\bigr]$ where $p_*$ is the best arm's mean. Lower is better.

For algorithms with $O(\log T)$ regret, the gap to the oracle grows only logarithmically — as $T \to \infty$, your average reward → $p_*$.

This is **not** the same as RL's total return. Regret measures **how much you lose by exploring** — the framing that makes bandits the simplest RL problem and the **direct ancestor of [[regretful-learning|regret-matching]] in game theory.**

## Connection to [[regretful-learning]] (the AirComp work)

Hart & Mas-Colell's regret-matching algorithm — the algorithmic anchor of Jayden's [[system-pipeline]] AirComp project — is **bandit-style regret** in a **multi-agent** setting. Each EDs is a "player" updating its action distribution by the cumulative regret over alternatives. **Bandits are the single-agent special case.**

For the cold-email writeup: positioning AirComp's regret-matching as a multi-agent extension of the bandit literature (Robbins 1952 → Lai-Robbins 1985 → Auer-Cesa-Bianchi-Fischer 2002 UCB → Hart-Mas-Colell 2000 regret-matching → AirComp 2026) gives a clean single-paragraph CV story.

## Why it matters / where it sits in the roadmap

- **Sutton-Barto Ch 2** — the **first chapter of the M7 RL reading**. Skipping bandits and jumping to MDPs is the most common pedagogical error.
- **The DSP↔RL identity for AirComp.** [[regretful-learning]] is precisely a multi-player bandit with regret-matching dynamics — Jayden already lives in this literature.
- **Wireless applications.** Beam selection (which beam to probe?), spectrum-sensing (which channel to listen on?), MCS selection (which rate to try?) — all bandit-shaped.
- **Practical link adaptation.** OLLA can be reframed as a contextual-bandit; SALAD's hypothesis-test is a Bayesian-bandit variant.

## Common mistakes
- **Confusing regret with return.** Return = sum of rewards. Regret = oracle return − your return. Different scales, different theory.
- **Using $\epsilon$-greedy when UCB / Thompson are easy.** $\epsilon$-greedy is a teaching example; serious work uses UCB or Thompson.
- **Treating contextual bandits as bandits.** Adding context (state) makes it harder — closer to RL than bandits.

## Related
- [[reinforcement-learning]] — bandit is the stateless special case.
- [[regretful-learning]] — multi-player generalization (the AirComp anchor).
- [[textbook-sutton-barto-rl]] — Ch 2.
- [[link-adaptation]] — bandit-style framing of OLLA.
- [[python-ml-wireless]]

## Practice
- **TODO (Phase 3 M7)** — Implement $\epsilon$-greedy, UCB1, Thompson sampling on a $K = 10$ Bernoulli bandit; plot regret vs. $T$. Then read Hart-Mas-Colell to connect to [[regretful-learning]].
