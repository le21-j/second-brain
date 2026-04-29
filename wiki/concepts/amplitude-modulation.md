---
title: Amplitude Modulation (AM)
type: concept
course: [[eee-304]]
tags: [eee-304, communication, modulation, am, fourier, sideband, carrier]
sources: [[lab-eee-304-lab-4-am-modulation]]
created: 2026-04-25
updated: 2026-04-26
---

# Amplitude Modulation (AM)

## In one line
Take a high-frequency carrier $\cos(\omega_c t)$ and let its amplitude **track** a low-frequency message $m(t)$ — the result $(A + m(t))\cos(\omega_c t)$ carries the message but lives at the carrier's frequency, which is exactly what makes long-distance radio practical.

## Example first

**Concrete numbers** (from [[lab-eee-304-lab-4-am-modulation]]): message tone at $2$ kHz, carrier at $20$ kHz, carrier amplitude $A = 2$.

$$m(t) = \sin(2\pi \cdot 2000 \cdot t) \qquad\text{(2 kHz tone)}$$

$$c(t) = 2\cos(2\pi \cdot 20000 \cdot t) \qquad\text{(20 kHz carrier)}$$

$$\Phi_{AM}(t) = \bigl(2 + m(t)\bigr)\cos(2\pi \cdot 20000 \cdot t) \qquad\text{(AM signal)}$$

In the **time domain**, the AM signal looks like a fast $20$ kHz oscillation whose envelope traces out the slow $2$ kHz tone — exactly Figure 1 in the lab manual.

In the **frequency domain**, the spectrum has three pieces:
- A **delta at $\pm 20$ kHz** (the unmodulated carrier).
- A copy of $M(j\omega)$ shifted to $+20$ kHz (around the positive carrier).
- A copy of $M(j\omega)$ shifted to $-20$ kHz (around the negative carrier).

Each shifted copy has an **upper sideband (USB)** above the carrier and a **lower sideband (LSB)** below. For our $2$ kHz tone, the sidebands are spectral lines at $18$ kHz and $22$ kHz.

## The idea

We want to send $m(t)$ ($\leq$ a few kHz, e.g. voice $\approx 4$ kHz) over the air. Two problems with sending it directly:
- **Antenna size.** The wavelength of a $1$ kHz EM wave is $300$ km; you cannot build that antenna.
- **Sharing the spectrum.** Everyone's voice is at $0$–$4$ kHz. If everyone transmits at baseband, everyone collides.

Both are fixed by **shifting $m(t)$ up to a much higher frequency** before transmission. AM picks the simplest possible shift: multiply by a single sinusoid $\cos(\omega_c t)$ and add the carrier itself so the envelope is always non-negative (which lets the cheap [[envelope-detection]] receiver work).

## Formal definition

$$\Phi_{AM}(t) = \bigl(A + m(t)\bigr)\cos(\omega_c t) = A\cos(\omega_c t) + m(t)\cos(\omega_c t)$$

- $A\cos(\omega_c t)$ — the **carrier**, an unmodulated tone at $\omega_c$.
- $m(t)\cos(\omega_c t)$ — the **modulated** part, a frequency-shifted copy of the message.

By the modulation property of the Fourier transform:

$$\mathcal{F}\bigl\{m(t)\cos(\omega_c t)\bigr\} = \tfrac{1}{2}\bigl[M(j\omega + j\omega_c) + M(j\omega - j\omega_c)\bigr]$$

so the full AM spectrum is

$$\mathcal{F}\bigl\{\Phi_{AM}(t)\bigr\} = \tfrac{1}{2}\bigl[M(j\omega + j\omega_c) + M(j\omega - j\omega_c)\bigr] + \pi A\bigl[\delta(\omega + \omega_c) + \delta(\omega - \omega_c)\bigr].$$

Each shifted copy has amplitude $A$ at peak (down from $2A$ in $M(j\omega)$ because of the $\tfrac{1}{2}$ factor). The total occupied bandwidth is $2B$ centered on $\omega_c$, where $B$ is the message bandwidth — twice the message's own bandwidth (this is the "wasted spectrum" SSB/DSB-SC try to recover).

## Why it matters / when you use it

- **AM broadcast radio ($530$–$1700$ kHz).** Direct application of this formula.
- **Pedagogy.** AM is the simplest modulation to derive — every other modulation (FM, PM, QAM, SSB) is most easily explained as a deviation from AM.
- **Building block for ML-PHY.** [[neural-receiver]] and [[autoencoder-phy]] still need to recover spectra; understanding AM analytically is the floor.

## Common mistakes
- **Forgetting the $\tfrac{1}{2}$ in the shifted copies.** Spectrum analyzer shows sidebands at amplitude $A$, not $2A$ — the $\tfrac{1}{2}$ factor halved them.
- **Confusing carrier amplitude $A$ with modulation index $\mu$.** They're related ($\mu = m_{\text{peak}}/A$) but $A$ is a free design choice; $\mu$ is the consequence. See [[modulation-index]].
- **Picking $\omega_c < 2B$.** The two shifted copies of $M(j\omega)$ overlap each other, irreversibly destroying the signal. Always choose $\omega_c \gg B$.
- **Treating AM and DSB-SC as the same.** AM has the carrier $A\cos(\omega_c t)$ term added; DSB-SC drops it. AM is bigger but enables envelope detection; DSB-SC is more efficient but needs coherent demodulation.

## Related
- [[modulation-index]] — the $\mu$ parameter that controls the depth of modulation
- [[coherent-demodulation]] — the recovery method that works for any $\mu$
- [[envelope-detection]] — the cheaper recovery method that needs $\mu \leq 1$
- [[butterworth-filter]] — what we use for the LPF after demodulation
- [[ofdm]] — spiritual descendant; multi-carrier AM with orthogonal $\omega_c$'s
- [[modulation-classification]] — ML side: identifying modulation type from received samples

## Sources / further reading
- Lab manual: `raw/labs/EEE 304 Lab4.pdf` (sections 1–3)
- Wikipedia: https://en.wikipedia.org/wiki/Amplitude_modulation
- B.P. Lathi, *Modern Digital and Analog Communication Systems* — chapter on linear modulation
