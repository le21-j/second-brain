---
title: Twiddle Factor
type: concept
course:
  - "[[eee-404]]"
tags: [fft, complex-numbers]
sources:
  - "[[slides-fft-core-equations]]"
  - "[[slides-fft-implementation]]"
created: 2026-04-21
updated: 2026-05-06
---

# Twiddle Factor

## In one line
$W_N = e^{-j2\pi/N}$: a complex number on the unit circle. All the "phase" multipliers in the DFT/FFT are just powers of this one number.

## Example first
For $N = 4$:
- $W_4^0 = e^0 = $ **1**
- $W_4^1 = e^{-j\pi/2} = $ **$-j$**
- $W_4^2 = e^{-j\pi} = $ **$-1$**
- $W_4^3 = e^{-j3\pi/2} = $ **$j$**

Notice the pattern: $W_4^k$ just rotates $90°$ clockwise on the unit circle per $k$. For $N = 8$, it rotates $45°$. In general $W_N$ spins $2\pi/N$ clockwise per step.

## The idea
The DFT sums $x[n]$ weighted by complex phases $e^{-j2\pi kn/N}$. Writing $W_N = e^{-j2\pi/N}$ lets you compactly denote those phases as $W_N^{kn}$. The FFT exploits three crucial identities:

- **Periodicity:** $W_N^{k+N} = W_N^k$ (comes back after $N$ steps).
- **Half-circle:** $W_N^{k + N/2} = -W_N^k$ (opposite side of the unit circle).
- **Square:** $(W_N)^2 = W_{N/2}$ (squaring doubles the step size).

That last one is the magic: it's what lets you turn an $N$-point DFT into two $N/2$-point DFTs.

## Formal definition

$$W_N = e^{-j\tfrac{2\pi}{N}}, \qquad W_N^k = \cos\tfrac{2\pi k}{N} - j\sin\tfrac{2\pi k}{N}$$

## In the FFT code
You precompute only **$\log_2 N$** twiddles and derive the rest as you go:
```c
for (L = 1; L <= log2N; L++) {
    B = 1 << (L-1);                           // butterflies in this stage's sub-DFT
    W[L-1].re =  cos(pi / B);
    W[L-1].im = -sin(pi / B);
}
```
Inside the butterfly loop, you maintain a running `U` and update `U = U * W[L-1]` after each butterfly index $j$. This sweeps $U$ through $W_N^0, W_N^{N/D}, W_N^{2N/D}, \ldots$ so it visits only the $k$-values actually needed.

## Common mistakes
- Sign of the imaginary part. DFT uses **$W_N = e^{-j2\pi/N}$** (negative). IDFT uses **$e^{+j2\pi/N}$**. Get the sign wrong and you'll end up with the inverse transform.
- Updating `U.re` before `U.im` (overwriting the value needed for the .im update). Always use a temp — see lab code `temp1.re`.

## Related
- [[fft]], [[butterfly]]
- [[complex-multiplication]]
- [[idft]] — uses the conjugate twiddle

## Practice
- [[fft-fundamentals-set-01]] (problems on $W_N$ values and periodicity)
