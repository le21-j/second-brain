---
title: EEE 304 Lab 4 — AM Modulation/Demodulation in Simulink
type: summary
source_type: labs
source_path: raw/labs/EEE 304 Lab4.pdf
source_date: 2026-04-25
course:
  - "[[eee-304]]"
tags: [eee-304, lab, am, modulation, demodulation, simulink, butterworth, communication, audio]
created: 2026-04-25
updated: 2026-05-06
---

# EEE 304 Lab 4 — AM Modulation/Demodulation in Simulink

## TL;DR

A three-part Simulink lab exploring **amplitude modulation** and its two demodulation strategies. Part #1 builds and exercises a **coherent demodulator** with a tunable Butterworth LPF; Part #2 swaps in **envelope detection** (the cheap non-coherent receiver) with a Butterworth bandpass; Part #3 is a fill-in-the-blanks exercise that reconstructs a coherent demodulator and routes the famous Windows `tada.wav` audio through it. The lab's pedagogic spine is the **contrast between coherent and envelope demodulation**: coherent works for any modulation index $\mu$; envelope detection breaks the moment $\mu > 1$.

## Source files

- `raw/labs/EEE 304 Lab4.pdf` — the assignment write-up
- `raw/labs/AM_Mod_coherent.slx` — Simulink model for Part #1
- `raw/labs/AM_Mod_incoherent.slx` — Simulink model for Part #2
- `raw/labs/AM_Mod_coherent_tada_inc.slx` — Simulink model for Part #3 (with the missing blocks)
- `raw/labs/tada.wav` — audio source for Part #3

## Key takeaways

- **AM signal model:** $\Phi_{AM}(t) = \bigl(A + m(t)\bigr)\cos(\omega_c t)$. Bandwidth $= 2B$. Sidebands at $\omega_c \pm B$.
- **Coherent demodulation:** multiply by carrier again, lowpass-filter the $2\omega_c$ images. Output is $\tfrac{1}{2}m(t)$ so a gain-of-2 follows. ==Works for any $\mu$.==
- **Envelope detection:** rectify ($|\cdot|$) + bandpass ($W_{\text{lo}}$/$W_{\text{hi}}$). Cheap and carrier-recovery-free. ==Only works for $\mu \leq 1$.==
- **Modulation index $\mu = m_{\text{peak}}/A$.** $\mu < 1$ under-modulates; $\mu = 1$ is the boundary; $\mu > 1$ over-modulates and breaks envelope detection irreversibly.
- **Carrier-frequency sanity:** $\omega_c > 2B$ is the rule. Below that the AM sidebands overlap and the message is destroyed at the transmitter.
- **Filter design rule of thumb (this lab):** Butterworth, order $4$–$6$, LPF cutoff between $B$ and $2\omega_c$ for coherent demod; bandpass with $W_{\text{lo}} \approx 30$ Hz (kill DC offset from $+A$) and $W_{\text{hi}} \approx 5$ kHz (kill $2\omega_c$ rectification harmonics) for envelope detection.

## Concepts introduced (new pages)

- [[amplitude-modulation]] — the AM signal, USB/LSB, spectrum
- [[modulation-index]] — $\mu$ definitions and regimes
- [[coherent-demodulation]] — multiply + LPF receiver; works for any $\mu$
- [[envelope-detection]] — rectify + bandpass receiver; needs $\mu \leq 1$
- [[butterworth-filter]] — order/cutoff trade-offs in MATLAB/Simulink (rad/s units)

## Walkthrough

The full per-question walkthrough is at [[eee-304-lab-4-walkthrough]] — concept + steps + expected outcomes for every numbered question (#1.1 through #3), formatted with bold/highlights/callouts for easy scanning while in front of Simulink.

## Open questions / sanity flags

- The PDF is named **Lab 4** but the assignment section calls itself **"Lab 2 Assignment"** — likely a stale template heading. Treated as Lab 4 throughout.
- The `tada.wav` audio bandwidth assumed $\sim 8$ kHz for the Part #3 LPF cutoff choice. If the actual file is different (sample rate or content), the cutoff may need bumping.

## Related

- [[eee-304]] — the course page
- [[ofdm]] — multi-carrier descendant; orthogonal carrier frequencies for parallel AM channels
- [[modulation-classification]] — ML-PHY application: identifying modulation type from received samples
- [[autoencoder-phy]] — end-to-end ML modulation + demodulation, where you learn modulation schemes from data

## Sources / further reading
- Lab manual: `raw/labs/EEE 304 Lab4.pdf`
- Wikipedia: https://en.wikipedia.org/wiki/Amplitude_modulation
- B.P. Lathi, *Modern Digital and Analog Communication Systems*, ch. on linear modulation
