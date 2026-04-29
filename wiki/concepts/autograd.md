---
title: Automatic differentiation (autograd)
type: concept
course: [[python-ml-wireless]]
tags: [autograd, dl, backprop, chain-rule]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# Automatic differentiation (autograd)

## In one line
A software system that takes any composition of elementary operations (add, multiply, matmul, relu, conv), records the ops as they execute, and — on request — runs them backwards with the chain rule to return gradients of outputs with respect to inputs.

## Example first

PyTorch autograd, minimal example:

```python
import torch

x = torch.tensor(3.0, requires_grad=True)
y = x**2 + 2*x + 1

y.backward()
print(x.grad)    # dy/dx at x=3 = 2x + 2 = 8.0
```

The critical line is `requires_grad=True`. That tells PyTorch to **record** every op applied to `x`, building a small computational graph under the hood. When you call `y.backward()`, autograd walks that graph in reverse, applies VJPs, and deposits the final gradient in `x.grad`.

## The idea

Autograd is the *implementation* of [[backpropagation]]. Two approaches:

1. **Static / define-and-run** (TensorFlow 1.x, early Theano). Build the graph explicitly; run inputs through it later. Pro: full-graph optimization. Con: Python control flow is hard.
2. **Dynamic / define-by-run** (PyTorch, JAX, TensorFlow 2.x eager, Autograd-py). The graph is built on the fly as ops execute. Pro: Python control flow just works; debugging is easy. Con: less opportunity for global optimization (partially addressed by `torch.compile`).

### Anatomy of a PyTorch autograd graph

Every tensor with `requires_grad=True` has a `grad_fn` — the function that produced it. The graph is a reverse linked-list of `grad_fn`s back to the leaves. At `.backward()` time:

1. Pick the output tensor's `grad_fn`.
2. Compute the VJP — the function's Jacobian times the incoming gradient.
3. Distribute the result to its inputs' `.grad` (if leaves) or their `grad_fn`s (if intermediate).
4. Recurse until every leaf has received its gradient.

### What autograd handles (and what it doesn't)

**Handles:** every differentiable op shipped with the framework; custom `Function`s you write; control flow (`if`, `for`) since graph is built dynamically.

**Doesn't handle (without help):**
- Discrete operations (argmax, sampling, quantization) — need straight-through estimators, Gumbel-softmax, or reparameterization.
- Non-differentiable dispatch (e.g., ray tracing with changing path topology in [[differentiable-ray-tracing]] — needs smooth approximations).

### JAX

[JAX](https://jax.readthedocs.io/) takes autograd further — composable `grad`, `jit`, `vmap`, `pmap` — and is increasingly used for wireless research that needs batched Monte-Carlo RT simulations. Sionna RT is framework-agnostic and supports JAX.

### Higher-order gradients

`torch.autograd.grad(..., create_graph=True)` lets you differentiate gradients — i.e., Hessians. Necessary for meta-learning (MAML), second-order optimizers, and physics-informed NNs.

## Formal definition

Given a function $f: \mathbb{R}^n \to \mathbb{R}^m$ decomposed as a DAG of elementary ops, autograd computes:
- **Forward mode**: Jacobian-vector product $Jv$, cost $\sim O(\text{fwd})$, efficient when $n \leq m$.
- **Reverse mode**: vector-Jacobian product $v^\top J$, cost $\sim O(\text{fwd})$, efficient when $n \geq m$ — the DL case (scalar loss, many params).

## Why it matters / when you use it

- **Makes DL feasible.** Without autograd, writing a training loop means writing a custom backward pass for every architecture — impractical.
- **Enables [[differentiable-ray-tracing]]** — Sionna RT is a ray tracer where autograd flows through the rays.
- **Enables [[physical-layer-ml]]** end-to-end learning — backprop through the channel only works because Sionna's channel is an autograd-friendly op.

## Common mistakes

- **Mutating a tensor that's needed for backward.** PyTorch throws `RuntimeError: one of the variables needed for gradient computation has been modified`. Use non-in-place ops.
- **Leaf vs non-leaf confusion.** `x + 0` is not a leaf; `.grad` is only populated on leaves. `torch.tensor(..., requires_grad=True)` is a leaf.
- **Creating the graph in inference.** Always wrap inference with `torch.no_grad()` to skip the tracking overhead.
- **Memory blowup from caching activations.** Gradient checkpointing trades recomputation for memory.

## Reading order

1. Karpathy's **micrograd** — https://github.com/karpathy/micrograd. Build autograd from scratch.
2. PyTorch autograd docs — https://pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html.
3. [[deep-learning-with-pytorch]] Ch 5.
4. The JAX docs if you're adventurous.

## Related
- [[backpropagation]]
- [[pytorch]]
- [[differentiable-ray-tracing]]
- [[sionna]]
- [[python-ml-wireless]]
