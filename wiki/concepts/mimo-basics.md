---
title: MIMO basics
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - mimo
  - foundations
  - wireless
  - massive-mimo
  - 5g-nr
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-05-01
updated: 2026-05-01
---

# MIMO basics

## In one line
**Multiple-Input Multiple-Output:** use $N_t$ transmit antennas + $N_r$ receive antennas to (a) increase spectral efficiency by **spatial multiplexing** (independent streams), (b) increase reliability by **diversity** (same info, multiple paths), or (c) **beamform** a directional pattern. Doubling antennas roughly doubles capacity in rich scattering. The single biggest 5G NR throughput driver.

## Example first

**$2 \times 2$ MIMO.** Transmit two parallel streams $\mathbf{x} = (x_1, x_2)$ from 2 antennas; receive $\mathbf{y} = (y_1, y_2)$ on 2 antennas through channel matrix
$$\mathbf{H} = \begin{pmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{pmatrix}.$$

Channel model:
$$\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}, \quad \mathbf{n} \sim \mathcal{CN}(0, \sigma^2 \mathbf{I}).$$

If $\mathbf{H}$ is invertible, **zero-forcing (ZF) detection**:
$$\hat{\mathbf{x}} = \mathbf{H}^{-1}\mathbf{y} = \mathbf{x} + \mathbf{H}^{-1}\mathbf{n}.$$

Concrete numbers: $\mathbf{H} = \begin{pmatrix} 1 & 0.5j \\ 0.3 & 0.8 \end{pmatrix}$, $\mathbf{x} = (1, j)$ (BPSK + QPSK), $\mathbf{n} = (0.1, -0.05)$.
- $\mathbf{y} = (1 - 0.5 + 0.1, 0.3 + 0.8j - 0.05) = (0.6, 0.25 + 0.8j)$.
- $\hat{\mathbf{x}} = \mathbf{H}^{-1}\mathbf{y} \approx (1, j)$ (ZF recovers).

But noise is **amplified** by the condition number of $\mathbf{H}$ — bad channels (near-singular $\mathbf{H}$) blow up noise. **MMSE detection** trades a small bias for variance reduction:
$$\hat{\mathbf{x}}_{\text{MMSE}} = (\mathbf{H}^*\mathbf{H} + \sigma^2 \mathbf{I})^{-1} \mathbf{H}^* \mathbf{y}.$$

## The idea

A single-antenna link has fixed rate. Add antennas → either:

1. **Spatial multiplexing.** Send $\min(N_t, N_r)$ independent streams in parallel. Capacity scales linearly: $C \approx \min(N_t, N_r) \log_2(\text{SNR})$.
2. **Diversity.** Send the same symbol from multiple antennas (often with phase weights) → reduce fading-induced outage. Diversity order = $N_t \cdot N_r$.
3. **Beamforming.** Steer the radiated pattern by adjusting per-antenna phase + amplitude. **Massive MIMO** ($N_t \gg N_r$) makes this dramatic — pencil-beams at mmWave.

5G NR uses all three depending on conditions: closed-loop precoding sets the trade-off based on CSI feedback ([[csi-feedback]]).

### Receiver detectors
| Detector | Complexity | Performance |
|---|---|---|
| **Zero Forcing (ZF)** | $O(N^3)$ | poor for ill-conditioned $\mathbf{H}$ |
| **MMSE** | $O(N^3)$ | better than ZF, especially low-SNR |
| **K-Best / sphere decoder** | exponential worst-case | near-ML |
| **Maximum Likelihood (ML)** | exponential | optimal |
| **Neural receiver** | learned | matches MMSE+ at much lower latency |

[[paper-nrx-cammerer-2023]] uses cross-antenna attention to handle MU-MIMO interference — the modern alternative.

### Massive MIMO and beamforming
At mmWave (28 GHz, 60 GHz), antennas are tiny ($\lambda/2 = $ a few mm). Pack 64+ antennas in a small array, beamform digitally / hybrid → **focused beams** with 20+ dB gain. This is the Wi-Lab / DeepMIMO / DeepSense regime.

## Formal definition

For $N_t$ TX, $N_r$ RX antennas:
- **Channel:** $\mathbf{H} \in \mathbb{C}^{N_r \times N_t}$.
- **Signal model:** $\mathbf{y} = \mathbf{H}\mathbf{x} + \mathbf{n}$.
- **Capacity (deterministic $\mathbf{H}$, equal power):** $C = \log_2 \det\!\left(\mathbf{I} + \frac{1}{\sigma^2}\mathbf{H}\mathbf{H}^*\right)$.
- **CSI-feedback regime:** TX learns $\mathbf{H}$ → precodes $\mathbf{x} = \mathbf{V}\mathbf{s}$ with $\mathbf{V}$ from SVD$(\mathbf{H}) = \mathbf{U}\boldsymbol\Sigma\mathbf{V}^*$ → optimal water-filling.

## Why it matters

- **5G/6G throughput** comes from MIMO. 1 Gbps → 10 Gbps progression is mostly antenna count + bandwidth.
- **CSI feedback ([[csi-feedback]])** is the bottleneck — TX needs $\mathbf{H}$ to precode, but feedback is bit-limited. CsiNet et al. attack exactly this.
- **Beam prediction ([[beam-prediction]])** in massive MIMO at mmWave — Wi-Lab's DeepSense Challenge predicts the optimal beam from sensors.
- **Neural receivers** for MU-MIMO are NVIDIA Sionna's flagship demo.

## Common mistakes

- **Confusing $N_r \times N_t$ with $N_t \times N_r$.** Channel is "rows = receive, columns = transmit" — $\mathbf{H}_{ij}$ is the gain from TX antenna $j$ to RX antenna $i$.
- **Assuming rich scattering.** MIMO gains depend on the channel having multiple independent paths. In LoS conditions, $\mathbf{H}$ is rank-1 → no multiplexing gain. mmWave LoS environments are MIMO-poor.
- **Ignoring CSI estimation error.** Real systems estimate $\hat{\mathbf{H}}$ with error; precoding based on $\hat{\mathbf{H}}$ degrades. Account for in any sim.
- **Not normalizing the channel.** Average channel power should be 1 by convention; failing this confuses SNR comparisons.

## Related
- [[csi-feedback]] — the bottleneck for closed-loop MIMO.
- [[beam-prediction]] — sensor-aided beam selection in massive MIMO.
- [[neural-receiver]] — modern detection.
- [[fading-channels]] — what makes $\mathbf{H}$ random.
- [[deepmimo]] — the canonical MIMO channel dataset.
- [[python-ml-wireless]] — Phase 1 multipath OFDM deliverable, Phase 3 DeepMIMO project.

## Practice
- For Rayleigh i.i.d. $\mathbf{H} \in \mathbb{C}^{2\times 2}$, simulate ZF and MMSE detection at SNR -5, 0, 5, 10, 15 dB; plot BER curves.
- For a $4 \times 4$ MIMO, plot capacity vs. SNR; compare with $4 \log_2(\text{SNR})$ asymptote.
- On DeepMIMO `O1_3p5`, generate a $32 \times 1$ channel and beamform; visualize the beam pattern.
