---
title: QAM modulation
type: concept
course:
  - "[[python-ml-wireless]]"
  - "[[eee-304]]"
tags:
  - modulation
  - qam
  - constellation
  - foundations
  - wireless
sources:
  - "[[textbook-prince-understanding-deep-learning]]"
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-05-01
updated: 2026-05-01
---

# QAM modulation (Quadrature Amplitude Modulation)

## In one line
Pack $\log_2 M$ bits per symbol by jointly modulating two quadrature carriers (in-phase and quadrature, $\cos$ and $\sin$). 16-QAM = 4 bits/symbol; 64-QAM = 6 bits/symbol; 256-QAM = 8 bits/symbol. The dominant data-channel modulation in 5G NR (alongside QPSK / $\pi/2$-BPSK for control).

## Example first

**16-QAM constellation.** 4 bits → 1 of 16 complex symbols arranged on a $4\times 4$ grid:
$$s = (I + jQ), \quad I, Q \in \{-3, -1, +1, +3\}.$$

The bit-to-symbol mapping uses **Gray code** so adjacent constellation points differ in exactly one bit — minimizes BER under noise.

```
   Q
 +3 ┌────┬────┬────┬────┐
    │1011│1010│0010│0011│
 +1 ├────┼────┼────┼────┤
    │1001│1000│0000│0001│
 -1 ├────┼────┼────┼────┤
    │1101│1100│0100│0101│
 -3 ├────┼────┼────┼────┤
    │1111│1110│0110│0111│
    └────┴────┴────┴────┘
   -3   -1   +1   +3   I
```

The transmitted signal is
$$s(t) = I\,\cos(2\pi f_c t) - Q\,\sin(2\pi f_c t)$$
which can be written compactly as $s(t) = \Re\{S\, e^{j 2\pi f_c t}\}$ with $S = I + jQ$.

In Python:
```python
import numpy as np
bits = np.random.randint(0, 2, size=(1000, 4))
gray = ...   # bits → constellation index via Gray code
constellation = np.array([(2*x-3) + 1j*(2*y-3) for x in range(4) for y in range(4)])
symbols = constellation[gray]
```

## The idea

Pre-QAM, BPSK transmits 1 bit/symbol ($\pm 1$ on the I axis). QPSK transmits 2 bits/symbol (4 corners). QAM generalizes: pack a square grid of $M = 2^k$ points in 2D space.

Each symbol uses **bandwidth $\sim 1/T_s$** Hz where $T_s$ is the symbol duration. Sending more bits per symbol packs more information into the same bandwidth — at the cost of needing higher SNR to distinguish closely-spaced points.

### Spectral efficiency vs. SNR
| Modulation | bits/symbol | Required $E_b/N_0$ for $10^{-5}$ BER |
|---|---|---|
| BPSK | 1 | 9.6 dB |
| QPSK | 2 | 9.6 dB (same — simply rotated) |
| 16-QAM | 4 | 13.4 dB |
| 64-QAM | 6 | 17.6 dB |
| 256-QAM | 8 | 23.8 dB |

The trade-off: each $4\times$ in $M$ costs ~$6$ dB. Modern adaptive systems (5G NR) pick $M$ based on measured SNR (link adaptation).

### In 5G NR
- **Data channels (PUSCH, PDSCH):** QPSK / 16-QAM / 64-QAM / 256-QAM / 1024-QAM (mode-dependent).
- **Control channels:** $\pi/2$-BPSK or QPSK.
- **Reference signals (DMRS, CSI-RS):** QPSK-like.

## Formal definition

For $M = 2^k$-QAM with $k$ even, square constellation:
$$S \in \{(2i - \sqrt{M} + 1) + j(2q - \sqrt{M} + 1) : i, q \in \{0, 1, \dots, \sqrt{M}-1\}\}.$$

Average symbol energy:
$$E_s = \mathbb{E}[|S|^2] = \frac{2(M-1)}{3}d^2$$
where $d$ = minimum distance between adjacent points (typically $d = 2$ for the "integer-grid" form above).

## Why it matters

- **The modulation scheme.** Every wireless modem implements QAM mapping/demapping.
- **The training signal in autoencoder-PHY.** The autoencoder of [[paper-oshea-hoydis-2017-autoencoder]] **learns** a constellation that often resembles QAM but isn't exactly QAM — bidirectional connection between QAM and learned PHY.
- **Constellation diagrams** are the classic visualization of channel impairment effects (rotation = phase error, smearing = SNR, distortion = nonlinearity).

## Common mistakes

- **Forgetting the scaling.** Different references normalize the constellation differently (unit-energy, integer-grid, peak-1). Always state which.
- **Ignoring bit-to-symbol mapping.** Naive binary mapping is much worse than Gray code at low SNR.
- **Confusing $E_b/N_0$ vs $E_s/N_0$.** They differ by $10\log_{10} k$ where $k = \log_2 M$. Plots should be explicit.
- **Mistaking QAM for an analog modulation.** QAM is digital; the analog precursor is amplitude modulation ([[amplitude-modulation]]).

## Related
- [[ofdm]] — multiplexes many QAM-modulated subcarriers in frequency.
- [[autoencoder-phy]] — the constellation can be **learned** instead of hand-designed.
- [[neural-receiver]] — recovers QAM symbols from received resource grid.
- [[ber-bler]] — the metric used to characterize QAM performance.
- [[modulation-classification]] — neural classifiers identify which QAM order is being used.
- [[python-ml-wireless]] — Phase 1, [[textbook-pysdr-lichtman]] Ch 4.

## Practice
- Plot 16-QAM constellation with Gray-code bit mapping; verify minimum-distance of adjacent points.
- Simulate $10^4$ symbols through AWGN at SNR = 10 dB; plot received constellation; compute BER.
- Reproduce the BER-vs-$E_b/N_0$ curves for BPSK / 16-QAM / 64-QAM via Q-function.
