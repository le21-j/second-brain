---
title: Physical-layer machine learning
type: concept
course: [[python-ml-wireless]]
tags: [wireless, ml, umbrella, phy]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# Physical-layer machine learning

## In one line
Replacing hand-designed blocks in the wireless physical layer (channel estimator, equalizer, demapper, decoder, beamformer) with learned neural networks trained end-to-end or block-wise, validated by BER/BLER and SNR gain on real or ray-traced channels.

## Example first

**The block-by-block picture.** A classical 5G NR receiver looks like this:

```
y  ->  [sync]  ->  [channel estimator]  ->  [equalizer]  ->  [demapper]  ->  [LDPC decoder]  ->  bits
```

Each block is hand-designed: channel estimator is LS or LMMSE, equalizer is ZF or MMSE, demapper is a log-likelihood-ratio formula, LDPC decoder is sum-product on a factor graph. The end-to-end performance is **Shannon-capacity-limited only under the modeling assumptions** — if the channel isn't truly Rayleigh, or the noise isn't truly Gaussian, the receiver leaves performance on the table.

**The ML receiver picture** (the [[neural-receiver]] line of work):
```
y  ->  [neural network (CNN / Transformer / GNN)]  ->  LLRs
```
One trainable block. You keep the outer LDPC decoder (it's already near-optimal when fed correct LLRs) and replace the middle with a network trained to minimize cross-entropy against the true bits. Trained on 3GPP UMi channels in Sionna, the resulting NRX beats a classical linear MMSE receiver by $\sim 1$–$2$ dB at $10^{-2}$ BLER — at a fraction of the computational complexity needed for a true MAP receiver.

The deeper example: in an **end-to-end autoencoder** ([[autoencoder-phy]]), *both* the transmitter constellation and the receiver are replaced by networks and jointly trained. The network discovers its own modulation that's Pareto-dominant over QAM on specific impaired channels.

## The idea

PHY-ML divides cleanly into four problem classes, and most of the literature lives in one of them:

1. **Learned estimation** — channel estimation, CSI compression and feedback, channel prediction. The network mimics a classical estimator but learns the channel's empirical prior instead of assuming Rayleigh + white noise. Examples: [[csi-feedback]] (CsiNet), DL channel estimation (He 2018; Neumann 2018; Hu 2021).
2. **Learned detection / decoding** — demapping LLRs, MIMO detection, iterative decoder unfolding. The network replaces or augments a known algorithm. Examples: Deep MIMO Detection (Samuel 2017), ViterbiNet (Shlezinger 2019), neural BP decoders (Nachmani 2018; Buchberger 2020).
3. **End-to-end learning** — jointly train TX $+$ RX. The network is both the encoder and decoder; the "channel" is either a differentiable simulator or a learned GAN. Autoencoder-PHY (O'Shea-Hoydis 2017), model-free training (Aït Aoudia 2019), full 5G NR neural receiver (Cammerer 2023; Wiesmayr 2024).
4. **Learned optimization / control** — beamforming, power control, scheduling, link adaptation. Usually RL or supervised imitation of an optimal solver. Examples: "Learning to Optimize" (Sun 2017), Spatial DL Scheduling (Cui 2018), SALAD (Wiesmayr 2025).

Common thread: **the model trades generalizable mathematical structure for empirical fit to channel statistics you actually see**. That's why site-specific DL (digital twins, ray-traced pretraining — see [[differentiable-ray-tracing]], [[wireless-digital-twin]]) is the current frontier: train the network on ray-traced channels for the specific cell site it will deploy in, and you get bigger gains than from a generic-trained network.

## Formal definition

In receiver-replacement form, the PHY-ML problem is:

$$\hat{\theta} = \arg\min_\theta \mathbb{E}_{(b, h, n)} \big[ \mathcal{L}\big(b, f_\theta(y(b,h,n))\big) \big]$$

where $b$ is the information bit vector, $h$ is the (random) channel realization, $n$ is noise, $y$ is the received waveform, $f_\theta$ is the learned receiver with parameters $\theta$, and $\mathcal{L}$ is typically binary cross-entropy over LLRs (or MSE for channel estimation). The expectation is over a **channel distribution** — either a 3GPP TDL/CDL model for generic training, or a ray-traced set from [[deepmimo]] / [[sionna]] RT for site-specific training.

## Why it matters / when you use it

- **Non-Gaussian impairments.** PAs, LO phase noise, I/Q imbalance, hardware aging — none of these are cleanly captured by the Rayleigh-AWGN model, but they shape the *empirical* distribution the receiver sees. A learned receiver captures them for free.
- **Pilot reduction.** A neural receiver can learn to estimate the channel with fewer pilots, recovering spectral efficiency — NVIDIA's standard-compliant NRX runs with *pilotless* RX variants.
- **Site-specific gains.** A digital-twin-trained network knows the specific multipath at your BS, which a generic network cannot.
- **Complexity.** Well-designed neural receivers are often *simpler* at inference than a MAP receiver (which requires iterative joint detection-decoding) — this is why NVIDIA ports them onto GPU baseband (cuPHY, Sionna Research Kit).

## Common mistakes

- **Training on one channel, deploying on another.** PHY-ML networks do not generalize across dramatically different channel statistics (e.g., training on UMi $3.5$ GHz, deploying at $60$ GHz mmWave). Best practice: site-specific fine-tuning on ray-traced channels from [[deepmimo]].
- **Skipping the classical baseline.** A DL paper without an LMMSE / MAP baseline at the same SNR sweep is not a credible paper.
- **Over-fitting to the simulator.** If your training channels come from one 3GPP model and your test channels come from the same model, you've validated the simulator, not the receiver. Mix real-world (OTA) test data when you can.

## Related
- [[sionna]] — the simulation stack everyone reproduces in
- [[deepmimo]] — the ray-traced channel dataset
- [[neural-receiver]] — the canonical architecture
- [[autoencoder-phy]] — the earliest seminal thread
- [[csi-feedback]] — a different axis (estimation, not detection)
- [[differentiable-ray-tracing]] — site-specific pretraining
- [[wireless-digital-twin]] — the deployment vision
- [[python-ml-wireless]] — curriculum

## Practice
*(Phase 2 reproductions are the practice here — see the roadmap.)*
