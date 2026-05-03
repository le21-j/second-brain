---
title: Stochastic gradient descent
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - optimization
  - sgd
  - foundations
  - dl
sources:
  - "[[textbook-prince-understanding-deep-learning]]"
created: 2026-05-01
updated: 2026-05-01
---

# Stochastic gradient descent (SGD)

## In one line
Gradient descent that uses **a small random batch** of training examples per step instead of the whole dataset — much cheaper per iteration, slightly noisy direction, but the noise actually helps escape sharp local minima.

## Example first

Suppose your training set has $N = 100{,}000$ examples and the loss is

$$L(\theta) = \frac{1}{N}\sum_{i=1}^{N} \ell(f_\theta(x_i), y_i).$$

**Full-batch GD** computes the gradient over all 100K examples per step — expensive, slow, exact.

**SGD with batch size 32** picks a random 32-example subset $\mathcal{B}_t$ each step:

$$g_t = \frac{1}{|\mathcal{B}_t|}\sum_{i \in \mathcal{B}_t} \nabla \ell(f_\theta(x_i), y_i), \qquad \theta_{t+1} = \theta_t - \eta\, g_t.$$

3000 steps to see the whole dataset once (one **epoch**), each 3000× cheaper than a full-batch step.

In PyTorch:
```python
loader = DataLoader(dataset, batch_size=32, shuffle=True)
for epoch in range(10):
    for x, y in loader:
        y_hat = model(x)
        loss = loss_fn(y_hat, y)
        opt.zero_grad()
        loss.backward()
        opt.step()
```

The inner loop runs once per **mini-batch**, not once per example.

## The idea

Computing $\nabla L$ over millions of examples is wasteful. The full-batch gradient is the **average** over per-example gradients — a small random sample is an unbiased estimate of that average. With batch size $|\mathcal{B}|$:

$$\mathbb{E}[g_t] = \nabla L(\theta_t), \qquad \text{Var}[g_t] \propto 1/|\mathcal{B}|.$$

So bigger batches → lower-variance estimates → smoother trajectory. But also: **2× batch = 2× compute per step** (with diminishing returns on convergence speed). The sweet spot in practice is $|\mathcal{B}| \in [32, 1024]$.

### Why noise helps
Counter-intuitively, the noise in the gradient is **a feature, not a bug**:
- Helps escape **sharp minima** that don't generalize well.
- Acts as implicit regularization (smaller batch = stronger regularization).
- Lets you use a larger learning rate than full-batch GD would tolerate.

This is why "small-batch SGD generalizes better than large-batch" became a well-known empirical observation (Keskar et al. 2017).

## Formal definition

Given training set $\{(x_i, y_i)\}_{i=1}^N$, sample mini-batch $\mathcal{B}_t \subset \{1, \dots, N\}$ of size $B$ uniformly at random (with or without replacement). Update:

$$\theta_{t+1} = \theta_t - \eta\, \frac{1}{B}\sum_{i \in \mathcal{B}_t} \nabla \ell(f_\theta(x_i), y_i).$$

Convergence rate: $O(1/\sqrt{t})$ for convex $L$ — slower than full-batch's $O(1/t)$ in iterations, but each iteration is $\sim N/B$ times cheaper.

## Why it matters

- **Default training algorithm** for every modern neural network.
- **Memory-bounded.** A batch of 32 fits in GPU memory; the full dataset doesn't.
- **Online / streaming compatible** — process examples as they arrive.

## Common mistakes

- **Confusing "epoch" and "step."** One **step** = one mini-batch update. One **epoch** = one full pass through the dataset (so $\lceil N/B \rceil$ steps).
- **Not shuffling.** If batches are correlated (e.g., consecutive examples are similar), gradient noise becomes structured and SGD's nice properties break. Always shuffle each epoch.
- **Batch size = 1 ("true SGD").** Maximum noise — slow, hard to converge. Modern practice uses mini-batches.
- **Tuning batch size and learning rate independently.** They interact: when you increase batch size by $k$, often you can scale learning rate by $\sim \sqrt{k}$ or $k$ (linear-scaling rule). Always re-tune $\eta$ when changing $B$.

## Related
- [[gradient-descent]] — the parent algorithm.
- [[adam-optimizer]] — adaptive-learning-rate variant; the modern default.
- [[backpropagation]] — how each per-example gradient is actually computed.
- [[regularization]] — SGD provides implicit regularization via gradient noise.
- [[python-ml-wireless]] — Phase 1, Prince Ch 6.2.

## Practice
- For a 2-layer MLP on MNIST, sweep batch size $\{1, 8, 32, 128, 512, 4096\}$ and observe (a) loss-vs-time curves and (b) test accuracy.
- Measure GPU utilization at each batch size — bigger isn't always faster wallclock.
