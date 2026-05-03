---
title: NVIDIA TensorRT
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - nvidia
  - inference-engine
  - gpu
  - phase-3
  - phase-4
sources:
  - "[[paper-sionna-research-kit-2025]]"
created: 2026-05-01
updated: 2026-05-01
---

# NVIDIA TensorRT

## In one line
**TensorRT is NVIDIA's GPU inference compiler — takes a trained ONNX/TF/PyTorch model, applies layer-fusion + INT8/FP16 quantization + kernel auto-tuning + memory-layout optimization, and emits a deployable engine that runs 5–10× faster than the unoptimized framework.**

## Example first

```python
import tensorrt as trt
import torch_tensorrt

# PyTorch model → TensorRT engine
model = NeuralReceiver(...)
trt_model = torch_tensorrt.compile(
    model,
    inputs=[torch_tensorrt.Input((1, 14, 256), dtype=torch.float16)],
    enabled_precisions={torch.float16},
)
trt_model.save("nrx.trt")

# Inference
output = trt_model(input_tensor)  # ~3-5x faster than vanilla PyTorch
```

This is the deployment path for the **NVIDIA Aerial neural receiver** in [[paper-sionna-research-kit-2025]] — Sionna trains in TensorFlow/Keras → exports to TensorRT → runs at slot timing on Jetson AGX Orin.

## The idea — what TensorRT does

| Optimization | What it does |
|---|---|
| **Layer fusion** | Merges adjacent ops (Conv+BN+ReLU → single CUDA kernel) |
| **Precision calibration** | FP32 → FP16 / INT8 / FP8 / INT4 with calibration sets |
| **Kernel auto-tuning** | Picks fastest CUDA kernel for the target GPU |
| **Memory layout** | Re-orders tensors to maximize coalesced reads |
| **Builder phase** | One-time, slow (minutes); produces a binary engine |
| **Runtime phase** | Fast, deterministic, no Python overhead |

The trade-off: **engine builds are GPU-specific** — an engine built for A100 won't run optimally on H100, and a Jetson Orin engine is different again. Production: build engines per deployment target.

## INT8 calibration workflow (the deployment-side detail)

INT8 quantization needs **per-tensor scales** $s$ such that $w_{\text{int8}} = \text{round}(w / s)$. TensorRT's calibration step computes these scales from a representative dataset.

```python
import tensorrt as trt

# 1. Define a calibrator (TensorRT's Entropy v2 is the standard)
class NRXCalibrator(trt.IInt8EntropyCalibrator2):
    def __init__(self, calibration_data, batch_size=32):
        super().__init__()
        self.batches = iter(calibration_data)  # representative SNR sweep
        self.batch_size = batch_size
        self.cache = "nrx_calibration.cache"

    def get_batch_size(self): return self.batch_size
    def get_batch(self, names):
        try:
            data = next(self.batches)
            return [int(data.data_ptr())]
        except StopIteration:
            return None
    def read_calibration_cache(self):
        if os.path.exists(self.cache):
            return open(self.cache, "rb").read()
    def write_calibration_cache(self, cache):
        open(self.cache, "wb").write(cache)

# 2. Build the INT8 engine
config = builder.create_builder_config()
config.set_flag(trt.BuilderFlag.INT8)
config.int8_calibrator = NRXCalibrator(calibration_data)
engine = builder.build_serialized_network(network, config)
```

**Three calibrator choices:**

| Calibrator | Picks scales by | When |
|---|---|---|
| `IInt8MinMaxCalibrator` | $s = (\max - \min) / 255$ | Simple; sensitive to outliers |
| **`IInt8EntropyCalibrator2`** | KL-divergence between FP32 and INT8 activation histograms | **TensorRT default — use this.** |
| `IInt8LegacyCalibrator` | Legacy entropy v1 | Don't — superseded |

**Per-tensor vs per-layer (per-channel) granularity:**
- **Per-tensor:** one $s$ for the whole tensor — fastest, lowest accuracy.
- **Per-channel** (weights only, activations remain per-tensor): one $s$ per output channel — slightly slower, recovers most of the FP32 accuracy. **Use per-channel for any deep model.**

> [!warning] Calibration-set composition matters
> An NRX calibrated only on high-SNR samples will saturate INT8 at low SNR. **Match the calibration SNR sweep to deployment conditions** — the same recipe [[paper-nrx-wiesmayr-2024]] uses.

**Verification step (do not skip):**
```bash
trtexec --onnx=nrx.onnx --int8 --calib=nrx_calibration.cache \
        --saveEngine=nrx-int8.trt --verbose
# Then evaluate on a held-out test set; compare BLER vs FP32 engine.
```

If post-INT8 BLER loses more than ~0.3 dB, **fall back to QAT** ([[quantization-aware-training]]) instead of pure PTQ.

## Why it matters / where it sits in the roadmap

- **Phase 4 M10–M11.** Any NVIDIA-internship deliverable that ships a model on hardware will use TensorRT. [[paper-sionna-research-kit-2025]] is the canonical example.
- **Latency unlock for AI-RAN.** 5G NR slot timing is ~1 ms; without TensorRT a Sionna-trained NRX is too slow for inline use.
- **Deployment-side knowledge.** NVIDIA-intern interview signal: knowing TensorRT distinguishes a researcher from someone who's actually shipped on NVIDIA hardware.

## Common mistakes
- **INT8 without calibration set.** Quantization without representative calibration gives bad accuracy.
- **Treating TensorRT as a framework.** It's a **compiler** — you train in PyTorch/TF, then compile.
- **Ignoring engine version drift.** TensorRT 9 → 10 broke API; engines are not forward-compatible.

## Related
- [[onnx]] — the **input format** TensorRT consumes; the universal training-to-deployment bridge.
- [[quantization-aware-training]] — when PTQ alone loses too much accuracy, train with simulated INT8 in the forward pass.
- [[mixed-precision-training]] — sister training-side concept.
- [[paper-sionna-research-kit-2025]] — TRT used to deploy Sionna-trained NRX.
- [[paper-nrx-wiesmayr-2024]] — uses QAT + TRT INT8 for the published real-time result.
- [[neural-receiver]] — primary deployment target on NVIDIA Aerial / Jetson.
- [[sionna]] — typical model source.
- [[python-ml-wireless]]
