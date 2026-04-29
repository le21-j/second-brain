---
title: EEE 404 Module 11 — Effect of Window + Speech Analysis (slide deck summary)
type: summary
source_type: slides
source_path: raw/slides/eee-404/m11-effect-of-window.pdf
source_date: 2026-04-29
course: [[eee-404]]
tags: [eee-404, window-function, spectral-leakage, speech-analysis, time-frequency, stft]
created: 2026-04-29
---

# EEE 404 Module 11 — Effect of Window + Speech Analysis

**Source:** Two PDFs in `raw/slides/eee-404/`:
- [`m11-effect-of-window.pdf`](../../raw/slides/eee-404/m11-effect-of-window.pdf) — main-lobe / side-lobe trade-offs in detail
- [`m11-speech-analysis.pdf`](../../raw/slides/eee-404/m11-speech-analysis.pdf) — applying STFT to speech (voiced/unvoiced, pitch, formants)

## TL;DR
Module 11 closes out the FFT chapter by examining how windowing shapes the DFT spectrum (spectral leakage, time-frequency trade-off) and applies it to **speech**. The "Effect of Window" deck quantifies the main-lobe-width vs. side-lobe-height trade-off across rect/Bartlett/Hann/Hamming/Blackman. The "Speech Analysis" deck shows STFT output for voiced (vowel) vs. unvoiced (fricative) speech, identifies pitch from low-frequency peaks, and motivates frame-based processing.

## Key takeaways

### Effect of Window
- **Spectral leakage** — energy from a tone at $\omega_0$ "leaks" into neighbouring DFT bins because the window's DTFT has finite-width main lobe and finite-height side lobes.
- **Trade-off table** (already in [[eee-404-exam-2-study-guide]]):
  | Window | Main lobe (rad/sample) | Peak side lobe (dB) |
  |---|---|---|
  | Rectangular | $4\pi/L$ | −13 |
  | Bartlett | $8\pi/L$ | −25 |
  | Hann | $8\pi/L$ | −31 |
  | Hamming | $8\pi/L$ | −41 |
  | Blackman | $12\pi/L$ | −58 |
- **Picking a window:** rectangular for max resolution; Hamming/Hann for general-purpose; Blackman when side-lobes must be small (e.g., faint tone next to loud one).

### Speech Analysis
- **Voiced speech** (vowels) is quasi-periodic — STFT shows clear pitch + harmonics.
- **Unvoiced** (fricatives like "s", "f") is noise-like — STFT shows broad spread.
- **Frame-based processing:** typical speech frame is **20–30 ms** (~$L = 160$–$240$ at 8 kHz), windowed with Hamming, overlapped 50%.
- **Pitch detection:** find the lowest-frequency peak in the magnitude spectrum.
- **Formants:** the 3–4 lowest spectral peaks above pitch — encode vowel identity.

## Concepts introduced / reinforced
- [[spectral-leakage]] — the reason windowing exists
- [[window-function]], [[hamming-window]], [[hann-window]], [[bartlett-window]], [[rectangular-window]] — all already in wiki
- [[stft]] — applies windowing to time-localised spectra

## Exam tie-in
**Exam 2 Practice Problem 3(b)** asks for the resolution condition using the rectangular-window main-lobe width. The walkthrough covers it.

**Exam 2 review topic list** specifically includes "Window functions (main lobe width and side lobes height tradeoff)" and "Effect of windowing, spectral leakage, time and frequency resolution tradeoff" — both directly from this module.

## Lab / EC tie-in
The **EC Quantum Lab** uses speech compression via peak-picking (FFT-based and QFT-based). The frame-based STFT structure from this module is exactly the J-DSP `SigGen(L)` block's behavior.

## Questions raised
- Is the speech analysis material on the exam? (Per the topic list, only window-related; speech specifics are background.)
