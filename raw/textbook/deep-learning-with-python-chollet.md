# Deep Learning with Python (2nd ed.) — François Chollet

**Category:** TensorFlow / Keras (authoritative source)
**Status:** paid book — not yet in repo
**Publisher:** Manning, 2021
**Author:** François Chollet (creator of Keras; Google Research until 2024)
**Roadmap phase:** Phase 2 Month 6 — TensorFlow/Keras crash course

## Topic coverage
- Ch 2: Math of neural networks (tensors, gradient descent).
- Ch 3: Intro to Keras and TensorFlow.
- Ch 7: Working with Keras (Functional API, custom layers, custom training loops).
- Ch 9: Computer vision advanced (ResNet, Xception, object detection).
- Ch 11: Deep learning for text (Transformers, BERT).

## Why it's on the roadmap
Sionna 1.x is built on Keras, and a large body of existing wireless-ML code is still TensorFlow. You need **working competence, not expertise**. Chollet is the authoritative voice because he wrote Keras.

## What the roadmap says to focus on
> "Chapters 3, 7, and 9 cover exactly what you need for Sionna."
> "Budget ~25–35 hours total."

**Chapter 7** is especially important because `tf.keras.layers.Layer` subclassing is how every Sionna block is written. Memorize the pattern:
```python
class MyLayer(tf.keras.layers.Layer):
    def __init__(self, ...): ...
    def build(self, input_shape): ...  # lazy weight init
    def call(self, inputs, training=None): ...  # forward pass
```

## Related wiki pages
- [[python-ml-wireless]]
- [[sionna]]
- [[francois-chollet]]
