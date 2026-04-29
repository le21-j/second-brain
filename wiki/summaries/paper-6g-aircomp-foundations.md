---
title: Over-the-Air Computation for 6G — Foundations, Technologies, and Applications (Wang et al. 2022)
type: summary
source_type: article
source_path: raw/articles/6g-research/aircomp-6g-foundations.pdf
source_date: 2022
course: [[research]]
tags: [aircomp, 6g, survey, multiple-antennas, foundations]
created: 2026-04-21
updated: 2026-04-26
---

# 6G AirComp — Foundations, Technologies, Applications

**Authors:** Wang, Zhao, Zhou, Shi, Jiang, Letaief. arXiv:2210.10524. Released one day after the Şahin & Yang survey (already ingested as `paper-aircomp-survey.md`).

## TL;DR
Complementary survey to [[paper-aircomp-survey]] — focuses on **MIMO-based AirComp** and **6G network architectures** (multi-cell, RIS, UAV, hierarchical). Less detail on synchronization/coding than Şahin & Yang, more on beamforming and cross-layer co-design. Referenced as the "Wang et al. 6G foundations" survey in most recent AirComp papers.

## Key additions vs Şahin & Yang

- **MIMO beamforming** as the dominant design lever in 6G (vs single-antenna pre-equalization in classical AirComp). ZF, MMSE, MRT at receiver; beamforming vector optimization at transmitter.
- **Multi-cell + RIS + UAV** architectures treated in depth.
- **Cross-layer co-design** — joint optimization of power control, resource allocation, RIS phase shifts, and ML hyperparameters.
- **Privacy + security** via channel superposition — extended discussion including semantic privacy.

## Not-covered
- Little on synchronization signal design (Şahin & Yang is better here).
- Light on PPDU / frame structure (refer to 5G NR or the demo papers).

## Use
Treat as a **companion** to [[paper-aircomp-survey]] for MIMO-specific questions. For signal-design specifics (sync, pilots, coding), prefer [[paper-aircomp-feel-demo]] + [[paper-experimental-ota-fl]].

## Related
- [[paper-aircomp-survey]]
- [[paper-rethinking-edge-ai-spm]]
