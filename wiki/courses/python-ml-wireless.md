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
| Jun (M2) | NumPy deep-dive ([[textbook-from-python-to-numpy]], 100 exercises); scipy.signal; [[textbook-pysdr-lichtman]] Ch 1–4; Ng ML Courses 2–3 | **OFDM-from-scratch notebook** — BER vs Eb/N0 vs theory |
| Jul (M3) | [[textbook-deep-learning-with-pytorch]] Ch 1–8; [Karpathy Zero-to-Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ); Ng DL Courses 1–2 | **CIFAR-10 ResNet-18 with AMP, W&B-logged** |

### Phase 2 — Deep learning + first wireless-ML projects (Aug–Oct 2026)

| Month | Primary study | Project deliverable |
| --- | --- | --- |
| Aug (M4) | Ng DL Courses 3–4 (CNNs); CS231n Assignment 2 (**full**); [[textbook-prince-understanding-deep-learning]] Ch 1–11 | **Reproduce O'Shea-Hoydis 2017 autoencoder** — BLER curves. **NVIDIA intern postings begin — monitor weekly.** |
| Sep (M5) | Ng DL Course 5; CS224N Lectures 5–7; transformers week (Illustrated → Karpathy → "Attention Is All You Need" → Prince Ch 12) | **Reproduce RadioML modulation classification** — CNN + ResNet + Transformer. **Submit early NVIDIA BS-level intern applications.** |
| Oct (M6) | TensorFlow/Keras crash course (25–35 h); [[textbook-deep-learning-with-python-chollet]] Ch 3, 7, 9; generative models (Prince Ch 14–15; Kingma VAE; Lilian Weng) | **Reproduce CsiNet + CRNet + CLNet** — compression ratios 1/4, 1/16, 1/32, 1/64. First Lightning+Hydra refactor. |

### Phase 3 — Physical-layer ML specialization (Nov 2026–Jan 2027)

| Month | Primary study | Project deliverable |
| --- | --- | --- |
| Nov (M7) | [[sionna]] tutorials Parts 1–4 on GPU; Sionna white paper; CS224W (GNNs); [[textbook-sutton-barto-rl]] Ch 1–8; David Silver lectures 1–7 | **Modified Sionna neural receiver** — Transformer block swap + blog writeup |
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

### Textbooks (summaries in `wiki/summaries/`)
**Full PDFs ingested + chapter-roadmapped (2026-05-01 batch 1):**
- [[textbook-prince-understanding-deep-learning]] — Prince UDL v5.0.3 (21 MB) — **primary DL textbook**
- [[textbook-sutton-barto-rl]] — Sutton-Barto 2nd ed (42 MB) — RL canon
- [[textbook-mackay-itila]] — MacKay Information Theory (5.4 MB) — LDPC chapters 47–50
- [[textbook-parr-matrix-calculus]] — Parr-Howard Matrix Calculus (one-sitting backprop math)

**Reference-card stubs (no PDF; pull when reading — 2026-05-01 batch 2):**
- [[textbook-pysdr-lichtman]] — Lichtman PySDR — Phase 1 M2 OFDM-from-scratch backbone + Ch 16 ML-for-RF on-ramp
- [[textbook-bishop-prml]] — Bishop PRML — DSP↔ML identity bridge (Ch 13 HMM/Kalman before M4 autoencoder repro; Ch 8 graphical models before M7 NRX)
- [[textbook-goodfellow-deep-learning]] — old-testament theoretical reference (Ch 5–10, 14–15)
- [[textbook-deep-learning-with-pytorch]] — PyTorch internals (Ch 1–8, Phase 1 M3)
- [[textbook-from-python-to-numpy]] — Rougier NumPy vectorization (Phase 1 M2)
- [[textbook-deep-learning-with-python-chollet]] — Chollet TF/Keras (Phase 2 M6 — Sionna 1.x prep)
- [[textbook-d2l-dive-into-deep-learning]] — code-first companion to Prince
- [[textbook-murphy-pml-intro]] — modern probabilistic ML encyclopedia
- [[textbook-ml-with-pytorch-scikit-learn]] — Raschka sklearn → PyTorch bridge
- [[textbook-scientific-visualization-matplotlib]] — Rougier matplotlib (THE headline-figure rule)

