---
title: Wave Polarization
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, electromagnetics, polarization, lhcp, rhcp]
sources: [raw/slides/eee-341/lecture-2-4-wave-polarization-22-59.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Wave Polarization

## In one line
The path traced by the tip of $\vec{E}$ at a fixed point in space as time advances — linear if it traces a line, circular if a circle, elliptical otherwise.

## Example first
Two perpendicular components of $\vec{E}$ on a wave traveling in $+\hat{z}$:

$$\vec{E}(0,t) = \hat{x}\cos(\omega t) + \hat{y}\cos(\omega t + \phi)$$

| $\phi$ | Trace | Polarization |
|---|---|---|
| $0$ | $E_x = E_y$, line at $45°$ | linear |
| $\pi$ | $E_x = -E_y$, line at $-45°$ | linear |
| $-\pi/2$ | circle, traversed CW (looking from receiver toward source — i.e. *along* $-\hat{z}$) | RHCP |
| $+\pi/2$ | circle, traversed CCW from receiver POV | LHCP |

> [!warning] **IEEE convention.** Sense of rotation is observed *looking in the direction of propagation* (from source toward receiver). RHCP = right-hand fingers curl with the rotation while thumb points along $\hat{k}$.

## The idea
Pick a fixed plane perpendicular to $\hat{k}$. Plot the tip of $\vec{E}$ over one period. The shape is at most an ellipse (lines and circles being degenerate cases). Polarization has two attributes: **shape** (axial ratio) and **sense** (handedness).

## Formal definition
The most general elliptically-polarized plane wave traveling in $+\hat{z}$:

$$\vec{E}(z,t) = \hat{x}\,E_{x0}\cos(\omega t - kz) + \hat{y}\,E_{y0}\cos(\omega t - kz + \phi)$$

Equivalently in phasor form: $\vec{E} = (\hat{x}\,E_{x0} + \hat{y}\,E_{y0}\,e^{j\phi})e^{-jkz}$.

### Polarization angles
Auxiliary angle: $\tan\psi = E_{y0}/E_{x0}$.
Tilt angle $\tau$: rotation of the major axis from $\hat{x}$.
Ellipticity angle $\chi$: $\sin 2\chi = \sin 2\psi\sin\phi$, with $+$ for LHCP, $-$ for RHCP.

### Axial ratio
$$\text{AR} = \frac{|\text{semi-major}|}{|\text{semi-minor}|}, \qquad \text{AR}_{\text{dB}} = 20\log_{10}\text{AR}$$

- $\text{AR} = 1$ (0 dB): circular.
- $\text{AR} \to \infty$: linear.
- Antennas often have AR target $\leq 3$ dB to be called "circularly polarized."

### Special cases
| Case | Condition |
|---|---|
| Linear (along $\hat{x}$) | $E_{y0} = 0$ |
| Linear ($45°$) | $E_{x0} = E_{y0}$, $\phi = 0$ |
| RHCP | $E_{x0} = E_{y0}$, $\phi = -\pi/2$ |
| LHCP | $E_{x0} = E_{y0}$, $\phi = +\pi/2$ |

## Why it matters / when you use it
- **Polarization-division multiplexing**: orthogonal polarizations carry independent signals on the same frequency (DBS-TV, MIMO).
- **GPS uses RHCP** so reflections (which flip handedness) get rejected.
- **Polarization mismatch loss**: at the receiver, the polarization-loss factor (PLF) cuts received power. PLF $= |\hat{p}_t\cdot\hat{p}_r^*|^2 \in [0,1]$.

## Common mistakes
- **Sense convention flipped.** IEEE looks along $\hat{k}$; physics often looks at the wave coming *at* you. The two are opposite.
- **Confusing axial ratio in dB vs linear.** AR (linear) is $\geq 1$; AR (dB) is $\geq 0$.
- **Forgetting the absolute phase doesn't matter.** Only the phase *difference* $\phi$ between $E_x$ and $E_y$ controls polarization.

## Related
- [[plane-wave-lossless]] — the carrier wave
- [[fresnel-coefficients]] — perpendicular vs parallel polarization at oblique incidence
