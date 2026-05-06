---
title: Non-Coherent Over-the-Air Decentralized Gradient Descent (Michelusi 2024)
type: summary
source_type: article
source_path: raw/articles/Non-Coherent OTA.pdf
source_date: 2024-09
course:
  - "[[research]]"
tags: [aircomp, decentralized, non-coherent, energy-superposition, dgd, federated-learning]
created: 2026-04-21
updated: 2026-05-06
---

# Non-Coherent Over-the-Air DGD (NCOTA-DGD)

**Author:** Michelusi (ASU). arXiv 2211.10777v4 (Sep 2024).

## TL;DR
Decentralized gradient descent over wireless with no central server, no scheduling, no CSI (neither instantaneous nor average). Each node encodes its state into **energy levels** on OFDM subcarriers (via cross-polytope codebook), transmits simultaneously; receivers exploit a **noisy energy-superposition property** — average received energy equals the weighted sum of transmitted energies, with average channel gains as Laplacian mixing weights. Provable $O(1/\sqrt{k})$ convergence for strongly convex problems.

## Key takeaways
- **Random phase shift + circular subcarrier shift** make the unbiased-estimate property hold under broad channel models (static, Rayleigh, frequency-selective).
- **Half-duplex randomization:** each node transmits with probability $p_{\text{tx}}$ or receives with $1 - p_{\text{tx}}$ in each frame. Optimal $p_{\text{tx}}$ derived in Lemma 2.
- **No need for mixing-weight design:** the path-loss profile itself provides the Laplacian mixing, eliminating the standard DGD weight-design overhead.
- **Convergence conditions:** learning stepsize $\eta_k \propto 1/k$, consensus stepsize $\gamma_k \propto k^{-3/4}$. Decay rate $\delta \leq (4/5)\mu\eta_0$.
- **Experiments:** fashion-MNIST, $N=200$ nodes, 2km radius. Outperforms QDGD, AirComp-FL, AirComp-D2D especially for dense networks.

## Notes for Jayden's pipeline
- NCOTA-DGD is the **fully decentralized** analog — no ES. HPSR still uses an ES (centralized receiver) but distributes the decision-making. Worth knowing as a topology alternative.
- Key insight transferable to HPSR: **random phase shift at transmitters** plus **random participation** can make the system robust to channel fluctuations without CSI. Could complement HPSR for phase alignment at the ES.
- Half-duplex randomization via $p_{\text{tx}}$ is a protocol pattern Jayden could adopt for avoiding ACK collisions in Step 2.

## Related
- [[paper-fsk-mv]] — another non-coherent scheme
- [[system-pipeline]]
