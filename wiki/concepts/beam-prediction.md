---
title: Beam prediction
type: concept
course:
  - "[[python-ml-wireless]]"
tags: [phy-ml, mmwave, beam, deepsense, multi-modal, task]
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-04-23
updated: 2026-05-06
---

# Beam prediction

## In one line
Given sensors (camera, GPS, sub-6 CSI, radar, LiDAR — whatever you have cheap and fast), predict which of $K$ mmWave beams from a codebook will give the best link, **without sweeping** all $K$ beams.

## Example first

The mmWave BS has $64$ narrow beams. Sweeping all $64$ to find the best one takes milliseconds per UE and eats spectral efficiency. If a dashcam photo $+$ GPS can predict "beam 37 is best" with $78\%$ top-1 accuracy, you save $63/64$ of the sweep cost.

That's the DeepSense 6G 2022 challenge. Top-entry architectures:
- A **Vision Transformer** on the RGB frame, global-pooled.
- An **MLP** on GPS (lat, lon, alt, heading).
- (Optional) a small encoder on sub-6 CSI.
- Concatenate features $\to$ classification head $\to$ softmax over $64$ beams.

Losses: **cross-entropy on beam index** $+$ optionally a distance-weighted loss (DBA-style).

## The idea

Beam prediction is one of the cleanest success stories of **PHY-ML + sensing-comm integration**. The core argument:

> "The best mmWave beam is highly correlated with the physical position and surroundings of the UE. If you can see the UE (camera) or estimate its position (GPS, sub-6) or model its reflectors (LiDAR, radar), you can predict the beam without the sweep."

Lineage:
- **Wang, Narasimha, Heath 2018** (SPAWC) — first to frame "beam prediction with situational awareness." Coarse situational labels.
- **Alkhateeb Wi-Lab 2019–2023** — pure-channel and then multi-modal beam predictors.
- **Jiang & Alkhateeb 2022** — vision-aided beam *tracking* (GLOBECOM workshops).
- **Charan et al. 2022** (arxiv:2209.07519) — the DeepSense 2022 Challenge baseline.
- **Demirhan & Alkhateeb 2026** — radar-aided beam prediction and tracking, IEEE TCOM.
- **Jiang & Alkhateeb 2023** (arxiv:2301.07682) — digital-twin-based beam prediction (the twin generates ground truth, a predictor is trained on it).

### Input modalities in the literature

- **Position** (GPS) — cheapest, works best when the BS has line-of-sight $+$ good geometry.
- **Sub-6 CSI** — frequency-agnostic fingerprint of the environment.
- **RGB camera** — directly sees obstructions.
- **LiDAR / depth** — best for reflective environments.
- **Radar** — works in weather where cameras fail.
- **Multi-modal fusion** — usually wins, if synchronization is solid.

### Metrics

- **Top-$k$ accuracy** ($k=1, 3, 5$) — fraction of predictions whose top-$k$ contains the true best beam.
- **DBA-Score (Distance-Based Accuracy)** — weights errors by how far the predicted beam is from the true beam in the codebook (angular or RSRP distance).
- **Downstream data rate** — the operational metric: given your predictor, what rate does the link achieve?

## Formal definition

Observations $\mathbf{o}_t$ (multi-modal; any subset of the above). True best beam $b^*_t = \arg\max_i \text{RSRP}(i, t)$. Predictor $f_\theta$:

$$\hat{\theta} = \arg\min_\theta \mathbb{E}_{t, \mathbf{o}}\big[\text{CE}(b^*_t, f_\theta(\mathbf{o}_t))\big]$$

With temporal context (beam *tracking*):

$$\hat{b}_{t+\Delta} = f_\theta(\mathbf{o}_t, \mathbf{o}_{t-1}, \ldots)$$

## Why it matters / when you use it

- **mmWave deployment is beam-bound.** Every $60$ GHz / FR2 system spends real overhead on beam management; cheap prediction directly improves throughput.
- **Task that frames multi-modal fusion.** Good exercise for learning fusion (concat, attention, Perceiver IO) on structured PHY inputs.
- **Career signal.** DeepSense Challenges appear on current Wi-Lab student CVs — a top-5 finish is a measurable credential.

## Common mistakes

- **Training on balanced data when the real distribution is skewed.** Beam indices are not uniform in real traffic. Report per-beam accuracy.
- **Claiming data-rate gain without a baseline.** Always compare to RSRP-sweep (oracle) and random (lower bound).
- **Confusing top-1 "accuracy" with "correct RSRP within $\varepsilon$." The DBA-Score exists for this reason — use it.

## Research ties

- **Key papers:** Charan et al. 2022 (arxiv:2209.07519); Jiang & Alkhateeb 2022 vision tracking; Demirhan 2026 radar; Jiang 2023 twin-based (arxiv:2301.07682).
- **Dataset:** [[deepsense-6g]].
- **People:** [[alkhateeb]], Gouranga Charan (2024 PhD), Shuaifeng Jiang (Bosch), Umut Demirhan (DeepMIMO maintainer).

## Portfolio move (Phase 3 Month 9)
DeepSense scenario 31 beam predictor:
1. Baseline: GPS-only MLP.
2. $+$ RGB (pretrained ResNet-50).
3. Multi-modal fusion (concat $+$ 2-layer MLP).
4. Report top-1, top-5, DBA-Score.
5. Stretch: fine-tune on scenario 32 for generalization.

## Related
- [[deepsense-6g]]
- [[mmwave-mimo]]
- [[wireless-digital-twin]] — twin-generated GT
- [[physical-layer-ml]]
- [[alkhateeb]]
- [[python-ml-wireless]]

## Practice
- Phase 3 M9 DeepSense scenario 31.
