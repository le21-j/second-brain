---
title: "Dörner, Cammerer, Hoydis, ten Brink 2018 — Deep Learning-Based Communication over the Air"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/dorner-2018-otaair.pdf
source_date: 2018
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - autoencoder
  - sdr
  - dorner
  - cammerer
  - hoydis
  - over-the-air
  - reproduction-target
created: 2026-05-01
updated: 2026-05-01
---

# Dörner, Cammerer, Hoydis, ten Brink 2018 — Deep Learning-Based Communication over the Air

**Authors:** Sebastian Dörner, Sebastian Cammerer, Jakob Hoydis, Stephan ten Brink (University of Stuttgart + Bell Labs). **IEEE JSTSP 2018** / **arxiv:1707.03384**. Mirrored at `raw/articles/ml-phy/pdfs/dorner-2018-otaair.pdf`.

## TL;DR
The **first fully neural-network-trained communication system actually deployed over the air via SDR.** Trains the autoencoder of [[paper-oshea-hoydis-2017-autoencoder]] on a simulated channel, then deploys to a USRP-pair link, fine-tunes online with a training-feedback channel, and demonstrates real-world BER-vs-Eb/N0 curves. Proves the autoencoder PHY paradigm survives sim-to-real transfer.

## Key contributions

1. **Real over-the-air deployment** of a learned PHY. Two USRPs running learned encoder/decoder networks, connected by an actual radio channel.
2. **Online fine-tuning.** Demonstrates that a sim-trained model can be **fine-tuned online** using a feedback channel that delivers ground-truth bits — closing the sim-to-real gap.
3. **Hardware impairment learning.** The fine-tuned receiver implicitly learns CFO, IQ imbalance, and PA nonlinearity correction — without explicit modeling.

## Why it matters

- **Validates the autoencoder-PHY thesis** at the bit level on real hardware.
- **Sets the deployment template** for any subsequent SDR-based PHY-ML system.
- **Sim-to-real honesty.** The roadmap's "validated the simulator, not the method" critique applies less to this paper because it actually crossed the gap.

## Roadmap relevance

- **Phase 2 stretch reproduction** — most relevant for the optional "$30 RTL-SDR listening exercise" + autoencoder over real hardware.
- **Reading reference** for any Phase 4 site-specific deployment work.

## Concepts grounded

- [[autoencoder-phy]]
- [[neural-receiver]]
- [[modulation-classification]] (transferable techniques)

## Related
- [[paper-oshea-hoydis-2017-autoencoder]] — the simulated predecessor.
- [[paper-aitaoudia-hoydis-2020-ofdm]] — pilotless OFDM extension.
- [[hoydis]], [[cammerer]] — authors.
