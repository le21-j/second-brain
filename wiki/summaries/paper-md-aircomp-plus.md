---
title: MD-AirComp+ — Adaptive Quantization for Blind Massive Digital AirComp (Qiao et al. 2026)
type: summary
source_type: article
source_path: raw/articles/MD-AirComp+ (Iteration of Two's Compliment).pdf
source_date: 2026-02
course:
  - "[[research]]"
tags: [aircomp, massive-mimo, unsourced-access, quantization, lasso, channel-hardening]
created: 2026-04-21
updated: 2026-05-06
---

# MD-AirComp+ — Adaptive Quantization for Blind Massive Digital AirComp

**Authors:** Qiao, Wang, Jiang, Liu, Xing, Wu, Gao. arXiv:2602.18332 (Feb 2026).

## TL;DR
Blind digital AirComp over massive MIMO: $K$ devices share a random-access codebook, map local values to codeword indices, transmit simultaneously. Receiver exploits channel hardening (large antenna array) to avoid pre-equalization / CSI feedback. Sparse recovery via LASSO + learned-ISTA (LISTA) for 25$\times$ complexity reduction. Adaptive quantization level $Q^*$ chosen to balance quantization error vs detection error under a preamble-length budget.

## Key takeaways
- **Blind operation:** rather than each device pre-equalizing its uplink, devices transmit the common pilot once to let the server estimate the **composite** channel $\bar h = \sum_k h_k$. Then multiplying RX by $\bar h^*/M$ leverages channel hardening (as $M\to\infty$, $H^H H/M \to K\cdot I$) to recover the sum.
- **MSE trade-off (Eq 19):** $\text{MSE} \lesssim (2R^2)/(3KQ^2) + C\cdot(2\sigma^2 Q \log Q)/(KL)$. First term = quantization error (shrinks with $Q$), second = detection error (grows with $Q$ under fixed preamble length $L$). U-shaped $\to$ optimal $Q^*$.
- **LASSO recovery:** $\hat z = \arg\min \tfrac{1}{2}\|\bar y - Pz\|^2 + \rho\|z\|_1$. LISTA unfolds 10 iterations vs 250 for plain ISTA.
- **VQ extension:** map $K$-dim probability vectors to a codeword via K-means centroids, transmit the index only — dramatic bandwidth reduction at fixed accuracy.

## Notes for Jayden's pipeline
- Orthogonal to HPSR — this is **quantize-and-detect** vs HPSR's **analog-power-control**. Different design philosophy.
- The channel hardening trick requires massive MIMO ($M \geq 256$ antennas). Jayden's single-antenna ES can't use this.
- The LS channel estimation in Jayden's Step 1 is mentioned approvingly here (Algorithm 1, step 2).

## Related
- [[paper-bpsk-complement]] — the precursor work
- [[aircomp-basics]]
