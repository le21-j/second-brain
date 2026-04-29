---
title: OFDM (orthogonal frequency-division multiplexing)
type: concept
course: [[python-ml-wireless]]
tags: [wireless, waveform, ofdm, 5g-nr, phy, dft, fft]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# OFDM — orthogonal frequency-division multiplexing

## In one line
Spread a wideband signal across many narrow parallel subcarriers by **IFFT**ing the symbols at the transmitter and **FFT**ing them at the receiver — turning a frequency-selective multipath channel into hundreds of simple flat channels, each of which can be equalized with a single complex division.

## Example first

A $20$ MHz signal hits a 3-tap Rayleigh multipath channel. In a single-carrier system, those taps cause severe inter-symbol interference (ISI) and you need a complex equalizer.

**In OFDM** (with $N = 64$ subcarriers, cyclic prefix $N_{CP}$ longer than the channel):

```
TX:  bits -> QAM symbols X[k]  ->  IFFT  ->  add cyclic prefix  ->  s[n] to DAC
channel: s[n] -> multipath -> received r[n]
RX:  r[n] -> strip CP  ->  FFT  ->  Y[k] = H[k] * X[k] + noise
     equalize: X_hat[k] = Y[k] / H_hat[k]   (one complex divide per subcarrier)
     demap X_hat[k] -> bits
```

The cyclic prefix converts the linear multipath convolution into a *circular* convolution over each OFDM symbol, and circular convolution in time $=$ pointwise multiplication in frequency. So what was a nasty ISI problem becomes **$64$ parallel one-tap problems**.

## The idea

OFDM is the **dominant physical-layer waveform of 4G LTE, 5G NR, WiFi 6/7, and the baseline candidate for 6G**. The elegance is that it trades physical-layer complexity (one-tap per subcarrier) for computational complexity (one $N$-point FFT per symbol) and an overhead tax (the cyclic prefix is dead air that carries no new information).

### Key parameters (5G NR numerology 0)

- **Subcarrier spacing (SCS):** $15$ kHz (numerology 0); higher numerologies use $30$ kHz, $60$ kHz, $120$ kHz.
- **FFT size:** $2048$ for $20$ MHz @ $15$ kHz SCS; smaller in narrowband.
- **Cyclic prefix:** typically $7$–$25\%$ of the OFDM symbol ($4.7\ \mu$s for normal CP at $15$ kHz SCS).
- **Active subcarriers:** a subset — guard bands on the edges $+$ DC null.

### Pilots, DMRS, and channel estimation

Because the equalizer needs $\hat H[k]$, OFDM systems embed **demodulation reference signals (DMRS)** on a known subset of (time, frequency) resource elements. The receiver interpolates $H$ across the grid — this is where [[channel-estimation]], [[csi-feedback]], and neural-receiver work intervene.

Classical channel estimators:
- **Least Squares (LS)** — $\hat{H}[k] = Y[k] / X_\text{pilot}[k]$ at pilot positions; interpolate.
- **LMMSE** — exploits the channel's correlation structure; theoretically optimal under a Gaussian prior.

### Where OFDM meets PHY-ML

- [[neural-receiver]] eats an OFDM resource grid and spits out LLRs, replacing all the "estimate $+$ equalize $+$ demap" classical steps.
- [[autoencoder-phy]] often uses OFDM as the channel-use medium.
- [[csi-feedback]] compresses the full-band $\hat{H}$ for the BS to use.
- RadioML datasets include OFDM as one of the modulation classes in [[modulation-classification]].

## Formal definition

Time-domain transmit samples for one OFDM symbol with subcarrier symbols $X[0], \ldots, X[N-1]$:

$$s[n] = \frac{1}{\sqrt{N}}\sum_{k=0}^{N-1} X[k]\, e^{j 2\pi k n / N}, \quad n = 0, \ldots, N-1$$

(This is the inverse DFT — see [[idft]].)

Then prepend the cyclic prefix: $s[-N_{CP}], \ldots, s[-1] = s[N - N_{CP}], \ldots, s[N-1]$.

After propagation through a channel with impulse response $h[n]$ of length $L \leq N_{CP} + 1$ and AWGN $w[n]$:

$$r[n] = (h * s)[n] + w[n]$$

At the receiver, strip CP and FFT:

$$Y[k] = H[k] \cdot X[k] + W[k]$$

where $H[k]$ is the DFT of the channel impulse response. One complex divide per subcarrier and you're back in symbol-space.

## Why it matters / when you use it

- **Essentially every modern wideband wireless system is OFDM-based.** Internalizing OFDM is not optional.
- **OFDM is where wireless meets DFT/FFT** — everything from [[eee-404]] (FFT arc) maps directly onto the OFDM pipeline.
- **It's the substrate for PHY-ML.** Neural receivers, E2E autoencoders, pilotless transmission schemes — all developed on OFDM.

## Common mistakes

- **Forgetting the $1/\sqrt{N}$ normalization.** Changes BER curves by $\sim 3$ dB if you mess it up.
- **Cyclic prefix too short.** If CP $<$ channel delay spread, you get ISI and ICI; don't.
- **Pilot alignment off by one.** Pilot index bookkeeping is the most common OFDM bug. Write a unit test.
- **Ignoring the DC null.** Most OFDM systems zero out DC because DC is polluted by LO leakage; forgetting means your classical estimator's interpolation blows up there.
- **Sampling-frequency offset.** SFO manifests as a phase ramp across subcarriers that rotates with symbol index. Standard in real SDRs; document assumption.

## Connections to the existing vault

Everything in [[eee-404]] — especially [[dft]], [[fft]], [[twiddle-factor]], [[decimation-in-time]], [[real-valued-fft]] — is machinery you use to build OFDM. The [[system-pipeline]] AirComp design uses OFDM numerology (5G NR numerology 0, $1.92$ MHz). [[channel-estimation]] in the research folder is essentially OFDM channel estimation.

## Research ties / reading order

1. PySDR Chapter 12 (OFDM) — [[pysdr-lichtman]] — the gentle introduction.
2. Sionna Tutorial Part 2 (OFDM primer) — code-first.
3. 3GPP TS 38.211 for the NR standard details (only when you need actual resource-grid specifics).
4. Bölcskei, Healey, Paulraj — classical OFDM MIMO tutorials.

## The move for Jayden
Phase 1 Month 2: **OFDM-from-scratch in NumPy** — bits $\to$ QAM $\to$ IFFT $\to$ CP $\to$ AWGN $\to$ FFT $\to$ equalize $\to$ demap $\to$ BER vs $E_b/N_0$ validated against Q-function. One week. First headline figure for the portfolio.

## Related
- [[dft]], [[fft]], [[idft]], [[real-valued-fft]] — existing EEE 404 FFT arc (foundation).
- [[neural-receiver]]
- [[csi-feedback]]
- [[channel-estimation]]
- [[modulation-classification]]
- [[pysdr-lichtman]]
- [[python-ml-wireless]]

## Practice
- Phase 1 Month 2 "OFDM from scratch" is both the classic OFDM exercise and the first wireless deliverable.
