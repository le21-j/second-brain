---
title: Overfitting and bias-variance
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - overfitting
  - bias-variance
  - generalization
  - foundations
  - dl
sources:
  - "[[textbook-prince-understanding-deep-learning]]"
created: 2026-05-01
updated: 2026-05-01
---

# Overfitting and bias-variance

## In one line
A model **overfits** when it memorizes training data instead of learning the underlying signal — train loss low, test loss high. **Bias-variance** decomposes generalization error into "model is too simple" (bias) and "model is too sensitive to training data" (variance). The deep-learning twist: **double descent** breaks the classical curve, and modern over-parameterized models can have low bias *and* low variance.

## Example first

Fit polynomials of degree $d$ to 20 noisy points sampled from $y = \sin(x) + \varepsilon$:

| Degree $d$ | Train MSE | Test MSE | Verdict |
|---|---|---|---|
| 1 (linear) | 0.45 | 0.43 | high bias — too simple |
| 3 (cubic) | 0.08 | 0.10 | sweet spot |
| 9 | 0.005 | 0.18 | overfitting — wiggles between points |
| 15 | 0.0001 | 0.92 | catastrophic — interpolates noise |

Plot **train MSE and test MSE vs. $d$**: train MSE decreases monotonically; test MSE forms a U-shape with minimum around $d = 3$. The minimum test MSE is the **classical bias-variance trade-off**.

## The idea

Generalization error $= $ bias$^2$ + variance + irreducible noise:

$$\mathbb{E}_{\mathcal{D}}\bigl[(y - \hat y(x; \mathcal{D}))^2\bigr] = \underbrace{(\bar y - \mathbb{E}_\mathcal{D}[\hat y])^2}_{\text{bias}^2} + \underbrace{\mathbb{E}_\mathcal{D}\bigl[(\hat y - \mathbb{E}_\mathcal{D}[\hat y])^2\bigr]}_{\text{variance}} + \sigma_\varepsilon^2.$$

| Source | What it is | Cure |
|---|---|---|
| **Bias** | model class can't represent the truth | use a more flexible model |
| **Variance** | model is sensitive to which training data it saw | more data, or regularize |
| **Noise** | irreducible | shrug |

### The classical U-shape
1. Simple models (low capacity) → high bias, low variance → high error.
2. Complex models (high capacity) → low bias, high variance → high error.
3. Sweet spot in between.

Until 2017, this was the textbook story. Then deep learning broke it.

### The double descent surprise
For massively over-parameterized models (like every modern neural network), the test-error curve has a **second descent** as you keep growing the model **past** the interpolation threshold (where train error = 0):

```
test error
   |
   |  classical regime    interpolation     modern regime
   |       /\                  ↓                /
   |      /  \                / \              /
   |     /    \              /   \            /
   |____/______\____________/_____\__________/_______→ model size
       (small)   (sweet)     (transition)    (huge → DL works)
```

For neural networks operating in the modern regime: **bigger models often generalize better**, contradicting classical bias-variance intuition. This is why GPT-4 has trillions of parameters.

## Formal definition (classical)

For an estimator $\hat y$ of true function $y(x)$ trained on dataset $\mathcal{D}$:
- **Bias:** $\mathbb{E}_\mathcal{D}[\hat y(x; \mathcal{D})] - y(x)$ — average error of the model class.
- **Variance:** $\mathbb{E}_\mathcal{D}\bigl[(\hat y(x; \mathcal{D}) - \mathbb{E}_\mathcal{D}[\hat y(x; \mathcal{D})])^2\bigr]$ — sensitivity to the random training data.

## Why it matters

- **Overfitting is the central failure mode.** Most ML failure stories trace back to overfitting in some form.
- **Validation curves are the gold standard.** Plotting train + val loss is the diagnostic for overfitting / underfitting / double-descent regime.
- **Wireless-ML data is small.** Small datasets push you toward the variance-dominated regime — regularization matters more than ever.
- **Scaling laws (Kaplan et al. 2020, Hoffmann et al. 2022).** Modern DL papers explicitly chart bias-variance-data trade-offs at scale; understanding the underlying decomposition is prerequisite.

## Common mistakes

- **Diagnosing high bias as high variance (or vice versa).** Symptoms differ:
  - **High bias:** train loss is high, val loss is high, both about equal. Underfit. Cure: bigger / different model.
  - **High variance:** train loss is low, val loss much higher. Overfit. Cure: more data, regularization, or smaller model.
- **No held-out test set.** Tuning hyperparameters on the test set silently overfits to it. Use **train/val/test** splits.
- **Confusing model capacity with epoch count.** A small model trained too long doesn't overfit because it can't — capacity is the dominant factor.
- **Trusting train loss to know when to stop.** Train loss never goes up with capacity / training time in classical settings. Always watch val loss.
- **Ignoring double descent.** A model that overfits at one size might generalize fine at 10× size — don't rule out big models.

## How to fight overfitting

| Technique | What it does |
|---|---|
| **More data** | Variance scales as $1/N$ |
| **Data augmentation** | Synthetic data variety |
| **[[regularization]]** | L2, L1 penalty |
| **[[dropout]]** | Stochastic ensemble |
| **[[batch-normalization]]** | Stabilizes activation distributions |
| **Early stopping** | Stop before memorization |
| **Smaller model** | Reduce capacity |
| **Ensemble methods** | Average multiple models |

## Related
- [[regularization]] — the umbrella for cures.
- [[dropout]], [[batch-normalization]] — specific cures.
- [[gradient-descent]] — its noise provides implicit regularization.
- [[textbook-prince-understanding-deep-learning]] — Ch 8 covers all of this.
- [[python-ml-wireless]] — Phase 1, Prince Ch 8.

## Practice
- For polynomial regression on $y = \sin(x) + \varepsilon$, plot train + val MSE vs. degree $d$ for $d \in \{1, \ldots, 20\}$.
- For an MLP on MNIST, sweep hidden width $\{16, 64, 256, 1024, 4096\}$ and observe whether double descent appears.
- Build a learning curve: for fixed model, sweep training set size $N \in \{100, 1K, 10K, 60K\}$ and plot train + val accuracy.
