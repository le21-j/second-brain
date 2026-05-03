---
title: 5G NR PUSCH structure — DM-RS, TBS, HARQ timing
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - 5g-nr
  - pusch
  - dm-rs
  - transport-block
  - harq
  - 3gpp
  - phase-3
  - phase-4
sources:
  - "[[paper-nrx-wiesmayr-2024]]"
  - "[[paper-sionna-research-kit-2025]]"
created: 2026-05-01
updated: 2026-05-01
---

# 5G NR PUSCH structure — DM-RS, TBS, HARQ timing

## In one line
**The Physical Uplink Shared Channel (PUSCH) is the 5G NR data-bearing uplink channel — and any standard-compliant neural receiver ([[paper-nrx-wiesmayr-2024]]) must consume the exact same resource grid, pilot pattern, transport-block-size table, and HARQ feedback timing as the 3GPP standard.** This page is the cheat sheet of those four things.

## Why this matters for the NVIDIA cold email

Before the first technical screen, expect questions like:
- "How is DM-RS placed on the resource grid for PUSCH Type 1?"
- "If MCS index 17 with 100 RBs and 12 OFDM symbols, what's the transport block size?"
- "What's the HARQ feedback timing in slot $n$ for a PUSCH transmission in slot $n - K_2$?"

If any of those land flat, you've signaled non-compliance fluency. **The Wiesmayr-Cammerer-Hoydis cluster cares because their work is *standard-compliant* by definition.**

## 1. Resource grid + numerology

Recall from [[ofdm-phy-basics]]: a **resource element (RE)** = (1 subcarrier, 1 OFDM symbol). A **resource block (RB)** = 12 contiguous subcarriers. A **slot** = 14 OFDM symbols (normal CP).

| Numerology $\mu$ | Subcarrier spacing | Slot duration | Symbols/slot |
|---|---|---|---|
| 0 | 15 kHz | 1 ms | 14 |
| 1 | 30 kHz | 0.5 ms | 14 |
| 2 | 60 kHz | 0.25 ms | 14 |
| 3 | 120 kHz | 0.125 ms | 14 |

**5G FR1 (sub-6 GHz)** typically uses $\mu = 0, 1$. **FR2 (mmWave)** uses $\mu = 2, 3$. AirComp Numerology 0 = $\mu = 0$ (15 kHz SCS, see [[system-pipeline]]).

## 2. DM-RS pilot structure

**DM-RS** (Demodulation Reference Signal) = the pilots placed in the resource grid for channel estimation. **The neural receiver sees DM-RS positions and must use them.**

Two configuration types:

| Type | Subcarrier pattern | CDM groups | Use case |
|---|---|---|---|
| **Type 1** | every other subcarrier (comb-2) | 2 | most common; full-rank with 4 ports |
| **Type 2** | 4 subcarriers per RB | 3 | up to 12 ports (massive MIMO) |

DM-RS lives in **specific OFDM symbols** of the slot. Configurable via:
- **Mapping Type A** — DM-RS at symbol 2 or 3 (frame-aligned).
- **Mapping Type B** — DM-RS at symbol 0 (mini-slot / short-PUSCH).

**Additional DM-RS positions** (1, 2, or 3 extra symbols) may be configured for high-Doppler scenarios — without them, the channel estimate ages over the slot.

> [!note] What the NRX consumes
> [[paper-nrx-wiesmayr-2024]]'s NRX takes a **resource grid with DM-RS already inserted** as input. It learns to use the pilots for joint channel estimation + demapping. Mismatched DM-RS positions → 3+ dB BLER degradation in the reproduction.

**3GPP spec anchor:** TR 38.211 §6.4 (DM-RS for PUSCH).

## 3. Transport block size (TBS)

**TBS** = number of information bits per slot, before LDPC encoding. Computed by:
1. Look up MCS index → modulation order $Q_m$ + target code rate $R$ from MCS Table.
2. Compute approximate raw bits $N_{\text{RE}} \cdot Q_m$, where $N_{\text{RE}}$ counts non-DM-RS REs.
3. Apply $R$ to get number of info bits.
4. Quantize to nearest valid TBS in the TBS table.

Some headline numbers worth memorizing:
- **MCS 0** (QPSK, $R \approx 0.12$): ~120 bits per RB-slot
- **MCS 17** (16-QAM, $R \approx 0.6$): ~700 bits per RB-slot
- **MCS 27** (64-QAM, $R \approx 0.93$): ~1300 bits per RB-slot

Full TBS table is in **3GPP TS 38.214 §5.1.3** (downlink) / **§6.1.4** (uplink). Sionna implements this exactly.

