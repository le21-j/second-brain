---
title: Complex Permittivity & Loss Tangent
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, electromagnetics, lossy-media, dielectric]
sources: [raw/slides/eee-341/lecture-2-2-time-harmonic-fields-complex-permittivity-and-helmholtz-equations-15.pdf, raw/slides/eee-341/lecture-2-6-special-cases-of-lossy-media-12-02.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Complex Permittivity

## In one line
A single complex number $\epsilon_c = \epsilon' - j\epsilon''$ that bundles together a material's real permittivity $\epsilon$ and its conduction loss $\sigma$ at a given frequency.

## Example first
Distilled water at $\omega = 2\pi\cdot 2.45$ GHz: $\epsilon_r = 78$, $\sigma \approx 0.5$ S/m. The complex permittivity is

$$\epsilon_c = \epsilon_0\epsilon_r - j\frac{\sigma}{\omega} = 8.854\times 10^{-12}(78) - j\frac{0.5}{2\pi\cdot 2.45\times 10^9} \approx 6.91\times 10^{-10} - j 3.25\times 10^{-11}$$

The loss tangent $\tan\delta = \epsilon''/\epsilon' \approx 0.047$ — water is a *quasi-conductor* at microwave frequencies, which is why microwave ovens work.

## The idea
In time-harmonic Ampere's law, conduction current $\sigma\vec{E}$ and displacement current $j\omega\epsilon\vec{E}$ are both proportional to $\vec{E}$. Combine them:

$$\nabla\times\vec{H} = \sigma\vec{E} + j\omega\epsilon\vec{E} = j\omega\Big(\epsilon - j\frac{\sigma}{\omega}\Big)\vec{E} = j\omega\epsilon_c\vec{E}$$

so a "lossy" medium is mathematically a "lossless" medium with a complex $\epsilon$.

## Formal definition

$$\epsilon_c = \epsilon' - j\epsilon'' = \epsilon - j\frac{\sigma}{\omega}$$

For most dielectrics there is also a polarization-loss contribution to $\epsilon''$ on top of $\sigma/\omega$. Define:

$$\boxed{\tan\delta = \frac{\epsilon''}{\epsilon'} = \frac{\sigma}{\omega\epsilon'}} \quad \text{(loss tangent)}$$

- $\tan\delta \ll 1$: **low-loss dielectric** (Teflon at 1 GHz, $\tan\delta \approx 3\times 10^{-4}$).
- $\tan\delta \gg 1$: **good conductor** (copper at 1 GHz, $\tan\delta \approx 10^{8}$).
- $\tan\delta \sim 1$: **quasi-conductor** (humid soil, biological tissue).

## Limiting cases for $\gamma$ and $\eta$
With $\gamma = j\omega\sqrt{\mu\epsilon_c}$:

**Low-loss dielectric ($\tan\delta \ll 1$):**
$$\alpha \approx \frac{\sigma}{2}\sqrt{\mu/\epsilon}, \quad \beta \approx \omega\sqrt{\mu\epsilon}$$
$$\eta \approx \sqrt{\mu/\epsilon}\,(1 + j\tan\delta/2) \approx \text{real}$$

**Good conductor ($\tan\delta \gg 1$):**
$$\alpha = \beta = \sqrt{\frac{\omega\mu\sigma}{2}} = \frac{1}{\delta_s}$$
$$\eta = (1+j)\sqrt{\frac{\omega\mu}{2\sigma}} = (1+j)\frac{1}{\sigma\delta_s}$$
where $\delta_s = 1/\alpha$ is the [[plane-wave-lossy|skin depth]].

## Why it matters / when you use it
Lets you solve any plane-wave problem (lossless *or* lossy) with one set of formulas — just replace real $\epsilon$ with complex $\epsilon_c$. Powers the [[fresnel-coefficients]] when one medium is lossy.

## Common mistakes
- **Sign of the imaginary part.** With time convention $e^{+j\omega t}$, loss is $-j\epsilon''$ (decaying wave). With $e^{-j\omega t}$ it would be $+j\epsilon''$. Stick with one convention.
- **Treating $\sigma$ as the only loss.** In dielectrics, $\epsilon''$ has a separate contribution from molecular relaxation that doesn't show up as DC conductivity.

## Related
- [[displacement-current]] — the $j\omega\epsilon$ piece
- [[plane-wave-lossy]] — the $\alpha,\beta$ that follow
- [[helmholtz-equation]] — where $\epsilon_c$ enters $\gamma$
