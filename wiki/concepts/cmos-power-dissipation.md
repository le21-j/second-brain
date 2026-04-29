---
title: CMOS Power Dissipation
type: concept
course: [[eee-335]]
tags: [cmos, power, dynamic, static, energy-delay, sedra-smith]
sources: [raw/slides/eee-335/unit-2-lecture-11-power-dissipation.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# CMOS Power Dissipation

## In one line
A CMOS inverter dissipates **zero static power** when its input is at a rail, and dynamic power $P_{\text{dyn}} = C V_{DD}^2 f$ from charging/discharging the load capacitance every cycle.

## Example first
Inverter with $C_L = 50$ fF, $V_{DD} = 1.8$ V, switching at $f = 1$ GHz.

$$P_{\text{dyn}} = C_L V_{DD}^2 f = (50 \times 10^{-15})(1.8)^2(10^9) = 0.162\text{ mW}$$

A chip with $10^7$ such gates each switching at average $f = 100$ MHz draws $\sim 162$ W on dynamic power alone — which is why **lowering $V_{DD}$** is the most effective lever (quadratic) for power scaling.

## The idea
Every clock cycle, the load capacitor at the output is **charged** to $V_{DD}$ (energy delivered from the supply: $CV_{DD}^2$) and **discharged** to ground (energy dissipated in the NMOS). Half the supplied energy ($\tfrac{1}{2}CV_{DD}^2$) is stored on the cap and dissipated next cycle; the other half is dissipated immediately in the PMOS during charging. Net energy per **full** cycle is $CV_{DD}^2$ — independent of pull-up/pull-down resistance.

## Formal definition

**Static power** (input held at $V_{DD}$ or 0):
$$P_{\text{static}} \approx 0\text{ W}$$
(Subthreshold leakage is nonzero in modern processes, but for hand analysis we treat it as 0.)

**Dynamic power** (full input swing at frequency $f$):
$$\boxed{\,P_{\text{dyn}} = \alpha\, C_L\, V_{DD}^2\, f\,}$$

where $\alpha$ is the **activity factor** — fraction of cycles in which the output actually switches (often $\alpha < 1$ for combinational logic; $\alpha = 1$ for clock nets).

**Short-circuit power** (transient through both transistors during the slope-= -1 region):
$$P_{\text{sc}} \approx \tfrac{1}{2} P_{\text{dyn}}$$
This is the contribution from the brief window when both NMOS and PMOS are saturated simultaneously. Sedra/Smith adopts the $\tfrac{1}{2}$ rule of thumb.

**Power–delay product (PDP):**
$$\text{PDP} = P_{\text{dyn,max}} \cdot t_p = \tfrac{1}{2} C_L V_{DD}^2$$

**Energy–delay product (EDP):**
$$\text{EDP} = \text{PDP} \cdot t_p = \tfrac{1}{2} C_L V_{DD}^2 t_p$$

PDP is technology-independent and characterizes a process; EDP includes speed, so smaller is better in both axes.

## Why it matters / when you use it
- **Voltage scaling** is the most powerful knob: $V_{DD} \downarrow 2\times$ → $P_{\text{dyn}} \downarrow 4\times$, but $t_p \uparrow$, so designers iterate.
- **Clock gating** kills $\alpha$ on inactive blocks.
- **Capacitance reduction** via shorter wires, smaller transistors — but conflicts with speed (need drive strength).
- **Why CMOS won:** before CMOS, NMOS-only logic burned $V_{DD}^2/R_{\text{pull-up}}$ continuously when output was low. CMOS's static-zero-power was the killer feature for VLSI.

## Common mistakes
- **Forgetting $\alpha$.** Not every gate switches every cycle; including activity factor matters for chip-level estimates.
- **Confusing energy and power.** Energy per transition is $CV_{DD}^2$ (charge + discharge = full cycle); power is energy/time = $CV_{DD}^2 f$.
- **Forgetting both halves.** $\tfrac{1}{2}CV_{DD}^2$ is dissipated in the PMOS during charging; the **other** $\tfrac{1}{2}CV_{DD}^2$ is dissipated in the NMOS during discharging. Total per cycle is $CV_{DD}^2$, not $\tfrac{1}{2}CV_{DD}^2$.
- **Static $\neq 0$ in modern processes.** Subthreshold leakage at advanced nodes (sub-65 nm) is non-negligible — but for EEE 335 analysis we ignore it.

## Related
- [[cmos-inverter-vtc]] — the VTC determines the short-circuit window
- [[cmos-transistor-sizing]] — wider transistors → larger $C$ → more dynamic power
- [[mosfet-iv-characteristics]] — peak short-circuit current is the saturation current at $V_M$
