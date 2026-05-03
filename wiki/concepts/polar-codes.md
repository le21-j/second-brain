---
title: Polar codes
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - channel-coding
  - 5g-nr
  - control-channel
  - polar
  - arikan
  - phase-3
  - phase-4
sources:
  - "[[textbook-mackay-itila]]"
  - "[[paper-gruber-2017-channel-decoding]]"
created: 2026-05-01
updated: 2026-05-01
---

# Polar codes

## In one line
**Polar codes are the first family of error-correcting codes proven to achieve the symmetric capacity of any binary-input discrete memoryless channel (B-DMC)** — and they're 5G NR's **control-channel** code (PBCH/PDCCH/PUCCH). LDPC handles data; polar handles control. Erdal Arıkan, 2009.

## Example first

**A length-8 polar code** (rate 4/8). Encoding is the matrix-vector product $\mathbf{x} = \mathbf{u} G_N$ where $G_N$ is the **Arıkan generator matrix** built recursively:

$$G_N = F^{\otimes n}, \qquad F = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}, \qquad N = 2^n$$

For $N = 8$: $G_8 = F \otimes F \otimes F$ — an $8 \times 8$ binary matrix. Encoding is $\mathbf{x} = \mathbf{u}\,G_8$ over $\mathrm{GF}(2)$.

The 4 highest-reliability $u$-positions carry **data bits**; the 4 lowest-reliability positions are **frozen** to 0. Bit reliability is computed offline per-channel via a recursive density-evolution / Bhattacharyya-bound procedure.

> [!note] Implementation
> In practice you don't materialize $G_N$ — the recursive XOR structure means encoding runs in $O(N \log N)$ via $n$ Kronecker stages, each a sweep of butterfly XOR operations. The structure is identical to FFT decimation-in-time.

Decoding (Successive Cancellation, SC): walk the butterfly backwards, decoding bit $u_1$ first using LLR of $x$, propagate, decode $u_2$, etc. **SCL (List)** decoding keeps the top-$L$ candidates instead of just one — and **CRC-aided SCL** with $L = 8$ is the actual 5G NR decoder.

## The idea — channel polarization

Arıkan's key insight: **combining $N$ identical noisy channels and decoding sequentially polarizes them** — some virtual channels become nearly noiseless, others nearly useless. As $N \to \infty$, the fraction of "good" channels approaches the channel capacity $C$.

Strategy: send your $K = NC$ data bits on the **good** channels; freeze the rest. Capacity-achieving in the asymptotic limit, and good even at $N = 1024$.

## Polar vs. LDPC — when 5G NR uses each

| Code | Use in 5G NR | Why |
|---|---|---|
| **[[ldpc-codes|LDPC]]** | Data channel (PDSCH, PUSCH) | Lower BLER at high rates; mature parallel decoder hardware |
| **Polar** | Control channel (PBCH, PDCCH, PUCCH) | Better at **short** blocklengths ($N \leq 1024$); CRC-aided SCL gets near-MAP performance with practical complexity |

This split — data = LDPC, control = polar — is **the** thing every 5G PHY engineer must know.

## Decoding algorithms — the practical hierarchy

| Decoder | Complexity | BLER |
|---|---|---|
| **SC (Successive Cancellation)** | $O(N \log N)$ | Mediocre at finite $N$ |
| **SCL ($L$ candidates)** | $O(L N \log N)$ | Better as $L$ grows |
| **CRC-SCL** | Same as SCL | **Industry standard** — CRC picks the right candidate from the list |
| **Neural polar decoder** | Trainable | Beats SC, matches SCL at $L=4$; see [[paper-gruber-2017-channel-decoding]] (NN-as-decoder) and Cammerer et al. 2017 *Scaling DL-based Decoding by Partitioning* (the polar-specific extension that scales NND to longer blocklengths) |

## Why it matters / where it sits in the roadmap

- **Phase 3 M7 reading.** The neural-decoder line ([[paper-gruber-2017-channel-decoding]] — Cammerer's PhD origin) **starts with polar codes** and only later extends to LDPC. The Cammerer cold email is incomplete without polar fluency.
- **Phase 4 M11.** Any 5G-NR-compliant work hits polar codes the moment you touch the control plane (every NR slot has PDCCH).
- **Adjacent to AirComp.** [[robust-signaling]] (Jayden's existing project) uses Gold/Golay/polar/CRC for the control plane — polar is one of the candidates.

## Common mistakes

- **Confusing polar with [[ldpc-codes]].** Different code families, different decoders, different use cases. They coexist in 5G NR.
- **Forgetting the CRC.** Pure SCL without CRC is worse than LDPC; CRC-SCL is what makes polar competitive.
- **Treating polar as "just a code."** It's a code + a decoder + a frozen-set design — all three matter for performance.
- **Polar and Reed-Muller.** Polar codes **generalize** [[reed-muller-codes|Reed-Muller]]. RM is the special case of polar with all-or-nothing freezing rule.

## Related
- [[ldpc-codes]] — the data-channel partner.
- [[reed-muller-codes]] — polar codes' parent family.
- [[belief-propagation]] — alternative polar decoder (BP-on-polar; Nachmani 2018 line).
- [[neural-decoder]] — neural-polar is the canonical first toy ([[paper-gruber-2017-channel-decoding]]).
- [[paper-gruber-2017-channel-decoding]] — Cammerer's PhD origin paper, polar codes specifically.
- [[textbook-mackay-itila]] — Ch 47–50 ground the algebraic-coding context.
- [[robust-signaling]] — Jayden's AirComp control-plane analysis cites polar as a candidate.
- [[python-ml-wireless]]

## Practice
- **TODO (Phase 3 M7)** — Implement SC decoder for a $(64, 32)$ polar code in PyTorch; reproduce BLER vs SNR curve. Then add SCL with $L = 4$. Compare to neural decoder ([[paper-gruber-2017-channel-decoding]] line).
