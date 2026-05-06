---
title: Antenna Array
type: concept
course:
  - "[[eee-341]]"
tags: [antennas, arrays, array-factor, beamforming, em]
sources: raw/slides/eee-341/lecture-6-8-antenna-arrays-18-04.pdf
created: 2026-04-28
updated: 2026-05-06
---

# Antenna Array

## In one line
A geometric arrangement of $N$ identical radiators whose far-field pattern is the **product** of a single element's pattern $\vec{E}_{\text{elem}}$ and an **array factor** $AF$ that depends only on element placement and excitation phases.

## Example first
Two half-wave dipoles separated by $d = \lambda/2$ along the $z$-axis, fed **in phase** with equal amplitudes (broadside array). The array factor is
$$AF(\theta) = 2\cos\!\left(\frac{\pi d}{\lambda}\cos\theta\right) = 2\cos\!\left(\frac{\pi}{2}\cos\theta\right).$$
- At $\theta = 90°$ (broadside, perpendicular to the array axis): $AF = 2\cos 0 = 2$ — **constructive**, peak.
- At $\theta = 0°$ (endfire, along the array): $AF = 2\cos(\pi/2) = 0$ — **null**.

So the elevation pattern is squeezed perpendicular to the dipole stack — exactly what you want for terrestrial broadcasting (radiate sideways, not up into the sky).

## The idea
Pattern multiplication: in the far field, when mutual coupling is negligible,
$$\vec{E}_{\text{total}}(\theta, \phi) = \vec{E}_{\text{element}}(\theta, \phi) \cdot AF(\theta, \phi).$$
The element pattern depends on the antenna type (e.g., $\sin\theta$ for a Hertzian dipole). The **array factor** $AF$ depends only on **(a)** geometry — number of elements, spacing $d$ — and **(b)** excitation — relative amplitudes and phase shifts $\beta$ between elements.

By tuning $d$ and $\beta$, you steer the main beam, deepen nulls, and shape the lobe pattern without touching the elements themselves. This is the foundation of beamforming, phased arrays, and 5G/6G MIMO.

## Two-element array factors (the only ones you need for EEE 341)

| Geometry | Excitation | Array factor |
|:---|:---|:---|
| Two elements along $\vec{z}$ | Equal-amplitude, in-phase ($\beta = 0$) | $AF(\theta) = 2\cos\!\left(\dfrac{\pi d}{\lambda}\cos\theta\right)$ |
| Two elements along $\vec{x}$ | Equal-amplitude, phase shift $\beta$ | $AF(\theta, \phi) = 2\cos\!\left(\dfrac{\pi d}{\lambda}\sin\theta\cos\phi + \dfrac{\beta}{2}\right)$ |

## Three canonical configurations

### 1. Broadside array ($d = \lambda/2$, $\beta = 0$)
- Maximum at $\theta = 90°$ (perpendicular to the line of elements).
- Nulls at $\theta = 0°, 180°$ (endfire directions).
- Doubles the gain over a single element along broadside.

### 2. Endfire array ($d = \lambda/4$, $\beta = -\pi/2$)
- Maximum along the array axis (forward direction).
- Used for directional links (e.g., yagi-uda derivatives).

### 3. Cardioid array ($d = \lambda/4$, $\beta = -\pi/2$, two elements along $\vec{x}$)
- Heart-shaped pattern: maximum forward ($\phi = 0°$), **deep null backward** ($\phi = 180°$).
- The lab's Section 3.4 uses this. The null-backward property is why cardioid microphones reject room sound from behind.

## Why it matters
Antenna arrays are how cellular base stations cover sectors, how 5G beamforming serves users at specific azimuths without raising total radiated power, and how radio astronomy synthesizes apertures kilometers wide. The array factor is the single mathematical knob that ties geometry + phase to beam shape.

## Common mistakes
- **Forgetting the element pattern.** The full pattern is $E_{\text{element}} \cdot AF$, not just $AF$. For a two-dipole stack, the element's $\sin\theta$ further suppresses the endfire direction.
- **Confusing $d$ and $\beta$ effects.** Spacing $d$ sets the periodicity of the AF; phase $\beta$ shifts where the maximum lands. Sweep $\beta$ at fixed $d$ to electronically steer the beam.
- **Ignoring mutual coupling.** Real elements perturb each other's currents; pattern multiplication assumes negligible coupling. Close-spaced elements ($d \lesssim \lambda/4$) need full numerical simulation (e.g., EZNEC, NEC2).

## Related
- [[hertzian-dipole]] — the elemental radiator
- [[half-wave-dipole]] — the workhorse element used in arrays
- [[antenna-gain-directivity]] — how arrays boost gain
- [[friis-formula]] — uses array gain in link budgets

## Practice
- [[eee-341-lab-5-walkthrough]] — Lab 5 sims a broadside ($\lambda/2$) and a cardioid array
