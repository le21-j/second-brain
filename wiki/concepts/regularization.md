---
title: Regularization
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - regularization
  - generalization
  - foundations
  - dl
sources:
  - "[[textbook-prince-understanding-deep-learning]]"
created: 2026-05-01
updated: 2026-05-01
---

# Regularization

## In one line
**Anything that improves validation performance at the expense of training performance.** The umbrella term for techniques that prevent a model from memorizing training data so it generalizes to new data — weight decay, [[dropout]], data augmentation, early stopping, and the implicit regularization of [[stochastic-gradient-descent]].

## Example first

Train a 100-parameter polynomial on 20 points. Without regularization, the model fits every training point perfectly — and predicts wildly between them. **L2 regularization** (a.k.a. weight decay) adds a $\lambda \|\theta\|^2$ penalty to the loss:

$$L_{\text{total}} = L_{\text{data}}(\theta) + \lambda \|\theta\|^2.$$

With $\lambda = 0.1$, the polynomial smooths out — train MSE goes up, validation MSE goes down. That's the regularization trade-off in one picture.

In PyTorch:
```python
opt = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-2)
```

## The idea

Deep networks have **far more parameters than training examples**. Without intervention, they memorize. Regularization techniques bias the optimization toward "simpler" solutions — where simpler is operationally defined as:

| Technique | What "simple" means |
|---|---|
| **L2 / weight decay** | small weights |
| **L1** | sparse weights |
| **[[dropout]]** | not over-reliant on any single neuron |
| **[[batch-normalization]]** | activations don't drift |
| **Early stopping** | stop before memorization |
| **Data augmentation** | invariant to label-preserving transforms |
| **Mixup / CutMix** | linearly compose training samples |
| **Label smoothing** | don't be 100% confident |
| **SGD noise** | implicit regularization (small batch helps) |

These are all instantiations of a single Bayesian intuition: **prior over simpler models reduces overfitting**.

### L1 vs L2
| | L1 (Lasso) | L2 (Ridge / weight decay) |
|---|---|---|
| Penalty | $\lambda \sum |\theta_i|$ | $\lambda \sum \theta_i^2$ |
| Geometry | corners of $\ell_1$ ball | sphere |
| Effect | drives weights to **exactly 0** (sparse) | shrinks toward 0 (small but non-zero) |
| Use | feature selection | generic shrinkage; default in DL |

### Weight decay vs L2 regularization (subtle)
In **plain SGD**, weight decay and L2 penalty are equivalent. In **adaptive optimizers like Adam**, they differ — the L2-in-the-loss interacts with the per-parameter learning rate scaling. **AdamW** decouples them: weight decay is applied directly to $\theta$, not as a gradient. **Always use AdamW with weight decay.**

## Formal definition

A regularized objective is
$$L_{\text{total}}(\theta) = L_{\text{data}}(\theta) + \lambda R(\theta),$$
where $R$ is the regularizer and $\lambda > 0$ is the regularization strength.

In Bayesian terms, this is **MAP estimation** with prior $p(\theta) \propto e^{-\lambda R(\theta)}$:
- L2 corresponds to a Gaussian prior.
- L1 corresponds to a Laplace prior.
- Dropout corresponds to a specific spike-and-slab prior approximation.

## Why it matters

- **Generalization is the actual goal of ML.** Training loss is a means; test loss is the end. Regularization is the bridge.
- **Modern DL models depend on it.** Transformers without dropout + weight decay don't generalize; ResNets without batch-norm don't train.
- **Wireless-ML data is small** — channel measurements, real-world labels are scarce. Regularization is essential at this data scale.

## Common mistakes

- **Tuning $\lambda$ on the test set.** $\lambda$ is a hyperparameter — tune on validation, not test. Test set is the final number.
- **Forgetting that BatchNorm regularizes.** A model with BN often needs less dropout. Don't stack regularization techniques without measuring their joint effect.
- **L2 with biases.** Regularizing bias terms is usually unhelpful. PyTorch's `weight_decay` applies to all parameters; manual setups often exclude biases and norm parameters.
- **Confusing weight decay with L2 in Adam.** As above — use AdamW.
- **Stopping too early.** Early stopping can underfit; check that val loss has actually plateaued, not just hit a local plateau.

## Related
- [[dropout]] — randomly zero activations during training.
- [[batch-normalization]] — implicitly regularizes via stochastic-batch statistics.
- [[overfitting-bias-variance]] — what regularization fights.
- [[stochastic-gradient-descent]] — implicit regularization through gradient noise.
- [[adam-optimizer]] — pair with AdamW for proper weight decay.
- [[textbook-prince-understanding-deep-learning]] — Ch 9 is the canonical reference.
- [[python-ml-wireless]] — Phase 1, Prince Ch 9.

## Practice
- For an over-parameterized polynomial on synthetic data, sweep $\lambda \in \{0, 0.001, 0.01, 0.1, 1.0, 10\}$ and plot train + val loss.
- Train ResNet-18 on CIFAR-10 with vs. without weight decay; report val accuracy.
- Train a transformer with dropout=0 vs. dropout=0.1 and observe training-vs-val curves.
