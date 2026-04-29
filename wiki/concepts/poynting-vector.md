---
title: Poynting Vector & EM Power Density
type: concept
course: [[eee-341]]
tags: [eee-341, electromagnetics, power, poynting]
sources: [raw/slides/eee-341/lecture-2-8-electromagnetic-power-density-9-58.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Poynting Vector

## In one line
$\vec{S} = \vec{E}\times\vec{H}$ — the instantaneous EM power per unit area, pointing along the direction of energy flow.

## Example first
A 1 V/m, 1 GHz plane wave in free space, polarized $\hat{x}$, traveling $+\hat{z}$:

$$\vec{E} = \hat{x}\cos(\omega t - k_0 z), \qquad \vec{H} = \hat{y}\frac{1}{\eta_0}\cos(\omega t - k_0 z)$$

$$\vec{S} = \vec{E}\times\vec{H} = \hat{z}\,\frac{1}{\eta_0}\cos^2(\omega t - k_0 z)$$

Time-average: $\vec{S}_{\text{av}} = \hat{z}\,\frac{1}{2\eta_0} \approx 1.33\text{ mW/m}^2$. Equivalent in phasor form:

$$\vec{S}_{\text{av}} = \tfrac{1}{2}\,\text{Re}\{\vec{E}\times\vec{H}^*\} = \hat{z}\,\frac{|E_0|^2}{2\eta_0}$$

## The idea
Energy stored in the EM field flows in the direction $\vec{E}\times\vec{H}$. The instantaneous magnitude is the volumetric power crossing a unit area per second. For a plane wave, this points along $\hat{k}$ — the wave carries its energy with itself.

## Formal definition

### Instantaneous
$$\vec{S}(\vec{r},t) = \vec{E}(\vec{r},t)\times\vec{H}(\vec{r},t) \quad [\text{W/m}^2]$$

### Time-average (time-harmonic fields)
$$\boxed{\vec{S}_{\text{av}}(\vec{r}) = \tfrac{1}{2}\,\text{Re}\{\vec{E}(\vec{r})\times\vec{H}^*(\vec{r})\}}$$

### Plane wave specializations
**Lossless:** $\vec{S}_{\text{av}} = \hat{k}\,\frac{|E_0|^2}{2\eta}$.

**Lossy:** $\vec{S}_{\text{av}} = \hat{k}\,\frac{|E_0|^2}{2|\eta|}\cos\theta_\eta\,e^{-2\alpha z}$, where $\theta_\eta$ is the phase of $\eta$ — the $\cos\theta_\eta$ factor accounts for $\vec{E}$ and $\vec{H}$ no longer being in phase, and $e^{-2\alpha z}$ is the power-attenuation envelope (twice the field-attenuation rate).

## Poynting's theorem (energy conservation)
For a closed volume $V$ bounded by surface $\Sigma$:

$$-\oint_\Sigma\vec{S}\cdot d\vec{A} = \frac{d}{dt}\!\!\int_V\Big(\tfrac{1}{2}\epsilon E^2 + \tfrac{1}{2}\mu H^2\Big)dV + \int_V\sigma E^2\,dV$$

In words: the net power flowing **into** the closed region equals the time-rate of change of stored EM energy plus ohmic dissipation.

## Decibel scale for attenuation

$$\text{Attenuation (dB)} = 10\log_{10}\frac{S_{\text{av}}(0)}{S_{\text{av}}(z)} = 10\log_{10}\,e^{2\alpha z} = 8.686\,\alpha z$$

So $\alpha$ in Np/m converts to dB/m by multiplying by $8.686$.

## Why it matters / when you use it
- Compute received power in [[friis-formula]] (power density × effective area).
- Determine penetration loss in lossy media — power decays *twice* as fast as field.
- Antenna radiation patterns ([[antenna-gain-directivity]]) are essentially scaled Poynting magnitudes vs angle.

## Common mistakes
- **Forgetting the $\tfrac{1}{2}$.** Phasor magnitudes are *peak* values; time-average power has the half.
- **Using $1/\eta$ in lossy media.** Use $\cos\theta_\eta/|\eta|$ — there is a phase angle that reduces real power flow.
- **Field decay vs power decay.** Field is $e^{-\alpha z}$; power is $e^{-2\alpha z}$.

## Related
- [[plane-wave-lossless]] — clean $|E_0|^2/(2\eta)$ result
- [[plane-wave-lossy]] — adds $e^{-2\alpha z}$
- [[friis-formula]] — uses time-average Poynting
- [[antenna-gain-directivity]] — pattern is normalized Poynting magnitude
