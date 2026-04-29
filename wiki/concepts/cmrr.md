---
title: Common-Mode Rejection Ratio (CMRR)
type: concept
course: [[eee-335]]
tags: [differential-pair, cmrr, sedra-smith]
sources: [raw/slides/eee-335/unit-6-lecture-34-common-mode-rejection-in-differential-amplifier.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Common-Mode Rejection Ratio (CMRR)

## In one line
CMRR is the ratio of differential gain to common-mode gain — $\text{CMRR} = |A_d / A_{cm}|$ (often expressed in dB) — and is the figure of merit for how well a differential amplifier amplifies the **wanted** differential signal while rejecting the **unwanted** common-mode noise.

## Example first
Differential pair, single-ended output, with $g_m = 1$ mS, $R_D = 10$ k$\Omega$, tail-source resistance $R_{SS} = 1$ M$\Omega$. Find CMRR.

$$A_{d,s.e.} = \tfrac{1}{2} g_m R_D = 5\text{ V/V}$$

$$A_{cm,s.e.} \approx -\frac{R_D}{2 R_{SS}} = -\frac{10\text{k}}{2\text{M}} = -0.005\text{ V/V}$$

$$\text{CMRR} = \left|\frac{A_d}{A_{cm}}\right| = \frac{5}{0.005} = 1000\text{ V/V} = \boxed{60\text{ dB}}$$

For differential output with **matched** loads, CMRR is theoretically infinite — but $R_D$ mismatch $\Delta R_D / R_D$ degrades it to:
$$\text{CMRR}_\text{diff} \approx 2 g_m R_{SS} \cdot \frac{R_D}{\Delta R_D}$$

## The idea
A differential amplifier sees two inputs and ideally outputs only their difference. But two effects degrade rejection:
1. **Finite tail impedance:** if the tail current source has output resistance $R_{SS}$ instead of $\infty$, a common-mode voltage on both inputs causes the tail node to move, which converts to differential current via the half-circuit.
2. **Mismatch:** unequal $R_D$ or $g_m$ causes a common-mode input to produce a non-zero differential output even with perfect $R_{SS}$.

## Formal definition

**Linear (definition):**
$$\text{CMRR} = \left|\frac{A_d}{A_{cm}}\right|$$

**dB:**
$$\text{CMRR}(\text{dB}) = 20 \log_{10} \left|\frac{A_d}{A_{cm}}\right|$$

**For a MOS diff pair, single-ended output** (neglecting $r_o$):
$$A_{d,s.e.} = \tfrac{1}{2} g_m R_D, \qquad A_{cm,s.e.} \approx -\frac{R_D}{2 R_{SS}}$$
$$\text{CMRR}_\text{s.e.} = g_m R_{SS}$$

**For differential output** (matched, neglecting $r_o$):
$$A_{cm,\text{diff}} = 0 \implies \text{CMRR}_\text{diff} = \infty$$

**With $R_D$ mismatch $\Delta R_D / R_D$ (differential output):**
$$A_{cm,\text{diff}} \approx -\frac{\Delta R_D}{2 R_{SS}}, \qquad \text{CMRR}_\text{diff} \approx \frac{g_m R_D}{|A_{cm,\text{diff}}|} = 2 g_m R_{SS} \cdot \frac{R_D}{\Delta R_D}$$

So CMRR scales with **both** the tail-source impedance and the mismatch ratio. Push $R_{SS}$ up (use a cascode current source) and $\Delta R_D / R_D$ down (careful matched layout) for high CMRR.

## Why it matters / when you use it
- **Op-amp PSRR/CMRR specs** are limited by this exact analysis. CMRR > 80 dB is the standard goal.
- **Sensor front-ends** (ECG, strain gauge, thermocouple) live and die by CMRR — power-line interference at 50/60 Hz is mostly common-mode.
- **Tail-source design choice:** simple resistor < simple current mirror < cascode current source < regulated cascode.

## Common mistakes
- **Forgetting that differential output gives ideally infinite CMRR** when matched. People compute single-ended CMRR and get worried, missing that diff output is fine.
- **CMRR depends on $R_{SS}$**, which depends on the tail-source topology. A cascoded mirror gives much higher $R_{SS}$ than a basic mirror.
- **dB conversion.** $20 \log_{10}$, not $10 \log_{10}$ — CMRR is a voltage ratio, not power.

## Related
- [[differential-pair]] — the host topology
- [[current-mirror]] — tail source
- [[cascode-amplifier]] — boost $R_{SS}$
