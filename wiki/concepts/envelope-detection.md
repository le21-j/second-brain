---
title: Envelope Detection (Non-Coherent Demodulation)
type: concept
course: [[eee-304]]
tags: [eee-304, communication, demodulation, am, envelope, non-coherent, bandpass]
sources: [[lab-eee-304-lab-4-am-modulation]]
created: 2026-04-25
updated: 2026-04-26
---

# Envelope Detection (Non-Coherent Demodulation)

## In one line
Take the **absolute value** of the received AM signal and **bandpass-filter** the result — what comes out is the envelope $A + m(t)$, which is the message (up to a DC offset) — **provided** the modulation index satisfies $\mu \leq 1$.

## Example first

Received AM signal: $r(t) = (A + m(t))\cos(\omega_c t)$. With $A = 2$, $m(t) = \sin(2\pi \cdot 2000 \cdot t)$, so $\mu = 0.5$ (safely under-modulated).

**Step 1 — $|r(t)|$:**

$$|r(t)| = |A + m(t)| \cdot |\cos(\omega_c t)| = (A + m(t)) \cdot |\cos(\omega_c t)| \qquad\text{(since } A + m(t) \geq 0 \text{ when } \mu \leq 1\text{)}.$$

$|\cos(\omega_c t)|$ is a fully-rectified cosine — it has DC content plus harmonics at $2\omega_c, 4\omega_c, \ldots$ Multiplied by the envelope $A + m(t)$, the result has:

- A **slow part** that looks like the envelope $A + m(t)$ — *this is the message we want*.
- **Fast spikes** at $2\omega_c, 4\omega_c, \ldots$ from the rectified carrier.
- A **DC offset** from the constant $A$ that was added at the transmitter.

**Step 2 — bandpass filter** to keep only the message band:

| Filter edge | Purpose | Lab value |
|---|---|---|
| $W_{\text{lo}}$ (high-pass cutoff) | remove the **DC offset** from $A$ | $30 \cdot 2\pi$ rad/s ($30$ Hz) |
| $W_{\text{hi}}$ (low-pass cutoff) | remove the $2\omega_c$ and higher carrier harmonics | $5000 \cdot 2\pi$ rad/s ($5$ kHz) |

Net output: $m(t)$, recovered (with whatever scale factor the rectification introduced).

> [!tip] **Why bandpass, not just low-pass?** Because we deliberately added $A$ to push the envelope above zero at the transmitter — and that $A$ shows up as **DC** at the receiver. A pure LPF would let it through; a bandpass with a small $W_{\text{lo}}$ blocks it.

## The idea

Envelope detection is the **dirt-cheap receiver**: just a diode (the $|\cdot|$) and a capacitor + resistor network (the bandpass). No local oscillator, no PLL, no phase recovery — *that's why AM broadcast radio works on a \$5 transistor radio*.

The cost: it needs the envelope to be **non-negative everywhere**, i.e., $A + m(t) \geq 0$, i.e., $m_{\text{peak}} \leq A$, i.e., $\mu \leq 1$. Once $\mu > 1$, the envelope dips below zero, the $|\cdot|$ flips it back, and the recovered signal becomes a half-rectified, harmonic-distorted version of the original.

## Formal definition

Given $r(t) = (A + m(t))\cos(\omega_c t)$:

$$y(t) = |r(t)| \;\xrightarrow{\;\text{bandpass}\;[W_{\text{lo}},\,W_{\text{hi}}]\;}\; \approx m(t).$$

Conditions for clean recovery:

1. **Modulation index** $\mu \leq 1$ (envelope non-negative).
2. $W_{\text{lo}} > 0$ but small enough not to attenuate the message's lowest frequency component ($\ll$ message bandwidth).
3. $W_{\text{hi}} >$ message bandwidth $B$ but $\ll 2\omega_c$.
4. **Carrier frequency** $\omega_c \gg B$ (so the rectification spikes are well separated from the message in frequency).

==**Master condition:** $\mu \leq 1$. Violate it and no filter can save you — the information is destroyed by the rectification step.==

## Why it matters / when you use it

- **AM broadcast radio receivers.** A diode + RC network = an envelope detector. Hundreds of millions of these were sold from the 1920s onward.
- **Cheap IoT receivers.** Wake-up radios, RFID, simple ASK demodulators all use envelope detection.
- **Visualizing modulation depth.** Plot the envelope against the message — instantly tells you $\mu$ and whether you're over-modulating.

## Common mistakes
- **Using a pure low-pass filter.** Misses the DC-offset problem; you'll see a constant $A/\pi$ (or similar) on top of $m(t)$.
- **Setting $W_{\text{lo}} = 0$.** Same problem — DC leaks through. The lab specifically asks "what happens when $W_{\text{lo}} = 1 \cdot 2\pi$?" because lowering $W_{\text{lo}}$ to nearly $0$ reveals exactly this DC bleed-through. ==**Lab observation: at $W_{\text{lo}} = 1 \cdot 2\pi$, you'll see a strong DC line in the spectrum that wasn't there at $W_{\text{lo}} = 30 \cdot 2\pi$.**==
- **Not adding $A$ at the transmitter.** Envelope detection needs the envelope to be non-negative; that's the *whole reason* AM is $(A + m(t))\cos(\omega_c t)$ and not just $m(t)\cos(\omega_c t)$ (which is DSB-SC and requires coherent demod).
- **Trying envelope detection with $\mu > 1$.** Over-modulated signals **cannot** be cleanly recovered by envelope detection — see [[modulation-index]]. The lab #2 question 5 explicitly tests this failure mode.
- **Confusing $W_{\text{lo}}$ with $n$.** $W_{\text{lo}}$/$W_{\text{hi}}$ are the band edges (rad/s); $n$ is the filter order ($10$ in the lab's bandpass).

## Related
- [[amplitude-modulation]] — the modulation that envelope detection inverts
- [[modulation-index]] — the master condition $\mu \leq 1$ for envelope detection to work
- [[coherent-demodulation]] — the alternative that handles $\mu > 1$ at the cost of carrier recovery
- [[butterworth-filter]] — the bandpass topology used in the lab

## Sources / further reading
- Lab manual: `raw/labs/EEE 304 Lab4.pdf` (section 2 + assignment #2)
- Wikipedia: https://en.wikipedia.org/wiki/Envelope_detector
