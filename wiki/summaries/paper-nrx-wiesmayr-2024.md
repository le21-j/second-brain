---
title: "Wiesmayr, Cammerer, Aït Aoudia, Hoydis et al. 2024 — Design of a Standard-Compliant Real-Time Neural Receiver for 5G NR"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/nrx-wiesmayr-2024.pdf
source_date: 2024
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - neural-receiver
  - nvidia
  - 5g-nr
  - real-time
  - quantization
  - wiesmayr
  - foundational
created: 2026-05-01
updated: 2026-05-01
---

# Wiesmayr et al. 2024 — Design of a Standard-Compliant Real-Time Neural Receiver for 5G NR

**Authors:** Reinhard Wiesmayr, Sebastian Cammerer, Fayçal Aït Aoudia, Jakob Hoydis (NVIDIA Research). **ICMLCN 2025** / **arxiv:2409.02912**. Code: https://github.com/NVlabs/neural_rx. Mirrored at `raw/articles/ml-phy/pdfs/nrx-wiesmayr-2024.pdf`.

## TL;DR
Builds on [[paper-nrx-cammerer-2023]] to deliver the **first real-time, standard-compliant** 5G NR neural receiver — runs on a single NVIDIA A100 within the strict latency budget of a PUSCH slot, achieves the same 1–2 dB BLER gain over LMMSE, and is **bit-level compatible** with deployed 5G UEs. The headline result: **deployable today on AI-RAN hardware**.

## Key contributions

1. **Latency engineering.** Slot processing must fit in $\sim 250\,\mu\text{s}$. Wiesmayr 2024 hits this via **mixed-precision (FP16/BF16)** inference, **operator fusion**, and **TensorRT export**. The earlier Cammerer 2023 NRX was FP32 and ran at ~5–10× real-time budget.
2. **Bit-level standard compliance.** Receiver passes 3GPP conformance tests — same outputs (within numerical tolerance) for deterministic test vectors. This is what makes the "deployable" claim real.
3. **Mixed-precision quantization-aware training.** Train at FP32, quantize-aware fine-tune to FP16/BF16. Pure post-training quantization loses ~0.5 dB BLER; QAT recovers it.
4. **Open-source release.** Full training + inference + evaluation code at https://github.com/NVlabs/neural_rx. **The single most important code drop in PHY-ML 2024.**

## Methods

- **Backbone:** simplified version of Cammerer 2023 — fewer residual blocks (3 vs 6), narrower attention, redesigned for memory locality.
- **Operator fusion:** Conv + BN + ReLU fused into a single TensorRT op; LayerNorm + Attention fused.
- **Channel:** 3GPP 38.901 UMi/UMa, both LoS and NLoS, multi-SNR curriculum -5 to 20 dB.
- **Hardware target:** NVIDIA A100 80GB (and downward to L4 / L40 for cost-effective deployment).

## Results

- **0.5–2 dB BLER gain** at $10^{-2}$ over LMMSE across UMi, UMa, RMa.
- **Real-time on A100:** processes a PUSCH slot in $< 200\,\mu\text{s}$.
- **5G NR test-vector compliance** — passes deterministic conformance.

## Why it matters / where it sits in the roadmap

- **The benchmark for any 2025+ neural-receiver work.** If your repo doesn't compare BLER + latency against this code, reviewers will ask why.
- **NVIDIA hiring lever.** This paper's code is the gateway: forking https://github.com/NVlabs/neural_rx, contributing a tutorial or a small extension, and citing it in a Sionna PR is the most direct path into NVIDIA Research's attention space.
- **AI-RAN deployment story.** Combined with **Sionna Research Kit** (Cammerer 2025) and **AODT**, this paper is part of NVIDIA's "AI-native 6G RAN" stack pitch.

## Concepts grounded

- [[neural-receiver]] — primary concept page; this is the headline real-time variant.
- [[sionna]] — built on Sionna 2.x.
- [[mixed-precision-training]] — *will be created* in foundation sprint.
- [[quantization-aware-training]] — *defer*.

## Portfolio move (Phase 4 M10)

> Combined with Sionna RT (Phase 4 M10) — **train a full neural receiver in Sionna RT (site-specific) using a custom OSM scene**.

The 2024 NRX is the **starting point** for site-specific NRX. Workflow:
1. Clone https://github.com/NVlabs/neural_rx; verify reproducibility on UMi.
2. Drop in a Sionna RT custom-scene channel sampler.
3. Pretrain on 3GPP UMi → fine-tune on the custom scene.
4. Compare site-specific BLER vs. cross-environment baseline.
5. Report findings in a workshop paper.

## Questions raised
- **Multi-cell / interference modeling** — current NRX trains on isolated cells; multi-cell mutual interference is an open extension.
- **Polar-decoder integration** for control channels — the 2024 NRX is data-channel only.

## Related
- [[python-ml-wireless]]
- [[neural-receiver]]
- [[paper-nrx-cammerer-2023]] — predecessor.
- [[paper-sionna-2022]] — the simulator.
- [[paper-sionna-rt-2023]] — site-specific channel source.
- [[hoydis]], [[wiesmayr]] — author pages (wiesmayr page TBD).
