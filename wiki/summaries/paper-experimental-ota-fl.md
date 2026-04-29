---
title: Experimental Demonstration of OTA Federated Learning for Cellular Networks (Pradhan et al. 2025)
type: summary
source_type: article
source_path: raw/articles/6g-research/experimental-ota-fl.pdf
source_date: 2025-03
course: [[research]]
tags: [aircomp, ota-fl, 5g-nr, ptp, octoclock, gold-sequences, usrp, testbed, orbit]
created: 2026-04-21
updated: 2026-04-26
---

# Experimental Demonstration of OTA-FL for Cellular Networks

**Authors:** Pradhan (UT Austin), Koc + Arfaoui + Pietraski + Periard + Zhang + Hudon (InterDigital), Alemdar (Northeastern), Chowdhury (UT Austin). arXiv:2503.06376 (Mar 2025).

## TL;DR
**First large-scale OTA-FL demo on a real 5G-compliant waveform.** ORBIT Testbed, USRP X310 SDRs, 20m UE-gNB distance, 5 UEs. Proves OTA-FL works in cellular networks within 5G NR constraints. Uses **Gold sequences for frame sync**, **CSI-RS-style pilots** for channel estimation, **PTP (IEEE 1588) + Octoclock** for dual-layer synchronization. Achieves 43× spectrum and 7× energy improvement over digital FL. **Direct practical template for Jayden's pipeline implementation.**

## Key signal-design takeaways

### Frame structure (Fig 3b)
```
┌──────────┬─────────┬───────────────────┬───────────┬─────────┐
│ Preamble │ Padding │ Pilots (1 sym)    │ Data      │ Padding │
│ (Gold)   │         │ (QPSK CSI-RS)     │ (weights) │         │
└──────────┴─────────┴───────────────────┴───────────┴─────────┘
```

- **Preamble: Gold Sequences** — chosen for "distinct correlation properties." Provides **sample-level** sync prior to OTA aggregation.
- **Pilot field: 1 OFDM symbol, QPSK CSI-RS-like**. LS estimator at the gNB calculates per-subcarrier channel. Feedback sent over **UDP socket** back to UEs for channel-inversion precoding.
- **Data field**: model weights mapped to I/Q pairs — one complex symbol carries two weights.

### Numerology (5G NR-compliant)
- Bandwidth per UE: 3.84 MHz, 256 subcarriers $\to$ subcarrier spacing 15 kHz (5G NR **numerology 0**).
- Symbol duration: $1/15000 = 66\, \mu\text{s}$.
- ORBIT cellular test: 10 MHz / 30 kHz spacing (numerology 1), 288 subcarriers, 24 RBs, CSI-RS at symbol 6 / subcarrier 6 per RB.
- Sync accuracy required: **sub-$\mu$s** to keep symbol alignment.

### Dual-layer synchronization (Sec IV-B)
- **Host-level:** **PTP (IEEE 1588)** synchronizes companion computer clocks via NIC hardware timestamps. Master-slave topology with gNB as master. Linux tools: `ptp4l` + `phc2sys`. Delivers sub-$\mu$s accuracy.
- **SDR-level:** ORBIT **Octoclock-G** distributes PPS + 10 MHz reference to all SDRs. Equal-length cables. Ensures minimal phase/time deviation.

Without PTP, correlation peaks misalign $\to$ garbage OTA aggregation. With PTP, peaks align $\to$ clean OTA.

### Key design insights

- **Transmit model deltas, not absolute weights**: $\Delta\Theta_{i,r} = \Theta_{i,r} - \Theta^g_{r-1}$. Incremental learning is more stable than absolute-weight transmission under noise.
- **Channel-inversion precoding** at UE: $x = \alpha \cdot W_i / \hat H^f_i$, where $\alpha$ is a power-control scalar chosen to satisfy $\|\alpha\cdot W_i/\hat H_i\|^2 < P_M^U$.
- **Hyperparameter tuning is critical**: larger batch size + lower learning rate $\to$ lower gradient variance $\to$ better analog-channel compatibility.
- **1-bit quantization NOT always optimal**: channel-estimation use case fails with SignSGD-style schemes because gradient magnitude carries information.

## Signal-design gaps this closes for Jayden's pipeline

1. **Sync concrete numbers**: sub-$\mu$s achievable on commodity SDR + PTP. Matches Jayden's Stage 4 needs (magnitude alignment requires similar precision).
2. **5G NR numerology validation**: 15 kHz spacing, 66 $\mu$s symbols, 24 RBs — this is the target template.
3. **Gold Sequences confirmed**: the preamble choice is validated in a real cellular testbed. Addresses Jayden's "Gold coding" mention explicitly.
4. **Feedback channel design**: Uses UDP socket for CSI feedback in this demo; for over-the-air feedback, a separate DL OFDM symbol with polar coding would be the 6G-native choice.

## What this paper does NOT address (still open for Jayden)
- Feedback is currently **error-free UDP** — no OTA feedback with FEC tested.
- Only 5 UEs — doesn't scale-test to hundreds.
- Static nodes only — no mobility.
- CSIT-aware style — does not evaluate blind or weighted variants.

## Related
- [[paper-rethinking-edge-ai-spm]] — the classification framework this fits into
- [[paper-aircomp-feel-demo]] — Şahin's earlier demo (FSK-MV, non-coherent)
- [[signal-design-gaps]]
- [[system-pipeline]]
- Code: https://github.com/genesys-neu/OTA-FL-Testbed
