---
title: Chopper Amplifier
type: concept
course: [[eee-304]]
tags: [eee-304, communication, amplifier, chopping, modulation, square-wave, fourier-series, dc-amplification]
sources: [[homework-2026-04-26-eee-304-hw7]]
created: 2026-04-26
updated: 2026-04-26
---

# Chopper Amplifier

## In one line
A **chopper amplifier** modulates a low-frequency (or DC) signal up to a high frequency by multiplying it by a square wave, **amplifies the high-frequency copy** with a clean bandpass amplifier, then demodulates back down — sidestepping the $1/f$ noise and DC drift that plague direct DC amplification.

## Example first

The classic problem: amplify a slowly-varying sensor signal $x(t)$ (think thermocouple, microvolt range, near-DC). A direct DC amplifier suffers from $1/f$ noise, op-amp offset drift, and temperature drift — each of which is much worse at low frequencies than at high.

The chopper solution: **shift the signal up to high frequency**, amplify it there where the amplifier's noise floor is flat, then **shift it back**.

```
                    [bandpass amp gain A]
x(t) ──[× s(ω_c·t)]──► x_m(t) ──[H_BP·A]──► x_bp(t) ──[× s(ω_c·t)]──► x_d(t) ──[LPF]──► x_a(t)
       chopper up                                      chopper down            recover

           s(ω_c·t) is a 50% (or D) duty-cycle square wave at ω_c = 100 kHz (HW7)
```

By the end, $x(t)$ has been amplified by a factor of $2A\sin^2(\pi D)/\pi^2$ — and **all the low-frequency junk the bandpass amp would have added has been filtered out**, because we never amplified at low frequency to begin with.

## The idea

A square wave with period $T$ and duty $D$ (fraction of time high) has Fourier series

$$s(\omega_c t) = \sum_k \frac{2\sin(k\pi D)}{k}\cos(k\omega_c t).$$

Multiplying $x(t)$ by $s(\omega_c t)$ shifts copies of $X(j\omega)$ to every harmonic $\pm k\omega_c$, scaled by $\sin(k\pi D)/(k\pi)$ — that's the $k$-th Fourier coefficient of the square wave divided by $2\pi$ for the convolution.

Each spectral block:

| Block | What happens to $X(j\omega)$ |
|---|---|
| **chopper up** ($\times s(\omega_c t)$) | $X_m(j\omega) = \sum_k \frac{\sin(k\pi D)}{k\pi}\,X(j(\omega - k\omega_c))$ — replicas at every $k\omega_c$ |
| **bandpass amp** (gain $A$, narrow band around $\pm\omega_c$) | only $k = \pm 1$ survives: $X_{\text{bp}}(j\omega) = A \cdot \frac{\sin(\pi D)}{\pi}\,X(j(\omega - \omega_c))$ (and the $k = -1$ copy too) |
| **chopper down** ($\times s(\omega_c t)$ again) | each surviving replica gets re-shifted; $k = +1$ and $k = -1$ together produce a baseband copy at $k = 0$ |
| **LPF** | drops all the $k \neq 0$ byproducts |

The two $k = \pm 1$ survivors after the second multiplication add coherently at baseband, contributing $2[\sin(\pi D)/\pi]^2 = 2\sin^2(\pi D)/\pi^2$. Multiplied by the bandpass gain $A$:

==**Overall gain:** $\;G = \dfrac{2A\sin^2(\pi D)}{\pi^2}$.==

For 50% duty cycle ($D = 0.5$), $\sin^2(\pi/2) = 1$, so $G = 2A/\pi^2 \approx 0.20\,A$. You give up a factor of $\sim 5$ in gain for the privilege of running your amplifier at high frequency away from $1/f$ noise and DC drift.

## Formal definition (the HW7 derivation, step by step)

Block diagram:

```
x(t)  →  [×]  →  x_m(t)  →  [H_BP, gain A]  →  x_bp(t)  →  [×]  →  x_d(t)  →  [H_LP]  →  x_a(t)
          ▲                                                    ▲
          │                                                    │
       s(ω_c·t)                                            s(ω_c·t)
```

**Step 1 — Square wave Fourier series.** With $T_1 = D \cdot (T/2)$ and $\omega_c T_1 = \pi D$:

$$S(j\omega) = \sum_k \frac{2\sin(k\pi D)}{k}\,\delta(\omega - k\omega_c).$$

