---
title: EEE 404 HW5 — Windowing, Resolution & FFT Compute Budget
type: summary
source_type: homework
source_path: raw/homework/hw5.pdf
source_date: 2026-04-27
course:
  - "[[eee-404]]"
tags: [eee-404, homework, dtft, dft, fft, windowing, hamming, rectangular, frequency-resolution, butterfly, stm32]
created: 2026-04-27
updated: 2026-05-06
---

# EEE 404 HW5 — Windowing, Resolution & FFT Compute Budget

## TL;DR
Two-problem homework set focused on **DTFT spectra of cosines, window-based spectral resolution, and FFT compute cost on the STM32**. Problem 1 (five parts) takes a two-tone signal at $f_s = 8$ kHz and asks how long a Hamming window must be to resolve the tones, the resulting DFT bin spacing, and the butterfly count for a 64-point FFT. Problem 2 (four parts) takes two signals sampled at $f_s = 1.68$ MHz, finds minimum rectangular and Hamming window lengths to resolve their frequency components, and finishes with a real-time-budget calculation tying segment length to a 168 MHz / 400-instruction processing budget.

## Source files
- `raw/homework/hw5.pdf` — the assignment, no solutions.

## Key takeaways
- **DTFT of $A\cos(\omega_0 n + \phi)$** is two impulses at $\pm \omega_0$, each of magnitude $A\pi$. Phase $\phi$ shifts the impulse phase but not the magnitude. Spectrum is $2\pi$-periodic. See [[dtft]].
- **Window resolution criterion:** two tones at $\omega_1, \omega_2$ are resolvable through a length-$L$ window iff $|\omega_1 - \omega_2| \geq \Delta\omega_{\text{main}}$. Rectangular: $\Delta\omega_{\text{main}} = 4\pi/L$. Hamming: $8\pi/L$. See [[window-resolution-criterion]].
- **Best time-resolution = smallest $L$** that still satisfies the frequency-resolution criterion. Trade-off is fundamental: bigger window → better $\Delta f$ but worse time localization.
- **DFT bin spacing $\Delta f = f_s/N$** is *independent* of the window shape — it depends only on FFT length $N$ and sampling rate $f_s$. Don't confuse this with main-lobe width.
- **FFT butterfly count:** an $N$-point radix-2 FFT runs $\log_2(N)$ stages of $N/2$ butterflies each $\Rightarrow$ $\frac{N}{2}\log_2(N)$ butterflies total. For $N = 64$: $32 \cdot 6 = 192$.
- **Real-time DSP budget:** processing time $\leq$ acquisition time. Processing time = (instructions) / (clock rate). Acquisition time = $L \cdot T_s$. Solve for max $L$ that fits the budget.

## Concepts introduced (new pages)
- [[dtft]] — Discrete-Time Fourier Transform, the continuous-frequency parent of the DFT
- [[window-resolution-criterion]] — when can a window separate two tones?

## Concepts reinforced
- [[hamming-window]], [[rectangular-window]] — main-lobe widths used as the design constraints
- [[frequency-resolution]] — $\Delta f = f_s/N$, used in 1(d)
- [[butterfly]], [[fft]] — used in 1(e)
- [[spectral-leakage]] — the cost of windowing
- [[stft]] — the time-vs-frequency trade-off implicit in 1(c)

## Walkthrough
The full per-problem walkthrough is at [[eee-404-hw5-walkthrough]] — concept-first, step-by-step derivation for every sub-question, with **collapsible drop-downs** next to each headline equation that expand to show the full derivation. Same `==highlight==` + callout-block format as the EEE 304 / 350 HW7 walkthroughs.

## Open questions / follow-ups
- HW5 doesn't include a worked-solution sample. Cross-check against Lecture 6 / `slides-fft-implementation.pdf` for the butterfly-count formula and `slides-window-functions.pdf` for the main-lobe widths.
- Problem 2(d)'s answer ($L^* = 4$) is much smaller than the resolution requirement of 2(b)/2(c) ($L \geq 24$ or $48$). The problem is illustrating the **fundamental tension** between real-time processing and frequency resolution — the lab-7 STM32 runs into the same wall.

## Related
- [[eee-404]] — course page
- [[lab-7-fft]] — earlier lab where the same STM32 / 168 MHz processor and FFT compute model came up
- [[fft-fundamentals-set-01]] — practice set covering the same concepts (MC questions from lecture)
