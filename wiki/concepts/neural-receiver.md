---
title: Neural receiver
type: concept
course:
  - "[[python-ml-wireless]]"
tags: [phy-ml, 5g-nr, receiver, sionna, nvidia, nrx]
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-04-23
updated: 2026-05-06
---

# Neural receiver

## In one line
A single end-to-end neural network that replaces the channel estimator $+$ equalizer $+$ demapper pipeline of a 5G NR receiver, outputs LLRs that feed an unchanged LDPC decoder, and is trained to minimize bit-level cross-entropy against truth.

## Example first

**The canonical 5G NR PUSCH receiver chain:**
```
y_grid -> [LS ch-est on DMRS] -> [MMSE equalize] -> [QAM->LLR demap] -> LDPC
```

Each block uses assumptions about Gaussian noise, known pilot positions, perfect synchronization. When those assumptions are wrong — nonlinear PA, phase noise, Doppler, pilot contamination — each block's error compounds.

**The NRX (neural RX) version** (Cammerer et al. 2023; Wiesmayr et al. 2024):
```
y_grid -> [CNN / Transformer over (freq x time x ant)] -> LLRs -> LDPC
```
One network sees the full resource grid, learns where the DMRS pilots are, learns the channel's statistics empirically, and outputs LLRs directly. Trained on 3GPP UMi at multiple SNRs, deployed standard-compliant. The standard-compliant version (arxiv:2409.02912, code at https://github.com/NVlabs/neural_rx) runs in real-time on an NVIDIA A100 and beats an LMMSE receiver by $1$–$2$ dB at $10^{-2}$ BLER in the critical low-SNR region.

## The idea

The neural receiver is the natural **block-replacement** formulation of [[physical-layer-ml]]: it doesn't touch the transmitter (so backward-compatible with deployed UEs), doesn't touch the LDPC decoder (which is already near-optimal when fed correct LLRs), but replaces the middle — where most of the receiver's performance loss happens.

### Architectural choices

The NRX line of work has converged on some patterns:

- **Input representation.** The resource grid itself: a complex-valued tensor indexed by (frequency bin, OFDM symbol, antenna, batch). Convert to 2-channel real or keep complex.
- **Backbone.** Early NRX papers used **stacked residual CNNs** (convolutions over freq $\times$ time — just like a 2D image). $2023+$ papers add **self-attention across antennas** for better MU-MIMO performance. The 2024 standard-compliant NRX uses a **lightweight transformer** over the resource grid.
- **Output head.** LLRs per coded bit, $L \in \mathbb{R}^{K}$. Trained with binary cross-entropy with logits against the true bit labels.
- **Pilot handling.** Two schools: (1) feed the pilot positions as an extra channel (supervised), or (2) let the network discover them (unsupervised). The standard-compliant NRX does (1).

### Training loop

Typical training:
1. Draw a batch of channel realizations from [[sionna]] 3GPP 38.901 UMi.
2. Draw random PUSCH transport blocks.
3. Run Sionna's standard-compliant TX chain $\to$ get `y_grid` after AWGN.
4. Run the neural network to get LLRs.
5. Compute binary cross-entropy against the known bits.
6. Backprop, update.

Because Sionna is **fully differentiable**, you can also backprop through the channel — useful for joint TX/RX optimization, which is the [[autoencoder-phy]] direction.

### Variants

- **Pilotless NRX.** Train the network to work with fewer or no DMRS pilots — recovers spectral efficiency. Aït Aoudia & Hoydis 2020 (arxiv:2009.05261).
- **Site-specific NRX.** Pretrain on generic channels, fine-tune on a specific cell site's ray-traced channels (see [[differentiable-ray-tracing]]).
- **Joint IDD $+$ NRX.** The neural receiver replaces the demapper and the **iterative detection-decoding** loop.

## Formal definition

For a PUSCH slot with received resource grid $\mathbf{Y} \in \mathbb{C}^{N_{\text{freq}} \times N_{\text{sym}} \times N_{\text{ant}}}$ and the true bit vector $\mathbf{b} \in \{0, 1\}^K$:

$$\hat{\theta} = \arg\min_\theta \mathbb{E}_{\mathbf{b}, \mathbf{H}, \mathbf{N}}\; \text{BCE}\big(\mathbf{b}, \sigma(L_\theta(\mathbf{Y}))\big)$$

with $\mathbf{Y} = \text{OFDMChannel}(\text{map}(\mathbf{b}); \mathbf{H}) + \mathbf{N}$.

At inference, the LLRs $L_\theta(\mathbf{Y})$ feed directly into the standard-compliant 5G LDPC decoder.

## Why it matters / when you use it

- **It is the current flagship NVIDIA Research project** in PHY-ML. Reproducing a neural receiver in Sionna is the single strongest signal to the NVIDIA Sionna team that you understand their work.
- **It is deployable.** Standard-compliant at the bit/slot level; only the receiver changes. This is the easiest path from DL paper to real RAN.
- **It is where Sionna's differentiability actually pays off.** Backprop through the channel is the reason you can train an NRX at all.

## Common mistakes

- **Training at a single SNR.** The receiver will only work there. Train at a range; use curriculum or SNR-conditioned training.
- **Ignoring quantization and fixed-point deployment.** An NRX that uses FP32 everywhere is a prototype, not a deployable thing. The SRK and ACAR papers are about bridging to INT8 / BF16 deployment.
- **Overfitting to your channel simulator.** Exactly the same channel model for train and eval means your BLER curve proves your simulator is consistent with itself. Use held-out scenarios.

## Research ties

- **Papers:** Cammerer, Aït Aoudia, Hoydis et al. 2023 (arxiv:2312.02601); Wiesmayr, Cammerer, Aït Aoudia, Hoydis et al. 2024 (arxiv:2409.02912); Aït Aoudia & Hoydis 2020 pilotless OFDM (arxiv:2009.05261).
- **Code:** https://github.com/NVlabs/neural_rx.
- **Upstream:** [[autoencoder-phy]] (O'Shea & Hoydis 2017), ViterbiNet (Shlezinger 2019).

## Portfolio move (Phase 3 Month 7)
**See [[nrx-reproduction-walkthrough]]** — the full 6-stage step-by-step reproduction guide. The walkthrough is the headline executable artifact for the entire roadmap; this concept page intentionally defers to it instead of duplicating.

## Related
- [[nrx-reproduction-walkthrough]] — **the M7 capstone walkthrough.**
- [[5g-nr-pusch-structure]] — the standard-compliant grid the NRX consumes.
- [[sionna]], [[sionna-api-cheatsheet]] — the simulator + how to assemble the training loop.
- [[neural-decoder]] — the post-NRX decoding subblock (or, in some architectures, the back end of a joint NRX).
- [[physical-layer-ml]] — umbrella.
- [[autoencoder-phy]] — the "E2E" relative.
- [[differentiable-ray-tracing]] — site-specific extension.
- [[hoydis]], [[cammerer]], [[aitaoudia]], [[wiesmayr]] — NVIDIA-target authors.
- [[python-ml-wireless]]

## Practice
- Phase 3 M7 — Sionna tutorials 1–4 $+$ Transformer swap.
- Phase 4 M10 — site-specific NRX in Sionna RT (custom OSM scene).
