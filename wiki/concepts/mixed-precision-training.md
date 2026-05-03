---
title: Mixed-precision training (FP16 / BF16 / FP8)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - pytorch
  - training-hygiene
  - fp16
  - bf16
  - amp
  - phase-1
  - phase-2
sources:
  - "[[textbook-deep-learning-with-pytorch]]"
  - "[[paper-sionna-research-kit-2025]]"
created: 2026-05-01
updated: 2026-05-01
---

# Mixed-precision training (FP16 / BF16 / FP8)

## In one line
**Train with FP16 / BF16 / FP8 weights and activations to halve memory + ~2× speed up on modern GPUs (Tensor Cores), while keeping a small set of "loss-scale" tricks to prevent gradient underflow.** PyTorch's `torch.cuda.amp` makes this a 3-line change.

## Example first — PyTorch Automatic Mixed Precision (AMP)

```python
import torch
from torch.cuda.amp import autocast, GradScaler

model = MyModel().cuda()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
scaler = GradScaler()

for batch in loader:
    optimizer.zero_grad()
    with autocast(dtype=torch.float16):           # fwd in FP16
        out = model(batch)
        loss = criterion(out, batch.target)
    scaler.scale(loss).backward()                 # scaled loss bwd
    scaler.step(optimizer)                        # unscale + step
    scaler.update()
```

That's it. Same training loop, ~2× faster, ~50% less memory — for free on any Tensor-Core GPU (V100+, A100, H100, RTX 30+, Jetson Orin).

## The idea — three precision regimes

| Format | Range | Mantissa | When to use |
|---|---|---|---|
| **FP32** | $\pm 10^{38}$ | 23 bits | Default; never wrong |
| **FP16** | $\pm 65504$ | 10 bits | Fast on Tensor Cores; **needs loss scaling** |
| **BF16** | $\pm 10^{38}$ | 7 bits | A100+/H100/TPU; same range as FP32, no loss scaling needed |
| **FP8** | $\pm 448$ | 4 bits | H100+ only; aggressive, hurts most architectures |

**FP16's problem:** range is small ($10^{-5}$ to $10^4$). Gradients smaller than $10^{-5}$ underflow to zero. **Loss scaling** multiplies the loss by ~$2^{15}$ before backward, then divides gradients before the optimizer step — same final update, but gradients live in the FP16-representable range during backward.

**BF16 dodges the underflow problem** by keeping FP32's exponent range with a smaller mantissa. **The default for modern (2023+) deep learning** if your GPU supports it.

## Why it matters / where it sits in the roadmap

- **Phase 1 M3 deliverable.** [[python-ml-wireless]] M3: "CIFAR-10 ResNet-18 with AMP, W&B-logged." AMP **is mixed-precision training** — without this concept page, the M3 task is opaque.
- **Phase 2 M4–M6 reproductions.** All NRX / autoencoder / generative reproductions at scale need AMP for tractable training on consumer GPUs.
- **Phase 4 M10–M11 deployment.** [[paper-sionna-research-kit-2025]] uses **TensorRT INT8** (one step further than FP16) for Jetson deployment. Concept inheritance: FP32 → FP16/BF16 (training) → INT8 (inference).
- **Cold-email talking point.** "Trained NRX in BF16 on an RTX 4090 in $X$ hours, reproduced published BLER" — concrete numbers signal real practitioner.

## Common mistakes

- **Forgetting `GradScaler` for FP16.** Loss → NaN within hundreds of steps.
- **Using BF16 on hardware that doesn't support it.** Most pre-A100 GPUs don't have native BF16 — silently falls back to slow software paths.
- **Mixing FP16 + non-AMP-safe ops.** Some ops (especially custom CUDA kernels, log-softmax with extreme inputs) need FP32. Use `with autocast(): ... output.float()` to upcast manually.
- **Comparing BF16 vs FP16 results without verification.** They train almost identically on most tasks; **but** for reinforcement learning, BF16 is more stable; for high-precision regression, FP32 may still be needed.
- **Mixed-precision in evaluation.** AMP is a training optimization. For BLER/NMSE measurements at $10^{-3}$ precision, evaluate in FP32.

## Related

- [[textbook-deep-learning-with-pytorch]] — Stevens et al. covers AMP in Ch 5+.
- [[pytorch]] — the framework that makes AMP one-line.
- [[gradient-descent]], [[stochastic-gradient-descent]], [[adam-optimizer]] — what's being executed.
- [[paper-sionna-research-kit-2025]] — uses INT8 (TensorRT) for inference; FP16/BF16 for training.
- [[tensorrt]] + [[onnx]] — the inference-side cousins (INT8 quantization).
- [[python-ml-wireless]]

## Practice
- **TODO (Phase 1 M3)** — Train CIFAR-10 ResNet-18 twice: once FP32, once FP16+AMP. Compare wall-clock time, peak GPU memory, final test accuracy. **This is the M3 deliverable.**
