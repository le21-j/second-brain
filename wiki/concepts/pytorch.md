---
title: PyTorch
type: concept
course: [[python-ml-wireless]]
tags: [pytorch, dl-framework, python, sionna, autograd]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# PyTorch

## In one line
An autograd-equipped tensor library for Python — feels like NumPy, runs on GPU, records every operation into a graph so `loss.backward()` computes gradients for you — and is the primary framework for modern deep-learning research.

## Example first

Train a 2-layer MLP on random data. **This snippet is the whole PyTorch mental model in 10 lines.**

```python
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(10, 32), nn.ReLU(), nn.Linear(32, 1))
opt   = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

for epoch in range(100):
    x = torch.randn(128, 10)
    y = torch.randn(128, 1)
    y_hat = model(x)                 # forward
    loss = loss_fn(y_hat, y)         # scalar tensor
    opt.zero_grad()
    loss.backward()                  # autograd walks the graph
    opt.step()                       # SGD step
```

Every tensor remembers what it was computed from; `.backward()` walks the graph backwards computing gradients via chain rule (see [[backpropagation]]); the optimizer steps those gradients into the parameters; `.zero_grad()` clears the accumulated gradients for the next step. That's 90% of PyTorch.

## The idea

PyTorch (Meta AI Research, open-sourced 2017, LF AI Foundation since 2022) combines:

1. **NumPy-like tensors** — same indexing rules, same broadcasting, same vectorized ops. Easy on-ramp for anyone with NumPy ([[numpy-vectorization]]).
2. **GPU acceleration** — `.to("cuda")` moves a tensor to GPU; ops dispatch to CUDA kernels.
3. **Define-by-run autograd** — the computational graph is built dynamically as you run forward code. Contrast with TensorFlow 1.x's static graphs. This is why you can use Python control flow (`for`, `if`) directly in a model.
4. **`nn.Module` hierarchy** — reusable, composable layer definitions with automatic parameter tracking.
5. **Optimizer registry** — SGD, Adam, AdamW, LAMB, etc., all with the same API.

### Components that matter for PHY-ML

| Building block | Purpose |
| --- | --- |
| `torch.tensor` | n-dim array |
| `torch.nn.Module` | base class for layers/models |
| `torch.nn.Linear` / `Conv1d` / `Conv2d` / `MultiheadAttention` | standard layers |
| `torch.optim.Adam` / `AdamW` | optimizers |
| `torch.nn.functional` | stateless versions (`F.relu`, `F.cross_entropy`) |
| `torch.autograd.grad` | explicit gradient computation |
| `torch.utils.data.Dataset` / `DataLoader` | data loading |
| `torch.cuda.amp.autocast` | mixed-precision FP16/BF16 |
| `torch.compile` | graph-capture + AOT compilation (PyTorch 2.0+) |
| `torch.distributed` (DDP, FSDP) | multi-GPU training |

### The Lightning wrapper

**PyTorch Lightning** (https://lightning.ai/docs/pytorch/) separates *research code* (forward pass, loss) from *engineering code* (device moves, checkpointing, distributed training). In practice you subclass `LightningModule`, implement `training_step` / `validation_step`, and Lightning handles the rest. The roadmap treats Lightning as the expected framework for serious projects.

### Complex tensors (critical for RF work)

PyTorch has first-class **complex dtype** support since 1.8: `torch.cfloat`, `torch.cdouble`. FFTs, matrix ops, autograd all work. This matters for PHY-ML because a lot of signal-processing math is genuinely complex-valued. Early wireless-ML code (pre-2020) often flattened complex as 2-channel real because the framework didn't support complex; modern code should use complex tensors directly.

## Formal definition — the autograd graph

For each tensor created with `requires_grad=True`, PyTorch records a **dynamic acyclic graph** of operations. When `loss.backward()` is called, PyTorch walks the graph from the loss backwards, applying the chain rule at each node. Gradients accumulate into `.grad` attributes of the leaf tensors.

`torch.no_grad()` disables graph recording (for inference, saving memory).
`tensor.detach()` removes a tensor from the graph (for gradient stopping).

## Why it matters / when you use it

- **Research default.** Every wireless-ML paper in 2024–2026 publishes PyTorch code (a few stragglers ship TensorFlow for legacy Sionna 1.x).
- **Sionna 2.x is PyTorch-native** — this is precisely why the roadmap bets on PyTorch.
- **Interoperates with JAX, NumPy, ONNX** via `dlpack`/ONNX export.

## Common mistakes

- **Forgetting `zero_grad()`.** Gradients accumulate across `.backward()` calls. Without `zero_grad()`, you get ghost gradients from previous steps.
- **Calling `.item()` in an inner loop.** It forces a GPU $\to$ CPU sync — kills throughput.
- **Mismatched dtype/device.** A cpu tensor and a cuda tensor can't be combined; a float16 and float32 can (with implicit promotion) but silently costs you speed.
- **Training mode vs eval mode.** Dropout and BatchNorm behave differently. Always `model.train()` / `model.eval()` at the right time.
- **Not using `torch.compile` in 2026.** On a recent GPU, `torch.compile(model)` often gives $1.5$–$2\times$ speedups; roadmap-era code should default to it.

## Research ties / reading order

1. PyTorch 60 Minute Blitz — official tutorial.
2. [[deep-learning-with-pytorch]] Ch 1–8 — Stevens/Antiga/Viehmann, PyTorch internals.
3. Daniel Bourke's `learnpytorch.io`.
4. Sebastian Raschka's "PyTorch in One Hour" for a refresher.
5. [Karpathy Zero-to-Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) — watch all episodes.

## Related
- [[autograd]]
- [[backpropagation]]
- [[numpy-vectorization]]
- [[sionna]] — built on PyTorch from 2.x
- [[deep-learning-with-pytorch]]
- [[ml-with-pytorch-scikit-learn]]
- [[python-ml-wireless]]
