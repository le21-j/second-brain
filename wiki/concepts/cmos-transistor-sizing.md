---
title: CMOS Transistor Sizing
type: concept
course:
  - "[[eee-335]]"
tags: [cmos, sizing, propagation-delay, fan-out, sedra-smith]
sources: [raw/slides/eee-335/unit-2-lecture-10-transistor-sizing.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# CMOS Transistor Sizing

## In one line
For a matched CMOS inverter, set $L_n = L_p = L_{\min}$ and choose $W_p / W_n = k_n' / k_p' = \mu_n / \mu_p \approx 2$–$3$ so the NMOS and PMOS deliver equal pull-down/pull-up currents — and size general gates so each series stack matches the **reference inverter**'s drive strength.

## Example first
Reference inverter: $W_n / L = 1.5$, $W_p / L = 3.0$ (assume $\mu_n / \mu_p = 2$). Design a 4-input NAND gate that has the same propagation delay.

- **NAND PDN:** 4 NMOS in **series** ($r = 4$). Each must drive $4 \times$ the reference NMOS to match resistance:
  $$W_n^{\text{NAND}} = 4 \cdot W_n^{\text{ref}} = 4 \cdot 1.5\, L_{\min} = 6\, L_{\min}$$
- **NAND PUN:** 4 PMOS in **parallel** ($q = 1$). Each is the same as the reference PMOS:
  $$W_p^{\text{NAND}} = 1 \cdot W_p^{\text{ref}} = 3.0\, L_{\min}$$

For a 4-input NOR (opposite topology): NMOS in parallel ($r=1$, $W_n = 1.5\,L_{\min}$), PMOS in series ($q=4$, $W_p = 12\,L_{\min}$). NOR is much wider — that's why NAND is preferred in static CMOS.

## The idea
**Series stacks degrade drive strength** because resistances add. To compensate, widen each transistor in a stack of $r$ by a factor of $r$ so the total stack resistance equals the reference inverter's single-transistor resistance. Width-scaling preserves drive current; length stays at $L_{\min}$ to minimize parasitic capacitance.

## Formal definition

**Inverter matching** (same fall and rise time):
$$\frac{(W/L)_p}{(W/L)_n} = \frac{k_n'}{k_p'} = \frac{\mu_n}{\mu_p}$$

For typical bulk-CMOS, $\mu_n / \mu_p \approx 2$–$3$, so $W_p \approx 2W_n$ to $3W_n$.

**General-gate sizing** — count series transistors in worst-case PDN ($r$) and PUN ($q$) paths:
$$W_n^{\text{gate}} = r \cdot W_n^{\text{inv}}, \qquad W_p^{\text{gate}} = q \cdot W_p^{\text{inv}}$$

**Inverter chain (fan-out scaling):** to drive a load $C_L$ from a small input cap $C_{\text{in}}$ through $N$ stages, each stage is a factor $S$ larger than the last, with optimum $S \approx 4$ minimizing total delay:

$$N \approx \log_S(C_L/C_{\text{in}}), \qquad t_{p,\text{total}} \approx N \cdot S \cdot t_{p0}$$

where $t_{p0}$ is the intrinsic delay of the smallest inverter.

## Why it matters / when you use it
- **Speed-area-power tradeoff:** larger $W$ → faster drive but higher input capacitance and more dynamic power $P = CV^2 f$.
- **Library characterization:** every standard cell in a digital library is sized so its worst-case path equals a reference inverter's delay — that's how you get composable timing.
- **NAND vs NOR choice:** because NMOS is faster, NAND (PMOS in parallel) is the preferred logic family. NOR's series PMOS stack would need impractical $W_p$.

## Common mistakes
- **Sizing for matching instead of speed.** Matching gives symmetric noise margins but is **not** optimal for speed. For speed, $W_p < \mu_n/\mu_p \cdot W_n$ minimizes input capacitance at the cost of some asymmetry.
- **Forgetting the $L = L_{\min}$ rule.** Increasing $L$ increases gate capacitance ($\propto WL$) without helping drive — only widen, never lengthen, to size up.
- **Counting gates wrong.** $r$ and $q$ are **worst-case series counts**, not parallel — for an N-input NAND, $r = N$ (NMOS series) and $q = 1$ (PMOS parallel).

## Related
- [[cmos-inverter-vtc]] — matched sizing → symmetric VTC
- [[cmos-power-dissipation]] — wider transistors = more dynamic power
- [[mosfet-iv-characteristics]] — current ∝ $W/L$
