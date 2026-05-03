---
title: "PySDR — Marc Lichtman (HTML reference, free)"
type: summary
source_type: other
source_path: raw/textbook/pysdr-lichtman.md
source_date: 2024
course:
  - "[[python-ml-wireless]]"
tags:
  - textbook
  - sdr
  - dsp
  - wireless
  - lichtman
  - phase-1
  - phase-3
  - reference-card-stub
created: 2026-05-01
updated: 2026-05-01
---

# PySDR — A Guide to SDR and DSP using Python (Marc Lichtman)

**Status:** stub — full summary pending. The book is HTML-only (no PDF mirrored). Reference card lives at `raw/textbook/pysdr-lichtman.md`. Hub: https://pysdr.org/.

## TL;DR
**The single most wireless-relevant free resource on the roadmap.** Sits exactly at the Python + DSP + wireless intersection. **Chapter 12 (OFDM)** is the foundation for the Phase 1 M2 OFDM-from-scratch project; **Chapter 16 (ML for RF)** is the gentle on-ramp to the O'Shea/Hoydis literature.

## Where it's used in the roadmap
- **Phase 1 M2** — Ch 1–4 (SDR + frequency-domain + IQ + digital modulation) groundwork.
- **Phase 1 M2 deliverable** — Ch 12 OFDM is the build target for the OFDM-from-scratch notebook.
- **Phase 3 M7+** — Ch 16 ML for RF as bridge to neural-receiver literature.
- **AirComp pipeline cross-pollination** — Ch 5 (PlutoSDR in Python) directly applies to Jayden's existing 4× Pluto AirComp build at [[system-pipeline]].

## Chapters that matter most

| Ch | Topic | Roadmap relevance |
|---|---|---|
| 2 | FFT / frequency domain | Reinforces [[dft]], [[fft]] from [[eee-404]] |
| 3 | IQ sampling | Foundation for any SDR work |
| 4 | Digital modulation (BPSK/QPSK/QAM) | [[qam-modulation]] reinforcement |
| 5 | PlutoSDR in Python | Direct application to [[system-pipeline]] |
| 8 | Filters | [[matched-filter]], FIR/IIR |
| 12 | **OFDM** | **Phase 1 M2 deliverable backbone** |
| 14 | Synchronization | Frame/timing sync — relevant to [[golay-sequence-sync]] |
| 16 | ML for RF | On-ramp to [[modulation-classification]], [[neural-receiver]] |

## Concepts grounded
- [[ofdm]] — primary
- [[qam-modulation]], [[matched-filter]]
- [[modulation-classification]] (Ch 16 introduction)

## Related
- [[python-ml-wireless]]
- [[lichtman]] — author
- [[paper-radioml-oshea-2018]] — natural follow-on for Ch 16 ML-for-RF concepts
- [[system-pipeline]] — Pluto-specific chapter applies directly
