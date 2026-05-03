---
title: "Prince — Understanding Deep Learning (UDL)"
type: summary
source_type: textbook
source_path: raw/textbook/pdfs/prince-udl.pdf
source_date: 2026-02-09
course:
  - "[[python-ml-wireless]]"
tags:
  - textbook
  - deep-learning
  - prince
  - primary-text
created: 2026-05-01
updated: 2026-05-01
---

# Prince — Understanding Deep Learning

**Author:** Simon J.D. Prince (Honorary Professor, University of Bath; ex-Borealis AI). **MIT Press, December 2023**; free PDF (CC BY-NC-ND) at https://udlbook.github.io/udlbook/. **PDF version v5.0.3 dated 2026-02-09 mirrored locally at `raw/textbook/pdfs/prince-udl.pdf`.** ~21 chapters, ~600 pages.

## TL;DR
The roadmap's **primary deep-learning textbook** ([[python-ml-wireless]] Phase 1 Month 4 → Phase 2 end). Prince trades Goodfellow's encyclopedic theory for the clearest pedagogical figures available — the chapters on transformers (Ch 12), diffusion (Ch 18), and CNNs (Ch 10) are the most-readable treatments in any current text. Every chapter pairs with an open-access Jupyter notebook in the udlbook repo.

## Confirmed table of contents

| Ch | Title | Roadmap relevance |
|---|---|---|
| 1 | Introduction | overview |
| 2 | Supervised learning | foundation |
| 3 | Shallow neural networks | foundation |
| 4 | Deep neural networks | foundation |
| **5** | **Loss functions** | grounds [[mse-loss]], [[cross-entropy-loss]], maximum-likelihood framing |
| **6** | **Fitting models** | grounds [[gradient-descent]], [[stochastic-gradient-descent]], momentum, [[adam-optimizer]] |
| 7 | Gradients and initialization | grounds [[backpropagation]], parameter init |
| 8 | Measuring performance | grounds [[overfitting-bias-variance]], double descent |
| **9** | **Regularization** | grounds [[regularization]], [[dropout]] |
| **10** | **Convolutional networks** | grounds [[convolutional-neural-network]] — best CNN exposition in any book |
| 11 | Residual networks | grounds [[batch-normalization]], skip connections |
| **12** | **Transformers** | grounds [[transformer]], [[attention-mechanism]] — clearest transformer treatment available |
| 13 | Graph neural networks | grounds [[graph-neural-network]] |
| 14 | Unsupervised learning | overview |
| 15 | Generative adversarial networks | grounds [[generative-adversarial-network]] |
| 16 | Normalizing flows | advanced generative |
| 17 | Variational autoencoders | grounds [[variational-autoencoder]] |
| **18** | **Diffusion models** | grounds [[diffusion-model]] — Lilian Weng's blog + this chapter is the canonical pair |
| 19 | Reinforcement learning | grounds [[reinforcement-learning]] (companion to Sutton-Barto for DL focus) |
| 20 | Why does deep learning work? | DL theory survey |
| 21 | Deep learning and ethics | optional |

## Roadmap reading order

Per [[python-ml-wireless]] Month-by-month plan:
- **M3 (Jul 2026):** Ch 1–4 (foundations) alongside Karpathy Zero-to-Hero.
- **M4 (Aug 2026):** Ch 5–9 (loss → SGD → backprop → regularization). This is the **non-negotiable foundations block**.
- **M4 (Aug 2026):** Ch 10–11 (CNNs + ResNets) ↔ CIFAR-10 ResNet-18 deliverable.
- **M5 (Sep 2026):** Ch 12 (transformers) ↔ RadioML modulation classification deliverable.
- **M6 (Oct 2026):** Ch 14–18 (generative models) ↔ CsiNet reproduction.
- **M9–M11 (Jan–Mar 2027):** Ch 13 (GNNs) ↔ neural decoder / GNN-BP project.

## Why it's load-bearing

> "The modern successor to Goodfellow et al., with the best pedagogical figures available. **This is your main DL book.**" — roadmap §3.

Prince spent years iterating the figures — readers consistently report concepts clicking in Prince that Goodfellow didn't. The book is also actively maintained (v5.0.3 is from Feb 2026 — the latest update post-MIT-Press release adds three chapters of corrections + new diffusion-model material).

## Concepts grounded by this textbook

**Already exist in the wiki, will be cross-linked to this summary as their primary source:**
- [[backpropagation]], [[autograd]], [[transformer]], [[attention-mechanism]], [[convolutional-neural-network]], [[variational-autoencoder]], [[generative-adversarial-network]], [[diffusion-model]], [[graph-neural-network]], [[reinforcement-learning]], [[relu]]

**Created in the 2026-05-01 foundational-pages sprint** (chapter map → wiki page):
- [[gradient-descent]] — Ch 6.1
- [[stochastic-gradient-descent]] — Ch 6.2
- [[adam-optimizer]] — Ch 6.4
- [[mse-loss]] — Ch 5.3
- [[cross-entropy-loss]] — Ch 5.7
- [[softmax]] — Ch 5.5
- [[regularization]] — Ch 9
- [[dropout]] — Ch 9.1
- [[batch-normalization]] — Ch 11.4
- [[overfitting-bias-variance]] — Ch 8.2

## Companion notebooks
Every chapter has a Jupyter notebook in https://github.com/udlbook/udlbook/tree/main/Notebooks. These are the practical anchor — Prince explains the concept; the notebook makes it run. **For Jayden's example-first learning style, run the notebook FIRST, then read the chapter.**

## Worked examples worth remembering
- **Ch 3 universal approximation theorem** (single hidden layer can approximate any continuous function) — sets up why depth helps.
- **Ch 6 Adam derivation** — why bias-correction matters in early steps.
- **Ch 12 attention as kernel-weighted lookup** — the framing that makes attention click.

## Questions this source raises (open)
- Section 12.9 ("Transformers for long sequences") covers FlashAttention only briefly — want a deeper dive.
- Ch 19 RL is shallow vs. Sutton-Barto — use Sutton-Barto as primary, Prince as DL-flavored companion.

## Related
- [[python-ml-wireless]] — the course page driving the reading order.
- [[textbook-d2l-dive-into-deep-learning]] — code-first companion (read chapter in Prince → run code in d2l).
- [[textbook-goodfellow-deep-learning]] — older theoretical reference.
- [[textbook-mackay-itila]] — information-theory grounding for Ch 5 loss-as-likelihood framing.
- [[prince]] — author page.
