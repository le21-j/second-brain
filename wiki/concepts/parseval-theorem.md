---
title: Parseval's Theorem (DFT)
type: concept
course:
  - "[[eee-404]]"
tags: [parseval, energy, dft, dsp, eee-404]
sources:
  - "[[summary-eee-404-m7-frequency-domain]]"
created: 2026-04-29
updated: 2026-05-06
---

# Parseval's Theorem (DFT)

## In one line
**Energy is conserved** between time and frequency domains: $\sum_n |x[n]|^2 = \frac{1}{N}\sum_k |X[k]|^2$.

## Example first

Take $x[n] = \{1, 2, -3, -4\}$ from Exam 2 Problem 4. Time-domain energy:
$$\sum_n |x[n]|^2 = 1^2 + 2^2 + 3^2 + 4^2 = 30$$

DFT was $X[k] = \{-4, 4-6j, 0, 4+6j\}$. Frequency-domain energy:
$$\frac{1}{N}\sum_k |X[k]|^2 = \frac{1}{4}\bigl(16 + (4^2 + 6^2) + 0 + (4^2 + 6^2)\bigr) = \frac{1}{4}(16 + 52 + 0 + 52) = \frac{120}{4} = 30 \checkmark$$

Equal — as Parseval guarantees.

## The idea

The DFT is a **unitary transform up to scaling** — it conserves total signal energy, just shuffles it between bins. The $1/N$ factor on the right comes from the IDFT scaling convention.

## Formal definition

For an $N$-point sequence $x[n]$ and its DFT $X[k]$:
$$\sum_{n=0}^{N-1} |x[n]|^2 = \frac{1}{N}\sum_{k=0}^{N-1} |X[k]|^2$$

Equivalently, $\langle x_1, x_2 \rangle = \tfrac{1}{N} \langle X_1, X_2 \rangle$ for any two sequences (the polarisation identity gives Parseval for $x_1 = x_2$).

For the **DTFT**:
$$\sum_n |x[n]|^2 = \frac{1}{2\pi}\int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega$$

## Why it matters / when you use it

- **Justifies "largest L" peak-picking** in the EC quantum-computing lab — keeping the largest-magnitude bins maximises retained energy → maximises reconstruction SNR.
- **Energy-based comparisons** (SNR, signal power, noise power) are often easier in the frequency domain.
- **Sanity-check your DFT computation** by checking $\sum |x[n]|^2 = \frac{1}{N}\sum |X[k]|^2$. If they don't match, you have a bug.

## Common mistakes

- **Missing the $1/N$ factor.** The frequency-side sum has the $1/N$ scaling; the time-side does not.
- **Using $|X[k]|$ instead of $|X[k]|^2$.** Parseval is about energy ($|\cdot|^2$), not magnitudes.
- **Confusing DFT-Parseval with DTFT-Parseval.** Same idea, different scaling factors.

## Related

- [[dft]], [[idft]] — the transforms themselves
- [[dft-properties]] — Parseval is one of the named properties
- [[eee-404-ec-quantum-walkthrough]] — Parseval's role in justifying largest-L peak-picking

## Practice
- Sanity-check Exam 2 Problem 4(a) DFT against time-domain energy
