---
title: "Parr & Howard — The Matrix Calculus You Need For Deep Learning"
type: summary
source_type: textbook
source_path: raw/textbook/pdfs/parr-matrix-calculus.pdf
source_date: 2018
course:
  - "[[python-ml-wireless]]"
tags:
  - textbook
  - math
  - matrix-calculus
  - parr-howard
created: 2026-05-01
updated: 2026-05-01
---

# Parr & Howard — The Matrix Calculus You Need For Deep Learning

**Authors:** Terence Parr (USF) + Jeremy Howard (fast.ai). **arXiv:1802.01528** (2018). Free PDF; HTML version at https://explained.ai/matrix-calculus/. ~33 pages full HTML / 8-page arXiv condensed version mirrored at `raw/textbook/pdfs/parr-matrix-calculus.pdf`.

## TL;DR
A **one-sitting read** that gives you exactly the matrix-calculus you need to derive [[backpropagation]] from scratch — Jacobians, vector chain rule, broadcasting derivatives — without slogging through a full math text. The roadmap calls it out explicitly: "in one sitting, fill ML-specific calculus gaps."

## What it covers

| Section | Content |
|---|---|
| 1 | What is a derivative — the scalar refresher |
| 2 | Vector calculus and partial derivatives — the bridge from $\partial f / \partial x$ to $\nabla f$ |
| **3** | **Matrix calculus** — Jacobians of vector-valued functions of vector inputs |
| **4** | **Generating common rules** — single-element, sum, vector dot product, vector reductions |
| **5** | **Vector chain rule** — the heart of backprop, derived element-by-element first then matrix-form |
| 6 | **Gradient of the neuron activation** — applying the chain rule to a single dense neuron |
| 7 | **Gradient of the neural network loss function** — full backprop derivation for a 2-layer MLP |
| App | Notation table (numerator vs. denominator layout — the source of all confusion) |

## Why it's load-bearing for the roadmap

> "Parr & Howard 'The Matrix Calculus You Need For Deep Learning' in one sitting; fill ML-specific gaps in your DSP-trained calculus." — roadmap §3.

Two reasons:

1. **Backprop is just the chain rule, repeatedly.** [[backpropagation]] needs only the vector chain rule + broadcasting awareness. This paper presents both with worked numerical examples — exactly the example-first style this wiki demands.
2. **Notation hygiene.** The single most common reason students stall on backprop derivations is **layout convention** (numerator vs. denominator) — the appendix here explicitly addresses both, so you can read other sources without confusion.

## Roadmap reading order

Per [[python-ml-wireless]]:
- **Phase 1 M3 (Jul 2026):** Read end-to-end **before** starting Karpathy's micrograd episode of *Zero to Hero*. The combo (Parr math → Karpathy code) is the fastest path to a working mental model of autograd.

## Concepts grounded by this textbook

**Already exists in the wiki:**
- [[backpropagation]] — Sections 5–7 are the cleanest written derivation. Will cross-link.
- [[autograd]] — Section 3 explains why every modern framework uses Jacobian-vector products.

**To be created from this** (low priority — Prince UDL Ch 7 + Karpathy videos cover the same ground):
- jacobian-matrix
- vector-chain-rule

## Worked examples worth remembering
- **§5 chain rule for $z = w \cdot x + b$, $a = \sigma(z)$, $L = (a-y)^2$** — the canonical 2-layer MLP backprop derivation done element-by-element AND matrix-form. Memorize this.
- **§7 final answer:** $\partial L / \partial \mathbf{W} = \delta \otimes \mathbf{x}^\top$ — the outer-product form that makes vectorized GPU implementation efficient.

## Questions this source raises (open)
- **Tensor calculus** (3D and beyond) is barely touched — for that, Bishop PRML Ch 1 appendix or Prince Ch 7 are better.
- **Higher-order derivatives** (Hessians, Fisher information) aren't covered — for natural gradient methods or Newton's method, supplement with Boyd Convex Optimization Ch 9.

## Related
- [[python-ml-wireless]] — the course page; Phase 1 read.
- [[backpropagation]] — wiki concept page.
- [[autograd]] — wiki concept page.
- [[textbook-prince-understanding-deep-learning]] — Prince Ch 7 covers the same ground at book-length.
