---
title: Reconfigurable Intelligent Surface (RIS)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - 6g
  - mmwave
  - metasurface
  - phase-4
sources:
  - "[[paper-osman-ris-oran-2025]]"
created: 2026-05-01
updated: 2026-05-01
---

# Reconfigurable Intelligent Surface (RIS)

## In one line
**A RIS is a planar array of subwavelength tunable scattering elements that can electronically steer a reflected wavefront — a "smart mirror" for radio waves, used to extend mmWave coverage around blockages.** One of the four 6G technology pillars (with mmWave-MIMO, sensing-comm fusion, AI-RAN).

## Example first

**1024-element 1-bit RIS at 28 GHz** ([[paper-osman-ris-oran-2025]]). 32×32 metasurface, each cell has a PIN diode that switches between two phase states (0 / π). A microcontroller biases the diodes per cell.

When the BS-UE direct path is blocked, the RIS provides a **virtual line-of-sight** by reflecting toward the UE. Field results: **9–20 dB indoor / 6–18 dB outdoor** signal-power gain.

Crucially, RIS is **passive** (no RF amplifier per cell) — much cheaper than a relay, and the control plane piggybacks on existing 5G O-RAN signaling.

## The idea

A RIS controls **(phase, amplitude, polarization)** of reflected waves at each element via tunable components (PIN diodes, varactors, MEMS, liquid crystal). Each element is subwavelength ($\sim \lambda/2$ or smaller). With $N$ elements, you can engineer arbitrary phase profiles — synthesizing beams, focusing on near-field hot spots, splitting into multiple users.

Not the same as a phased array (which transmits) — a RIS only **redirects incident** waves.

## Where it sits in the roadmap
- **Phase 4 M12 reading** — [[paper-osman-ris-oran-2025]] is the MILCOM 2025 Best Demo paper from Wi-Lab.
- **6G context.** RIS is the standard candidate for "additional degree of freedom" in 6G coverage planning.

## Common mistakes
- **Confusing 1-bit / 2-bit / continuous-phase RIS.** 1-bit ≈ 4 dB worse than continuous; 2-bit covers most of the gap.
- **Treating RIS as a relay.** Relays amplify; RIS does not. Path loss is **product** of two segments (TX→RIS and RIS→RX), not sum — the **squared** path-loss penalty is a real hardware constraint.

## Related
- [[mmwave-mimo]] — RIS extends mmWave coverage.
- [[paper-osman-ris-oran-2025]] — Wi-Lab hardware demo.
- [[o-ran]] — RIS deployments use O-RAN's E2 control interface.
- [[wireless-digital-twin]] — RIS placement is a digital-twin optimization use case.
- [[python-ml-wireless]]
