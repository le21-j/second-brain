---
title: CMOS Inverter VTC and Noise Margins
type: concept
course:
  - "[[eee-335]]"
tags: [cmos, inverter, vtc, noise-margin, sedra-smith]
sources: [raw/slides/eee-335/unit-2-lecture-7-digital-logic-inverters.pdf, raw/slides/eee-335/unit-2-lecture-8-cmos-inverters.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# CMOS Inverter VTC and Noise Margins

## In one line
The voltage transfer characteristic (VTC) of a matched CMOS inverter has **rail-to-rail swing** ($V_{OL} = 0$, $V_{OH} = V_{DD}$) and a sharp transition centered at $V_M = V_{DD}/2$, giving symmetric noise margins $NM_L = NM_H = \tfrac{1}{8}(3V_{DD} + 2V_t)$.

## Example first
Matched CMOS inverter with $V_{DD} = 1.8$ V, $V_t = V_{tn} = |V_{tp}| = 0.5$ V. Compute the noise margins.

$$NM_L = NM_H = \tfrac{1}{8}(3V_{DD} + 2V_t) = \tfrac{1}{8}(3 \cdot 1.8 + 2 \cdot 0.5) = \tfrac{1}{8}(6.4) = 0.8\text{ V}$$

So the inverter can tolerate $\pm 0.8$ V of noise on either rail before failing — about $44\%$ of $V_{DD}$, which is excellent.

## The idea
A CMOS inverter is an **NMOS pull-down** (PDN) and a **PMOS pull-up** (PUN) with their drains tied to the output. As $v_I$ sweeps from 0 to $V_{DD}$ the circuit cycles through 5 regions:

| $v_I$ range | NMOS region | PMOS region | $v_O$ |
|---|---|---|---|
| $0 \leq v_I < V_{tn}$ | cutoff | triode | $V_{DD}$ |
| $V_{tn} \leq v_I < V_{IL}$ | saturation | triode | high, $\approx V_{DD}$ |
| $V_{IL} \leq v_I \leq V_{IH}$ | saturation | saturation | sharp transition |
| $V_{IH} < v_I \leq V_{DD} - |V_{tp}|$ | triode | saturation | low, $\approx 0$ |
| $v_I > V_{DD} - |V_{tp}|$ | triode | cutoff | $0$ |

The transition is sharp because in the middle region both transistors are in saturation, where $I_D \propto V_{OV}^2$ — small input changes cause large current changes, and small currents move the output voltage rapidly because the only loading is the (small) gate capacitance of the next stage.

## Formal definition

For a **matched** CMOS inverter ($k_n'(W/L)_n = k_p'(W/L)_p$ and $V_{tn} = |V_{tp}| = V_t$):

**Output rails (no static current):**
$$V_{OL} = 0, \qquad V_{OH} = V_{DD}$$

**Switching threshold (midpoint):**
$$V_M = V_{DD}/2$$

**Critical input voltages** (where the VTC has slope $-1$):
$$V_{IL} = \tfrac{1}{8}(3V_{DD} + 2V_t), \qquad V_{IH} = \tfrac{1}{8}(5V_{DD} - 2V_t)$$

**Noise margins:**
$$NM_L = V_{IL} - V_{OL} = \tfrac{1}{8}(3V_{DD} + 2V_t)$$
$$NM_H = V_{OH} - V_{IH} = \tfrac{1}{8}(3V_{DD} + 2V_t)$$

For matched transistors, $NM_L = NM_H$ — the VTC is symmetric about $V_M$.

## Why it matters / when you use it
- **Logic cascading:** noise margins tell you how much noise a logic gate can absorb before passing it on. CMOS's rail-to-rail swing + symmetric margins are why it dominates digital design.
- **Sizing intuition:** to get matching, you need $W_p / W_n = \mu_n / \mu_p \approx 2$–$3$ — see [[cmos-transistor-sizing]].
- **Mismatched inverter:** moves $V_M$ away from $V_{DD}/2$, asymmetrizes $NM_L$ vs $NM_H$. Sometimes deliberate (e.g., a "skewed" inverter for fast falling edges).

## Common mistakes
- **Forgetting both transistors are saturated** in the middle region. People sometimes write a triode equation for one of them and get the wrong $V_{IL}$.
- **Confusing $V_M$ with $V_{IL}$ / $V_{IH}$.** $V_M$ is where $v_I = v_O$ (a single point); $V_{IL}/V_{IH}$ are where slope = $-1$. They're related but not the same.
- **Plugging the wrong $V_t$.** The formula assumes $V_{tn} = |V_{tp}| = V_t$. For mismatched thresholds, redo the slope-$=-1$ derivation with separate $V_{tn}$, $|V_{tp}|$.

## Related
- [[mosfet-iv-characteristics]] — where the region equations come from
- [[cmos-transistor-sizing]] — $W_p/W_n$ for matching
- [[cmos-power-dissipation]] — the inverter's dynamic energy budget
- [[pass-transistor-logic]] — when you can't get rail-to-rail swing

## Practice
- See [[eee-335-final-walkthrough]] Unit 2 problems on $NM_L/NM_H$ calculation and matched-inverter sizing.
