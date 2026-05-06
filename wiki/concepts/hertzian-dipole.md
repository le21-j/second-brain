---
title: Hertzian Dipole
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, antennas, dipole, radiation]
sources: [raw/slides/eee-341/lecture-6-2-the-hertzian-dipole-12-19.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Hertzian Dipole

## In one line
An infinitesimally short straight wire ($\ell \ll \lambda$) carrying a uniform sinusoidal current — the canonical "atom" of antenna theory; every wire antenna is a weighted superposition of Hertzian dipoles.

## Example first
A 1 mm Hertzian dipole at 1 GHz with $I_0 = 1$ A. Wavelength is $\lambda = 0.3$ m, so $\ell/\lambda = 1/300$ — well within the Hertzian regime.

Radiation resistance:
$$R_{\text{rad}} = 80\pi^2(\ell/\lambda)^2 = 80\pi^2(1/300)^2 \approx 8.77\times 10^{-3}\,\Omega$$

Total radiated power:
$$P_{\text{rad}} = \tfrac{1}{2}I_0^2 R_{\text{rad}} \approx 4.4 \text{ mW}$$

Tiny resistance ⇒ very inefficient match to a 50 Ω source ⇒ why electrically small antennas are hard.

## The idea
Solve for the vector potential $\vec{A}$ of a point current source, take the curl twice to get $\vec{E}$ and $\vec{H}$, then specialize to the **far field** ($k_0 R \gg 1$) where only the $1/R$ terms survive — those carry real power.

## Formal definition

### Far-field expressions ($k_0 R \gg 1$, $\ell \ll \lambda$)
$$\vec{E} \approx \hat{\theta}\,\frac{j\eta_0 k_0 I_0\ell}{4\pi R}\sin\theta\,e^{-jk_0 R}$$

$$\vec{H} \approx \hat{\phi}\,\frac{jk_0 I_0\ell}{4\pi R}\sin\theta\,e^{-jk_0 R}$$

So $|E|/|H| = \eta_0$ (free-space impedance) — locally the radiated wave is a plane wave.

### Radiation pattern (normalized intensity)
$$F(\theta,\phi) = \sin^2\theta$$

Independent of $\phi$ ⇒ **omnidirectional** about the dipole axis. Pattern looks like a donut centered on the wire; nulls along $\theta = 0,\pi$ (along the wire), maximum at $\theta = \pi/2$ (broadside).

### Radiation intensity
$$U(\theta,\phi) = \lim_{R\to\infty} R^2 S_{\text{av}}(R,\theta,\phi) = \frac{\eta_0 k_0^2(I_0\ell)^2}{32\pi^2}\sin^2\theta\quad [\text{W/sr}]$$

### Total radiated power
$$P_{\text{rad}} = \int_0^{2\pi}\!\!\int_0^\pi U\sin\theta\,d\theta\,d\phi = \frac{\eta_0 k_0^2(I_0\ell)^2}{12\pi}$$

Substituting $k_0 = 2\pi/\lambda$ and $\eta_0 \approx 120\pi$:

$$P_{\text{rad}} = \frac{1}{2}I_0^2 R_{\text{rad}}, \quad \boxed{R_{\text{rad}} = 80\pi^2(\ell/\lambda)^2 \approx 790(\ell/\lambda)^2 \,\Omega}$$

### Directivity
$$D_{\max} = \frac{4\pi U_{\max}}{P_{\text{rad}}} = \frac{3}{2} \approx 1.76\text{ dBi}$$

The Hertzian dipole is *barely* directional — only $1.5\times$ better than isotropic in its broadside direction.

## Why it matters / when you use it
- **Building block** for half-wave dipoles, Yagi-Uda, etc. — integrate Hertzian-dipole far fields weighted by the antenna's current distribution.
- **Worst-case efficiency benchmark** — any "electrically small" antenna ($\ell \ll \lambda$) has $R_{\text{rad}}$ that scales as $(\ell/\lambda)^2$, which is why phones at 700 MHz can't have 1-cm antennas without heroic matching.
- **EMC / radiated emissions** — a small loop of PCB trace at high frequency radiates like a Hertzian dipole.

## Common mistakes
- **Confusing $R_{\text{rad}}$ with the antenna's input resistance.** $R_{\text{in}} = R_{\text{rad}} + R_{\text{loss}}$. Hertzian's $R_{\text{loss}}$ may dominate for thin wires.
- **Using near-field formulas in the far field.** The Hertzian dipole has $1/R$, $1/R^2$, *and* $1/R^3$ terms; only the $1/R$ piece carries time-average power. Drop the rest beyond a few wavelengths.
- **Plotting in Cartesian.** Antenna patterns are conventionally polar plots in dB; an $\sin^2\theta$ pattern in dB is $20\log_{10}|\sin\theta|$.

## Related
- [[half-wave-dipole]] — practical realization (the Hertzian limit isn't fed-able)
- [[antenna-gain-directivity]] — derived quantities
- [[poynting-vector]] — used to compute $U(\theta,\phi)$
- [[friis-formula]] — link budget that uses these antennas
