---
title: Fresnel Reflection & Transmission Coefficients
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, electromagnetics, reflection, transmission, normal-incidence]
sources: [raw/slides/eee-341/lecture-3-1-wave-reflection-and-transmission-at-normal-incidence-part-1-12-27.pdf, raw/slides/eee-341/lecture-3-2-wave-reflection-and-transmission-at-normal-incidence-part-2-18-14.pdf, raw/slides/eee-341/lecture-3-9-reflectivity-and-transmissivity-9-36.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Fresnel Coefficients (Normal Incidence)

## In one line
At a planar interface, the reflection coefficient $\Gamma = (\eta_2 - \eta_1)/(\eta_2 + \eta_1)$ and transmission coefficient $\tau = 2\eta_2/(\eta_2 + \eta_1)$ tell you what fraction of the incident $\vec{E}$ amplitude bounces back versus crosses over.

## Example first
A 1 GHz plane wave in free space ($\eta_1 = 377$ Ω) hits glass ($\epsilon_r = 4 \Rightarrow \eta_2 = 377/2 = 188.5$ Ω) at normal incidence:

$$\Gamma = \frac{188.5 - 377}{188.5 + 377} = -\tfrac{1}{3} \approx -0.333$$

$$\tau = \frac{2(188.5)}{188.5 + 377} = \tfrac{2}{3} \approx 0.667$$

Sanity check: $1 + \Gamma = \tau$ ⇒ $1 - 1/3 = 2/3$. ✓

Reflectivity (power): $R = |\Gamma|^2 = 1/9 \approx 11.1\%$. Transmissivity: $T = 1 - R = 8/9 \approx 88.9\%$.

## The idea
At the interface, tangential $\vec{E}$ and tangential $\vec{H}$ must be continuous ([[boundary-conditions-em]]). The incident, reflected, and transmitted waves each have a definite $\vec{E}/\vec{H}$ ratio set by the intrinsic impedance of their medium. Solve the two continuity equations and you get $\Gamma$ and $\tau$.

## Formal definition
For a wave incident from medium 1 onto medium 2 at normal incidence:

$$\boxed{\Gamma = \frac{E_0^r}{E_0^i} = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}}$$

$$\boxed{\tau = \frac{E_0^t}{E_0^i} = \frac{2\eta_2}{\eta_2 + \eta_1}}$$

with the identity $1 + \Gamma = \tau$.

### Reflectivity and transmissivity (power)

$$R = |\Gamma|^2, \qquad T = \frac{\eta_1}{\eta_2}|\tau|^2 = 1 - R \;\;(\text{lossless})$$

The $\eta_1/\eta_2$ factor on $T$ matters because power = $|E|^2/(2\eta)$ and the impedances differ between the two media.

### Special cases
- **Free-space → PEC:** $\eta_2 = 0$ ⇒ $\Gamma = -1$, $\tau = 0$. Total reflection with phase flip; standing wave on the source side.
- **Free-space → matched dielectric:** $\eta_2 = \eta_1$ ⇒ $\Gamma = 0$, $\tau = 1$. No reflection.
- **Lossy medium 2:** $\eta_2$ becomes complex ⇒ $\Gamma$ and $\tau$ complex with phase shifts.

## Why it matters / when you use it
- Quarter-wave radome / anti-reflection coating design.
- Reflection from dielectric layers (skin depth, glass, plastic).
- Special case of Smith-chart [[reflection-coefficient-line]] when $\eta_1 \to Z_0$ and $\eta_2 \to Z_L$ — same formula.

## Common mistakes
- **Sign of $\Gamma$.** When $\eta_2 < \eta_1$ (going into a lower-impedance medium, e.g. into a denser dielectric), $\Gamma < 0$ — phase flip on reflection.
- **$T \neq |\tau|^2$.** Need the $\eta_1/\eta_2$ correction in lossless media; the *amplitude* ratio is $\tau$ but *power* ratio adjusts for the impedance change.
- **Mixing oblique with normal.** These formulas are normal incidence only. For oblique incidence, use the polarization-specific forms (see [[snells-law]] and [[brewster-angle]]).

## Related
- [[boundary-conditions-em]] — derivation source
- [[snells-law]] — generalizes to oblique incidence
- [[brewster-angle]] — angle where $\Gamma_\parallel = 0$
- [[total-internal-reflection]] — $|\Gamma|=1$ regime
- [[reflection-coefficient-line]] — same formula on transmission lines
