---
title: Antenna Gain, Directivity, Radiation Resistance
type: concept
course: [[eee-341]]
tags: [eee-341, antennas, gain, directivity, efficiency]
sources: [raw/slides/eee-341/lecture-6-1-overview-of-antennas-and-their-properties-17-19.pdf, raw/slides/eee-341/lecture-6-3-antenna-radiation-characteristics-15-19.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Antenna Gain, Directivity, Radiation Resistance

## In one line
**Directivity** $D$ is how much the antenna concentrates radiated power vs an ideal isotropic radiator; **gain** $G = \xi D$ adds in the radiation efficiency $\xi$ (the only difference between $G$ and $D$ is conductor and dielectric loss).

## Example first
A half-wave dipole with $D_0 = 1.64$ (2.15 dBi) and radiation efficiency $\xi = 0.85$:

$$G_0 = \xi D_0 = 0.85\cdot 1.64 = 1.39 \;\;(\approx 1.43\text{ dBi})$$

If you push 10 W into the antenna, it radiates $\xi\cdot 10 = 8.5$ W; in the broadside direction the radiated intensity is $G_0$ times what an isotropic 10 W radiator would produce — i.e. $\approx 1.39\times$ (in linear) or $+1.43$ dB.

## The idea
**Directivity** uses *radiated* power as the reference; **gain** uses *input* power. The discrepancy is whatever the antenna lost as heat (conductor + dielectric losses inside the antenna structure).

## Formal definitions

### Radiation intensity
$$U(\theta,\phi) = \lim_{R\to\infty} R^2\,S_{\text{av}}(R,\theta,\phi) \quad [\text{W/sr}]$$

A function of direction only.

### Total radiated power
$$P_{\text{rad}} = \int_0^{2\pi}\!\!\int_0^\pi U(\theta,\phi)\sin\theta\,d\theta\,d\phi$$

### Directivity
$$D(\theta,\phi) = \frac{U(\theta,\phi)}{P_{\text{rad}}/4\pi} = \frac{4\pi U(\theta,\phi)}{P_{\text{rad}}}$$

Often quoted as the maximum: $D_0 = 4\pi U_{\max}/P_{\text{rad}}$.

### Gain
$$G(\theta,\phi) = \frac{4\pi U(\theta,\phi)}{P_{\text{in}}} = \xi\, D(\theta,\phi)$$

where the **radiation efficiency** is

$$\xi = \frac{P_{\text{rad}}}{P_{\text{in}}} = \frac{R_{\text{rad}}}{R_{\text{rad}} + R_{\text{loss}}}, \qquad 0 \leq \xi \leq 1$$

### Realized gain
Realized gain $G_r$ also accounts for impedance mismatch and polarization loss at the antenna terminals:
$$G_r = (1 - |\Gamma|^2)\,\text{PLF}\,G$$

### Beam solid angle approximation
For a directional pattern, an estimate of $D_0$ from the half-power beamwidths in the two principal planes:
$$D_0 \approx \frac{4\pi}{\Omega_p} \approx \frac{4\pi}{\Theta_E\Theta_H}$$
with HPBWs in radians. Equivalently, in degrees:
$$D_0 \approx \frac{41{,}253}{\Theta_E^\circ\Theta_H^\circ}$$

### Decibel notation
- **dBi**: dB relative to isotropic radiator. Use for $D$, $G$.
- **dBd**: dB relative to a half-wave dipole. $G_{dBi} = G_{dBd} + 2.15$ dB.

## Radiation resistance

$$P_{\text{rad}} = \tfrac{1}{2}|I_0|^2 R_{\text{rad}}$$

For a short ($\ell \ll \lambda$) Hertzian dipole: $R_{\text{rad}} = 80\pi^2(\ell/\lambda)^2$. For a half-wave dipole: $R_{\text{rad}} \approx 73\,\Omega$.

The antenna's input impedance is $Z_{\text{in}} = R_{\text{rad}} + R_{\text{loss}} + jX_{\text{in}}$. Matching network only fights $X_{\text{in}}$ (and any deviation of $R_{\text{rad}} + R_{\text{loss}}$ from the line $Z_0$).

## Why it matters / when you use it
- **Link budget calculations** ([[friis-formula]]) need $G_t$ and $G_r$.
- **Antenna sizing**: a dish with $G = 30$ dBi has beam solid angle $4\pi/10^3 \approx 0.0126$ sr, beamwidth $\sim 6.4°$. Useful for satellite-dish back-of-envelope.
- **Efficiency-vs-directivity trade-off** for electrically small antennas: $D_0$ approaches $1.5$ no matter how small you make it, but $\xi$ collapses, so usable $G$ collapses too.

## Common mistakes
- **Confusing $G$ and $D$.** They differ by $\xi$ — for many handbook antennas they are within a fraction of a dB, but for lossy antennas (small loop on a phone PCB) gain can be 6+ dB below directivity.
- **Forgetting polarization-mismatch loss in the link.** PLF cuts received power *in addition* to the path loss factor.
- **Mixing dBi and dBd silently.** Always state which.

## Related
- [[hertzian-dipole]] — minimum-directivity benchmark ($D_0 = 1.5$)
- [[half-wave-dipole]] — $D_0 = 1.64$, default reference antenna
- [[friis-formula]] — uses $G_t G_r$
- [[poynting-vector]] — what $U$ integrates
