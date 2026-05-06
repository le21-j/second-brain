---
title: Channel charting
type: concept
course:
  - "[[python-ml-wireless]]"
tags: [phy-ml, self-supervised, csi, positioning, manifold-learning]
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-04-23
updated: 2026-05-06
---

# Channel charting

## In one line
A self-supervised method to learn a low-dimensional "chart" of user positions from massive-MIMO CSI alone, *without any GPS labels* — similar channels are placed near each other, dissimilar channels far apart, and the chart's geometry turns out to mirror the physical environment.

## Example first

You have a day of uplink CSI measurements from an $8$-element BS, across $500$ random UE positions. You want a map of where users were.

**Classical positioning:** triangulation needs extra signals (TDoA, AoA, fingerprint databases).

**Channel charting** (Studer et al. 2018):
1. Extract features from each CSI sample (e.g., sample covariance, beamspace projection).
2. Feed to a neural network (typically autoencoder or triplet-loss encoder).
3. Enforce: pairs of CSI samples that are *similar* in feature space map to nearby 2D points; dissimilar ones map far.
4. The learned 2D embedding — without labels — ends up matching the real physical geometry to within rotation/scale.

That 2D chart can then be used for handover, localization, anomaly detection, or just as a CSI fingerprint index.

## The idea

**Studer, Medjkouh, Gönültaş, Goldstein, Tirkkonen 2018** ([arxiv:1807.05247](https://arxiv.org/abs/1807.05247)). The key insight: CSI is an extremely rich geographic signature; **the manifold of CSI traces out the manifold of positions** in massive-MIMO. You don't need labels to discover the manifold — manifold-learning (autoencoders, t-SNE-like losses, triplet margin losses) finds it.

### Why this is elegant

- **Self-supervised.** No GPS needed (training label-free).
- **Privacy-preserving.** No real position data leaves the BS.
- **Directly useful.** The chart is a proxy for position, useful for handover prediction, beam prediction, fingerprint-based localization.
- **Physics-grounded.** The topology of CSI-space *provably* corresponds to position-space in massive-MIMO (up to symmetries).

### Architectures

- **Autoencoder** — reconstruction loss $+$ a 2D or 3D bottleneck.
- **Siamese networks** — pairs of similar-in-time CSI mapped close; dissimilar pushed apart.
- **Triplet-loss encoders** — anchor $+$ positive $+$ negative, standard metric-learning setup.
- **Graph-based** — build a KNN graph of CSI samples, apply Laplacian eigenmaps or UMAP.

### Modern extensions

- Combine with temporal priors (UE moves smoothly $\to$ successive CSI should map to nearby chart points).
- Fuse with sparse GPS beacons (semi-supervised).
- Foundation-model variant: use [[large-wireless-model]] as the feature extractor, then chart.

## Formal definition

Given unlabeled CSI samples $\mathbf{h}_1, \ldots, \mathbf{h}_N$, learn $f_\theta: \mathbb{C}^d \to \mathbb{R}^2$ (or $\mathbb{R}^3$) such that:

$$\big| f_\theta(\mathbf{h}_i) - f_\theta(\mathbf{h}_j) \big| \approx D(\mathbf{h}_i, \mathbf{h}_j)$$

where $D$ is a dissimilarity measure — often based on time-delay-of-arrival or angle-of-arrival features, not on raw CSI Euclidean distance (which is dominated by fast fading).

Performance metric: **CT / TW (continuity / trustworthiness)** — how well nearby points in the chart correspond to nearby positions (evaluated on a labeled held-out set).

## Why it matters / when you use it

- **Positioning without extra signals.** CSI is already measured for communication; channel charting repurposes it.
- **Anomaly detection.** A chart point that jumps far $=$ likely a hijacked or spoofed channel.
- **Feature engineering for downstream.** "Your estimated chart coords" is a strong input feature for any downstream PHY-ML model.

## Common mistakes

- **Training on shuffled data.** The natural CSI manifold has temporal structure; shuffling throws it away. Keep sessions / trajectories together for contrastive training.
- **Assuming rotation-invariance.** The learned chart has gauge freedom (rotate/scale/reflect). Always reference ground truth via a few known anchor points before comparing.
- **Using fast-fading-dominated features.** Large-scale features (spatial covariance eigenvalues, AoA histograms) are much more robust than raw complex CSI for chart stability.

## Research ties

- **Canonical paper:** Studer et al. 2018 (arxiv:1807.05247).
- **Authors:** Studer (now at ETH), Medjkouh, Gönültaş, Goldstein (UT Austin), Tirkkonen (Aalto).
- **Active area at Wi-Lab** — Kengmin Lin and others.

## Related
- [[large-wireless-model]] — natural feature extractor
- [[csi-feedback]] — a different use of CSI compression
- [[physical-layer-ml]]
- [[python-ml-wireless]]
