---
title: Reed-Muller codes
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - channel-coding
  - 5g-nr
  - reed-muller
  - polar
  - phase-3
sources:
  - "[[textbook-mackay-itila]]"
created: 2026-05-01
updated: 2026-05-01
---

# Reed-Muller codes

## In one line
**Reed-Muller (RM) codes are an algebraic code family from the 1950s — and they turn out to be the special case of [[polar-codes]] with a fixed all-or-nothing freezing rule.** 5G NR uses small RM codes (RM(1, m)) for very short PUCCH (1–11 bit acknowledgements).

## Example first

**RM(1, 3)** — a length-8 code that encodes 4 bits with minimum distance 4. Generator matrix:

$$\mathbf{G}_{4 \times 8} = \begin{pmatrix} 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\ 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \end{pmatrix}$$

Each codeword = data $\mathbf{u} \cdot \mathbf{G}$. 16 codewords, distance 4 — corrects any single error.

The decoder uses **majority logic** — count the votes of certain parity sums to recover each information bit.

## The idea

RM codes have a recursive Plotkin (u, u+v) construction:
- RM(r, m) takes two RM(r, m-1) codewords $\mathbf{u}$ and $\mathbf{v}$, then concatenates $(\mathbf{u}, \mathbf{u} + \mathbf{v})$.
- Length $N = 2^m$, minimum distance $d_{\min} = 2^{m-r}$, dimension $K = \sum_{i=0}^{r}\binom{m}{i}$.

This **recursive XOR structure is the same one polar codes use** — and that's not a coincidence: polar codes are built on the same Plotkin construction.

## Why it matters / where it sits in the roadmap

- **Foundation for [[polar-codes]].** Understanding RM gives the algebraic intuition for why polar's frozen-set design works. **Read RM first, polar second.**
- **5G NR PUCCH Format 0/1.** Very short uplink control (1 or 2 bit ACK/NACK) uses tiny RM codes — the simplest possible 5G channel-coding case.
- **MacKay Ch 12 + 47.** Foundational reading.

## Common mistakes
- **Treating RM as obsolete.** RM is still used in 5G for very-short control. The "obsolete" framing is wrong; it's pedagogically out of fashion but practically alive.
- **Confusing RM with Reed-Solomon.** Different code family. Reed-Solomon (RS) is non-binary (operates over $GF(q)$); RM is binary.

## Related
- [[polar-codes]] — RM's modern descendant; polar with all-or-nothing freezing **is** RM.
- [[ldpc-codes]] — modern data-channel cousin.
- [[textbook-mackay-itila]] — Ch 12 (linear codes), Ch 47 (extended discussion).
- [[python-ml-wireless]]
