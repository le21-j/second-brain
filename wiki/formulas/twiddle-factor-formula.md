---
title: Twiddle Factor (Formula)
type: formula
course:
  - "[[eee-404]]"
tags: [fft, twiddle]
sources:
  - "[[slides-fft-core-equations]]"
created: 2026-04-21
updated: 2026-05-06
---

# Twiddle Factor — Formula

## Definition

$$W_N = e^{-j\tfrac{2\pi}{N}}, \qquad W_N^k = \cos\!\tfrac{2\pi k}{N} - j\sin\!\tfrac{2\pi k}{N}$$

## Identities used in FFT

| Identity | What it gives you |
|---|---|
| $W_N^{k+N} = W_N^k$ | Periodicity |
| $W_N^{k+N/2} = -W_N^k$ | Half-circle $\to$ butterfly $-$sign |
| $(W_N)^2 = W_{N/2}$ | Squaring $\to$ next recursion level |
| $W_N^0 = 1$, $W_N^{N/4} = -j$, $W_N^{N/2} = -1$ | Quarter-turn values |

## Reference table (small $N$)

**$N = 2$:** $W_2^0 = 1$, $W_2^1 = -1$.
**$N = 4$:** $W_4^0 = 1$, $W_4^1 = -j$, $W_4^2 = -1$, $W_4^3 = j$.
**$N = 8$:** $W_8^0 = 1$, $W_8^1 = (\sqrt{2}/2)(1 - j)$, $W_8^2 = -j$, $W_8^3 = -(\sqrt{2}/2)(1 + j)$, $W_8^4 = -1$, and $W_8^{k+4} = -W_8^k$.

## Related
- [[twiddle-factor]]
- [[butterfly]]
