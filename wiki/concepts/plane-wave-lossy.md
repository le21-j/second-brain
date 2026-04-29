---
title: Plane Wave in Lossy Media & Skin Depth
type: concept
course: [[eee-341]]
tags: [eee-341, electromagnetics, plane-wave, attenuation, skin-depth]
sources: [raw/slides/eee-341/lecture-2-5-plane-wave-propagation-in-lossy-media-9-44.pdf, raw/slides/eee-341/lecture-2-6-special-cases-of-lossy-media-12-02.pdf, raw/slides/eee-341/lecture-2-7-current-flow-in-a-good-conductor-15-40.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Plane Wave in Lossy Media

## In one line
In a lossy medium $\gamma = \alpha + j\beta$ is complex, so the plane wave decays as $e^{-\alpha z}$ while it propagates as $e^{-j\beta z}$; the $1/e$ amplitude depth is the **skin depth** $\delta_s = 1/\alpha$.

## Example first
A 1 GHz plane wave entering copper ($\sigma = 5.8\times 10^7$ S/m, $\mu_r = \epsilon_r = 1$). Copper at 1 GHz is a good conductor ($\sigma/(\omega\epsilon) \approx 10^9$). Use the good-conductor formulas:

$$\alpha = \beta = \sqrt{\frac{\omega\mu\sigma}{2}} = \sqrt{\frac{2\pi(10^9)(4\pi\times 10^{-7})(5.8\times 10^7)}{2}} \approx 4.78\times 10^5 \text{ Np/m}$$

$$\delta_s = 1/\alpha \approx 2.09\,\mu\text{m}$$

So a 1 GHz signal penetrates only $\sim 2$ µm into copper — which is why thin copper plating works fine for RF.

## The idea
With finite conductivity, $\gamma = j\omega\sqrt{\mu\epsilon_c}$ has nonzero real part. The phasor $E_x(z) = E_0\,e^{-\gamma z} = E_0\,e^{-\alpha z}e^{-j\beta z}$ — exponential decay times oscillation. The intrinsic impedance $\eta = \sqrt{j\omega\mu/(\sigma + j\omega\epsilon)}$ becomes complex too, so $\vec{E}$ and $\vec{H}$ are no longer in phase.

## Formal definition

### General lossy
$$\gamma = \alpha + j\beta = j\omega\sqrt{\mu\epsilon_c}, \qquad \epsilon_c = \epsilon - j\sigma/\omega$$

$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}} \in \mathbb{C}$$

### Good conductor ($\sigma/(\omega\epsilon) \gg 1$)

$$\alpha = \beta = \sqrt{\frac{\omega\mu\sigma}{2}} = \sqrt{\pi f\mu\sigma}$$

$$\delta_s = \frac{1}{\alpha} = \frac{1}{\sqrt{\pi f\mu\sigma}}$$

$$\eta_c = (1+j)\,\frac{1}{\sigma\delta_s} = (1+j)\sqrt{\frac{\omega\mu}{2\sigma}}$$

The angle of $\eta_c$ is exactly $45°$ — $\vec{E}$ leads $\vec{H}$ by $\pi/4$ in a good conductor.

### Low-loss dielectric ($\tan\delta\ll 1$)
$$\alpha \approx \frac{\sigma}{2}\sqrt{\mu/\epsilon}, \quad \beta \approx \omega\sqrt{\mu\epsilon}$$
$\eta$ is approximately real.

## Skin depth and surface impedance
Surface resistance:
$$R_s = \frac{1}{\sigma\delta_s} = \sqrt{\pi f\mu/\sigma} \quad [\Omega/\square]$$

Internal (surface) impedance: $Z_s = R_s(1+j) = (1+j)/(\sigma\delta_s)$. AC resistance per unit length of a wire of radius $a$ at high frequency: $R_{ac}' = R_s/(2\pi a)$.

## Why it matters / when you use it
- **Penetration depth** for radio into seawater, biological tissue, soil.
- **AC wire resistance** — lossy at HF because current rides the outer skin only.
- **Conductor loss in transmission lines and waveguides** scales with $R_s\propto\sqrt{f}$.

## Common mistakes
- **Using lossless $\eta$ in a good conductor.** $\eta_c$ is complex with $45°$ phase; using real $\eta$ gives the wrong reflection coefficient.
- **Forgetting $\delta_s$ depends on $\sqrt{f}$.** Doubling frequency *halves* skin depth by $1/\sqrt{2}$, not $1/2$.

## Related
- [[plane-wave-lossless]] — the $\sigma=0$ limit
- [[complex-permittivity]] — collapses $\sigma$ into $\epsilon_c$
- [[poynting-vector]] — adds a $e^{-2\alpha z}$ on power
