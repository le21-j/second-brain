---
title: Physical-Layer ML Roadmap
type: course
tags: [roadmap, curriculum, ml, wireless, sionna, deepmimo, nvidia, wi-lab]
created: 2026-04-23
updated: 2026-04-23
---

# Physical-Layer ML Roadmap — 14 months to NVIDIA + Wi-Lab

This is a **meta-course**, not a class: a personal 14-month curriculum (May 2026 → June 2027) designed to carry Jayden from "junior with a DSP background" to "credible candidate for NVIDIA Summer 2027 intern + Wi-Lab Fall 2028 PhD." Source document: [[article-2026-04-23-physical-layer-ml-roadmap]] (see that page for full provenance).

## Overview

Two target labs: **NVIDIA's Sionna team** (Jakob Hoydis, Sebastian Cammerer, Fayçal Aït Aoudia — link-level simulation, neural receivers, differentiable ray tracing) and **Prof. Ahmed Alkhateeb's Wireless Intelligence Lab at ASU** (DeepMIMO, DeepSense 6G, Large Wireless Model, digital twins). They are the two most tightly coupled research programs in physical-layer ML: DeepMIMO integrates directly with NVIDIA Sionna RT and the Aerial Omniverse Digital Twin, and a former Wi-Lab PhD (João Morais) is now at NVIDIA.

Organizing rule: three parallel tracks every week — **(1) structured coursework, (2) a shipping project, (3) paper reading** ($\geq 1$ paper summary per week). If any one stalls, pause the others; never skip the artifact.

## Canonical toolchain

