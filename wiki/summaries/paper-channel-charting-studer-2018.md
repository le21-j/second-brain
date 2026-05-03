---
title: "Studer et al. 2018 — Channel Charting"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/channel-charting-studer-2018.pdf
source_date: 2018
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - channel-charting
  - studer
  - self-supervised
  - localization
  - massive-mimo
created: 2026-05-01
updated: 2026-05-01
---

# Studer, Medjkouh, Gönültaş, Goldstein, Tirkkonen 2018 — Channel Charting

**Authors:** Christoph Studer (ETH Zürich, then Cornell), Saïd Medjkouh, Emre Gönültaş, Tom Goldstein (UMD), Olav Tirkkonen (Aalto). **arxiv:1807.05247**. Mirrored at `raw/articles/ml-phy/pdfs/channel-charting-studer-2018.pdf`.

## TL;DR
**Channel Charting** is a **self-supervised** technique that takes raw CSI samples and learns a low-dimensional embedding (a "chart") preserving **spatial neighborhood** structure — without needing ground-truth user locations. Functionally, it's t-SNE / UMAP / Siamese networks applied to CSI distance metrics. Enables **GPS-free positioning, beam-management priors, and proximity-based handover** in massive-MIMO.

## Key contributions

1. **Self-supervised positioning.** No GPS, no labeled positions — only the assumption that **CSI changes smoothly with UE motion**. Use this implicit "near-in-CSI ⇒ near-in-space" prior.
2. **Distance metrics in CSI space.** Define $d_\text{CSI}(H_i, H_j)$ via correlation, angle, or kernel — the choice matters and is paper-dependent.
3. **Manifold-learning algorithms.** Sammon's mapping, t-SNE, autoencoders, and Siamese networks all produce useful charts.
4. **Massive-MIMO context.** The richness of multi-antenna CSI is what makes charts work — single-antenna systems don't have enough information.

## Methods

- **CSI vector:** stacked complex channels $H \in \mathbb{C}^{N_t \times N_f}$; vectorize.
- **Distance:** $d(H_i, H_j) = 1 - |\langle H_i, H_j \rangle|^2 / (\|H_i\|^2 \|H_j\|^2)$ (the cosine-similarity-based metric proposed in the paper).
- **Embedding:** Sammon's mapping or autoencoder bottleneck → 2D coordinates.

## Results

- Charts recover **continuous spatial neighborhood structure** (a UE moving in a circle traces a circle in chart space).
- The chart can be calibrated against a few labeled GPS points to give absolute positioning.
- **Robust to multipath.** In NLoS scenarios where geometric positioning fails, channel charts still capture proximity.

## Why it matters / where it sits in the roadmap

- **Phase 4 candidate downstream task** — channel charting is one of the [[large-wireless-model]] downstream tasks (LWM features → chart fine-tune).
- Bridges **self-supervised representation learning** (the modern ML paradigm) and **wireless sensing** — the fashion-forward research direction in 2024–2026.
- Wi-Lab has published in this space; cite this paper in any positioning / sensing-related Wi-Lab cold-email.

## Concepts grounded

- [[channel-charting]] — primary concept page.
- [[csi-feedback]] — adjacent compressive technique.
- [[large-wireless-model]] — channel charting can be a downstream task.

## Portfolio move (optional Phase 4)

> Use LWM-pretrained features + channel-charting head on a DeepMIMO scenario; compare against from-scratch Sammon mapping.

This isn't on the explicit Phase-4 list but would be a credible LWM-extension paper in the M11 capstone window.

## Questions raised
- **Absolute positioning calibration** with minimal labeled samples — open research direction.
- **Time-varying environments** (mobility, blockage) — charts can drift; how to maintain over time?

## Related
- [[python-ml-wireless]]
- [[channel-charting]]
- [[csi-feedback]]
- [[large-wireless-model]]
- [[deepmimo]] — natural data source.
- [[studer]] — author (TBD as person page).
