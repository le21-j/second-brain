---
title: Robust Signaling Layer — Gold/Golay/FEC/Sync
type: concept
course: [[research]]
tags: [signaling, golay, gold-codes, zadoff-chu, polar-code, crc, ppdu, wifi]
sources: [[paper-aircomp-feel-demo]], [[paper-aircomp-survey]]
created: 2026-04-21
updated: 2026-04-26
---

# Robust Signaling Layer

## In one line
A catalog of coding and sequence choices — frame sync (Golay), channel estimation (Zadoff-Chu), control signaling (polar + CRC), user identification (Gold codes), and WiFi-inspired ACK/MAC patterns — used to make the AirComp control plane reliable without depending on strong channel conditions.

## Example first
Jayden says "use Gold coding or FEC wherever you can." The [[paper-aircomp-feel-demo]] PPDU does exactly that at different layers:

| Role | Sequence/Code | Why |
|---|---|---|
| Frame sync | **Golay-32, 4$\times$ repeated** | Ideal autocorrelation, CFO-tolerant via repetition. |
| Channel estimation | **Zadoff-Chu-97** | Constant amplitude + flat spectrum $\to$ good LS. |
| Header (control) | **Polar-128, rate 1/2, BPSK + CRC-8** | Short payload, near-capacity, easy to decode. |
| Data | **Polar-128, rate 1/2, BPSK, 56-bit chunks** | Reuses header codec. |
| Phase tracking | **QPSK Golay-64** on pilot subcarriers | Corrects residual CFO drift mid-packet. |

## Gold vs Golay — a clarification
These are different things, often confused:

- **Golay sequence** — a pair $(G_a, G_b)$ of $\pm 1$ sequences with complementary autocorrelation ($R_{G_a} + R_{G_b} = \delta$). Used for **synchronization** because they have ideal peak-to-sidelobe after coherent addition. Used in 802.11ad and in the demo paper.
- **Gold code** — a family of pseudo-random sequences with **low cross-correlation** between different codes in the family. Used for **user identification** (CDMA, GPS satellites) because the ES can distinguish which user is transmitting even under superposition.

**Which does Jayden want?** Probably both:
- Golay for initial frame sync + channel estimation.
- Gold codes as per-ED **signature sequences** so that, in Stage 2 (ACK + CSI report), the ES can distinguish which ED is speaking even if two EDs accidentally overlap.

## WiFi-inspired protocol primitives (relevant to the pipeline)

- **Beacon frames (802.11):** periodic broadcasts carrying BSS info, sync, and capability bits. $\to$ Stage 1 in pipeline.
- **Association Request / Response:** devices announce identity, server assigns a short AID (Association ID). $\to$ Stage 2 user-ID assignment.
- **RTS/CTS (optional):** clear-to-send handshake to avoid hidden-terminal collisions. Could protect Stage 4 AirComp transmissions if multiple ESs are nearby.
- **Block ACK (802.11n):** one aggregated ACK for multiple MPDUs. $\to$ Stage 7 feedback ACK — aggregate instead of per-ED ACK.
- **NACK-less operation:** if a frame is not ACKed within a timeout, retransmit. $\to$ Stage 2 / Stage 7 dropout logic: no ACK $\to$ skip this epoch.
- **TSF (Timing Synchronization Function):** ES broadcasts a microsecond-precision clock in the beacon so EDs stay aligned. $\to$ Critical for AirComp phase coherence.

## FEC and CRC choices

- **FEC** — forward error correction on payload.
  - Polar codes (demo paper, 5G NR control channel): near-capacity at short block lengths.
  - LDPC (5G NR data channel): better for longer blocks.
  - Convolutional $+$ Viterbi (classical, 802.11a/g): simple, good fallback.
- **CRC** — error detection.
  - CRC-8 on 56-bit messages (demo paper): catches burst errors up to 8 bits.
  - CRC-32 on larger frames (802.11 MAC).

**Recommendation for Jayden:** mirror the demo paper. Polar-128 rate-1/2 + CRC-8 is a tested combo for exactly this setting.

## The PPDU template (lifted from [[paper-aircomp-feel-demo]])

```
┌────────────┬───────┬─────────┬────────┬─────────┐
│ Frame Sync │ CHEST │ Header  │ Data   │  ...    │
│ (Golay ZC) │ (ZC)  │ (Polar) │(Polar) │         │
└────────────┴───────┴─────────┴────────┴─────────┘
  CP+IFFT →  CP+IFFT → CP+IFFT → CP+IFFT → ...
```

Each block is an OFDM symbol with $N_{\text{IDFT}}=256$, $N_{\text{CP}}=64$, $M=192$ active subcarriers $+\,8$ DC subcarriers.

Signaling bits (in the data field):
- 4 bits — signaling type (`t_cal`, `t_feed`, `t_grd`, `t_mv`, or custom for Jayden's pipeline).
- 25 bits — user multiplexing (AID-like).
- 32 bits — time offset per ED (for calibration).
- 8 bits — power control per ED.

## Common mistakes
- **Mixing up Gold and Golay.** Gold $\neq$ Golay — one is for user-ID, the other for sync.
- **Skipping CRC on short control frames.** Undetected errors in 8-bit shift-factor fields can desync the whole network.
- **Designing sync waveform with high PAPR.** Frame-sync sequences transmit at full power; high PAPR causes the transmitter PA to clip. Golay $+$ low-order modulation (BPSK) keeps PAPR manageable.
- **Using the same preamble for every epoch.** An eavesdropper or interferer can lock onto it. Rotate / randomize per epoch.

## Related
- [[paper-aircomp-feel-demo]] — the template lifted here
- [[system-pipeline]] — how these fit into the end-to-end protocol
- [[zadoff-chu-sequence]] — ZC properties
- [[golay-complementary-pair]] — Golay properties