> [!warning] Standard-compliance trap
> A "neural receiver that beats LMMSE on synthetic CDL channels" is interesting; a "neural receiver that beats LMMSE on **standard-compliant PUSCH with the right TBS table and DM-RS positions**" is publishable. The 3GPP machinery is **what separates Cammerer-2023 from Wiesmayr-2024**.

## 4. HARQ timing

When the BS receives a PUSCH transmission in slot $n$, it sends ACK/NACK on the downlink in slot $n + K_1$ (where $K_1$ depends on numerology + processing time). On NACK, the UE retransmits in slot $n + K_1 + K_2$.

Three HARQ-control fields the UE / receiver must track:
- **HARQ process ID** (0..15) — which transport block this is.
- **NDI** (New Data Indicator) — toggles to signal "this is a fresh TB", not a retransmission.
- **RV** (Redundancy Version, 0/2/3/1) — which subset of the LDPC parity bits is being sent.

Up to 4 retransmissions; chase-combining or incremental-redundancy combine the soft LLRs across them. See [[harq]] for the algorithmic detail.

**3GPP spec anchor:** TS 38.214 §6.1.5 (UL HARQ-ACK timing).

## Where this fits in the 3GPP spec triangle

| Spec | What it covers | Which Sionna module |
|---|---|---|
| **TS 38.211** | Physical channels + signals (DM-RS, PT-RS, SRS) | `sionna.phy.pusch.PUSCHTransmitter` |
| **TS 38.212** | Multiplexing + channel coding (LDPC base graphs, rate matching, segmentation) | `sionna.phy.fec.ldpc` |
| **TS 38.214** | Procedures for the data-channel (MCS / TBS / HARQ timing) | `sionna.phy.pusch.PUSCHConfig` |

> [!tip] Reading order
> Don't read these specs cover-to-cover (~500 pages each). **Skim TS 38.214 §5.1.3 (TBS), TS 38.211 §6.4 (DM-RS), and TS 38.214 §6.1.5 (HARQ timing) before the NVIDIA technical screen.** That's ~30 pages total.

## Common interview questions (Sionna-team probes)

1. **"How does DM-RS density trade against data throughput?"** — More pilots = better channel estimation = lower BLER, but fewer data REs = lower throughput. Type 1 (comb-2) wastes 50% of subcarriers in DM-RS symbols; additional DM-RS symbols cost more.
2. **"Why does Wiesmayr's NRX achieve standard-compliance only at certain configurations?"** — TBS table + LDPC base-graph selection (BG1 vs BG2) is configuration-dependent; an NRX trained on BG1 (long codes) won't match BG2 (short codes). [[paper-nrx-wiesmayr-2024]]'s testbed picks specific configs to stay in the standard envelope.
3. **"What's the difference between PDSCH and PUSCH for an NRX?"** — Direction (DL vs UL), DM-RS structure (PDSCH supports more port configurations), and timing reference (PDSCH is BS→UE, PUSCH is UE→BS — affects channel coherence assumptions).

## Common mistakes
- **Confusing PDSCH (downlink data) with PUSCH (uplink data).** The NRX papers focus on PUSCH receiver; the channel-prediction line ([[paper-lwm-temporal-2026]]) often targets PDSCH.
- **Ignoring CRC + segmentation.** TBS doesn't equal raw info bits — there's a 16-bit (small TBs) or 24-bit (large TBs) CRC, plus segmentation if TB > 8448 bits.
- **Treating DM-RS pattern as static.** It's RRC-configurable; an NRX trained on one config won't generalize.

## Related
- [[ofdm-phy-basics]] — the resource-grid foundation.
- [[harq]] — the retransmission protocol.
- [[ldpc-codes]] — what 38.212 §5 specifies for the data channel.
- [[neural-receiver]] — operates on this exact structure.
- [[link-adaptation]] — selects MCS that determines TBS.
- [[paper-nrx-cammerer-2023]] — uses simplified PUSCH-like grid.
- [[paper-nrx-wiesmayr-2024]] — **standard-compliant PUSCH; the most direct application of this page.**
- [[paper-sionna-research-kit-2025]] — Jetson testbed runs this stack.
- [[sionna-api-cheatsheet]] — Sionna 2.x API for instantiating PUSCH configs.
- [[python-ml-wireless]]

## Practice
- **TODO (Phase 3 M7)** — Open Sionna 2.x; instantiate a `PUSCHConfig` with $\mu = 0$, MCS = 14, 100 RBs, mapping Type A. Read off the resulting `num_info_bits` (should match the 38.214 TBS table). Then change DM-RS to Type 2 + 1 additional symbol; re-check info bits.
