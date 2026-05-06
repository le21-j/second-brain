---
title: Digitalizing AirComp via Complement Coded Modulation (Wang et al. 2025)
type: summary
source_type: article
source_path: raw/articles/BPSK Two's Compliment.pdf
source_date: 2025-12
course:
  - "[[research]]"
tags: [aircomp, digital-modulation, bpsk, twos-complement, ofdm, lmmse]
created: 2026-04-21
updated: 2026-05-06
---

# BPSK Two's Complement AirComp

**Authors:** Wang, Yao, Xu, Shi, Huang. arXiv:2512.24788 (Dec 2025).

## TL;DR
Digital AirComp scheme: quantize each ED's value with $b$ bits in two's-complement, transmit each bit as a BPSK symbol on a separate OFDM subcarrier, use truncated channel inversion + LMMSE detection at the receiver. Achieves asymptotically error-free computation with minimal codeword length $L = b$. Adds an uneven-power-allocation strategy (geometric) to exploit bit importance.

## Key takeaways
- **Encoder (Eq 5-6):** scaled integer $\zeta\bar s_k$ expressed in two's-complement $\{x_{k,b}, \ldots, x_{k,1}\}$. Each bit $\to$ BPSK $t_{k,l} = 2x_{k,l} - 1$.
- **Decoder (Eq 6):** $f_{\text{dec}}(r_1,\ldots,r_L) = (1/\zeta)(\sum_{l=1}^{L-1} r_l\cdot 2^{l-1} - r_L\cdot 2^{L-1})$. Linearity of two's-complement arithmetic makes superposition over MAC = arithmetic sum.
- **TCI pre-equalization (Eq 7):** $\rho_{k,l} = \sqrt{p_l} \cdot h^*_{k,l} / |h_{k,l}|^2$ if device is in the "active set" $K_l$, else 0. Threshold based on channel gain.
- **LMMSE detector (Prop 1):** $\hat r_l = \lambda_l \cdot \text{Re}\{y_l\} + \mu_l$ with closed-form $\lambda_l = \sqrt{p_l}|K_l|/(2p_l|K_l|+\sigma_l^2)$, $\mu_l = K/2$. Reduces to "just use mean" at low SNR.
- **Power allocation:** geometric sequence $P_{k,l}/P_{k,l-1} = \varpi > 1$ — higher bits get more power, since their contribution to the decoded value is weighted $2^{l-1}$ more.
- **Reliable at low SNR:** outperforms analog baseline (channel-inversion-only), Binary+ML, Balance, Bit-slicing schemes.

## Notes for Jayden's pipeline
- Two's complement is **fundamentally incompatible** with HPSR's regret-learning framework: HPSR is analog/continuous power selection, whereas this is digital bit-level.
- Useful as a **comparison baseline** if Jayden later explores digital AirComp variants.
- The LMMSE detector idea (estimate mean + correction) might transfer — HPSR's $\eta$ denoising factor plays an analogous role.

## Related
- [[paper-md-aircomp-plus]] — MD-AirComp+ extends similar ideas to massive access
- [[aircomp-basics]]
