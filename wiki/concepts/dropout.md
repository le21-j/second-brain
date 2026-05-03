---
title: Dropout
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - dropout
  - regularization
  - foundations
  - dl
sources:
  - "[[textbook-prince-understanding-deep-learning]]"
created: 2026-05-01
updated: 2026-05-01
---

# Dropout

## In one line
During training, **randomly zero a fraction $p$ of activations on each forward pass.** Forces the network to not rely on any single neuron — a stochastic ensemble that improves generalization at almost no implementation cost. Hinton et al. 2012; Srivastava et al. 2014.

## Example first

Dense layer outputs activation vector $\mathbf{a} = (1.0, 2.0, 3.0, 4.0, 5.0)$.

**Training:** Drop with $p = 0.5$. Sample binary mask $\mathbf{m} \sim \text{Bernoulli}(0.5)$ — say $\mathbf{m} = (1, 0, 1, 1, 0)$. Apply, then **rescale** to keep expected activation:
$$\mathbf{a}' = \mathbf{a} \odot \mathbf{m} / (1-p) = (2.0, 0, 6.0, 8.0, 0).$$

The scaling by $1/(1-p) = 2$ is the **inverted dropout** trick — keeps the activation scale unchanged on average so no further calibration is needed at test time.

**Inference:** Mask becomes all-ones; no dropout applied; activations are deterministic.

PyTorch:
```python
self.dropout = nn.Dropout(p=0.5)
def forward(self, x):
    x = self.fc(x)
    x = F.relu(x)
    x = self.dropout(x)   # only active when model.train()
    return x
```

## The idea

Without dropout, neurons can co-adapt: neuron $i$ specializes to "fix" the consistent error of neuron $j$. The network becomes brittle — the units don't independently encode useful features.

Dropout breaks the co-adaptation:
1. On each minibatch, a random subset of neurons is "absent."
2. Surviving neurons must produce a useful activation **on their own**.
3. Over many minibatches, every neuron learns to be useful when alone.

**Geometric interpretation.** Dropout trains a **Bayesian-ensemble approximation**: each minibatch trains a different sub-network; inference averages their predictions. This is the rigorous justification (Gal & Ghahramani 2016).

### Where to apply dropout
- **After activation, before the next linear layer.** Standard.
- **Inside attention** — modern transformers apply dropout to the attention weights (after softmax) and to MLP activations.
- **Not on the output layer.** Don't dropout the final logits.
- **Not on convolution feature maps for image tasks** (use SpatialDropout/Dropout2D) — dropping individual pixels doesn't break co-adaptation across the channel dimension.

### Typical values
| Architecture | Dropout $p$ |
|---|---|
| Fully-connected MLP, small dataset | 0.5 |
| CNN (conv layers) | 0.1–0.2 |
| Transformer attention/MLP | 0.1 |
| Output layer | 0 |

## Formal definition

For activation vector $\mathbf{a}$ during training:
$$\mathbf{a}' = \mathbf{a} \odot \frac{\mathbf{m}}{1-p}, \quad m_i \sim \text{Bernoulli}(1-p) \text{ i.i.d.}$$
At inference: $\mathbf{a}' = \mathbf{a}$.

This is **inverted dropout** — scale at training so no scaling needed at inference. PyTorch implements this by default.

## Why it matters

- **Effective regularization** with no extra parameters or compute (just a random mask).
- **Implicit ensemble.** Trains $2^n$ subnetworks (where $n$ = number of activations) and averages them implicitly.
- **Modern transformers depend on it.** GPT, BERT, every transformer in [[python-ml-wireless]] uses dropout.
- **Small-data regimes.** Wireless-ML datasets are often small; dropout helps generalize.

## Common mistakes

- **Forgetting `model.eval()` at inference.** Without it, dropout is still active — predictions become non-deterministic. Always `model.eval()` before evaluation.
- **Tuning $p$ as if it's the most important hyperparameter.** It's important but not paramount. Default $p=0.1$ for transformers, $p=0.5$ for FC layers, then move on.
- **Using dropout where it doesn't help.** Dropout in BatchNorm-heavy networks is often redundant — BN already provides stochastic regularization.
- **Naive dropout in conv layers.** Use Dropout2D / SpatialDropout to drop entire feature maps, not individual pixels.

## Variants worth knowing
- **DropConnect** — randomly zero **weights** instead of activations.
- **Variational dropout** — Bayesian-grounded; learns dropout rates per parameter.
- **Stochastic depth** — drop entire residual blocks (used in ResNet variants).
- **DropBlock** — drop contiguous regions of feature maps in CNNs.

## Related
- [[regularization]] — the umbrella concept.
- [[batch-normalization]] — alternative regularization mechanism; partially overlapping.
- [[transformer]] — uses dropout extensively.
- [[textbook-prince-understanding-deep-learning]] — Ch 9.1.
- [[python-ml-wireless]] — Phase 1, Prince Ch 9.

## Practice
- Train an MLP on MNIST with $p \in \{0, 0.1, 0.3, 0.5, 0.7\}$; plot train + val accuracy.
- Verify the inverted-dropout scaling: with `nn.Dropout(p=0.5)`, the mean activation in train mode equals the mean in eval mode.
- Implement Monte Carlo dropout (keep dropout active at inference, sample 100 forward passes) for uncertainty estimation.
