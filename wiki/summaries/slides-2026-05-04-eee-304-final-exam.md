---
title: EEE 304 Final Exam (1 pp, 8 problems, 350 pts) — Source Summary
type: summary
source_type: slides
source_path: raw/slides/eee-304/304final-1.pdf
source_date: 2026-05-04
course:
  - "[[eee-304]]"
tags: [eee-304, final, exam, source, transfer-function, steady-state, butterworth, roc, forward-euler, pam, tdm, phase-margin, sampled-data]
created: 2026-05-04
---

# EEE 304 Final Exam — Source Summary

## TL;DR

Single-page final exam (Tsakalis 2026): **8 problems, 350 pts, open-book**. Each problem corresponds 1:1 to one of the 8 problem types in the [[slides-2026-05-04-eee-304-final-exam-preview]] preview deck — no surprises. Bottom of the sheet has a small Laplace + Fourier + z-transform pair table (the same one repeated on slide 1 of the preview).

## The 8 problems (numbers + topic)

| # | pts | topic | numbers |
|---|---:|---|---|
| 1 | 40 | Steady-state to step (4 sub-systems, mix DT/CT, mix stable/unstable) | systems given as ODE/difference equations |
| 2 | 40 | First-order CT LPF, find $\tau$ | $f_c = 7$ Hz |
| 3 | 40 | First-order DT LPF, find $a$ | $f_s = 200$ Hz, $f_c = 10$ Hz |
| 4 | 40 | ROC of stable system | $H(z) = (z-4)/[(z+0.5)(z-0.2)]$ |
| 5 | 40 | Forward Euler discretization | $H(s) = 1/(0.01s + 2)^2$, $f_s = 200$ Hz |
| 6 | 50 | TDM PAM bandwidth | 8 kHz voice, 225 kHz channel limit |
| 7 | 50 | Loop shaping (gain crossover + phase margin) | $\omega_{gc} = 4$ rad/s, PM = 50° |
| 8 | 50 | Sampled-data + ideal reconstruction | $H(z) = (z-1)/(z-0.7)$, $T = 0.01$ s, $x(t) = \cos(t) + 1$ |

## Key takeaways

- **No surprises** vs the preview. Every problem is one of the 8 types previewed.
- **Problem 1 has 4 sub-systems** with mixed stability — the trap is applying FVT to unstable systems. Two of the four are unstable; "DNE" is the right answer for those.
- **Problem 5 collapses both poles to $z = 0$** because $\omega_c T = 1$ exactly — illustrates the FE-fails-when-not-oversampled lesson.
- **Problem 8's filter has a zero at $z = 1$** (DC notch / high-pass) — the constant term in $x(t)$ is killed; only the $\cos(t)$ component survives, scaled to ~$0.033$ and shifted by ~$90°$ (filter ≈ derivative at low frequencies).
- **Problem 7 is the only design problem** — both phase and magnitude conditions at $\omega_{gc} = 4$, two unknowns, solved sequentially (phase first → $\tau_z$, then magnitude → $K$).

## Filed alongside

- [[eee-304-final-exam-walkthrough]] — full per-problem solutions.
- [[slides-2026-05-04-eee-304-final-exam-preview]] — the preview deck that maps each exam problem to its source module/HW/lab.
- `raw/slides/eee-304/fourier.pdf` — the 12-page Oppenheim-Willsky transform tables (open-book reference, summarized below).

## Open-book reference panel (`fourier.pdf`, 12 pp — Oppenheim/Willsky tables)

Includes (page-indexed roughly):
- **Table 5.3** — Fourier series + transform expressions (CT vs DT, time vs frequency)
- **Table 3.1, 3.2** — FS properties (CT, DT)
- **Table 4.1, 4.2** — FT properties + basic pairs (CT)
- **Table 5.1, 5.2** — DTFT properties + pairs
- **Table 9.1, 9.2** — Laplace properties + pairs (with ROC)
- **Table 10.1, 10.2, 10.3** — z-transform properties + pairs (with ROC) + unilateral z-transform

This is the canonical open-book sheet. Bring it to the exam — every transform you need is in here, no need to memorize.
