---
title: Maxwell's Equations
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, electromagnetics, maxwell, faradays-law, amperes-law, gauss-law]
sources: [raw/slides/eee-341/lecture-1-4-displacement-current-9-30.pdf, raw/slides/eee-341/lecture-1-5-boundary-conditions-for-electromagnetics-11-37.pdf, raw/slides/eee-341/lecture-2-2-time-harmonic-fields-complex-permittivity-and-helmholtz-equations-15.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Maxwell's Equations

## In one line
Four coupled PDEs that tie together every classical electromagnetic phenomenon: Gauss for electric flux, Gauss for magnetic flux, Faraday's induction, and Ampere–Maxwell with [[displacement-current]].

## Example first
A parallel-plate capacitor with no wire between the plates: a sinusoidal source on one plate produces a time-varying $\vec{E}$ across the gap. There is no conduction current in the gap (vacuum) — yet a magnetometer placed in the gap reads a time-varying $\vec{B}$. Pre-Maxwell Ampere predicts $\vec{B}=0$ (no $\vec{J}$). The fix is the displacement current $\partial\vec{D}/\partial t$:

$$\oint\vec{H}\cdot d\vec{l} = \int\!\!\int\!\Big(\vec{J} + \tfrac{\partial\vec{D}}{\partial t}\Big)\cdot d\vec{S}$$

That single $\partial\vec{D}/\partial t$ term is what closes the loop and lets EM waves exist.

## The idea
A time-varying electric field acts like a current and produces a magnetic field; a time-varying magnetic field induces an electric field. The two feed each other and the disturbance propagates outward at speed $1/\sqrt{\mu\epsilon}$. Maxwell's contribution was the displacement current; everything else (Coulomb, Gauss, Ampere, Faraday) was already known.

## Formal definition

### Point (differential) form

$$\nabla\cdot\vec{D} = \rho_v \qquad \text{(Gauss's law)}$$

$$\nabla\cdot\vec{B} = 0 \qquad \text{(Gauss's law for magnetism)}$$

$$\nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t} \qquad \text{(Faraday's law)}$$

$$\nabla\times\vec{H} = \vec{J} + \frac{\partial\vec{D}}{\partial t} \qquad \text{(Ampere–Maxwell)}$$

with constitutive relations $\vec{D}=\epsilon\vec{E}$, $\vec{B}=\mu\vec{H}$, $\vec{J}=\sigma\vec{E}$ in a simple (linear/isotropic/homogeneous/time-invariant) medium.

### Integral form

$$\oint\vec{D}\cdot d\vec{S} = Q_{\text{enc}} \qquad \oint\vec{B}\cdot d\vec{S} = 0$$

$$\oint\vec{E}\cdot d\vec{l} = -\frac{d}{dt}\!\!\int\!\!\int\!\vec{B}\cdot d\vec{S}$$

$$\oint\vec{H}\cdot d\vec{l} = I_{\text{enc}} + \frac{d}{dt}\!\!\int\!\!\int\!\vec{D}\cdot d\vec{S}$$

### Time-harmonic (phasor) form
Replace $\partial/\partial t \to j\omega$:

$$\nabla\cdot\vec{D} = \rho_v, \quad \nabla\cdot\vec{B} = 0$$

$$\nabla\times\vec{E} = -j\omega\mu\vec{H}, \quad \nabla\times\vec{H} = (\sigma + j\omega\epsilon)\vec{E} = j\omega\epsilon_c\vec{E}$$

where $\epsilon_c = \epsilon - j\sigma/\omega$ is the [[complex-permittivity]].

## Why it matters / when you use it
Every problem in EEE 341 starts here: plane-wave propagation comes from solving Maxwell in a source-free region (gives [[helmholtz-equation]]), [[boundary-conditions-em]] come from the integral form applied to a pillbox/Amperian loop straddling an interface, and [[poynting-vector]] follows from manipulating $\vec{E}\times\vec{H}$ and dotting with the curl equations.

## Common mistakes
- **Forgetting the displacement current.** Static-Ampere $\nabla\times\vec{H}=\vec{J}$ is *not* consistent with the [[charge-current-continuity]] equation $\partial\rho/\partial t + \nabla\cdot\vec{J}=0$. Maxwell's $\partial\vec{D}/\partial t$ fix is what restores consistency.
- **Mixing $\vec{D}$ vs $\vec{E}$ and $\vec{H}$ vs $\vec{B}$.** The free-source equations use $\vec{D}$ and $\vec{H}$; the force law uses $\vec{E}$ and $\vec{B}$. In a simple medium the relation is just a scalar $\epsilon$ or $\mu$ — but in lossy media $\epsilon$ becomes complex.
- **Sign conventions on Faraday's law.** The minus sign is Lenz's law — the induced EMF opposes the flux change.

## Related
- [[displacement-current]] — the term that makes the equations self-consistent
- [[boundary-conditions-em]] — what Maxwell forces at material interfaces
- [[helmholtz-equation]] — the wave equation that pops out in a source-free, time-harmonic, simple medium
- [[complex-permittivity]] — collapses $\sigma$ and $\epsilon$ into one complex parameter
- [[poynting-vector]] — power flow consequence
