---
title: Christopher Bishop
type: person
tags: [ml, probabilistic, prml, microsoft]
course: [[python-ml-wireless]]
created: 2026-04-23
updated: 2026-04-23
---

# Christopher Bishop

**Affiliation:** Technical Fellow + Director, Microsoft Research AI4Science.
**Author of:** *Pattern Recognition and Machine Learning* (Springer, 2006) — "PRML."
**Earlier book:** *Neural Networks for Pattern Recognition* (1995).

## Why he matters to Jayden

PRML is the book that bridges DSP-style probabilistic reasoning and modern ML. See [[bishop-prml]] for chapter-by-chapter pointers.

Key identities from PRML that pay dividends for DSP applicants:
- Ridge regression = Bayesian linear regression = MMSE estimator (Ch 3).
- Kalman filter = linear-Gaussian HMM inference (Ch 13).
- Sum-product / belief propagation on factor graphs (Ch 8) — the identity that makes iterative decoders intelligible as ML.
- EM / variational inference (Ch 9–10) — the derivation pipeline for VAEs.

## Related
- [[bishop-prml]]
- [[murphy-pml-intro]] — modern replacement.
- [[python-ml-wireless]]
