---
title: Millimeter-wave (mmWave) MIMO
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - mmwave
  - mimo
  - beamforming
  - 5g
  - 6g
  - alkhateeb
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
  - "[[paper-deepsense-6g-2023]]"
  - "[[paper-deepmimo-2019]]"
created: 2026-05-01
updated: 2026-05-01
---

# Millimeter-wave (mmWave) MIMO

## In one line
**At mmWave (24–100 GHz), antennas shrink so $\lambda/2$-spaced arrays of 64–256 elements fit on a phone — and you NEED that many because path loss is ~30 dB worse than sub-6, so beamforming from large arrays is the only way to close the link.**

## Example first

**5G NR FR2 phone.** 28 GHz carrier ($\lambda = 1.07$ cm). The phone's mmWave module is a $4 \times 4$ patch array — that's 16 antennas in roughly the area of a thumbnail. The base station has a $32 \times 8 = 256$-element panel. To start a session:
1. **Beam sweep.** BS transmits ~64 candidate beams (one synchronization signal per beam direction); UE measures RSRP per beam and reports the strongest.
2. **Beam tracking.** As the user walks, the strongest beam direction drifts. UE feeds back the index periodically; BS retunes.
3. **MIMO data layer.** Once the link is locked, the BS can send up to ~4 spatial streams along sub-beams of the chosen wide beam.

If a body or wall blocks the LoS, the link fails fast (~10s of dB drop) — recovery requires re-sweeping or a digital twin / sensor-aided guess. **This blockage-sensitivity is exactly why DeepSense 6G + LWM exist.**

## The idea

mmWave bands offer **GHz-scale bandwidth** — 100× more than sub-6 GHz — but at three costs:
1. **Path loss is severe.** Friis $\propto \lambda^2$; smaller $\lambda$ = larger loss for the same antenna gain. **You compensate with antenna arrays** because $\lambda/2$-spaced elements are 5–10 mm apart (vs. 6–15 cm at sub-6), so you can fit 16–256 of them in handheld form factors.
2. **Beams are pencil-thin.** 64 antennas → ~10° main-lobe width. Slight misalignment kills the link.
3. **Blockage is severe.** mmWave doesn't diffract well around bodies, walls, foliage. Channels are highly **sparse** in angle-delay (typically 1–4 dominant paths) and **non-stationary** as users move.

Beamforming options: **digital** (one RF chain per antenna — too power-hungry at 256 antennas), **analog** (one RF chain + phase shifters — cheap but only one beam at a time), or **hybrid** (a few digital streams × analog phase shifters — the standard 5G NR FR2 approach).

## Formal definition

Channel model with $N_t$ TX antennas and $N_r$ RX antennas:

$$\mathbf{H} = \sum_{l=1}^{L} \alpha_l \, \mathbf{a}_r(\theta_l^{\text{rx}}) \, \mathbf{a}_t^H(\theta_l^{\text{tx}}) \in \mathbb{C}^{N_r \times N_t}$$

with $L$ paths, complex gains $\alpha_l$, and array steering vectors $\mathbf{a}_t, \mathbf{a}_r$. mmWave's defining feature: **$L$ is small (typically 1–4)** vs. sub-6 GHz where $L$ can be 20+. This **sparsity in angle-delay-Doppler** is what foundation models like LWM exploit.

Beamforming combines channel coefficients into one effective scalar: $y = \mathbf{w}_r^H \mathbf{H} \mathbf{w}_t s + \mathbf{w}_r^H \mathbf{n}$. Optimal $\mathbf{w}_t, \mathbf{w}_r$ = principal singular vectors of $\mathbf{H}$ — but you need $\mathbf{H}$ to compute them, hence the whole "beam prediction" problem.

## Why it matters / when you use it

- **Phase 3 M9 deliverable.** [[python-ml-wireless]] explicitly calls **DeepSense 6G beam prediction (scenario 31, top-K accuracy, DBA-Score)** the primary M9 project. mmWave-MIMO is the underlying problem.
- **Phase 4 M11 capstone — LWM extension.** Foundation models for wireless rely on mmWave-MIMO datasets (DeepMIMO scenarios are mostly mmWave); you can't extend LWM without understanding the channel model.
- **Both target labs work mmWave-first.** Wi-Lab's flagship problems (DeepSense, LWM, RIS-O-RAN, vehicle-to-everything beam tracking) are all mmWave; NVIDIA Sionna's 28-GHz indoor reproduction in [[paper-diff-rt-calibration-2024]] is mmWave. **You can't speak the language without it.**
- **Sensing-comm fusion stack.** mmWave's blockage problem motivates camera/LiDAR/radar/RGB-aided beam prediction — the [[deepsense-6g]] thesis.

## Common mistakes

- **Treating mmWave as just sub-6 with bigger numbers.** The sparsity ($L \leq 4$) and blockage-sensitivity change which algorithms work. Linear MMSE estimators that work at sub-6 may underperform sparse-recovery (compressed sensing, ML-with-priors) at mmWave.
- **Ignoring hybrid-beamforming hardware constraints.** Papers that assume fully-digital beamforming for 256 antennas are unrealistic for mobile devices.
- **Path-loss formula confusion.** Friis is for free space; real mmWave channels have additional foliage/body/glass losses (10–30 dB) that simulators must include — see DeepMIMO ray-traced scenarios.
- **Antenna spacing and element count.** $\lambda/2 \approx 5$ mm at 28 GHz; sub-arrays must be designed accordingly. Confusing $\lambda/2$ with $1$ cm gives wrong beam-width predictions.

## Related

- [[mimo-basics]] — the general framework. mmWave-MIMO is sparse + hybrid + blockage-prone variant.
- [[antenna-array]] — the array geometry mmWave depends on.
- [[fading-channels]] — mmWave blockage = abrupt path birth/death (different from Rayleigh).
- [[beam-prediction]] — the headline mmWave-MIMO task.
- [[deepsense-6g]], [[deepmimo]] — the canonical mmWave-MIMO datasets.
- [[paper-deepsense-6g-2023]], [[paper-deepmimo-2019]] — sources.
- [[paper-lwm-temporal-2026]] — channel-trajectory modeling for mmWave.
- [[paper-diff-rt-calibration-2024]] — indoor 28-GHz calibration.

## Practice
- **TODO** — DeepMIMO `O1_28` channel exploration: visualize the angle-delay sparsity, compare to sub-6 `O1_3p5`. Defer to Phase 3 M8.
