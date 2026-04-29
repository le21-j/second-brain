---
title: MOSFET Small-Signal Model
type: concept
course: [[eee-335]]
tags: [mosfet, small-signal, gm, ro, hybrid-pi, t-model, sedra-smith]
sources: [raw/slides/eee-335/unit-4-lecture-18-small-signal-model.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# MOSFET Small-Signal Model

## In one line
Around a Q-point in saturation, the MOSFET is linear: a small input $v_{gs}$ produces a small drain current $i_d = g_m v_{gs} + v_{ds}/r_o$, captured by a hybrid-$\pi$ model with transconductance $g_m$ and output resistance $r_o$.

## Example first
NMOS biased at $I_D = 100\ \mu\text{A}$, $V_{OV} = 0.2$ V, $V_A = 10$ V. Find $g_m$ and $r_o$.

$$g_m = \frac{2 I_D}{V_{OV}} = \frac{2 \cdot 100\,\mu}{0.2} = 1000\ \mu\text{A/V} = 1\text{ mS}$$

$$r_o = \frac{V_A}{I_D} = \frac{10}{100\,\mu} = 100\text{ k}\Omega$$

**Intrinsic gain:**
$$A_{v0} = -g_m r_o = -(1\text{ mS})(100\text{ k}\Omega) = -100\text{ V/V}$$

So this single transistor (with an ideal current-source load) can give about $40$ dB of voltage gain.

## The idea
DC bias holds the device at a fixed point on the saturation $I$–$V$ curve. **Small** signals around that point see a linear circuit:
- **$g_m$** is the slope of the $I_D$-vs-$V_{GS}$ curve at the Q-point — how much current changes per volt of input.
- **$r_o$** is the inverse slope of the $I_D$-vs-$V_{DS}$ curve — captures channel-length modulation as a finite output resistance.
- **$g_{mb}$** is the body-effect transconductance — extra current per volt of $v_{bs}$, see [[mosfet-body-effect]].

## Formal definition

**Three equivalent forms of $g_m$:**
$$\boxed{\,g_m = k_n'\!\left(\tfrac{W}{L}\right) V_{OV} \;=\; \frac{2 I_D}{V_{OV}} \;=\; \sqrt{2 k_n' (W/L) I_D}\,}$$

(All equal — pick whichever you have data for. $g_m = 2 I_D / V_{OV}$ is usually the fastest in problems.)

**Output resistance from channel-length modulation:**
$$r_o = \frac{1}{\lambda I_D} = \frac{V_A}{I_D}$$

where $V_A = 1/\lambda$ is the **Early voltage** (often $V_A = V_A' \cdot L$, so longer channels → larger $r_o$).

**Body-effect transconductance:**
$$g_{mb} = \chi g_m, \qquad \chi = \frac{\gamma}{2\sqrt{2\phi_F + V_{SB}}}, \quad \chi \approx 0.1\text{–}0.3$$

**Hybrid-$\pi$ small-signal current equation:**
$$i_d = g_m v_{gs} + g_{mb} v_{bs} + \frac{v_{ds}}{r_o}$$

**T-model** equivalent (some configurations are easier in the T):
- Current source $g_m v_{gs}$ between drain and source.
- Resistance $1/g_m$ from gate to source (gate sees the source through this).
- $r_o$ between drain and source.

**Intrinsic voltage gain** (best a single transistor can do, with an ideal current-source load):
$$A_{v0,\text{intrinsic}} = -g_m r_o = -\frac{2 V_A}{V_{OV}}$$

## Why it matters / when you use it
- **All single-stage analog amplifiers** ([[common-source-amplifier]], [[common-gate-amplifier]], [[source-follower]]) reduce to this model — the only difference is which terminal is grounded.
- The **bias** sets $g_m, r_o$, so bias and gain are linked: more $I_D$ → more $g_m$ but less $r_o$. The product $g_m r_o = 2V_A/V_{OV}$ depends only on $V_{OV}$ and process.
- Modeling at higher frequencies adds capacitances ($C_{gs}, C_{gd}$) — see [[mosfet-high-frequency-model]].

## Common mistakes
- **Confusing $r_o$ with $r_{DS}$.** $r_{DS}$ is the **deep-triode** small-signal resistance ($V_{DS} \to 0$, channel acts as a resistor); $r_o$ is the **saturation** small-signal output resistance. Different physics, different formulas.
- **Forgetting the negative sign.** $A_{v0} = -g_m r_o$ for a CS — the inversion is real (input up → output down).
- **Using $g_m = k_n V_{OV}$ when you have $I_D$.** All three formulas are equivalent; use $2 I_D / V_{OV}$ when you have $I_D$ — it's faster.
- **Neglecting $g_{mb}$ in cascodes.** When $V_{SB} \neq 0$ (top transistor of a cascode), $g_{mb}$ adds to $g_m$ and matters.

## Related
- [[mosfet-iv-characteristics]] — where $g_m$ comes from (slope at Q-point)
- [[mosfet-body-effect]] — origin of $g_{mb}$
- [[common-source-amplifier]], [[common-gate-amplifier]], [[source-follower]] — three configurations
- [[mosfet-high-frequency-model]] — adds $C_{gs}, C_{gd}$
