---
title: Common-Gate Amplifier
type: concept
course:
  - "[[eee-335]]"
tags: [amplifier, cg, current-buffer, sedra-smith]
sources: [raw/slides/eee-335/unit-4-lecture-19-basic-configurations.pdf, raw/slides/eee-335/unit-4-lecture-22-buffers-common-gate-and-source-follower.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Common-Gate Amplifier

## In one line
The common-gate (CG) amplifier — input at source, output at drain, gate grounded (AC) — has very low input resistance ($\approx 1/g_m$), high output resistance ($\approx g_m r_o R_S$), unity short-circuit current gain, and is the canonical **current buffer** that enables the [[cascode-amplifier]].

## Example first
CG with $g_m = 1$ mS, $r_o = 100$ k$\Omega$, source impedance $R_S = 50$ k$\Omega$. Find $R_{\text{in}}$ and $R_{\text{out}}$.

$$R_{\text{in}} \approx \frac{1}{g_m} + \frac{R_L}{g_m r_o} = \frac{1}{1\text{ mS}} + \text{tiny} = 1\text{ k}\Omega$$

$$R_{\text{out}} \approx g_m r_o R_S = (1\text{ mS})(100\text{ k}\Omega)(50\text{ k}\Omega) = 5\text{ M}\Omega$$

So the CG **transforms impedance**: takes a 50 kΩ source impedance and presents 1 kΩ at its input, while presenting 5 MΩ at its output. This is impedance amplification by the factor $g_m r_o = 100$.

## The idea
- **Input at source:** the source terminal sees the input through $1/g_m$ — small-signal current $i = g_m v_{gs}$, with $v_{gs} = -v_{\text{in}}$ (source higher than gate). So $i_{\text{in}} = g_m v_{\text{in}}$ → $R_{\text{in}} = v_{\text{in}}/i_{\text{in}} = 1/g_m$.
- **Output at drain:** same current flows out the drain. So $A_i = i_{\text{out}}/i_{\text{in}} = +1$ (current buffer).
- **Voltage gain $+g_m R_D$:** same magnitude as CS but **non-inverting** (no minus sign).

CG turns a current at its source into an even higher-impedance current at its drain — the perfect "current Darlington."

## Formal definition

**Without $r_o$** (first-order):

| Quantity | Value |
|---|---|
| $R_{\text{in}}$ | $1/g_m$ |
| $R_o$ | $R_D$ |
| $A_{v0}$ | $+g_m R_D$ |
| $A_i$ (short-circuit current gain) | $+1$ A/A |

**With $r_o$ and load $R_L$** (the realistic IC formulas):

$$R_{\text{in}} \approx \frac{1}{g_m}\left(1 + \frac{R_L}{r_o}\right) \;\approx\; \frac{1}{g_m} + \frac{R_L}{g_m r_o}$$

$$R_{\text{out}} \approx g_m r_o R_S \quad\text{(if } R_S \ll r_o\text{)}$$

(Body effect: replace $g_m$ by $g_m(1 + \chi)$ in these — the gate **and** body are AC-grounded, so both contribute.)

**Cascode application:** stack a CG on top of a CS. The CG's low input resistance presents a small load to the CS's drain, but the CG's high output resistance dominates the overall output. The product $A_v = -g_{m1}(g_{m2} r_{o2} r_{o1})$ — a factor of $g_m r_o$ better than basic gain cell. See [[cascode-amplifier]].

## Why it matters / when you use it
- **Cascode top transistor** — its high $R_{\text{out}}$ is the whole point.
- **Current mirror output stage** — same role.
- **High-frequency amplifier** — no Miller multiplication on $C_{gd}$ because input and output are on different terminals (source vs drain). See [[cs-amplifier-frequency-response]] for why CS suffers from Miller.

## Common mistakes
- **Sign confusion.** CG is **non-inverting**: $A_v = +g_m R_D$, not $-g_m R_D$.
- **Forgetting body effect.** Source is the input — $V_{SB}$ varies with the signal, so $g_{mb}$ is in series with $g_m$. Net effective transconductance $g_m + g_{mb} = g_m(1 + \chi)$.
- **Confusing input current and voltage gain.** $A_i = 1$ (current buffer); $A_v = g_m R_D$ (can be large). They're consistent because $R_{\text{in}}$ is small ($v_{\text{in}}/i_{\text{in}} = 1/g_m$, so $A_v = A_i \cdot R_D \cdot g_m = g_m R_D$).
- **$R_{\text{out}}$ depending on $R_S$.** It does — CG output resistance increases linearly with source impedance. That's why CG is "lossy" if you drive it with a low impedance.

## Related
- [[mosfet-small-signal-model]]
- [[common-source-amplifier]] — voltage gain stage
- [[source-follower]] — voltage buffer (the CG's dual)
- [[cascode-amplifier]] — CS + CG combination
- [[current-mirror]] — uses CG-like output transistors
