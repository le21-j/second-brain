---
title: Snell's Laws of Reflection & Refraction
type: concept
course: [[eee-341]]
tags: [eee-341, electromagnetics, oblique-incidence, refraction]
sources: [raw/slides/eee-341/lecture-3-3-snell-s-laws-of-reflection-and-refraction-18-09.pdf, raw/slides/eee-341/lecture-3-4-wave-reflection-and-transmission-at-oblique-incidence-perpendicular-.pdf, raw/slides/eee-341/lecture-3-6-wave-reflection-and-transmission-at-oblique-incidence-parallel-polar.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Snell's Laws

## In one line
At an interface, the angle of reflection equals the angle of incidence ($\theta_r = \theta_i$), and the angles of incidence and refraction obey $n_1\sin\theta_i = n_2\sin\theta_t$.

## Example first
Light going from air ($n_1 = 1$) into glass ($n_2 = 1.5$) at $\theta_i = 30°$:

$$\sin\theta_t = \frac{n_1}{n_2}\sin\theta_i = \frac{1}{1.5}\sin 30° = \frac{0.5}{1.5} = 0.333$$

$$\theta_t = \arcsin(0.333) \approx 19.5°$$

Ray bends *toward* the normal — going from less dense to more dense medium.

## The idea
**Phase matching.** At the boundary, all three propagation factors (incident, reflected, transmitted) must agree on their tangential dependence — otherwise the boundary conditions can't be satisfied for all positions $x$ along the surface. Equating the tangential components of the wavevectors gives Snell's laws.

## Formal definition

### Index of refraction
$$n = \frac{c}{u_p} = \sqrt{\mu_r\epsilon_r} \stackrel{\text{non-mag}}{=} \sqrt{\epsilon_r}$$

The wavenumber is $k = nk_0$.

### Snell's laws
$$\theta_r = \theta_i \qquad \text{(law of reflection)}$$
$$n_1\sin\theta_i = n_2\sin\theta_t \qquad \text{(law of refraction)}$$

Equivalently, $k_1\sin\theta_i = k_2\sin\theta_t$ — the tangential wavenumber is conserved.

### Bending direction
- $n_1 < n_2$ (less dense → more dense): $\theta_t < \theta_i$. Ray bends *toward* normal.
- $n_1 > n_2$ (more dense → less dense): $\theta_t > \theta_i$. Ray bends *away* from normal. ⇒ enables [[total-internal-reflection]].

## Reflection coefficients at oblique incidence
Two cases depending on the polarization (orientation of $\vec{E}$ relative to the **plane of incidence** — the plane containing $\hat{k}$ and the surface normal):

### Perpendicular polarization (TE — $\vec{E}\perp$ plane of incidence)
$$\Gamma_\perp = \frac{\eta_2\cos\theta_i - \eta_1\cos\theta_t}{\eta_2\cos\theta_i + \eta_1\cos\theta_t}$$
$$\tau_\perp = \frac{2\eta_2\cos\theta_i}{\eta_2\cos\theta_i + \eta_1\cos\theta_t}$$

### Parallel polarization (TM — $\vec{E}\parallel$ plane of incidence)
$$\Gamma_\parallel = \frac{\eta_2\cos\theta_t - \eta_1\cos\theta_i}{\eta_2\cos\theta_t + \eta_1\cos\theta_i}$$
$$\tau_\parallel = \frac{2\eta_2\cos\theta_i}{\eta_2\cos\theta_t + \eta_1\cos\theta_i}$$

> [!note] **Sanity check:** at $\theta_i = 0$, both reduce to the normal-incidence [[fresnel-coefficients]].

## Why it matters / when you use it
- Lensing, fiber optics ([[total-internal-reflection]]).
- [[brewster-angle]] for parallel polarization.
- Radar absorber and dielectric coating design.

## Common mistakes
- **Using $\eta$ where you mean $n$.** Snell's law uses $n$ (or $k$); reflection coefficients use $\eta$.
- **Swapping perpendicular and parallel.** Perpendicular = $\vec{E}\perp$ plane of incidence; parallel = $\vec{E}\parallel$ plane of incidence. Some textbooks use opposite labels.
- **Forgetting Snell when computing $\Gamma$.** You need $\theta_t$ before you can plug into $\Gamma$.

## Related
- [[fresnel-coefficients]] — normal-incidence limit
- [[brewster-angle]] — $\Gamma_\parallel = 0$
- [[total-internal-reflection]] — $\theta_i > \theta_c$
- [[boundary-conditions-em]] — phase-matching derivation
