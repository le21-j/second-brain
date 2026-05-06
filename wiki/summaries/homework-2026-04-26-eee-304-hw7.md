---
title: EEE 304 HW7 — Cascaded AM, TDM-PAM, Chopper Amplifier
type: summary
source_type: homework
source_path: raw/homework/HW7.pdf
source_date: 2026-04-26
course:
  - "[[eee-304]]"
tags: [eee-304, homework, am, modulation, demodulation, pam, tdm, chopper-amplifier, fourier]
created: 2026-04-26
updated: 2026-05-06
---

# EEE 304 HW7 — Cascaded AM, TDM-PAM, Chopper Amplifier

## TL;DR

Three-problem homework set built on the AM material from Lab 4. **Problem 1** asks for the demod frequencies after cascaded modulation (multiplying by $\cos(2\pi(100\text{ kHz})t)$ then $\cos(2\pi(300\text{ kHz})t)$) — the answer is the **sum and difference** of the two carriers ($200$ kHz or $400$ kHz). **Problem 2** is a TDM-PAM bandwidth calculation — sample 20 audio channels at Nyquist ($40$ kHz each), squeeze them plus a sync slot into each frame, and the wire's pulse rate must reach $\mathbf{840}$ **kHz**. **Problem 3** is the **chopper amplifier** — derive the overall gain $G = 2A\sin^2(\pi D)/\pi^2$ by carrying the message up through a square-wave Fourier series, bandpass-amplifying at $\omega_c$, and choppering back down.

## Source files

- `raw/homework/HW7.pdf` — the assignment, no solutions (2026 copyright)
- `raw/homework/304_hw7_sample25.pdf` — the same three problems with **fully worked solutions** from a previous semester (2024 copyright). Use as a verification reference, not a substitute for the derivation.

## Key takeaways

- **Cascaded modulation** creates replicas at $f_1 \pm f_2$ (sum and difference). Either one is a valid demodulation frequency, because demodulation just shifts a chosen replica back to baseband.
- **TDM-PAM bandwidth** $= (N + N_{\text{sync}}) \cdot f_s$ where $f_s$ is the per-channel Nyquist rate. Always include the sync slot — forgetting it gives a tempting wrong answer ($800$ kHz instead of $840$ kHz here).
- **Chopper amplifier gain** $= \dfrac{2A\sin^2(\pi D)}{\pi^2}$, peaked at $D = 0.5$ giving $G_{\max} \approx 0.20\,A$. The factor of $\sim 5$ loss vs direct DC amplification is the price of escaping $1/f$ noise + drift.
- **Square-wave Fourier series:** $s(\omega_c t) = \sum_k \dfrac{2\sin(k\pi D)}{k}\cos(k\omega_c t)$. Even-$k$ terms vanish at 50% duty.
- **The bandpass amplifier in the chopper is *necessary*, not stylistic** — it picks off only the $k = \pm 1$ replicas so the second chopping cleanly reconstructs the message.

## Concepts introduced (new pages)

- [[pulse-amplitude-modulation]] — sample, send each sample as a pulse
- [[time-division-multiplexing]] — interleave multiple PAM streams in a frame with sync
- [[chopper-amplifier]] — the full architecture and the gain derivation

## Walkthrough

The full per-problem walkthrough is at [[eee-304-hw7-walkthrough]] — concept + step-by-step derivation + cross-check against the 2024 sample for every problem. Designed to be readable while doing the homework.

## Open questions / follow-ups

- The course hasn't yet introduced (in this vault) the **sampling theorem** as its own page. Problem 2 leans on it implicitly. ==Worth promoting to a dedicated `[[sampling-theorem]]` page once Lab 5 / HW8 force the issue.==
- Problem 3's spectrum sketches are best drawn by hand. The walkthrough lists what each panel should show, but Jayden may want to verify by simulating the chopper in Simulink (analogous to Lab 4's models) — a possible extension.

## Related

- [[eee-304]] — course page
- [[lab-eee-304-lab-4-am-modulation]] / [[eee-304-lab-4-walkthrough]] — Lab 4, the prerequisite material for everything in HW7
- [[amplitude-modulation]] — the underlying signal model
- [[coherent-demodulation]], [[envelope-detection]] — demodulation methods that frame Problem 1
- [[butterworth-filter]] — the filter family used for the bandpass (chopper) and the lowpass (final stage)
- [[modulation-index]] — $\mu = m_{\text{peak}}/A$, threshold for envelope detection

## Sources / further reading

- HW7 (this assignment): `raw/homework/HW7.pdf`
- Sample with worked solutions: `raw/homework/304_hw7_sample25.pdf`
- B.P. Lathi, *Modern Digital and Analog Communication Systems* — chapters on AM, sampling, TDM
