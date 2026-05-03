---
title: OFDM PHY basics — subcarriers, CP, pilot grid
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - ofdm
  - phy
  - 5g-nr
  - subcarrier
  - cyclic-prefix
  - pilots
  - resource-grid
  - phase-1
  - phase-3
sources:
  - "[[textbook-pysdr-lichtman]]"
  - "[[paper-aitaoudia-hoydis-2020-ofdm]]"
  - "[[paper-nrx-wiesmayr-2024]]"
created: 2026-05-01
updated: 2026-05-01
---

# OFDM PHY basics — subcarriers, CP, pilot grid

## In one line
**OFDM is a multicarrier transmission scheme that turns a frequency-selective channel into a parallel set of flat-fading channels — by splitting bandwidth into $N$ orthogonal subcarriers, prefixing each block with a cyclic prefix, and using a known pilot pattern for channel estimation.**

## Example first — 5G NR Numerology 0

| Parameter | 5G NR Numerology 0 |
|---|---|
| Subcarrier spacing $\Delta f$ | 15 kHz |
| Total subcarriers $N$ | 1024 (typical FFT size; data uses subset) |
| FFT size for AirComp / [[system-pipeline]] | 128 |
| Cyclic prefix length | 32 samples (normal CP) |
| Active subcarriers | 600 (NR FR1 typical 10 MHz BW) |
| Sample rate | 1.92 MHz (Numerology 0, narrow-band) |
| Symbol duration | 71.4 μs (CP-extended) |
| Slot duration | 1 ms (14 OFDM symbols) |

A **resource grid** = (time × frequency) lattice. Each cell ("resource element", RE) carries one QAM symbol. A 5G NR slot = 14 symbols × 12 subcarriers/RB = 168 REs per resource block.

## The idea — three load-bearing features

### 1. Subcarrier orthogonality
Choose subcarrier spacing $\Delta f$ so that adjacent carriers are **orthogonal over a symbol period** $T = 1/\Delta f$. Sum of complex sinusoids at multiples of $\Delta f$ has zero cross-correlation when integrated over $T$.

This is what the IFFT/FFT pair achieves automatically — modulating $N$ subcarriers via IFFT generates an orthogonal time-domain signal; the FFT at the receiver inverts it.

### 2. Cyclic prefix (CP)
Multipath fading causes inter-symbol interference (ISI). Adding a **cyclic prefix** — copying the last $L_{cp}$ samples of an OFDM symbol to its front — converts linear convolution with the channel into **circular convolution** within the FFT window. After FFT, the channel becomes diagonal: each subcarrier sees its own scalar gain $H[k]$.

CP length must exceed the channel's delay spread. 5G NR normal CP is 32 samples at Numerology 0 (≈ 4.7 μs delay spread tolerance).

### 3. Pilot grid
You can't equalize what you can't estimate. A subset of REs carry **known pilots**; the receiver estimates $H[k, t]$ at pilot positions and interpolates across (frequency, time) for data REs.

5G NR typical: **DM-RS** pilots in specific OFDM symbols of the slot, allowing per-slot channel-estimate refresh. The pilot pattern matters — an [[paper-nrx-wiesmayr-2024|NRX]] sees pilots and data jointly; mismatched pilot positions break the model.

## OFDM transceiver block diagram

```
TX:  bits → QAM → S/P → IFFT → +CP → P/S → DAC → RF
                                                     ↓ channel + noise
RX:  RF → ADC → S/P → -CP → FFT → equalize → P/S → demap → bits
                            ↑
                       ← pilots → channel estimation
```

## Where OFDM appears in the roadmap

- **Phase 1 M2** — [[python-ml-wireless]] M2 deliverable: "OFDM-from-scratch notebook — BER vs Eb/N0 vs theory." This concept page is the prereq.
- **Phase 3 M7** — Sionna NRX modification ([[paper-nrx-cammerer-2023]] reproduction) operates on a 5G NR-style resource grid.
- **AirComp (Jayden's existing work)** uses OFDM at Numerology 0 with N=128, CP=32 — see [[system-pipeline]].
- **Aıt Aoudia & Hoydis 2020** ([[paper-aitaoudia-hoydis-2020-ofdm]]) — end-to-end OFDM autoencoder learns its own pilot pattern + receiver. **The Phase 2 M4 reproduction operates entirely on OFDM grids.**

## Common mistakes

- **CP too short for the channel's delay spread.** Inter-symbol interference returns; BER floor.
- **Pilot interpolation between widely-spaced pilots.** Channel decorrelates; estimate is bad. 5G NR pilot density tracks the coherence bandwidth.
- **Ignoring DC subcarrier null.** 5G NR / Wi-Fi blank the DC subcarrier (carrier leakage); leaving it active causes a notch at baseband.
- **Wrong PAPR handling.** OFDM has high peak-to-average power ratio (~10 dB). Naïvely applying a saturating PA destroys orthogonality — see [[paper-signal-peak-power]].

## Related

- [[ofdm]] — a related higher-level umbrella concept page.
- [[textbook-pysdr-lichtman]] — Ch 12 is the canonical OFDM-from-scratch reference.
- [[paper-aitaoudia-hoydis-2020-ofdm]] — end-to-end learned OFDM (Phase 2 M4).
- [[paper-nrx-wiesmayr-2024]] — standard-compliant NRX consumes a 5G NR OFDM grid.
- [[neural-receiver]] — operates on the resource grid.
- [[system-pipeline]] — Jayden's AirComp OFDM stack.
- [[matched-filter]] — pilot-based channel estimation = matched filtering against pilot sequences.
- [[fading-channels]] — the channel OFDM converts to flat per-subcarrier.
- [[python-ml-wireless]]

## Practice
- **TODO (Phase 1 M2)** — Build OFDM-from-scratch in NumPy: 16-QAM data, 64 subcarriers, CP-16, AWGN; plot BER vs Eb/N0 against theoretical 16-QAM curve. **This is the M2 deliverable.**
