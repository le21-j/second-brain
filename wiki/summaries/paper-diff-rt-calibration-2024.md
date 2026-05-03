---
title: "Hoydis et al. 2024 — Learning Radio Environments by Differentiable Ray Tracing"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/diff-rt-calibration-2024.pdf
source_date: 2024
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - sionna-rt
  - differentiable-ray-tracing
  - calibration
  - hoydis
  - cammerer
  - aitaoudia
  - nvidia
  - reproduction-target
created: 2026-05-01
updated: 2026-05-01
---

# Hoydis et al. 2024 — Learning Radio Environments by Differentiable Ray Tracing

**Authors:** Jakob Hoydis, Fayçal Aït Aoudia, Sebastian Cammerer, Florian Euchner, Merlin Nimier-David, Stephan ten Brink, Alexander Keller (NVIDIA + U. Stuttgart). **arxiv:2311.18558** / **IEEE TMLCN 2024**. Code at https://github.com/NVlabs/diff-rt-calibration. Mirrored at `raw/articles/ml-phy/pdfs/diff-rt-calibration-2024.pdf`.

## TL;DR
**Calibrate a ray tracer the same way you train a neural network.** The paper introduces a gradient-based calibration method for [[sionna]] RT: treat material conductivity, permittivity, scattering coefficients, and antenna patterns as **trainable parameters** of a giant computational graph, and optimize them against measured channel frequency responses (CFRs) via backprop. Validated on synthetic data and **real indoor multi-MIMO channel sounder measurements**. Outperforms classical aggregate-statistics calibration. **The method paper for Phase 4 M10.**

## Key contributions

1. **Calibration-as-training paradigm.** Field computation in a differentiable ray tracer is reframed as a large computational graph; material and antenna parameters are weights; channel measurements are training targets. A "physics-informed NN" but every parameter retains exact physical meaning (relative permittivity $\epsilon_r$, conductivity $\sigma$, scattering coefficient $S$, antenna gain $G(\theta,\phi)$).
2. **Differentiable parametrizations** for:
   - **Material properties** — splines over $\epsilon_r, \sigma$ vs. frequency.
   - **Scattering patterns** — directive and Lambertian models, parametric mixture.
   - **Antenna patterns** — spherical-harmonics basis or directly-trained $C(\theta,\phi) \in \mathbb{C}^2$.
3. **Loss function** — log-distance between simulated and measured CFRs, summed over all (TX, RX) pairs.
4. **Validation on real measurements** — distributed indoor MIMO channel sounder dataset; calibration recovers per-material-type parameters consistent with literature values.
5. **Open-source release** — dataset (the **DICHASUS** distributed-MIMO sounder corpus from U. Stuttgart) + 3D scene model + code; fully reproducible.

## Baselines compared

The paper benchmarks against three classical calibration approaches (Section I refs [24]–[29]):
- **Aggregate-statistics fitting** — tune materials to match measured path loss / delay spread (closed-form for simplified RT; simulated annealing for general RT).
- **Per-ray super-resolution matching** — extract individual rays from measurements via super-resolution then match to RT predictions (used at 28 GHz outdoor).
- **Per-object material measurement** — directly probe each material's $\epsilon_r, \sigma$ — the only option when no channel measurements are available, but does not scale.

Any reproduction of this paper must compare against the same baselines on the same data.

## Methods

- **Sionna RT** (TensorFlow-based, differentiable) is the simulation backend.
- **Material model.** Each unique material (concrete, drywall, metal, glass) has its own learnable $(\epsilon_r, \sigma)$ — frequency-dependent via spline.
- **Scattering model.** Per-material scattering coefficient $S$ + cross-polarization ratio $K_x$ + directional weight $\alpha$.
- **Antenna model.** Trainable spherical-harmonics expansion of the antenna pattern — captures real-world antenna imperfections.
- **Optimizer.** Adam, learning rate $10^{-2}$, 1000 iterations. Loss: $\frac{1}{NM}\sum_{n,m} \log\bigl|H_{nm}^{\text{sim}} - H_{nm}^{\text{meas}}\bigr|^2$ where $(n,m)$ indexes (subcarrier, TX-RX pair).

