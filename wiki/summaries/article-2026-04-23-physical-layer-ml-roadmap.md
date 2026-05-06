---
title: Physical-Layer ML Roadmap — 14 months to NVIDIA and Wi-Lab
type: summary
source_type: other
source_path: raw/other/python learning roadmap.md
source_date: 2026-04-23
course:
  - "[[python-ml-wireless]]"
tags: [roadmap, curriculum, sionna, deepmimo, nvidia, wi-lab, ml, wireless]
created: 2026-04-23
updated: 2026-05-06
---

# Physical-Layer ML Roadmap — 14 months to NVIDIA and Wi-Lab

**Source:** `raw/other/python learning roadmap.md` (Jayden's personal roadmap, April 2026).

## TL;DR
A 14-month plan (May 2026 → June 2027) for a junior aiming at **NVIDIA's Sionna team** (Hoydis / Cammerer / Aït Aoudia) and **Prof. Ahmed Alkhateeb's Wi-Lab at ASU**. Structured in five phases, each producing one shippable GitHub artifact. The organizing insight: these two labs are tightly coupled — DeepMIMO integrates directly with NVIDIA Sionna RT and the Aerial Omniverse Digital Twin, and João Morais (Alkhateeb PhD 2025) is now a Wireless SWE at NVIDIA — so **every hour spent on Sionna + DeepMIMO pays double**.

Target outcome by June 2027: 6 polished GitHub repos, 1–2 arXiv preprints, a Sionna PR merged, a DeepSense 6G Challenge submission, and a warm cold-email introduction to Alkhateeb before PhD applications open.

## Key takeaways

- **Three parallel tracks, every week, no exceptions:** structured coursework, a shipping project, paper reading. Never let one stall the others.
- **Canonical toolchain:** Python 3.11+, VS Code, JupyterLab, uv for envs, Git + GitHub, **PyTorch + Lightning** primary, TensorFlow/Keras working knowledge (for legacy Sionna 1.x), **Weights & Biases** for tracking, **Hydra** for configs, ruff + black + pre-commit, Google Colab / Kaggle for GPU.
- **Sionna and DeepMIMO are the two load-bearing frameworks.** Your Sionna neural-receiver tutorial reproduction (Month 7) and LWM extension (Month 11) are the two most important items in the document.
- **NVIDIA Research targets PhDs**, so the realistic intern target is a BS-level ML/SWE role (portal opens Aug–Oct 2026). Cold-email Hoydis/Cammerer/Aït Aoudia *after* a Sionna project is on GitHub.
- **Alkhateeb explicitly invites cold email.** Window: late May to early September 2027. 150–200 words, name a specific paper, link to 4–6 concrete repos.
- **The portfolio is the application.** Every repo ships with README + results table + headline figure + Hydra configs + W&B report.

## Phase structure

- **Phase 1 (May–Jul 2026):** Python fundamentals, NumPy/SciPy, PyTorch fluency. Deliverables: OFDM-from-scratch notebook, CIFAR-10 ResNet.
- **Phase 2 (Aug–Oct 2026):** DL (CS231n Assignment 2), CNNs, transformers, TensorFlow crash-course, first PHY-ML reproduction (O'Shea-Hoydis 2017), RadioML modulation classification, CsiNet. **NVIDIA Summer 2027 applications open this window.**
- **Phase 3 (Nov 2026–Jan 2027):** Sionna tutorials end-to-end, first Sionna OSS PR, DeepMIMO installed, DeepSense 6G beam prediction, first Asilomar paper draft.
- **Phase 4 (Feb–Apr 2027):** Site-specific neural receiver, research-level project (LWM extension is the suggested anchor), arXiv preprint.
- **Phase 5 (May–Jun 2027):** Cold-email Alkhateeb; PhD school list finalized; SoP drafting; letter-writer outreach.

## Concepts introduced or reinforced

Mostly new to the vault. Summary of the big ones:

- [[sionna]] — NVIDIA's open-source link-level + ray-tracing simulator; PHY+SYS migrated to PyTorch in 2.x.
- [[deepmimo]] — Alkhateeb's ray-tracing-based channel dataset; v4 is a unified Python toolchain with convert() bridges to Sionna RT / Wireless InSite / NVIDIA AODT.
- [[deepsense-6g]] — multi-modal real-world testbed (mmWave + camera + LiDAR + radar + GPS).
- [[large-wireless-model]] — Wi-Lab's foundation model for wireless channels (masked channel modeling, 1M+ DeepMIMO channels, Hugging Face `wi-lab/lwm`).
- [[neural-receiver]] — NVIDIA's standard-compliant 5G NR neural receiver.
- [[autoencoder-phy]] — O'Shea & Hoydis 2017, the thread that started it all.
- [[csi-feedback]] — CsiNet and follow-ups for compressing massive-MIMO CSI.
- [[differentiable-ray-tracing]] — Sionna RT + differentiable wireless propagation.
- [[wireless-digital-twin]] — Alkhateeb's vision and build-out papers; the bridge between ray-traced training and deployment.
- [[physical-layer-ml]] — the umbrella concept tying the roadmap together.
- [[channel-charting]], [[modulation-classification]], [[beam-prediction]] — specific PHY-ML subtopics.

## Worked examples worth remembering

**Milestone projects from the ladder:**

1. *Level 1 — OFDM from scratch* — bits $\to$ QAM $\to$ IFFT $\to$ CP $\to$ AWGN $\to$ FFT $\to$ equalize $\to$ demap; BER vs $E_b/N_0$ validated against theory. One week. See [[ofdm-from-scratch-example]].
2. *Level 2 — O'Shea/Hoydis 2017 autoencoder* — $(n,k)$ autoencoder over AWGN, learned constellations, BLER against Hamming codes.
3. *Level 2 — RadioML modulation classification* — CNN/ResNet/Transformer comparison on RadioML 2016.10a, 2018.01A, per-SNR curves, CFO robustness.
4. *Level 2 — CsiNet reproduction* — compression ratios $1/4, 1/16, 1/32, 1/64$ on COST2100; swap in CRNet/CLNet.
5. *Level 3 — DeepSense 6G beam prediction* — scenario 31; LSTM+MLP position baseline; add RGB ResNet branch; fuse; top-$k$ accuracy + DBA-Score.
6. *Level 3 — Site-specific neural receiver in Sionna RT* — custom OSM scene; pretrain on 3GPP UMi; fine-tune per-BS; show BLER gain.
7. *Level 4 (capstone) — Reproduce & extend LWM* — fine-tune on a new DeepMIMO scenario for a new downstream task; baseline against from-scratch ResNet.

## Questions this source raised

- **Which NVIDIA internship posting is actually the right match?** The roadmap flags BS-level ML/SWE roles but doesn't name specific teams; will need to check postings when they open Aug–Oct 2026.
- **How does Jayden approach his letter writers?** The roadmap mentions "one wireless/DSP professor, one ML professor, one research mentor" but doesn't identify who. Worth a conversation — at least one will likely be from the AirComp project ([[system-pipeline]]).
- **Integration with ongoing AirComp work.** The roadmap runs in parallel with [[system-pipeline]] / [[regretful-learning]]. Some Phase 1–2 projects (OFDM from scratch, channel estimation) reinforce the AirComp research directly.

## Related
- [[python-ml-wireless]] — course page for this curriculum.
- [[system-pipeline]] — existing AirComp research thread (parallel track).
- [[alkhateeb]], [[hoydis]] — target advisors / researchers.
