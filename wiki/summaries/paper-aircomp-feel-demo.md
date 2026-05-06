---
title: A Demonstration of Over-the-Air Computation for FEEL (Şahin 2022)
type: summary
source_type: article
source_path: raw/articles/A_Demonstration_of_Over-the-Air_Computation_for_Federated_Edge_Learning.pdf
source_date: 2022
course:
  - "[[research]]"
tags: [aircomp, sdr, fsk-majority-vote, ofdm, synchronization, polar-code, golay]
created: 2026-04-21
updated: 2026-05-06
---

# A Demonstration of OAC for Federated Edge Learning

**Author:** Şahin (Univ. South Carolina). IEEE GLOBECOM Wkshps 2022.

## TL;DR
First practical SDR demonstration of an OAC scheme for FEEL. Five Adalm Pluto SDRs + one edge server, synchronized via a hard-coded Golay-sequence–based sync waveform and a custom PPDU with polar coding. MNIST test accuracy >95% with FSK-MV, no CSI needed at EDs. **This is the closest practical blueprint for Jayden's pipeline — protocol, PPDU, calibration, all documented.**

## Key takeaways
- **Synchronization IP block (Sec II):** hard-coded FPGA block detects a sync waveform $x_{\text{SYNC}}$ (repeated Golay-32 sequence, 4$\times$ repetition for CFO robustness) in RX or TX direction and triggers DMA transfers. The CC (companion computer) handles baseband in Python without strict timing.
- **Procedure (Fig 1c):**
  1. ED issues `refill(N_ED)` to prep RX RAM; RX DMA disabled until sync detected.
  2. ES transmits $[x_{\text{SYNC}}\, x_{\text{DL}}]$; at sync detection, block disables ES RX for $T_{\text{PC,ES}}$ seconds.
  3. EDs receive $x_{\text{DL}}$, read from RAM via `read(N_ED)`.
  4. Each ED synthesizes $x_{\text{UL},k}$ and queues $[x_{\text{SYNC}}\, x_{\text{DL}}]$ in TX RAM.
  5. TX DMAs enabled simultaneously $\to$ EDs transmit UL data concurrently.
  6. ES receives the superposed signal $\sum x_{\text{UL},k}$.
- **Calibration (Sec II-B, Fig 2):** ES sends $t_{\text{cal}}$ + sync. Each ED responds with a ZC-sequence calibration signal in its assigned slot. ES cross-correlates to get per-ED time offsets $\Delta T_k$, packs them into $t_{\text{feed}}$ feedback and broadcasts. Each ED updates local $T_{\text{PC,ED}} \mathrel{+}= \Delta T_k$. **Directly analogous to Jayden's Step 2 (per-ED ACK + CSI reporting).**
- **PPDU structure (Sec IV, Fig 5):** four fields — Frame Sync (ZC-97, 2$\times$ time-domain repetition for CFO est), CHEST (QPSK Golay-96 pair), Header (polar-128 rate-1/2 BPSK + 56 signature bits + 8 CRC), Data (polar-128 rate-1/2 BPSK, message chunks of 56 bits). **This is a ready-made template for Jayden's robust signaling layer.**
- **Signaling bits:** 4 bits signaling type, 25 bits user multiplexing, 32 bits time-offset, 8 bits power-control per ED.
- **Experimental results:**
  - Jitter after calibration: $\sim 1\, \mu\text{s}$ std dev (for $T_{\text{PC,ED}}+T_{\text{RX,ED}}=0.8$s).
  - FSK-MV robust against this jitter because it doesn't use phase/amplitude.
  - Closed-loop power control imperfect — some EDs in deep fade couldn't be compensated.
  - 95% MNIST accuracy in both IID and heterogeneous (non-IID) data settings.

## Concepts introduced or reinforced
- [[ppdu-design]] — custom frame for WiFi-inspired AirComp signaling
- [[golay-sequence-sync]] — frame sync via repeated Golay
- [[zadoff-chu-calibration]] — timing calibration
- [[polar-code-signaling]] — control-plane coding for AirComp
- [[calibration-procedure]] — closed-loop time/CFO/power calibration

## Questions this source raised
- Phase synchronization is the Achilles heel for coherent AirComp; FSK-MV sidesteps it but loses analog precision. Jayden's pipeline assumes magnitude alignment (HPSR utility function), which requires phase coherence or at least consistent energy accumulation — closer to coherent than FSK-MV. Design choice to revisit.
- The demo uses CSI feedback for rough power control; full channel inversion was not attempted.
- Polar-128 + CRC-8 @ rate 1/2 is the demo's FEC; Jayden could reuse directly.

## Related
- [[system-pipeline]] — the pipeline inherits PPDU + calibration pattern from here
- [[paper-fsk-mv]] — the algorithm demonstrated
- [[robust-signaling]] — summary of Gold/Golay/FEC choices
