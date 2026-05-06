---
title: Cascode Amplifier
type: concept
course:
  - "[[eee-335]]"
tags: [amplifier, cascode, cs-cg, gain-boost, sedra-smith]
sources: [raw/slides/eee-335/unit-6-lecture-cca-cascode-amplifier.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Cascode Amplifier

## In one line
A cascode is a CS amplifier (current source) loaded by a CG amplifier (current buffer); the CG's high output resistance ($\approx g_{m2} r_{o2} r_{o1}$) boosts the CS gain by a factor of $g_m r_o$, giving total intrinsic gain $\approx (g_m r_o)^2$ instead of $g_m r_o$.

## Example first
Two matched transistors: $g_m = 1$ mS, $r_o = 100$ k$\Omega$. Compare basic CS (current-source load) vs cascode (current-source load).

**Basic gain cell** (CS with ideal current-source load):
$$A_{v0,\text{CS}} = -g_m r_o = -100\text{ V/V} = -40\text{ dB}$$

**Cascode** (with **ideal** current-source load):
$$R_o^{\text{cascode}} = g_m r_o \cdot r_o = (100)(100\text{ k}) = 10\text{ M}\Omega$$

$$A_{v0,\text{cascode}} = -g_m R_o = -(1\text{ mS})(10\text{ M}\Omega) = \boxed{-10{,}000\text{ V/V} = -80\text{ dB}}$$

That's **100×** the basic gain cell. Caveat: this is **only** with an ideal current-source load. With a realistic PMOS load $r_{o3} \ll R_o$, the gain is throttled back to $-g_m r_{o3}$ — a cascode-on-cascode load is needed to retain the boost.

## The idea
The gain bottleneck of the basic gain cell is its output resistance $r_o$. A cascode breaks that bottleneck by stacking a CG on top of the CS — the CG's input is the CS's drain, and the CG presents an enormous output resistance at its drain.

- **CS (bottom):** generates current $i_d = g_m v_i$ in response to input voltage. Acts as transconductor.
- **CG (top):** current buffer — passes the same current through with $A_i = 1$, but transforms the impedance from $r_{o1}$ at its source to $\sim g_{m2} r_{o2} r_{o1}$ at its drain.

## Formal definition

**Output resistance** (NMOS cascode = NMOS CS + NMOS CG):
$$R_o^{\text{cascode}} \approx g_{m2}\,r_{o2}\,r_{o1}$$

(With body effect: replace $g_{m2}$ by $g_{m2} + g_{mb2} = g_{m2}(1 + \chi)$.)

**Intrinsic gain** (with ideal current source load):
$$A_{v0} = -g_{m1}\,R_o = -g_{m1}\,(g_{m2}\,r_{o2}\,r_{o1})$$

If matched ($g_{m1} = g_{m2} = g_m$, $r_{o1} = r_{o2} = r_o$):
$$\boxed{\,A_{v0} \approx -(g_m r_o)^2\,}$$

**With realistic PMOS current-source load** (output resistance $r_{o3}$):
$$A_v \approx -g_{m1}\,(R_o \| r_{o3}) \approx -g_{m1}\,r_{o3}$$

since $r_{o3} \ll R_o$. **You need a cascode load too** to actually realize the cascode's gain. Cascode load output resistance $\approx g_{m3} r_{o3} r_{o4}$, so the fully-cascoded amp:

$$A_v \approx -g_{m1}\,(g_{m2}\,r_{o2}\,r_{o1}) \| (g_{m3}\,r_{o3}\,r_{o4}) \approx -\tfrac{1}{2}(g_m r_o)^2$$

if all four transistors match.

**Headroom cost:** the cascode adds another $V_{OV}$ to the minimum $V_{DS}$ requirement. Output swing is reduced by $V_{OV}$ on each end — important in low-voltage designs.

## Why it matters / when you use it
- **High-gain op-amps:** open-loop gain $\sim 80$ dB or more requires cascode (or multi-stage) topology.
- **Active-load differential amps:** cascode current-mirror loads boost CMRR and gain — see [[differential-pair]].
- **Bandwidth:** by reducing voltage swing at the CS drain (the CG's source is held nearly fixed), Miller multiplication of $C_{gd1}$ is suppressed. Cascodes have wider bandwidth than basic CS at the same gain.

## Common mistakes
- **Forgetting the load also limits gain.** A cascode amplifier with a non-cascode load has only $-g_m r_{o,\text{load}}$ gain. The cascoded output resistance is wasted. Always cascode both CS and load.
- **Body effect at the upper transistor.** The CG transistor has $V_{SB} > 0$; include $g_{mb}$ in $R_o$ unless you have triple-well isolation.
- **Headroom budget.** Each cascode level eats $V_{OV}$. In a 1.0 V supply, you can barely afford one cascode. Modern designs use folded cascodes or low-voltage cascodes.
- **Confusing "cascode" with "cascade."** Cascode = stacked CS+CG **inside one stage**; cascade = two amplifier stages connected in series.

## Related
- [[common-source-amplifier]] — bottom transistor
- [[common-gate-amplifier]] — top transistor (current buffer)
- [[current-mirror]] — cascode mirrors use the same idea
- [[mosfet-small-signal-model]] — formulas for $g_m, r_o$
