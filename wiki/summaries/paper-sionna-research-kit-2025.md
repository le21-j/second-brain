---
title: "Cammerer, Marcus, Zirr, Aït Aoudia, Maggi, Hoydis, Keller 2025 — Sionna Research Kit: A GPU-Accelerated Research Platform for AI-RAN"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/sionna-research-kit-2025.pdf
source_date: 2025-05-19
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - sionna
  - sionna-research-kit
  - jetson
  - openairinterface
  - ai-ran
  - cammerer
  - hoydis
  - aitaoudia
  - nvidia
created: 2026-05-01
updated: 2026-05-01
---

# Cammerer et al. 2025 — Sionna Research Kit: A GPU-Accelerated Research Platform for AI-RAN

**Authors:** Sebastian Cammerer, Guillermo Marcus, Tobias Zirr, Fayçal Aït Aoudia, Lorenzo Maggi, Jakob Hoydis, Alexander Keller (NVIDIA). **arxiv:2505.15848** (May 2025). Mirrored at `raw/articles/ml-phy/pdfs/sionna-research-kit-2025.pdf`.

## TL;DR
**A real-time end-to-end AI-RAN testbed: NVIDIA Jetson AGX Orin + Sionna-trained neural receiver + TensorRT inference + USRP B210 + commercial 5G UE.** Bridges the gap between academic Sionna simulations and operational 5G NR systems. Open-source code release. **The hardware platform every Sionna-research career path runs through.**

## Key contributions

1. **Affordable AI-RAN testbed.** Jetson AGX Orin (~$2K) + USRP B210 + commercial Quectel 5G modem — within reach of a grad student. Replaces the need for expensive PXIe / FlexRAN setups.
2. **Real-time neural receiver demo.** A Sionna-trained NRX deployed via TensorRT in a 5G NR network with a real commercial UE — proves NRX latency budgets are achievable on Jetson.
3. **Built on OpenAirInterface (OAI).** O-RAN compliant. Software-defined PHY/MAC/RLC stack — researchers can replace any block with a learned variant.
4. **Inline vs. look-aside acceleration.** Paper distinguishes the two GPU-acceleration paradigms in detail; argues inline (Jetson Orin) is preferred for AI-RAN over look-aside (PCIe ASIC).
5. **Open-source release.** Code examples published — re-deployable end-to-end.

## Methods
- **Hardware:** Jetson AGX Orin (275 TOPS), USRP B210 (10–100 MHz instantaneous BW), commercial 5G NR UE (Quectel RM520N-GL).
- **Software:** OpenAirInterface gNB stack + custom CUDA blocks for the neural receiver inference path.
- **Inference:** Sionna trains TF model → TensorRT compiles → Jetson runs at NR slot timing (~1 ms).

## Why it matters / where it sits in the roadmap

- **Phase 4 M10–M11 hardware deliverable possibility.** [[python-ml-wireless]] M11 has "substantive Sionna PR" as one of three research-level capstone options — a Sionna Research Kit reproduction is the natural fit.
- **Bridges Phase-1 AirComp Pluto work to Phase 4 NVIDIA work.** Jayden's [[system-pipeline]] AirComp build experience translates directly: USRP / IIO / GPU offload — same problem space, different stack.
- **NVIDIA-intern signal.** The Research Kit is the **literal demonstration vehicle** an NVIDIA Aerial intern would deploy, profile, and extend. Familiarity is direct interview prep.
- **Cammerer + Hoydis + Aït Aoudia + Keller** are all on this paper — the entire Sionna trio plus the Mitsuba author. The most-NVIDIA-aligned paper in the entire list.

## Concepts grounded
- [[sionna]] — the simulator that produces the model deployed here.
- [[sionna-rt]] — RT module used for site-specific training.
- [[neural-receiver]] — the demonstrated AI-RAN application.
- [[nvidia-aodt]] — the productized cousin running the same stack.

## Portfolio move (Phase 4)

**Reproduce first, extend second.**

**Reproduce:** clone the Research Kit code; build Jetson + USRP B210 + commercial UE testbed; deploy the published NRX checkpoint; reproduce throughput / BLER claims.

**Extend:** swap the NRX block with a different architecture (e.g., a Transformer-based NRX from [[paper-nrx-cammerer-2023]] modification work); re-measure throughput / latency.

> [!tip] Interviewer talking point
> "I deployed the Sionna Research Kit demo on a Jetson Orin + USRP B210 testbed and benchmarked throughput; happy to share the writeup."

## Related
- [[python-ml-wireless]]
- [[paper-sionna-2022]] — the simulator stack.
- [[paper-nrx-cammerer-2023]], [[paper-nrx-wiesmayr-2024]] — the deployed NRX line.
- [[hoydis]], [[cammerer]], [[aitaoudia]] — full NVIDIA Sionna team.
