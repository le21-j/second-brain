---
title: Discrete-Time Fourier Transform (DTFT)
type: concept
course: [[eee-404]]
tags: [dtft, fourier, fundamentals]
sources: [[homework-2026-04-27-eee-404-hw5]]
created: 2026-04-27
updated: 2026-04-27
---

# Discrete-Time Fourier Transform (DTFT)

## In one line
The DTFT takes a discrete-time signal $x[n]$ and returns a **continuous, $2\pi$-periodic** function $X(e^{j\omega})$ of digital frequency $\omega$ (rad/sample) — the spectrum at every frequency, not just at sampled bins.

## Example first
For a single cosine $x[n] = \cos(\omega_0 n)$:
$$X(e^{j\omega}) = \pi\bigl[\delta(\omega - \omega_0) + \delta(\omega + \omega_0)\bigr], \qquad |\omega| \leq \pi$$

Two impulses, one at $+\omega_0$ and one at $-\omega_0$, each of height $\pi$. Outside $[-\pi, \pi]$ the pattern repeats with period $2\pi$.

For an amplitude-$A$ cosine $x[n] = A\cos(\omega_0 n + \phi)$ the impulse heights become $A\pi$ each — the constant phase $\phi$ shifts the impulses' phase but **not the magnitude**.

## Formal definition
$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]\,e^{-j\omega n}, \qquad \omega \in \mathbb{R}$$

The output is **continuous in $\omega$** and **$2\pi$-periodic** ($X(e^{j(\omega+2\pi)}) = X(e^{j\omega})$).

## DTFT vs DFT — the crucial distinction

| | **DTFT** | **DFT** |
|:---|:---|:---|
| Signal | Aperiodic, infinite-length $x[n]$ | Finite-length $x[n]$, $N$ samples |
| Output | Continuous function of $\omega$ | $N$ discrete samples $X[k]$ |
| Use | Theoretical analysis | Numerical computation |
| Relation | DFT = DTFT samples at $\omega_k = 2\pi k/N$ | — |

The DFT is "the DTFT, sampled at $N$ equally-spaced points around the unit circle." See [[dft]].

## Common DTFT pairs

| $x[n]$ | $X(e^{j\omega})$ on $|\omega| \leq \pi$ |
|:---|:---|
| $\delta[n]$ | $1$ |
| $1$ (constant) | $2\pi\,\delta(\omega)$ |
| $\cos(\omega_0 n)$ | $\pi[\delta(\omega - \omega_0) + \delta(\omega + \omega_0)]$ |
| $\sin(\omega_0 n)$ | $\frac{\pi}{j}[\delta(\omega - \omega_0) - \delta(\omega + \omega_0)]$ |
| $A\cos(\omega_0 n + \phi)$ | $A\pi[e^{j\phi}\delta(\omega - \omega_0) + e^{-j\phi}\delta(\omega + \omega_0)]$ |
| Rectangular $w[n]$, $0 \leq n \leq L-1$ | $e^{-j\omega(L-1)/2}\cdot\dfrac{\sin(\omega L/2)}{\sin(\omega/2)}$ |

## Why it matters / when you use it
- The DTFT is the natural "ground truth" spectrum of a discrete-time signal — what an infinite-length DFT would give.
- Windowing in time = **convolution** in DTFT. So a finite-window spectrum $S(e^{j\omega}) = X(e^{j\omega}) * W(e^{j\omega})$ — windowing smears each spectral impulse into a copy of the window's main lobe. See [[spectral-leakage]] and [[window-resolution-criterion]].
- For real signals, $|X(e^{j\omega})|$ is **even** in $\omega$ (conjugate symmetry).

## Common mistakes
- **Conflating DTFT with DFT.** The DTFT is continuous in $\omega$ and aperiodic in $n$; the DFT is discrete in $k$ and periodic. Different objects. The DFT *samples* the DTFT.
- **Forgetting $2\pi$-periodicity.** $X(e^{j\omega})$ at $\omega = \pi$ and at $\omega = \pi + 2\pi = 3\pi$ are the same value. Plots typically only show $|\omega| \leq \pi$.
- **Magnitude vs phase.** A phase shift in $x[n]$ multiplies the DTFT by $e^{j\phi}$ but leaves $|X(e^{j\omega})|$ unchanged.

## Related
- [[dft]] — discrete samples of the DTFT
- [[spectral-leakage]] — what happens when you window
- [[window-resolution-criterion]] — when two DTFT impulses can be told apart through a window
- [[hamming-window]], [[rectangular-window]] — window DTFTs
- [[conjugate-symmetry]] — why real signals have $|X|$ even in $\omega$

## Practice
- [[fft-fundamentals-set-01]]
- [[eee-404-hw5-walkthrough]] — HW5 problems 1(a) and 2(a) compute DTFTs of cosines
