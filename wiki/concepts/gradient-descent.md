---
title: Gradient descent
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - optimization
  - gradient-descent
  - foundations
  - dl
sources:
  - "[[textbook-prince-understanding-deep-learning]]"
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-05-01
updated: 2026-05-01
---

# Gradient descent

## In one line
Walk downhill. To minimize a function $f(\theta)$ of parameters $\theta$, compute the gradient $\nabla f$ (the direction of steepest ascent) and step in the **opposite** direction: $\theta \leftarrow \theta - \eta \nabla f(\theta)$. The whole of deep-learning training is variations on this one rule.

## Example first

**Minimize $f(\theta) = (\theta - 3)^2$ from a starting guess $\theta = 0$.**

The gradient is $f'(\theta) = 2(\theta - 3)$. Pick learning rate $\eta = 0.1$:

| Step | $\theta$ | $f(\theta)$ | $f'(\theta)$ | Update |
|---|---|---|---|---|
| 0 | 0.0 | 9.0 | -6.0 | $\theta \leftarrow 0 - 0.1\cdot(-6) = 0.6$ |
| 1 | 0.6 | 5.76 | -4.8 | $\theta \leftarrow 0.6 + 0.48 = 1.08$ |
| 2 | 1.08 | 3.69 | -3.84 | $\theta \leftarrow 1.46$ |
| 5 | 2.21 | 0.62 | -1.57 | $\theta \leftarrow 2.37$ |
| 20 | 2.97 | 0.0008 | -0.06 | $\theta \leftarrow 2.97$ |

Converges to $\theta = 3$. Same algorithm in PyTorch:

```python
theta = torch.tensor([0.0], requires_grad=True)
opt = torch.optim.SGD([theta], lr=0.1)
for _ in range(50):
    loss = (theta - 3)**2
    opt.zero_grad()
    loss.backward()
    opt.step()
```

## The idea

A neural network's loss $L(\theta)$ is a function of millions of parameters. We can't solve $\nabla L = 0$ in closed form — the surface is too high-dimensional and non-convex. So we **iterate**: at each step, evaluate $\nabla L$ at the current $\theta$, then take a small step in the direction that decreases $L$ the most.

The **learning rate** $\eta$ controls step size. Too large: overshoot, diverge. Too small: takes forever. Picking $\eta$ is the single most important hyperparameter in deep learning.

### The two questions every gradient-descent variant answers
1. **What gradient do we compute?** Full-batch ($\nabla L$ over the whole dataset, expensive but exact) → mini-batch ($\nabla L$ over a small subset, noisy but cheap) → stochastic ($\nabla L$ over a single sample, noisiest but cheapest). See [[stochastic-gradient-descent]].
2. **What direction do we step?** Plain $-\nabla L$ (pure gradient descent) → momentum-augmented (smooth across steps) → adaptive ($\eta$ per parameter, scaled by historical gradient magnitudes — [[adam-optimizer]]).

## Formal definition

Given a differentiable loss $L: \mathbb{R}^d \to \mathbb{R}$ and a starting point $\theta_0$, gradient descent iterates:

$$\theta_{t+1} = \theta_t - \eta\, \nabla L(\theta_t)$$

with learning rate $\eta > 0$. Under standard assumptions (Lipschitz continuous gradient, convex $L$), gradient descent converges to a global minimum at rate $O(1/t)$. For non-convex $L$ (most neural nets), it converges to a critical point — usually a "good" local minimum or saddle.

## Why it matters / when you use it

- **Training every neural network.** You will not write a model that doesn't use some variant of GD.
- **Backbone of all modern optimizers.** [[adam-optimizer]], RMSprop, Adagrad, AdamW are all gradient descent with smarter step rules.
- **Connects to maximum-likelihood estimation.** Minimizing negative-log-likelihood = MLE = a gradient-descent procedure on the loss surface.

## Common mistakes

- **Wrong sign.** $\theta \leftarrow \theta + \eta \nabla L$ goes uphill — this is the most common student bug. The minus sign is non-negotiable.
- **Learning rate too high.** Loss spikes, then NaN. Cure: reduce $\eta$ by 3–10×.
- **Learning rate too low.** Loss plateaus immediately. Cure: increase $\eta$, use a learning-rate finder (Smith 2017).
- **Forgetting to zero gradients.** PyTorch accumulates `.grad` across `.backward()` calls. Always `optimizer.zero_grad()` before computing the next gradient.
- **Confusing batch and full-batch.** "Gradient descent" without qualification usually means full-batch in classical ML, mini-batch in DL. In practice you almost always mean **stochastic gradient descent** ([[stochastic-gradient-descent]]).

## Related
- [[stochastic-gradient-descent]] — the cheap-noisy version everyone actually uses.
- [[adam-optimizer]] — the adaptive-learning-rate descendant that's the modern default.
- [[backpropagation]] — how $\nabla L$ is actually computed for a deep network.
- [[mse-loss]], [[cross-entropy-loss]] — the loss functions $L$ that gradient descent minimizes.
- [[overfitting-bias-variance]] — what happens when GD finds a too-good fit on training data.
- [[python-ml-wireless]] — Phase 1 Month 4 reading, Prince Ch 6.

## Practice
- Implement gradient descent from scratch on $f(\theta) = (\theta - 3)^2$, then on the 2D Rosenbrock function. Plot the trajectory.
- Sweep $\eta \in \{0.001, 0.01, 0.1, 1.0, 10.0\}$ and observe divergence / convergence.
