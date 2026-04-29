---
title: MOSFET I–V Characteristics
type: concept
course: [[eee-335]]
tags: [mosfet, nmos, pmos, triode, saturation, sedra-smith]
sources: [raw/slides/eee-335/unit-1-lecture-1-mos-transistor-structure-and-operation.pdf, raw/slides/eee-335/unit-1-lecture-2-current-voltage-characteristics.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# MOSFET I–V Characteristics

## In one line
An NMOS transistor operates in three regions — **cutoff** ($V_{GS} < V_{tn}$), **triode** ($V_{DS} < V_{OV}$), and **saturation** ($V_{DS} \geq V_{OV}$) — with the drain current $I_D$ following a different formula in each region.

## Example first
NMOS with $V_{tn} = 0.5$ V, $k_n' = 200\ \mu\text{A}/\text{V}^2$, $W/L = 5$. Bias at $V_{GS} = 1.0$ V, $V_{DS} = 1.0$ V.

1. **Check region.** $V_{OV} = V_{GS} - V_{tn} = 0.5$ V. Since $V_{DS} = 1.0 \geq V_{OV} = 0.5$, the device is in **saturation**.
2. **Apply the saturation formula.**
$$I_D = \tfrac{1}{2} k_n' (W/L)\, V_{OV}^2 = \tfrac{1}{2}(200\ \mu)(5)(0.5)^2 = 125\ \mu\text{A}$$

## The idea
$V_{GS}$ above threshold creates an inversion-layer channel. Once the channel exists, $V_{DS}$ controls the current. For small $V_{DS}$ the channel acts like a resistor (linear/triode). As $V_{DS}$ grows toward $V_{OV}$, the channel pinches off at the drain end and the current saturates — further $V_{DS}$ increases (almost) don't push more current through.

## Formal definition

**Triode region** ($V_{GS} \geq V_{tn}$ and $0 \leq V_{DS} \leq V_{OV}$):

$$I_D = k_n' \tfrac{W}{L}\!\left[V_{OV}\,V_{DS} - \tfrac{1}{2}V_{DS}^2\right]$$

**Deep triode** ($V_{DS} \ll V_{OV}$): the $V_{DS}^2$ term drops; the device looks like a resistor with channel resistance

$$r_{DS} = \frac{1}{k_n'(W/L)\,V_{OV}}$$

**Saturation region** ($V_{GS} \geq V_{tn}$ and $V_{DS} \geq V_{OV}$):

$$I_D = \tfrac{1}{2}\, k_n' \tfrac{W}{L}\, V_{OV}^2 \,(1 + \lambda V_{DS})$$

The $\lambda V_{DS}$ term is **channel-length modulation** — see [[mosfet-small-signal-model]] for how it gives rise to $r_o$. We typically set $\lambda = 0$ for DC analysis and only include it when computing small-signal $r_o = 1/(\lambda I_D) \approx V_A / I_D$.

**PMOS:** swap subscripts and signs. With $V_{tp} < 0$, the PMOS is on when $V_{SG} \geq |V_{tp}|$, and saturation is $V_{SD} \geq |V_{OV}|$ where $V_{OV} = V_{SG} - |V_{tp}|$. Drain current flows source-to-drain:

$$I_D = \tfrac{1}{2}\, k_p' \tfrac{W}{L}\, (V_{SG} - |V_{tp}|)^2$$

## Why it matters / when you use it
- **Digital design:** transistors as switches — you need triode (on, low resistance) ↔ cutoff (off).
- **Analog design:** transistors as amplifiers — you need saturation, where small changes in $V_{GS}$ cause large changes in $I_D$ ([[mosfet-small-signal-model]], [[common-source-amplifier]]).
- The **Q-point** of every analog circuit lives somewhere on these curves. Picking $V_{OV}$ trades off speed (high $V_{OV}$ → high $g_m/I$) vs. headroom (low $V_{OV}$ → more swing).

## Common mistakes
- **Wrong region.** Always compute $V_{OV}$ first, then compare to $V_{DS}$. Don't assume saturation.
- **PMOS sign confusion.** Use $V_{SG}$ and $V_{SD}$ (positive) and $|V_{tp}|$ — never plug a negative $V_{tp}$ into the NMOS formula.
- **Forgetting the $\tfrac{1}{2}$** in saturation. The triode formula has $V_{OV}V_{DS} - \tfrac{1}{2}V_{DS}^2$; saturation has $\tfrac{1}{2}V_{OV}^2$.
- **$r_o$ vs $r_{DS}$.** $r_{DS}$ is the deep-triode channel resistance ($V_{DS} \to 0$); $r_o$ is the saturation output resistance from channel-length modulation. Don't mix them up.

## Related
- [[mosfet-body-effect]] — what happens when $V_{SB} \neq 0$
- [[mosfet-small-signal-model]] — linearizing around a Q-point
- [[common-source-amplifier]] — where the saturation Q-point lives
- [[cmos-inverter-vtc]] — uses both regions during switching

## Practice
- See [[eee-335-final-walkthrough]] Unit 1 for region-identification and biasing problems.
