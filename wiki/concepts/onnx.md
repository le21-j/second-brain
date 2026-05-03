---
title: ONNX (Open Neural Network Exchange)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - ml-deployment
  - onnx
  - tensorrt
  - interoperability
  - phase-3
  - phase-4
sources:
  - "[[paper-sionna-research-kit-2025]]"
created: 2026-05-01
updated: 2026-05-01
---

# ONNX (Open Neural Network Exchange)

## In one line
**ONNX is the cross-framework "lingua franca" for trained neural networks** — a serialized graph format that PyTorch / TensorFlow / Keras / JAX can all export to, and that deployment runtimes ([[tensorrt|TensorRT]], ONNX Runtime, CoreML, OpenVINO) can all consume. **The bridge between training and shipping.**

## Example first

```python
import torch
import torch.onnx

model = NeuralReceiver(...)
model.eval()
dummy_input = torch.randn(1, 14, 256)  # match your inference shape
torch.onnx.export(
    model,
    dummy_input,
    "nrx.onnx",
    opset_version=17,
    input_names=["rx_grid"],
    output_names=["llrs"],
    dynamic_axes={"rx_grid": {0: "batch"}, "llrs": {0: "batch"}},
)
```

Now `nrx.onnx` is consumable by:
- **TensorRT** — `trtexec --onnx=nrx.onnx --fp16 --saveEngine=nrx.trt`
- **ONNX Runtime** — `onnxruntime-gpu` for direct CPU/GPU inference.
- **TFLite** — via converter (mobile deployment).

Same model, multiple deployment targets. **This is exactly the path the [[paper-sionna-research-kit-2025]] testbed uses** — Sionna trains in TF/Keras, exports to ONNX, compiles via TensorRT for the Jetson Orin.

## The idea

Training frameworks are optimized for **flexibility** (autograd, dynamic shapes, eager mode). Inference runtimes are optimized for **speed** (kernel fusion, quantization, fixed shapes). ONNX is the **handoff format**.

The graph is a list of operators (Conv, MatMul, ReLU, Attention, ...) with versioning ("opset"). Operators are standardized; runtimes implement them efficiently.

## Why it matters / where it sits in the roadmap

- **Phase 3 → 4 deployment chain.** Any wireless ML model that gets shipped to NVIDIA Aerial / Jetson / a 5G testbed goes through ONNX.
- **NVIDIA-intern signal.** Mentioning the ONNX → TensorRT pipeline in an interview signals you've actually deployed, not just trained.
- **Sibling to [[tensorrt]].** ONNX is the **input**; TensorRT is the **compiler**.

## Common mistakes
- **Opset mismatch.** PyTorch exports at the opset version you specify; the runtime needs to support it. Check both sides.
- **Dynamic shapes not declared.** Without `dynamic_axes`, the exported graph is fixed at `dummy_input`'s shape — re-shaping at inference fails.
- **Custom CUDA ops.** If your model has custom CUDA layers, ONNX export fails. Either reimplement in standard ops or write a TensorRT plugin.
- **Treating ONNX as a runtime.** ONNX is a **format**; ONNX Runtime is one implementation. Saying "I deployed via ONNX" without naming the runtime is ambiguous.

## Related
- [[tensorrt]] — the most common consumer of ONNX-exported models.
- [[paper-sionna-research-kit-2025]] — uses ONNX → TensorRT for the Jetson NRX.
- [[neural-receiver]] — natural deployment target.
- [[pytorch]] — most common producer.
- [[python-ml-wireless]]
