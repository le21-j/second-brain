---
title: Open-Circuit Time Constants (OCTC) Method
type: concept
course: [[eee-335]]
tags: [octc, bandwidth, frequency-response, sedra-smith]
sources: [raw/slides/eee-335/unit-5-lecture-29-method-of-open-circuit-time-constants.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Open-Circuit Time Constants (OCTC) Method

## In one line
Estimate the upper-3 dB frequency $\omega_H$ of an amplifier with $m$ capacitors as $\omega_H \approx 1 / \sum_k C_k R_k$, where $R_k$ is the resistance "seen" by capacitor $C_k$ with all **other** capacitors open-circuited and all independent sources zeroed.

## Example first
CS amplifier with three caps: $C_{gs} = 100$ fF, $C_{gd} = 20$ fF, $C_L = 50$ fF. Resistances seen by each:
- $R_{gs} = R_{\text{sig}}' = 50$ k$\Omega$ (Thevenin resistance at gate node)
- $R_{gd} = R_L' + g_m R_L' R_{\text{sig}}' + R_{\text{sig}}'$, with $R_L' = 10$ k$\Omega$, $g_m = 1$ mS:
  $$R_{gd} = 10\text{k} + (1\text{mS})(10\text{k})(50\text{k}) + 50\text{k} = 10\text{k} + 500\text{k} + 50\text{k} = 560\text{ k}\Omega$$
- $R_{C_L} = R_L' = 10$ k$\Omega$

Sum the time constants:
$$\tau_{\text{total}} = C_{gs} R_{gs} + C_{gd} R_{gd} + C_L R_{C_L}$$
$$= 100\text{f} \cdot 50\text{k} + 20\text{f} \cdot 560\text{k} + 50\text{f} \cdot 10\text{k}$$
$$= 5\text{ ns} + 11.2\text{ ns} + 0.5\text{ ns} = 16.7\text{ ns}$$

$$\omega_H \approx \frac{1}{\tau_{\text{total}}} = \frac{1}{16.7\text{ ns}} = 60\text{ Mrad/s} \implies f_H \approx 9.5\text{ MHz}$$

The dominant contributor is $C_{gd}$ (Miller-multiplied $R_{gd}$ is huge) — exactly the warning Miller's theorem predicts.

## The idea
For a transfer function with $m$ poles:
$$H(s) = \frac{1}{(1 + s/p_1)(1 + s/p_2)\cdots(1 + s/p_m)}$$

If you expand and keep only the linear-in-$s$ term in the denominator, the effective "first-order pole" is at $\omega_H$ where:

$$\frac{1}{\omega_H} = b_1 = \sum_k \frac{1}{p_k}$$

The OCTC method gives $b_1$ directly via $b_1 = \sum_k C_k R_k$ — no need to find the individual poles. This is exact for the dominant-pole approximation when one pole is much smaller than the others, and a useful upper-bound estimate even when poles are comparable.

## Formal definition

**Step 1.** Identify all $m$ capacitors $C_k$ in the small-signal circuit.

**Step 2.** For each $C_k$:
- Open-circuit all **other** capacitors.
- Zero all independent sources (short voltages, open currents).
- Apply a test source to $C_k$'s terminals.
- Compute the Thevenin resistance $R_k$ seen by $C_k$.

**Step 3.** Sum:
$$\tau_{\text{total}} = \sum_{k=1}^{m} C_k R_k$$

**Step 4.** Estimate:
$$\omega_H \approx \frac{1}{\tau_{\text{total}}}, \qquad f_H \approx \frac{1}{2\pi\tau_{\text{total}}}$$

**Resistances for the CS amplifier:**

| Cap | Seen resistance |
|---|---|
| $C_{gs}$ | $R_{gs} = R_{\text{sig}}'$ |
| $C_{gd}$ | $R_{gd} = R_L' + R_{\text{sig}}'(1 + g_m R_L')$ |
| $C_L$ (load cap at drain) | $R_{C_L} = R_L'$ |

The $R_{gd}$ formula contains the **Miller multiplier** $1 + g_m R_L'$ — OCTC and Miller's theorem give the same Miller-dominated estimate.

## Why it matters / when you use it
- **Multi-cap circuits** where pole-zero analysis is tedious. Cascode, differential pair, multi-stage amps — OCTC handles all uniformly.
- **Design intuition:** the $C_k R_k$ contribution shows you which cap is the bandwidth bottleneck. Engineering iteration: shrink the cap or reduce its seen-resistance.
- **Faster than full transfer-function expansion** by an order of magnitude.

## Common mistakes
- **Not zeroing sources.** Independent voltage source short, current source open. The $g_m$-controlled current source stays!
- **Forgetting Miller-like resistance for bridging caps.** $R_{gd}$ is **not** just $R_L'$ — it includes the dependent-source contribution that gives $1 + g_m R_L'$ multiplication.
- **OCTC is an estimate**, not exact. When poles are widely separated (a "dominant pole" exists), it's accurate to a few percent. When poles are close, it's still a useful upper bound on $\omega_H$ (so $f_H$ is the **lower bound** estimate).
- **Mixing "open" and "short" rules.** OCTC: open the other caps. There's also "Short-Circuit Time Constants" (SCTC) for **low-frequency** $\omega_L$, where you short all big coupling caps except the one you're computing for.

## Related
- [[millers-theorem]] — alternative bandwidth method via input-referred cap
- [[cs-amplifier-frequency-response]] — application to common-source
- [[mosfet-high-frequency-model]] — where the caps come from
