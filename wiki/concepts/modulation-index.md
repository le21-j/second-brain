---
title: Modulation Index ($\mu$)
type: concept
course: [[eee-304]]
tags: [eee-304, communication, modulation, am, modulation-index, over-modulation]
sources: [[lab-eee-304-lab-4-am-modulation]]
created: 2026-04-25
updated: 2026-04-26
---

# Modulation Index ($\mu$)

## In one line
The modulation index $\mu = m_{\text{peak}}/A$ is the ratio of message peak amplitude to carrier amplitude — it tells you how deeply the carrier is being modulated, and **whether the cheap envelope detector at the receiver will work or fail**.

## Example first

Take the lab setup: carrier amplitude $A = 2$, message $m(t) = m_{\text{peak}}\sin(2\pi \cdot 2000 \cdot t)$.

| $m_{\text{peak}}$ | $\mu = m_{\text{peak}}/A$ | Regime | Envelope detector? |
|---|---|---|---|
| $0.5$ | $0.25$ | under-modulated | ✅ works fine |
| $1.0$ | $0.50$ | under-modulated | ✅ works fine |
| $2.0$ | $1.00$ | perfect | ✅ on the boundary |
| $4.0$ | $2.00$ | **over-modulated** | ❌ envelope distortion |

The AM signal envelope is $A + m(t)$. As long as $A + m(t) \geq 0$ for all $t$, the envelope is non-negative and the receiver's $|\cdot|$ (envelope detector) sees the message intact. That non-negativity condition is exactly $\mu \leq 1$.

## The idea

Geometrically, $\mu$ is "how big is the message swing relative to the carrier amplitude?"

- $\mu < 1$ → the envelope $A + m(t)$ stays strictly positive. The envelope detector (just $|\cdot|$ followed by an LPF) recovers $m(t) + A$ cleanly.
- $\mu = 1$ → the envelope just barely touches zero at the message's troughs. Still works, but the detector has zero margin.
- $\mu > 1$ → the envelope **goes negative** during deep troughs, and $|\cdot|$ flips the sign. The recovered signal is no longer $m(t)$ — it's a phase-distorted, half-rectified mess. This is **over-modulation**.

> [!warning] **Over-modulation distorts irreversibly.** The envelope detector cannot recover $m(t)$ once $\mu > 1$, no matter how perfect the LPF afterward.

## Formal definition

For a sinusoidal message $m(t) = m_{\text{peak}}\cos(\omega_m t)$ and carrier amplitude $A$:

$$\mu = \frac{m_{\text{peak}}}{A}.$$

Three regimes:

| Range | Name | Coherent demod | Envelope detection |
|---|---|---|---|
| $\mu < 1$ | under-modulation | ✅ | ✅ |
| $\mu = 1$ | 100% modulation | ✅ | ✅ (boundary) |
| $\mu > 1$ | over-modulation | ✅ | ❌ |

==**The asymmetry is the key fact:** [[coherent-demodulation]] doesn't care about $\mu$, but [[envelope-detection]] only works for $\mu \leq 1$.==

## Why it matters / when you use it

- **Picking transmit power vs message amplitude.** AM broadcast stations ride at $\sim 80$–$90\%$ modulation — close to $\mu = 1$ for max audio loudness, but with safety margin to never clip.
- **Diagnosing a broken receiver.** If your demodulated output is half-rectified or distorted-only-on-loud-passages, suspect over-modulation, not the filter.
- **Choosing modulation scheme.** If the receiver must be cheap (a basic envelope detector, no carrier recovery), you must ensure $\mu \leq 1$ at the transmitter.

## Common mistakes
- **Confusing $\mu$ with carrier-to-message ratio.** $\mu$ is $m_{\text{peak}}/A$, not $A/m_{\text{peak}}$. Larger $\mu$ = deeper modulation.
- **Computing $\mu$ from the modulated signal.** Use the envelope's max and min:

  $$\mu = \frac{\text{env}_{\max} - \text{env}_{\min}}{\text{env}_{\max} + \text{env}_{\min}}.$$

  Or just use $m_{\text{peak}}/A$ directly if you set both at the source.
- **Assuming over-modulation always sounds bad.** It can sound *louder* and not obviously distorted on simple sources, but on complex audio (like `tada.wav`) the harmonic distortion is audible.
- **Trying to fix over-modulation with a better filter.** It's not a filter problem — the information was destroyed at the transmitter.

## Related
- [[amplitude-modulation]] — the modulation that this index parameterizes
- [[envelope-detection]] — the receiver where $\mu$ matters
- [[coherent-demodulation]] — the receiver where $\mu$ does **not** matter

## Sources / further reading
- Lab manual: `raw/labs/EEE 304 Lab4.pdf` (section 3)
- Wikipedia: https://en.wikipedia.org/wiki/Amplitude_modulation#Modulation_index
