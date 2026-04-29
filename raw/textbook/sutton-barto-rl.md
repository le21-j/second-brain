# Reinforcement Learning: An Introduction (2nd ed.) — Sutton & Barto

**Category:** Reinforcement Learning (the canon)
**Status:** FREE
**URL:** http://incompleteideas.net/book/the-book-2nd.html (PDF, HTML)
**Authors:** Richard Sutton (U. Alberta), Andrew Barto (UMass Amherst)
**Publisher:** MIT Press, 2018
**Roadmap phase:** Phase 3 Month 7 — primary RL text

## Topic coverage (priority chapters)
- Ch 1: The RL problem.
- Ch 2: Multi-armed bandits — **ε-greedy, UCB; the conceptual link to regret learning**.
- Ch 3: Markov decision processes.
- Ch 4: Dynamic programming (value iteration, policy iteration).
- Ch 5: Monte Carlo methods.
- Ch 6: Temporal-difference learning — Q-learning, SARSA.
- Ch 7: n-step bootstrapping.
- Ch 8: Planning and learning with tabular methods — **Dyna, Monte Carlo Tree Search**.
- Ch 9: On-policy prediction with approximation.
- Ch 10: On-policy control with approximation.
- Ch 11: Off-policy methods with approximation.
- Ch 13: **Policy gradient methods** (REINFORCE, actor-critic, natural policy gradient).

## Why it's on the roadmap
Sutton wrote the field into existence; the 2nd edition is the de facto RL canon. Every wireless application paper that cites DRL cites this book for notation.

## Wireless connection
**Regret matching (Hart & Mas-Colell, which powers [[regretful-learning]] in the AirComp pipeline) is a bandit-relative of the methods in Ch 2.** The conceptual bridge — averaging counterfactual regret, ε-greedy exploration, strategy updates — is exactly what Ch 2 is teaching.

## Pair with
- David Silver's DeepMind/UCL RL course on YouTube (chalk-talk version of this book).
- Hugging Face Deep RL Course for hands-on.
- OpenAI Spinning Up for algorithm reference implementations.
- CleanRL for single-file reference implementations of modern algos.

## Related wiki pages
- [[python-ml-wireless]]
- [[regretful-learning]]
- [[reinforcement-learning]]
- [[richard-sutton]]
