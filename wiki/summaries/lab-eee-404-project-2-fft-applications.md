---
title: EEE 404 Project 2 — Applications of Fast Fourier Transform (Source Summary)
type: summary
source_type: labs
source_path: raw/labs/eee-404/project-2-lab-manual.pdf
source_date: 2026-05-02
course:
  - "[[eee-404]]"
tags: [eee-404, project, fft, stft, windowing, vowel-analysis, pitch-detection, formant, stm32, cmsis]
created: 2026-05-02
updated: 2026-05-06
---

# EEE 404 Project 2 — Applications of Fast Fourier Transform

## TL;DR
Two FFT-based DSP applications on the STM32F407G-DISC1: (1) **vowel analysis** — record "a" and "i" through Audacity, find pitch via autocorrelation and read off formants from the FFT plot in MATLAB, then mirror the algorithm on the MCU by implementing `max_index`; and (2) a **real-time spectrum analyzer** — the on-board MP45DT02 PDM mic feeds the STM32, which runs a 1024-point FFT via the CMSIS DSP library and streams power-spectrum bins over UART (115 200 baud) to a MATLAB plot. Student fills four `FILL_IN_BLANK` lines and writes one helper (`apply_window`) to enable Hamming/Hanning/rectangular windows.

## Key takeaways
- **CMSIS `arm_rfft_fast_f32` packed format** — for a real $N$-point input, the output buffer holds $N/2$ complex bins as $\{\text{Re}[0], \text{Re}[N/2], \text{Re}[1], \text{Im}[1], \text{Re}[2], \text{Im}[2], \dots\}$. Bin 0 (DC) and bin $N/2$ (Nyquist) are real-valued, so they get packed into the first two slots to save space — easy to mishandle.
- **Pitch ≠ formant.** Pitch is the **fundamental frequency** $f_0$ of the glottal source (about 100–250 Hz). Formants are **vocal-tract resonances** ($F_1, F_2, F_3, \dots$) — they shape the spectral envelope and identify the vowel. Pitch is read from the **autocorrelation peak**, formants are read from the **FFT magnitude peaks**.
- **Why autocorrelation for pitch?** Periodicity at lag $T$ means the autocorrelation has a peak at lag $T$. Inverse-FFT of the power spectrum equals the autocorrelation (Wiener–Khinchin). The first non-trivial peak gives the pitch period in samples; $f_0 = f_s / T$.
- **Windowing controls spectral leakage.** Rectangular = sharpest mainlobe but worst sidelobes ($-13$ dB). Hamming/Hanning trade mainlobe width for sidelobe rejection ($-43$ dB / $-31$ dB). The visual difference is dramatic on a single sinusoid. See [[window-function]], [[hamming-window]], [[hann-window]], [[rectangular-window]].
- **STFT pipeline = window → FFT → magnitude² → log → display.** This project builds exactly that pipeline in C, then sends the dB values out USART for plotting.

## Files in `raw/labs/eee-404/`
- `project-2-lab-manual.pdf` — the assignment.
- `project-2-overview-slides.pdf` — overview deck.
- `project-2-code/` — starter project (unzipped from `project-2-code.zip`):
  - `audio_spectrum_analyzer/` — STM32CubeIDE project for the real-time spectrum analyzer.
  - `vowel_analysis/` — STM32 project for vowel analysis (uses pre-recorded `vowel_a.h` / `vowel_i.h` headers).
  - `uart_receive_fft_plot_spectrum.m` — MATLAB receiver that opens COM31 @ 115 200 baud and bar-plots the FFT.
- `project-2-pages/` — Canvas wiki pages (just MediaPlus video iframes — no text content, watch the videos for the workflow).

## Concepts introduced or reinforced
- [[fft]] — the workhorse; reused from Lab 7.
- [[real-valued-fft]] — 2× memory saving for real input; CMSIS uses this.
- [[stft]] — the spectrum analyzer is a streaming STFT.
- [[window-function]], [[hamming-window]], [[hann-window]], [[rectangular-window]] — windowing.
- [[autocorrelation-pitch-detection]] *(new)* — Wiener–Khinchin shortcut for pitch.
- [[formant]] *(new)* — vocal-tract resonances; separate from pitch.
- [[cmsis-dsp-fft]] *(new)* — the `arm_rfft_fast_*` API and packed output layout.

## Worked examples worth remembering
- **Pitch from autocorrelation peak.** If the autocorrelation peak (excluding lag 0) is at sample index $k$ and $f_s = 8000$ Hz, then $f_0 = f_s / k = 8000 / k$ Hz. The MATLAB reference script reports both `pitch_index` and `pitch` (Hz).
- **Spectrum from CMSIS packed output.** For $i \geq 2$ even: $|Y[i/2]|^2 = Y[i]^2 + Y[i+1]^2$. For the two real-only bins: $|Y[0]|^2 = Y[0]^2$, $|Y[N/2]|^2 = Y[1]^2$.

## Questions this source raised
- The Canvas pages for the project are video-only (no transcripts). If the formant and pitch reading workflow is unclear, the videos have to be watched — there is no written instruction on which spectrogram pane to look at.
- The lab manual shows a wiring diagram for a generic CH340 USB-to-serial converter without specifying which one Jayden bought; the pinout matches the standard 4-pin board the course distributes.
