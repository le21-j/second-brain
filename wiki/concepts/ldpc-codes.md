---
title: LDPC codes
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - ldpc
  - error-correction
  - belief-propagation
  - foundations
  - wireless
sources:
  - "[[textbook-mackay-itila]]"
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-05-01
updated: 2026-05-01
---

# LDPC codes (Low-Density Parity-Check codes)

## In one line
**Linear error-correcting codes defined by a sparse parity-check matrix $\mathbf{H}$**, decoded by **belief propagation** message-passing on the corresponding Tanner graph. Gallager 1962 (forgotten), MacKay 1996 (rediscovered), now the **5G NR data-channel code**. Capacity-approaching, deeply tied to the iterative-decoding paradigm that GNN message-passing extends.

## Example first

**$(7, 4)$ Hamming-style LDPC.** Code rate $R = k/n = 4/7$. Parity-check matrix:

$$\mathbf{H} = \begin{pmatrix} 1 & 1 & 0 & 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & 1 & 1 & 0 & 0 & 1 \end{pmatrix}.$$

A codeword $\mathbf{c} \in \{0,1\}^7$ satisfies $\mathbf{H}\mathbf{c}^\top = \mathbf{0} \pmod 2$. Each row is a **parity-check** (one bit is the XOR of others); each column is a **variable**.

**Tanner graph.**

```
v1 --- c1
v2 --- c1, c3
v3 --- c2, c3
v4 --- c1, c2, c3
v5 --- c1
v6 --- c2
v7 --- c3
```

Variable nodes $v_i$ on one side, check nodes $c_j$ on the other. Edges connect $v_i$ to $c_j$ iff $\mathbf{H}_{ji} = 1$.

**Belief propagation decoding.** Iteratively pass log-likelihood-ratios (LLRs) along edges:
1. Variables → checks: each $v_i$ sends its current LLR estimate.
2. Checks → variables: each $c_j$ enforces the parity constraint by combining incoming LLRs from other variables.
3. Update variable LLRs and decide $\hat c_i = \text{sign}(\text{LLR}_i)$.

After ~10–50 iterations, BP converges to a (near-)maximum-likelihood codeword.

In Sionna ([[paper-sionna-2022]]):
```python
encoder = sionna.fec.ldpc.LDPC5GEncoder(k=4, n=7)
decoder = sionna.fec.ldpc.LDPC5GDecoder(encoder, num_iter=50)
b = torch.randint(0, 2, (1024, 4))
c = encoder(b)              # encode
y = c + noise               # AWGN channel
b_hat = decoder(y, snr_db)  # decode
```

## The idea

For decades the optimal code design was thought intractable — minimum-distance codes (Hamming, Reed-Solomon, BCH) approached capacity slowly with code length. Then Gallager (1962) proposed using **sparse, randomly-constructed parity-check matrices** that admit local message-passing decoding.

The breakthrough insight: **sparseness allows iterative local decoding to converge.** With sparse $\mathbf{H}$, each parity check involves only ~$d_c$ variables, and each variable participates in only ~$d_v$ checks. Message-passing on the resulting graph is computationally cheap and theoretically near-optimal.

The trade-offs:
- **Rate flexibility.** Choose $\mathbf{H}$ shape to set code rate; standard families (regular, irregular, QC-LDPC) give graceful design.
- **Block length.** Performance improves with $n$. 5G NR supports $n$ from 40 to 8448.
- **Decoder complexity.** ~$n$ messages per iteration × 10–50 iterations = $\sim 10^5$ ops per codeword. GPU-friendly.

### LDPC vs. Polar codes (5G NR)
| | LDPC | Polar |
|---|---|---|
| **5G NR usage** | data channels | control channels |
| **Block length** | medium-long | short-medium |
| **Decoder** | BP / min-sum (parallel) | SCL / SC (sequential) |
| **Latency** | medium | low |

## Formal definition

A **binary** LDPC code is the null space of a sparse parity-check matrix $\mathbf{H} \in \mathbb{F}_2^{m \times n}$:
$$\mathcal{C} = \{\mathbf{c} \in \mathbb{F}_2^n : \mathbf{H}\mathbf{c}^\top = \mathbf{0}\}.$$

**Sparseness:** the number of 1s per row and column is $O(\log n)$ (or constant for regular codes).

The Tanner graph has $n$ variable nodes and $m$ check nodes; edge $(v_i, c_j)$ iff $\mathbf{H}_{ji} = 1$.

## Why it matters

- **The data-channel code in 5G NR.** Every PUSCH/PDSCH transmission is LDPC-encoded.
- **The decoder feeds [[neural-receiver]].** NRX outputs LLRs; LDPC consumes them. The interface is exactly LLR-per-coded-bit.
- **GNN-decoder thread.** Nachmani et al. 2018 → Cammerer et al. 2019 → Buchberger 2020 — neural networks that **learn weights for BP messages** or replace BP entirely with a GNN. The cleanest "DSP-meets-ML" research line.

## Common mistakes

- **Confusing parity-check $\mathbf{H}$ with generator $\mathbf{G}$.** $\mathbf{c} = \mathbf{u}\mathbf{G}$ for encoding; $\mathbf{H}\mathbf{c}^\top = 0$ for the constraint. Different matrices, different roles.
- **Forgetting that BP is iterative.** "One-shot" decoding doesn't work; BP needs $\sim 10$+ iterations.
- **Min-sum vs sum-product.** Min-sum is a hardware-friendly approximation; loses ~0.5 dB but much cheaper. 5G uses min-sum variants in practice.
- **Quantizing LLRs too aggressively.** 4-bit LLRs are common in hardware; below that, BP convergence breaks.

## Related
- [[polar-codes]] — **the data/control split partner**: 5G NR uses LDPC for data, polar for control.
- [[reed-muller-codes]] — polar's parent family.
- [[paper-csinet-wen-2018]] — different problem (compression) but same coding-vs-uncoded comparison framework.
- [[neural-receiver]] — produces LLRs that LDPC consumes.
- [[autoencoder-phy]] — the autoencoder learns its own coding scheme; LDPC is the classical baseline.
- [[textbook-mackay-itila]] — Ch 47 is the canonical introduction.
- [[python-ml-wireless]] — Phase 3 (read MacKay Ch 47–50 alongside neural-decoder work).

## Practice
- For a $(7,4)$ Hamming code, build the parity-check matrix; verify its codewords; implement BP decoding by hand for one message.
- In Sionna, train an autoencoder-PHY and compare BLER against LDPC at the same rate — reproduces the [[paper-oshea-hoydis-2017-autoencoder]] headline figure.
- Read Nachmani et al. 2018 — "Deep Learning Methods for Improved Decoding of Linear Codes" — and reproduce their weight-tied BP unrolling for a small LDPC.
