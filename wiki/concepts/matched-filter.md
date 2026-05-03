---
title: Matched filter
type: concept
course:
  - "[[python-ml-wireless]]"
  - "[[eee-404]]"
tags:
  - matched-filter
  - detection
  - dsp
  - foundations
  - wireless
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-05-01
updated: 2026-05-01
---

# Matched filter

## In one line
**The optimal linear filter for detecting a known waveform in additive white Gaussian noise.** Take the received signal, **correlate** it with a time-reversed conjugate of the known waveform $s(t)$, and the SNR at the sample point is **maximized**. Backbone of pulse-shaped digital communications, frame synchronization, radar detection.

## Example first

Transmit BPSK $b \in \{+1, -1\}$ shaped by a rectangular pulse $p(t) = 1$ for $0 \leq t < T$. Received signal:
$$r(t) = b\, p(t) + n(t), \quad n \sim \mathcal{N}(0, N_0/2).$$

Matched filter: correlate with $p(t)$ over the symbol period:
$$y = \int_0^T r(t)\, p(t)\, dt = b\, T + \int_0^T n(t)\, dt.$$

Output SNR:
$$\text{SNR}_{\text{out}} = \frac{(bT)^2}{T \cdot N_0/2} = \frac{2T b^2}{N_0} = \frac{2 E_s}{N_0}.$$

This is **provably the maximum** SNR achievable by any linear filter on $r(t)$. The detector then thresholds: $\hat b = \text{sign}(y)$, achieving $\text{BER} = Q(\sqrt{2 E_b / N_0})$.

In Python (digital matched filter):
```python
import numpy as np
samples_per_symbol = 8
pulse = np.ones(samples_per_symbol)              # rect pulse shape
b = 2*np.random.randint(0, 2, 1000) - 1          # ±1 BPSK
upsampled = np.zeros(1000 * samples_per_symbol); upsampled[::samples_per_symbol] = b
tx = np.convolve(upsampled, pulse, mode='full')  # pulse-shaped TX
rx = tx + 0.5*np.random.randn(len(tx))
matched = np.convolve(rx, pulse[::-1].conj(), mode='full')  # MF
samples = matched[samples_per_symbol-1::samples_per_symbol] # one sample per symbol
b_hat = np.sign(samples[:1000])
```

## The idea

Goal: detect a known signal $s(t)$ in additive white noise $n(t)$ with PSD $N_0/2$. Linear filter $h(t)$, output $y(t) = (s + n) * h$. **Maximize SNR at sampling instant $t_0$**:

$$\text{SNR}(t_0) = \frac{|(s * h)(t_0)|^2}{N_0/2 \cdot \int |h(t)|^2 dt}.$$

By Cauchy-Schwarz, this is maximized when $h(t) = c \cdot s^*(t_0 - t)$ — the **time-reversed, conjugated copy** of $s$. That's the matched filter.

### Equivalently: correlation
$y(t_0) = \int r(\tau) s^*(\tau - (t_0 - T)) d\tau$ — a **correlator** with the known waveform. Matched filtering and correlation are the same operation, expressed in two ways.

### Pulse shaping in digital comms
Modern digital systems use pulse shapes with controlled bandwidth (e.g., **root-raised-cosine**, RRC). The transmit filter $p_T(t) = $ RRC; the receive filter $p_R(t) = p_T^*(-t) = $ matched-RRC. Concatenated, $p_T * p_R = $ raised-cosine pulse with **zero ISI** at sampling instants — this is the Nyquist criterion.

## Formal definition

Maximum-SNR linear filter for known signal $s(t)$ in white noise of PSD $N_0/2$:
$$h_{\text{MF}}(t) = K \cdot s^*(T - t), \quad t \in [0, T]$$
where $K$ is an arbitrary constant. The filter output sampled at $t = T$ gives output SNR
$$\text{SNR}_{\text{MF}} = \frac{2 E_s}{N_0}, \quad E_s = \int_0^T |s(t)|^2 dt.$$

For complex signals, replace conjugate-time-reversal: $h(t) = s^*(T - t)$.

## Why it matters

- **Pulse-shaped digital communications.** Every digital modem implements a matched filter (RRC) at the receiver.
- **Frame synchronization.** Detect a known preamble (Gold sequence, ZC, Golay) — correlation peaks at the frame boundary. Used in 5G NR PSS/SSS, OTA-FL preambles ([[paper-experimental-ota-fl]]).
- **Channel estimation.** Pilot-based estimation correlates received pilots with known transmitted pilots — matched-filtering in disguise.
- **Radar.** Matched filter is the optimal range estimator.

## Common mistakes

- **Confusing matched filter with whitening filter.** Matched filter assumes **white** noise. For **colored** noise, prepend a whitening filter, then matched.
- **Incorrect time alignment.** Matched filter peaks at $t = T$ (the end of the pulse). Sampling earlier or later loses SNR fast.
- **Forgetting the conjugate.** For complex signals (QAM, OFDM), the matched filter is $s^*(T - t)$, not $s(T - t)$.
- **Pulse-shape mismatch.** TX uses RRC with roll-off 0.25; RX must use matching RRC with same roll-off. Mismatch causes ISI.

## Related
- [[qam-modulation]] — needs pulse-shaping; RX uses matched filter.
- [[ofdm]] — implicit matched filtering via FFT.
- [[neural-receiver]] — modern alternative; learns matched-filtering implicitly.
- [[fading-channels]] — matched filter optimal in AWGN; in fading, use **maximum-ratio combining** (per-tap matched filter).
- [[python-ml-wireless]] — Phase 1, [[textbook-pysdr-lichtman]] Ch 8 (Pulse Shaping).

## Practice
- Implement RRC pulse shaping with roll-off 0.25, simulate BPSK over AWGN, recover with matched filter — verify BER matches Q-function.
- Implement frame sync with Gold-sequence preamble; observe correlation peak.
- For a 3-tap multipath channel, compare matched-filter detection with maximum-ratio combining.
