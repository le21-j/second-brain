---
title: Automatic modulation classification (AMC)
type: concept
course: [[python-ml-wireless]]
tags: [phy-ml, modulation-classification, radioml, amc, oshea]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# Automatic modulation classification (AMC)

## In one line
Given a stretch of baseband I/Q samples from an unknown transmitter, output which modulation scheme (BPSK, QPSK, 16-QAM, AM-DSB, FSK, OFDM, etc.) is being used — the wireless analogue of "image classification for RF."

## Example first

You record a few-hundred-sample burst of I/Q at an SDR. You want to know: is that BPSK, QPSK, or 16-QAM? Classical AMC uses **cumulants** or **cyclostationary signatures** — features designed by humans to distinguish modulations. Deep learning skips the features:

```python
# RadioML 2016.10a canonical setup.
iq = samples[:128, :]          # 128 samples x 2 (I, Q)
iq = iq.reshape(2, 128)        # CNN input shape
logits = cnn(iq)               # 11 classes of modulation
pred = logits.argmax()
```

A small 1D CNN (**O'Shea, Corgan, Clancy 2016** style; then the 2018 RadioML 2018.01A treatment) achieves $\sim 75\%+$ top-1 at $18$ dB SNR and degrades gracefully below. Adding residual connections or a small transformer gives another $1$–$3$ points.

## The idea

**Tim O'Shea et al.** turned AMC into a deep-learning benchmark with the RadioML datasets:
- **RadioML 2016.10a** — $11$ modulations, $220$k samples, SNRs from $-20$ dB to $+18$ dB. Small, CPU-trainable.
- **RadioML 2018.01A** — $24$ modulations, $2.5$M samples, **over-the-air** recorded (not pure simulation). The "ImageNet of RF."

**O'Shea, Roy, Clancy 2018** (IEEE JSTSP, [arxiv:1712.04578](https://arxiv.org/abs/1712.04578)) is the reference paper — it establishes the OTA dataset and shows that deep ResNets beat classical cumulant-based classifiers by wide margins, especially at low SNR.

### What makes AMC a good first PHY-ML project

- Inputs are small ($128$ or $1024$ samples), so fast to iterate.
- The problem is natively sequence-like (I/Q is a time series), but also image-like (reshape to 2D and a CNN works).
- You get to try CNN, ResNet, Transformer architectures on the same data and see which wins.
- Robustness tests (CFO, sample-rate offset, phase rotation) are cheap to add.

### Architectures, in the order history tried them

1. **Dense MLP** — works poorly; I/Q structure is lost.
2. **1D CNN** — O'Shea 2016, the original; works well.
3. **ResNet (2D)** — reshape I/Q to $2\times N$, treat as image; strong.
4. **ResNet (1D) $+$ dilated conv** — better at capturing long-range modulation features.
5. **Transformer** — overkill at $128$ samples, but at $1024+$ samples and for $24$-class 2018.01A, attention helps.
6. **TorchSig pretrained models** (https://torchsig.com/) — newer, task-specific backbones.

### Canonical metrics

- **Overall accuracy** (top-1, averaged over all SNRs).
- **Per-SNR accuracy curve** (accuracy vs SNR plot).
- **Confusion matrix at peak SNR** — reveals which pairs are hard (e.g., AM-DSB vs AM-SSB).
- **Robustness to CFO** — train at perfect carrier; evaluate with random CFO injected; measure accuracy degradation.

## Formal definition

Given a sequence of I/Q samples $\mathbf{x} \in \mathbb{C}^N$ drawn from a modulated signal of class $c \in \{1, \ldots, C\}$ passed through an impaired channel, learn $f_\theta$:

$$\hat{\theta} = \arg\min_\theta \mathbb{E}_{c, \mathbf{x}}\big[\text{CE}(c, f_\theta(\mathbf{x}))\big]$$

At test time, evaluate per-SNR — the hard regime is low SNR.

## Why it matters / when you use it

- **Cognitive radio / spectrum sensing.** AMC is step 2 after "something is transmitting" — before you can demodulate, you need to know how.
- **Signal intelligence / ELINT.** The military-SIGINT motivation, and the reason a lot of early RF-ML funding existed.
- **A good PHY-ML learning project.** The roadmap uses it as the canonical reproduction for Phase 2 Month 5.

## Common mistakes

- **Mixing 2016 and 2018 datasets.** Different modulation sets, different quirks. Be explicit.
- **Reporting only overall accuracy.** The interesting story is in the per-SNR curve.
- **Not testing robustness.** A model that hits $90\%$ on RadioML test but collapses under $100$ Hz CFO is brittle.
- **Training on OTA $+$ testing on sim.** Keep OTA vs sim apart in train/test to see the sim-to-real gap honestly.

## Research ties

- **Reference paper:** O'Shea, Roy, Clancy 2018 (arxiv:1712.04578).
- **Datasets:** https://www.deepsig.ai/datasets/
- **Modern tooling:** TorchSig (https://torchsig.com/) is PyTorch-native RF signal framework with pretrained models.
- **Person:** [[oshea]] — founder of DeepSig, the company behind these datasets.

## Portfolio move (Phase 2 Month 5)
Reproduction repo with three models on RadioML 2016.10a $+$ 2018.01A:
- CNN (baseline).
- ResNet-18 adapted to 1D.
- Small Transformer.
- Per-SNR accuracy curves side by side.
- CFO robustness test.

## Related
- [[physical-layer-ml]]
- [[oshea]]
- [[python-ml-wireless]]

## Practice
- Phase 2 M5 — RadioML reproduction.
