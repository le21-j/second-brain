---
title: Softmax
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - activation
  - softmax
  - classification
  - foundations
  - dl
sources:
  - "[[textbook-prince-understanding-deep-learning]]"
created: 2026-05-01
updated: 2026-05-01
---

# Softmax

## In one line
The function that turns a vector of real numbers ("logits") into a probability distribution: $p_i = e^{z_i} / \sum_j e^{z_j}$. Used at the output of every multiclass classifier; pairs with [[cross-entropy-loss]] and the resulting gradient is beautifully simple ($p - q$).

## Example first

Logits $\mathbf{z} = (2.0, 1.0, 0.1)$.

**Step 1.** Exponentiate: $(e^{2.0}, e^{1.0}, e^{0.1}) = (7.389, 2.718, 1.105)$.

**Step 2.** Sum: $7.389 + 2.718 + 1.105 = 11.212$.

**Step 3.** Normalize: $\mathbf{p} = (0.659, 0.242, 0.099)$.

The largest logit gets the largest probability, but probabilities are spread "softly" by the temperature implicit in the exponential — hence the name.

PyTorch:
```python
p = F.softmax(logits, dim=-1)            # over last axis
log_p = F.log_softmax(logits, dim=-1)    # use this with NLL for stability
```

## The idea

Softmax is the **probabilistic analogue of "argmax."** For a hard decision, you'd pick $\arg\max_i z_i$. For a soft, differentiable decision, you pick a distribution that:
- Assigns higher probability to higher logits.
- Sums to 1.
- Is smooth and differentiable (so gradients flow).

The exponential is what makes it work: small differences in logits $\to$ small differences in probabilities; large differences $\to$ extreme probabilities. **Temperature** $\tau$ scales the input: $p_i = e^{z_i/\tau}/\sum_j e^{z_j/\tau}$.
- $\tau \to 0$: approaches argmax (one-hot).
- $\tau = 1$: standard softmax.
- $\tau \to \infty$: approaches uniform.

### Why softmax + cross-entropy together
The gradient of $L_{\text{CE}}$ with respect to the logit is $\partial L / \partial z_i = p_i - q_i$ — the prediction minus the truth. Clean, never vanishes (for non-perfect predictions), and matches what intuition expects. **This is why softmax + CE is the canonical pairing for classification.**

## Formal definition

For $\mathbf{z} \in \mathbb{R}^C$:
$$\text{softmax}(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^{C} e^{z_j}}.$$

Properties:
- **Output is a probability distribution.** $p_i \geq 0$, $\sum_i p_i = 1$.
- **Translation-invariant.** $\text{softmax}(\mathbf{z}) = \text{softmax}(\mathbf{z} + c)$ for any constant $c$. **Implementations subtract $\max(\mathbf{z})$ before exponentiating** for numerical stability.
- **Smooth.** $\partial p_i / \partial z_j = p_i(\delta_{ij} - p_j)$ — the softmax-Jacobian formula.

## Why it matters

- **Multiclass classification head** in every neural network.
- **Attention mechanism** in transformers ([[attention-mechanism]]) — scaled dot-product attention applies softmax over keys.
- **Reinforcement learning** — softmax over Q-values for exploration; Boltzmann policy.
- **Mixture-of-experts gating** — softmax over expert weights.

## Common mistakes

- **Numerical overflow.** $e^{1000}$ is `inf`. Always use the **log-sum-exp** trick: subtract $\max(\mathbf{z})$ before exponentiating.
- **Applying softmax + softmax.** Confused with a "double softmax" — never useful, always wrong.
- **Forgetting which axis.** `softmax(x, dim=-1)` for class-axis output; `dim=1` for batched logits depending on your tensor shape. Triple-check.
- **Using `softmax` then `cross_entropy`.** PyTorch `F.cross_entropy` includes softmax — feeding it `softmax(z)` produces a softmax-of-softmax (almost uniform). Use raw logits.

## Related
- [[cross-entropy-loss]] — pairs naturally with softmax.
- [[attention-mechanism]] — scaled dot-product attention uses softmax.
- [[transformer]] — built on attention.
- [[textbook-prince-understanding-deep-learning]] — Ch 5.5.
- [[python-ml-wireless]] — Phase 1, Prince Ch 5.

## Practice
- Implement softmax with the log-sum-exp trick from scratch; compare numerical stability vs. naive `exp/sum(exp)`.
- Derive the Jacobian $\partial p_i / \partial z_j = p_i(\delta_{ij} - p_j)$ and verify with autograd.
- For a single example, compute the gradient of cross-entropy w.r.t. logits, and verify it equals $p - q$.
