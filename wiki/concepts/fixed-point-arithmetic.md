---
title: Fixed-Point Arithmetic (Q15)
type: concept
course: [[eee-404]]
tags: [fixed-point, embedded, dsp]
sources: [[lab-7-fft]]
created: 2026-04-21
updated: 2026-04-26
---

# Fixed-Point Arithmetic (Q15)

## In one line
Represent fractional numbers as scaled integers: a value $v$ is stored as `int32_t(v * 2^15)` — a "Q15" fixed-point number with 15 fractional bits.

## Example first
Store $0.5$ in Q15: `0.5 * 32768 = 16384` $\to$ stored as `int32_t 16384`.
Store $-0.25$: `-0.25 * 32768 = -8192` $\to$ stored as `-8192`.
Store $1.0$: `1.0 * 32768 = 32768` $\to$ stored as `32768`. (Technically this is the limit of Q15 since $2^{15} = 32768$.)

**Multiply $0.5 \times 0.25$:**
- Q15: `16384 * -8192 = -134217728` $\to$ this is in "Q30" (product of two Q15s).
- Right-shift by 15 to renormalize: `-134217728 >> 15 = -4096`.
- `-4096 / 32768 = -0.125` $\checkmark$

So multiplication in Q15 is `(a * b) >> 15`. That's the `>>shift_factor` you see in Lab 7 code.

## The idea
Microcontrollers like the STM32F407 can multiply integers much faster than floating-point. Fixed-point gives you "fake fractions" using integers: pick a scale factor $2^S$, store $v$ as `int(v * 2^S)`, and keep track of the scale through arithmetic.

- **Add/subtract:** just add the integers. Scale doesn't change.
- **Multiply:** multiply the integers, then divide by $2^S$ (shift right) to restore scale.
- **Shift right by $S$ after every multiply.** Miss it and your numbers blow up.

For Q15 with 32-bit storage:
- Range: approximately $[-1, 1)$.
- Product (Q15 $\times$ Q15) fits in Q30, which fits in 32 bits.
- After `>> 15`, result is back in Q15, still in 32-bit.

## In Lab 7

Look at how the code handles the twiddle factor multiply:

```c
// float version
temp1.re = U.re * W[L-1].re - U.im * W[L-1].im;

// fixed-point version
temp1.re = (U.re * W[L-1].re - U.im * W[L-1].im) >> shift_factor;
```

Every complex multiply in the fixed-point FFT adds a `>> shift_factor` to undo the Q30 $\to$ Q15 scale growth.

## Why scale by `shift_factor = 15`?
- Q15 lets you represent numbers in roughly $[-1, 1)$. Input FFT samples are in that range for normalized signals.
- Q15 $\times$ Q15 $\to$ Q30 (fits in 32 bits with room for a few additions without overflow).
- Standard DSP practice. ARM's CMSIS-DSP library uses Q15 extensively.

## Overflow still possible
Fixed-point scaling keeps *single* multiplies safe. But FFT butterflies **add** values (`X[i] + temp`), and sums can grow. That's why [[fft-scaling]] is still needed *in addition* to Q15 conventions — the two do different jobs.

## Common mistakes
- Forgetting `>> shift_factor` after a multiply $\to$ huge overflow.
- Shifting **before** the sum: `(A >> 15) + (B >> 15)` loses precision vs. `((A + B) >> 15)` when $A, B$ are already small.
- Using floating-point `pow(2, shift_factor)` in a hot loop — the lab uses it once in setup, fine. Don't do it per-sample.

## Related
- [[fft-scaling]] — the other overflow defense
- [[butterfly]]
- [[lab-7-fft]]
