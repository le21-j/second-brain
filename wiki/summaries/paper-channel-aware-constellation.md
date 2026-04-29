---
title: Channel-Aware Constellation Design for Digital OTA Computation (Li, Chen, Fischione 2025)
type: summary
source_type: article
source_path: raw/articles/6g-research/channel-aware-constellation.pdf
source_date: 2025-01
course: [[research]]
tags: [aircomp, digital, constellation-design, cell-free-mimo, asymmetric-functions]
created: 2026-04-21
updated: 2026-04-26
---

# Channel-Aware Constellation Design for Digital OTA

**Authors:** Li, Chen, Fischione (KTH). arXiv:2501.14675 (Jan 2025).

## TL;DR
Instead of pre-equalizing to cancel the channel, **use channel randomness AS the constellation design** at the receiver. The CP dynamically generates the demodulation constellation per-epoch based on $|\hat h_k|$ (or $\hat h_k$) from pilot estimation. Because channels are almost-surely distinct (continuous random variables), different transmit vectors map to unique received constellation points with probability 1 — no overlap, no power blowup from channel inversion.

## Key takeaways

### Two transmit-coefficient types (Eq 6)
- **Type I (pre-equalized):** $b_k = \sqrt{P_t} \cdot h^*_k / |h_k|$. Works best in **small cells / high SNR** — uniform constellation spacing.
- **Type II (blind, constant power):** $b_k = \sqrt{P_t}$. Works best in **large cells / low SNR** — some pairs of constellation points are well-separated which improves robustness.

**Key finding (Fig 4):** optimal choice of $b_k$ depends on cell radius $R_c$. Type I beats Type II for small $R_c$ ($< \sim 400$m outdoor), Type II takes over as $R_c$ grows.

### Supports arbitrary functions
Unlike HPSR's arithmetic mean and most classical AirComp schemes (restricted to symmetric functions), the channel-aware constellation supports:
- **Symmetric**: sum, product, max, sum of squares.
- **Asymmetric**: weighted sum $\sum g_k \cdot x_k$, weighted product, weighted max, weighted sum of squares.

Achieved because every distinct transmit vector maps to a unique received point (injective mapping, proven in Appendix B).

### Communication protocol (Fig 1)
```
1. tau_p channel-estimation samples -> pilots from each ED.
2. CP estimates h_hat_k, generates per-epoch combined constellation s~ or s_breve.
3. CP acknowledges h*_k/|h_k| to each ED (only if Type I used).
4. EDs transmit modulated signals for tau_c - tau_p samples.
5. CP demodulates against the pre-generated constellation.
6. Process repeats within the smallest coherence block among K nodes.
```

### Amplification factor $A_R$
Received signal is amplified to guarantee minimum symbol Euclidean distance $d_E \geq d_R$ (receiver resolution):
$A_R = \max(1, d_R/d_E)$. Bounded by hardware's $A_{RM}$. If exceeded, tune constellation parameters $a_1, a_2, Q_1, Q_2, \theta$ until $A_R \leq A_{RM}$.

## Gaps this exposes / fills in Jayden's pipeline

1. **Constellation design — explicit alternative to continuous power control.** HPSR selects $P_n$ from discrete set $\{0, P_{\max}/L, \ldots\}$ but doesn't specify what the transmit constellation looks like. This paper gives a concrete design in the **digital AirComp** paradigm.
2. **Mode selection by cell size:** small cells $\to$ Type I (pre-equalized); large cells $\to$ Type II (blind). HPSR currently assumes one regime implicitly.
3. **Asymmetric functions matter**: regret learning's utility function involves $g(|h_n|)\cdot\sqrt{P_n}$ — which can be viewed as channel-dependent weighting. The channel-aware constellation framework naturally supports such weighted aggregation.
4. **Pilot protocol matches Jayden's Stage 1**: $\tau_p$ channel-estimation samples per coherence block, identical to Jayden's beacon-then-LS approach.

## Limitations
- Assumes stationary nodes (channel stable over coherence block).
- Digital scheme — higher receiver complexity than HPSR's analog.
- Doesn't address feedback signaling (assumes CP-to-ED acknowledge is error-free).

## Related
- [[paper-aircomp-survey]]
- [[paper-rethinking-edge-ai-spm]] — this fits the CSIT-aware category there
- [[signal-design-gaps]]
