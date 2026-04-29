---
title: Total Internal Reflection & Critical Angle
type: concept
course: [[eee-341]]
tags: [eee-341, electromagnetics, fiber-optics, evanescent-wave]
sources: [raw/slides/eee-341/lecture-3-8-critical-angle-total-internal-reflection-and-brewster-angle-12-08.pdf, raw/slides/eee-341/lecture-5-1-fiber-optics-18-27.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Total Internal Reflection (TIR)

## In one line
When a wave goes from a denser medium ($n_1$) to a less dense one ($n_2 < n_1$) at incidence angle $\theta_i > \theta_c = \arcsin(n_2/n_1)$, all the power is reflected and an evanescent (non-propagating) wave decays into medium 2.

## Example first
Light in water ($n_1 = 1.33$) hitting the water–air ($n_2 = 1$) boundary from below:

$$\theta_c = \arcsin(1/1.33) = 48.6°$$

For $\theta_i > 48.6°$, no light escapes the water — that's why looking up from underwater, only a circular "window" overhead transmits the sky; outside that disk you see a mirror reflection of the bottom. Same physics powers fiber optic communication.

## The idea
Snell's law $n_1\sin\theta_i = n_2\sin\theta_t$ requires $\sin\theta_t = (n_1/n_2)\sin\theta_i$. When $n_1 > n_2$ and $\theta_i$ is large enough, the right side exceeds 1 — no real $\theta_t$ exists. The transmitted wavevector becomes complex; the resulting field decays exponentially into medium 2 (an **evanescent wave**), no real power crosses the boundary, and the reflection coefficient has $|\Gamma|=1$.

## Formal definition

### Critical angle
$$\boxed{\theta_c = \arcsin\frac{n_2}{n_1}, \qquad n_2 < n_1}$$

For $\theta_i > \theta_c$: total internal reflection.

### Evanescent wave in medium 2
Beyond the critical angle, write the transmitted wavevector along $z$ (into medium 2) as imaginary:
$$k_{2z} = \pm jk_2\sqrt{(n_1/n_2)^2\sin^2\theta_i - 1}$$

The transmitted field is then
$$\vec{E}_t \propto e^{-jk_{2x}x}\,e^{-\alpha_e z}, \qquad \alpha_e = k_2\sqrt{(n_1/n_2)^2\sin^2\theta_i - 1}$$

— a wave traveling along the surface ($x$) with exponential decay perpendicular to it ($z$). Time-average power flow into medium 2 is **zero**.

### Reflection coefficient magnitude
For $\theta_i > \theta_c$, both $\Gamma_\perp$ and $\Gamma_\parallel$ have $|\Gamma| = 1$ (unity magnitude, but with a phase shift that depends on polarization).

## Why it matters / when you use it
- **Fiber optics** — light bouncing inside the core stays inside as long as it hits the cladding above $\theta_c$.
- **Prisms** — porro prisms in binoculars use TIR instead of mirrors (lossless).
- **Frustrated TIR** — bring a second high-index medium within the evanescent decay length and a tiny bit of power can tunnel across (basis of beam-splitter cubes, FTIR microscopy).

## Common mistakes
- **Forgetting $n_1 > n_2$.** TIR only happens going from dense to less dense. Going the other way, refraction always succeeds.
- **Thinking the field is zero in medium 2.** It's not — it's an evanescent wave with finite amplitude near the surface, just no real power flow.
- **Confusing critical angle with Brewster angle.** Both are interface-angle phenomena, but different physics: Brewster needs $\theta_i < 90°$ and $\Gamma_\parallel = 0$; TIR needs $\theta_i > \theta_c$ and $|\Gamma| = 1$.

## Related
- [[snells-law]] — when does $\sin\theta_t = 1$?
- [[brewster-angle]] — the other special angle
- [[fresnel-coefficients]] — base formulas
- Fiber optics (see lecture 5-1 in `raw/slides/eee-341/`)
