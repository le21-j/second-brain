---
title: FFT — Common Mistakes
type: mistake
course:
  - "[[eee-404]]"
tags: [mistakes, fft]
concept:
  - "[[fft]]"
created: 2026-04-21
updated: 2026-05-06
---

# FFT — Common Mistakes

## Known gotchas (general — from lecture + code review)

- **Sign of twiddle exponent.** DFT uses $W_N = e^{-j2\pi/N}$ (minus). IDFT uses $e^{+j2\pi/N}$ (plus). Flipping these accidentally gives you the inverse transform.
- **Divide by $N$.** Forgetting the $/N$ in the IDFT recipe is a classic. Magnitudes will be off by a factor of $N$.
- **Reading `X[i]` after writing it.** In a butterfly, compute **both** $P$ and $Q$ before writing either back to $X$. Otherwise $Q$ reads the modified (corrupted) `X[i]`.
- **Updating `U.re` before `U.im`.** The twiddle update $U_r\cdot W_r - U_i\cdot W_i$ and $U_r\cdot W_i + U_i\cdot W_r$ both read the **old** `U.re`. Use a `temp1` to save the new `U.re` until after `U.im` is updated.
- **Bit-reversing in decimal.** It's **binary** bit reversal. For $N = 4$ use 2 bits; for $N = 128$ use 7 bits.
- **Double-applying bit reversal.** Either reverse the input or reverse the output, not both. DIT convention: reverse input.
- **Confusing bin index with Hz.** Bin $k$ maps to $f = k\cdot(f_s/N)$. Two different numbers.
- **Plotting all $N$ bins of a real spectrum.** Only $N/2 + 1$ are independent; the second half is conjugate-mirror of the first.
- **Using rectangular window and complaining about leakage.** That's what rectangular *does*. Switch to Hann.
- **Forgetting the `>> shift_factor` after fixed-point multiplies.** Q15 $\times$ Q15 $= $ Q30; you must renormalize by right-shifting 15.
- **Running large FFTs in fixed-point without scaling.** $\log_2 N$ stages each potentially doubling the magnitude $\to$ overflow on anything past about $N = 8$ for Q15 inputs near full-scale.

## Jayden's personal log

_(Each time you miss a practice problem or catch a mistake in the lab, add a dated line here. Pattern-match-able entries are more valuable than "got confused" — write the specific thing you did wrong and the correct rule.)_

- _(no entries yet — this log fills in as you hit things)_
