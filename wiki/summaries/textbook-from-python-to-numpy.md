---
title: "Rougier — From Python to NumPy"
type: summary
source_type: other
source_path: raw/textbook/from-python-to-numpy.md
source_date: 2017
course:
  - "[[python-ml-wireless]]"
tags:
  - textbook
  - numpy
  - vectorization
  - rougier
  - phase-1
  - reference-card-stub
created: 2026-05-01
updated: 2026-05-01
---

# Rougier — From Python to NumPy

**Status:** stub — free online at https://www.labri.fr/perso/nrougier/from-python-to-numpy/. Reference card at `raw/textbook/from-python-to-numpy.md`.

## TL;DR
**The best free resource focused on NumPy vectorization.** For a DSP-background applicant doing PHY-layer ML, vectorization is the cheat code: every SIMD-friendly inner loop you avoid writing is an hour of debugging saved. Pair with Rougier's [100 NumPy Exercises](https://github.com/rougier/numpy-100) for drill.

## Topic coverage
1. **Why vectorize** — concrete side-by-side timings.
2. **Anatomy of an array** — shape, stride, dtype, contiguous vs non-contiguous.
3. **Code vectorization** — transforming loops into array ops.
4. **Problem vectorization** — reformulating entire algorithms (the harder skill).
5. **Custom vectorization** — structured arrays, memmaps, Numba hooks.
6. **Beyond NumPy** — Cython, JAX, PyTorch analogues.

## Where it's used in the roadmap
- **Phase 1 M2** — paired with the [100 NumPy Exercises](https://github.com/rougier/numpy-100) drill.
- **Phase 1 M2 deliverable** — vectorization lessons applied directly to the OFDM-from-scratch notebook.

## Companion practice
- **[100 NumPy Exercises](https://github.com/rougier/numpy-100)** — drill after each section.
- **[Stanford CS231n Python/NumPy tutorial](https://cs231n.github.io/python-numpy-tutorial/)** — "80% of what you'll use in one dense hour."

## Concepts grounded
- [[numpy-vectorization]] — primary
- DSP cross-pollination: every FFT and digital-modulation snippet in the AirComp [[system-pipeline]] is a NumPy/PyTorch vectorization exercise

## Related
- [[python-ml-wireless]]
- [[rougier]] — author
- [[textbook-scientific-visualization-matplotlib]] — Rougier's matplotlib companion
- [[numpy-vectorization]]
