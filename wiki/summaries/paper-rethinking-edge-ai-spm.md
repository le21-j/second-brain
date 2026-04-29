---
title: Over-the-Air Federated Learning — Rethinking Edge AI Through Signal Processing (Azimi-Abarghouyi, Fischione, Huang 2025)
type: summary
source_type: article
source_path: raw/articles/6g-research/rethinking-edge-ai-spm.pdf
source_date: 2025-12
course: [[research]]
tags: [aircomp, feel, signal-processing, 6g, csit-aware, blind, weighted, synchronization]
created: 2026-04-21
updated: 2026-04-26
---

# Rethinking Edge AI Through Signal Processing

**Authors:** Azimi-Abarghouyi (KTH), Fischione (KTH), Huang (HKU). IEEE Signal Processing Magazine, Dec 2025. arXiv:2512.03719.

## TL;DR
Tutorial-style classification of AirFL into three design philosophies: **CSIT-aware** (power control at devices), **blind** (equalization at server + massive MIMO), and **weighted** (aggregation weights + MSE constraint). Crucially, gives a three-level synchronization taxonomy — clock, time-alignment, and carrier-phase — plus an explicit fine-vs-coarse sync distinction that directly informs signal design choices. **This is the most important 6G signal-design reference for the pipeline.**

## Key takeaways

### Three AirFL classes (Fig 1-style taxonomy)
| Class | Key design element | Sync needed | CSI needed | Antennas | Complexity |
|---|---|---|---|---|---|
| **Orthogonal (baseline)** | TDMA/FDMA | None | CSIR | $\geq 1$ | $O(0)$ per round, but $K\times$ resources |
| **CSIT-aware** | Power control $p_k$ | **Fine** | CSIT + CSIR | $\geq 1$ | $O(K((M^2+K)^3+M^6))$ |
| **Blind** | Equalization $b$ | Coarse | CSIR (sum-channel) | $\infty$ (massive MIMO) | $O(0)$ |
| **Weighted (WAFeL)** | Aggregation weights $\alpha$ | Coarse | CSIR | $\geq 1$ | $O(K^3)$ |

### Fine vs coarse synchronization (Sec II-B)
**Three independent sync requirements** must hold for the baseband MAC model to be valid:

1. **Clock sync (frame + symbol timing):** all devices begin within a common timing window. Small residual offsets get absorbed into effective channel $h_{k,m}$.
2. **Time alignment (waveform overlap):** all symbols overlap within one symbol interval. If residual delay spread < symbol duration, it's absorbed into $h_{k,m}$; otherwise OFDM-CP or equalization needed.
3. **Carrier-frequency + carrier-phase sync:** residual CFO and phase noise must evolve slowly within one AirComp block.

**Fine synchronization** = symbol-level time alignment + tight CFO/phase (needed for CSIT-aware with channel inversion).
**Coarse synchronization** = frame-level alignment with moderately stable carriers (sufficient for blind/weighted schemes — residual offsets absorbed into channel).

### Partial-phase-aware blind (single-antenna, Sec V-B)
Novel signal design for single-antenna servers: each device compensates its phase only to within **one quadrant** ($[0, \pi/2)$ accuracy is enough). This is a huge relaxation — just enough precision to prevent sign inversions after aggregation, nothing more. Convergence proven under **$\alpha$-stable (heavy-tailed) interference**, matching real-world IoT measurements [Clavier et al. 2021] where interference is NOT Gaussian.

### Weighted AirFL (WAFeL, Sec VI)
Instead of forcing AirComp to approximate a fixed equal-weight aggregation, **let the weights adapt to the channel**:
- Device $k$ transmits $x_k = \sqrt{P} \cdot \exp(-j\cdot\angle\tilde h_k) \cdot \bar w_k$ (normalized model, quadrant-compensated phase only, constant power).
- Server aggregates with learnable $\alpha_k$.
- Weights optimized to balance $\|\alpha\|^2$ (learning fairness) vs MSE (communication quality).
- Supports **heterogeneous batch sizes** — devices with smaller $B_k$ get down-weighted automatically.

Outperforms CSIT-aware BAA by $\sim$15% test accuracy at $t=100$ on MNIST, despite using only partial-phase info.

## Signal-design gaps this exposes in Jayden's pipeline

1. **Pipeline assumes fine sync** (for coherent magnitude alignment) but doesn't specify how to achieve it. This paper distinguishes sync levels and shows what can be achieved with each. Jayden should pick his sync regime explicitly and cite the capability matrix.
2. **No current allowance for heavy-tailed interference** (IoT reality, per [Clavier 2021]). The $\alpha$-stable analysis here matters — symmetric AWGN assumption in HPSR is a simplification.
3. **No weighted-aggregation option** — Jayden's pipeline is strictly CSIT-aware (via the $g(|h_n|)$ projection). WAFeL shows strictly better performance can be achieved with adaptive weights even with less CSI.

## Related
- [[paper-aircomp-survey]]
- [[paper-experimental-ota-fl]] — the testbed paper implementing CSIT-aware style
- [[signal-design-gaps]] — the gap analysis
- [[system-pipeline]]
