---
title: Slides — FFT for Real-Valued Signal
type: summary
source_type: slides
source_path: raw/slides/eee-404/fft_real_valued_signal.pdf
course: [[eee-404]]
tags: [fft, real-valued, conjugate-symmetry, optimization]
created: 2026-04-21
updated: 2026-04-26
---

# Slides — FFT for Real-Valued Signal

## TL;DR
For a real $N$-point signal $x[n]$, you don't need a full $N$-point complex FFT. Pack even samples into the real part of $z[n]$ and odd samples into the imaginary part — now $z[n]$ is $N/2$-point complex. Run $N/2$-point FFT, extract $X_e$ and $X_o$ via conjugate-symmetry identities, combine with one butterfly stage to recover $X[k]$. Savings: roughly halves the multiply count.

## Key takeaways
- **Pack:** $z[n] = x_e[n] + j\cdot x_o[n]$, where $x_e[n] = x[2n], x_o[n] = x[2n+1]$.
- **FFT:** compute $Z[k] = (N/2)$-point FFT of $z[n]$.
- **Extract:**
  - $X_e[k] = (Z[k] + Z^*[(-k) \bmod (N/2)]) / 2$
  - $X_o[k] = (Z[k] - Z^*[(-k) \bmod (N/2)]) / (2j)$
- **Combine (last butterfly stage):**
  - $X[k]     = X_e[k] + W_N^k \cdot X_o[k]$,   $k = 0..N/2-1$
  - $X[k+N/2] = X_e[k] - W_N^k \cdot X_o[k]$
- **Complexity:** $(\log_2(N/2)\cdot N + 2N)$ real MULTs $\approx$ half of the direct $N$-point FFT's $2N\cdot\log_2 N$.
- **Conjugate symmetry of real signals:** $X[k] = X^*[N-k]$. Only need bins $0..N/2$.

## Concepts introduced or reinforced
- [[real-valued-fft]] — the packing trick
- [[conjugate-symmetry]] — $X[k] = X^*[N-k]$ for real $x$
- [[dft-computation-complexity]] — the comparison table

## Worked examples worth remembering
- $x[n] = [1, 2, 0, 0] \to X[k] = [3, 1-2j, -1, 1+2j]$ via complex 2-pt FFT. See [[real-valued-fft-4pt]].
- Exercise: $x[n] = [2, 1, -1, 3] \to X[k] = [5, 3+2j, -3, 3-2j]$. Covered in same example.
- Comparison for $N = 4$: direct DFT = 64 MULTs, 4-pt FFT = 16 MULTs, complex-2pt-based = 12 MULTs.

## Questions this source raised
- Practice question: $N = 64$, how many real MULTs using complex 32-pt FFT? Answer: $\log_2(32)\cdot 64 + 2\cdot 64 = 5\cdot 64 + 128 =$ **448**.
