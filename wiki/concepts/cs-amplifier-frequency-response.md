---
title: CS Amplifier Frequency Response
type: concept
course:
  - "[[eee-335]]"
tags: [cs-amplifier, frequency-response, miller, bandwidth, sedra-smith]
sources: [raw/slides/eee-335/unit-5-lecture-25-high-frequency-response-of-cs-amplifier.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# CS Amplifier Frequency Response

## In one line
A CS amplifier with source impedance $R_{\text{sig}}$ and load $R_L'$ has midband gain $A_M = -g_m R_L'$ and upper-3 dB frequency $f_H \approx 1 / [2\pi R_{\text{sig}}' (C_{gs} + C_{gd}(1 + g_m R_L'))]$ — Miller multiplication of $C_{gd}$ usually dominates and limits bandwidth.

## Example first
CS amplifier: $g_m = 1$ mS, $R_L' = r_o \| R_D \| R_L = 10$ k$\Omega$, $R_{\text{sig}}' = 50$ k$\Omega$, $C_{gs} = 100$ fF, $C_{gd} = 20$ fF.

**Midband gain:**
$$A_M = -g_m R_L' = -(1\text{ mS})(10\text{ k}\Omega) = -10\text{ V/V}$$

**Miller-multiplied input cap:**
$$C_{\text{in}} = C_{gs} + C_{gd}(1 + g_m R_L') = 100 + 20(1 + 10) = 100 + 220 = 320\text{ fF}$$

**Upper-3 dB:**
$$f_H = \frac{1}{2\pi R_{\text{sig}}' C_{\text{in}}} = \frac{1}{2\pi(50\text{k})(320\text{f})} = \boxed{9.95\text{ MHz}}$$

Without Miller multiplication you'd have $C_{\text{in}} = 120$ fF and $f_H = 26$ MHz — a 2.6× hit from the Miller effect.

## The idea
Three time constants compete to set the bandwidth:
1. **Input pole** at the gate, due to $R_{\text{sig}}'$ and $C_{gs} + (1+|A|)C_{gd}$.
2. **Output pole** at the drain, due to $R_L'$ and $C_{gd}$ (small Miller share) + $C_L$ + $C_{db}$.
3. **Direct-feedforward zero** at $\omega_z = +g_m / C_{gd}$ — usually well above $f_H$, ignored.

Miller multiplication of $C_{gd}$ at the input is the dominant effect when gain is high. For low-gain stages (or cascodes that suppress the inverting gain on $C_{gd}$), the input pole becomes negligible and the output pole takes over.

## Formal definition

**Two equivalent methods:**

**(1) Single-pole Miller approximation:**
$$A_M = -g_m R_L' \cdot \frac{R_G}{R_G + R_{\text{sig}}}$$
$$f_H \approx \frac{1}{2\pi R_{\text{sig}}' C_{\text{in}}}, \qquad C_{\text{in}} = C_{gs} + C_{gd}(1 + g_m R_L')$$

(where $R_{\text{sig}}' = R_{\text{sig}} \| R_G$).

**(2) Open-Circuit Time Constants (OCTC, more accurate):**

$$\tau_{gs} = C_{gs} R_{\text{sig}}'$$
$$\tau_{gd} = C_{gd}\left[R_L' + R_{\text{sig}}'(1 + g_m R_L')\right]$$
$$\tau_{C_L} = C_L R_L'$$

$$f_H \approx \frac{1}{2\pi(\tau_{gs} + \tau_{gd} + \tau_{C_L})}$$

OCTC includes the output-side contribution of $C_{gd}$ and is more accurate when the output time constant is comparable to the input one.

**Right-half-plane zero** (often dropped):
$$\omega_z = +\frac{g_m}{C_{gd}}$$

This is the frequency where the direct feedforward through $C_{gd}$ cancels the gain — at very high frequencies (well above $f_T$), so usually ignored.

**Bandwidth–gain trade:** since $A_M \propto R_L'$ and Miller multiplier $\propto |A_M|$, the gain × bandwidth product is roughly fixed for a given transistor + topology — the canonical $f_T$-limited tradeoff.

## Why it matters / when you use it
- **Why cascodes are wider-bandwidth.** Cascode keeps the CS drain swing tiny (load is $1/g_m$ at the CG source), so Miller multiplication is suppressed. Same gain, ~10× wider bandwidth.
- **Why source impedance matters.** A high $R_{\text{sig}}$ kills bandwidth quadratically (it's both the source for the input pole AND the multiplier for the Miller-multiplied cap). Always buffer with a source-follower if needed.
- **Predicting the bandwidth bottleneck.** If $\tau_{gd} \gg \tau_{gs}$, fix Miller (cascode, lower gain). If $\tau_{C_L}$ dominates, fix the output node (smaller $R_L'$ or $C_L$).

## Common mistakes
- **Forgetting the $1 + g_m R_L'$ multiplier.** Sometimes people write $C_{gd}$ alone at the input — that's the **non-inverting** approximation and is wrong for a CS.
- **Mixing methods.** Miller approximation gives a single-pole estimate; OCTC gives a sum-of-time-constants estimate. They agree to first order but OCTC is generally tighter.
- **Ignoring the right-half-plane zero in feedback amps.** In open-loop CS this zero is harmless. In feedback amplifiers it can cause instability — relevant in op-amp design (EEE 425).

## Related
- [[millers-theorem]] — input-cap multiplication
- [[octc-method]] — alternative bandwidth method
- [[mosfet-high-frequency-model]] — where the caps come from
- [[common-source-amplifier]] — DC version
- [[cascode-amplifier]] — Miller-suppressed alternative
