---
title: Standing Wave Ratio (SWR)
type: concept
course:
  - "[[eee-341]]"
tags: [transmission-lines, antennas, matching, swr]
sources: raw/slides/eee-341/lecture-4-2-review-of-transmission-lines-part-2-14-57.pdf
created: 2026-04-28
updated: 2026-05-06
---

# Standing Wave Ratio (SWR)

## In one line
$\text{SWR} = (1 + |\Gamma|)/(1 - |\Gamma|)$ — the ratio of voltage maximum to voltage minimum on a transmission line, a single number that tells you how well-matched a load is to the line.

## Example first
A half-wave dipole presents $Z_A \approx 73 + j42\,\Omega$ at resonance. Connect it to a $Z_0 = 50\,\Omega$ feedline. The reflection coefficient at the antenna is
$$\Gamma = \frac{Z_A - Z_0}{Z_A + Z_0} = \frac{23 + j42}{123 + j42} \approx 0.31\angle 49°$$
so $|\Gamma| \approx 0.31$ and
$$\text{SWR} = \frac{1 + 0.31}{1 - 0.31} \approx 1.9.$$
That's a **1.9:1 match** — usable, but not great. Below-1.5:1 is the typical engineering target; above 3:1 you're losing serious power.

## The idea
A traveling wave on a mismatched line interferes with its own reflection, producing a standing-wave pattern with peaks ($V_{\max} = V^+(1 + |\Gamma|)$) and troughs ($V_{\min} = V^+(1 - |\Gamma|)$). SWR is the ratio of those:
$$\text{SWR} = \frac{V_{\max}}{V_{\min}} = \frac{1 + |\Gamma|}{1 - |\Gamma|}.$$
SWR = 1 means **perfect match** ($|\Gamma| = 0$), no reflection. SWR = $\infty$ means **total reflection** (open, short, or pure reactive load).

## Inverse relationship
Solving for $|\Gamma|$:
$$|\Gamma| = \frac{\text{SWR} - 1}{\text{SWR} + 1}.$$
The fraction of incident power reflected: $|\Gamma|^2$. Fraction delivered to the load: $1 - |\Gamma|^2$.

## Quick lookup table (memorize)

| SWR | $\|\Gamma\|$ | $\|\Gamma\|^2$ (reflected) | Power delivered |
|:---:|:---:|:---:|:---:|
| 1.0:1 | 0 | 0% | 100% |
| 1.5:1 | 0.20 | 4% | 96% |
| 2.0:1 | 0.33 | 11% | 89% |
| 3.0:1 | 0.50 | 25% | 75% |
| 5.0:1 | 0.67 | 44% | 56% |
| 10:1 | 0.82 | 67% | 33% |

So SWR ≤ 2:1 is "pretty good" — 89% efficiency at the connector. Most ham/RF gear hard-limits transmit power above 3:1 to protect the final amplifier.

## Frequency dependence
A real antenna's $Z_A$ varies with frequency. SWR plotted vs $f$ shows a **dip at the resonant frequency** and rises on either side. Bandwidth of the antenna is conventionally defined as the frequency range where SWR < 2:1 (or sometimes < 1.5:1 for tight specs).

In Lab 5 you'll sweep a half-wave dipole's SWR around 300 MHz and see the characteristic V-shape.

## Why it matters
- **Quick health check** for any antenna installation. One number, one meter.
- **Power efficiency.** High SWR wastes transmit power as heat in the line and at the source.
- **Equipment protection.** Most RF amplifiers see high SWR as risk of damage from reflected power.
- **Bandwidth metric.** SWR < 2:1 bandwidth defines the usable operating range.

## Common mistakes
- **SWR is a magnitude, not a phase.** It tells you how mismatched, not what kind of mismatch. To redesign matching, you also need $\angle\Gamma$ — see [[smith-chart]].
- **SWR is line-independent in lossless lines** but degrades in lossy ones. Long coax can mask a bad antenna because cable loss attenuates the reflected wave.
- **"VSWR" = "SWR"** — same thing, the V is for "voltage" (you also occasionally see "ISWR" for current SWR; identical for TEM lines).

## Related
- [[reflection-coefficient-line]] — $\Gamma_L = (Z_L - Z_0)/(Z_L + Z_0)$
- [[transmission-line-model]] — where standing waves come from
- [[smith-chart]] — graphical SWR + impedance matching tool
- [[half-wave-dipole]] — example of a 73-Ω antenna driving a 50-Ω line

## Practice
- [[eee-341-lab-5-walkthrough]] — Section 3.1 sweeps SWR for a half-wave dipole
