# From Python to NumPy — Nicolas Rougier

**Category:** Scientific Python (NumPy deep-dive)
**Status:** FREE online — not yet mirrored into repo
**URL:** https://www.labri.fr/perso/nrougier/from-python-to-numpy/
**GitHub:** https://github.com/rougier/from-python-to-numpy
**License:** CC BY-NC-SA 4.0
**Roadmap phase:** Phase 1 weeks 3–4 (NumPy deep-dive)

## Topic coverage
- Why vectorize — concrete side-by-side timings
- Anatomy of an array — shape, stride, dtype, contiguous vs non-contiguous
- Code vectorization — transforming loops into array ops
- Problem vectorization — reformulating entire algorithms
- Custom vectorization — structured arrays, memmaps, Numba hooks
- Beyond NumPy — Cython, JAX, PyTorch analogues

## Why it's on the roadmap
The roadmap singles this out as "the best free resource focused on vectorization, which is exactly the skill you need for DSP and ML prototyping." For someone with a DSP background doing PHY-layer ML, vectorization is the cheat code: every SIMD-friendly inner loop you avoid writing is an hour of debugging saved.

## Companion practice
- **[100 NumPy Exercises](https://github.com/rougier/numpy-100)** — drill after reading each section.
- **[Stanford CS231n Python/NumPy tutorial](https://cs231n.github.io/python-numpy-tutorial/)** — "80% of what you'll use in one dense hour."

## Concepts this book anchors
- [[numpy-vectorization]]
- [[broadcasting]]
- [[array-stride]]

## Related wiki pages
- [[python-ml-wireless]]
- [[nicolas-rougier]]
- [[scientific-visualization-matplotlib]]
