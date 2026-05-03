---
title: "Alkhateeb et al. 2023 — DeepSense 6G: A Large-Scale Real-World Multi-Modal Sensing and Communication Dataset"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/deepsense-6g-2023.pdf
source_date: 2023
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - deepsense
  - alkhateeb
  - dataset
  - multi-modal
  - mmwave
  - foundational
created: 2026-05-01
updated: 2026-05-01
---

# Alkhateeb et al. 2023 — DeepSense 6G: A Large-Scale Real-World Multi-Modal Sensing and Communication Dataset

**Authors:** Ahmed Alkhateeb, Gouranga Charan, Tawfik Osman, Andrew Hredzak, João Morais, Umut Demirhan, Nikhil Srinivas (Wi-Lab @ ASU). **IEEE Communications Magazine 2023** / **arxiv:2211.09769**. Mirrored at `raw/articles/ml-phy/pdfs/deepsense-6g-2023.pdf`.

## TL;DR
**DeepSense 6G** is a **real-world** multi-modal mmWave + sensing dataset — the testbed counterpart to the ray-traced [[deepmimo]]. **1M+ synchronized samples** across 40+ scenarios with **mmWave (60 GHz phased array) + RGB/360° cameras + 32-channel LiDAR + 77 GHz FMCW radar + RTK GPS + sub-6 GHz channels**. The dataset that powers Wi-Lab's beam-prediction Challenge series. **Phase 3 Month 9 deliverable target.**

## Key contributions

1. **Synchronized multi-modal real-world data.** Most wireless-ML datasets are simulated (DeepMIMO) or single-modality (RadioML). DeepSense pairs all the sensors that **inform** beam direction (vision, LiDAR, radar, GPS) with the **mmWave channel that needs to be configured** — enabling sensing-aided beamforming research at the right realism level.
2. **40+ scenarios.** Indoor (lab corridor), outdoor (parking lot, street, V2V vehicles, drones, busy intersections). Mix of LoS / NLoS / blockage / mobility regimes.
3. **Open challenges.** Multi-Modal Beam Prediction 2022 (scenario 31 held-out), LiDAR-Aided 2023, Multi-Modal V2V 2023, etc. Challenge submissions appear on Wi-Lab admit profiles.
4. **DeepVerse 6G synthetic counterpart.** Digital-twin replica of DeepSense scenarios, generated from ray-tracing — pair real and synthetic for sim-to-real transfer studies.

## Methods

- **Hardware:** Mobile testbed (mmWave 60 GHz phased array IBM-built, multi-antenna sub-6 GHz, GoPro 360° cameras, Velodyne 32-ch LiDAR, Texas Instruments 77 GHz FMCW radar, Trimble RTK GPS). All time-synchronized via PTP.
- **Scenario authoring:** the team drives / walks / flies through environments while continuously recording.
- **Data layout:** per-sample dict with all modalities + metadata; HDF5 storage, PyTorch / TF dataloader provided.
- **Baselines:** Wi-Lab provides PyTorch reference implementations at https://github.com/DeepSense6G.

## Results

- **Sensing-aided beamforming.** Vision + position fusion outperforms position-only by ~10% top-1 accuracy in beam prediction.
- **Blockage prediction.** Camera + LiDAR predicts mmWave blockage with high accuracy at 0.5 s horizons.
- **V2V scenarios** demonstrate that vehicle motion + camera + sub-6 channel features can predict the V2V beam pair.

## Why it matters / where it sits in the roadmap

- **Phase 3 Month 9 deliverable** — "DeepSense 6G beam prediction (scenario 31, top-k acc, DBA-Score)" is the headline milestone. Build LSTM+MLP position baseline → add RGB ResNet branch → fuse → submit to leaderboard.
- **Wi-Lab strike zone.** A top-5 finish on a DeepSense Challenge appears on **every current Wi-Lab student's CV**. This is the single most direct application signal for the lab.
- **Sim-to-real honesty.** Pair DeepSense (real) with DeepMIMO (simulated) for the most credible PHY-ML papers.

## Concepts grounded

- [[deepsense-6g]] — primary concept page.
- [[beam-prediction]] — DeepSense is the canonical benchmark.
- [[deepmimo]] — synthetic counterpart.
- [[wireless-digital-twin]] — DeepVerse 6G is the digital-twin replica.

## Portfolio move (Phase 3 M9)

> Beam prediction on DeepSense 6G — pick scenario 31. Build LSTM+MLP position baseline, add RGB branch with pretrained ResNet, fuse features, compete on top-k accuracy and DBA-Score. Reference: Charan et al. arxiv:2209.07519 and the LiDAR baseline arxiv:2203.05548.

Steps:
1. Download scenario 31 via DeepSense API.
2. PyTorch Lightning + Hydra: position-only LSTM+MLP baseline.
3. Add RGB ResNet-18 (pretrained on ImageNet, frozen → fine-tuned).
4. Late-fusion (concat features → MLP head) or Perceiver IO cross-attention.
5. Eval on held-out test split: top-1, top-3, top-5 accuracy + DBA-Score.
6. Submit to leaderboard; write up as workshop paper.

## Questions raised
- **Generalization across cities.** DeepSense is largely Tempe / ASU campus — domain shift to other cities is a measured but addressable issue.
- **Sub-6 / mmWave joint operation** is provided but most submissions don't use it — opportunity for a credible novelty.

## Related
- [[python-ml-wireless]]
- [[deepsense-6g]]
- [[paper-deepmimo-2019]] — synthetic counterpart.
- [[beam-prediction]]
- [[alkhateeb]], [[morais]] — authors.
