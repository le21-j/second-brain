---
title: Bit-Reversed Order
type: concept
course: [[eee-404]]
tags: [fft, indexing, algorithm]
sources: [[slides-fft-implementation]], [[lab-7-fft]]
created: 2026-04-21
updated: 2026-04-26
---

# Bit-Reversed Order

## In one line
Permute indices by **reversing the bits of their binary representation** — that's the order a DIT FFT wants its input in.

## Example first
$N = 8$ (3-bit indices). Original index $\to$ binary $\to$ reversed $\to$ new index:

| Original | Binary | Reversed | New |
|---|---|---|---|
| 0 | 000 | 000 | 0 |
| 1 | 001 | 100 | 4 |
| 2 | 010 | 010 | 2 |
| 3 | 011 | 110 | 6 |
| 4 | 100 | 001 | 1 |
| 5 | 101 | 101 | 5 |
| 6 | 110 | 011 | 3 |
| 7 | 111 | 111 | 7 |

So $x[n] = [a, b, c, d, e, f, g, h]$ is reshuffled to $[a, e, c, g, b, f, d, h]$ before the FFT loops touch it.

For $N = 4$ (2-bit indices):

| Original | Binary | Reversed | New |
|---|---|---|---|
| 0 | 00 | 00 | 0 |
| 1 | 01 | 10 | 2 |
| 2 | 10 | 01 | 1 |
| 3 | 11 | 11 | 3 |

So $[a, b, c, d] \to [a, c, b, d]$. The question about IDFT in [[slides-fft-idft]] uses this: conjugate of $[1, 2-j, -3, 2+j]$ is $[1, 2+j, -3, 2-j]$, bit-reversed $\to$ **$[1, -3, 2+j, 2-j]$**.

## The idea
The [[decimation-in-time]] recursion keeps pulling out even-indexed samples to one half and odd-indexed to the other. After $\log_2 N$ levels, sample $x[n]$ ends up at position `bitreverse(n)` in the reordered sequence. Reordering the input first (rather than the output) means the FFT can write its stage-by-stage results **in place**.

## Why it matters
Without bit-reversal, your FFT output is scrambled. Every DIT FFT implementation either:
- bit-reverses the **input** before running (what the lab code does), **or**
- produces bit-reversed **output** and the caller un-reverses it.

The lab provides `bit_rev()` already, so you just call it before `fft()`.

## The lab's bit-reversal algorithm

```c
j = 0;
for (i = 1; i < size - 1; i++) {
    k = size >> 1;                  // k starts at N/2
    while (k <= j) { j -= k; k >>= 1; }
    j += k;                         // j now = bitreverse(i)
    if (i < j) swap(X[i], X[j]);    // swap only once per pair
}
```

This computes bit-reversed indices incrementally rather than computing each from scratch — neat trick. The `if (i < j)` guard prevents swapping a pair back to original order.

## Common mistakes
- Reversing digits but not in binary. It's **binary** bit reversal, not decimal digit reversal.
- Applying bit-reversal twice (once on input, once on output). That undoes the whole point — the output is already in natural order after a correct DIT FFT on bit-reversed input.
- Getting the bit count wrong. For $N = 2^\nu$ indices, reverse exactly $\nu$ bits. For $N=4$ use 2 bits, for $N=128$ use 7 bits.

## Related
- [[decimation-in-time]] — the reason bit-reversal shows up
- [[fft]]

## Practice
- [[fft-fundamentals-set-01]] — includes a bit-reversal question
