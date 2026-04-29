---
title: 6T SRAM Cell
type: concept
course: [[eee-335]]
tags: [memory, sram, latch, sizing, sedra-smith]
sources: [raw/slides/eee-335/unit-3-lecture-16-the-sram-cell.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# 6T SRAM Cell

## In one line
A 6T SRAM cell is a back-to-back inverter latch (4 transistors) with two NMOS access transistors gated by the word line — the access/latch transistor sizing must satisfy a specific ratio so that **read** can't disturb the stored bit and **write** is always able to flip it.

## Example first
6T cell with $V_{DD} = 1.8$ V, $V_{t0} = 0.5$ V. Required: during read, internal node $v_Q$ must stay below $V_{t0}$ so the opposite-side NMOS doesn't turn on and corrupt the bit.

Apply the read-sizing rule:
$$\frac{(W/L)_a}{(W/L)_n} \;=\; \frac{1}{1 - \tfrac{1}{V_{DD} - V_{t0}}\sqrt{V_{t0}^2 - 2V_{t0} \cdot 0}} - 1 \;=\; \frac{V_{t0}^2}{2 V_{t0}(V_{DD} - V_{t0}) - V_{t0}^2}$$

Plugging in:
$$\frac{(W/L)_a}{(W/L)_n} \approx \frac{0.25}{2(0.5)(1.3) - 0.25} = \frac{0.25}{1.05} \approx 0.24$$

So the **access transistor should be ~4× narrower than the latch NMOS** for a safe read.

## The idea
- **Latch:** four transistors $Q_1$–$Q_4$ form two cross-coupled CMOS inverters. Together they have two stable states — call them "1" ($Q = V_{DD}, \overline{Q} = 0$) and "0".
- **Access transistors:** $Q_5, Q_6$ are NMOS pass transistors gated by the **word line** (W). When W is high, the cell connects to the bit lines $B$ and $\overline{B}$.
- **Read:** pre-charge $B$ and $\overline{B}$ to $V_{DD}$, raise W. The "0" side of the cell pulls **its** bit line down through the access NMOS; a sense amp detects which side dropped first.
- **Write:** drive $B$ and $\overline{B}$ to the desired values, raise W. The drivers force the internal nodes to flip.

The constraint: during **read**, the bit-line voltage drop must not raise the internal "0" node above $V_{tn}$ (which would partially turn on the opposite NMOS and corrupt the stored bit).

## Formal definition

Standard 6T cell:
- $Q_1, Q_3$ — latch NMOS (size $W_n$)
- $Q_2, Q_4$ — latch PMOS (size $W_p$)
- $Q_5, Q_6$ — access NMOS (size $W_a$)
- All at $L = L_{\min}$.

**Read-sizing rule** (so that stored bit is preserved):

$$\frac{(W/L)_a}{(W/L)_n} \;\leq\; \frac{1}{\dfrac{1}{1 - \tfrac{V_{t0}}{V_{DD} - V_{t0}}^2} - 1}$$

Practical interpretation: $W_a < W_n$ — access transistor narrower than latch NMOS, by roughly a factor of 2–4.

**Write-sizing rule** (so that the cell can be flipped):

$$\frac{(W/L)_p}{(W/L)_a} \;\leq\; \frac{k_n'}{k_p'}\!\cdot\!\dfrac{1}{\dfrac{1}{1 - \tfrac{V_{t0}}{V_{DD} - V_{t0}}^2} - 1}$$

Practical interpretation: $W_p < W_a \cdot \mu_p / \mu_n$ — latch PMOS narrower than access NMOS divided by mobility ratio.

**Read time:**
$$t_{\text{read}} = \frac{C_B \cdot \Delta V_o}{I_5}$$

where $C_B$ is the bit-line capacitance, $\Delta V_o$ is the sense-amp threshold (a few hundred mV), and $I_5$ is the access transistor current.

## Why it matters / when you use it
- SRAM is the **fastest** on-chip memory and dominates cache (L1/L2/L3) area in modern CPUs/GPUs.
- The 6T sizing tradeoff is one of the most studied analog problems in VLSI: shrink area → narrower transistors → less margin → more bit failures. Modern caches use 8T or 10T cells at advanced nodes for this reason.
- The sizing rules generalize: any **ratioed** circuit (where two transistors fight to determine an output level) needs the same kind of analysis.

## Common mistakes
- **Forgetting the body effect** in the access transistor analysis. Sedra/Smith neglects it for tractability — but it's a real second-order correction.
- **Mixing read and write rules.** Read rule constrains $W_a$ vs $W_n$; write rule constrains $W_p$ vs $W_a$. They're separate inequalities that both must hold.
- **Pre-charge confusion.** Both bit lines pre-charge to $V_{DD}$, then **only one** drops during read. The differential $\Delta V$ is the sense-amp signal.

## Related
- [[pass-transistor-logic]] — access transistors are NMOS pass devices
- [[cmos-inverter-vtc]] — the latch is two cross-coupled CMOS inverters
- [[mosfet-iv-characteristics]] — saturation (access) vs triode (latch) during read