### Papers (summaries in `wiki/summaries/`, PDFs in `raw/articles/ml-phy/pdfs/`)
**Phase 1–3 ingested 2026-05-01 (foundational batch):**
- **PHY-ML autoencoder thread:** [[paper-oshea-hoydis-2017-autoencoder]], [[paper-aitaoudia-hoydis-2020-ofdm]], [[paper-dorner-2018-otaair]]
- **NVIDIA Sionna:** [[paper-sionna-2022]], [[paper-sionna-rt-2023]]
- **NVIDIA neural receivers:** [[paper-nrx-cammerer-2023]], [[paper-nrx-wiesmayr-2024]]
- **Wi-Lab stack:** [[paper-deepmimo-2019]], [[paper-deepsense-6g-2023]], [[paper-lwm-2024]], [[paper-digital-twin-vision-2023]]
- **Subdomain canon:** [[paper-csinet-wen-2018]], [[paper-radioml-oshea-2018]], [[paper-channel-charting-studer-2018]]
- **Filed as PDF only (no summary needed — well-known general ML):** Simeone 2018 ML primer, ResNet 2015, Attention Is All You Need 2017.

**Phase 4 ingested 2026-05-01 (Tier-1 sweep — directly cited from M10 + M12):**
- **Sionna RT calibration (M10 NVIDIA-portfolio capstone):** [[paper-diff-rt-calibration-2024]] — Hoydis et al. 2024 IEEE TMLCN; gradient-based RT calibration on **DICHASUS** indoor MIMO sounder.
- **Wi-Lab 2026 LWM family (M12 reading):** [[paper-lwm-spectro-2026]] (Kim/Alikhani/Alkhateeb — MoE for I/Q spectrograms) + [[paper-lwm-temporal-2026]] (Alikhani/Malhotra/Hamidi-Rad/Alkhateeb — sparse spatio-temporal attention for trajectories).

**Phase 4 ingested 2026-05-01 (Tier-2 sweep — 2024-2026 NVIDIA + Wi-Lab papers):**
- **NVIDIA Aerial 2025 flagship line:** [[paper-sionna-research-kit-2025]] (Cammerer et al. — real-time Jetson + Sionna + TensorRT 5G testbed; the **literal product an NVIDIA Aerial intern would deploy**) + [[paper-wiesmayr-salad-2025]] (Wiesmayr et al. — ACK/NACK-only link adaptation, beats industry-standard OLLA by up to 15%).
- **Wi-Lab sim-to-real / digital-twin operationalization:** [[paper-morais-similarity-2026]] (task-aware dataset distance metric, Pearson > 0.85) + [[paper-luo-dt-csi-feedback-2025]] (site-specific digital twins for CSI compression with fidelity decomposition).
- **Wi-Lab V2V + RIS hardware:** [[paper-deepsense-v2v-2024]] (120 km mmWave V2V dataset) + [[paper-osman-ris-oran-2025]] (1024-element 28-GHz RIS in 5G O-RAN, MILCOM 2025 Best Demo).

**Tier-3 ingested 2026-05-01 (foundational papers + Phase 3 RL coverage):**
- **Cammerer-cold-email prereq (M7 reading):** [[paper-gruber-2017-channel-decoding]] — Gruber/Cammerer/Hoydis/ten Brink 2017 CISS; **mandatory** prereq for any Cammerer cold email — it's where his PhD line starts.
- **Phase 2 M6 generative trio:** [[paper-kingma-2013-vae]] + [[paper-goodfellow-2014-gan]] + [[paper-ho-2020-ddpm]] — the three foundational generative papers M6 reproduction needs.

## Reading list (pointers into `raw/`)

- `raw/textbook/README.md` — book catalog (Python / ML / DL / wireless / RL / math).
- `raw/textbook/pdfs/` — downloaded PDFs (4 textbooks as of 2026-05-01).
- `raw/articles/ml-phy/README.md` — paper canon (~60 papers, grouped by subtopic).
- `raw/articles/ml-phy/pdfs/` — downloaded PDFs (17 papers as of 2026-05-01).
- `raw/other/online-courses.md` — course catalog.
- `raw/other/datasets.md` — DeepMIMO, DeepSense 6G, RadioML, COST2100.

## Concept pages seeded from this roadmap

