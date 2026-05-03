---
title: Equalization
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - equalization
  - isi
  - lmmse
  - foundations
  - wireless
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-05-01
updated: 2026-05-01
---

# Equalization

## In one line
**Undo the channel's distortion at the receiver.** A linear filter (or nonlinear estimator) that inverts inter-symbol interference (ISI) introduced by frequency-selective fading. Linear ZF / LMMSE equalizers are the textbook baselines; **neural receivers** ([[neural-receiver]]) replace these blocks with a learned mapping.

## Example first

**Three-tap Rayleigh ISI channel:**
$$y_n = h_0\, x_n + h_1\, x_{n-1} + h_2\, x_{n-2} + n_n$$
with $h_0 = 1$, $h_1 = 0.5$, $h_2 = 0.2$ (a typical mild ISI).

Without equalization, BER **floors** because each symbol overlaps with neighbors. **Linear MMSE equalizer** computes weights $\mathbf{w}$ minimizing $\mathbb{E}|\hat x_n - x_n|^2$:
$$\mathbf{w}_{\text{MMSE}} = (\mathbf{H}^*\mathbf{H} + \sigma^2 \mathbf{I})^{-1} \mathbf{H}^*$$
where $\mathbf{H}$ is the channel convolution matrix. Output: $\hat x_n = \sum_k w_k\, y_{n+k}$.

In OFDM ([[ofdm]]), the cyclic prefix turns frequency-selective fading into **per-subcarrier flat fading**, so equalization becomes a **scalar per-subcarrier division** $\hat X_k = Y_k / H_k$ (ZF) or $\hat X_k = H_k^* Y_k / (|H_k|^2 + \sigma^2)$ (MMSE) — much simpler than time-domain equalization.

```python
# OFDM per-subcarrier MMSE
H = np.fft.fft(h, N)         # frequency-domain channel
Y = np.fft.fft(y_with_cp[:N])  # received OFDM (after CP removal)
X_hat = (np.conj(H) * Y) / (np.abs(H)**2 + sigma2)
```

## The idea

Multipath fading creates **inter-symbol interference (ISI)**: each received symbol is a linear combination of several transmitted symbols. Equalization reverses this:

| Equalizer | Method | Pros | Cons |
|---|---|---|---|
| **Zero-Forcing (ZF)** | $\mathbf{w} = \mathbf{H}^{-1}$ | exact at high SNR | noise amplification when $\mathbf{H}$ ill-conditioned |
| **LMMSE** | $\mathbf{w} = (\mathbf{H}^*\mathbf{H} + \sigma^2 \mathbf{I})^{-1}\mathbf{H}^*$ | optimal MSE; well-conditioned | needs $\sigma^2$ estimate |
| **DFE (Decision Feedback)** | linear forward + decided-symbol cancellation | better than linear | error propagation |
| **Viterbi / MAP** | trellis search | optimal symbol detection | exponential in delay spread |
| **Neural receiver** | learn end-to-end | matches LMMSE+ at lower latency | needs training |

### OFDM simplification
OFDM transforms a length-$L$ ISI channel into $N$ parallel **per-subcarrier flat-fading channels** (where $L \leq $ CP length). Equalization becomes scalar division per subcarrier — the reason OFDM dominates 5G/Wi-Fi / 4G LTE.

### Joint with channel estimation
Real receivers don't have perfect $\mathbf{H}$ — they estimate it from pilots ([[csi-feedback]] / DMRS). Equalization quality depends on $\hat{\mathbf{H}}$ accuracy. **Neural receivers** ([[paper-nrx-cammerer-2023]]) learn channel estimation + equalization + demapping **jointly**, removing error compounding between blocks.

## Formal definition

For an ISI channel $\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}$ with $\mathbf{n} \sim \mathcal{CN}(0, \sigma^2 \mathbf{I})$:

**Zero-Forcing:**
$$\hat{\mathbf{x}}_{\text{ZF}} = (\mathbf{H}^*\mathbf{H})^{-1}\mathbf{H}^*\mathbf{y}.$$

**LMMSE:**
$$\hat{\mathbf{x}}_{\text{MMSE}} = (\mathbf{H}^*\mathbf{H} + \sigma^2 \mathbf{I})^{-1}\mathbf{H}^*\mathbf{y}.$$

**ML (optimal symbol-detector for finite alphabet $\mathcal{X}$):**
$$\hat{\mathbf{x}}_{\text{ML}} = \arg\min_{\mathbf{x} \in \mathcal{X}^N} \|\mathbf{y} - \mathbf{H}\mathbf{x}\|^2.$$

ML is exponential in $N$; LMMSE is the polynomial-time relaxation.

## Why it matters

- **Every wireless receiver equalizes.** The block diagram universally has an equalizer between channel estimator and demapper.
- **Replaced by neural receivers.** [[paper-nrx-cammerer-2023]] / [[paper-nrx-wiesmayr-2024]] fold equalization into a single neural net.
- **OFDM's per-subcarrier equalization** is why OFDM is the dominant 5G/Wi-Fi waveform.
- **CSI quality determines equalization quality.** Imperfect $\hat{\mathbf{H}}$ causes residual ISI — a thread that connects to [[csi-feedback]] and [[deepmimo]]-based ML estimation.

## Common mistakes

- **ZF in low SNR.** Noise amplification dominates. Use LMMSE.
- **Forgetting noise variance for LMMSE.** Use a noise estimator or fix $\sigma^2 = N_0$ if known.
- **Per-tap vs per-subcarrier.** Time-domain equalizers fight ISI directly; OFDM equalizers handle each subcarrier independently. Don't confuse.
- **Stale CSI.** Channel changes faster than CSI feedback — equalizing with outdated $\hat{\mathbf{H}}$ is worse than no equalization in fast-fading regimes.
- **Not jointly optimizing with channel coding.** Modern receivers iterate between equalization and decoding (turbo equalization). Linear equalize-then-decode loses 0.5–1 dB.

## Related
- [[ofdm]] — turns ISI into per-subcarrier flat fading.
- [[fading-channels]] — what creates ISI in the first place.
- [[neural-receiver]] — modern learned alternative to ZF/LMMSE.
- [[csi-feedback]] — the channel-state-information equalization needs.
- [[matched-filter]] — equalization assumes you've already matched-filtered + sampled.
- [[python-ml-wireless]] — Phase 1 multipath extension, Phase 3 channel-estimation project.

## Practice
- Implement ZF and LMMSE equalizers for a 3-tap Rayleigh channel; plot BER vs. SNR. Show LMMSE wins at low SNR.
- For an OFDM signal, implement per-subcarrier LMMSE equalization given perfect CSI; verify it matches Sionna's `LMMSEEqualizer`.
- Train a small neural receiver end-to-end (no separate channel estimator) and compare BLER vs. classical chain — reproduces a Sionna tutorial result.
