---
title: Sionna RT (differentiable ray tracer)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - sionna
  - ray-tracing
  - nvidia
  - mitsuba
  - differentiable-simulation
  - phase-3
  - phase-4
sources:
  - "[[paper-sionna-rt-2023]]"
  - "[[paper-diff-rt-calibration-2024]]"
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-05-01
updated: 2026-05-01
---

# Sionna RT (differentiable ray tracer)

## In one line
**Sionna RT is the ray-tracing module of NVIDIA's [[sionna]] — built on Mitsuba 3, GPU-accelerated, and differentiable end-to-end so you can backprop from a measured CFR through the ray-tracer to material properties / antenna patterns / scattering coefficients.**

## Example first

**Indoor 28-GHz path-loss prediction with a learnable concrete material.**

```python
import sionna.rt as rt
import tensorflow as tf

scene = rt.load_scene("munich.xml")  # OpenStreetMap-derived
scene.tx_array = rt.PlanarArray(num_rows=4, num_cols=4, vertical_spacing=0.5, horizontal_spacing=0.5, pattern="iso", polarization="V")
scene.rx_array = rt.PlanarArray(num_rows=1, num_cols=1, vertical_spacing=0.5, horizontal_spacing=0.5, pattern="iso", polarization="V")

# Make concrete's permittivity trainable
# (verify exact API against your installed Sionna version — the radio-material
# accessor moved between 0.18 / 0.19 / 1.x; the canonical 1.x form is below)
concrete = scene.radio_materials["itu_concrete"]
concrete.relative_permittivity = tf.Variable(5.31, trainable=True)

# Compute paths + CFR — both are differentiable wrt concrete.relative_permittivity
paths = scene.compute_paths(max_depth=3, num_samples=int(1e6))
cfr = paths.cfr(frequencies=tf.linspace(28e9, 28.4e9, 64))

# Now optimize concrete.relative_permittivity to match measured CFR
# (this is exactly what paper-diff-rt-calibration-2024 does)
```

The whole pipeline — geometry → ray launching → path tracing → field computation → CFR — is wrapped in TensorFlow's automatic differentiation. **You can train a ray tracer like a neural network** and that's exactly the [[paper-diff-rt-calibration-2024]] thesis.

## The idea

Classical ray tracers (Wireless InSite, Remcom etc.) are non-differentiable black boxes — given a scene + materials, they output channels. Sionna RT inverts the relationship: **anything in the scene description can be a TensorFlow Variable**, including:
- **Material parameters** ($\epsilon_r, \sigma$, scattering coefficient $S$, cross-pol ratio $K_x$)
- **Antenna patterns** (spherical-harmonics expansion, polarization)
- **Scattering distributions** (Lambertian / directive parametric)
- **Even the geometry itself** (vertex positions, with Mitsuba 3's diff-rendering primitives)

Because everything is a tensor, gradient-based learning is the natural calibration / inverse-problem method.

## Formal anatomy

A Sionna-RT simulation has three layers:

| Layer | What it does | Backend |
|---|---|---|
| **Geometry** | Triangle mesh of the scene; XML or `.ply` import | Mitsuba 3 |
| **Ray engine** | Launches rays, intersects, tracks reflections / refractions / scattering / diffraction up to `max_depth` | Custom CUDA (Mitsuba) |
| **Field engine** | For each path, applies antenna pattern + material reflection coefficient + Friis spreading + polarization rotation; coherent sum to CFR | TensorFlow ops |

The top-level user-facing API:
```python
scene = rt.load_scene(...)              # geometry
paths = scene.compute_paths(...)        # ray tracing
cfr = paths.cfr(frequencies)            # field computation → CFR
cir = paths.cir()                       # → CIR
```

## Why it matters / where it sits in the roadmap

- **Phase 4 M10 capstone** — [[python-ml-wireless]] explicitly calls for "site-specific neural receiver in Sionna RT — custom OSM scene." Sionna RT is the **engine** for that work.
- **Direct cold-email vocabulary.** Sionna RT is what Hoydis / Cammerer / Aït Aoudia ship and maintain — every paper of theirs since 2023 uses it. Talking about Sionna without distinguishing **the link-level simulator** ([[sionna]]) from **the differentiable ray tracer** signals lack of familiarity.
- **The differentiator vs. classical RT.** Site-specific channel modeling for digital twins is the [[wireless-digital-twin]] thesis, and Sionna RT is the only open-source differentiable RT — putting it at the center of the NVIDIA-Wi-Lab intersection.
- **Foundation for [[paper-diff-rt-calibration-2024]] reproduction** (the **single highest-leverage Phase 4 NVIDIA portfolio item**).

## Common mistakes

- **Confusing Sionna with Sionna RT.** [[sionna]] is the link-level simulator (transmitter / channel / receiver — works with any channel model, including 3GPP TDL). **Sionna RT** is one of several channel models that can feed into Sionna. Only Sionna RT does ray tracing.
- **`max_depth` too high.** Each bounce roughly multiplies compute by N where N is the number of triangles a ray can hit. `max_depth=3` is usually sufficient indoors; `max_depth=5` for outdoor; higher mostly adds noise via low-energy paths.
- **Mixing TF1 graph mode with diff-RT.** Sionna RT requires TF2 eager (or `@tf.function`-wrapped). Classical Keras-1 patterns break the autograd.
- **Ignoring scattering.** Default materials in Sionna RT have scattering disabled. **Real indoor channels need scattering on** for accurate delay-spread; turn it on with `material.scattering_coefficient = 0.5` or via the calibration pipeline.

## Related

- [[sionna]] — the umbrella simulator. Sionna RT is one channel-model option inside it.
- [[paper-sionna-rt-2023]] — the Sionna RT paper.
- [[paper-diff-rt-calibration-2024]] — the calibration method paper; uses Sionna RT.
- [[differentiable-ray-tracing]] — broader concept page.
- [[wireless-digital-twin]] — Sionna RT is the simulation backbone of digital-twin networks.
- [[nvidia-aodt]] — NVIDIA's Aerial Omniverse Digital Twin product, the productized cousin.
- [[deepmimo]] — Wi-Lab's ray-traced dataset can be imported via `dm.convert()` from Sionna RT scenes.
- [[paper-sionna-research-kit-2025]] — uses Sionna RT for site-specific NRX training in the Jetson testbed.
- [[paper-luo-dt-csi-feedback-2025]] — uses Sionna RT for site-specific digital-twin CSI training data.
- [[hoydis]], [[cammerer]], [[aitaoudia]] — the Sionna RT trio at NVIDIA.

## Practice
- **TODO** — Phase 3 M7: walk through Sionna RT Tutorial Part 4 (calibration); reproduce a simple indoor scene and compute CFR. Defer to Nov 2026.
