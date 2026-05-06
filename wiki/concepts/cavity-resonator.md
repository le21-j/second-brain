---
title: Cavity Resonator
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, waveguide, cavity, resonator, q-factor]
sources: [raw/slides/eee-341/lecture-5-8-cavity-resonators-11-16.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Cavity Resonator

## In one line
Close both ends of a section of waveguide and you trap standing waves at discrete eigenfrequencies — those are cavity modes, indexed TE$_{mnp}$ or TM$_{mnp}$ where $p$ counts half-wave variations along the length.

## Example first
Air-filled rectangular cavity from a length of WR-90 ($a = 0.9$", $b = 0.4$") cut to $d = 0.6$" $= 15.24$ mm. With convention $a > d > b$, the dominant mode is TE$_{101}$:

$$f_{101} = \frac{c}{2}\sqrt{(1/a)^2 + (1/d)^2} = \frac{3\times 10^8}{2}\sqrt{(1/0.02286)^2 + (1/0.01524)^2}$$

$$= 1.5\times 10^8\sqrt{43.74^2 + 65.62^2} = 1.5\times 10^8\sqrt{6217} \approx 11.83\text{ GHz}$$

## The idea
Take the waveguide mode TE$_{10}$ ($e^{-j\beta_{10} z}$) and add reflecting walls at $z = 0$ and $z = d$. Reflection from a PEC has $\Gamma = -1$, so a standing wave forms. The $z$-variation must vanish at both walls — quantizing $\beta_{10} d = p\pi$ for integer $p$. That promotes the continuous $\beta$ into a discrete set $\beta = p\pi/d$.

## Formal definition

### Resonant frequency (rectangular cavity)
$$\boxed{f_{mnp} = \frac{c}{2\sqrt{\mu_r\epsilon_r}}\sqrt{(m/a)^2 + (n/b)^2 + (p/d)^2}}$$

### Mode indexing
- **TM$_{mnp}$:** $m, n \geq 1$, $p \geq 0$.
- **TE$_{mnp}$:** $m, n \geq 0$ (not both zero), $p \geq 1$.

Dominant mode (lowest $f$) with convention $a > d > b$: **TE$_{101}$**.

### TE$_{101}$ field expressions
$$E_y = E_0\sin\!\left(\frac{\pi x}{a}\right)\sin\!\left(\frac{\pi z}{d}\right)$$
$$H_x = -j\frac{E_0}{Z_{TE}}\sin\!\left(\frac{\pi x}{a}\right)\cos\!\left(\frac{\pi z}{d}\right)$$
$$H_z = j\frac{E_0\pi}{\eta_0\beta a}\cos\!\left(\frac{\pi x}{a}\right)\sin\!\left(\frac{\pi z}{d}\right)$$

## Quality factor (Q)

$$Q = 2\pi\,\frac{\text{energy stored at resonance}}{\text{energy dissipated per cycle}} = \omega\,\frac{W_S}{P_L}$$

For TE$_{101}$ mode with conductor losses only (air-filled, no dielectric loss):
$$Q_{101} = \frac{\pi f_{101}\mu_0\,a b d\,(a^2 + d^2)}{R_s\bigl[2b(a^3 + d^3) + ad(a^2 + d^2)\bigr]}$$

where $R_s = \sqrt{\pi f \mu/\sigma}$ is the wall surface resistance.

Loaded Q $Q_L$ accounts for energy leaving via coupling ports; unloaded Q $Q_0$ is the intrinsic loss only.

## Why it matters / when you use it
- **Frequency stability** of microwave oscillators (klystrons, magnetrons).
- **Filters** — bandpass filters made of coupled cavities have far lower loss than lumped LC at $f > 1$ GHz.
- **Material characterization** — cavity perturbation method measures $\epsilon_r$ and loss tangent of small samples.

## Common mistakes
- **Forgetting $p \geq 1$ for TE.** A TE$_{10*0*}$ mode would have no $z$-variation — that's a waveguide mode, not a cavity mode.
- **Mixing waveguide and cavity formulas.** Waveguide cutoff has $(m/a)^2 + (n/b)^2$; cavity adds the $(p/d)^2$ term.
- **Treating $Q$ as a property of the cavity alone.** $Q$ depends on conductor *and* coupling — quote unloaded vs loaded.

## Related
- [[waveguide-modes]] — open-ended cousin
- [[waveguide-cutoff]] — basis for the $f_{mn}$ part
- [[helmholtz-equation]] — 3-D eigenvalue problem with PEC walls