(Each impulse weight is $2\pi \times$ Fourier coefficient; some texts present the coefficients as $2\sin(k\pi D)/k$ directly, which is what HW7's worked solution uses.)

**Step 2 — First multiplication (chop up).**

$$X_m(j\omega) = \frac{1}{2\pi}\,X(j\omega) * S(j\omega) = \sum_k \frac{\sin(k\pi D)}{k\pi}\,X(j(\omega - k\omega_c)).$$

**Step 3 — Bandpass amplification.** $H_{\text{BP}}(j\omega)$ passes only the $k = \pm 1$ replicas:

$$X_{\text{bp}}(j\omega) = A \cdot \frac{\sin(\pi D)}{\pi}\bigl[X(j(\omega - \omega_c)) + X(j(\omega + \omega_c))\bigr].$$

**Step 4 — Second multiplication (chop down).**

$$X_d(j\omega) = \frac{1}{2\pi}\,X_{\text{bp}}(j\omega) * S(j\omega) = \sum_m \frac{\sin(m\pi D)}{m\pi}\,X_{\text{bp}}(j(\omega - m\omega_c)).$$

The $k = +1$ replica shifted by $m = -1$ lands at baseband. So does $k = -1$ shifted by $m = +1$. Both contribute $[\sin(\pi D)/\pi]^2 \, X(j\omega)$. Sum:

$$X_d(j\omega)\bigr|_{\text{baseband}} = 2A\left[\frac{\sin(\pi D)}{\pi}\right]^2 X(j\omega) + \text{(other terms at } \pm k\omega_c \text{ that LPF will kill)}.$$

**Step 5 — Lowpass.** Keep baseband only:

$$X_a(j\omega) = \frac{2A\sin^2(\pi D)}{\pi^2}\,X(j\omega).$$

==**Final gain:** $\;G = \dfrac{2A\sin^2(\pi D)}{\pi^2}$. Maximized at $D = 0.5$ $\to$ $G_{\max} = 2A/\pi^2$.==

## Why it matters / when you use it

- **DC-coupled instrumentation amplifiers.** Op-amp offset drift is *the* failure mode of high-gain DC amplification. Chopper-stabilized op-amps (LTC1051, LTC2050, AD8628) are entire product categories built around this technique.
- **Lock-in amplifiers.** A chopper at the source + a synchronous demodulator at the receiver. The $s(\omega_c t)$ square wave is the "reference"; the lock-in measures only the part of the input that correlates with the reference. Same math; instrumentation pedigree.
- **DSP analogue.** Same idea as moving low-frequency information to a high-frequency carrier for transmission ([[amplitude-modulation]]) — except here you don't transmit it, you just amplify it cleanly and bring it back. Pedagogic stepping stone between AM and lock-in detection.

## Common mistakes

- **Picking the wrong duty cycle and expecting unit gain.** The factor $\sin^2(\pi D)$ peaks at $D = 0.5$ but never exceeds $1$. There is **always** a $2/\pi^2 \approx 0.20$ ceiling on the gain coefficient. The bandpass $A$ does the heavy lifting.
- **Forgetting the bandpass step.** Without a bandpass amplifier (just an LPF), the chopper architecture wouldn't help — you'd amplify low-frequency noise too. The whole point is "amplify only the high-frequency neighborhood of $\pm\omega_c$ where the noise floor is flat."
- **Confusing $k\pi D$ with $k\pi T_1$.** $T_1$ is the high time of the square wave (in seconds); $D$ is the dimensionless duty fraction. The HW7 solution uses $\omega_c T_1 = \pi D$ to convert.
- **Treating the square wave as a single tone.** It's a sum of harmonics — the higher-order ones ($k = 3, 5, \ldots$ for symmetric square wave) leak through and would land at $\pm 2\omega_c$ and $\pm 4\omega_c$ after the second chopping. The LPF kills them; without the LPF the output is a mess.

## Related
- [[amplitude-modulation]] — the sinusoidal-carrier counterpart of chopping
- [[coherent-demodulation]] — same "multiply twice" structure, with sinusoid instead of square wave
- [[butterworth-filter]] — used as both the bandpass and the final lowpass
- [[homework-2026-04-26-eee-304-hw7]] — HW7 problem 3 derives the gain in full

## Sources / further reading
- HW7 problem 3: `raw/homework/HW7.pdf` and the fully worked sample at `raw/homework/304_hw7_sample25.pdf` (with spectrum sketches at $D = 0.5$)
- Wikipedia: https://en.wikipedia.org/wiki/Chopper_(electronics)
- Analog Devices, *Chopper-Stabilized Operational Amplifier* application notes