| Category | Tool |
| --- | --- |
| Python | 3.11+ |
| Editor | VS Code or Cursor |
| Notebooks | JupyterLab |
| Env mgmt | **uv** (primary), conda (when CUDA bundling needed) |
| DL framework | **PyTorch + Lightning** (primary), TensorFlow/Keras (working knowledge for Sionna 1.x) |
| Experiment tracking | **Weights & Biases** |
| Config | **Hydra** |
| Code quality | ruff + black + pre-commit; mypy optional |
| GPU | Google Colab / Kaggle / local |
| Template | **[Lightning-Hydra-Template](https://github.com/ashleve/lightning-hydra-template)** |

## Roadmap — 5 phases

### Phase 1 — Foundations (May–Jul 2026)

Python fluency + scientific Python + PyTorch.

| Month | Primary study | Project deliverable |
| --- | --- | --- |
| May (M1) | CS50P (compressed); Andrew Ng ML Course 1; 3Blue1Brown playlists | `learning-log` repo, Kaggle Titanic submission |
| Jun (M2) | NumPy deep-dive ([[from-python-to-numpy]], 100 exercises); scipy.signal; [[pysdr-lichtman]] Ch 1–4; Ng ML Courses 2–3 | **OFDM-from-scratch notebook** — BER vs Eb/N0 vs theory |
| Jul (M3) | [[deep-learning-with-pytorch]] Ch 1–8; [Karpathy Zero-to-Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ); Ng DL Courses 1–2 | **CIFAR-10 ResNet-18 with AMP, W&B-logged** |

### Phase 2 — Deep learning + first wireless-ML projects (Aug–Oct 2026)

| Month | Primary study | Project deliverable |
| --- | --- | --- |
| Aug (M4) | Ng DL Courses 3–4 (CNNs); CS231n Assignment 2 (**full**); [[prince-understanding-deep-learning]] Ch 1–11 | **Reproduce O'Shea-Hoydis 2017 autoencoder** — BLER curves. **NVIDIA intern postings begin — monitor weekly.** |
| Sep (M5) | Ng DL Course 5; CS224N Lectures 5–7; transformers week (Illustrated → Karpathy → "Attention Is All You Need" → Prince Ch 12) | **Reproduce RadioML modulation classification** — CNN + ResNet + Transformer. **Submit early NVIDIA BS-level intern applications.** |
| Oct (M6) | TensorFlow/Keras crash course (25–35 h); [[deep-learning-with-python-chollet]] Ch 3, 7, 9; generative models (Prince Ch 14–15; Kingma VAE; Lilian Weng) | **Reproduce CsiNet + CRNet + CLNet** — compression ratios 1/4, 1/16, 1/32, 1/64. First Lightning+Hydra refactor. |

### Phase 3 — Physical-layer ML specialization (Nov 2026–Jan 2027)

| Month | Primary study | Project deliverable |
| --- | --- | --- |
| Nov (M7) | [[sionna]] tutorials Parts 1–4 on GPU; Sionna white paper; CS224W (GNNs); [[sutton-barto-rl]] Ch 1–8; David Silver lectures 1–7 | **Modified Sionna neural receiver** — Transformer block swap + blog writeup |
| Dec (M8) | HF Deep RL Units 1–4; Spinning Up VPG→PPO; read DeepMIMO (arxiv:1902.06435) and DeepSense 6G (arxiv:2211.09769) in full | **First Sionna OSS PR merged** (even tiny); DeepMIMO v4 working locally |
| Jan (M9) | Read LWM paper (arxiv:2411.08872) + digital-twin vision (arxiv:2301.11283); Asilomar 2027 paper draft begins | **DeepSense 6G beam prediction** (scenario 31, top-k acc, DBA-Score); **DeepMIMO channel est (CNN/U-Net)** |

### Phase 4 — Advanced projects + original research (Feb–Apr 2027)

| Month | Primary study | Project deliverable |
| --- | --- | --- |
| Feb (M10) | Wiesmayr NRX paper (arxiv:2409.02912); Hoydis RT calibration paper | **Site-specific neural receiver in Sionna RT** — custom OSM scene |
| Mar (M11) | Research-level push, chosen from (a) LWM reproduce+extend, (b) DeepSense Challenge, (c) substantive Sionna PR | Asilomar 2027 workshop submission |
| Apr (M12) | Read 2025–2026 Wi-Lab papers: LWM-Spectro, LWM-Temporal, Morais similarity, Osman RIS-O-RAN | **arXiv preprint submitted**; polished CV; cold-email draft |

### Phase 5 — Application & polish (May–Jun 2027)

| Month | Action |
| --- | --- |
| May (M13) | Execute NVIDIA internship if landed OR continue research push. **Cold-email Alkhateeb** (late May–early Jun window). SoP draft. |
| Jun (M14) | PhD school list (ASU ECEE + 4–6). Polish every repo README. Reach out to 3 letter writers. Attend ICC 2027 virtually. |

## Application targets

- **NVIDIA Summer 2027 intern** — BS-level ML/SWE role. Postings open Aug–Oct 2026. Apply early (Sept–Oct window = highest yield). Cold-email Hoydis/Cammerer/Aït Aoudia **only after** a Sionna project is on GitHub.
- **Wi-Lab PhD Fall 2028** — ASU ECEE. Apps open Nov 2027, deadline ~Dec 15. Cold-email Alkhateeb May–Sep 2027 window.

## Sources filed

- [[article-2026-04-23-physical-layer-ml-roadmap]] — **the roadmap itself.**

## Reading list (pointers into `raw/`)

- `raw/textbook/README.md` — book catalog (Python / ML / DL / wireless / RL / math).
- `raw/articles/ml-phy/README.md` — paper canon (~60 papers, grouped by subtopic).
- `raw/other/online-courses.md` — course catalog.
- `raw/other/datasets.md` — DeepMIMO, DeepSense 6G, RadioML, COST2100.

## Concept pages seeded from this roadmap

**Wireless+ML core:**
- [[sionna]], [[deepmimo]], [[deepsense-6g]], [[large-wireless-model]]
- [[neural-receiver]], [[autoencoder-phy]], [[csi-feedback]]
- [[differentiable-ray-tracing]], [[wireless-digital-twin]]
- [[physical-layer-ml]] — umbrella concept
- [[channel-charting]], [[modulation-classification]], [[beam-prediction]]

**Python/ML foundations:**
- [[pytorch]], [[numpy-vectorization]]
- [[transformer]], [[attention-mechanism]], [[convolutional-neural-network]]
- [[variational-autoencoder]], [[generative-adversarial-network]], [[diffusion-model]]
- [[graph-neural-network]], [[reinforcement-learning]]
- [[backpropagation]], [[autograd]]

**Wireless crossover (DSP ↔ ML):**
- [[ofdm]] — the waveform
- [[belief-propagation]] — decoders ↔ GNN
- [[mmwave-mimo]]

**People:**
- [[alkhateeb]], [[hoydis]], [[oshea]], [[morais]] — target-lab researchers
- [[karpathy]], [[raschka]], [[rougier]], [[chollet]] — teachers & library authors
- [[prince]], [[bishop]], [[murphy]], [[goodfellow]], [[sutton]] — textbook authors
- [[bjornson]], [[heath]], [[goldsmith]], [[lichtman]], [[mackay]] — wireless/info-theory anchors
- [[ng]] — coursework anchor

## Open questions
- Letter-writer shortlist — flag at Phase 5 kickoff.
- Which specific NVIDIA team to target when postings open — decide Sept 2026.
- Whether the AirComp / [[system-pipeline]] work becomes an arXiv publication (it's a natural Phase-4 candidate).

## Cross-link with existing research

This roadmap runs in parallel with the existing [[system-pipeline]] AirComp + regret-learning project. Phase 1–2 deliverables reinforce it directly:
- OFDM-from-scratch (M2) ↔ AirComp numerology.
- Channel estimation (M9) ↔ [[channel-estimation]] in the pipeline.
- O'Shea-Hoydis autoencoder (M4) is conceptually adjacent to the AirComp autoencoder ideas in the [[signal-design-gaps]] doc.

Don't treat them as separate careers — treat AirComp as the "first paper" and this roadmap as the "research portfolio into which AirComp gets framed."