**Wireless+ML core:**
- [[sionna]] (umbrella), [[sionna-rt]] *(NEW 2026-05-01 — differentiable RT module distinct from umbrella)*, [[nvidia-aodt]] *(NEW 2026-05-01 — Aerial Omniverse Digital Twin product)*
- [[deepmimo]], [[deepsense-6g]], [[large-wireless-model]]
- [[neural-receiver]], [[neural-decoder]] *(NEW 2026-05-01 — distinct from neural-receiver; the BP-replacement subblock)*
- [[autoencoder-phy]], [[csi-feedback]]
- [[differentiable-ray-tracing]], [[wireless-digital-twin]]
- [[physical-layer-ml]] — umbrella concept
- [[channel-charting]], [[modulation-classification]], [[beam-prediction]]

**Python/ML foundations:**
- [[pytorch]], [[numpy-vectorization]]
- [[transformer]], [[attention-mechanism]], [[convolutional-neural-network]]
- [[variational-autoencoder]], [[generative-adversarial-network]], [[diffusion-model]]
- [[graph-neural-network]], [[reinforcement-learning]]
- [[backpropagation]], [[autograd]]

**Optimization, loss, regularization (NEW 2026-05-01 — Phase 1 foundations):**
- [[gradient-descent]], [[stochastic-gradient-descent]], [[adam-optimizer]]
- [[cross-entropy-loss]], [[mse-loss]], [[softmax]]
- [[regularization]], [[dropout]], [[batch-normalization]]
- [[overfitting-bias-variance]]

**Wireless basics (NEW 2026-05-01 — Phase 1–2 foundations):**
- [[qam-modulation]], [[ldpc-codes]], [[ber-bler]]
- [[mimo-basics]], [[mmwave-mimo]], [[fading-channels]], [[antenna-array]]
- [[matched-filter]], [[equalization]]
- [[link-adaptation]] — MCS selection (OLLA classical, SALAD modern)

**Reinforcement learning atoms (NEW 2026-05-01 — Phase 3 M7–M8):**
- [[bandit-regret]] — Sutton-Barto Ch 2; the **direct ancestor of Jayden's existing [[regretful-learning]] AirComp work** — the single-agent special case
- [[q-learning]], [[sarsa]] — tabular TD-control
- [[policy-gradient]], [[reinforce]], [[actor-critic]] — policy-based methods
- [[gae]] — Generalized Advantage Estimation; load-bearing for PPO
- [[ppo]] — modern on-policy default
- [[sac]] — off-policy continuous-action default (the actual wireless-RL workhorse)
- [[dqn]] — deep Q-learning

**Industrial / deployment (NEW 2026-05-01 — Phase 3–4):**
- [[5g-nr-pusch-structure]] — **NEW (Lyra audit)** — DM-RS / TBS / HARQ timing; first-technical-screen probe
- [[sionna-api-cheatsheet]] — **NEW (Lyra audit)** — Sionna 2.x ResourceGrid + channel + LDPC + training-loop scaffold
- [[quantization-aware-training]] — **NEW (Lyra audit)** — PTQ vs QAT; the Wiesmayr-2024 0.5 dB recovery technique
- [[ris]] — Reconfigurable Intelligent Surface (6G technology pillar)
- [[o-ran]] — Open RAN architecture, xApps / E2 interface
- [[link-adaptation]] — MCS selection (OLLA + SALAD)
- [[harq]] — Hybrid ARQ retransmission (the feedback signal driving link adaptation)
- [[onnx]] — PyTorch → TensorRT bridge format
- [[tensorrt]] — NVIDIA's GPU inference compiler (deployment path for trained models)
- [[umap]] — dim reduction (used by Morais 2026 dataset-similarity)

**Wireless crossover (DSP ↔ ML):**
- [[ofdm]] — the waveform
- [[belief-propagation]] *(NEW 2026-05-01 — sum-product on factor graph = neural BP / GNN message-passing; the load-bearing DSP↔ML identity for decoders)*
- [[mmwave-mimo]] *(NEW 2026-05-01 — sparse + hybrid + blockage-prone variant; the SHARED Wi-Lab/Sionna problem)*

**People:**
- [[alkhateeb]], [[hoydis]], [[aitaoudia]], [[cammerer]], [[wiesmayr]], [[alikhani]], [[oshea]], [[morais]] — target-lab researchers (4 new 2026-05-01: NVIDIA #2/#3, ETH-with-NVIDIA-internship Wiesmayr, Wi-Lab LWM first author Alikhani)
- [[karpathy]], [[raschka]], [[rougier]], [[chollet]] — teachers & library authors
- [[prince]], [[bishop]], [[murphy]], [[goodfellow]], [[sutton]] — textbook authors
- [[bjornson]], [[heath]], [[lichtman]], [[mackay]] — wireless/info-theory anchors
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
