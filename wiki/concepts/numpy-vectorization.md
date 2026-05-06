---
title: NumPy vectorization
type: concept
course:
  - "[[python-ml-wireless]]"
tags: [numpy, vectorization, python, performance, broadcasting]
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-04-23
updated: 2026-05-06
---

# NumPy vectorization

## In one line
Replace Python `for` loops with single calls to NumPy operations on whole arrays — the work moves into compiled C/BLAS code, the garbage collector stops thrashing, and your code often runs $100\times+$ faster without looking harder.

## Example first

Compute a Gaussian-weighted kernel distance between every pair of vectors in two batches. The Python-loop way:

```python
# Slow: 3 nested Python loops. O(N·M·D) Python iterations.
def loop_kernel(X, Y, sigma):
    K = np.zeros((len(X), len(Y)))
    for i in range(len(X)):
        for j in range(len(Y)):
            s = 0.0
            for d in range(X.shape[1]):
                s += (X[i,d] - Y[j,d])**2
            K[i,j] = np.exp(-s / (2*sigma**2))
    return K
```

The vectorized way:

```python
# Fast: one BLAS call + one elementwise exp.
def vec_kernel(X, Y, sigma):
    # Broadcasting trick: shape (N,1,D) - (1,M,D) -> (N,M,D)
    d2 = ((X[:,None,:] - Y[None,:,:])**2).sum(-1)
    return np.exp(-d2 / (2*sigma**2))
```

Same answer. On `X: (1000,50), Y: (1000,50)`, the loop version is $\sim 30$ seconds; the vectorized is $\sim 50$ ms. **$600\times$ speedup, no algorithmic change.**

## The idea

NumPy arrays are **homogeneous, contiguous blocks of memory** with metadata describing their shape and stride. When you write `A + B`, NumPy doesn't loop in Python — it dispatches to a SIMD-aware C kernel that walks the memory directly. Every Python-level loop you avoid is a Python interpreter tax you dodge.

The three skills that matter:

1. **Broadcasting** — the rules NumPy uses to combine arrays of different shapes. Mastering broadcasting is the single highest-leverage skill for vectorization. Canonical rule: shapes are compared right-to-left; each dim must be equal or one of them must be 1 (which gets stretched).
2. **Axis thinking** — every reduction (`sum`, `mean`, `max`) takes an `axis` argument. If you want "column sums" or "batch-wise mean," you parameterize by `axis`, not by looping.
3. **Fancy indexing and masking** — index arrays, boolean masks, `np.where`, `np.take`. These replace conditional loops.

### The transform sequence (Rougier's approach)

The pedagogy in [[textbook-from-python-to-numpy]] is to look at a loop and **systematically transform** it:

1. Identify the loop's body — what scalar operation happens per iteration?
2. Rewrite it on whole arrays — replace scalar indices with array indexing.
3. Replace explicit loops with NumPy ops.
4. Use broadcasting to eliminate the last nested loops.

### DSP-specific vectorization patterns

For Jayden's wireless context:
- **Convolution / correlation** $\to$ `np.convolve`, `scipy.signal.fftconvolve`, `scipy.signal.correlate`.
- **FFT over last axis** $\to$ `np.fft.fft(x, axis=-1)`.
- **Filter across batches** $\to$ `scipy.signal.sosfiltfilt` supports batch input over one axis.
- **Compute BER across many SNR levels in one go** $\to$ build an SNR axis in broadcasting, add noise, demodulate, compute errors — all at once.
- **Stack matrix inversions** $\to$ `np.linalg.inv` works on batched matrices (`(B, N, N)` input, `(B, N, N)` output).

### When vectorization stops helping

- When your data doesn't fit in RAM (use generators, chunking, `memmap`).
- When your operation is genuinely sequential (e.g., iterative solvers with state) — use Numba, Cython, or porting to JAX/PyTorch.
- When the vectorized form allocates huge intermediates. Sometimes a chunked inner loop with smaller per-iteration work wins.

## Formal rules — broadcasting

Given two arrays with shapes $(a_1, \ldots, a_m)$ and $(b_1, \ldots, b_n)$, broadcasting succeeds iff **padding the shorter shape with 1s on the left**, each pair $(a_i, b_i)$ satisfies $a_i = b_i$ OR $a_i = 1$ OR $b_i = 1$. The output shape is the elementwise max of the two. The size-1 axis gets "stretched" (actually: strided with stride 0 — no memory copy).

Learning broadcasting solidly pays for itself inside an hour.

## Why it matters / when you use it

- **Training time.** DL experiments live or die on iteration speed. Vectorized NumPy/PyTorch preprocessing shaves hours off.
- **Sim-sweep speed.** Wireless sim sweeps over SNR $\times$ code rate $\times$ channel model $\times$ trial index are a 4D broadcast; vectorization turns them from overnight jobs into minutes.
- **Career signal.** The quality of your vectorization is visible in any code you ship.

## Common mistakes

- **`.append` in a loop to grow an array.** NumPy arrays aren't Python lists — appending reallocates. Pre-allocate or use a list + `np.stack` at the end.
- **Unintended broadcasting.** `a + b` where one has shape $(N,)$ and one $(N,1)$ *silently* produces $(N,N)$. Use explicit shape tests.
- **Float vs int broadcasting.** Promotes to float; silently ups memory. Watch dtypes.
- **Copying when views would do.** `arr[::2]` is a view; `arr[list_of_indices]` is a copy.

## Reading order

1. CS231n NumPy tutorial — one dense hour.
2. [[textbook-from-python-to-numpy]] — Rougier; the definitive free text on vectorization.
3. Rougier's 100 NumPy exercises (1-star and 2-star).
4. Anytime you write a Python `for` loop over a NumPy array — **stop and ask whether you can vectorize it.**

## Related
- [[pytorch]] — same vectorization mental model (tensors instead of ndarrays).
- [[textbook-from-python-to-numpy]]
- [[textbook-scientific-visualization-matplotlib]]
- [[python-ml-wireless]]
