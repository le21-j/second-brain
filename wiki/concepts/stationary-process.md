---
title: Stationary Process
type: concept
course: [[eee-350]]
tags: [stationary, stochastic-process]
sources: [[slides-47-stochastic-processes]]
created: 2026-04-21
updated: 2026-04-26
---

# Stationary Process

## In one line
A stochastic process is **stationary** if its statistics **don't depend on the absolute time** — only on relative times between observations.

## Example first
**White Gaussian noise** $X[n] \sim N(0, \sigma^2)$ i.i.d. is stationary: the distribution of $(X[100], X[101])$ is the same as $(X[1000], X[1001])$ — both pairs are i.i.d. Gaussian.

**Random walk** $S_n = S_{n-1} + X_n$ with i.i.d. increments is **not** stationary: $\text{Var}(S_n) = n\sigma^2$ grows with $n$.

## Two flavors

### Strict-sense stationary (SSS)
Joint distribution of $(X_{t_1}, \ldots, X_{t_k})$ = joint distribution of $(X_{t_1 + \tau}, \ldots, X_{t_k + \tau})$ for **any** shift $\tau$ and any $k$.

Strong condition — all finite-dim distributions time-invariant.

### Wide-sense stationary (WSS)
Weaker:
- $E[X_t]$ = constant (not depending on $t$).
- $\text{Cov}(X_t, X_s)$ depends only on $t - s$ (the lag).

WSS uses only 1st and 2nd moments. All SSS processes are WSS; converse holds for Gaussian processes (1st and 2nd moments fully determine Gaussians).

## Autocorrelation function
For WSS process: $R_X(\tau) = E[X_t \cdot X_{t+\tau}]$. Function of lag $\tau$ only.
- $R_X(0) = E[X^2]$ (power).
- $R_X$ is symmetric: $R_X(\tau) = R_X(-\tau)$.
- $|R_X(\tau)| \leq R_X(0)$.

Fourier transform of $R_X$ is the **power spectral density** (PSD) — beyond this course but key in DSP.

## Why it matters
- **Most tools work only for WSS processes.** Spectral analysis, filtering, linear estimation all assume stationarity.
- **Modeling real signals:** stationarity is an idealization. Real signals are often **locally** stationary (stationary over short windows). This is why STFT / windowing is used.

## Common non-stationary processes
- Random walks (mean or variance grows).
- Signals with trends.
- Signals with changing statistics over time (speech, ECG).

## Related
- [[stochastic-process]]
- [[white-gaussian-process]] — prototypical stationary
- [[colored-noise]]
