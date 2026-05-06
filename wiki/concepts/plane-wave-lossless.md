---
title: Plane Wave in Lossless Media
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, electromagnetics, plane-wave, propagation]
sources: [raw/slides/eee-341/lecture-2-3-plane-wave-propagation-in-lossless-media-12-36.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Plane Wave in Lossless Media

## In one line
A uniform plane wave in a lossless simple medium has $\vec{E}$, $\vec{H}$, and propagation direction mutually orthogonal (TEM), with $\vec{E}/\vec{H}$ ratio equal to the intrinsic impedance $\eta$ and propagation factor $e^{-j\beta z}$.

## Example first
A 1 GHz plane wave in free space, polarized along $\hat{x}$, propagating in $+\hat{z}$:

- Wavenumber: $k_0 = \omega\sqrt{\mu_0\epsilon_0} = 2\pi(10^9)/(3\times 10^8) \approx 20.94$ rad/m.
- Wavelength: $\lambda_0 = 2\pi/k_0 = 0.30$ m.
- Intrinsic impedance: $\eta_0 = \sqrt{\mu_0/\epsilon_0} \approx 377$ Ω.
- Phasor electric field: $\vec{E}(z) = \hat{x}\,E_0\,e^{-j k_0 z}$ V/m.
- Phasor magnetic field: $\vec{H}(z) = \hat{y}\,(E_0/\eta_0)\,e^{-j k_0 z}$ A/m.

If $E_0 = 1$ V/m, then $|\vec{H}| \approx 2.65$ mA/m. Time-average power density (see [[poynting-vector]]):
$$\vec{S}_{\text{av}} = \tfrac{1}{2}\frac{|E_0|^2}{\eta_0}\hat{z} \approx 1.33 \text{ mW/m}^2$$

## The idea
Drop the lossy assumption ($\sigma=0$) into [[helmholtz-equation]] and you get a real wavenumber $k$. The 1-D Helmholtz $d^2 E_x/dz^2 + k^2 E_x = 0$ has plane-wave solutions $e^{\mp jkz}$, which translate to time-domain $\cos(\omega t \mp kz)$. Faraday's law then ties $\vec{H}$ to $\vec{E}$ via $\eta$.

## Formal definition
For a plane wave propagating along $\hat{k}$ in a simple lossless medium ($\sigma=0$):

$$\vec{E}(\vec{r}) = \vec{E}_0\,e^{-j\vec{k}\cdot\vec{r}}, \qquad \vec{H}(\vec{r}) = \frac{1}{\eta}\hat{k}\times\vec{E}(\vec{r})$$

where:

| Symbol | Name | Formula |
|---|---|---|
| $k$ | wavenumber | $\omega\sqrt{\mu\epsilon}$ |
| $\beta$ | phase constant | equals $k$ here |
| $\lambda$ | wavelength | $2\pi/k$ |
| $u_p$ | phase velocity | $\omega/k = 1/\sqrt{\mu\epsilon}$ |
| $\eta$ | intrinsic impedance | $\sqrt{\mu/\epsilon}$ |

In free space: $u_p = c$, $\eta_0 = 377$ Ω.

In a non-magnetic dielectric ($\mu=\mu_0$, $\epsilon = \epsilon_0\epsilon_r$):
$$k = k_0\sqrt{\epsilon_r}, \quad \eta = \eta_0/\sqrt{\epsilon_r}, \quad u_p = c/\sqrt{\epsilon_r}$$

## Why it matters / when you use it
Foundation for everything in Modules 2–3. Reflection/transmission, [[wave-polarization]], and [[poynting-vector]] all start from this template.

## Common mistakes
- **Using $\eta$ when you mean $n$.** $\eta$ is intrinsic impedance (units Ω); $n=c/u_p$ is index of refraction (dimensionless). For non-magnetic dielectric, $\eta = \eta_0/n$.
- **Forgetting $\hat{k}\times\vec{E}$ for $\vec{H}$.** $\vec{H}$ is in the direction $\hat{k}\times\hat{E}$ — get the cross product wrong and the Poynting vector points the wrong way.

## Related
- [[helmholtz-equation]] — parent ODE
- [[plane-wave-lossy]] — adds $\alpha$
- [[wave-polarization]] — what direction $\vec{E}$ traces in time
- [[poynting-vector]] — $|E_0|^2/(2\eta)$ for time-average power
