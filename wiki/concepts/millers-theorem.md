---
title: Miller's Theorem
type: concept
course:
  - "[[eee-335]]"
tags: [miller, frequency-response, capacitance, sedra-smith]
sources: [raw/slides/eee-335/unit-5-lecture-26-miller-s-theorem.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Miller's Theorem

## In one line
A bridging impedance $Z$ from input to output of an inverting amplifier with gain $K = v_o / v_i$ is equivalent to two grounded impedances: $Z_1 = Z / (1 - K)$ at the input and $Z_2 = Z \cdot K / (K - 1)$ at the output — for capacitors, this means $C_{gd}$ at the input acts like $(1 + |K|) C_{gd}$, the **Miller multiplication**.

## Example first
CS amplifier with gain $K = -50$ V/V, $C_{gd} = 10$ fF. Find the input-referred Miller capacitance.

$$C_1 = C_{gd}(1 - K) = 10\text{ fF}\,(1 - (-50)) = 10 \cdot 51 = \boxed{510\text{ fF}}$$

A 10 fF feedback cap looks like 510 fF at the input. **That's why CS amplifiers have low bandwidth** — the input pole sees an effectively-huge capacitance. The output side gets:

$$C_2 = C_{gd}(1 - 1/K) = 10\,(1 - 1/(-50)) \approx 10.2\text{ fF}$$

— only slightly more than $C_{gd}$ itself.

## The idea
A signal from the input flows through $Z$ to the output. Because the output swings $K$ times bigger (and inverted) than the input, the **voltage** across $Z$ is $v_i - K v_i = v_i(1 - K)$. So the current through $Z$ is $i = v_i(1 - K) / Z$, which from the input's perspective looks like an admittance to ground of $(1 - K) / Z$.

Substituting an equivalent **shunt** impedance: $Z_1 = Z / (1 - K)$. For an inverting amplifier ($K < 0$), $1 - K = 1 + |K|$, which is large and positive — so the input sees a **smaller** impedance, equivalent to a **larger** capacitance. That's the Miller effect.

## Formal definition

**Miller's Theorem (general $Z$, gain $K = v_o/v_i$):**

$$Z_1 = \frac{Z}{1 - K} \quad \text{(input to ground)}$$

$$Z_2 = \frac{Z}{1 - 1/K} \quad \text{(output to ground)}$$

**Capacitor specialization** ($Z = 1/sC$, so admittance $Y = sC$):

$$\boxed{\,C_1 = C(1 - K), \qquad C_2 = C(1 - 1/K)\,}$$

For inverting amplifier $K = -|K|$:
$$C_1 = C(1 + |K|), \qquad C_2 \approx C \;\text{ (when }|K| \gg 1\text{)}$$

So **the input sees the bridging cap multiplied by $(1 + |K|)$**, and the output sees roughly the original.

**Why it's an approximation:** the theorem assumes $K$ is constant over frequency. In reality, $K(s)$ rolls off, so the effective Miller multiplication at the dominant pole is closer to the **midband** gain — that's still useful for hand analysis.

## Why it matters / when you use it
- **CS amplifier bandwidth:** $C_{gd}$ is small, but at the input it looks like $(1 + g_m R_L)C_{gd}$ — often the dominant pole. See [[cs-amplifier-frequency-response]].
- **Cascode bandwidth advantage:** the CG transistor on top of a CS keeps the CS drain (and hence $K_{CS}$) small — so Miller multiplication is suppressed. Cascode is faster than basic CS at the same gain.
- **Common-gate / source-follower:** these have **non-inverting**, near-unity gain, so Miller multiplication is small. That's why they're good high-frequency stages.

## Common mistakes
- **Sign of $K$.** Use $K = v_o/v_i$ with sign. For a CS, $K = -g_m R_L'$ (negative). Plug **minus** $|K|$ into $1 - K$ to get $1 + |K|$.
- **Applying it to non-bridging elements.** Miller's theorem is for **feedback** elements (input ↔ output). Don't apply to a $C_{gs}$ that's only at the input.
- **Forgetting it's a midband approximation.** At very high frequencies the loop gain rolls off and the approximation fails — that's why exact analysis or [[octc-method]] is sometimes needed.

## Related
- [[mosfet-high-frequency-model]] — where $C_{gd}$ enters
- [[cs-amplifier-frequency-response]] — Miller-dominated bandwidth
- [[cascode-amplifier]] — Miller-suppressed bandwidth
- [[octc-method]] — alternative bandwidth method
