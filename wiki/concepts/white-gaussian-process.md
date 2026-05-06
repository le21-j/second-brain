---
title: White Gaussian Process (WGN)
type: concept
course:
  - "[[eee-350]]"
tags: [white-noise, gaussian, stochastic-process]
sources:
  - "[[slides-47-stochastic-processes]]"
created: 2026-04-21
updated: 2026-05-06
---

# White Gaussian Process / White Gaussian Noise (WGN)

## In one line
A stochastic process where each $X[n]$ is Gaussian with the **same** distribution and **independent** across $n$. "White" = flat spectrum; "Gaussian" = Gaussian distribution; "independent" = what makes it white.

## Example — discrete time
$X[n] \sim N(0, \sigma^2)$, independent across $n$. Samples at different times are **independent Gaussians** with the same variance.

- MATLAB: `wgn(1000, 1, 0)` generates 1000 samples of WGN with 0 dBm power (here, variance 1 mW).

## Why "white"?
Autocorrelation $R_X(\tau) = \sigma^2 \cdot \delta[\tau]$. Its Fourier transform (= PSD) is $\sigma^2$ — **flat** across all frequencies. Analogy to white light: all frequencies equal.

## Stationary
WGN is **strictly stationary** — joint distribution is shift-invariant.

## Why it matters
- **Noise model** of choice for receivers (thermal noise, amplifier noise).
- **Building block:** filter WGN to get **colored noise** with any desired PSD. Any WSS Gaussian process = WGN filtered by some linear system.
- **Optimal detection/estimation** often assumes WGN — gives closed-form solutions.

## Continuous-time WGN (subtlety)
Continuous-time "white noise" has infinite power — isn't a proper random process in the usual sense. It's a **generalized process** (integrals of it make sense). The discrete-time version has no such issue.

## Related
- [[stationary-process]]
- [[colored-noise]]
- [[iid-samples]]
