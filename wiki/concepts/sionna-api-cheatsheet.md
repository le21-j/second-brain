---
title: Sionna 2.x API cheatsheet
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - sionna
  - api
  - tensorflow
  - keras
  - phase-3
  - phase-4
sources:
  - "[[paper-sionna-2022]]"
  - "[[paper-sionna-research-kit-2025]]"
  - "[[paper-nrx-cammerer-2023]]"
created: 2026-05-01
updated: 2026-05-01
---

# Sionna 2.x API cheatsheet

## In one line
**The minimum Sionna 2.x API surface needed to assemble an end-to-end PUSCH training run** — channel models, OFDM resource grid, LDPC encoder/decoder, NRX-style receiver, training loop scaffold. Memorize the patterns once; recall under interview pressure.

> [!tip] How this page is meant to be used
> Not a deep API reference (the official docs at https://nvlabs.github.io/sionna/ are exhaustive). This is the **interview cheatsheet**: the 12 imports, the 6 typical objects, the 3 patterns that compose an end-to-end training run.

## The 12-line end-to-end PUSCH simulation

```python
import sionna.phy as phy
import tensorflow as tf

# 1. PUSCH configuration (38.214 TBS table baked in)
pusch_config = phy.pusch.PUSCHConfig(
    num_layers=1, mcs_index=14, num_resource_blocks=100,
    mapping_type="A", dmrs_additional_position=1,
)

# 2. Transmitter assembles {bits → CRC → LDPC → modulation → DM-RS → grid}
tx = phy.pusch.PUSCHTransmitter(pusch_config)

# 3. Channel — 3GPP TDL-C 300ns at 30 km/h
channel = phy.channel.tr38901.TDL("C", 300e-9, carrier_frequency=3.5e9, ut_velocity=30/3.6)

# 4. Receiver — LMMSE baseline (or your trained NRX)
rx = phy.pusch.PUSCHReceiver(pusch_config, channel_estimator="lmmse")

# 5. Forward pass: bits → tx → channel → rx → bits
bits = phy.bits.BinarySource()(shape=[batch_size, pusch_config.tb_size])
x_grid = tx(bits)
y_grid = channel([x_grid, no])  # `no` = noise variance
bits_hat = rx([y_grid, no])

# 6. Loss + backprop
loss = phy.losses.compute_ber(bits, bits_hat)
```

## The 6 objects an NRX reproduction touches

| Object | Module | Purpose |
|---|---|---|
| `PUSCHConfig` | `sionna.phy.pusch` | Wraps 38.214 — TBS, DM-RS, layer count, MCS. See [[5g-nr-pusch-structure]] |
| `PUSCHTransmitter` | `sionna.phy.pusch` | Assembles bits → grid (CRC + LDPC + modulation + DM-RS insertion) |
| `PUSCHReceiver` | `sionna.phy.pusch` | Channel estimation + demapping + LDPC decoding; **swap with NRX here** |
| `TDL` / `CDL` | `sionna.phy.channel.tr38901` | 3GPP standard channels |
| `RayTracingChannel` | `sionna.rt` | Site-specific channel (see [[sionna-rt]]) |
| `LDPC5GEncoder` / `LDPC5GDecoder` | `sionna.phy.fec.ldpc` | 38.212-compliant rate-matched LDPC |

## The 3 typical training-run shapes

### A. Train an NRX (Cammerer-style)
```python
class NeuralReceiver(tf.keras.Model):
    def __init__(self, config):
        super().__init__()
        self.cnn = tf.keras.Sequential([
            tf.keras.layers.Conv2D(64, 3, padding="same", activation="relu"),
            # ... ResNet blocks
        ])
        self.demapper = phy.mapping.Demapper("app", "qam", config.num_bits_per_symbol)
        self.ldpc_decoder = phy.fec.ldpc.LDPC5GDecoder(...)

    def call(self, y_grid):
        h_features = self.cnn(y_grid)
        llrs = self.demapper(h_features)
        bits_hat = self.ldpc_decoder(llrs)
        return bits_hat

model = NeuralReceiver(pusch_config)
model.compile(optimizer=tf.keras.optimizers.Adam(1e-3), loss="bce")
model.fit(dataset, epochs=100)
```

### B. Train an end-to-end autoencoder ([[paper-aitaoudia-hoydis-2020-ofdm]] style)
Same Sionna stack, but **replace `Demapper` with a learnable demapper module** and learn the mapper at the TX side too.

### C. Train a Sionna RT site-specific NRX ([[paper-diff-rt-calibration-2024]] companion)
Replace `tr38901.TDL` with `sionna.rt.RayTracingChannel(scene)`; the rest of the pipeline is unchanged. **This is the M10 capstone.**

## Patterns to memorize

### `tf.keras.layers.Layer` subclassing — the Sionna idiom
Every Sionna block is a Keras Layer. Memorize:

```python
class MyBlock(tf.keras.layers.Layer):
    def __init__(self, ...):
        super().__init__()
        # store config
    def build(self, input_shape):
        # lazy weight init — called on first forward pass
        self.w = self.add_weight(...)
    def call(self, inputs, training=None):
        # forward pass; check `training` for BN/dropout/QAT
        return outputs
```

### XLA compilation for speed
```python
@tf.function(jit_compile=True)
def train_step(batch):
    with tf.GradientTape() as tape:
        out = model(batch.x)
        loss = compute_loss(out, batch.y)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    return loss
```

XLA gives ~2× speedup on Sionna-style models. Required for tractable NRX training on consumer GPUs.

### Mixed precision (see [[mixed-precision-training]])
```python
from tensorflow.keras import mixed_precision
mixed_precision.set_global_policy("mixed_float16")
```
Two extra lines; cuts training time roughly in half on Tensor-Core GPUs.

## Sionna 0.x → 2.x breaking changes (the gotcha list)

| 0.x | 2.x | Notes |
|---|---|---|
| `sionna.OFDMResourceGrid` | `sionna.phy.ofdm.ResourceGrid` | Module reorganization |
| `RadioMaterial(name="concrete")` | `scene.radio_materials["itu_concrete"]` | Material accessor moved |
| `tf.complex64` everywhere | mixed: `complex64` for sample-level, `float32` for ML layers | Watch for dtype mismatches |
| `LDPC5GDecoder(num_iter=20)` | same — but the `cn_type` arg added | Default minsum vs offset-minsum |

> [!warning] Pin to the repo's `requirements.txt`
> The NRX repo and the Sionna Research Kit pin specific Sionna versions. Don't `pip install --upgrade sionna` mid-reproduction; the API drifts.

## Where to find more

- **Official tutorials** — https://nvlabs.github.io/sionna/tutorials/ — start with Part 1 (link-level basics) then Part 4 (custom layers).
- **Sionna 2 examples repo** — https://github.com/NVlabs/sionna — `examples/` directory has end-to-end notebooks.
- **NRX repo** — https://github.com/NVlabs/neural_rx — uses the API above; read it after the tutorials.

## Why this matters / where it sits in the roadmap

- **Phase 3 M7 NRX reproduction.** [[nrx-reproduction-walkthrough]] Stages 1–3 lean entirely on this API surface.
- **Phase 4 M10 site-specific NRX.** Same API + Sionna RT.
- **Cold-email signal.** Saying "I assembled a PUSCH end-to-end in 12 lines using Sionna 2.x" is concrete proof of fluency that beats any concept-level claim.

## Common mistakes

- **Confusing Sionna with Sionna RT.** [[sionna]] is the umbrella simulator; [[sionna-rt]] is one channel-model option inside it. Different APIs.
- **Mixing `sionna.phy.*` and the older top-level `sionna.*` imports.** 2.x reorganized; pick one and be consistent.
- **Calling `tf.complex64` operations in eager mode without GPU.** Falls back to slow CPU paths; profile if NRX training feels too slow.
- **Forgetting to set `tf.config.experimental.set_memory_growth(gpu, True)`.** Sionna grabs all GPU memory by default; can OOM other processes.

## Related
- [[sionna]] — umbrella concept page.
- [[sionna-rt]] — RT-specific API.
- [[neural-receiver]] — what you build with this API.
- [[5g-nr-pusch-structure]] — the standard the API encodes.
- [[mixed-precision-training]] — Sionna-side AMP.
- [[ldpc-codes]] — what `LDPC5GDecoder` decodes.
- [[paper-sionna-2022]], [[paper-sionna-rt-2023]] — the source papers.
- [[nrx-reproduction-walkthrough]] — the deliverable that uses every line above.
- [[python-ml-wireless]]