## Results

- **Synthetic dataset** — recovers ground-truth $\epsilon_r$ to within 1% across all material classes.
- **Real indoor measurements** — calibrated CFR matches measured CFR to within 1–2 dB across 100s of measurement positions.
- **Reduces RMS path-loss error** from ~6 dB (uncalibrated default-material RT) to ~1–2 dB.
- **Antenna pattern learning** — recovers real measured patterns better than vendor data sheets when imperfections are present.

## Why it matters / where it sits in the roadmap

- **Phase 4 M10 deliverable.** [[python-ml-wireless]] explicitly calls for a "site-specific neural receiver in Sionna RT — custom OSM scene." This paper is the calibration backbone for that work.
- **Demonstrates the Hoydis-team method.** Reading this is part of speaking the team's language for the cold-email.
- **NVIDIA-intern target — direct match.** Hoydis, Aït Aoudia, Cammerer are the three NVIDIA authors and they are the team Jayden is targeting for Summer 2027 internship.
- **Cross-pollinates with [[wireless-digital-twin]].** Calibrated RT scenes are the data source for digital twins.

## Concepts grounded

- [[differentiable-ray-tracing]] — primary concept page.
- [[sionna]] — RT is a Sionna submodule.
- [[wireless-digital-twin]] — calibrated RT = ground truth for the twin.
- [[autograd]] — calibration is autograd applied to physics.

## Portfolio move (Phase 4 M10)

> **Reproduce first, extend second.** This is Jayden's single highest-leverage NVIDIA-portfolio item — the artifact must match the published metrics before any extension is attempted.

**Reproduce (the artifact):**
1. `git clone https://github.com/NVlabs/diff-rt-calibration` and run the **indoor DICHASUS reproduction** as published — material recovery within 1% on synthetic data, calibrated CFR within 1–2 dB of measured on the DICHASUS indoor benchmark.
2. Run a **synthetic ablation** — start from deliberately-wrong material defaults; confirm gradient calibration converges to ground truth.
3. Match the same baselines the paper reports (aggregate-statistics fitting, per-ray super-resolution).
4. Write up reproduction as a blog post + figure-by-figure verification — this is the Hoydis-team-cold-email artifact.

**Extend (Phase 4 stretch goals — only after reproduction lands):**
- Add **diffraction parameter** calibration (paper explicitly leaves for future work).
- Apply to a **custom OSM scene** of an ASU building or apartment — site-specific calibration with a fresh measurement campaign.
- Submit as a Sionna RT contributor PR or as an Asilomar 2027 workshop submission.

> [!tip] Interviewer talking point
> "I reproduced your DICHASUS indoor calibration result and recovered the published $\epsilon_r$ values to within 1%; I then extended to diffraction-parameter calibration which the paper marked as future work."

## Questions raised
- **Calibration of moving objects** — paper assumes static scene. Extending to moving humans / vehicles is open.
- **Calibration with sparse measurements** — current method needs many TX-RX pairs. Few-shot calibration with regularization is open research.
- **Combined geometry + material calibration** — paper assumes geometry is given. Joint calibration is open.

## Related
- [[python-ml-wireless]]
- [[digital-twin-calibration]] — the closed-loop concept page that wraps this paper's methodology.
- [[differentiable-ray-tracing]]
- [[paper-sionna-rt-2023]] — the differentiable RT engine this paper calibrates.
- [[paper-sionna-2022]] — the broader Sionna stack.
- [[paper-digital-twin-vision-2023]] — the digital-twin context.
- [[hoydis]], [[cammerer]], [[aitaoudia]] — the three target NVIDIA authors.
