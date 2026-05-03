---
title: "Wiesmayr, Maggi, Cammerer, Hoydis, Aït Aoudia, Keller 2025 — SALAD: Self-Adaptive Link Adaptation"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/wiesmayr-salad-2025.pdf
source_date: 2025-10-07
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - link-adaptation
  - mcs-selection
  - bler
  - olla
  - 5g-nr
  - wiesmayr
  - cammerer
  - hoydis
  - aitaoudia
  - nvidia
created: 2026-05-01
updated: 2026-05-01
---

# Wiesmayr et al. 2025 — SALAD: Self-Adaptive Link Adaptation

**Authors:** Reinhard Wiesmayr (ETH/NVIDIA — internship), Lorenzo Maggi, Sebastian Cammerer, Jakob Hoydis, Fayçal Aït Aoudia, Alexander Keller (NVIDIA). **arxiv:2510.05784** (Oct 2025). Mirrored at `raw/articles/ml-phy/pdfs/wiesmayr-salad-2025.pdf`.

## TL;DR
**SALAD selects the modulation-and-coding-scheme (MCS) for 5G NR using ONLY ACK/NACK feedback** — no CQI reports needed — and **outperforms the industry-standard outer-loop link adaptation (OLLA) by up to 15% throughput** in over-the-air 5G testbed experiments. Inference: SINR via cross-entropy minimization between received ACK/NACKs and predicted BLER values; MCS via hypothesis testing. **Same Wiesmayr-Cammerer-Hoydis trio as the standard-compliant NRX paper.**

## Key contributions

1. **ACK/NACK-only SINR inference.** Cross-entropy loss between observed ACK/NACK pattern and tabulated BLER curve → posterior over SINR. No CQI needed.
2. **Hypothesis-test MCS selection.** Pick highest MCS such that the SINR estimate is "likely high enough" — controls aggressiveness vs. BLER target.
3. **Adaptive feedback control loop.** Adjusts the instantaneous BLER target so the long-term BLER tracks the desired τ ≈ 10%.
4. **Real-testbed validation.** Over-the-air 5G experiments — beats OLLA across multiple traffic regimes with **a single set of parameters** (OLLA needs different stepsize per regime).

## Methods
- **Problem.** Single user, MCS index $u_t$ from set $\mathcal{U}$, true SINR $\gamma_t$, transport-block size $b_t$, BLER target $\tau$. Maximize SE × success-prob s.t. BLER ≤ τ.
- **SINR estimation.** Maintain posterior over $\gamma$; update by $\nabla L_{CE}$ where $L_{CE}$ is cross-entropy between observed ACK/NACKs and predicted BLER from a pre-computed table.
- **MCS selection.** Hypothesis test: select highest $u$ such that $P(BLER(u, \hat{\gamma}) \leq \tau) \geq 1-\delta$.
- **OLLA comparison.** OLLA uses fixed-stepsize SINR offset adjustment; SALAD adapts stepsize.

## Results
- **Up to 15% higher SE** than OLLA across multiple traffic regimes — single parameter set.
- **BLER target met** consistently — long-term BLER tracks τ.
- Demonstrated **on a 5G testbed** (likely NVIDIA Aerial / Sionna Research Kit).

## Why it matters / where it sits in the roadmap

- **Phase 4 M10 reading complement.** Pairs naturally with [[paper-nrx-wiesmayr-2024]] (Wiesmayr's standard-compliant NRX). Same Wiesmayr-Cammerer-Hoydis-Aït Aoudia-Keller authorship — the **NVIDIA-Aerial-team flagship 2025 result**.
- **Concrete recurring intern problem.** Link adaptation runs every slot; MCS selection is a closed bottleneck — high impact for any internship deliverable.
- **DSP↔ML identity.** Cross-entropy + hypothesis testing → exactly the [[eee-350]] inference framework Jayden already has. The DSP-prior superpower is on display.
- **Stochastic approximation theory** is the analytical backbone — touches [[textbook-sutton-barto-rl]] Ch 1–2 (RL with bandits) and [[textbook-bishop-prml]] Ch 11 (sampling).

## Baselines compared
- **OLLA** with multiple stepsize variants (small / medium / large).
- **Vanilla CQI-based MCS selection.**

## Concepts grounded
- [[neural-receiver]] (adjacent — link adaptation is the "outer" controller)
- [[ber-bler]] — directly invokes BLER target machinery.
- [[neyman-pearson-test]] — the hypothesis-testing framework SALAD's MCS selector uses.

## Portfolio move (Phase 4)
**Reproduce first.** Implement SALAD in Sionna (synthetic testbed); reproduce 5–15% SE gain over OLLA on 3GPP CDL channels at multiple Doppler levels.

**Extend.** Combine with neural-receiver SINR estimates (vs. ACK/NACK only) — a hybrid.

## Related
- [[python-ml-wireless]]
- [[link-adaptation]] — concept umbrella.
- [[harq]] — provides the ACK/NACK feedback signal SALAD operates on (load-bearing).
- [[paper-nrx-wiesmayr-2024]] — Wiesmayr's other NVIDIA paper.
- [[paper-nrx-cammerer-2023]] — same authorship cluster.
- [[paper-sionna-research-kit-2025]] — likely the testbed used.
- [[hoydis]], [[cammerer]], [[aitaoudia]] — NVIDIA Sionna team.
