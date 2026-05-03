---
title: "Aït Aoudia & Hoydis 2020 — End-to-end Learning for OFDM"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/aitaoudia-hoydis-2020-ofdm.pdf
source_date: 2020
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - autoencoder
  - ofdm
  - aitaoudia
  - hoydis
  - pilotless
created: 2026-05-01
updated: 2026-05-01
---

# Aït Aoudia & Hoydis 2020 — End-to-end Learning for OFDM

**Authors:** Fayçal Aït Aoudia, Jakob Hoydis (Bell Labs / NVIDIA). **arxiv:2009.05261**. Mirrored at `raw/articles/ml-phy/pdfs/aitaoudia-hoydis-2020-ofdm.pdf`.

## TL;DR
Trains a **pilotless** OFDM end-to-end autoencoder where both transmitter (constellation + pilot pattern) and receiver are learned. Recovers spectral efficiency by removing the explicit pilot overhead — the "pilots" become part of the learned constellation itself. The follow-on to [[paper-oshea-hoydis-2017-autoencoder]] specifically for OFDM systems.

## Key contributions

1. **Pilot-free design.** Standard OFDM allocates ~5–10% of resource elements to DMRS pilots. This paper trains a system that uses **none** — receiver learns to extract channel info from data symbols themselves.
2. **Joint TX/RX optimization with realistic OFDM constraints.** Includes CP, FFT, frequency-domain channel.
3. **Performance vs. spectral overhead.** Quantifies the BLER-vs-overhead trade-off — pilotless E2E beats pilot-based receivers when the channel is slowly varying.

## Why it matters

- **Spectral efficiency** — the dream of "zero overhead" PHY-ML.
- **Limit case for autoencoder-PHY** — useful counterpoint to [[paper-nrx-cammerer-2023]] which keeps pilots.

## Roadmap relevance

- **Phase 2 reproduction** — could be a stretch goal after the basic O'Shea-Hoydis 2017 reproduction.
- **Phase 3 reading** — informs the design choices of modern NRX work.

## Concepts grounded

- [[autoencoder-phy]]
- [[ofdm]]
- [[neural-receiver]]

## Related
- [[paper-oshea-hoydis-2017-autoencoder]]
- [[paper-nrx-cammerer-2023]]
- [[hoydis]]
