---
title: Half-Wave Dipole
type: concept
course: [[eee-341]]
tags: [eee-341, antennas, dipole]
sources: [raw/slides/eee-341/lecture-6-4-half-wave-dipole-antenna-14-09.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Half-Wave Dipole

## In one line
A center-fed straight wire of total length $\lambda/2$ — the most-used wire antenna because its input impedance is roughly real and near 50 Ω, matching common feed lines without a matching network.

## Example first
A FM-radio dipole tuned to 100 MHz: $\lambda = c/f = 3$ m, so the antenna is 1.5 m total (each leg 0.75 m). Properties:

- Input impedance $\approx 73 + j42\,\Omega$ (close to 50 Ω; can be tuned to pure resistance by trimming slightly shorter).
- Radiation resistance $R_{\text{rad}} \approx 73\,\Omega$.
- Directivity $D_0 \approx 1.64 \approx 2.15$ dBi.
- Pattern: donut around the wire (omnidirectional in azimuth, nulls along the wire axis).

## The idea
Assume a sinusoidal current distribution $I(z) = I_0\cos(\beta z)$ for $|z| \leq \lambda/4$ — physically reasonable for a center-fed thin wire (current zero at the open ends). Integrate the [[hertzian-dipole]] far-field over the length, weighted by this current.

## Formal definition

### Assumed current distribution
$$I(z) = I_0\cos\!\left(\frac{2\pi}{\lambda}z\right) = I_0\cos(\beta z), \qquad -\lambda/4 \leq z \leq \lambda/4$$

### Far-field electric field
$$\vec{E} \approx \hat{\theta}\,\frac{j\eta_0 I_0}{2\pi R}\,\frac{\cos[(\pi/2)\cos\theta]}{\sin\theta}\,e^{-j\beta R}$$

### Normalized radiation intensity
$$F(\theta) = \left[\frac{\cos((\pi/2)\cos\theta)}{\sin\theta}\right]^2$$

For quick estimates, the approximation $F(\theta) \approx \sin^3\theta$ works well — slightly more directive than the Hertzian's $\sin^2\theta$.

### Radiation resistance and directivity
$$R_{\text{rad}} \approx 73\,\Omega, \qquad D_0 \approx 1.64 \;(2.15\text{ dBi})$$

(Compare Hertzian: $D_0 = 1.5 = 1.76$ dBi.) The half-wave is only marginally more directive than the elemental dipole, but its impedance match makes it vastly more usable.

### Half-power beamwidth
HPBW $\approx 78°$ in the elevation plane (broadside is the maximum). FNBW (first-null) is $180°$ — the nulls are along the wire ends.

## Quarter-wave monopole (related)
A $\lambda/4$ monopole over a large conducting ground plane radiates the same upper-hemisphere pattern as a $\lambda/2$ dipole, but with half the radiation resistance ($\approx 36.5\,\Omega$) and the lower hemisphere shielded.

## Why it matters / when you use it
- Default starting design for any narrow-band, narrow-bandwidth antenna in the VHF/UHF/microwave range.
- Reference for measuring gain in *dBd* (dB above a half-wave dipole): $G_{dBi} = G_{dBd} + 2.15$ dB.
- Core element of Yagi-Uda arrays, log-periodic dipoles, dipole arrays.

## Common mistakes
- **Building it $\lambda/2$ exactly.** Real-world wires need to be trimmed $\sim 5\%$ shorter to compensate for end effects (capacitive loading); the resonant length is closer to $0.475\lambda$.
- **Forgetting the radiation pattern is donut-shaped, not isotropic.** Two antennas oriented along each other's nulls don't talk well.
- **Using monopole values for a dipole.** Monopole has half the impedance and twice the directivity (in the upper hemisphere) of the equivalent dipole.

## Related
- [[hertzian-dipole]] — the integrand
- [[antenna-gain-directivity]] — quantities used here
- [[friis-formula]] — link budget with $D_0 = 1.64$ on each side
