---
title: Waveguide Modes — TEM, TE, TM
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, waveguide, te-mode, tm-mode, tem]
sources: [raw/slides/eee-341/lecture-5-3-general-relations-for-electric-and-magnetic-fields-in-waveguides-8-0.pdf, raw/slides/eee-341/lecture-5-4-guided-wave-modes-tem-te-and-tm-15-13.pdf, raw/slides/eee-341/lecture-5-5-tm-modes-in-rectangular-waveguide-15-13.pdf, raw/slides/eee-341/lecture-5-6-te-modes-in-rectangular-waveguide-17-49.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Waveguide Modes

## In one line
Inside a uniform tube, EM fields decompose into eigenmodes classified by which longitudinal component is zero: TEM ($E_z = H_z = 0$), TE ($E_z = 0$, $H_z \neq 0$), TM ($H_z = 0$, $E_z \neq 0$).

## Example first
WR-90 air-filled rectangular waveguide ($a = 22.86$ mm, $b = 10.16$ mm). The dominant mode is TE$_{10}$ with cutoff at:

$$f_{c,10} = \frac{c}{2a} = \frac{3\times 10^8}{2(0.02286)} \approx 6.56\text{ GHz}$$

Recommended operating range: $8.2$–$12.4$ GHz (X-band) — above $f_{c,10}$ but below $f_{c,20} = 13.1$ GHz so only one mode propagates.

## The idea
Solve Helmholtz separately for the longitudinal field ($E_z$ or $H_z$) with PEC boundary conditions on the walls, then derive transverse fields from it. The boundary conditions force discrete eigenvalues $k_c$ — there are infinitely many modes labeled by integer indices.

## Formal definition

### Mode classification
| Mode | $E_z$ | $H_z$ |
|---|---|---|
| **TEM** (transverse EM) | 0 | 0 |
| **TE** (transverse electric) | 0 | $\neq 0$ |
| **TM** (transverse magnetic) | $\neq 0$ | 0 |
| **Hybrid** | $\neq 0$ | $\neq 0$ |

### Single-conductor hollow waveguides cannot support TEM
TEM requires $k_c = 0$, so a TEM mode would propagate at DC. But a hollow tube DC-shorts itself (no return path) — proof that hollow waveguides need a cutoff.

### Cutoff wavenumber and propagation
For each mode, Helmholtz gives $k_c$ as an eigenvalue. The longitudinal propagation constant is:

$$\gamma_{mn} = \sqrt{k_c^2 - k^2}$$

where $k = \omega\sqrt{\mu\epsilon}$. Two regimes:
- $f > f_c$ ($k > k_c$): $\gamma = jk\sqrt{1-(f_c/f)^2}$ — **propagating** ($e^{-j\beta z}$).
- $f < f_c$ ($k < k_c$): $\gamma = k_c\sqrt{1-(f/f_c)^2}$ — **evanescent** ($e^{-\alpha z}$, no real power transmitted).

### Cutoff frequency
$$\boxed{f_{c,mn} = \frac{c}{2\sqrt{\mu_r\epsilon_r}}\sqrt{(m/a)^2 + (n/b)^2}}$$

for a rectangular waveguide with $a \times b$ cross-section.

### Mode indexing rules (rectangular WG)
- **TM$_{mn}$:** $m \geq 1$, $n \geq 1$ — both must be positive (else $E_z = 0$ everywhere).
- **TE$_{mn}$:** $m, n \geq 0$ but not both zero — TE$_{00}$ would be TEM.
- **Dominant mode** (lowest $f_c$): TE$_{10}$ when $a > b$.

### Wave impedance per mode
$$Z_{TE} = \frac{j\omega\mu}{\gamma} \stackrel{f>f_c}{=} \frac{\eta}{\sqrt{1-(f_c/f)^2}}$$

$$Z_{TM} = \frac{\gamma}{j\omega\epsilon} \stackrel{f>f_c}{=} \eta\sqrt{1-(f_c/f)^2}$$

## TE$_{10}$ field expressions (for reference)
For air-filled WG with $a$ along $x$:
$$E_y = -\frac{j\omega\mu_0 a}{\pi}\sin\!\left(\frac{\pi x}{a}\right)e^{-j\beta_{10} z}$$
$$H_x = \frac{j\beta_{10} a}{\pi}\sin\!\left(\frac{\pi x}{a}\right)e^{-j\beta_{10} z}, \qquad H_z = \cos\!\left(\frac{\pi x}{a}\right)e^{-j\beta_{10} z}$$

## Why it matters / when you use it
- **Power delivery** at microwave frequencies (radar, satellite uplinks) prefers waveguides over coax above ~10 GHz because of lower loss.
- Each mode has its own [[waveguide-cutoff]] — picking operating band is constrained by single-mode operation.
- Cavity resonators ([[cavity-resonator]]) are waveguides closed at both ends.

## Common mistakes
- **Allowing TE$_{00}$ or TM$_{00}$.** Both give zero fields — they don't exist as modes.
- **Treating $\eta$ as the wave impedance.** Inside a WG, $Z_{TE}$ or $Z_{TM}$ depends on frequency; only at $f \to \infty$ does $Z_{TE} \to \eta$.
- **Phase vs group velocity.** $u_p = c/\sqrt{1-(f_c/f)^2}$ is *greater* than $c$; $u_g = c\sqrt{1-(f_c/f)^2}$ is less. Information travels at $u_g$, no laws violated.

## Related
- [[helmholtz-equation]] — parent eigenvalue problem
- [[waveguide-cutoff]] — when does a mode propagate?
- [[cavity-resonator]] — closed waveguide
- [[boundary-conditions-em]] — what PEC walls force
