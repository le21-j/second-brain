---
title: "Kim, Alikhani, Alkhateeb 2026 — LWM-Spectro: A Foundation Model for Wireless Baseband Signal Spectrograms"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/lwm-spectro-2026.pdf
source_date: 2026-01-13
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - large-wireless-model
  - lwm
  - foundation-model
  - mixture-of-experts
  - alkhateeb
  - alikhani
  - asu-wi-lab
  - spectrogram
created: 2026-05-01
updated: 2026-05-01
---

# Kim, Alikhani, Alkhateeb 2026 — LWM-Spectro: A Foundation Model for Wireless Baseband Signal Spectrograms

**Authors:** Namhyun Kim, Sadjad Alikhani, Ahmed Alkhateeb (Wi-Lab @ ASU). **arxiv:2601.08780** (Jan 2026). Hugging Face: `wi-lab/lwm-spectro`. Mirrored at `raw/articles/ml-phy/pdfs/lwm-spectro-2026.pdf`.

## TL;DR
**LWM-Spectro extends the LWM family from channels to raw I/Q baseband signals — represented as STFT spectrograms.** A transformer with a **mixture-of-experts (MoE)** architecture pretrained via masked spectrogram modeling and contrastive learning on **9.2 million I/Q spectrograms** spanning WiFi / LTE / 5G, multiple SNRs, mobility regimes, and ray-traced sites. A lightweight router selects the appropriate per-protocol expert at inference. Beats SoTA on modulation classification and joint SNR/mobility recognition, in both few-shot and data-rich regimes. **Phase 4 M12 reading.**

## Key contributions

1. **Reproducible spectrogram pretraining pipeline** — synthesizes diverse I/Q across WiFi / LTE / 5G with protocol-compliant PHY chains, 3GPP TR 38.901 TDL channels, mobility models, SNR sweeps. Produces 9.2M spectrograms.
2. **MoE foundation model for spectrograms.** Multiple Transformer encoders (one per protocol family), each pretrained with masked spectrogram modeling + contrastive learning. A lightweight router activates the most relevant expert per input — protocol-aware feature extraction with shared propagation modeling.
3. **Two pretext tasks combined:**
   - **Masked spectrogram modeling** — mask random time-frequency patches; predict their values from context (analogous to BERT MLM and ViT-MAE).
   - **Contrastive learning** — pull augmented views of the same signal together; push different signals apart.
4. **Few-shot evaluation** on modulation classification and joint SNR + mobility recognition. Beats from-scratch deep-learning baselines especially with limited labeled data.

## Methods

- **Input.** I/Q baseband samples $y[n] = \sum_{l} h_l[n] x[n-l] + w[n]$ → STFT → spectrogram $S \in \mathbb{R}^{F \times T}$.
- **Patchification.** Spectrogram is split into non-overlapping time-frequency patches → linear embeddings + positional encoding (ViT-style).
- **Architecture.** Per-protocol expert encoders (WiFi/LTE/5G), MoE router weights ≪ encoder weights so router overhead is negligible at inference.
- **Pretraining objectives.** Combined MLM (mask 15% of patches) + InfoNCE contrastive loss with augmentations: random crop, frequency masking, SNR perturbation.
- **Channel model.** 3GPP TR 38.901 TDL with multiple Doppler/SNR settings; ray-tracing-augmented for site-specific multipath.

## Results

- **Modulation classification** — beats SoTA RadioML benchmarks especially in $\leq 1$K labeled-samples regime.
- **Joint SNR/mobility recognition** — outperforms supervised CNN/Transformer baselines.
- **Cross-protocol transfer** — features pretrained on one protocol family transfer to others via the MoE router.

## Baselines compared

A reproduction must inherit the same comparison set:
- **CNN classifier from scratch** — the RadioML 2018.01A standard baseline.
- **ResNet from scratch** — deeper supervised baseline.
- **ViT from scratch** — Transformer without pretraining.
- **Single-expert Transformer (no MoE)** — ablation showing MoE benefit.
- **Supervised contrastive baselines (SimCLR-style on spectrograms)** — pretrained-but-not-MoE.

## Why it matters / where it sits in the roadmap

- **Phase 4 M12 specific reading** — [[python-ml-wireless]] M12 explicitly lists LWM-Spectro as "2025–2026 Wi-Lab papers to read."
- **Direct extension to LWM-2024** — Alikhani is the LWM first author; this paper is the I/Q sequel to the channel-domain LWM. Reading this is mandatory before cold-emailing Alkhateeb.
- **Bridges modulation classification ↔ foundation models.** Modulation classification ([[modulation-classification]]) was a cold benchmark; LWM-Spectro reframes it as a downstream task for a foundation model.
- **MoE for wireless** is novel; protocol-specialized experts is a clean idea worth knowing.

## Concepts grounded

- [[large-wireless-model]] — extends to spectrograms.
- [[modulation-classification]] — primary downstream task.
- [[transformer]] — backbone; ViT-style patchification.
- [[stft]] — spectrogram = STFT magnitude.

## Portfolio move (Phase 4)

> **Reproduce first, extend second.** Without a reproduced baseline, the extension has nothing to point at.

**Reproduce (the artifact — Step 0):**
1. Pull `wi-lab/lwm-spectro` from Hugging Face.
2. Reproduce the paper's **modulation classification on RadioML 2018.01A** + **joint SNR/mobility recognition** results.
3. Match the baselines listed above (from-scratch CNN/ResNet/ViT) at the same SNR / few-shot budgets the paper reports.
4. Write up the reproduction as a blog + figure-verification.

**Extend (after reproduction lands):**
- Fine-tune on a downstream task LWM-Spectro does NOT evaluate: interference detection, radar-vs-comm classification, waveform ID (Bluetooth, LoRa) — generated via GNU Radio.
- Submit results as Asilomar 2027 workshop paper or extend the Hugging Face Space demo.

> [!tip] Interviewer talking point (Wi-Lab cold email)
> "I reproduced LWM-Spectro on RadioML and extended to [Bluetooth / LoRa / radar-vs-comm]; the MoE router specialization holds across the new protocol — happy to share the writeup."

## Questions raised
- **Router design.** Lightweight router is an FFN over per-patch features; alternative top-K routing or mixture-of-depths could be explored.
- **Few-shot regime sample efficiency** — competitive against contrastive baselines like SimCLR / MoCo specifically tailored to spectrograms?
- **Online adaptation.** Could the MoE adapt its router for a newly-deployed protocol without retraining experts?

## Related
- [[python-ml-wireless]]
- [[large-wireless-model]]
- [[paper-lwm-2024]] — the original LWM (channels).
- [[paper-lwm-temporal-2026]] — sequel for spatiotemporal channels.
- [[paper-radioml-oshea-2018]] — modulation-classification benchmark.
- [[modulation-classification]]
- [[alkhateeb]], [[alikhani]] — Wi-Lab team.
