---
title: O-RAN (Open RAN)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - 5g
  - 6g
  - oran
  - architecture
  - phase-3
  - phase-4
sources:
  - "[[paper-osman-ris-oran-2025]]"
  - "[[paper-sionna-research-kit-2025]]"
created: 2026-05-01
updated: 2026-05-01
---

# O-RAN (Open RAN)

## In one line
**O-RAN is an industry-standard architecture that decomposes the 5G/6G base station into open, multi-vendor, software-defined components with standardized interfaces — and exposes ML-friendly hooks ("xApps") for per-slot intelligent control.**

## Example first

A 5G gNB in O-RAN is split into:
- **O-DU** (Distributed Unit) — handles PHY/MAC.
- **O-CU** (Centralized Unit) — RLC/PDCP/RRC.
- **Near-RT RIC** (Real-Time Intelligent Controller) — runs **xApps** that act on 10ms–1s decisions.
- **Non-RT RIC** — runs **rApps** that act on >1s decisions.
- **E2 interface** connects RIC to O-DU/O-CU.

A real-world example: [[paper-osman-ris-oran-2025]] uses an **xApp on the Near-RT RIC** to issue RIS-configuration commands via E2, without modifying any 3GPP-standard signaling.

## The idea

Traditional cellular vendors (Ericsson, Nokia) ship monolithic gNB stacks. O-RAN is the **counter-bet**: open, standard interfaces let operators mix vendors and inject ML / openness / customization.

For ML: the RIC layers are explicitly designed for AI/ML deployment. Train models offline → deploy as rApps/xApps → act on standardized observations.

## Why it matters / where it sits in the roadmap

- **Phase 3 M7+ context.** Sionna Research Kit ([[paper-sionna-research-kit-2025]]) is built on **OpenAirInterface (OAI)**, the canonical O-RAN-compliant open-source 5G stack.
- **Phase 4 M12 reading.** [[paper-osman-ris-oran-2025]] uses E2 interface; understanding O-RAN's structure is mandatory.
- **Where ML "fits" in 5G/6G.** xApps + rApps are the deployable surface for trained models. NRX, link adaptation, beam management — all natural xApps.

## Common mistakes
- **Confusing O-RAN with OAI.** O-RAN is the **standard**; OpenAirInterface is **one open-source implementation** of it. Like HTTP vs. nginx.
- **Confusing Near-RT-RIC vs Non-RT-RIC.** Near-RT is fast (10ms–1s); Non-RT is slow (>1s). Different deployment profiles.

## Related
- [[paper-sionna-research-kit-2025]] — uses OAI (O-RAN compliant).
- [[paper-osman-ris-oran-2025]] — uses E2 for RIS control.
- [[neural-receiver]], [[link-adaptation]] — natural xApp candidates.
- [[python-ml-wireless]]
