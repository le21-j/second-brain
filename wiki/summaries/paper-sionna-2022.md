---
title: "Hoydis, Cammerer, Aït Aoudia et al. 2022 — Sionna: An Open-Source Library for Next-Generation Physical Layer Research"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/sionna-2022.pdf
source_date: 2022
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - sionna
  - nvidia
  - hoydis
  - cammerer
  - simulator
  - foundational
created: 2026-05-01
updated: 2026-05-01
---

# Sionna 2022 — An Open-Source Library for Next-Generation Physical Layer Research

**Authors:** Jakob Hoydis, Sebastian Cammerer, Fayçal Aït Aoudia, Avinash Vem, Nikolaus Binder, Guillermo Marcus, Alexander Keller (all NVIDIA Research). **arxiv:2203.11854** (March 2022). Mirrored at `raw/articles/ml-phy/pdfs/sionna-2022.pdf`.

## TL;DR
The white paper introducing **Sionna**, NVIDIA's GPU-accelerated, fully differentiable, open-source link-level simulator for 5G NR physical-layer research. Built on TensorFlow 2 (in 2022; PyTorch backend added in v2.x). The defining feature: **every signal-processing block — mapper, FFT, channel, demapper — is a differentiable tensor op**, so gradients flow end-to-end and you can train a neural receiver against a 3GPP UMi channel without writing any custom autograd code.

## Key contributions

1. **Differentiable PHY toolbox.** Exposes blocks for QAM mapping/demapping, OFDM modulation, 5G NR LDPC + polar coding, MIMO detection, 3GPP TR 38.901 channel models (UMi, UMa, RMa, InF, InH, TDL, CDL) — all as `tf.keras.layers.Layer` subclasses with custom backward passes.
2. **GPU-native simulation.** Batched Monte Carlo over $10^4$+ channel realizations on a single GPU. Sionna 2022 reports ~$100\times$ throughput vs. CPU MATLAB for equivalent simulations.
3. **Neural-receiver template.** Published `Neural Receiver` example (later expanded into [[paper-nrx-cammerer-2023]]) becomes the canonical starting point for PHY-ML research.
4. **Reference implementations** of textbook results — autoencoder over AWGN, OFDM-MIMO with LMMSE/MMSE-PIC/EP detectors, LDPC BP variants — all open source at https://github.com/NVlabs/sionna.

## Methods

- Stack: TensorFlow 2 + Keras + custom CUDA kernels. Fully framework-agnostic for Sionna RT (Mitsuba 3 + Dr.Jit).
- Code organized as `sionna.channel`, `sionna.mapping`, `sionna.ofdm`, `sionna.fec`, `sionna.mimo`, `sionna.utils`. Sionna 2.x reorganized into `sionna.phy`, `sionna.sys`, `sionna.rt`.

## Results / impact

- **2022 release → standard reference.** Within 18 months, Sionna became the citation-required baseline for any link-level ML paper.
- **Adopted as a teaching tool** — NVIDIA Developer YouTube tutorials, multiple Stanford / TUM courses build on it.
- **Lineage to Sionna RT (2023)**, NRX (2023), Sionna Research Kit (2025), AODT (2024–2026).

## Why it matters / where it sits in the roadmap

- **Phase 3 Month 7 deliverable** — the roadmap mandates running **Sionna Tutorials Parts 1–4 end-to-end on a GPU**, culminating in a modified neural receiver. This paper is the conceptual map for those tutorials.
- **NVIDIA application leverage.** A Sionna project on GitHub is the single strongest signal to the NVIDIA Sionna team. Reading and citing this paper in your repo README is part of the application package.

## Concepts grounded

- [[sionna]] — primary concept page (already detailed).
- [[differentiable-ray-tracing]] — the RT module gets its own paper ([[paper-sionna-rt-2023]]).
- [[neural-receiver]] — the canonical Sionna example.
- [[autoencoder-phy]] — productionized in Sionna's `Autoencoder` example.
- [[ofdm]] — `sionna.ofdm` is the cleanest pedagogical OFDM implementation.

## Reproduction / portfolio move

> Phase 3 M7 — Sionna tutorials Parts 1–4 + Transformer block swap + BLER curves on CDL-A and UMi.

Steps:
1. `pip install sionna` (verify 1.x vs 2.x — pin in `requirements.txt`).
2. Run `examples/Hello_World.ipynb` → `examples/Sionna_tutorial_part4.ipynb`.
3. Modify the neural receiver: replace one CNN block with a small Transformer encoder block.
4. Compare BLER curves on **CDL-A** (clustered delay line, simple) and **UMi** (3GPP urban micro-cell) at SNR -5 to 15 dB.
5. Push to GitHub with README, results table, headline figure, W&B link, Hydra config.

## Questions raised
- **Sionna 2.x migration.** The paper is TensorFlow-era. The PyTorch port (Sionna 2.x, 2025) is documented separately in NVIDIA blog posts; tutorials still mid-port as of April 2026.
- **System-level Sionna SYS** is post-2022. See newer papers for that part.

## Related
- [[python-ml-wireless]]
- [[sionna]]
- [[paper-sionna-rt-2023]] — the differentiable-RT extension.
- [[paper-nrx-cammerer-2023]] — first NRX built in Sionna.
- [[hoydis]], [[morais]] — NVIDIA people; Morais is the Wi-Lab → NVIDIA bridge.
