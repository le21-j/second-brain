---
title: "Morais, Alikhani, Malhotra, Hamidi-Rad, Alkhateeb 2026 — Wireless Dataset Similarity: Measuring Distances in Supervised and Unsupervised ML"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/morais-similarity-2026.pdf
source_date: 2026-01-03
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - dataset-similarity
  - sim-to-real
  - transfer-learning
  - alkhateeb
  - morais
  - alikhani
  - asu-wi-lab
  - interdigital
created: 2026-05-01
updated: 2026-05-01
---

# Morais et al. 2026 — Wireless Dataset Similarity: Measuring Distances in Supervised and Unsupervised ML

**Authors:** João Morais (Wi-Lab → NVIDIA), Sadjad Alikhani (Wi-Lab), Akshay Malhotra & Shahab Hamidi-Rad (InterDigital), Ahmed Alkhateeb (Wi-Lab @ ASU). **arxiv:2601.01023** (Jan 2026). Mirrored at `raw/articles/ml-phy/pdfs/morais-similarity-2026.pdf`.

## TL;DR
**A task- and model-aware framework for measuring "distance" between wireless datasets** — applied to dataset selection, sim-to-real comparison, synthetic-data generation, and model deployment. UMAP embeddings + Wasserstein/Euclidean distances achieve **Pearson > 0.85 correlation between dataset distance and cross-dataset transferability** for both unsupervised (CSI compression with autoencoders) and supervised (beam prediction with CNN) tasks. **Solves the "is my pretraining dataset similar enough to my deployment?" problem.**

## Key contributions

1. **Task-aware dataset distance framework.** Define distance metrics that correlate with cross-dataset transfer performance (train-on-A, test-on-B).
2. **UMAP-based unsupervised distance.** Embed both datasets via UMAP → compute Wasserstein / Euclidean distance between embeddings. Pearson > 0.85 with autoencoder transferability for CSI compression.
3. **Label-aware supervised distance.** Integrates supervised UMAP + dataset-imbalance penalties. Outperforms classical baselines for beam-prediction transferability.
4. **Three target use cases:**
   - **Distribution-shift detection** — flag when deployment data drifts from training data.
   - **Transfer-learning dataset selection** — pick the most-transferable pretraining dataset.
   - **Synthetic data augmentation** — generate synthetic samples that close the distribution gap.

## Methods
- **Test datasets:** various DeepMIMO scenarios + DeepSense subsets.
- **CSI compression task:** CsiNet-style autoencoder — train on dataset $D_A$, evaluate NMSE on dataset $D_B$. Plot $d(D_A, D_B)$ vs. NMSE; look for high correlation.
- **Beam prediction task:** CNN predicting beam index — train-on-one / test-on-another.
- **Distance metrics evaluated:** Wasserstein (UMAP-embedded), Euclidean (raw + UMAP-embedded), classical KL, Jensen-Shannon, Frechet (FID-style).

## Results
- **CSI compression — Pearson > 0.85** between UMAP-Wasserstein distance and cross-dataset NMSE.
- **Beam prediction — label-aware UMAP** beats unsupervised distance by ~10% Pearson.
- Classical KL / JS / FID metrics underperform UMAP-based metrics.

## Why it matters / where it sits in the roadmap

- **The sim-to-real pillar of the roadmap.** [[python-ml-wireless]] explicitly flags **sim-to-real honesty**: "any PHY-ML result that only uses one channel model / one SNR / one scenario gets flagged as 'validated the simulator, not the method.'" This paper IS the analytical framework for that flagging.
- **Direct Wi-Lab cold-email talking point.** Morais (now at NVIDIA) is the connective-tissue alumnus; co-authoring with Alikhani (LWM family) is intentional.
- **InterDigital co-authorship** — industrial validation; matters for Wi-Lab thesis stories about deployment.
- **Phase 4 M11 capstone enabler.** Any LWM extension that claims "transfer learning" must measure dataset similarity — this paper is the metric.

## Baselines compared
- **Classical KL divergence** between channel distributions.
- **Jensen-Shannon divergence.**
- **Frechet Inception Distance (FID)** adapted to channels.
- **Maximum Mean Discrepancy (MMD).**

## Concepts grounded
- [[deepmimo]], [[deepsense-6g]] — dataset sources.
- [[csi-feedback]] — application task.
- [[beam-prediction]] — application task.
- [[large-wireless-model]] — natural downstream consumer.

## Portfolio move (Phase 4)
**Reproduce first.** Compute UMAP-Wasserstein dataset distances between two DeepMIMO scenarios (e.g., O1_28 vs Boston5G_28); train CsiNet on one, test on the other; plot distance vs. NMSE.

**Extend.** Apply to LWM transferability: predict whether a pretraining dataset will transfer well to a held-out scenario before fine-tuning.

> [!tip] Interviewer talking point (Wi-Lab)
> "I implemented the Morais 2026 dataset-similarity metric and used it to predict LWM transferability across DeepMIMO scenarios — 0.87 Pearson with downstream NMSE."

## Related
- [[python-ml-wireless]]
- [[paper-deepmimo-2019]], [[paper-deepsense-6g-2023]] — dataset sources.
- [[paper-lwm-2024]], [[paper-lwm-temporal-2026]] — natural extension targets.
- [[paper-csinet-wen-2018]] — CSI-compression baseline.
- [[morais]], [[alikhani]], [[alkhateeb]] — Wi-Lab team.
