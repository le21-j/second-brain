---
title: Coherent Demodulation
type: concept
course: [[eee-304]]
tags: [eee-304, communication, demodulation, am, coherent, lpf, fourier]
sources: [[lab-eee-304-lab-4-am-modulation]]
created: 2026-04-25
updated: 2026-04-26
---

# Coherent Demodulation

## In one line
Multiply the received AM signal by **the same carrier** $\cos(\omega_c t)$ again — this shifts the message back to baseband — then **low-pass filter** out the high-frequency junk that lands at $2\omega_c$.

## Example first

The received signal:

$$r(t) = \bigl(A + m(t)\bigr)\cos(\omega_c t) \qquad\text{(the AM transmission)}$$

**Step 1 — multiply by the carrier again:**

$$r(t)\cos(\omega_c t) = \bigl(A + m(t)\bigr)\cos^2(\omega_c t) = \bigl(A + m(t)\bigr) \cdot \tfrac{1}{2}\bigl[1 + \cos(2\omega_c t)\bigr]$$

$$= \underbrace{\tfrac{1}{2}\bigl(A + m(t)\bigr)}_{\text{what we want, at baseband}} + \underbrace{\tfrac{1}{2}\bigl(A + m(t)\bigr)\cos(2\omega_c t)}_{\text{garbage, at } 2\omega_c}.$$

**Step 2 — low-pass filter** with cutoff between $B$ (the message bandwidth) and $2\omega_c$. The $2\omega_c$ term is rejected, the DC $\tfrac{1}{2}A$ is a constant offset (often blocked by AC-coupling), and what comes out is $\tfrac{1}{2}m(t)$ — the message, scaled by $\tfrac{1}{2}$.

In the lab: message at $2$ kHz, carrier at $20$ kHz, so the demodulated-but-unfiltered signal has spectral content at $2$ kHz (the message) and $40$ kHz (the $2\omega_c$ image). Picking an LPF cutoff anywhere between $5$ kHz and $30$ kHz cleanly separates them.

## The idea

In the frequency domain, the receiver's multiplication by $\cos(\omega_c t)$ does the **same shift** that the transmitter did — every spectral copy moves both up and down by $\omega_c$. Apply that to the AM spectrum (which already has copies at $\pm\omega_c$) and you get:

| Source copy | After receiver shift | Result |
|---|---|---|
| copy at $+\omega_c$ shifted down by $\omega_c$ | $0$ | message back at baseband ✓ |
| copy at $+\omega_c$ shifted up by $\omega_c$ | $+2\omega_c$ | garbage to be filtered |
| copy at $-\omega_c$ shifted down by $\omega_c$ | $-2\omega_c$ | garbage |
| copy at $-\omega_c$ shifted up by $\omega_c$ | $0$ | message (overlapping with above) ✓ |

The two copies at $0$ add up to give the message back. The $\pm 2\omega_c$ copies are removed by the LPF.

> [!tip] **Why "coherent"?** Because the receiver's local oscillator must have **the same frequency AND the same phase** as the transmitter's carrier. If the phase is off by $\theta$, the recovered signal scales by $\cos(\theta)$ — a $90°$ phase error annihilates the message entirely. Real receivers use a Costas loop or PLL to lock onto the carrier phase.

## Formal definition

Let $R(j\omega)$ be the Fourier transform of $r(t)\cos(\omega_c t)$:

$$R(j\omega) = \tfrac{1}{2}M(j\omega) \;+\; \tfrac{1}{4}\bigl[M(j\omega + j2\omega_c) + M(j\omega - j2\omega_c)\bigr] \;+\; \tfrac{A}{2}\delta(\omega) \;+\; \tfrac{\pi A}{2}\bigl[\delta(\omega + 2\omega_c) + \delta(\omega - 2\omega_c)\bigr].$$

The four terms are: message at baseband, message images at $\pm 2\omega_c$, DC carrier residue, and carrier images at $\pm 2\omega_c$.

After an ideal LPF with cutoff $\omega_{\text{LP}}$ satisfying $B < \omega_{\text{LP}} < 2\omega_c$:

$$\text{output}(t) = \tfrac{1}{2}m(t) + \tfrac{A}{2}.$$

A **gain of $2$** at the output cancels the $\tfrac{1}{2}$, and DC blocking removes the $A/2$. Result: $m(t)$, recovered.

## Why it matters / when you use it

- **High-fidelity AM receivers.** Coherent demodulation has higher SNR than envelope detection (about $3$ dB) and works for **any** modulation index, including over-modulation.
- **Building block for SSB, DSB-SC, QAM.** All of these strip the carrier at the transmitter and *require* a coherent receiver — there's no envelope to detect.
- **Pedagogically.** It's just "multiplication is multiplication is multiplication" — the same operation that did the modulation does the demodulation. Hard to forget.

## Filter design — the LPF after multiplication

Choosing the LPF (a [[butterworth-filter]] in the lab):

| Parameter | Constraint | Lab default |
|---|---|---|
| **Cutoff frequency** | must satisfy $B < \text{cutoff} < 2\omega_c$ (in Hz: $2$ kHz $<$ cutoff $<$ $40$ kHz) | $\sim 5$ kHz comfortable |
| **Order $n$** | higher = sharper rolloff but more phase distortion | $4$–$6$ typical |

In MATLAB workspace for the lab Simulink model (the cutoff variable is in **rad/s**, not Hz):

```matlab
n      = 4;
cutoff = 2*pi*5000;     % 5 kHz cutoff in rad/s
```

## Common mistakes
- **Forgetting the gain of $2$.** The demod is $\tfrac{1}{2}m(t)$, not $m(t)$. Without the $\times 2$ gain, the recovered signal sounds quiet.
- **Using a cutoff $< B$.** You'll cut off the high-frequency content of the message itself. The cutoff must be **above** the message bandwidth.
- **Using a cutoff $> 2\omega_c$.** The $2\omega_c$ images leak through. Spectrum analyzer will show ghost peaks.
- **Phase mismatch between TX and RX carriers.** Out-of-phase by $90°$ kills the signal completely. Real systems use a PLL; in Simulink the carriers are tied to the same source so phase is exact.
- **Confusing $\text{cutoff}$ (rad/s) with $f_{\text{cutoff}}$ (Hz).** Simulink's Analog Filter Design block takes rad/s; multiply your Hz value by $2\pi$.

## Related
- [[amplitude-modulation]] — what this is undoing
- [[envelope-detection]] — the cheaper alternative; only works for $\mu \leq 1$
- [[modulation-index]] — coherent demod doesn't care about it (key contrast)
- [[butterworth-filter]] — the LPF used in the lab
- [[ofdm]] — coherent demod at scale; every subcarrier is its own coherent receiver

## Sources / further reading
- Lab manual: `raw/labs/EEE 304 Lab4.pdf` (section 2)
