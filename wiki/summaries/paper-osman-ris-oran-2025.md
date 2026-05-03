---
title: "Osman, Shekhawat, Roy, Trichopoulos, Alkhateeb 2025 — RIS-Aided mmWave O-RAN: Coverage Extension and User Mobility Handling"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/osman-ris-oran-2025.pdf
source_date: 2025-10-23
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - ris
  - reconfigurable-intelligent-surface
  - mmwave
  - oran
  - 5g
  - 6g
  - alkhateeb
  - asu-wi-lab
  - milcom-best-demo
created: 2026-05-01
updated: 2026-05-01
---

# Osman, Shekhawat, Roy, Trichopoulos, Alkhateeb 2025 — RIS-Aided mmWave O-RAN

**Authors:** Tawfik Osman, Aditya Shekhawat (co-equal first authors), Abhradeep Roy, Georgios Trichopoulos, Ahmed Alkhateeb (Wi-Lab @ ASU). **arxiv:2510.20088** (Oct 2025). **MILCOM 2025 Best Demo Award.** Mirrored at `raw/articles/ml-phy/pdfs/osman-ris-oran-2025.pdf`.

## TL;DR
**End-to-end design + field deployment of a 1024-element 1-bit Reconfigurable Intelligent Surface (RIS) at 28 GHz integrated into a 5G O-RAN system.** Extensive indoor + outdoor field trials show **9–20 dB indoor and 6–18 dB outdoor signal-power gains** from RIS deployment. Two **UE-mobility management algorithms** developed for joint RIS + UE beam tracking. **The MILCOM 2025 Best Demo paper for Wi-Lab.**

## Key contributions

1. **1024-element (32×32) 1-bit RIS at 28 GHz** with modular tiled architecture (4 tiles × 256 elements).
2. **O-RAN E2 interface integration** — RIS reconfiguration via the standard O-RAN control plane, no modifications to 5G signaling.
3. **Field trial validation:**
   - **Indoor:** 9–20 dB received-power gain.
   - **Outdoor:** 6–18 dB received-power gain.
4. **Two mobility-management algorithms** for joint RIS + UE beam tracking — track the user as they move, jointly steering the RIS and the UE beam.
5. **Real-time evaluation on the testbed.**

## Methods
- **Hardware:** 32×32 metasurface @ 28 GHz; 1-bit phase quantization; PIN-diode switch per cell; tiled modular design.
- **5G integration:** O-RAN architecture; RIS controller exposed as a "near-RT RIC xApp"; commands routed via E2 interface.
- **Field trial methodology:** received-signal-strength measurements at varying user positions; LoS blocked → RIS provides virtual-LoS path.

## Results
- **Indoor:** 9–20 dB average gain across deployment scenarios.
- **Outdoor:** 6–18 dB gain.
- **Mobility tracking:** the joint-beam algorithm sustains link as user moves in real-time.

## Why it matters / where it sits in the roadmap

- **The Wi-Lab "everything works in the real world" exemplar.** A demo paper with a Best Demo award + real RIS hardware. Demonstrates Alkhateeb's group ships hardware, not just papers.
- **Phase 4 M12 reading.** [[python-ml-wireless]] M12 explicitly lists "Osman RIS-O-RAN" as 2025 Wi-Lab reading.
- **6G research vocabulary.** RIS is one of the four 6G technology pillars (with mmWave-MIMO, sensing-comm fusion, AI-RAN). Knowing the practical state of RIS is necessary background for the cold email.
- **Cross-link to NVIDIA AODT.** RIS deployment optimization is a digital-twin use case — Sionna RT can simulate RIS reflections; AODT can model the deployment.

## Concepts grounded
- [[ris]] — the core technology *(stub TBD — Tier 3)*.
- [[mmwave-mimo]] — RIS extends mmWave coverage in NLoS.
- [[o-ran]] *(stub TBD — Tier 3)* — the standard whose E2 interface is leveraged for RIS control.

## Portfolio move (Phase 4)
**Reproduce first (sim).** Implement an RIS-assisted mmWave channel in Sionna RT; reproduce the 9–20 dB indoor signal-power-gain claim under matched scenario.

**Extend.** Apply ML to RIS phase optimization: train a CNN to map (UE position, blockage state) → (RIS phase configuration). Compare to the paper's algorithm.

> [!tip] Interviewer talking point (Wi-Lab)
> "I reproduced the Osman 2025 RIS-O-RAN gain in Sionna RT and tested an ML-driven RIS phase optimizer; 1.5 dB additional gain over your Algorithm 2."

## Related
- [[python-ml-wireless]]
- [[mmwave-mimo]]
- [[wireless-digital-twin]] — RIS-assisted networks are a digital-twin showpiece.
- [[paper-digital-twin-vision-2023]]
- [[alkhateeb]] — group lead.
