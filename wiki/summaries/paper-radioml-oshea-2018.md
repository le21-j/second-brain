---
title: "O'Shea, Roy, Clancy 2018 — Over-the-Air Deep Learning Based Radio Signal Classification (RadioML)"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/radioml-oshea-2018.pdf
source_date: 2018
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - radioml
  - modulation-classification
  - oshea
  - dataset
  - foundational
  - reproduction-target
created: 2026-05-01
updated: 2026-05-01
---

# O'Shea, Roy, Clancy 2018 — Over-the-Air Deep Learning Based Radio Signal Classification

**Authors:** Tim O'Shea (Virginia Tech / DeepSig), Tamoghna Roy (DeepSig), T. Charles Clancy (Virginia Tech). **IEEE JSTSP 2018** / **arxiv:1712.04578**. Dataset: **RadioML 2018.01A** at https://www.deepsig.ai/datasets/. Mirrored at `raw/articles/ml-phy/pdfs/radioml-oshea-2018.pdf`.

## TL;DR
The **RadioML 2018.01A dataset paper.** Releases a 24-modulation dataset captured over-the-air with realistic channel impairments (CFO, multipath, hardware nonlinearity) and benchmarks a CNN/ResNet/inception-style classifier. Establishes **automatic modulation classification (AMC)** as a deep-learning benchmark task. Used in 100+ subsequent papers. **Phase 2 Month 5 reproduction target.**

## Key contributions

1. **RadioML 2018.01A dataset.** 24 modulations (AM-DSB, FM, OOK, BPSK, QPSK, 8PSK, 16QAM, 64QAM, OFDM, GMSK, etc.); SNR sweep -20 to +30 dB in 2 dB steps; **2.5M samples**; over-the-air captured via USRP (not synthetic).
2. **Benchmark CNN/ResNet/Inception.** Demonstrates that a 1D ResNet achieves **>95% accuracy at SNR ≥ +6 dB** across all 24 modulations.
3. **CFO and channel-impairment robustness.** Includes residual carrier-frequency-offset, multipath, and hardware nonlinearity in the captures — making the benchmark substantially harder than synthetic-channel tests.
4. **Earlier RadioML 2016.10a dataset** (11 modulations, smaller) is the predecessor; 2018.01A is the canonical version for any modern paper.

## Methods

- **Capture:** USRP-pair over an SDR testbed, with deliberate CFO drift, indoor multipath, and PA-induced nonlinearity.
- **Architectures benchmarked:** small CNN (the original 2016 baseline); ResNet (residual blocks); Inception-style; LSTM (for sequence modeling).
- **Input:** $1024 \times 2$ real-valued I/Q windows; **alternative:** $128 \times 2$ for shorter-window experiments.

## Results

- **ResNet > CNN > LSTM** in accuracy and training time.
- **>95% accuracy** at SNR $\geq 6$ dB; gracefully degrades to ~50% at -10 dB.
- **CFO robustness:** with on-the-fly CFO injection during training, the classifier remains accurate even under residual frequency offsets up to $\pm 100$ Hz.

## Why it matters / where it sits in the roadmap

- **Phase 2 Month 5 deliverable** — "Reproduce RadioML modulation classification: CNN/ResNet/Transformer comparison with per-SNR accuracy curves and CFO robustness."
- **First "transformer-block-swap" experiment** of the roadmap — establish CNN/ResNet baselines, then add a small transformer head, compare.
- **Bridge to NVIDIA application timing.** Phase 2 M5 aligns with the **September NVIDIA early intern application window** — a polished RadioML repo by then is the strongest possible application artifact at that stage.

## Concepts grounded

- [[modulation-classification]] — primary concept page.
- [[convolutional-neural-network]] — ResNet backbone.
- [[transformer]] — comparison architecture.
- [[autoencoder-phy]] — sibling line (O'Shea's other 2017 paper).

## Portfolio move (Phase 2 M5)

> Reproduce RadioML modulation classification: CNN, ResNet, and a small Transformer with per-SNR accuracy curves and CFO robustness testing.

Steps:
1. Download RadioML 2018.01A from https://www.deepsig.ai/datasets/.
2. PyTorch Lightning + Hydra: 1D-CNN baseline → 1D-ResNet → small Transformer head.
3. Per-SNR accuracy curves on test split.
4. CFO injection during training — robustness curve.
5. Report confusion matrices to show which modulations get confused at low SNR.

## Questions raised
- **Domain gap to real spectrum.** Even though RadioML is OTA-captured, the diversity of modulations and channels is constrained by the testbed. For real-world performance, supplement with TorchSig.
- **Newer datasets.** RadioML 2024.x, GNU Radio dataset variants — defer.

## Related
- [[python-ml-wireless]]
- [[modulation-classification]]
- [[paper-oshea-hoydis-2017-autoencoder]] — sibling paper, same author.
- [[oshea]] — author / DeepSig founder.
