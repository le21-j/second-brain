---
title: "Chollet — Deep Learning with Python (2nd ed.)"
type: summary
source_type: other
source_path: raw/textbook/deep-learning-with-python-chollet.md
source_date: 2021
course:
  - "[[python-ml-wireless]]"
tags:
  - textbook
  - tensorflow
  - keras
  - chollet
  - sionna
  - phase-2
  - reference-card-stub
created: 2026-05-01
updated: 2026-05-01
---

# Chollet — Deep Learning with Python (2nd ed.)

**Status:** stub — paid Manning book; PDF not in repo. Reference card at `raw/textbook/deep-learning-with-python-chollet.md`.

## TL;DR
**The authoritative TensorFlow/Keras source — written by Keras's creator.** Roadmap target is **working competence, not expertise** (~25–35 hours total). Critical because **Sionna 1.x is built on Keras** and a large body of existing wireless-ML code is still TensorFlow.

## Chapters that matter (Ch 3, 7, 9 + 11)

| Ch | Topic | Why |
|---|---|---|
| 2 | Math of NNs (tensors, gradient descent) | TF / Keras lens on familiar territory |
| 3 | Intro to Keras + TensorFlow | the API basics |
| 7 | **Working with Keras** | **`tf.keras.layers.Layer` subclassing — the pattern every Sionna block uses** |
| 9 | Computer vision advanced (ResNet, Xception, detection) | reference |
| 11 | Deep learning for text (Transformers, BERT) | TensorFlow-side transformer reference |

## Sionna API memorization target

Every Sionna block follows this Keras pattern (memorize):
```python
class MyLayer(tf.keras.layers.Layer):
    def __init__(self, ...): ...
    def build(self, input_shape): ...   # lazy weight init
    def call(self, inputs, training=None): ...   # forward pass
```

## Where it's used in the roadmap
- **Phase 2 M6** — TensorFlow/Keras crash course (~25–35 h budget) before Phase 3 Sionna work.
- **Phase 3 M7+** — re-reference Ch 7 when modifying Sionna NRX layers.

## Concepts grounded
- [[transformer]] (Ch 11)
- [[convolutional-neural-network]] (Ch 9)
- [[sionna]] — every Sionna block is a `tf.keras.layers.Layer`

## Related
- [[python-ml-wireless]]
- [[chollet]] — author + Keras creator
- [[sionna]]
- [[textbook-prince-understanding-deep-learning]] — companion theory book
- [[paper-sionna-2022]] — uses every Keras pattern Ch 7 teaches
