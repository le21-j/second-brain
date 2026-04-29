---
title: Industrial Viewpoints on RAN Technologies for 6G (2025)
type: summary
source_type: article
source_path: raw/articles/6g-research/industrial-viewpoints-6g-ran.pdf
source_date: 2025-08
course: [[research]]
tags: [6g, ran, industry, ericsson, 3gpp-release-20, ssb]
created: 2026-04-21
updated: 2026-04-26
---

# Industrial Viewpoints on RAN Technologies for 6G

**arXiv:** 2508.08225 (Aug 2025). Joint industry perspective (Ericsson, Nokia, Huawei contributors).

## TL;DR
Industry consensus on 6G RAN direction: **separate idle-mode and connected-mode signals** (major change from 5G NR where both depend on SSB). 6G SSB can be hidden in reserved 5G resources for forward compatibility. AI-native signal design is assumed.

## Key signal-design findings relevant to the pipeline

1. **6G SSB will be distinct from 5G SSB**, placed in unoccupied 5G SSB positions or hidden via reserved-resource mechanism. This means Jayden's beacon design doesn't need to conform to 5G SSB exactly; can be cleanly 6G-native.
2. **Connected-mode vs idle-mode separation** — nodes used only for data transmission don't transmit idle-mode signals and can power down. Maps naturally to Jayden's ES: it can sleep between epochs since EDs only need beacons when an AirComp round is scheduled.
3. **Feedback channel redesign** — 6G will probably move control feedback from PUCCH/UCI-on-PUSCH to MAC Control Elements (MAC-CEs). Lower overhead, more flexible. Jayden's Stage 6 feedback fits this direction naturally.
4. **AI-for-PHY is assumed default** — receiver-side decoders, channel estimators, and CSI compressors will be ML-based by 2030.

## Use
Architecture-level reference for how 6G thinks about idle / connected / feedback signals. For actual numerology/coding specifics, wait for 3GPP Release 20/21 (expected 2025-2027).

## Related
- [[paper-itu-r-m2516]]
- [[signal-design-gaps]]
