---
title: Differentiable ray tracing for wireless
type: concept
course: [[python-ml-wireless]]
tags: [sionna, ray-tracing, mitsuba, digital-twin, calibration, nvidia]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# Differentiable ray tracing for wireless

## In one line
Ray tracing where the gradient of the received signal with respect to *anything* — material permittivity, antenna pattern, scene geometry — is computable, so you can backprop from a measured channel back to "what material is this wall?" and calibrate a digital twin from real RF data.

## Example first

You deploy a $28$ GHz BS in a specific building. You drive around and measure channels at $500$ UE positions. You also have a rough 3D model of the building (from OpenStreetMap). The question: what are the electromagnetic properties of the walls — glass? concrete? steel-reinforced concrete? Each has a different permittivity, which changes reflection coefficients, which changes channels.

**Classical approach:** use tabulated material values; accept $\sim 5$–$10$ dB errors in RSRP predictions.

**Differentiable-RT approach** (Hoydis et al. 2024, IEEE TMLCN):
```python
# Scene with one building, unknown material.
permittivity = torch.tensor(5.0, requires_grad=True)

for epoch in range(500):
    # Compute predicted channels at measured positions via ray tracing.
    h_pred = sionna_rt.compute(scene, permittivity, positions)
    loss = ((h_pred - h_measured)**2).sum()
    loss.backward()          # gradient FLOWS through the ray tracer
    permittivity.data -= lr * permittivity.grad
    permittivity.grad.zero_()
```

Gradient descent converges to permittivity $\approx 6.5$ (concrete). RSRP prediction error drops by $5+$ dB across the scene. You have just **calibrated the digital twin from real RF data**, and you can now train a site-specific neural receiver on the twin's output with confidence.

## The idea

Ray tracing computes the RF channel as a sum of paths. Each path has amplitude that depends on reflection coefficients, diffraction losses, scattering, which in turn depend on material properties and antenna patterns. A *differentiable* ray tracer keeps all of that in an autograd graph, so `y.backward()` gives gradients wrt every continuous parameter.

### How Sionna RT makes it differentiable

- Built on **Mitsuba 3 $+$ Dr.Jit** — a just-in-time-compiled GPU renderer originally for graphics, now repurposed for RF. Dr.Jit provides reverse-mode autodiff.
- **Continuous parameters are differentiable by construction**: material permittivity, conductivity, antenna patterns (when parameterized by continuous gains), transmit powers, RIS phase shifts.
- **Discrete decisions (which rays to trace) are non-differentiable** — handled by sampling with low variance or by **smoothed reparameterizations**. This is the technical meat of the Sionna RT papers.
- **Path tree topology**: for a given scene, the computed paths are deterministic. Small changes to geometry can add/remove paths; handle with soft masks.

### What you can calibrate with differentiable RT

- **Material parameters.** Permittivity, conductivity per material class.
- **Antenna patterns.** Parameterized gain functions, polarization.
- **RIS configurations.** Phase per element, as continuous variables.
- **Scene geometry.** Small perturbations to building positions (needs special handling for topology).

### Where it unlocks research

1. **Digital-twin calibration** (Hoydis 2024, code at https://github.com/NVlabs/diff-rt-calibration). Fit the twin to real data.
2. **RIS optimization.** Differentiable phase-per-element lets you optimize a $1024$-element RIS by gradient descent.
3. **Antenna array design.** Patterns optimized for a specific scene.
4. **Inverse source localization.** Find transmitters from received channels.
5. **Learnable digital twins** (Jiang et al. 2024, arxiv:2409.02564, Meta Reality Labs collaboration) — differentiate through the RT to tune neural components alongside physical ones.

## Formal definition

For a scene $\mathcal{S}(\boldsymbol{\psi})$ parameterized by $\boldsymbol{\psi}$ (materials, antennas, geometry), transmitter $t_x$ with signal $\mathbf{s}$, and receiver $r_x$, the received signal is:

$$\mathbf{y}(\boldsymbol{\psi}) = \sum_{p \in \mathcal{P}(\mathcal{S}, t_x, r_x)} A_p(\boldsymbol{\psi})\; e^{-j 2 \pi f \tau_p(\boldsymbol{\psi})}\; \mathbf{s}(t - \tau_p(\boldsymbol{\psi})) + \mathbf{n}$$

Differentiable RT guarantees $\partial A_p / \partial \boldsymbol{\psi}$ and $\partial \tau_p / \partial \boldsymbol{\psi}$ are defined and autograd-computable for each path $p$. The total gradient $\partial \mathbf{y} / \partial \boldsymbol{\psi}$ is assembled via the chain rule.

## Why it matters / when you use it

- **Digital-twin calibration** — the only way to close the sim-to-real gap without a deep learning model on top of a non-differentiable RT.
- **Site-specific training** — generate ray-traced channels for a specific scene $+$ reuse as the data source for [[neural-receiver]] fine-tuning.
- **Research agenda coupling** — this is the technology NVIDIA Aerial Omniverse Digital Twin (AODT) and Alkhateeb's digital twins both build on. A single technical skill that serves both target labs.

## Common mistakes

- **Assuming it's a drop-in for Mitsuba graphics rendering.** It models EM reflection/diffraction/scattering, not optics. Don't expect photorealistic images.
- **Treating high-order reflections naively.** Each additional bounce explodes the path tree. Set a max-depth and document it.
- **Non-smooth scene changes.** Moving a wall by 1 cm might add or remove a whole new reflection path. The gradient sees a step — you may need **smooth scene priors** during optimization.

## Research ties

- **Canonical papers:** Hoydis et al. "Sionna RT: Differentiable Ray Tracing" (arxiv:2303.11103); 2025 technical report (arxiv:2504.21719); "Learning Radio Environments by Differentiable Ray Tracing" (IEEE TMLCN 2024, https://github.com/NVlabs/diff-rt-calibration).
- **Related Wi-Lab work:** Jiang et al. "Learnable Wireless Digital Twins" (arxiv:2409.02564, 2024, Meta Reality Labs collab).
- **Tooling:** [[sionna]] RT; Mitsuba 3 + Dr.Jit.

## Portfolio move (Phase 4 Month 10)
Train a **site-specific neural receiver** in Sionna RT:
1. Build a custom scene (OSM → Sionna RT).
2. Generate ray-traced channels, mirror into [[deepmimo]] via `dm.convert()`.
3. Pretrain [[neural-receiver]] on 3GPP UMi.
4. Fine-tune on the scene's ray-traced channels.
5. Report BLER gain of site-specific vs generic.

## Related
- [[sionna]], [[sionna-rt]]
- [[wireless-digital-twin]]
- [[digital-twin-calibration]] — the closed-loop concept that uses differentiable RT for inverse rendering.
- [[deepmimo]]
- [[neural-receiver]]
- [[paper-diff-rt-calibration-2024]] — the load-bearing calibration paper.
- [[hoydis]], [[cammerer]], [[aitaoudia]]
- [[python-ml-wireless]]

## Practice
- Phase 4 M10 site-specific NRX project.
