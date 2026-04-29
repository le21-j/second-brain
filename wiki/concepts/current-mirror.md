---
title: Current Mirror
type: concept
course: [[eee-335]]
tags: [current-mirror, biasing, ic-design, sedra-smith]
sources: [raw/slides/eee-335/unit-4-lecture-20-ic-biasing.pdf]
created: 2026-04-28
updated: 2026-04-28
---

# Current Mirror

## In one line
A diode-connected reference transistor sets a $V_{GS}$, and an output transistor with the same $V_{GS}$ replicates the reference current scaled by $W/L$ ratio: $I_O = I_{\text{REF}} \cdot (W/L)_2 / (W/L)_1$.

## Example first
Reference current $I_{\text{REF}} = 50\ \mu$A through $Q_1$ with $(W/L)_1 = 2$. Output transistor $Q_2$ with $(W/L)_2 = 8$. Find $I_O$.

$$I_O = I_{\text{REF}} \cdot \frac{(W/L)_2}{(W/L)_1} = 50\ \mu\text{A} \cdot \frac{8}{2} = \boxed{200\ \mu\text{A}}$$

So the mirror **multiplies** the reference current by 4. By choosing $(W/L)$ ratios, you can fan out a single off-chip $I_{\text{REF}}$ to dozens of bias points across the chip — that's the whole reason mirrors exist.

## The idea
- **Diode-connected** $Q_1$ has $V_{GS} = V_{DS}$, forcing it into saturation. The reference current $I_{\text{REF}}$ sets $V_{GS,1}$ via the saturation equation.
- **Output** $Q_2$ shares the same gate node and source node, so $V_{GS,2} = V_{GS,1}$. As long as $Q_2$ is also in saturation (i.e., $V_{DS,2} \geq V_{OV,2}$), it draws the same current up to a $(W/L)_2/(W/L)_1$ scaling.
- **The compliance limit:** $Q_2$ leaves saturation when $V_{O} < V_{OV}$ — call this the minimum output voltage $V_{O,\min} = V_{OV}$.

## Formal definition

**Basic mirror, two transistors:**
$$I_O = I_{\text{REF}} \cdot \frac{(W/L)_2}{(W/L)_1} \cdot \left[1 + \lambda(V_O - V_{GS})\right]$$

The bracketed term is channel-length modulation — it makes $I_O$ slowly rise with $V_O$, which is **bad** because we want a clean current source.

**Output resistance:**
$$R_O = r_{o2} = \frac{V_A}{I_O}$$

This is the small-signal "stiffness" of the current source — large is good.

**Compliance (minimum $V_O$ in saturation):**
$$V_{O,\min} = V_{OV,2}$$

**Cascode current mirror** (4 transistors): a CG on top of $Q_2$ multiplies $R_O$ by $g_{m,\text{cas}} r_{o,\text{cas}}$:
$$R_O^{\text{cascode}} = g_{m3} r_{o3} r_{o2}$$

Penalty: compliance worsens by one $V_{OV}$ — minimum $V_O$ becomes $2V_{OV} + V_t$ (or in low-voltage cascodes, $2V_{OV}$).

**Current-source small-signal model** (when used as a load):
- Replaces a passive $R_D$ with $r_{o2}$ — much larger ($V_A/I_D$ vs $V_{DD}/I_D$).
- That's why the [[basic-gain-cell]] uses a current-source load: gain becomes $g_m r_o$ instead of $g_m R_D$.

## Why it matters / when you use it
- **Biasing:** every analog block on a chip is biased from a current mirror. One off-chip resistor (or bandgap reference) sets all the bias currents on a die.
- **Active load:** a PMOS current mirror at the drain of an NMOS amplifier replaces $R_D$ with $r_{o,\text{PMOS}}$ — see [[common-source-amplifier]] basic gain cell.
- **Differential pair active load:** converts differential current to a single-ended voltage with full $g_m r_o$ gain — see [[differential-pair]].

## Common mistakes
- **Forgetting saturation check on $Q_2$.** If $V_O < V_{OV}$, $Q_2$ enters triode and the mirror current collapses — this is a common bug in low-voltage designs.
- **Ignoring channel-length modulation.** For DC bias, the $(1 + \lambda V_O)$ term changes $I_O$ noticeably as $V_O$ swings. Use a cascode mirror if you need precision.
- **Mismatch.** Real $W/L$ ratios are quantized to layout dimensions; matching errors of $\sim 1\%$ are typical. Use unit-cell-based layouts (multi-finger devices) for matched mirrors.

## Related
- [[mosfet-small-signal-model]] — $r_o$ is the mirror's output resistance
- [[mosfet-iv-characteristics]] — saturation is required
- [[common-source-amplifier]] — uses a mirror as active load
- [[cascode-amplifier]] — also boosts mirror output resistance
- [[differential-pair]] — uses tail mirror for biasing
