---
title: ITU-R M.2516 — Future Technology Trends of IMT Systems Towards 2030 and Beyond
type: summary
source_type: article
source_path: raw/articles/6g-research/itu-r-m2516-imt2030.pdf
source_date: 2022-11
course:
  - "[[research]]"
tags: [itu, imt-2030, 6g, standardization, reference-signal]
created: 2026-04-21
updated: 2026-05-06
---

# ITU-R M.2516-0 — IMT-2030 (6G) Framework

**Publisher:** ITU-R Working Party 5D. November 2022. The foundational 6G framework document — 59 contributions from industry + governments worldwide. Jayden's HPSR paper and most AirComp/6G research cite this as the standard reference.

## TL;DR
The definitive 6G technology trends report. Establishes the **AI-native air interface** direction, integrated sensing + communication + computation (ISCC) as a unifying paradigm, and calls out AirComp-style aggregation as one of the key enablers for massive-device intelligence. Doesn't specify signal designs (that's 3GPP's job in Release 20/21) but sets the architectural priorities that signal-design research aims at.

## Key directions relevant to Jayden's pipeline

1. **AI-native new air interface** — reference signals and pilots should be designed not just for channel estimation but also to support downstream AI tasks (e.g., OTA federated learning). Implicit: traditional CRS/DMRS/CSI-RS may evolve into combined pilots that serve ML+comm jointly.
2. **ISCC (integrated sensing, communication, computation)** — AirComp is positioned as a central technology in this convergence. Jayden's pipeline falls squarely in this bucket.
3. **Sub-THz + extreme MIMO + RIS** — numerologies and pilot densities will need to adapt to much wider bandwidths (e.g., 1 GHz at 140 GHz). Jayden's current 5G-based template may need revisiting for 6G targets.
4. **Interconnection of terrestrial + non-terrestrial networks** — pipeline's ES could be a satellite or UAV; beacon/feedback frame must tolerate much larger propagation delays.
5. **Enhanced trustworthiness** — AirComp's implicit privacy through superposition is a listed advantage. But requires robust authentication + key management — layer Jayden's pipeline currently doesn't specify.

## Standardization timeline
- **ITU-R WP5D M.2516:** Nov 2022 (foundational)
- **3GPP Release 20:** 6G Study Item phase, begins **fall 2025**.
- **3GPP Release 21:** 6G Work Item phase.

As of April 2026, we are in early Release 20 study-item activity. No 6G-specific spec for beacon/sync/reference signals yet published.

## Why this matters for Jayden's pipeline
Jayden's pipeline should be compatible with the **direction** ITU-R has set:
- ✅ AirComp-based aggregation — matches ISCC priority.
- ✅ Distributed decision-making — matches AI-native direction (compute at the edge, not full CSI at server).
- ⚠️ 5G NR numerology baseline — fine for prototyping but 6G will introduce new numerologies (larger subcarrier spacings for higher bands).
- ⚠️ Centralized ES — may need hierarchical or non-terrestrial-aware variants.

## Related
- [[paper-rethinking-edge-ai-spm]]
- [[signal-design-gaps]]
