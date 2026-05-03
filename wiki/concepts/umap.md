---
title: UMAP (Uniform Manifold Approximation and Projection)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - dimensionality-reduction
  - manifold-learning
  - umap
  - visualization
  - phase-2
sources:
  - "[[paper-morais-similarity-2026]]"
created: 2026-05-01
updated: 2026-05-01
---

# UMAP (Uniform Manifold Approximation and Projection)

## In one line
**UMAP is a non-linear dimensionality-reduction algorithm that preserves local structure of high-dimensional data while remaining fast on large datasets — the modern default for visualization and as a feature step before clustering.** McInnes et al. 2018.

## Example first

```python
import umap
reducer = umap.UMAP(n_components=2, n_neighbors=15, min_dist=0.1)
X_2d = reducer.fit_transform(X)  # X: (N, 64) → (N, 2)
plt.scatter(X_2d[:,0], X_2d[:,1], c=labels)
```

Compared to t-SNE: faster, deterministic seeded, preserves global structure better.

## The idea

UMAP builds a **fuzzy graph** in high dimensions where edge weights encode local similarity (k-nearest-neighbors in the original space). Then it optimizes a low-dim layout whose graph approximates the original — using cross-entropy between the two graphs.

Key params:
- **`n_neighbors`** — local-vs-global trade-off (10–50 typical).
- **`min_dist`** — how tight clusters in the embedding can be (0.0 = tight clusters, 1.0 = diffuse).
- **`metric`** — distance function in the original space (Euclidean, cosine, Hamming, custom).

## Why it matters / where it sits in the roadmap

- **Phase 4 M11+ reading.** [[paper-morais-similarity-2026]] uses UMAP embeddings + Wasserstein distance to measure inter-dataset distance for wireless data.
- **Phase 2 M5–M6 toolkit.** Visualizing channel embeddings, latent spaces from autoencoders, modulation-classification features — UMAP is the default.
- **Library.** `umap-learn` Python package (`pip install umap-learn`).

## Common mistakes
- **Reading too much into UMAP cluster shapes.** UMAP preserves topology, not metric distances exactly. Two clusters being "close" in 2D doesn't mean they're close in original space.
- **Confusing UMAP with t-SNE conclusions.** Both are visualization tools; cluster sizes / distances are not directly interpretable.
- **`n_neighbors=2`** — too local, destroys global structure.

## Related
- [[paper-morais-similarity-2026]] — primary application in this wiki.
- [[channel-charting]] — sibling manifold-learning technique applied to wireless CSI.
- [[python-ml-wireless]]
