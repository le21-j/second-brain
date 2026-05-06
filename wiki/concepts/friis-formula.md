---
title: Friis Transmission Formula
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, antennas, link-budget, path-loss]
sources: [raw/slides/eee-341/lecture-6-6-friis-transmission-formula-4-07.pdf, raw/slides/eee-341/lecture-6-5-effective-area-of-a-receiving-antenna-2-47.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Friis Transmission Formula

## In one line
Free-space link budget: $P_r/P_t = G_t G_r (\lambda/4\pi R)^2$, valid when both antennas are in each other's far field.

## Example first
Wi-Fi link at 2.4 GHz, $R = 30$ m, both ends omnidirectional ($G_t = G_r = 1$, dipole-ish), $P_t = 100$ mW. $\lambda = c/f = 0.125$ m:

$$\frac{P_r}{P_t} = (1)(1)\!\left(\frac{0.125}{4\pi\cdot 30}\right)^2 = (1.105\times 10^{-4})^2 \approx 1.10\times 10^{-8}$$

In dB:
$$\text{Path loss} = 20\log_{10}\frac{4\pi R}{\lambda} = 20\log_{10}(3015) \approx 69.6\text{ dB}$$

$P_r = 100\text{ mW}/10^{6.96} = 1.10\text{ nW} = -59.6$ dBm. A typical Wi-Fi receiver sensitivity is $-80$ to $-90$ dBm — comfortable margin.

## The idea
Step 1: an *isotropic* source at distance $R$ produces power density $P_t/(4\pi R^2)$. Step 2: real antennas concentrate by $G_t$ in the receiver direction, so the actual density is $G_t P_t/(4\pi R^2)$. Step 3: receiver intercepts via its **effective area** $A_e$, which is related to gain by $A_e = G_r\lambda^2/(4\pi)$. Multiply.

## Formal definition

### Friis formula
$$\boxed{\frac{P_r}{P_t} = G_t G_r\left(\frac{\lambda}{4\pi R}\right)^2}$$

Equivalent forms:
- $P_r = \text{EIRP}\cdot A_e/(4\pi R^2)$ where $\text{EIRP} = P_t G_t$ and $A_e = G_r\lambda^2/(4\pi)$.
- In dB: $P_r[\text{dBm}] = P_t[\text{dBm}] + G_t[\text{dB}] + G_r[\text{dB}] - L_{\text{path}}[\text{dB}]$.

### Free-space path loss
$$L_{\text{path}}[\text{dB}] = 20\log_{10}\frac{4\pi R}{\lambda} = 20\log_{10}(R) + 20\log_{10}(f) - 147.55$$

(with $R$ in m, $f$ in Hz) — both squared, so each doubling of distance or frequency adds 6 dB.

### Effective aperture
$$A_e = \frac{\lambda^2}{4\pi}G_r$$

For an aperture antenna (dish, horn) with physical aperture $A_{\text{phys}}$ and aperture efficiency $\eta_{\text{ap}}$: $A_e = \eta_{\text{ap}}A_{\text{phys}}$.

## Assumptions baked into Friis
1. **Free space** — no obstructions, no multipath, no atmospheric absorption.
2. **Far field on both ends** — $R \geq 2D^2/\lambda$ where $D$ is the larger antenna's max dimension.
3. **Polarization match** — if mismatched, multiply by $\text{PLF} \in [0,1]$.
4. **Impedance match at both ends** — otherwise multiply by $(1 - |\Gamma_t|^2)(1 - |\Gamma_r|^2)$.

Real-world links: add path-loss exponent $> 2$ (urban: $n \approx 3$–$4$), shadowing, fading.

## Why it matters / when you use it
- Sanity-check any wireless link: cell tower → phone, satellite → dish, GPS → receiver.
- Antenna trade studies: doubling antenna gain on either end is one $\Delta$ dB free, vs doubling tx power costs $2\times$ DC power.
- Defines the cost of going to higher carrier frequencies — same antennas have lower $A_e$ as $\lambda$ shrinks (unless gain scales with aperture).

## Common mistakes
- **Forgetting the wavelength factor.** Path loss is *not* just $1/R^2$ — at fixed antenna gains, doubling frequency at the same distance adds 6 dB of loss.
- **Mixing dB and linear.** $P_r = P_t G_t G_r/(4\pi R/\lambda)^2$ is *linear*; the dB form replaces multiplication with addition.
- **Using gain in dB inside the linear formula.** Convert first.

## Related
- [[antenna-gain-directivity]] — sets $G_t$ and $G_r$
- [[poynting-vector]] — basis of "power density" step
- [[hertzian-dipole]], [[half-wave-dipole]] — common antenna $G$ values
