---
title: DFT Properties
type: concept
course:
  - "[[eee-404]]"
tags: [dft, properties, linearity, time-shift, parseval, convolution, dsp, eee-404]
sources:
  - "[[summary-eee-404-m7-frequency-domain]]"
created: 2026-04-29
updated: 2026-05-06
---

# DFT Properties

## In one line
A short list of identities that turn **DFT analysis problems** into bookkeeping (linearity, shifts, convolution, Parseval) — memorise them; they show up everywhere in Exam 2 and the FFT module.

## Example first

> **Q:** What's the DFT of $y[n] = x[n - 2]$ (circular shift by 2)?
> **A:** Apply the **time-shift property**: $Y[k] = X[k] e^{-j 2\pi (2) k / N} = X[k] W_N^{2k}$. No re-computation needed.

> **Q:** Energy in the time vs frequency domain?
> **A:** **Parseval:** $\sum_n |x[n]|^2 = \frac{1}{N}\sum_k |X[k]|^2$. The factor $1/N$ comes from the IDFT scaling.

## The idea

Every DFT property mirrors a continuous-Fourier property — but **circular** in the time index $n$ (because the DFT implicitly periodises $x[n]$ with period $N$).

## The DFT property table

| Property | Formula | Used for |
|---|---|---|
| **Linearity** | $\alpha x_1 + \beta x_2 \leftrightarrow \alpha X_1 + \beta X_2$ | Decompose signals into known pieces |
| **Time shift** (circular) | $x[(n - n_0)_N] \leftrightarrow X[k] e^{-j 2\pi k n_0 / N}$ | Compute DFT of shifted version |
| **Frequency shift** (modulation) | $x[n] e^{j 2\pi k_0 n / N} \leftrightarrow X[(k - k_0)_N]$ | Frequency-domain shifting |
| **Time reversal** | $x[(-n)_N] \leftrightarrow X[(-k)_N]$ | Symmetry tricks |
| **Conjugation** | $x^*[n] \leftrightarrow X^*[(-k)_N]$ | Real signals get conjugate-symmetric DFTs |
| **Conjugate symmetry (real $x$)** | $X[N - k] = X^*[k]$ | Halves storage for real-signal FFT |
| **Circular convolution** | $x_1 \circledast x_2 \leftrightarrow X_1[k] X_2[k]$ | Multiply-in-frequency = convolve-in-time |
| **Multiplication** | $x_1[n] x_2[n] \leftrightarrow \tfrac{1}{N} (X_1 \circledast X_2)[k]$ | Windowing produces convolution in $k$ |
| **Parseval** | $\sum_n |x[n]|^2 = \tfrac{1}{N}\sum_k |X[k]|^2$ | Energy conservation |

## Why it matters / when you use it

- **Exam 2 Problem 3** uses linearity (decomposing $\sin + \sin$), implicit windowing (rectangular window's DFT structure), and convolution.
- **Exam 2 Problem 4** uses conjugate symmetry as a sanity check on the 4-pt DFT.
- **The IFFT-via-FFT trick** is built on the conjugation property.
- **Real-valued FFT** halves the work using conjugate symmetry.

## Common mistakes

- **Linear vs. circular convolution.** DFT product = **circular** convolution, not linear. To get linear convolution from a DFT, **zero-pad** both signals to length $\geq N_1 + N_2 - 1$.
- **Forgetting the $1/N$ in Parseval.** The IDFT has $1/N$, so Parseval has it too on the frequency side.
- **Confusing circular shift with linear shift.** Circular shift wraps around: $x[N-1]$ slides to position 0. Linear shift truncates at the boundary.

## Related

- [[dft]], [[idft]] — the transforms themselves
- [[twiddle-factor]] — the $W_N^{kn}$ that appears in shifts
- [[parseval-theorem]] — energy conservation in detail
- [[real-valued-fft]] — uses conjugate symmetry
- [[eee-404-exam-2-walkthrough]] — multiple problems use these

## Practice
- Exam 2 Practice Problems 3 and 4
