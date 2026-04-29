---
title: Common-Source Amplifier
type: concept
course: [[eee-335]]
tags: [amplifier, cs, gain, sedra-smith]
sources: [raw/slides/eee-335/unit-4-lecture-19-basic-configurations.pdf, raw/slides/eee-335/unit-4-lecture-21-the-basic-gain-cell.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Common-Source Amplifier

## In one line
The common-source (CS) amplifier — input at gate, output at drain, source grounded — is the workhorse voltage amplifier with infinite input resistance, output resistance equal to the drain load, and gain $-g_m R_L'$ where $R_L' = r_o \| R_D \| R_L$.

## Example first
CS amplifier with $g_m = 1$ mS, $r_o = 100$ k$\Omega$, drain resistor $R_D = 20$ k$\Omega$, load $R_L = 50$ k$\Omega$. Find midband gain.

$$R_L' = r_o \| R_D \| R_L = 100\text{k} \| 20\text{k} \| 50\text{k}$$

$$\frac{1}{R_L'} = \frac{1}{100} + \frac{1}{20} + \frac{1}{50} = 0.01 + 0.05 + 0.02 = 0.08\ \text{(k}\Omega^{-1}\text{)}$$

$$R_L' = 12.5\text{ k}\Omega \implies A_v = -g_m R_L' = -(1\text{ mS})(12.5\text{ k}\Omega) = \boxed{-12.5\text{ V/V}}$$

The $r_o$ shunts the load — without channel-length modulation, you'd have $R_L' = R_D \| R_L = 14.3$ k$\Omega$ and gain $-14.3$ V/V.

## The idea
- **Input at the gate:** infinite DC input resistance ($R_{\text{in}} = \infty$).
- **Output at the drain:** small-signal current $i_d = g_m v_{gs}$ flows through the load, generating output voltage $v_o = -i_d R_L'$. The minus sign comes from the convention that $i_d$ flows **into** the drain.
- **Source grounded:** so $v_{gs} = v_i$ directly, no degeneration.

The **basic gain cell** is a CS amplifier with a current-source load instead of a resistor — gives the maximum possible gain of $-g_m r_o$.

## Formal definition

**CS with passive resistor load $R_D$, output load $R_L$** (neglecting $r_o$):

| Quantity | Value |
|---|---|
| $R_{\text{in}}$ | $\infty$ |
| $R_o$ | $R_D$ |
| $A_{v0}$ (open circuit) | $-g_m R_D$ |
| $A_v$ (with load $R_L$) | $-g_m (R_D \| R_L)$ |
| $G_v$ (overall, $v_o/v_{\text{sig}}$) | $-g_m (R_D \| R_L)$ if $R_{\text{sig}}$ ignored |

**With $r_o$ included** (necessary for IC analysis):
$$A_v = -g_m\,(r_o \| R_D \| R_L)$$

**CS with source resistor $R_S$ (degeneration)** — $R_S$ between source and ground:
$$A_v = -\frac{g_m\,(R_D \| R_L)}{1 + g_m R_S}$$

For $g_m R_S \gg 1$: $A_v \approx -(R_D \| R_L)/R_S$ — gain is set by **resistor ratio**, much more linear and PVT-tolerant. Trade gain for stability and bandwidth.

**Basic gain cell** (CS with ideal current-source load):
$$A_{v0} = -g_m r_o = -\frac{2 V_A}{V_{OV}}$$

This is the **intrinsic gain** of the transistor — the best a single CS stage can do.

**Real (non-ideal) current-source load** (e.g., PMOS with output resistance $r_{o2}$):
$$A_{v0} = -g_{m1}(r_{o1} \| r_{o2}) = -\tfrac{1}{2} g_m r_o\quad\text{if } r_{o1} = r_{o2}$$

So a "real" basic gain cell loses 6 dB compared to the intrinsic ceiling.

## Why it matters / when you use it
- **First stage of any voltage amplifier** — high $R_{\text{in}}$ doesn't load the source.
- **Op-amp input stages** — CS-style differential pair is the canonical input front-end. See [[differential-pair]].
- **Cascoded** to boost output resistance — see [[cascode-amplifier]] — when the basic gain cell isn't enough.

## Common mistakes
- **Sign of the gain.** Always negative for a CS — input at gate, output at drain, inverter behavior.
- **Forgetting $r_o$.** In IC design (no big resistors available), $r_o$ is often the dominant load — never neglect it once you have a current-source instead of $R_D$.
- **Assuming $R_S$ helps gain.** It doesn't — degeneration **lowers** gain. It helps **bandwidth** and **linearity**.
- **Open-circuit vs loaded gain.** $A_{v0}$ is with $R_L = \infty$; $A_v$ includes $R_L$. They are different by the divider $R_L/(R_L + R_o)$.

## Related
- [[mosfet-small-signal-model]] — where $g_m$ and $r_o$ come from
- [[common-gate-amplifier]] — different terminal grounded, very different impedances
- [[source-follower]] — output at source, gain $\approx 1$
- [[cascode-amplifier]] — boost the basic gain cell's output resistance
- [[cs-amplifier-frequency-response]] — bandwidth analysis with Miller
