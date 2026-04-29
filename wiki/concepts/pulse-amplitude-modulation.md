---
title: Pulse Amplitude Modulation (PAM)
type: concept
course: [[eee-304]]
tags: [eee-304, communication, modulation, pam, pulse, sampling, tdm]
sources: [[homework-2026-04-26-eee-304-hw7]]
created: 2026-04-26
updated: 2026-04-26
---

# Pulse Amplitude Modulation (PAM)

## In one line
PAM is the simplest pulse modulation: take a continuous-time message $m(t)$, sample it at regular intervals, and send each sample as a **pulse** whose **amplitude equals the sample value** — so the message rides on a train of fixed-width pulses spaced one sample period apart.

## Example first

A $4$ kHz audio tone, sampled at $8$ kHz (Nyquist):

$$m(t) = \sin(2\pi \cdot 4000 \cdot t), \qquad T_s = \frac{1}{8000} = 125\,\mu\text{s},$$

sample at $t = 0, 125\,\mu\text{s}, 250\,\mu\text{s}, \ldots$

The PAM output:

$$\text{PAM}(t) = \sum_n m(n T_s)\,p(t - n T_s),$$

where $p(t)$ is a narrow rectangular pulse (width $\tau \ll T_s$). What the wire sees is a **stream of pulses**, one every $125\,\mu$s, with **heights** that trace out the original sine.

> [!tip] **PAM is sampling, made visible.** When you sample $m(t)$ ideally with a Dirac comb you get $\sum_n m(n T_s)\,\delta(t - n T_s)$. PAM is the same thing but each delta is **stretched into a finite-width pulse** so it can actually be transmitted.

## The idea

Two reasons to convert continuous $m(t)$ into a pulse stream:

1. **Time-division multiplexing (TDM).** Once a signal is a pulse train, you have **silence between pulses** — slots you can use to interleave other signals' pulses. See [[time-division-multiplexing]]. This is the dominant motivation for PAM in HW7 problem 2.
2. **Digitization.** Quantize each pulse height to a finite set of levels and you have PCM (Pulse Code Modulation) — the foundation of all digital audio, telephony, and modern wireless.

## Formal definition

For a message $m(t)$ bandlimited to $B$, sampled at rate $f_s \geq 2B$ (Nyquist), with pulse $p(t)$ of width $\tau$:

$$\text{PAM}(t) = \sum_{n=-\infty}^{\infty} m(n T_s)\,p(t - n T_s), \qquad T_s = \frac{1}{f_s}.$$

In the **frequency domain**, the spectrum of an ideally-sampled signal is

$$\sum_k M(j(\omega - k\omega_s)) \qquad\text{where } \omega_s = 2\pi f_s,$$

— copies of $M(j\omega)$ at every multiple of $\omega_s$. PAM with finite-width pulses scales each copy by the pulse's Fourier transform $P(j\omega)$ (a sinc-shape for rectangular $p$), but the recovery method is the same as for ideal sampling: **lowpass filter** to keep only the baseband copy, recover $m(t)$.

==**Master rule (Nyquist):** the sample rate must satisfy $f_s \geq 2B$. For audio bandlimited to $20$ kHz, $f_s \geq 40$ kHz.==

## Why it matters / when you use it

- **TDM in telephony.** Classic T1 lines multiplex $24$ voice channels, each PAM-sampled at $8$ kHz, into a single $1.544$ Mbps stream. Same idea HW7 problem 2 is asking about.
- **A/D converters.** Every ADC starts by doing PAM internally — sample-and-hold at $f_s \geq 2B$, then quantize.
- **Stepping stone to PCM and digital comms.** Quantize the PAM amplitudes $\to$ PCM. Encode the bits $\to$ QAM/QPSK/etc. Everything starts from "sample the analog signal."

## Common mistakes

- **Sampling at exactly $2B$.** This is Nyquist *floor*, not Nyquist *recipe*. In practice you sample at $2.2B$ to $2.5B$ to leave room for non-ideal anti-aliasing filters. The HW says "at least" $40$ kHz for $20$ kHz audio.
- **Forgetting the sync slot in TDM.** When multiplexing $N$ PAM signals, you need at least one extra slot per frame for synchronization (so the receiver knows which pulse belongs to which channel). HW7 problem 2 explicitly accounts for this with $20 + 1 = 21$ slots.
- **Confusing pulse width with pulse period.** Width $\tau$ is how wide each pulse is. Period $T_s$ is how often pulses come. $\tau \ll T_s$ for clean PAM.
- **Mixing PAM with PWM / PPM.** PAM modulates **amplitude**. PWM modulates **width**. PPM modulates **position in time**. Different schemes; PAM is the simplest.

## Related
- [[time-division-multiplexing]] — what PAM enables (multiplexing many signals on one wire)
- [[amplitude-modulation]] — sibling concept, but for continuous (not pulse) carriers
- [[modulation-index]], [[coherent-demodulation]], [[envelope-detection]] — AM-side counterparts
- [[sampling-theorem]] — *(future page)* the Nyquist criterion that governs $f_s$

## Sources / further reading
- HW7 problem 2: `raw/homework/HW7.pdf` and the worked sample at `raw/homework/304_hw7_sample25.pdf`
- B.P. Lathi, *Modern Digital and Analog Communication Systems*, ch. 6
- Wikipedia: https://en.wikipedia.org/wiki/Pulse-amplitude_modulation
