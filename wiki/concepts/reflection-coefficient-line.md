---
title: Reflection Coefficient & VSWR on a Transmission Line
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, transmission-lines, reflection-coefficient, vswr]
sources: [raw/slides/eee-341/lecture-4-3-review-of-transmission-lines-part-3-12-24.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Reflection Coefficient on a Transmission Line

## In one line
The load reflection coefficient $\Gamma_L = (Z_L - Z_0)/(Z_L + Z_0)$ measures how much of an incoming voltage wave bounces off the load; VSWR$=(1+|\Gamma|)/(1-|\Gamma|)$ measures the resulting standing-wave ripple.

## Example first
A 50 Ω line terminated in $Z_L = 25\,\Omega$:

$$\Gamma_L = \frac{25 - 50}{25 + 50} = -\tfrac{1}{3}$$

$$\text{VSWR} = \frac{1 + 1/3}{1 - 1/3} = \frac{4/3}{2/3} = 2 \quad \text{(written ``2:1'')}$$

The voltage envelope on the line oscillates between $|V_{\max}| = (1 + |\Gamma|)|V_0^+| = (4/3)|V_0^+|$ and $|V_{\min}| = (2/3)|V_0^+|$.

## The idea
At the load, KCL/KVL force the ratio $V/I = Z_L$. The forward wave has $V^+/I^+ = Z_0$, the reflected wave has $V^-/I^- = -Z_0$. Solving gives $V_0^-/V_0^+ = (Z_L - Z_0)/(Z_L + Z_0)$. Same form as the optical [[fresnel-coefficients]] — replace $\eta$ with $Z_0$, $\eta'$ with $Z_L$.

## Formal definition

### Load reflection coefficient
$$\boxed{\Gamma_L = \frac{V_0^-}{V_0^+} = \frac{Z_L - Z_0}{Z_L + Z_0}}$$

### Generalized reflection coefficient (at any point $z$ on the line)
$$\Gamma(z) = \Gamma_L\,e^{2\gamma z}$$

For a *lossless* line ($\gamma = j\beta$): $\Gamma(z) = \Gamma_L\,e^{j2\beta z}$ — magnitude is constant, phase rotates as you slide along the line.

### Line impedance
$$Z(z) = Z_0\,\frac{1 + \Gamma(z)}{1 - \Gamma(z)}$$

Lossless input impedance at distance $\ell$ from the load:
$$Z_{\text{in}} = Z_0\,\frac{Z_L + jZ_0\tan\beta\ell}{Z_0 + jZ_L\tan\beta\ell}$$

### Special cases
| $Z_L$ | $\Gamma_L$ | VSWR | Notes |
|---|---|---|---|
| $Z_0$ (matched) | $0$ | $1$ | No reflection |
| $\infty$ (open) | $+1$ | $\infty$ | Full reflection in phase |
| $0$ (short) | $-1$ | $\infty$ | Full reflection, $\pi$ flip |
| $jX$ (pure reactive) | $|\Gamma|=1$ | $\infty$ | Phase angle depends on $X$ |

### VSWR (Voltage Standing-Wave Ratio)
$$\boxed{\text{VSWR} = S = \frac{1 + |\Gamma|}{1 - |\Gamma|}, \qquad |\Gamma| = \frac{S-1}{S+1}}$$

Always $S \geq 1$; $S = 1$ means matched.

### Quarter-wave magic
At $\ell = \lambda/4$, $\tan\beta\ell \to \infty$, so $Z_{\text{in}} = Z_0^2/Z_L$ — the line *inverts* the load. This is the basis of the quarter-wave transformer in [[smith-chart]] matching.

## Why it matters / when you use it
- Compute return loss (RL) $= -20\log_{10}|\Gamma|$ — the standard impedance-mismatch metric.
- VSWR < 2 is a typical "good match" specification (return loss $> 9.5$ dB).
- Underpins everything on the [[smith-chart]].

## Common mistakes
- **Forgetting $\Gamma$ rotates only on lossless lines.** On a lossy line, $|\Gamma(z)| = |\Gamma_L|\,e^{-2\alpha (\ell - z)}$ — magnitude shrinks toward the load.
- **Forgetting $|\Gamma|$ = 1 for purely reactive loads.** Inductors and capacitors reflect *all* power back, just with a phase shift.

## Related
- [[transmission-line-model]] — parent
- [[smith-chart]] — graphical $\Gamma\leftrightarrow Z$
- [[fresnel-coefficients]] — same formula in optics
