---
title: "Goodfellow, Bengio, Courville — Deep Learning"
type: summary
source_type: other
source_path: raw/textbook/goodfellow-deep-learning.md
source_date: 2016
course:
  - "[[python-ml-wireless]]"
tags:
  - textbook
  - dl
  - goodfellow
  - reference
  - reference-card-stub
created: 2026-05-01
updated: 2026-05-01
---

# Goodfellow, Bengio, Courville — Deep Learning

**Status:** stub — HTML free at https://www.deeplearningbook.org/. Reference card at `raw/textbook/goodfellow-deep-learning.md`.

## TL;DR
**The "old testament" of deep learning** — historically the first comprehensive DL textbook (2016). Pre-transformer, but **still the clearest exposition of theoretical foundations** (bias-variance, optimization theory, regularization theory, autoencoders). Use as reference when [[textbook-prince-understanding-deep-learning]] is too modern or [[textbook-bishop-prml]] is too probabilistic.

## Chapters that matter most

| Ch | Topic | Replacement / status |
|---|---|---|
| 5 | ML basics | bias-variance theory; **complementary to Prince** |
| 6 | Feedforward networks | canonical reference |
| 7 | Regularization (L1/L2, dropout, batch norm) | grounds [[regularization]], [[dropout]], [[batch-normalization]] |
| 8 | Optimization for DL | grounds [[gradient-descent]], [[stochastic-gradient-descent]], [[adam-optimizer]] |
| 9 | CNNs | theoretical motivation; pair with Prince Ch 10 |
| 14–15 | Autoencoders + representation learning | **precursor to modern self-supervised** (LWM, BERT) |

## What's dated (don't read for these)
- **No transformers** (book predates 2017).
- **No diffusion models.**
- **GAN treatment** is the original 2014 take, now superseded by Prince Ch 14–15.

## Where it's used in the roadmap
**Reference, not linear read.** Pull Ch 5/6/7/8 when wanting first-principles bias-variance / SGD / regularization theory.

## Concepts grounded
- [[regularization]], [[dropout]], [[batch-normalization]], [[overfitting-bias-variance]]
- [[gradient-descent]], [[stochastic-gradient-descent]], [[adam-optimizer]]

## Related
- [[python-ml-wireless]]
- [[goodfellow]] — author
- [[textbook-prince-understanding-deep-learning]] — modern DL replacement (transformers, diffusion)
- [[textbook-d2l-dive-into-deep-learning]] — code-first companion
