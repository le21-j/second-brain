---
title: "Morais, Charan, Srinivas, Alkhateeb 2024 — DeepSense-V2V: A Vehicle-to-Vehicle Multi-Modal Sensing, Localization, and Communications Dataset"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/deepsense-v2v-2024.pdf
source_date: 2024-06-25
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - dataset
  - v2v
  - mmwave
  - multi-modal
  - deepsense
  - alkhateeb
  - morais
  - asu-wi-lab
created: 2026-05-01
updated: 2026-05-01
---

# Morais, Charan, Srinivas, Alkhateeb 2024 — DeepSense-V2V

**Authors:** João Morais, Gouranga Charan, Nikhil Srinivas, Ahmed Alkhateeb (Wi-Lab @ ASU). **arxiv:2406.17908** (Jun 2024). Mirrored at `raw/articles/ml-phy/pdfs/deepsense-v2v-2024.pdf`.

## TL;DR
**The first large-scale multi-modal dataset for mmWave vehicle-to-vehicle (V2V) communications.** A two-vehicle testbed with **360° camera + 4 radars + 4× 60-GHz phased arrays + 3D LiDAR + 2 precise GPSs** drove **120 km day + night across intercity and rural settings, up to 100 km/hr**. **More than 1 million detected objects.** Anchors the V2V branch of the DeepSense 6G family.

## Key contributions

1. **Two-vehicle synchronized sensor stack** — 360° camera, 4 radars, **4 phased arrays at 60 GHz** (the V2V data plane), 3D LiDAR (32-channel), 2× RTK GPS.
2. **120 km of driving data** — day + night, intercity + rural, up to 100 km/hr — the only dataset capturing real high-mobility blockage at mmWave for V2V.
3. **Object-detection annotations** — >1M detected objects (cars, trucks, bicycles, pedestrians).
4. **Available via DeepSense-V2V hub.** Standard ML evaluation splits.

## Sensor + scenario summary

| Sensor | Spec | Purpose |
|---|---|---|
| 360° camera | 8K | situational awareness |
| 4 radars | 77 GHz FMCW | object tracking |
| 4 phased arrays | **60 GHz** | mmWave V2V comm |
| 3D LiDAR | 32-channel | precise object localization |
| 2 GPSs | RTK | sub-cm position |

## Why it matters / where it sits in the roadmap

- **Phase 3 M9 → Phase 4 M11 candidate task.** [[python-ml-wireless]] M11 lists "DeepSense Challenge" as a research-level capstone; V2V is one of the most active sub-tracks (DeepSense Multi-Modal V2V challenge 2023).
- **Where Wi-Lab's mmWave-MIMO pillar meets sensing-comm fusion.** The combination of [[mmwave-mimo]] sparsity + [[wireless-digital-twin]] integration + multi-modal sensing makes V2V the most-cited application of Wi-Lab's stack.
- **Morais authorship** — same researcher who later joined NVIDIA; **direct cold-email signal** ("João, I worked with the V2V dataset you released — particularly interested in the 60-GHz blockage challenge…").
- **Industry-integrated.** Vehicle-to-everything (V2X) is a major NVIDIA Drive Sim use case; DeepSense-V2V slots cleanly into that product.

## Concepts grounded
- [[deepsense-6g]] — the parent dataset family.
- [[mmwave-mimo]] — primary technology (60 GHz phased arrays).
- [[beam-prediction]] — natural task on this dataset.
- [[fading-channels]] — high-mobility / blockage propagation.

## Portfolio move (Phase 3 / Phase 4)
**Reproduce first.** Train a baseline beam-prediction CNN on DeepSense-V2V scenario subsets; compare against the published DBA-Score / top-K accuracy.

**Extend.** Apply LWM-Temporal (channel trajectory modeling) to V2V — channel evolution under 100 km/hr is exactly what LWM-Temporal targets ([[paper-lwm-temporal-2026]]).

> [!tip] Interviewer talking point (Wi-Lab)
> "I trained a baseline + LWM-Temporal-fine-tuned beam-prediction model on the V2V dataset; the trajectory model outperforms the per-snapshot baseline by Δ% top-1 accuracy at 80+ km/hr."

## Related
- [[python-ml-wireless]]
- [[paper-deepsense-6g-2023]] — parent dataset paper.
- [[paper-lwm-temporal-2026]] — natural fine-tuning target on this data.
- [[paper-digital-twin-vision-2023]] — V2V is a digital-twin use case.
- [[deepsense-6g]], [[beam-prediction]], [[mmwave-mimo]]
- [[morais]], [[alkhateeb]] — Wi-Lab team.
