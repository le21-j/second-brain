---
title: Antipodal Signaling (AWGN)
type: concept
course:
  - "[[eee-350]]"
tags: [communications, detection, awgn, bpsk]
sources:
  - "[[slides-43.5-bayesian-inference]]"
created: 2026-04-21
updated: 2026-05-06
---

# Antipodal Signaling (under AWGN)

## In one line
A binary communication model where transmitted symbol $\theta \in \{+1, -1\}$ is received as $X = \theta + N$ with $N \sim N(0, \sigma^2)$ — "additive white Gaussian noise". Simplest model for digital comms; used to illustrate [[map-detection|MAP detection]].

## Setup
- **Transmit:** $\theta \in \{+1, -1\}$ (antipodal = opposite values, equal magnitude).
- **Channel:** $X = \theta + N$, $N \sim N(0, \sigma^2)$.
- **Priors:** $P(\theta = +1) = \pi_0$, $P(\theta = -1) = \pi_1$ (often equal, sometimes not).

## MAP detector

Decide $\hat\theta = +1$ iff $p(X \mid +1)\cdot\pi_0 > p(X \mid -1)\cdot\pi_1$.

Taking log and simplifying (shown in [[map-detection]]):
$$X \;\overset{H_0}{\underset{H_1}{\gtrless}}\; \tau, \qquad \tau = \frac{\sigma^2}{2}\ln\frac{\pi_1}{\pi_0}$$

- **Equal priors ($\pi_0 = \pi_1 = 0.5$):** $\tau = 0$. Decide $+$ if $X > 0$.
- **$\pi_0 > \pi_1$:** $\tau < 0$. Threshold moves toward $-1$ — if $+1$ is more likely a priori, you declare $+$ even for slightly negative $X$.

## Bit error rate (BER)

Under equal priors with threshold 0:
$$P(\text{error}) = P(X < 0 | +1) = P(N < -1) = \Phi(-1/\sigma) = Q(1/\sigma)$$

where $Q(x) = 1 - \Phi(x)$. Depends only on **signal-to-noise ratio** $1/\sigma$.

Higher SNR (smaller $\sigma$) $\to$ smaller $Q$ $\to$ fewer bit errors. In dB: error probability drops roughly exponentially with SNR in dB.

## Why it matters
- **BPSK** (Binary Phase-Shift Keying) is exactly this model in practice.
- Introduces the decision-theoretic framework used in all of digital comms.
- Shows concretely how MAP works with and without symmetric priors.

## Related
- [[map-detection]]
- [[bayesian-inference]]
- [[standard-normal-table]]
