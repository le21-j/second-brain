---
title: MOSFET High-Frequency Model
type: concept
course: [[eee-335]]
tags: [mosfet, high-frequency, capacitances, ft, sedra-smith]
sources: [raw/slides/eee-335/unit-5-lecture-24-high-frequency-mosfet-model.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# MOSFET High-Frequency Model

## In one line
At high frequencies, the small-signal MOSFET model adds four parasitic capacitances — $C_{gs}$, $C_{gd}$, $C_{sb}$, $C_{db}$ — and the **unity-gain frequency** $f_T = g_m / [2\pi(C_{gs} + C_{gd})]$ caps how fast a transistor can amplify.

## Example first
NMOS with $g_m = 1$ mS, $C_{gs} = 50$ fF, $C_{gd} = 10$ fF. Find $f_T$.

$$f_T = \frac{g_m}{2\pi(C_{gs} + C_{gd})} = \frac{10^{-3}}{2\pi(60 \times 10^{-15})} = \boxed{2.65\text{ GHz}}$$

To improve $f_T$: raise $g_m$ (more bias current or larger $W/L$) or shrink the capacitances (smaller $W$ — but then $g_m$ falls). Net result: $f_T \propto V_{OV} \cdot \mu / L^2$, so **shorter channels** and **higher $V_{OV}$** are the levers.

## The idea
DC analysis treats the MOSFET as instantaneous: $i_d = g_m v_{gs}$. At high frequencies, the parasitic capacitances form low-pass paths that **shunt** the input or feed input to output:

- **$C_{gs}$** (gate-source overlap + channel charge) — shunts input to source. Lowest-pass.
- **$C_{gd}$** (gate-drain overlap) — bridges input to output. Cause of [[millers-theorem]] multiplication.
- **$C_{sb}, C_{db}$** (source/drain-body junction caps) — depletion-region depletion capacitance.

## Formal definition

**Capacitance formulas:**

$$C_{ov} = W L_{ov} C_{ox}$$

$$C_{gd} = C_{ov}$$

$$C_{gs} = \tfrac{2}{3} W L\, C_{ox} + C_{ov}$$

$$C_{sb} = \frac{C_{sb,0}}{\sqrt{1 + V_{SB}/V_0}}, \quad C_{db} = \frac{C_{db,0}}{\sqrt{1 + V_{DB}/V_0}}$$

**Hybrid-$\pi$ small-signal model + caps:** add $C_{gs}$ from gate to source, $C_{gd}$ from gate to drain. (Junction caps $C_{sb}, C_{db}$ are usually small enough to neglect for hand analysis when $C_{gs}, C_{gd}$ dominate.)

**Unity-gain frequency** ($\omega_T$): the frequency at which the short-circuit current gain of the basic gain cell equals 1.

$$\boxed{\,\omega_T = \frac{g_m}{C_{gs} + C_{gd}}, \qquad f_T = \frac{\omega_T}{2\pi}\,}$$

**Relation to $V_{OV}$:** since $g_m = k_n V_{OV}$ and $C_{gs} \approx \tfrac{2}{3} W L C_{ox}$, you can show:

$$f_T \propto \frac{\mu V_{OV}}{L^2}$$

— shorter channels and higher $V_{OV}$ both help. This is why scaling (smaller $L$) drove transistor speed for decades.

## Why it matters / when you use it
- **Bandwidth:** $f_T$ is the fundamental speed limit. Any amplifier you build from a transistor has $f_{3\text{dB}} < f_T / |A_v|$ — there's a "gain × bandwidth product" constraint.
- **Process spec:** $f_T$ at a given current is **the** figure of merit advertised by foundries (e.g., "65 nm CMOS, $f_T = 250$ GHz at $I_D = 10$ mA").
- **Miller effect:** $C_{gd}$ at the input of a CS amp is multiplied by $(1 + |A_v|)$ — see [[millers-theorem]] and [[cs-amplifier-frequency-response]].

## Common mistakes
- **Forgetting $C_{gs}$ in the $f_T$ denominator.** Both $C_{gs}$ and $C_{gd}$ contribute. Sometimes simplified to $C_{gs}$ alone if $C_{gd} \ll C_{gs}$.
- **Confusing $f_T$ with $f_{3\text{dB}}$ of an amplifier.** $f_T$ is the transistor's intrinsic limit; $f_{3\text{dB}}$ depends on the **circuit** — load, source impedance, gain. Typically $f_{3\text{dB}} \ll f_T$.
- **Ignoring junction caps in low-impedance nodes.** $C_{sb}, C_{db}$ matter at drain/source nodes with high impedance — neglect them only after checking.

## Related
- [[mosfet-small-signal-model]] — DC version
- [[millers-theorem]] — $C_{gd}$ multiplication
- [[cs-amplifier-frequency-response]] — Miller'd CS bandwidth
- [[octc-method]] — bandwidth from open-circuit time constants
