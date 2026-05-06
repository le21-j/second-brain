---
title: Transmission Line Model & Characteristic Impedance
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, transmission-lines, telegraphers-equations, characteristic-impedance]
sources: [raw/slides/eee-341/lecture-4-1-review-of-transmission-lines-part-1-18-49.pdf, raw/slides/eee-341/lecture-4-2-review-of-transmission-lines-part-2-14-57.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Transmission Line Model

## In one line
A two-wire path becomes a transmission line when its length is comparable to a wavelength; model it as a chain of infinitesimal $R\,dz$, $L\,dz$ in series and $G\,dz$, $C\,dz$ in shunt — solving the resulting telegrapher's equations gives traveling waves with characteristic impedance $Z_0 = \sqrt{(R+j\omega L)/(G+j\omega C)}$.

## Example first
RG-58 coaxial cable. Per-unit-length parameters (lossless approximation): $L' = 250$ nH/m, $C' = 100$ pF/m. Characteristic impedance:

$$Z_0 = \sqrt{L'/C'} = \sqrt{250\times 10^{-9}/100\times 10^{-12}} = \sqrt{2500} = 50\,\Omega$$

Phase velocity:
$$u_p = 1/\sqrt{L'C'} = 1/\sqrt{(250\times 10^{-9})(100\times 10^{-12})} = 2\times 10^8 \text{ m/s} \approx 0.67c$$

So a 1 ns rise time delivers a wave that travels 20 cm — anything longer is "distributed."

## The idea
At each $dz$ slice, Kirchhoff gives an inductive volt drop $L\,\partial i/\partial t$ and a capacitive shunt current $C\,\partial v/\partial t$. Take $dz\to 0$ and you get the **telegrapher's equations**, whose solutions are traveling-wave voltages $V_0^\pm e^{\mp\gamma z}$.

## Formal definition

### Telegrapher's equations (lossless form)
$$\frac{\partial v}{\partial z} = -L'\frac{\partial i}{\partial t}, \qquad \frac{\partial i}{\partial z} = -C'\frac{\partial v}{\partial t}$$

Combine to get the 1-D wave equation $\partial^2 v/\partial z^2 = L'C'\,\partial^2 v/\partial t^2$.

### Time-harmonic / lossy form
$$\frac{dV}{dz} = -(R' + j\omega L')I, \qquad \frac{dI}{dz} = -(G' + j\omega C')V$$

Propagation constant:
$$\gamma = \alpha + j\beta = \sqrt{(R' + j\omega L')(G' + j\omega C')}$$

Characteristic impedance:
$$\boxed{Z_0 = \sqrt{\frac{R' + j\omega L'}{G' + j\omega C'}}}$$

Lossless limit ($R'=G'=0$): $Z_0 = \sqrt{L'/C'}$, real; $\beta = \omega\sqrt{L'C'}$; $\alpha = 0$.

### General solution on a finite line
$$V(z) = V_0^+ e^{-\gamma z} + V_0^- e^{+\gamma z}$$
$$I(z) = \frac{1}{Z_0}\bigl(V_0^+ e^{-\gamma z} - V_0^- e^{+\gamma z}\bigr)$$

## Lumped vs distributed (rules of thumb)
| Test | Lumped | Distributed |
|---|---|---|
| Rise time vs travel time | $T_r/T_d > 10$ | $T_r/T_d < 1$ |
| Period vs travel time | $T_d/T < 0.01$ | $T_d/T > 0.1$ |
| Length vs wavelength | $\ell/\lambda < 0.01$ | $\ell/\lambda > 0.1$ |

## Why it matters / when you use it
- Foundation of all RF / microwave design and high-speed digital signal integrity.
- [[reflection-coefficient-line]] and [[smith-chart]] are tools applied directly on top of this model.
- TEM modes of waveguides are also "transmission lines" in this sense.

## Common mistakes
- **Using $Z_0$ in place of input impedance.** $Z_0$ is the impedance of the line itself; $Z_{\text{in}}$ at a point depends on what's at the load and how much line is between you and it.
- **Treating a 1 cm trace at 5 GHz as lumped.** $\lambda \approx 6$ cm in air, $\sim 4$ cm on FR-4. The trace is $0.25\lambda$ — *very* distributed.

## Related
- [[reflection-coefficient-line]] — load-driven $\Gamma_L$
- [[smith-chart]] — the $Z\leftrightarrow\Gamma$ visualization
- [[plane-wave-lossless]] — TEM modes are transmission lines
- [[waveguide-modes]] — non-TEM "transmission lines" with cutoff
