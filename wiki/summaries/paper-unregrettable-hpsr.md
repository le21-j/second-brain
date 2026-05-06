---
title: Unregrettable Distributed Power Control in AirComp (HPSR 2026)
type: summary
source_type: article
source_path: raw/articles/HPSR_2026____Srini__Aruzhan__EET_Camera_Ready.pdf
source_date: 2026
course:
  - "[[research]]"
tags: [aircomp, regret-learning, game-theory, power-control, correlated-equilibrium]
created: 2026-04-21
updated: 2026-05-06
---

# Unregrettable Distributed Power Control in AirComp

**Authors:** Sabyrbek, Purisai Ramanujam, Tsiropoulou (ASU PROTON Lab). HPSR 2026.

## TL;DR
Formulates AirComp power control as a non-cooperative game among edge devices (EDs) and solves it with a regret-learning algorithm that provably converges to a Correlated Equilibrium without needing global CSI. A channel-aware "projection" $g(|h_n|) = 1/|\log|h_n||^\alpha$ compresses high-dynamic-range channels; an adaptive inertia $\mu$ balances exploration/exploitation. This is **the anchor paper** for the pipeline Jayden is implementing.

## Key takeaways
- **System model (Eq 2):** $y = \sum_n |h_n|\sqrt{P_n} \cdot s_n + W$ where $s_n$ are zero-mean unit-variance data symbols. Denoised estimate $\hat f = y / (N\sqrt{\eta})$.
- **MSE (Eq 4):** $\text{MSE}(P,\eta) = (1/N^2) \sum_n (|h_n|\sqrt{P_n}/\sqrt{\eta} - 1)^2 + \sigma^2/(N^2\eta)$. Each ED wants its $|h_n|\sqrt{P_n}/\sqrt{\eta}$ to be close to 1 — i.e., magnitude alignment at the receiver.
- **Strategy space:** discrete power levels $P_n \in \{0, P^{\max}/L, 2P^{\max}/L, \ldots, P^{\max}\}$. $L=100$ in simulations.
- **Utility function (Eq 5-6):** coupling term $g(|h_n|)\sqrt{P_n}/\sqrt{\eta} \cdot \sum_{n'\neq n} g(|h_{n'}|)\sqrt{P_{n'}}/\sqrt{\eta}$ minus a quadratic "cost" term. $g(|h_n|) = 1/|\log|h_n||^\alpha$ is the key projection.
- **Regret matching (Hart & Mas-Colell, Eq 9-12):** each ED tracks counterfactual regret $R^t_n(a_j, a_k)$ for not having played $a_k$ instead of $a_j$, then sets next-round probability $\psi^{t+1}_n(a_k) = R^t_n(a_j,a_k)/\mu$. Inertia $\mu$ ensures probabilities stay in $[0,1]$.
- **Convergence:** empirical distribution of joint actions converges a.s. to the set of Correlated Equilibria (Theorem 1).
- **What each ED needs to compute utility locally:** its own $|h_n|$, plus the aggregate $\sum_{n'\neq n} g(|h_{n'}|)\sqrt{P_{n'}}$ from the ES. No full CSI broadcast needed (the paper stresses this at the end of Sec III).
- **Adaptive $\mu$:** paper shows that tuning $\mu$ inversely to total regret at each step speeds convergence vs constant $\mu$.
- **Simulation params:** $P^{\max}=1$W, radius 100m, 1000 Monte Carlo trials, $\sigma^2=10^{-12}$, $f_c=2.405$ GHz, $\eta=0.5$, $\alpha=0.1$, $\varepsilon=0.005$, $\mu=3000$. Channel models from 3GPP TR 38.901 (UMi Street Canyon, InH Office).
- **Limitations noted:** centralized baselines (Min-MSE, Max-Utility) are better in theory but require perfect global CSI. Regret learning beats them on execution time + energy, with comparable MSE.

## Concepts introduced or reinforced
- [[regretful-learning]] — the algorithm itself, as a concept page
- [[aircomp-basics]] — system model, MSE
- [[channel-projection-g]] — the $g(|h_n|) = 1/|\log|h_n||^\alpha$ trick for HDR channels
- [[correlated-equilibrium]] — relaxation of Nash, guaranteed to exist, reachable by regret matching

## Questions this source raised
- How does each ED actually **measure** $|h_n|$? The paper assumes it's known. (Jayden's pipeline answers this: beacon + LS estimation.)
- How is $\sum_{n'\neq n} g(|h_{n'}|)\sqrt{P_{n'}}$ fed back? The paper says "easily broadcasted" but doesn't specify the protocol. (Jayden's pipeline answers this with a feedback signal.)
- How does the system handle devices that fail to receive feedback? (Jayden's pipeline's ACK + fallback addresses this.)

## Related
- [[regretful-learning]] — concept
- [[system-pipeline]] — the implementation design Jayden is building
- [[paper-aircomp-survey]] — broader context on AirComp
