---
title: Fading channels
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - fading
  - channel-model
  - rayleigh
  - rician
  - foundations
  - wireless
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-05-01
updated: 2026-05-01
---

# Fading channels

## In one line
**Wireless propagation isn't AWGN.** Multipath from buildings, walls, and vehicles creates a time-varying complex channel coefficient $h(t, \tau)$ with **Rayleigh** (no LoS) or **Rician** (LoS + multipath) statistics. Every realistic PHY simulator and dataset uses fading; "AWGN-only" results are PHY-ML papers' biggest sin.

## Example first

**Rayleigh flat-fading.** Single-tap channel: $h \sim \mathcal{CN}(0, 1)$ — complex circularly-symmetric Gaussian, unit variance. The amplitude $|h|$ is **Rayleigh-distributed** with PDF
$$f_{|h|}(r) = 2r\,e^{-r^2}, \quad r \geq 0.$$

Effect on BPSK: instead of fixed SNR $\gamma_0 = E_b/N_0$, the **instantaneous SNR** is $\gamma = |h|^2 \gamma_0$, exponentially distributed. Average BER:
$$\text{BER}_{\text{Rayleigh, BPSK}} = \frac{1}{2}\left(1 - \sqrt{\frac{\gamma_0}{1 + \gamma_0}}\right) \approx \frac{1}{4\gamma_0}.$$

Compare AWGN BPSK BER $\approx \frac{1}{2\sqrt{\pi}} e^{-\gamma_0}/\sqrt{\gamma_0}$ — exponential decay vs. **only $1/\gamma_0$ in Rayleigh**. The qualitative gap: Rayleigh occasionally has **deep fades** that destroy your link; AWGN never does.

```python
# Simulate Rayleigh flat-fading BPSK
import numpy as np
N = 100000; snr_db = 10
snr = 10**(snr_db/10)
b = 2*np.random.randint(0, 2, N) - 1  # ±1 BPSK
h = (np.random.randn(N) + 1j*np.random.randn(N)) / np.sqrt(2)  # CN(0,1)
n = (np.random.randn(N) + 1j*np.random.randn(N)) / np.sqrt(2*snr)
y = h*b + n
b_hat = np.sign(np.real(y * np.conj(h)))  # coherent demod
ber = np.mean(b_hat != b)
```

## The idea

A wireless signal arrives via **multiple propagation paths** — direct (LoS, sometimes), reflections off buildings, diffraction around corners, scattering off rough surfaces. Each path has its own delay $\tau_i$, phase $\phi_i$, and amplitude $\alpha_i$. The composite channel impulse response is
$$h(t, \tau) = \sum_i \alpha_i(t)\, e^{j\phi_i(t)}\, \delta(\tau - \tau_i(t)).$$

Two key dimensions:

### 1. Frequency selectivity (multipath delay spread)
- **Flat fading:** delay spread $\ll$ symbol duration → channel is one complex coefficient $h$. OK at low symbol rates.
- **Frequency-selective fading:** delay spread $\sim$ symbol duration → ISI; need equalizer or OFDM.

### 2. Time selectivity (Doppler spread)
- **Slow fading:** coherence time $\gg$ packet duration → channel is constant per packet.
- **Fast fading:** coherence time $\sim$ packet → channel changes within packet → channel tracking required.

### Common channel models
| Model | When to use |
|---|---|
| **AWGN** | toy / theoretical baseline only |
| **Rayleigh** | NLoS multipath, indoor / urban |
| **Rician** ($K$ factor) | mixed LoS + multipath |
| **Nakagami-$m$** | severe scattering, fits some empirical data |
| **TDL / CDL** (3GPP 38.901) | standardized 5G NR test channels |
| **UMi / UMa / RMa** (3GPP 38.901) | full-system urban / rural / indoor |
| **Ray-traced ([[deepmimo]], [[differentiable-ray-tracing]])** | physically grounded, scenario-specific |

In Sionna ([[paper-sionna-2022]]): `sionna.channel.tr38901.UMi(...)` gives 3GPP UMi channels; `sionna.channel.RayleighBlockFading(...)` gives the toy Rayleigh case.

## Formal definition

For a frequency-selective time-varying multipath channel:
$$y(t) = \int h(t, \tau) x(t - \tau)\,d\tau + n(t).$$

In a discrete OFDM system with $L$ taps:
$$\mathbf{y}_k = H_k\, \mathbf{x}_k + \mathbf{n}_k, \quad H_k = \sum_{l=0}^{L-1} h_l\, e^{-j 2\pi k l/N}$$
where $H_k$ is the per-subcarrier frequency-domain channel — the cyclic-prefix trick that makes OFDM a flat-fading channel **per subcarrier**.

## Why it matters

- **Every realistic PHY simulation requires fading models.** Pure AWGN simulations get rejected by PHY reviewers.
- **The reason MIMO works.** Rich multipath = high-rank channel matrix = spatial multiplexing.
- **CSI feedback ([[csi-feedback]])** is the system's response to time-varying $\mathbf{H}$.
- **Wireless-ML datasets are all about fading.** [[deepmimo]] (ray-traced fading), [[deepsense-6g]] (real-world fading), 3GPP CDL/TDL (standardized test fading).

## Common mistakes

- **Reporting AWGN BER for a wireless paper.** No reviewer accepts AWGN-only results.
- **Confusing flat with frequency-selective.** Flat = one complex number per symbol. Selective = vector of taps. Use FFT-domain processing if selective.
- **Doppler ignored at low mobility.** Even pedestrian speeds give significant Doppler at mmWave (2 m/s × 60 GHz / $c$ ≈ 400 Hz).
- **Generating fading with one realization, not many.** BER under fading must be **ergodic-averaged** over many channel realizations, not computed for a single $\mathbf{H}$.
- **Mismatched reference frame.** "Train on UMi, test on UMi" — overfit-to-channel-model. Always test on held-out scenarios.

## Related
- [[ofdm]] — turns frequency-selective into per-subcarrier flat fading.
- [[mimo-basics]] — multipath richness drives MIMO gains.
- [[neural-receiver]] — receives the faded signal.
- [[csi-feedback]] — the protocol for telling the TX what $\mathbf{H}$ is.
- [[deepmimo]], [[differentiable-ray-tracing]], [[deepsense-6g]] — datasets that capture realistic fading.
- [[python-ml-wireless]] — Phase 1 multipath extension, Phase 3 channel estimation.

## Practice
- Simulate Rayleigh flat-fading BPSK at SNR 0–20 dB; plot BER vs. SNR; verify the $\sim 1/\gamma_0$ slope.
- For a 3-tap Rayleigh channel, simulate frequency-selective ISI on BPSK without equalizer; observe BER floor.
- In Sionna, run `sionna.channel.tr38901.UMi`; visualize the resulting per-subcarrier $|H_k|$ to see frequency-selective fading.
