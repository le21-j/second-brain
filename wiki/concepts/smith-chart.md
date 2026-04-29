---
title: Smith Chart
type: concept
course: [[eee-341]]
tags: [eee-341, transmission-lines, smith-chart, impedance-matching]
sources: [raw/slides/eee-341/lecture-4-4-introduction-to-the-smith-chart-12-25.pdf, raw/slides/eee-341/lecture-4-5-properties-of-the-smith-chart-15-44.pdf, raw/slides/eee-341/lecture-4-6-impedance-matching-part-1-10-50.pdf, raw/slides/eee-341/lecture-4-7-impedance-matching-part-2-12-08.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Smith Chart

## In one line
A polar plot of the complex reflection coefficient $\Gamma$ overlaid with circles of constant normalized resistance $r$ and reactance $x$ — turns transmission-line impedance gymnastics into compass-and-ruler geometry.

## Example first
Match a load $Z_L = 25 + j50$ Ω to a 50 Ω line with a single short-circuited shunt stub.

1. Normalize: $z_L = 0.5 + j1.0$. Plot the point — it's in the upper half (inductive) of the chart.
2. Move from $z_L$ to $y_L$ by going $180°$ across the chart's center: $y_L \approx 0.4 - j0.8$.
3. Slide along the constant-$|\Gamma|$ circle (toward generator, *clockwise*) until you land on the $g = 1$ circle. Two intersections; pick the closer one. Distance $d \approx 0.13\lambda$ from the load.
4. At the intersection $y_d = 1 - jb$. Need a stub with $y_s = +jb$ to cancel.
5. Solve stub length: SC stub of length $\ell_s = (\lambda/2\pi)\arctan(1/b)$ (or use the chart edges directly).

The result: $y_d + y_s = 1$, perfectly matched at one frequency.

## The idea
The bilinear map $\Gamma = (z-1)/(z+1)$ takes the right half of the complex impedance plane onto the unit disk. Constant-$r$ contours of impedance map to circles tangent to $\Gamma=1$; constant-$x$ contours map to arcs orthogonal to those. Sliding along a lossless line is a pure phase rotation on $\Gamma$, which is a rotation around the center of the chart.

## Formal definition
With normalized impedance $z = Z/Z_0 = r + jx$:

$$\Gamma = \frac{z-1}{z+1}, \qquad z = \frac{1+\Gamma}{1-\Gamma}$$

### Key features
| Point | Meaning |
|---|---|
| Center ($\Gamma = 0$) | $z = 1$ — perfect match |
| Right edge ($\Gamma = +1$) | open circuit ($z \to \infty$) |
| Left edge ($\Gamma = -1$) | short circuit ($z = 0$) |
| Outer circle ($|\Gamma|=1$) | purely reactive loads (no real part) |
| Real axis | purely resistive loads |
| Upper half | inductive ($x > 0$) |
| Lower half | capacitive ($x < 0$) |

### Allowed "moves" (matching game)
1. **Slide along constant-$|\Gamma|$ circle** — adding line length (clockwise = toward generator, $360°$ = $\lambda/2$).
2. **Slide along constant-$r$ circle** — adding series reactance.
3. **Slide along constant-$g$ circle** (admittance chart) — adding shunt susceptance.
4. **Quarter-wave jump** — $z\to 1/z$ at $\lambda/4$ (real-axis points jump across the center).

## Common matching networks

### Quarter-wave transformer
For real $Z_L$:
$$Z_Q = \sqrt{Z_L Z_0}$$
For complex $Z_L$: first slide $\lambda$ down the line until $Z$ is real, then insert $Z_Q$.

### Single-stub (shunt) matching
1. Find $d$ where $y(d)$ lies on the $g = 1$ circle.
2. Add a shunt SC stub of length $\ell_s = (\lambda/2\pi)\arctan(1/b)$ (or OC equivalent: $-\arctan(b)$).

### Lumped L-network
Shunt cap or inductor at distance $d$ chosen so that $\text{Re}(Y_d) = Y_0$, then the lumped element cancels $\text{Im}(Y_d)$.

## Why it matters / when you use it
- **Every** RF design tool (ADS, Microwave Office) shows Smith charts. Reading them by hand still beats simulation for sanity checks.
- Quick visualization of how lines, lumped elements, and stubs change impedance.
- VSWR is read off as the radial distance from center: $|\Gamma|$ → outer = high VSWR.

## Common mistakes
- **Wrong rotation direction.** Going *toward generator* is clockwise on the standard chart; *toward load* is counterclockwise.
- **Forgetting "wavelengths toward generator" scale wraps every $0.5\lambda$.** A full revolution is $\lambda/2$, not $\lambda$.
- **Confusing impedance and admittance charts.** The admittance chart is a $180°$ rotation of the impedance chart — always note which one you're on.

## Related
- [[reflection-coefficient-line]] — what's plotted
- [[transmission-line-model]] — what makes it work
