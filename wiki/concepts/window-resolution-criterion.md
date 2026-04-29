---
title: Window Resolution Criterion
type: concept
course: [[eee-404]]
tags: [window, resolution, fft, dsp-design]
sources: [[homework-2026-04-27-eee-404-hw5]]
created: 2026-04-27
updated: 2026-04-27
---

# Window Resolution Criterion

## In one line
**Two spectral tones at frequencies $\omega_1$ and $\omega_2$ can be resolved through a window of length $L$ iff their separation $|\omega_1 - \omega_2|$ is at least the window's main-lobe width.**

## Example first
Two tones at $\omega_1 = \pi/4$ and $\omega_2 = \pi/3$. Separation: $\pi/3 - \pi/4 = \pi/12 \approx 0.262$ rad/sample.

| Window | Main-lobe width | Min $L$ to resolve | Verdict at $L = 64$ |
|:---|:---:|:---:|:---:|
| Rectangular | $4\pi / L$ | $4\pi/L \leq \pi/12 \Rightarrow L \geq 48$ | ✅ resolves |
| Hamming | $8\pi / L$ | $8\pi/L \leq \pi/12 \Rightarrow L \geq 96$ | ❌ blurs together |

So at $L = 64$ a rectangular window separates the two tones; a Hamming window doesn't.

## The idea
Multiplying $x[n]$ by a window $w[n]$ in time = **convolving** $X(e^{j\omega})$ with $W(e^{j\omega})$ in frequency. Each spectral impulse of $X$ gets replaced by a shifted copy of the window's spectrum $W$.

If the original spectrum had two impulses at $\omega_1$ and $\omega_2$, after windowing each becomes a "lump" of width $\Delta\omega_{\text{main}}$ (the window main-lobe width). The two lumps remain distinguishable only if their centers are far enough apart that the lumps don't merge — i.e., the centers are separated by **at least the main-lobe width**.

> If $|\omega_1 - \omega_2| < \Delta\omega_{\text{main}}$, the two impulses' main lobes overlap and you see one wide blob. Tones unresolvable.

## Main-lobe widths (memorize these four)

| Window | Main-lobe width | First side-lobe |
|:---|:---:|:---:|
| Rectangular | $4\pi/L$ | $-13$ dB |
| Bartlett (triangular) | $8\pi/L$ | $-26$ dB |
| Hamming | $8\pi/L$ | $-43$ dB |
| Hann | $8\pi/L$ | $-32$ dB |
| Blackman | $12\pi/L$ | $-58$ dB |

**Rule of thumb:** rectangular has the *narrowest* main lobe but the *worst* side-lobe leakage. Tapered windows (Hamming/Hann/Blackman) trade resolution for cleaner side-lobe rejection.

## Design recipe
1. Find the **smallest separation** $\Delta\omega_{\min}$ between any pair of tones you need to resolve.
2. Pick the window family based on side-lobe rejection requirements.
3. Set the window length $L$ so that **main-lobe width $\leq \Delta\omega_{\min}$**:
   - Rectangular: $L \geq 4\pi / \Delta\omega_{\min}$.
   - Hamming/Hann/Bartlett: $L \geq 8\pi / \Delta\omega_{\min}$.
   - Blackman: $L \geq 12\pi / \Delta\omega_{\min}$.

> [!tip] **Time-resolution trade-off.** A longer $L$ means finer frequency resolution but coarser **time** resolution — the window blurs over $L$ samples of time. The "best time-resolution while still resolving frequencies" is achieved at the **smallest $L$** that satisfies the criterion. See [[stft]].

## Why it matters
Two adjacent musical notes, two close radio carriers, two narrow-band interferers — if your window is too short for the tone separation, the FFT you compute will show one peak instead of two, and you've lost information you can't recover by post-processing. Pick $L$ first; everything else follows.

## Common mistakes
- **Using the rectangular formula for a Hamming window** (or vice versa). The factor of 2 between $4\pi/L$ and $8\pi/L$ matters.
- **Confusing resolution with bin spacing.** Bin spacing is $\Delta f = f_s/N$ (a property of the FFT length $N$, not the window length). Frequency *resolution* is the window's main-lobe width — you can have $N \gg L$ (zero-pad) and still not resolve the tones because the window length is what controls main-lobe width.
- **Picking the largest window.** A larger window resolves better in frequency but worse in time. For non-stationary signals, the *smallest* window meeting the resolution criterion is best.

## Related
- [[window-function]], [[hamming-window]], [[rectangular-window]], [[hann-window]], [[bartlett-window]]
- [[spectral-leakage]] — the side-lobe consequence of windowing
- [[frequency-resolution]] — bin spacing $\Delta f = f_s/N$, distinct from main-lobe width
- [[stft]] — short-time FFT, where the time-vs-frequency trade-off is central
- [[dtft]] — what gets convolved with $W(e^{j\omega})$

## Practice
- [[eee-404-hw5-walkthrough]] — HW5 problems 1(b,c) and 2(b,c) apply this criterion
