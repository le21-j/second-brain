---
title: Waveguide Cutoff Frequency
type: concept
course: [[eee-341]]
tags: [eee-341, waveguide, cutoff, evanescent]
sources: [raw/slides/eee-341/lecture-5-4-guided-wave-modes-tem-te-and-tm-15-13.pdf, raw/slides/eee-341/lecture-5-7-propagation-velocities-12-07.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Waveguide Cutoff Frequency

## In one line
The frequency $f_c$ below which a given waveguide mode is evanescent ($\beta \to 0$, exponential decay) and above which it propagates with $\beta = k\sqrt{1-(f_c/f)^2}$.

## Example first
Air-filled WR-90 rectangular waveguide ($a = 0.9$" $= 22.86$ mm, $b = 0.4$" $= 10.16$ mm), TE$_{10}$ mode:

$$f_{c,10} = \frac{c}{2a} = \frac{3\times 10^8}{2\cdot 0.02286} = 6.56\text{ GHz}$$

At $f = 10$ GHz:

$$\beta_{10} = \frac{2\pi(10^{10})}{c}\sqrt{1 - (6.56/10)^2} = 209.4\sqrt{1 - 0.430} = 158.0\text{ rad/m}$$

Guide wavelength: $\lambda_g = 2\pi/\beta_{10} = 39.8$ mm (vs free-space $\lambda_0 = 30.0$ mm — guide wavelength is *longer* above cutoff).

## The idea
A waveguide mode is just two plane waves bouncing back and forth between the walls. Below $f_c$, the bounce angle goes imaginary — the mode can't satisfy the boundary conditions while propagating, so it dies exponentially.

## Formal definition

### General formula (rectangular waveguide, $a\times b$ cross-section)
$$\boxed{f_{c,mn} = \frac{c}{2\sqrt{\mu_r\epsilon_r}}\sqrt{(m/a)^2 + (n/b)^2}}$$

Equivalent forms:
- Cutoff wavenumber: $k_{c,mn} = \pi\sqrt{(m/a)^2 + (n/b)^2}$.
- Cutoff angular frequency: $\omega_c = ck_c$.

### Above cutoff ($f > f_c$): propagating
$$\beta = k\sqrt{1 - (f_c/f)^2}, \qquad u_p = \frac{c}{\sqrt{1-(f_c/f)^2}}, \qquad u_g = c\sqrt{1-(f_c/f)^2}$$

with $u_p u_g = c^2$.

### Below cutoff ($f < f_c$): evanescent
$$\alpha = k_c\sqrt{1 - (f/f_c)^2}, \qquad \beta = 0$$

The mode amplitude decays as $e^{-\alpha z}$. No real power propagates.

## Dispersion ($\omega$–$\beta$) diagram
A plot of $\omega$ vs $\beta c$ for a hollow waveguide is a hyperbola:
- $\beta = 0$ at $\omega = \omega_c$ (the y-intercept).
- For large $\omega$, asymptote $\omega = c\beta$ (the **light line**).
- Slope $d\omega/d\beta = u_g$; ray from origin has slope $\omega/\beta = u_p$.

WG modes are **fast-wave** modes ($u_p > c$); points sit *above* the light line.

## Mode chart for WR-90 (a = 0.9", b = 0.4")
Ordered by cutoff:
1. **TE$_{10}$** — 6.56 GHz (dominant)
2. TE$_{20}$ — 13.1 GHz
3. TE$_{01}$ — 14.8 GHz
4. TE$_{11}$ / TM$_{11}$ — 16.2 GHz

Single-mode operation = between TE$_{10}$ and TE$_{20}$. Recommended range $8.2$–$12.4$ GHz leaves margin for tolerances.

## Why it matters / when you use it
- **Bandplan**: every microwave waveguide is specified for single-mode operation between dominant and second mode.
- **Filter design**: cutoff WGs make short, simple high-pass filters.
- **Field probes**: a probe placed at $x = a/2$ in a TE$_{10}$ guide couples to the field maximum.

## Common mistakes
- **Treating wavelength as $c/f$ in a WG.** Above cutoff, $\lambda_g = 2\pi/\beta = c/(f\sqrt{1-(f_c/f)^2}) > c/f$. Use $\lambda_g$, not free-space $\lambda$, for half-wave matching.
- **Forgetting $u_p$ exceeds $c$.** Phase velocity above $c$ violates nothing — information travels at $u_g < c$.

## Related
- [[waveguide-modes]] — mode classification
- [[helmholtz-equation]] — eigenvalue problem
- [[cavity-resonator]] — closes the WG to discrete frequencies
