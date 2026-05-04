---
title: CMRR — Mistakes
type: mistake
course:
  - "[[eee-335]]"
tags:
  - mistakes
  - cmrr
  - differential-pair
concept:
  - "[[cmrr]]"
  - "[[differential-pair]]"
  - "[[current-mirror]]"
  - "[[cascode-amplifier]]"
created: 2026-05-04
updated: 2026-05-04
---

# CMRR — Common Mistakes

## Known gotchas (general)

- **The $\tfrac{1}{2}$'s cancel in the ratio.** Both single-ended gains carry a factor of $\tfrac{1}{2}$:
  $$A_{d,s.e.} = \tfrac{1}{2} g_m R_D, \qquad A_{cm,s.e.} \approx -\frac{R_D}{2 R_{SS}}.$$
  When you take the ratio, the $\tfrac{1}{2}$'s annihilate:
  $$\text{CMRR}_{s.e.} = g_m R_{SS}.$$
  **No $\tfrac{1}{2}$ in the CMRR formula.** Forgetting the cancellation gives a 6 dB underestimate. See [[cmrr]] line 43 for the canonical derivation.

- **Cascode boosts $R_{SS}$ by the intrinsic-gain factor $g_m r_o$.** Single-NMOS tail: $R_{SS} = r_o$. Cascoded NMOS tail: $R_{SS} \approx g_m r_o^2$ — the lower transistor's $r_o$ is "boosted" by the upper transistor's intrinsic gain. This buys ~40 dB of CMRR over the simple mirror at the same bias point.

- **CMRR is dimensionless and converted with $20 \log_{10}$, not $10 \log_{10}$.** It's a voltage-gain ratio, not a power ratio.

- **Differential-output CMRR is theoretically infinite when matched.** Mismatch $\Delta R_D / R_D$ is what brings it down to the finite value $\text{CMRR}_\text{diff} \approx 2 g_m R_{SS} \cdot R_D / \Delta R_D$. Don't compute single-ended CMRR for a differential-output spec.

## Jayden's personal log

- `2026-05-04` — *Plugged a spurious $\tfrac{1}{2}$ into the CMRR formula during EEE 335 final-prep drill (final is the next day, May 5).* Computed CMRR as $\tfrac{1}{2} g_m R_{SS}$ (wrong) instead of $g_m R_{SS}$ (correct). Source of the slip: pattern-matching from the single-ended diff-pair gain formula $A_{d,s.e.} = \tfrac{1}{2} g_m R_D$, where the $\tfrac{1}{2}$ is real. Pattern to remember: **the $\tfrac{1}{2}$ lives in each gain, but cancels in the ratio — CMRR has no $\tfrac{1}{2}$.** Numerical impact: 50 V/V (34 dB) instead of 100 V/V (40 dB) for the simple-mirror tail, and 5000 V/V (74 dB) instead of 10{,}000 V/V (80 dB) for the cascoded tail. Both numbers 6 dB low; relative cascode-vs-simple delta of 40 dB was correctly preserved.
