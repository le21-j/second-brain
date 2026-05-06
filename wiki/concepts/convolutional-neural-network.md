---
title: Convolutional neural network (CNN)
type: concept
course:
  - "[[python-ml-wireless]]"
tags: [cnn, conv, dl, image-models, resnet, wireless]
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-04-23
updated: 2026-05-06
---

# Convolutional neural network (CNN)

## In one line
A neural network whose hidden layers apply **learned local filters** (small weight kernels) to their input — the same filter sweeps over all positions, so the network can recognize a pattern wherever it appears and uses orders of magnitude fewer parameters than a dense MLP would.

## Example first

Image classification (the canonical use):

```python
import torch.nn as nn

cnn = nn.Sequential(
    nn.Conv2d(3, 32, 3, padding=1),   # 3 input channels, 32 filters, 3x3
    nn.ReLU(),
    nn.MaxPool2d(2),                  # downsample 2x
    nn.Conv2d(32, 64, 3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(64 * 8 * 8, 10),        # CIFAR-10: 10 classes
)
```

The same `Conv2d(3,32,3)` filter is applied at every spatial location — so the feature "this $3\times 3$ pattern is an edge" is reusable across the image. For the wireless analog: replace the image $(H, W, 3)$ with a resource grid (freq, time, complex-as-2-channels), and you have a neural receiver's front end — see [[neural-receiver]].

## The idea

**Hubel & Wiesel 1959** (visual cortex), **LeCun 1989–1998** (LeNet), **Krizhevsky 2012** (AlexNet — 2012 ImageNet win that started the deep-learning era), **He 2015** (ResNet — residuals + 152-layer networks). The core insights:

1. **Local connectivity.** Each hidden unit depends only on a small local patch of its input — because in natural data (images, audio, time series) relevant features are local.
2. **Weight sharing.** The same filter weights are reused everywhere — translation equivariance, parameter efficiency, and inductive bias that matches natural data.
3. **Hierarchy via stacking.** Early filters learn edges; middle layers learn textures; late layers learn object parts. Empirically observed, though it's not a hard-coded inductive bias.
4. **Residual learning (ResNet).** Identity shortcuts let you train networks hundreds of layers deep — without them, optimization breaks down.

### Canonical blocks

| Block | What it does |
| --- | --- |
| `Conv2d(C_in, C_out, k, s, p)` | learned filter kernel |
| `BatchNorm2d` | normalize + learn affine per channel; stabilizes training |
| `ReLU` / `GELU` | activation |
| `MaxPool2d` / `AvgPool2d` | downsample |
| Skip connection (`x + f(x)`) | the ResNet innovation |
| Global average pooling | turn (C, H, W) into (C,) before the classifier |

### Famous architectures, in order

1. **LeNet-5 (1998)** — digit classification.
2. **AlexNet (2012)** — $5$ conv $+\,3$ FC; ReLU; dropout; GPU training. Started the modern era.
3. **VGG (2014)** — simple, all $3\times 3$ convs, very deep.
4. **GoogLeNet / Inception** — parallel conv paths.
5. **ResNet (2015)** — residual connections; $152$ layers. Still a common baseline.
6. **DenseNet** — every layer connects to every later layer.
7. **MobileNet (v1/v2/v3)** — depthwise separable convs for edge devices.
8. **EfficientNet (2019)** — compound scaling of width/depth/resolution.
9. **ConvNeXt (2022)** — modernized CNN competitive with Vision Transformers.

### Wireless applications

CNNs dominate wireless PHY-ML because channel matrices, CSI, spectrograms, and resource grids are natively 2D:
- **[[neural-receiver]]** — stacked residual CNNs over the (freq $\times$ time) resource grid.
- **[[csi-feedback]]** (CsiNet, CRNet, CLNet) — CNN autoencoders over angle-delay-domain CSI.
- **[[modulation-classification]]** (RadioML) — 1D or reshape-to-2D CNNs over I/Q.
- **[[beam-prediction]]** — CNN branches over RGB / LiDAR.

## Formal definition

A 2D convolution with kernel $\mathbf{W} \in \mathbb{R}^{k \times k \times C_\text{in}}$ and bias $b$:

$$
y_{i,j,m} = b_m + \sum_{c=1}^{C_\text{in}}\sum_{p=0}^{k-1}\sum_{q=0}^{k-1} W_{p,q,c,m}\, x_{i+p, j+q, c}
$$

for output channel $m$. Note "convolution" in the DL sense is really **cross-correlation** (no kernel flip) — a naming quirk that DSP folks immediately trip on. For actual signal-processing convolution (with flip), use `scipy.signal.convolve`.

## Why it matters / when you use it

- **Strong inductive bias for grid data.** CSI matrices, spectrograms, constellation diagrams — all 2D. CNNs are the first thing to try.
- **Parameter efficiency.** A $3\times 3$ kernel has $9$ params independent of input size — vs a fully connected layer's $O(N^2)$.
- **Compute efficiency.** Modern GPUs ship optimized convolution kernels (cuDNN); throughput is very good.
- **Inductive-bias stack for PHY-ML.** Virtually every published wireless-ML paper begins with a CNN baseline.

## Common mistakes

- **Mismatched input shape.** PyTorch is $(B, C, H, W)$; TensorFlow/Keras default is $(B, H, W, C)$. Frame-of-reference error ruins models.
- **Forgetting padding.** Without `padding`, each conv layer shrinks spatial dims; stacking many layers eats your resolution.
- **Applying BatchNorm before a small batch.** Batch norm is meaningless at batch size $2$. Use GroupNorm or LayerNorm instead.
- **Calling 2D convs on complex tensors without a dtype plan.** PyTorch's complex Conv2d is still a bit rough; many wireless codebases split into 2-channel real.

## Reading order (per roadmap)

1. Prince [[textbook-prince-understanding-deep-learning]] Ch 10–11.
2. Stanford CS231n (notes + Assignment 2 — "the single best exercise for your research goal").
3. Papers in chronological order: LeNet-5 $\to$ AlexNet $\to$ VGG $\to$ ResNet (arxiv:1512.03385) $\to$ DenseNet $\to$ MobileNetV2 $\to$ EfficientNet $\to$ ConvNeXt.
4. [[textbook-deep-learning-with-pytorch]] Ch 8 for the internals.

## Related
- [[transformer]]
- [[neural-receiver]]
- [[csi-feedback]]
- [[modulation-classification]]
- [[pytorch]]
- [[python-ml-wireless]]
