---
title: Cross-entropy loss
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - loss-function
  - classification
  - cross-entropy
  - foundations
  - dl
sources:
  - "[[textbook-prince-understanding-deep-learning]]"
  - "[[textbook-mackay-itila]]"
created: 2026-05-01
updated: 2026-05-01
---

# Cross-entropy loss

## In one line
The negative log-probability your model assigns to the correct class. **Minimize this and you're maximizing likelihood** — the loss connects directly to information theory and statistics.

## Example first

3-class classifier on a single example with true label $y = 2$ (the second of three classes, 0-indexed). Model outputs raw logits $\mathbf{z} = (1.0, 2.5, 0.3)$.

**Step 1 — Softmax.** Convert logits to probabilities:
$$p_i = \frac{e^{z_i}}{\sum_j e^{z_j}} \implies \mathbf{p} = (0.157, 0.704, 0.139).$$

**Step 2 — Cross-entropy loss.** Take negative log of the probability assigned to the true class:
$$L = -\log p_{y=1} = -\log 0.704 = 0.351.$$

If the model had been certain ($p_1 \approx 1$), $L \to 0$. If it had been catastrophically wrong ($p_1 \approx 0$), $L \to \infty$. The loss tightly couples to model confidence.

In PyTorch (note: `CrossEntropyLoss` takes raw logits, applies softmax internally):
```python
logits = model(x)            # shape (B, num_classes), raw logits
loss = F.cross_entropy(logits, y)   # y is class indices (B,)
```

## The idea

Given a one-hot true distribution $\mathbf{q}$ (1 at the true class, 0 elsewhere) and a predicted distribution $\mathbf{p}$, the **cross-entropy** is:
$$H(\mathbf{q}, \mathbf{p}) = -\sum_i q_i \log p_i.$$

Because $\mathbf{q}$ is one-hot, this collapses to $-\log p_{y}$ — just the negative log-prob of the true class.

### Why it's the right loss for classification
1. **Maximum likelihood.** $-\log p_y$ averaged over the dataset is the negative log-likelihood. Minimizing it = ML estimation of the model.
2. **Information theory.** $H(\mathbf{q}, \mathbf{p})$ is the average bits-to-encode-data-from-$q$-using-code-built-for-$p$. Minimizing = matching your model's distribution to the truth.
3. **Gradient is well-behaved.** $\partial L/\partial z_i = p_i - q_i$ — the prediction error. Compare MSE, whose gradient through softmax has a nasty $p(1-p)$ term that vanishes when $p$ is near 0 or 1.

### Binary classification case
For 2 classes with predicted probability $p \in [0,1]$ and binary label $y \in \{0,1\}$:
$$L = -y\log p - (1-y)\log(1-p).$$
This is **binary cross-entropy** (BCE). PyTorch: `F.binary_cross_entropy_with_logits(z, y)` — takes raw logit $z$ instead of $p$ for numerical stability.

## Formal definition

For a $C$-class classifier predicting probability vector $\mathbf{p} \in \Delta^{C-1}$ (the simplex) and one-hot target $\mathbf{q}$:
$$L_{\text{CE}}(\mathbf{p}, \mathbf{q}) = -\sum_{i=1}^{C} q_i \log p_i.$$

When $\mathbf{p}$ comes from softmax over logits $\mathbf{z}$:
$$L = -z_y + \log\sum_i e^{z_i}.$$

The second form — **logit space** — is what implementations actually compute (numerically stable via log-sum-exp).

## Why it matters

- **The default loss for classification.** Used in every image classifier, language model, and PHY-ML paper for [[modulation-classification]], CSI compression evaluation, etc.
- **Connects DL to information theory.** Through MacKay Ch 5, cross-entropy is the source-coding rate to encode the truth using the model's distribution.
- **Backbone of distillation, calibration, knowledge transfer.** All built on cross-entropy variants.

## Common mistakes

- **Applying softmax twice.** PyTorch `nn.CrossEntropyLoss` applies softmax internally — feeding it `softmax(logits)` instead of `logits` silently produces a near-uniform softmax-of-softmax distribution.
- **Computing cross-entropy from probabilities directly when $p \to 0$.** $-\log 0 = \infty$ → NaN. Use the **logit-space** form (`F.cross_entropy` or `F.binary_cross_entropy_with_logits`).
- **Confusing CE with MSE for classification.** MSE works on logits but converges much slower because of vanishing gradients near 0/1.
- **Wrong target shape.** PyTorch `cross_entropy(logits, y)` wants `y` as **class indices** (LongTensor of shape (B,)), not one-hot. `binary_cross_entropy_with_logits` wants `y` as float with same shape as logits.
- **Imbalanced classes.** Plain CE weights every example equally; with imbalanced data the rare class's loss is drowned. Use class-weighted CE or focal loss.

## Information-theoretic framing
$$L = -\log p(y \mid x; \theta) = -\log \prod_n p(y_n \mid x_n; \theta) \quad (\text{per-sample}).$$
Average over the dataset: $L = \frac{1}{N}\sum_n -\log p(y_n \mid x_n; \theta) = \text{NLL}$, the negative log-likelihood. Minimizing CE = MLE for $\theta$.

## Related
- [[mse-loss]] — the regression cousin.
- [[softmax]] — the activation that produces $\mathbf{p}$.
- [[gradient-descent]] — what minimizes $L$.
- [[modulation-classification]], [[autoencoder-phy]], [[neural-receiver]] — all use BCE/CE as training loss.
- [[textbook-mackay-itila]] — Ch 5 information-theoretic grounding.
- [[python-ml-wireless]] — Phase 1, Prince Ch 5.7.

## Practice
- Implement CE-with-logits from scratch using log-sum-exp; verify it matches `F.cross_entropy`.
- Train a 3-class softmax classifier on synthetic 2D data; visualize the loss landscape.
- For a 2-class problem, derive $\partial L_{\text{BCE}}/\partial z = \sigma(z) - y$ and verify by autograd.
