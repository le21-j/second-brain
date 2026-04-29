---
title: DeepSense 6G
type: concept
course: [[python-ml-wireless]]
tags: [dataset, multi-modal, wi-lab, asu, sensing, mmwave, real-world]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# DeepSense 6G

## In one line
A **real-world** multi-modal sensing-and-communication dataset — Wi-Lab drove a testbed around Phoenix and collected 1M+ synchronized samples of mmWave beam power, RGB/$360^\circ$ video, LiDAR, radar, GPS, and sub-6 CSI, so you can train a model to predict the best mmWave beam from a camera frame.

## Example first

**The 2022 beam-prediction challenge task.** You're given:
- An RGB image from a dashcam.
- The user's GPS position.
- Sub-6 GHz CSI (cheap, omnidirectional).

You're asked to predict which of $64$ narrow $60$ GHz beams from the BS will give the best signal. Top-1 accuracy on scenario 31 (held-out test) for the winning entries in 2022 was around $70$–$80\%$, using a Vision Transformer $+$ position MLP fusion. Classical RSRP-based selection needs to sweep all $64$ beams and take $\sim 32\times$ more time; the ML model gets close to the oracle using a single RGB frame.

```python
# Illustrative — actual code uses the DeepSense6G baseline repo.
img = read_image("dashcam.jpg")            # 224x224x3
pos = read_gps_coords()                    # (lat, lon, alt, heading)
feat = vit(img) + pos_mlp(pos)             # fuse
logits = beam_head(feat)                   # 64 beams
best = logits.argmax()
```

## The idea

Alkhateeb et al. 2023 ([IEEE ComMag, arxiv:2211.09769](https://arxiv.org/abs/2211.09769)) argue that **sensing and communication will co-locate in 6G**: the same hardware that transmits will see the environment, and the same environment that the camera sees affects the channel. DeepSense 6G is the dataset that makes this concrete — every sample pairs channel measurements with sensor readings taken at the same instant.

### Sensors on the testbed

| Modality | Hardware |
| --- | --- |
| mmWave beam | **$60$ GHz phased array** (Sivers) — measures RSRP per beam across a $64$-beam codebook |
| RGB | forward dashcam (1080p) |
| $360^\circ$ | $360^\circ$ camera (both vehicle $+$ infrastructure units) |
| LiDAR | **$32$-channel spinning LiDAR** (Ouster) |
| Radar | **$77$ GHz FMCW radar** (Texas Instruments) |
| GPS | RTK GPS (cm-level) |
| Sub-6 | Sub-6 GHz channel estimates (complementary omni channel) |

### Scenarios & challenges

- **$40+$ scenarios** across urban, suburban, V2I, V2V, drone-UAV settings.
- **Scenario 31** — the held-out test for the 2022 Beam Prediction Challenge. Competitive top-1 $\sim 78\%$, DBA $\sim 0.85$.
- **Scenarios 32–34** — follow-on challenges.
- **2022 challenge:** Multi-Modal Beam Prediction.
- **2023 challenges:** LiDAR-Aided, Multi-Modal V2V.
- **DeepSense-V2V (arxiv:2406.17908, IEEE TVT 2025)** — Morais et al. V2V-specific task.

### Synthetic twin: DeepVerse 6G

https://deepverse6g.net/. A fully synthetic, ray-traced digital twin of the DeepSense testbed. Train in DeepVerse, fine-tune on DeepSense — cleaner sim-to-real transfer than any simulator-only approach.

### Official baselines

https://github.com/DeepSense6G — first-party baselines for every challenge, which you should beat before claiming a result.

## Formal definition (what "multi-modal beam prediction" is)

Given observations $o_t = (\text{img}_t, \text{lidar}_t, \text{radar}_t, \text{gps}_t, \text{sub6}_t)$ at time $t$, predict the next-best mmWave beam index:

$$
\hat b_{t+\Delta} = f_\theta(o_t, o_{t-1}, \ldots, o_{t-W})
$$

trained with cross-entropy against the ground-truth best-beam index from the mmWave codebook sweep. Success metrics: **top-$k$ accuracy** ($k=1, 3, 5$) and the **DBA-Score** (Distance-Based Accuracy — penalizes predictions far from the true beam, rewards near ones).

## Why it matters / when you use it

- **Real-world validation.** Simulator-only PHY-ML papers are suspect — DeepSense is the testbed you reach for when someone asks "does this work on real radios."
- **Sensing-comm co-design.** Every 6G roadmap (3GPP Rel-19/20, ITU-R IMT-2030) names ISAC as a pillar. DeepSense is the only open dataset that lets you do data-driven ISAC research right now.
- **Career lever.** Top-5 finish in a DeepSense Challenge shows up on current Wi-Lab PhD students' CVs. It's a recognized channel for "noticed by Alkhateeb."

## Common mistakes

- **Ignoring time alignment.** The sensors all have slightly different sample rates and latencies. Use the official synchronization tools; don't assume you can just `.iloc[idx]` your way through the data.
- **Testing on training scenarios.** The challenges define train/test scenarios separately on purpose. Using scenario-1 train to benchmark scenario-1 test is cheating.
- **Skipping the simpler baseline.** Before a Transformer $+$ multi-modal fusion, run a plain RSRP-sweep baseline. If you can't beat "try all $64$ beams," something is wrong.

## Research ties

- **Paper:** Alkhateeb et al. 2023 (arxiv:2211.09769).
- **Companion twin:** DeepVerse 6G (https://deepverse6g.net/).
- **Key follow-ups:** Charan et al. 2022 (arxiv:2209.07519), Demirhan 2026 (radar-aided), Jiang 2022 (vision-aided tracking), Morais 2024 (V2V).
- **Forum:** linked from challenge pages at https://www.deepsense6g.net/challenges/.

## Related
- [[deepmimo]] — synthetic companion (ray-traced, not real).
- [[beam-prediction]] — the task DeepSense is built around.
- [[wireless-digital-twin]] — DeepVerse is DeepSense's digital twin.
- [[alkhateeb]]
- [[python-ml-wireless]] — Phase 3 M9 deliverable.

## Practice
- Phase 3 M9 — beam prediction on scenario 31, LSTM$+$MLP $+$ RGB ResNet fusion.
- Phase 4 M11 — optional DeepSense Challenge submission.
