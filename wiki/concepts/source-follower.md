---
title: Source Follower (Common Drain)
type: concept
course:
  - "[[eee-335]]"
tags: [amplifier, cd, source-follower, voltage-buffer, sedra-smith]
sources: [raw/slides/eee-335/unit-4-lecture-19-basic-configurations.pdf, raw/slides/eee-335/unit-4-lecture-22-buffers-common-gate-and-source-follower.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Source Follower (Common Drain)

## In one line
The source follower — input at gate, output at source, drain held at $V_{DD}$ (AC ground) — has $R_{\text{in}} = \infty$, gain very close to $+1$, and output resistance $\approx 1/g_m$, making it the canonical **voltage buffer**.

## Example first
Source follower with $g_m = 1$ mS driving load $R_L = 1$ k$\Omega$. Find $A_v$.

$$A_v = \frac{R_L}{R_L + 1/g_m} = \frac{1\text{k}}{1\text{k} + 1\text{k}} = \boxed{0.5\text{ V/V}}$$

With $R_L = \infty$ (open-circuit): $A_{v0} = 1$. With $R_L = 10$ k$\Omega$: $A_v = 10/(10+1) = 0.91$. So the buffer is "good" (gain near 1) when $R_L \gg 1/g_m$.

## The idea
- **Input at gate:** $R_{\text{in}} = \infty$ (no input current).
- **Output at source:** as $v_{\text{in}}$ rises, the source rises with it (because $V_{GS}$ self-adjusts to keep $I_D$ roughly constant). So $v_o$ "follows" $v_i$ — non-inverting, gain $\approx 1$.
- **Output resistance is $1/g_m$:** small. That's exactly what a voltage buffer needs to drive a low-impedance load without losing much voltage.

The source follower is the dual of the [[common-gate-amplifier]]: same $1/g_m$ impedance, but at the **output** (low) instead of the input (low).

## Formal definition

**Without $r_o$** (open-circuit):

| Quantity | Value |
|---|---|
| $R_{\text{in}}$ | $\infty$ |
| $R_o$ | $1/g_m$ |
| $A_{v0}$ | $+1$ V/V (open circuit, $R_L = \infty$) |

**With finite load $R_L$:**
$$A_v = \frac{R_L}{R_L + 1/g_m} = \frac{g_m R_L}{1 + g_m R_L}$$

**With $r_o$:** add $r_o$ in parallel with $R_L$ at the source:
$$A_v = \frac{g_m (r_o \| R_L)}{1 + g_m (r_o \| R_L)}$$

**Body effect:** since the source is the output node, $V_{SB} \neq 0$ in general → $g_{mb}$ shows up. The effective transconductance becomes $g_m + g_{mb}$, slightly improving gain but never above 1.

## Why it matters / when you use it
- **Output stage** of an op-amp or any voltage amplifier — converts a high-impedance voltage signal to a low-impedance one capable of driving a load (resistor, line, ADC).
- **Level shifter** — the DC offset is $V_{GS} \approx V_t + V_{OV}$ between gate and source. Useful for biasing the next stage.
- **Cascading amplifiers** without loading: put a SF between two CS stages and the second CS sees an effectively-zero source impedance.

## Common mistakes
- **Expecting $A_v$ exactly 1.** Open-circuit gives $A_{v0} = 1$, but with any finite load you lose some — the divider $R_L / (R_L + 1/g_m)$ is always $< 1$.
- **Forgetting the body effect.** It can subtract $\sim 10\%$ from the gain in standard CMOS where the bulk is tied to ground.
- **Sign.** SF is non-inverting (same as CG, opposite of CS). $A_v = +g_m R_L / (1 + g_m R_L)$.
- **Confusing with emitter follower.** Same idea but for BJT: gain → 1 as $\beta \to \infty$ rather than as $g_m R_L \to \infty$.

## Related
- [[mosfet-small-signal-model]]
- [[common-source-amplifier]] — voltage **gain** stage (vs SF voltage **buffer**)
- [[common-gate-amplifier]] — current buffer (the dual)
