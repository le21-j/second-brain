---
title: Jakob Hoydis
type: person
tags: [nvidia, sionna, wireless-ml, neural-receiver, target-researcher]
course:
  - "[[python-ml-wireless]]"
created: 2026-04-23
updated: 2026-05-06
---

# Jakob Hoydis

**Affiliation:** Distinguished Research Scientist, NVIDIA Research (Munich)
**Role:** Wireless ML research lead; co-maintainer of [[sionna]]
**Profile:** https://research.nvidia.com/person/jakob-hoydis
**LinkedIn:** https://www.linkedin.com/in/jhoydis/
**PhD:** Supélec / LSS; wireless signal processing / massive MIMO

## Why he matters to Jayden

**Primary NVIDIA target researcher.** Co-author of the **seminal PHY-ML paper** (O'Shea-Hoydis 2017) and leads the research group behind Sionna. Cold-emailable *after* a Sionna project is on GitHub.

## Canonical papers (read in order)

1. **O'Shea & Hoydis 2017** — "An Introduction to Deep Learning for the Physical Layer," IEEE TCCN (arxiv:1702.00832). The paper that started the field. See [[autoencoder-phy]].
2. **Dörner, Cammerer, Hoydis, ten Brink 2018** — "DL-Based Communication over the Air," IEEE JSTSP (arxiv:1707.03384). First fully-NN SDR.
3. **Aït Aoudia & Hoydis 2019** — "Model-Free Training of End-to-End Communication Systems," IEEE JSAC (arxiv:1812.05929). Model-free E2E learning.
4. **Hoydis, Cammerer, Aït Aoudia et al. 2022** — [[sionna]] (arxiv:2203.11854). The framework paper.
5. **Hoydis et al. 2023** — "Sionna RT: Differentiable Ray Tracing" (arxiv:2303.11103). See [[differentiable-ray-tracing]].
6. **Cammerer, Aït Aoudia, Hoydis et al. 2023** — "A Neural Receiver for 5G NR Multi-user MIMO" (arxiv:2312.02601). See [[neural-receiver]].
7. **Wiesmayr, Cammerer, Aït Aoudia, Hoydis et al. 2024** — Standard-compliant 5G NR NRX (arxiv:2409.02912). Real-time on GPU baseband.
8. **Hoydis et al. 2024** — "Learning Radio Environments by Differentiable Ray Tracing," IEEE TMLCN (https://github.com/NVlabs/diff-rt-calibration). Digital-twin calibration.

## NVIDIA group

Collaborators at NVIDIA Research Munich:
- **Sebastian Cammerer** — Sionna co-maintainer, co-author on most of the above.
- **Fayçal Aït Aoudia** — Sionna co-maintainer, RT lead.
- **Reinhard Wiesmayr** — NRX, SALAD.
- **Alexander Keller** — Senior Director of Research, Mitsuba / Dr.Jit lineage.
- **Lorenzo Maggi, Guillermo Marcus, Merlin Nimier-David, Tobias Zirr** — various RT/systems roles.
- **João Morais** — Wi-Lab alum, now on the team. See [[morais]].

## On social

Primarily **LinkedIn** (not X/Twitter). LinkedIn posts often include Sionna release notes and research-code announcements. Follow on GitHub too (`@jhoydis`).

## How to approach

Per the roadmap's Phase 4 guidance: once your portfolio has real content (one Sionna-based project merged or demonstrably live), send a concise pitch naming a specific 2024–2025 paper of his and proposing a concrete extension. **Do not email without a Sionna project on GitHub.**

Examples of pitch hooks:
- "I have a reproduction of the standard-compliant NRX and a proposed site-specific pretraining experiment in custom OSM scenes."
- "I built a Sionna tutorial on [specific thing the gallery lacks]; happy to PR it."
- "I'd like to extend SALAD to [a specific link-adaptation extension]."

NVIDIA Research operates on a **sponsor model** — a specific researcher must want you on their project. Cold emails that name the project and the extension have the highest response rate.

## Related
- [[sionna]]
- [[neural-receiver]]
- [[autoencoder-phy]]
- [[differentiable-ray-tracing]]
- [[oshea]] — co-author on the seminal paper.
- [[morais]] — bridge from Wi-Lab.
- [[python-ml-wireless]]
