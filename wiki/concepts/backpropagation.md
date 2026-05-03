---
title: Backpropagation
type: concept
course: [[python-ml-wireless]]
tags: [backprop, autograd, dl, training, chain-rule]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# Backpropagation

## In one line
Compute the gradient of a scalar loss with respect to every parameter in a neural network by applying the **chain rule** layer by layer, from the loss back through the network — reusing intermediate products so the full gradient costs about the same as one forward pass.

## Example first

2-layer MLP, $x \to h = \sigma(W_1 x) \to y = W_2 h$, scalar loss $L = (y - y^*)^2$.

**Forward:**

$$h = \text{sigmoid}(W_1 x), \quad y = W_2 h, \quad L = (y - y^*)^2$$

**Backward (chain rule):**

$$\frac{\partial L}{\partial y} = 2(y - y^*)$$

$$\frac{\partial L}{\partial W_2} = \frac{\partial L}{\partial y} \cdot h^\top \quad \text{(chain rule on } y = W_2 h\text{)}$$

$$\frac{\partial L}{\partial h} = W_2^\top \cdot \frac{\partial L}{\partial y} \quad \text{(backprop past the product)}$$

$$\frac{\partial L}{\partial z} = \frac{\partial L}{\partial h} \cdot \sigma'(z) \quad \text{(chain rule on } h = \sigma(z)\text{)}$$

$$\frac{\partial L}{\partial W_1} = \frac{\partial L}{\partial z} \cdot x^\top \quad \text{(chain rule on } z = W_1 x\text{)}$$

That's it. Each quantity $\partial L / \partial \text{variable}$ is called the **adjoint** of that variable. You compute adjoints by walking backwards from the loss, using the rule that the adjoint of a function output times the function's local Jacobian equals the adjoint of its input.

## The idea

**Rumelhart, Hinton, Williams 1986** are the names most associated with introducing backprop to neural-network training, though the reverse-mode automatic differentiation idea dates to the 1960s.

The key insight: in a network with $N$ parameters, computing gradients *naively* (one finite-difference estimate per parameter) is $O(N \cdot \text{forward cost})$. Backprop is $O(\text{forward cost})$ — **independent of $N$**. This is what makes training networks with billions of parameters tractable.

### The chain rule, written for DL

For a computational graph $L = f_n(f_{n-1}(\ldots f_1(x) \ldots))$, the gradient with respect to an intermediate variable $a$ in layer $k$ is:

$$
\frac{\partial L}{\partial a} = \frac{\partial L}{\partial f_n}\; \frac{\partial f_n}{\partial f_{n-1}}\; \cdots \; \frac{\partial f_{k+1}}{\partial a}
$$

Reverse-mode autodiff computes this from left to right — loss side first — so each partial Jacobian is only needed once and can be discarded.

### Backprop vs autograd

- **Backprop** is the algorithm (chain rule, reverse mode).
- **Autograd** is the *infrastructure* — a system that records the forward ops and replays them in reverse. Every DL framework has one. PyTorch's is called `torch.autograd`. See [[autograd]].

Most of the time you don't *write* backprop — autograd does it. But knowing the mechanics is essential for:
- Debugging exploding/vanishing gradients.
- Writing custom `Function`s with `.backward()` overrides.
- Reasoning about memory (backprop stores activations).
- Understanding gradient checkpointing (trade compute for memory).

### Computational and memory costs

- **Compute:** $\sim 2\times$ the forward pass.
- **Memory:** needs to hold all intermediate activations from the forward pass (until they're used in backward). Dominates memory in deep networks.
- **Mitigations:** gradient checkpointing (recompute activations on demand — trade FLOPs for RAM), mixed precision (FP16/BF16).

## Formal definition

For an operation $\mathbf{z} = f(\mathbf{x})$, the vector-Jacobian product (VJP) is:

$$
\bar{\mathbf{x}} = \bar{\mathbf{z}}^\top \, \frac{\partial f}{\partial \mathbf{x}}
$$

where $\bar{\mathbf{v}}$ denotes the adjoint of $\mathbf{v}$ (i.e., $\partial L / \partial \mathbf{v}$). Reverse-mode autodiff recursively propagates adjoints by VJPs, from loss backwards. Forward-mode autodiff does the analogous computation in the other direction (JVP), better when $N_\text{input} \ll N_\text{output}$ — but DL has $N_\text{params} \gg N_\text{loss dims}$ (loss is scalar), so reverse-mode wins.

## Why it matters / when you use it

- **Every DL training step uses backprop.** Not optional.
- **Understanding backprop demystifies training pathologies.** Vanishing gradients, exploding gradients, instability in GANs — all are backprop diagnoses.
- **Required to write custom layers** (e.g., a straight-through-estimator for quantization, which appears in neural receivers with quantized I/O).

## Common mistakes

- **Forgetting to zero gradients** (see [[pytorch]]). Gradients accumulate by default.
- **In-place ops breaking the graph.** `x.add_(1)` modifies x; if x is needed for backward, you get an error.
- **Detaching a tensor that's needed for backprop.** Use `.detach()` only when you explicitly want to stop gradient.

## Reading order

1. Karpathy, "Micrograd" notebook — https://github.com/karpathy/micrograd. **Build autograd from scratch in 100 lines.** Best pedagogy anywhere.
2. [[textbook-parr-matrix-calculus]] — one-sitting.
3. Goodfellow [[textbook-goodfellow-deep-learning]] Ch 6.5.
4. Prince [[textbook-prince-understanding-deep-learning]] Ch 7.

## Related
- [[autograd]]
- [[pytorch]]
- [[textbook-parr-matrix-calculus]]
- [[python-ml-wireless]]
