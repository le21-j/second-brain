---
title: MOS Differential Pair
type: concept
course:
  - "[[eee-335]]"
tags: [amplifier, differential-pair, op-amp, sedra-smith]
sources: [raw/slides/eee-335/unit-6-lecture-32-the-mos-differential-pair-1.pdf, raw/slides/eee-335/unit-6-lecture-33-the-mos-differential-pair-2.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# MOS Differential Pair

## In one line
A matched pair of NMOS transistors with their sources tied to a tail current source $I$ amplifies the **difference** $v_{id} = v_{G1} - v_{G2}$ with gain $A_d = g_m R_D$ (single-ended) or $A_d = -g_m R_D$ (differential output), while ideally rejecting common-mode signals.

## Example first
Diff pair with tail $I = 200\ \mu$A, $V_{OV} = 0.2$ V (so $g_m = I/V_{OV} = 1$ mS per side, but each device sees $I/2 = 100\ \mu$A). Drain resistors $R_D = 10$ k$\Omega$.

$$g_m = \frac{2 \cdot I/2}{V_{OV}} = \frac{I}{V_{OV}} = \frac{200\ \mu}{0.2} = 1\text{ mS}$$

$$A_d^{\text{diff}} = g_m R_D = (1\text{ mS})(10\text{ k}\Omega) = 10\text{ V/V}$$

For differential output ($v_{od} = v_{D2} - v_{D1}$): $A_d = -g_m R_D = -10$ V/V (with sign convention).

## The idea
- Both transistors share a common source node, fed by a tail current $I$.
- A **common-mode** input ($v_{G1} = v_{G2} = V_{CM}$) sets each transistor at $I/2$ — perfectly symmetric, zero differential output.
- A **differential** input ($v_{G1} - v_{G2} = v_{id}$) tilts the current: more flows through one device, less through the other, with $\Delta I = g_m v_{id}/2$ on each side. The drain voltages move oppositely.

When the input is small ($v_{id} \ll 2 V_{OV}$), the response is linear with transconductance $g_m = 2(I/2)/V_{OV} = I/V_{OV}$ per side.

## Formal definition

**DC operating point** (with $v_{G1} = v_{G2} = V_{CM}$):
$$I_{D1} = I_{D2} = I/2, \qquad V_{OV} = \sqrt{\frac{I}{k_n'(W/L)}}$$

**Linear (small-signal) regime:**

| Quantity | Single-ended output | Differential output |
|---|---|---|
| $A_d$ | $\tfrac{1}{2} g_m R_D$ | $g_m R_D$ |
| $A_d$ (with $r_o$, current-source load) | $\tfrac{1}{2} g_m (r_o \| R_L)$ | $g_m (r_o \| R_L)$ |
| $g_m$ (each side) | $I/V_{OV}$ | $I/V_{OV}$ |

**Half-circuit principle:** since the source is a virtual ground in differential mode, each side is a CS amplifier with $R_D$ load (or current-source load). Analysis collapses to one CS with input $v_{id}/2$.

**Maximum linear input:**
$$|v_{id,\max}| = \sqrt{2}\, V_{OV}$$

Beyond this, one transistor cuts off and the other carries all the tail current.

**Common-mode gain** (with tail-source resistance $R_{SS}$, single-ended output):
$$A_{cm,s.e.} \approx -\frac{R_D}{2 R_{SS}}$$

For differential output with **matched** loads, $A_{cm,\text{diff}} = 0$ ideally — see [[cmrr]].

**Active-load (current-mirror load):** PMOS mirror at the drains converts both differential currents into one single-ended output with **full** gain (no $\tfrac{1}{2}$ factor):
$$A_d \approx g_m\,(r_{o,\text{NMOS}} \| r_{o,\text{PMOS}})$$

This is the canonical op-amp input stage.

**Input common-mode range:**
$$V_{CM,\min} = -V_{SS} + V_{CS} + V_{OV} + V_t$$
$$V_{CM,\max} = V_{DD} - \tfrac{I}{2}R_D + V_t$$

where $V_{CS}$ is the minimum voltage across the tail current source for it to stay in saturation.

## Why it matters / when you use it
- **Op-amp input stage** — the textbook canonical input front-end. Symmetric topology rejects PSU noise.
- **Sense amplifier** in SRAM read paths — converts a small differential bit-line voltage into a rail-swing logic level.
- **PHY / RF mixers** at higher frequencies — same idea adapted for current commutation.
- **Comparators** when biased into the nonlinear regime.

## Common mistakes
- **Forgetting that $g_m$ uses $I/2$, not $I$.** Each side carries half the tail current. Compute $g_m$ from $I_D = I/2$.
- **Single-ended vs differential gain.** Single-ended (one drain to ground) gives **half** the differential gain. Don't double-count.
- **Common-mode range.** People forget to subtract the tail-source $V_{CS}$ from the bottom — at low supply voltages, this can shrink the input range to nothing.
- **Asymmetry → CMRR.** Real diff pairs always have some $\Delta R_D$ or $\Delta g_m$, which converts common-mode input to differential output. See [[cmrr]].

## Related
- [[common-source-amplifier]] — half-circuit reduces to this
- [[current-mirror]] — tail current source + active load
- [[cascode-amplifier]] — for higher gain in the diff pair
- [[cmrr]] — quantifying common-mode rejection
- [[mosfet-small-signal-model]]
