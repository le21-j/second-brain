---
title: On Signal Peak Power Constraint of Over-the-Air Federated Learning (2025)
type: summary
source_type: article
source_path: raw/articles/6g-research/signal-peak-power-ota-fl.pdf
source_date: 2025-12
course: [[research]]
tags: [aircomp, papr, peak-power, instantaneous-power, ofdm-airfl]
created: 2026-04-21
updated: 2026-04-26
---

# Signal Peak Power Constraint in OTA-FL

**arXiv:** 2512.23381 (Dec 2025).

## TL;DR
Investigates the gap between **average power constraints** (assumed in most AirComp papers) and **instantaneous peak power constraints** (what real PAs enforce). OTA-FL gradients — unlike uniformly distributed symbols — have high PAPR because gradient values cluster around small magnitudes with occasional spikes. A single-carrier system tolerates this via peak clipping; multi-carrier OFDM suffers more because peaks are amplified by the IFFT.

## Why this matters for Jayden's pipeline
- **Stage 4 (AirComp training transmission)**: Jayden's current pipeline uses known fixed amplitudes during training (safe). But **operational mode** — transmitting random $s_n$ symbols — will hit the PAPR problem. Need a PAPR-reduction scheme (tone reservation, clipping + LDPC, or per-EDO randomization).
- **FSK-MV inherently PAPR-low** ([[paper-fsk-mv]]) because it modulates energy not amplitude. Jayden's CSIT-aware pipeline is more susceptible.
- Peak-power matters more as $N$ grows: aggregate at receiver is $N \times$ individual amplitude, so ADC saturation is a real concern above $N \sim 100$.

## Practical recommendation for the pipeline
During the operational phase, either:
1. Add a randomization phase per ED per subcarrier (as in [[paper-fsk-mv]]'s QPSK randomization).
2. Budget $\text{OBO}_{\min}$ per [[paper-aircomp-survey]] Eq 44 — reduces effective cell radius.
3. Use tone reservation (reserve a few OFDM subcarriers for canceling peaks).

## Related
- [[paper-fsk-mv]] — low-PAPR by construction
- [[paper-aircomp-survey]] Sec IV-B.2 — power management at transmitter side
- [[signal-design-gaps]]
