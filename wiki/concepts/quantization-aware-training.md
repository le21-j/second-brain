---
title: Quantization-aware training (QAT)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - quantization
  - qat
  - tensorrt
  - int8
  - deployment
  - phase-4
sources:
  - "[[paper-nrx-wiesmayr-2024]]"
  - "[[paper-sionna-research-kit-2025]]"
created: 2026-05-01
updated: 2026-05-01
---

# Quantization-aware training (QAT)

## In one line
**QAT trains a neural network with simulated INT8 quantization in the forward pass — the model learns weights that quantize cleanly.** Recovers the ~0.5 dB accuracy gap that **post-training quantization (PTQ)** loses on edge-deployed neural receivers. Used in [[paper-nrx-wiesmayr-2024]] to ship NRX on Jetson at full BLER performance.

## Example first

```python
import torch
import torch.ao.quantization as Q

# 1. Mark the model for QAT
model = NeuralReceiver()
model.qconfig = Q.get_default_qat_qconfig("x86")  # or "qnnpack" for ARM
Q.prepare_qat(model, inplace=True)

# 2. Train normally — but the forward pass simulates INT8
for batch in loader:
    optimizer.zero_grad()
    out = model(batch.x)            # ← weights/activations fake-quantized in fwd
    loss = criterion(out, batch.y)
    loss.backward()                 # ← gradients flow through real FP32 weights
    optimizer.step()

# 3. Convert to actual INT8 model after training
model.eval()
int8_model = Q.convert(model.cpu(), inplace=False)
```

The trick: **forward pass uses FakeQuantize stubs that simulate INT8 rounding while keeping FP32 weights**. The optimizer updates the FP32 weights; gradients use the **straight-through estimator** (STE) to bypass the non-differentiable quantize-dequantize. Result: weights converge to a configuration that survives quantization.

## PTQ vs QAT — when to use which

| Method | Cost | Accuracy retention | When |
|---|---|---|---|
| **PTQ (Post-Training Quantization)** | One pass over a calibration set | Loses 0.2–2 dB on deep models | Default first attempt — cheap |
| **QAT (Quantization-Aware Training)** | Full training run | Recovers nearly all accuracy | When PTQ loss is unacceptable |
| **PTQ + a few QAT epochs** | Hybrid | Often within 0.05 dB of FP32 | Production sweet spot |

For [[paper-nrx-wiesmayr-2024]]'s real-time NRX: PTQ alone lost ~0.5 dB; the published Wiesmayr result uses **QAT during the final fine-tuning phase** to recover it.

## The straight-through estimator (the load-bearing idea)

Quantize-dequantize is non-differentiable (rounding). The forward pass:

$$\tilde w = \text{round}\!\left(\frac{w}{s}\right) \cdot s, \qquad s = \frac{w_{\max} - w_{\min}}{255}$$

The backward pass uses the **STE**: pretend the round is the identity, so $\partial \tilde w / \partial w = 1$ (or $1$ inside the quantization range, $0$ outside). This is mathematically a hack — but it works empirically and is what every modern QAT framework (PyTorch, TensorRT, ONNX-Runtime, TFLite) uses.

## Calibration sets — PTQ's other half

Whether you do PTQ or QAT, you eventually need to compute the per-tensor scale $s$. The **calibration set** is a few hundred representative inputs used to compute activation ranges.

| Calibrator | How it picks $s$ |
|---|---|
| **MinMax** | $s = (\max - \min) / 255$ |
| **Entropy** (TensorRT default) | $s$ that minimizes KL-divergence between FP32 and INT8 activation histograms |
| **Percentile** | $s$ from 99.9th percentile (clip outliers) |

> [!warning] Calibration-set composition matters
> If your calibration set is unrepresentative (e.g., only high-SNR samples for an NRX), the activation ranges are too narrow and INT8 saturates on real data. **Use a representative SNR sweep matching deployment conditions.**

## Why this matters / where it sits in the roadmap

- **Phase 4 M10–M11.** [[paper-nrx-wiesmayr-2024]] explicitly uses QAT to ship NRX in real-time; reproducing this paper without QAT loses the headline result.
- **NVIDIA-intern signal.** Knowing the QAT vs PTQ trade-off + STE is **specifically** the kind of deployment-side knowledge that distinguishes a researcher from someone who's actually shipped on hardware.
- **Cold-email talking point.** "I reproduced Wiesmayr 2024 NRX with PTQ-only, lost 0.4 dB BLER, then added QAT and recovered 0.35 dB" — concrete, technical, measurable.

## Common mistakes

- **Comparing QAT vs PTQ at different SNRs.** Both must be evaluated at matched operating points.
- **QAT without warm-starting from FP32.** Train FP32 to convergence first, then enable QAT for the last 10–20% of epochs. Cold-start QAT is unstable.
- **Calibration set leak.** Don't calibrate on test data; it inflates final BLER.
- **Quantizing the LDPC decoder.** Many decoders need FP16+ precision in their tanh / atanh ops. Mixed precision (FP32 decoder, INT8 NRX backbone) is the practical recipe.

## Related

- [[mixed-precision-training]] — sister concept; FP16/BF16 in training, INT8 in deployment.
- [[tensorrt]] — the production INT8 inference compiler that consumes QAT models.
- [[onnx]] — the export format that carries QAT scales/zero-points.
- [[neural-receiver]] — primary target for QAT.
- [[paper-nrx-wiesmayr-2024]] — the canonical wireless QAT reference.
- [[paper-sionna-research-kit-2025]] — Jetson deployment uses QAT-trained models.
- [[python-ml-wireless]]

## Practice
- **TODO (Phase 4 M10)** — Take a trained NRX checkpoint; run TensorRT PTQ with 500 calibration samples; measure BLER gap vs FP32. Then run 5 epochs of QAT; re-quantize; measure recovery. **The PTQ→QAT recovery delta is the cold-email number.**
