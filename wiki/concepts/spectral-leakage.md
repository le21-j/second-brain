---
title: Spectral Leakage
type: concept
course: [[eee-404]]
tags: [fft, leakage, window]
sources: [[slides-window-functions]]
created: 2026-04-21
updated: 2026-04-26
---

# Spectral Leakage

## In one line
Energy from a tone that isn't exactly at a DFT bin "leaks" into neighboring bins — and if the window has tall side lobes, it leaks even further.

## Example first
$f_s = 8192$ Hz, $N = 64$, so bins sit at multiples of $\Delta f = 128$ Hz: $[0, 128, 256, 384, \ldots]$.

- A pure $256$ Hz tone lands **exactly** on bin $2$ — clean spectrum, single spike.
- A pure $200$ Hz tone lands **between** bins $1$ ($128$ Hz) and $2$ ($256$ Hz). Energy appears in bins $1$ and $2$ (big), and smaller amounts spill into bins $0, 3, 4, 5, \ldots$ — that's the leak.

Now take a second tone at $192$ Hz that's weak. If the stronger $200$ Hz tone's side lobes (from a rectangular window) are higher than the $192$ Hz tone's main peak, the weaker tone is **hidden under the leakage** of the stronger one.

## The idea
The DFT assumes your $N$-sample signal is **one period of an infinitely repeating signal**. If the actual frequency doesn't divide evenly into the window length, the edges don't match, the "periodic extension" has jumps, and the jumps produce broadband garbage in the spectrum.

Multiplying in time $= $ convolving in frequency. A rectangular window is sinc-like in frequency (tall side lobes decaying as $1/k$). Convolving your true spectrum with that sinc smears each true tone into a sinc pattern — that's the leakage.

Smoother windows (Hann, Hamming) have smaller side lobes $\to$ less leakage, at the cost of a wider main lobe (worse resolution for very close tones).

## Three ways to reduce leakage

1. **Use a better window** — Hann, Hamming, Blackman — smaller side lobes. Most common fix. See [[window-function]].
2. **Use a longer FFT (bigger $N$)** — narrower bins, so fewer tones fall between bins. Diminishing returns; doesn't fix *everything*.
3. **Coherent sampling** — arrange so the tone frequency *is* an exact bin. Rarely possible for real signals.

## Quantitative example
Rectangular window of length $L = 64$: the first side lobe is only $\approx 13$ dB below the main lobe. Hamming: $\approx 43$ dB. Hann: $\approx 32$ dB (but with faster decay afterward).

## Common mistakes
- Thinking leakage is bug-like. It's a **mathematical consequence** of finite-window DFT — unavoidable, only manageable.
- Using rectangular window for anything sensitive. Default to Hann unless you've thought about why.
- Confusing leakage (spectrum spreading) with aliasing (frequency folding from bad sampling). They're different problems.

## Related
- [[window-function]]
- [[stft]]
- [[frequency-resolution]]
