---
title: DFT Bin Interpretation (Which Bin = Which Frequency)
type: concept
course: [[eee-404]]
tags: [fft, interpretation, frequency]
sources: [[slides-fft-interpretation]]
created: 2026-04-21
updated: 2026-04-26
---

# DFT Bin Interpretation

## In one line
Bin $k$ of an $N$-point DFT corresponds to frequency **$f_k = k \cdot (f_s/N)$** for $k \leq N/2$, and to the **negative** frequency $(k - N)\cdot(f_s/N)$ for $k > N/2$.

## Example first
You sample a $256$ Hz sinusoid at $f_s = 8192$ Hz and take a 64-point DFT. Which bin is the tone?

- **Frequency resolution:** $\Delta f = f_s/N = 8192 / 64 = $ **$128$ Hz per bin**.
- $256$ Hz $/ 128$ Hz/bin $= $ **bin 2**. So $X[2]$ is nonzero.
- Real signal $\to$ conjugate symmetry $\to$ also non-zero at $X[N-2] = X[62]$ (the negative-frequency image).

Result: $X[2]$ and $X[62]$ are the only non-zero bins.

Another example (from a course question): $f_s = 8192$, $N = 128$. If $X[4]$ and $X[124]$ are non-zero, what's the frequency?
- $\Delta f = 8192 / 128 = 64$ Hz.
- $f = 4 \cdot 64 = $ **$256$ Hz**.

## The idea
The $k$-th DFT bin correlates $x[n]$ against a complex sinusoid rotating at digital frequency $\omega_k = 2\pi k/N$ rad/sample. In analog terms, that's an angular frequency of $\Omega_k = \omega_k \cdot f_s = 2\pi k\cdot f_s/N$ rad/s, or $f_k = k\cdot f_s/N$ Hz.

**Intuition:** bin $k$ asks *"does the signal contain exactly $k$ complete cycles in the $N$-sample window?"* — see [[frequency-resolution]] for the full derivation (both the cycles-per-window route and the DFT-algebra route).

Because of the DFT's periodicity and conjugate symmetry for real inputs:

| $k$ range | What it represents | Analog frequency |
|---|---|---|
| $k = 0$ | DC | $0$ |
| $1 \leq k \leq N/2 - 1$ | Positive frequencies | $k\cdot(f_s/N)$ |
| $k = N/2$ | Nyquist | $f_s/2$ |
| $N/2 + 1 \leq k \leq N - 1$ | Negative frequencies | $(k - N)\cdot(f_s/N)$ |

A real sinusoid $\cos(2\pi f\cdot t)$ shows up at **two** bins: $k = f/\Delta f$ AND $k = N - f/\Delta f$. Their magnitudes are equal because $X[N-k] = X^*[k]$. See [[conjugate-symmetry]].

## The "fftshift" view
If you want a symmetric spectrum centered at $0$ (negative freqs left, positive right), shift the second half of $X$ to the front:
- MATLAB: `fftshift(X)`
- What you plot: $[X[N/2+1], \ldots, X[N-1], X[0], X[1], \ldots, X[N/2]]$ against $f = [-f_s/2 + \Delta f, \ldots, 0, \ldots, f_s/2]$.

## Common mistakes
- Treating all $N$ bins as positive frequencies. Only half the array does.
- Confusing bin index $k$ with frequency in Hz. They're linked by $\Delta f = f_s/N$, but different numbers.
- Forgetting the conjugate pair. For a real input, every real-frequency tone produces **two** bins symmetric about $N/2$.

## Related
- [[frequency-resolution]]
- [[nyquist-frequency]]
- [[conjugate-symmetry]]
- [[dft]]

## Practice
- [[fft-fundamentals-set-01]] — multiple bin-to-freq and freq-to-bin problems
- See also worked example: [[frequency-bin-256hz]]
