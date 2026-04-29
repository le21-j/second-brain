---
title: Example — Lab 7 FILL_IN_BLANKs Walkthrough
type: example
course:
  - - eee-404
tags:
  - lab
  - fft
  - implementation
  - fixed-point
  - eee-404
sources:
  - - lab-7-fft
created: 2026-04-21
updated: 2026-04-26
---

# Lab 7 FILL_IN_BLANKs Walkthrough

Ties every blank in `main.c`'s `fft()` and `fft_fixed_point()` back to the concept it implements. Work through the example **before** looking at each snippet — try to write it yourself first, then compare.

## The three-loop structure

```c
for (L = 1; L <= num_stages; L++) {           // stage loop
    num_pt_sub_DFT  = 1 << L;                 // D in lecture
    num_butterflies = num_pt_sub_DFT >> 1;    // B in lecture
    U.re = 1.0;  U.im = 0.0;                  // reset twiddle
    for (j = 0; j < num_butterflies; j++) {   // butterfly index j
        for (i = j; i < num_pt_FFT; i += num_pt_sub_DFT) { // pair index i
            k = i + num_butterflies;          // bottom index
            // butterfly math here
        }
        // twiddle update here
    }
}
```

See [[butterfly]] for the conceptual meaning of each loop.

## Blank 1 — outer stage bound
```c
for (L = 1; L <= num_stages; L++)
```
`num_stages` $= \log_2 N$. For `SIZE_FFT = 4`, `num_stages = 2`; for $128$, `num_stages = 7`.

## Blank 2 — inner j loop bound
```c
for (j = 0; j < num_butterflies; j++)
```
`num_butterflies = num_pt_sub_DFT >> 1` $= D/2$. Number of butterflies in one sub-DFT at this stage.

## Blank 3 — i-loop stride
```c
for (i = j; i < num_pt_FFT; i += num_pt_sub_DFT)
```
Strides by $D$ (size of current sub-DFT), visiting corresponding butterflies across all sub-DFTs at this stage.

## Blank 4 — bottom index
```c
butterfly_bottom_index = butterfly_top_index + num_butterflies;
```
Pair `i` with `i + B` — offset to lower point is $B = $ `num_butterflies`. (This is the "$+ N/2$" in the butterfly equations, but at the sub-DFT level.)

## Blank 5 — the butterfly math (the core)

Read top first, then compute:
```c
// temp = U * X[k] (complex multiply)
temp.re = U.re * X[butterfly_bottom_index].re - U.im * X[butterfly_bottom_index].im;
temp.im = U.re * X[butterfly_bottom_index].im + U.im * X[butterfly_bottom_index].re;

// P = X[i] + temp    (top output, scaled)
P.re = (X[butterfly_top_index].re + temp.re) * scale;
P.im = (X[butterfly_top_index].im + temp.im) * scale;

// Q = X[i] - temp    (bottom output, scaled)
Q.re = (X[butterfly_top_index].re - temp.re) * scale;
Q.im = (X[butterfly_top_index].im - temp.im) * scale;

// Write back (in-place)
X[butterfly_top_index].re    = P.re;
X[butterfly_top_index].im    = P.im;
X[butterfly_bottom_index].re = Q.re;
X[butterfly_bottom_index].im = Q.im;
```

Key ordering: compute **P and Q before writing** either back — otherwise Q reads a corrupted X[i]. See [[butterfly]].

## Blank 6 — twiddle update
```c
temp1.re = U.re * W[L-1].re - U.im * W[L-1].im;
U.im     = U.re * W[L-1].im + U.im * W[L-1].re;   // uses OLD U.re
U.re     = temp1.re;                              // now overwrite
```
You need `temp1` because `U.im`'s update reads `U.re`. If you computed `U.re` first, `U.im` would use the already-updated value.

## Fixed-point version

Same structure, but every complex multiply is followed by `>> shift_factor` to renormalize Q15. See [[fixed-point-arithmetic]].

```c
temp.re = (U.re * X[k].re - U.im * X[k].im) >> shift_factor;
temp.im = (U.re * X[k].im + U.im * X[k].re) >> shift_factor;
P.re = (X[i].re + temp.re);        // no scale if scale_or_not  0
P.im = (X[i].im + temp.im);
// if scale_or_not  1: shift P, Q right by 1 instead of * 0.5
Q.re = (X[i].re - temp.re);
Q.im = (X[i].im - temp.im);
// write-back same as float
```

Twiddle update in fixed-point:
```c
temp1.re = (U.re * W[L-1].re - U.im * W[L-1].im) >> shift_factor;
U.im     = (U.re * W[L-1].im + U.im * W[L-1].re) >> shift_factor;
U.re     = temp1.re;
```

## Sanity-check: 4-pt vector `{0.6, 0.3, -0.1, 0.3}`, no scaling, `shift_factor = 15`

Hand compute with forward DFT:
- $X[0] = 0.6 + 0.3 - 0.1 + 0.3 = $ **$1.1$**
- $X[1] = 0.6 + 0.3\cdot(-j) + (-0.1)\cdot(-1) + 0.3\cdot(j) = 0.7 + (-0.3j + 0.3j) = $ **$0.7$**
- $X[2] = 0.6 - 0.3 - 0.1 - 0.3 = $ **$-0.1$**
- $X[3] = 0.6 + 0.3\cdot(j) + (-0.1)\cdot(-1) + 0.3\cdot(-j) = 0.7 + 0 = $ **$0.7$**

Your code should match these (floating point), and fixed-point (Q15) should be close within rounding.

## Sanity-check: 128-pt sinusoid
`sine_table.h` holds $x[n] = \sin(2\pi\cdot 256\cdot n/8192)$ for $n = 0, \ldots, 127$. So $f = 256$ Hz, $f_s = 8192$ Hz, $N = 128$. Expected non-zero bins: **$X[4]$** and **$X[124]$** ($\Delta f = 64$, $k = 256/64 = 4$). See [[frequency-bin-256hz]].

## What to say in the write-up for Task 4
- "What is the frequency of the sinusoid?" $\to$ **$256$ Hz**. Show: $\Delta f = 8192/128 = 64$, non-zero at $k=4 \to f = 4\cdot 64 = 256$ Hz.
- "Do you get correct FFT result with scaling off?" $\to$ **No**, because the 128-pt FFT has 7 stages and the intermediate sums exceed Q15 range $\to$ overflow wraps values and spectrum is garbage.
- "Why is scaling used?" $\to$ To prevent that overflow: each stage halves the magnitude so sums stay in range, and multiplying by $N$ at the end restores the correct magnitude.

## Related
- [[lab-7-fft]] — the lab assignment
- [[butterfly]], [[twiddle-factor]], [[bit-reversed-order]]
- [[fft-scaling]], [[fixed-point-arithmetic]]
- [[dft-bin-interpretation]]
