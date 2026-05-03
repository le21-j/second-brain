---
title: Batch normalization
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - batch-norm
  - normalization
  - foundations
  - dl
sources:
  - "[[textbook-prince-understanding-deep-learning]]"
created: 2026-05-01
updated: 2026-05-01
---

# Batch normalization (BatchNorm, BN)

## In one line
**Normalize each feature to zero mean and unit variance using minibatch statistics, then re-scale and re-shift with learned parameters $\gamma, \beta$.** The single most-impactful trick for training deep networks: lets you use 10× larger learning rates, removes the need for finicky weight initialization, and acts as a stochastic regularizer. Ioffe & Szegedy 2015.

## Example first

Batch of $B = 4$ activations on a single feature: $\mathbf{a} = (5.0, 7.0, 9.0, 11.0)$.

**Step 1.** Compute batch statistics:
$$\mu = \frac{1}{4}(5+7+9+11) = 8, \qquad \sigma^2 = \frac{1}{4}\sum(a_i - 8)^2 = 5.$$

**Step 2.** Normalize:
$$\hat a_i = \frac{a_i - \mu}{\sqrt{\sigma^2 + \epsilon}} = \frac{a_i - 8}{\sqrt{5}} \approx (-1.34, -0.45, 0.45, 1.34).$$

**Step 3.** Scale + shift with learned $\gamma, \beta$:
$$y_i = \gamma\, \hat a_i + \beta.$$
If $\gamma = 1, \beta = 0$, the BN output is just $\hat a$. The learnable $\gamma, \beta$ let the network undo normalization if it wants.

PyTorch:
```python
self.bn = nn.BatchNorm1d(num_features=64)   # 1d for FC, 2d for conv
def forward(self, x):
    x = self.fc(x)
    x = self.bn(x)
    x = F.relu(x)
    return x
```

## The idea

Without BN, the distribution of activations at every layer **shifts** as previous layers update — Ioffe & Szegedy called this **internal covariate shift**. The network has to constantly re-adapt to the new input distribution at each layer, which slows training and forces small learning rates.

BN says: at each layer, normalize the activations to a fixed distribution (zero mean, unit variance) using **minibatch statistics**. Then let the network re-adjust via $\gamma, \beta$ if normalization isn't actually what it wants.

### Modern reinterpretation
Subsequent papers (Santurkar et al. 2018) showed that BN's success isn't really about covariate shift — it's about **smoothing the loss landscape**. Either way: BN works, and the empirical effects (10× larger learning rate, faster convergence, regularization) are real.

### Train vs. eval mode
- **Training:** use **minibatch** statistics. Activations are stochastic — different batches give different normalization.
- **Inference:** use **running average** of training statistics. Activations are deterministic.

This dual behavior is why `model.train()` / `model.eval()` matters for BN-containing networks.

### BN locations
- **Standard:** Linear/Conv → BN → ReLU.
- **Pre-activation ResNet:** BN → ReLU → Linear/Conv.
- **Modern transformers don't use BN** — they use [[layer-normalization]] (LN), which normalizes across feature dim per example, not across batch.

## Formal definition

For a minibatch of activations $\{a_i\}_{i=1}^{B}$ on one feature dimension:
$$\mu_\mathcal{B} = \frac{1}{B}\sum_{i=1}^{B} a_i, \quad \sigma_\mathcal{B}^2 = \frac{1}{B}\sum_{i=1}^{B}(a_i - \mu_\mathcal{B})^2,$$
$$\hat a_i = \frac{a_i - \mu_\mathcal{B}}{\sqrt{\sigma_\mathcal{B}^2 + \epsilon}}, \quad y_i = \gamma\, \hat a_i + \beta.$$

At inference, $\mu_\mathcal{B}, \sigma_\mathcal{B}^2$ are replaced by **exponential moving averages** $\mu_\text{run}, \sigma^2_\text{run}$ accumulated during training.

## Why it matters

- **Trains deeper networks.** Pre-BN, networks with $> 20$ layers were extremely hard to train. BN + ResNet (2015) unlocked 100+ layers.
- **10× larger learning rate.** Major practical effect.
- **Implicit regularization.** Stochastic minibatch means slightly noisy normalization → effect similar to [[dropout]].
- **The default in CNN architectures.** Every modern CNN uses BN.

## Common mistakes

- **Using small batches.** BN's statistics are unreliable for $B < 8$. Use **GroupNorm** or **LayerNorm** instead.
- **Forgetting `model.eval()` at inference.** Without it, BN uses minibatch statistics — works for $B = 1$ inference but with completely wrong scaling. Use `model.eval()`.
- **Mismatched train/eval BN statistics from frozen layers.** When fine-tuning with frozen layers, the BN running averages may be wrong for the new data distribution. Common gotcha.
- **Stacking BN + dropout.** Mostly redundant; BN already regularizes. Either use BN alone or dropout alone unless empirically motivated.
- **BN before activation vs after.** Usually BN-then-ReLU works; some papers prefer ReLU-then-BN. The difference is small in practice.

## Related variants
- **LayerNorm** — normalize over feature dim per example (no batch dependence). Standard in transformers.
- **GroupNorm** — normalize over groups of channels per example. Good for small batches.
- **InstanceNorm** — per-channel per-example. Used in style transfer.
- **WeightNorm** — normalize the weights instead of activations.

## Related
- [[regularization]] — BN is partly a regularizer.
- [[dropout]] — alternative regularization mechanism.
- [[gradient-descent]] — BN allows much larger learning rates.
- [[convolutional-neural-network]] — every modern CNN uses BN.
- [[transformer]] — uses LN instead of BN.
- [[textbook-prince-understanding-deep-learning]] — Ch 11.4 (Residual networks).
- [[python-ml-wireless]] — Phase 1, Prince Ch 11.

## Practice
- Train a 10-layer MLP on MNIST with vs. without BN. With small initial learning rate, BN should massively accelerate training.
- For batch size $B \in \{2, 8, 32, 128\}$, observe how BN's training stability changes; switch to GroupNorm at $B = 2$.
- Inspect the running mean / variance buffers (`bn.running_mean`, `bn.running_var`) before / after training.
