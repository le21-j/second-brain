---
title: "Stevens, Antiga, Viehmann — Deep Learning with PyTorch"
type: summary
source_type: other
source_path: raw/textbook/deep-learning-with-pytorch.md
source_date: 2020
course:
  - "[[python-ml-wireless]]"
tags:
  - textbook
  - pytorch
  - phase-1
  - phase-2
  - reference-card-stub
created: 2026-05-01
updated: 2026-05-01
---

# Stevens, Antiga, Viehmann — Deep Learning with PyTorch

**Status:** stub — free PDF at https://www.manning.com/books/deep-learning-with-pytorch. Reference card at `raw/textbook/deep-learning-with-pytorch.md`.

## TL;DR
**The book that explains PyTorch internals best** — tensors, storage, strides, views, autograd. Roadmap calls out **chapters 1–8 specifically**. The reason this matters: when a Sionna tutorial hits a CUDA OOM or you need to profile GPU utilization, this book's memory model is what lets you debug it.

## Chapters that matter most (Ch 1–8)

| Ch | Topic | Why |
|---|---|---|
| 1–3 | Tensors + NumPy analogues | foundation for [[pytorch]] |
| 4 | Real-world tensor examples (time-series, text, images) | "how do I load my data" reference |
| 5 | **Autograd mechanics** | grounds [[autograd]] + [[backpropagation]] |
| 6–7 | First neural net + first CNN | grounds [[convolutional-neural-network]] |
| 8 | Convolutions in depth | CNN architecture |

Parts 2–3 (lung-cancer CT detector + deployment) are a real-world end-to-end project; useful as a reference but not roadmap-critical.

## Where it's used in the roadmap
- **Phase 1 M3** — Ch 1–8 alongside Karpathy Zero-to-Hero.
- **Phase 2 M4** — re-read Ch 5 (autograd) + Ch 8 (convolutions) before O'Shea-Hoydis autoencoder reproduction.

## Concepts grounded
- [[pytorch]], [[autograd]], [[backpropagation]]
- [[convolutional-neural-network]]
- [[gradient-descent]], [[stochastic-gradient-descent]]

## Related
- [[python-ml-wireless]]
- [[textbook-ml-with-pytorch-scikit-learn]] — Raschka companion (sklearn → PyTorch bridge)
- [[textbook-prince-understanding-deep-learning]] — theory
- [[textbook-d2l-dive-into-deep-learning]] — multi-framework code companion
