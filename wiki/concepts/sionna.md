---
title: Sionna
type: concept
course: [[python-ml-wireless]]
tags: [nvidia, simulator, pytorch, tensorflow, ray-tracing, 5g-nr, phy]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# Sionna

## In one line
NVIDIA's open-source, GPU-accelerated, fully differentiable simulator for link-level physical-layer research — 5G NR blocks, channel models, MIMO-OFDM, and now ray tracing — written so every signal path is a tensor that gradients can flow through.

## Example first

**You want to train a neural receiver on 3GPP UMi channels.** In Sionna, that looks like:

```python
import sionna.phy as phy
import torch

# 1. Build a batch of channel realizations from the 3GPP 38.901 UMi model.
channel = phy.channel.tr38901.UMi(carrier_frequency=3.5e9,
                                   o2i_model="low", ...)
# 2. Build a 5G NR PUSCH transmitter and a neural receiver.
pusch_config = phy.nr.PUSCHConfig()
tx = phy.nr.PUSCHTransmitter(pusch_config)
rx = MyNeuralReceiver(num_layers=6)  # a PyTorch module you wrote

# 3. Run a batched forward pass — everything is a tensor.
b = torch.randint(0, 2, (1024, pusch_config.tb_size))
x, _ = tx(b)                      # TX -> modulated symbols
y = channel(x, snr_db=5.0)        # channel -> noisy received symbols
llr = rx(y, pilots=tx.pilots)     # neural RX -> log-likelihood ratios

# 4. Backprop a BLER-aligned loss through channel, TX, and RX.
loss = binary_cross_entropy_with_logits(llr, b)
loss.backward()
```

The channel is **differentiable** — the gradient flows from the loss, through the neural receiver, back through the channel model, and into whatever part of the TX you chose to leave trainable. That is what makes Sionna qualitatively different from MATLAB 5G Toolbox or Vienna 5G simulator: you can train across the whole link.

## The idea

Sionna (pronounced "Shannon"-like, from Irish `shiona`, "foxglove") started in 2022 as a TensorFlow/Keras library from NVIDIA Research in Munich (Hoydis, Cammerer, Aït Aoudia et al.; arxiv:2203.11854). As of the roadmap date (April 2026), the library is split into three modules and two versions:

| Module | What it does | Status |
| --- | --- | --- |
| **Sionna PHY** | Link-level — 5G NR LDPC $+$ polar, modulation/demapping, MIMO, OFDM, channel estimation, 5G NR PUSCH, 3GPP 38.901 channels | PyTorch in 2.x; TensorFlow in 1.x |
| **Sionna SYS** | System-level PHY abstraction, link adaptation, scheduling, power control | PyTorch in 2.x |
| **Sionna RT** | Differentiable ray tracing on Mitsuba 3 $+$ Dr.Jit; framework-agnostic (TF/PyTorch/JAX/NumPy) | Framework-agnostic throughout |

**Version reality as of April 2026:**
- **Sionna 2.x** — Python 3.11+, PyTorch 2.9+. PHY and SYS migrated.
- **Sionna 1.2.x** — remains TensorFlow. Many published tutorials still assume 1.x. **Always check which backend a tutorial targets.**

### Sionna PHY building blocks to know

- `Mapper` / `Demapper` — symbol $\leftrightarrow$ LLR. Supports QAM, PAM, arbitrary constellations.
- `OFDMChannel` — frequency-domain channel application.
- `ResourceGrid` / `ResourceGridMapper` — 5G NR resource grid.
- `LDPC5GEncoder` / `LDPC5GDecoder` — standard-compliant 5G LDPC (with BP, min-sum, and neural variants).
- `PolarEncoder` / `PolarSCLDecoder` — polar codes for control.
- `tr38901.UMi` / `UMa` / `RMa` / `InF` / `InH` — 3GPP channel models.
- `TDL` / `CDL` — tapped delay line / clustered delay line channels.
- `LSChannelEstimator`, `LMMSEChannelEstimator` — classical baselines to compare against.
- `LinearDetector`, `KBestDetector`, `EPDetector` — classical MIMO detectors.

### Sionna RT — differentiable ray tracing

Built on Mitsuba 3 $+$ Dr.Jit, so backprop flows through *physical* ray bounces. You can:
- Load a scene (Mitsuba XML or glTF / GLB; OSM buildings are a common source).
- Place transmitters, receivers, RIS elements.
- Query the path tree (time of arrival, angle of departure/arrival, amplitude).
- Compute **Radio Maps** — coverage heatmaps over a scene.
- Differentiate with respect to material properties, antenna patterns, even scene geometry $\to$ the foundation for [[differentiable-ray-tracing]] calibration (Hoydis TMLCN 2024).

