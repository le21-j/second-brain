---
title: Helmholtz Equation
type: concept
course: [[eee-341]]
tags: [eee-341, electromagnetics, wave-equation, time-harmonic]
sources: [raw/slides/eee-341/lecture-2-1-unbounded-electromagnetic-waves-and-definition-of-a-simple-medium-19.pdf, raw/slides/eee-341/lecture-2-2-time-harmonic-fields-complex-permittivity-and-helmholtz-equations-15.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Helmholtz Equation

## In one line
The time-harmonic wave equation: $\nabla^2\vec{E} - \gamma^2\vec{E} = 0$ — what Maxwell collapses to in a source-free, simple medium when you assume $e^{j\omega t}$ time dependence.

## Example first
A uniform plane wave propagating in $+z$ with only an $x$-component, $\vec{E} = \hat{x}E_x(z)$, in a lossless medium. Helmholtz reduces to a 1-D ODE:

$$\frac{d^2 E_x}{dz^2} + k^2 E_x = 0$$

The general solution is $E_x(z) = E_0^+ e^{-jkz} + E_0^- e^{+jkz}$ — a forward and backward traveling wave. Pick the radiation condition (no source at infinity) and only the $E_0^+ e^{-jkz}$ term survives.

## The idea
Take the curl of Faraday's law, substitute Ampere–Maxwell, use $\nabla\times\nabla\times = \nabla(\nabla\cdot) - \nabla^2$, and the source-free condition $\nabla\cdot\vec{E}=0$ kills the gradient term. What's left is a Laplacian acting on $\vec{E}$ matched to a frequency-dependent constant.

## Formal definition
In a source-free, simple medium with phasor $\vec{E}$:

$$\boxed{\nabla^2\vec{E} - \gamma^2\vec{E} = 0}$$

where the **propagation constant**

$$\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)} = j\omega\sqrt{\mu\epsilon_c}$$

splits into:
- **Attenuation constant** $\alpha$ (Np/m) — lossy media only.
- **Phase constant** $\beta$ (rad/m) — sets the wavelength via $\lambda = 2\pi/\beta$.

In a **lossless** medium ($\sigma=0$, real $\epsilon$), $\alpha = 0$ and $\beta = k = \omega\sqrt{\mu\epsilon}$ is called the **wavenumber**. Helmholtz then reads $\nabla^2\vec{E} + k^2\vec{E} = 0$ — same equation, different sign convention.

## Why it matters / when you use it
- Plane-wave problems ([[plane-wave-lossless]], [[plane-wave-lossy]]) are 1-D Helmholtz solutions.
- Waveguide modes ([[waveguide-modes]]) come from solving the *transverse* Helmholtz equation with PEC boundary conditions.
- Cavity resonators ([[cavity-resonator]]) are 3-D Helmholtz with PEC on all faces — discrete eigenfrequencies.

## Common mistakes
- **Sign conventions.** Some books use $\gamma^2$, others $-k^2$. With $\gamma = j k$ they are the same equation; double-check the convention before you apply.
- **Treating $\gamma$ as real in a lossy medium.** It is generally complex — see [[plane-wave-lossy]].

## Related
- [[maxwell-equations]] — the parent
- [[plane-wave-lossless]] — the simplest 1-D solution
- [[plane-wave-lossy]] — adds attenuation
- [[complex-permittivity]] — folds $\sigma$ into $\epsilon_c$
- [[waveguide-modes]] — Helmholtz with boundary conditions
