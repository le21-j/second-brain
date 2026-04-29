---
title: Butterworth Filter
type: concept
course: [[eee-304]]
tags: [eee-304, filter, lpf, bpf, communication, simulink, analog]
sources: [[lab-eee-304-lab-4-am-modulation]]
created: 2026-04-25
updated: 2026-04-26
---

# Butterworth Filter

## In one line
A Butterworth filter has a **maximally flat** magnitude response in the passband — no ripple at all — at the cost of a slow rolloff into the stopband; the **order $n$** controls how fast the rolloff is, and the **cutoff $\omega_c$** sets where it happens.

## Example first

In the lab Simulink "Analog Filter Design" block we set:

```matlab
n      = 4;            % filter order
cutoff = 2*pi*5000;    % 5 kHz cutoff, expressed in rad/s
```

This gives a **4th-order low-pass Butterworth** with magnitude response:

$$|H(j\omega)| = \frac{1}{\sqrt{1 + (\omega/\omega_c)^{2n}}} = \frac{1}{\sqrt{1 + \bigl(\omega/(2\pi \cdot 5000)\bigr)^{8}}}.$$

Plotting the magnitude:

| $\omega$ (Hz) | $|H|$ (4th-order at $5$ kHz) | What it does |
|---|---|---|
| $100$ Hz | $1.000$ | passes (deep passband) |
| $2{,}000$ Hz | $0.998$ | passes (the message) |
| $5{,}000$ Hz | $0.707$ ($= -3$ dB) | **the cutoff** |
| $10{,}000$ Hz | $0.062$ | attenuates $\sim 24$ dB |
| $40{,}000$ Hz | $0.00024$ | attenuates $\sim 72$ dB (the $2\omega_c$ image) |

So a 4th-order Butterworth at $5$ kHz **cleanly passes the $2$ kHz message** and **deeply attenuates the $40$ kHz demodulation image**. Job done.

## The idea

When you design a filter you trade off three things: **passband flatness**, **transition steepness**, and **phase linearity**. Different filter families pick different points on this trade space:

| Family | Passband | Transition | Stopband | Phase |
|---|---|---|---|---|
| **Butterworth** | maximally flat (no ripple) | gentle | monotonic | smooth |
| Chebyshev I | ripple in passband | steeper | monotonic | distorted |
| Chebyshev II | flat | steeper | ripple in stopband | distorted |
| Elliptic | ripple in both | steepest | ripple in both | most distorted |
| Bessel | flat | gentlest | gentle | linear (best) |

Butterworth is the **default workhorse** because it's flat in the passband (so it doesn't color the message) and the rolloff is "good enough" once you bump up the order.

## Formal definition

For a low-pass Butterworth of order $n$ with cutoff $\omega_c$:

$$|H(j\omega)|^2 = \frac{1}{1 + (\omega/\omega_c)^{2n}}.$$

Properties:

- At $\omega = \omega_c$, $|H| = 1/\sqrt{2} \approx 0.707$, i.e., $-3$ dB — by definition.
- The first $2n - 1$ derivatives of $|H|^2$ are zero at $\omega = 0$ — this is what "maximally flat" means.
- Stopband rolloff is $-20n$ dB/decade (or $-6n$ dB/octave). So a 4th-order filter rolls off at $-80$ dB/decade — every $10\times$ in frequency past the cutoff costs the signal a factor of $10^4$.

For a **bandpass** (used in [[envelope-detection]]):

- Specify two cutoffs $W_{\text{lo}}$ and $W_{\text{hi}}$, both in rad/s.
- Order $n$ applies to each transition. Lab #2 uses $n = 10$ for the bandpass.

## Why it matters / when you use it

- **Demodulation LPF.** Both [[coherent-demodulation]] (LPF) and [[envelope-detection]] (BPF) need a filter that doesn't distort the passband. Butterworth's flatness is exactly the property you want.
- **Anti-aliasing before sampling.** Smooth passband, smooth rolloff — minimal in-band distortion.
- **Default first guess.** When you don't have a specific reason to pick another family, start with Butterworth, evaluate, and switch only if you need (say) sharper rolloff ($\to$ elliptic) or linear phase ($\to$ Bessel).

## Choosing $n$ and $\text{cutoff}$ — a procedure

For a demodulation LPF after [[coherent-demodulation]] of a message at bandwidth $B$ modulated at carrier $\omega_c$:

> [!example] **Procedure**
> 1. **Cutoff lower bound:** must pass the message $\to$ $\text{cutoff} > B$ (with margin, say $\text{cutoff} > 1.2B$).
> 2. **Cutoff upper bound:** must reject the $2\omega_c$ demod image $\to$ $\text{cutoff} < 2\omega_c$ (with margin, say $\text{cutoff} < 0.5 \cdot 2\omega_c = \omega_c$).
> 3. **Pick something comfortably in the middle**, e.g., $\text{cutoff} = 2.5B$ if $2\omega_c \gg B$.
> 4. **Pick $n$ based on required attenuation at $2\omega_c$.** Each unit of $n$ adds $6$ dB/octave. For $60$ dB attenuation across one octave, $n \geq 10$; usually $n = 4$–$6$ is enough.
> 5. **Convert Hz $\to$ rad/s** if the block expects rad/s: $\text{cutoff}_{\text{rad}} = 2\pi \cdot \text{cutoff}_{\text{Hz}}$.

## Common mistakes

- **Mixing up Hz and rad/s.** Simulink's "Analog Filter Design" block typically takes **rad/s**. Pass `2*pi*f_hz`, not `f_hz`.
- **Picking $\text{cutoff} < B$.** Cuts off the message itself; demodulated output sounds muffled.
- **Picking $\text{cutoff} > 2\omega_c$.** Lets the demodulation image through; spectrum analyzer shows ghost tones.
- **Picking $n$ too high.** Each additional pole adds phase distortion (group-delay nonlinearity) and computational cost. $n = 4$–$6$ for most LPF demod work; $n = 10$ for the lab's bandpass because the band edges are aggressive.
- **Forgetting the variables must be in the workspace.** Simulink block reads $n$ and $\text{cutoff}$ from the MATLAB workspace; if you didn't `assignin` or run from the command window first, the block errors out.

## Related
- [[coherent-demodulation]] — uses Butterworth as the post-multiplication LPF
- [[envelope-detection]] — uses Butterworth as a bandpass to suppress DC and $2\omega_c$
- [[hamming-window]], [[hann-window]] — alternative shaping (frequency-domain windowing vs filtering — different tools, both shape spectra)

## Sources / further reading
- Lab manual: `raw/labs/EEE 304 Lab4.pdf` (sections used the Butterworth in both Simulink models)
- Wikipedia: https://en.wikipedia.org/wiki/Butterworth_filter
- MATLAB docs — `butter`, `analog filter design block`