Supports specular $\&$ diffuse reflection, refraction, **diffraction (since v1.2)**, **RIS (since v0.18)**, and mobility.

### Core Sionna tutorials to complete

The roadmap calls out this ordered list (https://nvlabs.github.io/sionna/phy/tutorials.html):

1. Part 1 (Getting Started)
2. Part 2
3. Part 3
4. **Part 4 (Advanced Neural Receiver — training $+$ benchmarking)** $\leftarrow$ the high-leverage one
5. 5G NR PUSCH
6. OFDM MIMO Detection
7. Autoencoder (end-to-end learning)
8. Realistic Multiuser MIMO
9. Iterative Detection and Decoding
10. Pulse Shaping
11. Sionna RT: Introduction + Mobility + Radio Maps + RIS

All source at https://github.com/NVlabs/sionna/tree/main/examples.

### Sionna Research Kit (SRK)

Released 2025 (Cammerer et al., arxiv:2505.15848). A GPU-accelerated research platform for **AI-RAN** — ties Sionna to NVIDIA's production cuPHY/cuMAC/Aerial stack so research prototypes can run on real baseband hardware.

## Formal definition (what is "differentiable" doing)

Sionna guarantees that the forward pass $y = \text{channel}(x; \text{params})$ and every PHY block satisfies:

$$\frac{\partial y_i}{\partial x_j}, \quad \frac{\partial y_i}{\partial \text{params}_k}$$

are defined and computable by the tensor framework's autograd. This is non-trivial — it required re-writing classical DSP blocks (FIR filters, FFTs, hard-decision demappers) so they stay within the autograd graph. Hard thresholds become soft (temperature-scaled); non-differentiable samplers become Gumbel-softmax or reparameterization tricks.

## Why it matters / when you use it

- **Training E2E receivers.** The canonical reason. See [[neural-receiver]].
- **Calibrating a digital twin.** Differentiable RT lets you optimize scene material parameters to match real-world measurements — Hoydis 2024.
- **Generating ray-traced training data.** Export to `dm.convert()` and you have [[deepmimo]]-compatible channels for any custom scene.
- **Benchmarking.** Every new PHY-ML paper in 2024+ benchmarks against the nearest Sionna implementation.

## Common mistakes

- **Using Sionna 1.x tutorials with Sionna 2.x installed.** Import paths changed; Keras-style training loops no longer work. Pin your version.
- **Leaving `tf.function`-wrapped Sionna 1.x blocks inside a PyTorch loop.** The frameworks don't mix; pick one.
- **Assuming Sionna RT is photorealistic.** It models EM propagation (reflections, diffraction, diffuse scattering) — it does *not* model the visible-light interactions that Mitsuba 3 does for graphics. If your goal is rendering, use vanilla Mitsuba; for RF, use Sionna RT.

## Research ties

- **Key papers:** Sionna (arxiv:2203.11854); Sionna RT (arxiv:2303.11103, 2504.21719); NRX (arxiv:2312.02601, 2409.02912); RT calibration (https://github.com/NVlabs/diff-rt-calibration); SRK (arxiv:2505.15848); SALAD (arxiv:2510.05784).
- **People:** [[hoydis]], Cammerer, Aït Aoudia, Wiesmayr, Keller.
- **OSS:** https://github.com/NVlabs/sionna, https://github.com/NVlabs/neural_rx, https://github.com/NVlabs/sionna-rk, https://github.com/NVlabs/diff-rt-calibration.

## The move for Jayden's portfolio
A **Sionna project on GitHub** is the single strongest intern-application signal. The minimum viable project: reproduce Tutorial Part 4 (neural receiver), swap a CNN for a small Transformer block, compare BLER curves on CDL-A and UMi. Total effort: $\sim 3$ weeks.

## Related
- [[physical-layer-ml]]
- [[neural-receiver]]
- [[deepmimo]] — interoperates via `dm.convert()`
- [[differentiable-ray-tracing]]
- [[wireless-digital-twin]]
- [[hoydis]] — lead
- [[deep-learning-with-python-chollet]] — for the legacy TF API

## Practice
- Phase 3 Month 7 deliverable: tutorials Parts 1–4 on GPU $+$ modified neural receiver.
- Phase 4 Month 10: site-specific neural receiver using Sionna RT custom scene.
