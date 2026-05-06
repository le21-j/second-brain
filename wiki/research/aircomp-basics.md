---
title: AirComp — System Model and MSE
type: concept
course:
  - "[[research]]"
tags: [aircomp, system-model, mse, denoising]
sources:
  - "[[paper-unregrettable-hpsr]]"
  - "[[paper-aircomp-survey]]"
created: 2026-04-21
updated: 2026-05-06
---

# AirComp — System Model and MSE

## In one line
Over-the-Air Computation exploits the natural superposition property of the wireless multiple-access channel to compute a function (usually arithmetic mean) of many devices' data simultaneously, on the same time-frequency resources.

## Example first
10 temperature sensors each want the ES to learn the **average** temperature. Instead of each sending its reading on a dedicated slot (10$\times$ bandwidth), they all transmit $\sqrt{P_n} \cdot s_n$ simultaneously; the channel naturally sums them. The ES divides by 10 to recover the mean. **Total airtime: 1 slot instead of 10.**

## The canonical model (from [[paper-unregrettable-hpsr]] Eq 2-4)

Received signal at ES:

$$y = \sum_n |h_n| \cdot \sqrt{P_n} \cdot s_n + W$$

- $s_n$ — normalized data symbol at ED $n$, $\mathbb{E}[s_n]=0$, $\mathbb{E}[s_n^2]=1$.
- $|h_n|$ — channel gain magnitude between ED $n$ and ES.
- $P_n$ — transmit power at ED $n$.
- $W \sim \mathcal{N}(0, \sigma^2)$ — AWGN.

Recovered target function (arithmetic mean):

$$\hat{f} = y / (N \cdot \sqrt{\eta})$$

where $\eta$ is a fixed denoising scaling factor chosen based on receiver hardware.

MSE between estimate and true mean $f = (1/N)\sum s_n$:

$$\text{MSE}(P, \eta) = \frac{1}{N^2} \cdot \sum_n \left(\frac{|h_n| \cdot \sqrt{P_n}}{\sqrt{\eta}} - 1\right)^2 + \frac{\sigma^2}{N^2 \cdot \eta}$$

## Why it matters
The $(|h_n|\sqrt{P_n}/\sqrt{\eta} - 1)^2$ term is the **magnitude-alignment error** for each ED. If every ED perfectly sets $P_n = \eta/|h_n|^2$, all coefficients equal 1 and the sum superimposes coherently — this is "truncated channel inversion" (TCI). But TCI requires accurate CSI at each ED and fails when $|h_n|$ is small (power blows up).

[[regretful-learning]] avoids TCI by letting each ED pick $P_n$ from a discrete set via a game-theoretic utility, converging to a Correlated Equilibrium instead.

## Common mistakes
- **Confusing $|h_n|$ with $h_n$** — the regret learning utility only uses the **magnitude**, not the complex phase. This simplifies the channel estimation (only need the modulus) but implicitly requires phase coherence at the ES, or a non-coherent detection scheme.
- **Forgetting noise scales with $1/\eta$** — larger $\eta$ suppresses noise but requires higher transmit power. Trade-off in the denoising factor.
- **Assuming superposition = sum** — only true if transmissions are time- and phase-aligned. See [[paper-aircomp-feel-demo]] for the sync machinery required.

## Related
- [[regretful-learning]] — how to choose $P_n$ without global CSI
- [[channel-estimation]] — how each ED learns its own $|h_n|$
- [[paper-aircomp-survey]] — broader context
- [[system-pipeline]] — the end-to-end design
