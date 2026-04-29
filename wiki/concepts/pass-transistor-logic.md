---
title: Pass Transistor Logic and Transistors as Switches
type: concept
course: [[eee-335]]
tags: [cmos, pass-transistor, switch, transmission-gate, sedra-smith]
sources: [raw/slides/eee-335/unit-3-lecture-12-transistors-as-switches.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Pass Transistor Logic and Transistors as Switches

## In one line
A single NMOS transistor passes a logic-0 cleanly but only delivers a "poor 1" capped at $V_{DD} - V_t$ (worse with body effect); a CMOS **transmission gate** (parallel NMOS + PMOS) fixes the problem at the cost of two transistors and an inverted control signal.

## Example first
NMOS pass transistor with gate held at $V_{DD} = 1.8$ V, $V_{t0} = 0.5$ V, $\gamma = 0.4\ \text{V}^{1/2}$, $2\phi_F = 0.7$ V. Input switches from 0 to $V_{DD}$. What's the steady-state output across a load capacitor?

The NMOS keeps charging until $V_{GS} = V_t$, i.e., $v_O = V_{DD} - V_t$. But $V_t$ rises with $V_{SB} = v_O$ (body tied to ground):
$$V_t(v_O) = 0.5 + 0.4(\sqrt{0.7 + v_O} - \sqrt{0.7})$$

Iterate: at $v_O = 1.0$ V → $V_t = 0.836$ → next-iteration $v_O = 1.8 - 0.836 = 0.964$. Converging on $\boxed{v_O \approx 0.96\text{ V}}$ — about $V_{DD}/2$, far short of $V_{DD}$.

## The idea
- **NMOS is good at pulling down** (passing 0): when $v_I = 0$, the source is at 0, $V_{GS} = V_{DD}$, the device stays strongly on. Output drops cleanly to 0.
- **NMOS is bad at pulling up** (passing 1): when $v_I = V_{DD}$, the **source is the output** (lower terminal), so as $v_O$ rises, $V_{GS}$ shrinks. Once $V_{GS} \leq V_t$, the device cuts off — and body effect makes $V_t$ even bigger.

PMOS has the opposite asymmetry. Combine them and you get a **transmission gate** that's strong in both directions.

## Formal definition

**NMOS pass transistor (low → high transition):**
- At $t = 0^+$: $V_{GS} = V_{DD}$, device in saturation, charging current $I_D = \tfrac{1}{2} k_n (V_{DD} - V_t)^2$.
- As $v_O$ rises: source rises, $V_{GS}$ shrinks, $V_t$ grows (body effect).
- Stops at $v_O = V_{DD} - V_t(v_O)$ — the **poor 1**.

**NMOS pass transistor (high → low transition):**
- At $t = 0^+$: $v_I = 0$ becomes the source, $v_O = V_{DD}$ is the drain. $V_{GS} = V_{DD}$.
- No body effect ($V_{SB} = 0$).
- $v_O$ falls cleanly to 0. **Strong 0.**

**CMOS Transmission Gate** — NMOS and PMOS in parallel with inverted gate signals:
- Pass 1: PMOS dominates, passes $V_{DD}$ cleanly.
- Pass 0: NMOS dominates, passes 0 cleanly.
- Cost: 2 transistors + a complement signal.

**DC restorer (keeper):** a small PMOS feedback transistor that snaps a "poor 1" back up to $V_{DD}$ once an inverter sees the high input. Used in dynamic logic and SRAM read paths.

## Why it matters / when you use it
- **SRAM cells** use NMOS access transistors — see [[sram-cell]] — and the body-effect-degraded read voltage drives the sense-amp design.
- **Multiplexers** can be built from transmission gates with fewer transistors than a static-CMOS implementation (4T MUX2-1 vs 8T NAND-NAND).
- **Latches and flip-flops** use transmission gates as the storage-loop switches.
- **Analog switches** (e.g., in [[chopper-amplifier]]) — TG passes both polarities of analog signals.

## Common mistakes
- **Forgetting which terminal is source.** "The source is the lower-voltage terminal" — when $v_I$ is high and $v_O$ is rising, the source is $v_O$, **not** $v_I$. This determines $V_{GS}$ and whether the device is saturated or cut off.
- **Forgetting body effect.** The poor 1 isn't just $V_{DD} - V_{t0}$ — it's $V_{DD} - V_t(v_O)$ with $V_t$ self-consistently solved for. The result is even worse than the textbook $V_{DD} - V_{t0}$ estimate.
- **Cascading PT logic carelessly.** Each NMOS pass loses a $V_t$. Two NMOS in series → $V_{DD} - 2V_t$ output. That's why TG or static CMOS is preferred for deep logic.

## Related
- [[mosfet-body-effect]] — why $V_t$ rises during pull-up
- [[sram-cell]] — uses NMOS access transistors, accepts the asymmetry
- [[mosfet-iv-characteristics]] — saturation/triode regions during charge
