---
title: FFT Butterfly
type: concept
course:
  - "[[eee-404]]"
tags: [fft, butterfly, algorithm]
sources:
  - "[[slides-fft-core-equations]]"
  - "[[slides-fft-implementation]]"
created: 2026-04-21
updated: 2026-05-06
---

# FFT Butterfly

## In one line
The butterfly takes two complex numbers ($X_e[k], X_o[k]$) and a twiddle factor $W_N^k$, and produces two outputs ($X[k], X[k+N/2]$). It's named "butterfly" because of the $\times$-shaped signal-flow graph.

## Example first
Say we have $X_e[0] = 3$, $X_o[0] = 1$, and twiddle $W_4^0 = 1$ (so at the top-of-the-stage butterfly for $N=4$):

- Upper output: $X[0] = X_e[0] + W_4^0 \cdot X_o[0] = 3 + 1\cdot 1 = $ **4**
- Lower output: $X[0+2] = X_e[0] - W_4^0 \cdot X_o[0] = 3 - 1\cdot 1 = $ **2**

That's one butterfly. An 8-point FFT has 12 of them (3 stages $\times$ 4 per stage). Most of the complexity of writing an FFT is just tracking which butterflies exist at which stage and with which twiddle.

## The idea

```
        X_e[k] ─────────●────────── X[k]
                        ▲
                        │ +
                        │
                        │   × W_N^k
        X_o[k] ────────●─────────── X[k+N/2]
                          -
```

Two inputs in, two outputs out:
- **Top output:** upper input + twiddle × lower input
- **Bottom output:** upper input $-$ twiddle $\times$ lower input

The bottom output "comes for free" once you've computed the top — that's where the N log N savings come from. Without the butterfly reuse, you'd recompute everything.

## Formal equations

$$X[k]         = X_e[k] + W_N^k \cdot X_o[k]$$
$$X[k + N/2]   = X_e[k] - W_N^k \cdot X_o[k]$$

for $k = 0, 1, \ldots, N/2 - 1$. The minus sign in the second equation comes from the [[twiddle-factor]] identity $W_N^{k+N/2} = -W_N^k$.

## In code (from [[lab-7-fft]])

```c
temp.re = U.re * X[k].re - U.im * X[k].im;  // temp = U * X[k]
temp.im = U.re * X[k].im + U.im * X[k].re;
P.re = (X[i].re + temp.re) * scale;         // top output
P.im = (X[i].im + temp.im) * scale;
Q.re = (X[i].re - temp.re) * scale;         // bottom output
Q.im = (X[i].im - temp.im) * scale;
X[i] = P;  X[k] = Q;                        // in-place store
```

Key point: the computation is **in-place**. `X[i]` and `X[k]` are overwritten by their own butterfly's outputs; nothing else reads them until the next stage.

## Butterfly count

| $N$ | Stages ($\log_2 N$) | Butterflies per stage ($N/2$) | Total |
|---|---|---|---|
| 4 | 2 | 2 | 4 |
| 8 | 3 | 4 | 12 |
| 128 | 7 | 64 | 448 |
| 1024 | 10 | 512 | 5120 |

## Common mistakes
- **Reading `X[i]` after you've written `P`** — in the 2-line sequence `P` then `Q`, you must compute `Q` from the *original* `X[i]`, not the overwritten one. The code above is safe because it reads `X[i]` twice before writing.
- Using the wrong twiddle for the wrong butterfly. Twiddle exponent depends on stage and butterfly index, not just one of them.
- Forgetting the scale factor at a stage when overflow is expected. See [[fft-scaling]].

## Related
- [[fft]] — the context
- [[twiddle-factor]] — the $W$ in $W\cdot X[k]$
- [[fft-scaling]] — where the `* scale` comes from
- [[decimation-in-time]] — why the even/odd split generates butterflies

## Practice
- [[fft-fundamentals-set-01]]
