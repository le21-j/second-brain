---
title: Distributed Learning with FSK-Based Majority Vote (Şahin et al. 2021)
type: summary
source_type: article
source_path: raw/articles/Distributed_Learning_over_a_Wireless_Network_with_FSK-Based_Majority_Vote.pdf
source_date: 2021
course:
  - "[[research]]"
tags: [aircomp, fsk, majority-vote, signsgd, feel, non-coherent]
created: 2026-04-21
updated: 2026-05-06
---

# Distributed Learning with FSK-Based Majority Vote (FSK-MV)

**Authors:** Şahin, Everette, Hoque (Univ. South Carolina). IEEE CommNet 2021.

## TL;DR
Original FSK-MV paper: each ED transmits the sign of its local gradient by activating one of two OFDM subcarriers; the ES detects the majority vote via non-coherent energy detection. No CSI needed at ED or ES. Robust to sync errors and low PAPR via QPSK randomization.

## Key takeaways
- **Encoding:** for gradient sign $+1$, ED transmits $\sqrt{E_s} \cdot s_{k,i}$ on subcarrier $m^+$; for $-1$, on $m^-$. $s_{k,i}$ is a random QPSK symbol for PAPR reduction.
- **MV detection (Eq 13):** $v_i = \text{sign}(|r_{l+,m+}|^2 - |r_{l-,m-}|^2)$ — pure energy comparison.
- **Convergence theorem:** for $\mu$-strongly convex, $L$-smooth loss, convergence rate $O(1/\sqrt{N})$ for iterations, parameter $\lambda \in [0,1]$ capturing power-control / path-loss / cell-size effects (Eq 16, 22). Better power control $\to$ larger $\lambda \to$ faster convergence.
- **Robustness:** tolerant to time-sync errors within CP window (no phase info encoded) and PA non-linearity.
- **Comparison vs OBDA (Zhu et al. one-bit broadband):** FSK-MV works without CSI; OBDA requires TCI at EDs. FSK-MV uses 4$\times$ the time-freq resources but avoids the TCI overhead.

## Notes for Jayden's pipeline
- FSK-MV is the **non-coherent alternative** to the HPSR-style coherent regret-learning approach. Worth knowing about as a fallback if phase sync turns out to be too hard in implementation.
- The convergence analysis framework (path loss + power control + cell size $\to \lambda$ parameter) is useful for predicting how sparse deployments will affect HPSR's convergence.

## Related
- [[paper-aircomp-feel-demo]] — the SDR demo that implements this scheme
- [[paper-ncota-dgd]] — decentralized extension
