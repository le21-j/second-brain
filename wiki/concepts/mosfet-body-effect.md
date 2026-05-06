---
title: MOSFET Body Effect
type: concept
course:
  - "[[eee-335]]"
tags: [mosfet, body-effect, threshold-voltage, sedra-smith]
sources: [raw/slides/eee-335/unit-1-lecture-4-body-effect-and-other-topics.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# MOSFET Body Effect

## In one line
When the source-to-body voltage $V_{SB} > 0$, the MOSFET threshold voltage **increases** above its $V_{SB} = 0$ value $V_{t0}$ — this is the body effect, and it's why NMOS pass transistors deliver a "poor 1."

## Example first
NMOS with $V_{t0} = 0.8$ V, $2\phi_F = 0.7$ V (so $\phi_F = 0.35$ V), $\gamma = 0.4\ \text{V}^{1/2}$. Find $V_t$ when $V_{SB} = 3$ V.

$$V_t = V_{t0} + \gamma\!\left(\sqrt{2\phi_F + V_{SB}} - \sqrt{2\phi_F}\right)$$

$$V_t = 0.8 + 0.4\!\left(\sqrt{0.7 + 3} - \sqrt{0.7}\right) = 0.8 + 0.4(1.924 - 0.837) = 0.8 + 0.435 = \boxed{1.23\text{ V}}$$

The threshold went from $0.8$ V to $1.23$ V — a $54\%$ increase — because the source floats $3$ V above the body.

## The idea
The MOSFET has a fourth terminal — the **body** — which is normally tied to the most-negative supply (ground for NMOS, $V_{DD}$ for PMOS). When the source is **not** at the body voltage, the depletion region under the channel widens, requiring a larger $V_{GS}$ to invert the channel. Hence $V_t$ rises.

## Formal definition

$$\boxed{\,V_t = V_{t0} + \gamma\!\left(\sqrt{2\phi_F + V_{SB}} - \sqrt{2\phi_F}\right)\,}$$

- $V_{t0}$: threshold at $V_{SB} = 0$
- $\gamma = \sqrt{2 q N_A \epsilon_s}/C_{ox}$: body-effect parameter (units $\text{V}^{1/2}$)
- $\phi_F$: bulk Fermi potential (units V)
- $V_{SB}$: source-to-body voltage (positive for NMOS)

In **small-signal** terms, the body adds a second transconductance $g_{mb}$:

$$g_{mb} = g_m \cdot \chi, \qquad \chi = \frac{\gamma}{2\sqrt{2\phi_F + V_{SB}}}$$

Typically $\chi \approx 0.1$–$0.3$, so $g_{mb}$ is a 10–30% correction on $g_m$. See [[mosfet-small-signal-model]].

## Why it matters / when you use it
- **NMOS pass transistor:** as the output rises, $V_{SB}$ rises, $V_t$ rises, and the transistor turns off when $V_O = V_{DD} - V_t$. The output never reaches $V_{DD}$ — the "poor 1" — see [[pass-transistor-logic]].
- **Cascode amplifier:** the upper transistor has $V_{SB} > 0$, so its $V_t$ is higher and $g_{mb}$ contributes to $R_{out}$. See [[cascode-amplifier]].
- **Stacked-source circuits** (differential pair tail, current mirrors with source degeneration): always check whether $V_{SB} \neq 0$.

## Common mistakes
- **Plugging $V_{SB}$ into the wrong square root.** The formula is $\sqrt{2\phi_F + V_{SB}} - \sqrt{2\phi_F}$, **not** $\sqrt{V_{SB}}$ alone — the offset by $2\phi_F$ matters at small $V_{SB}$.
- **Sign for PMOS.** PMOS needs $V_{BS} > 0$ (body above source) for the analogous effect; flip $V_{SB} \to V_{BS}$.
- **Ignoring it in cascodes.** The upper transistor in a cascode always has $V_{SB} > 0$ unless the body is tied to its source — usually it isn't, in standard CMOS.

## Related
- [[mosfet-iv-characteristics]] — where $V_t$ enters the current equations
- [[mosfet-small-signal-model]] — $g_{mb}$ as the body-effect transconductance
- [[pass-transistor-logic]] — the "poor 1" gotcha
- [[cascode-amplifier]] — body effect in the upper transistor
