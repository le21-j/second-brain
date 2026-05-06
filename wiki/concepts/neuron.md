---
title: Neuron (Artificial)
type: concept
course:
  - "[[eee-404]]"
tags: [neural-network, mlp, perceptron, dsp, eee-404]
sources:
  - "[[summary-eee-404-m6-neural-networks]]"
created: 2026-04-29
updated: 2026-05-06
---

# Neuron (Artificial)

## In one line
A **neuron** computes a weighted sum of its inputs, adds a bias, and applies a nonlinear activation — the atomic building block of every neural network.

## Example first

A 2-input neuron with $w_1 = 0.5$, $w_2 = -0.3$, $b = 0.1$, ReLU activation. Inputs $x_1 = 2$, $x_2 = 1$.

1. Weighted sum: $(0.5)(2) + (-0.3)(1) = 1 - 0.3 = 0.7$.
2. Add bias: $0.7 + 0.1 = 0.8$.
3. Apply activation: $\text{ReLU}(0.8) = \max(0, 0.8) = 0.8$.

**Output: 0.8.**

If instead $x_1 = 0.1, x_2 = 5$, the pre-activation is $(0.5)(0.1) + (-0.3)(5) + 0.1 = 0.05 - 1.5 + 0.1 = -1.35$, and $\text{ReLU}(-1.35) = 0$ — the negative pre-activation gets clipped.

## The idea

Inspired loosely by biological neurons. Three operations, in order:

1. **Weighted sum** $z = \sum_j w_j x_j$ — a linear combination of inputs.
2. **Bias** $z + b$ — a per-neuron offset that lets the neuron activate even when all inputs are zero.
3. **Activation** $\text{out} = f(z + b)$ — a nonlinear function. Without nonlinearity, stacking neurons gives only a linear map; nonlinearity is what makes deep networks more expressive than shallow ones.

## Formal definition

$$\text{out} = f\!\left(\sum_{j=1}^{N_\text{in}} w_j x_j + b\right)$$

In vector form: $\text{out} = f(\vec w^\top \vec x + b)$.

## Activation functions you must know for EEE 404

| Name | Formula | Range | Notes |
|---|---|---|---|
| ReLU | $\max(0, y)$ | $[0, \infty)$ | Default in EEE 404 labs and exam problems |
| Sigmoid | $\sigma(y) = \dfrac{1}{1 + e^{-y}}$ | $(0, 1)$ | Smooth; vanishing gradient at extremes |
| Tanh | $\dfrac{e^y - e^{-y}}{e^y + e^{-y}}$ | $(-1, 1)$ | Zero-centered version of sigmoid |
| Identity | $y$ | $\mathbb R$ | Linear output layer for regression |

## Why it matters / when you use it

- **Every** MLP, CNN, RNN, transformer is built out of neurons.
- The **forward-pass equation** above is the only thing you compute on Exam 2 Problem 1 — and on the EC ML lab.
- The combination of "weighted sum + bias + nonlinearity" is what gives neural networks their universal-function-approximation property.

## Common mistakes

- **Forgetting the bias.** Each neuron has its own bias; don't reuse one across neurons.
- **Skipping the activation.** "Pre-activation" $z + b$ is not the neuron's output — apply $f$.
- **Negative pre-activation passing through ReLU.** $\text{ReLU}(-0.049) = 0$, not $-0.049$. Always check signs.
- **Wrong weight indexing in diagrams.** Convention: weight $w_{i \to j}$ is on the wire from neuron $i$ to neuron $j$.

## Related

- [[mlp]] — stacking many neurons in layers
- [[forward-propagation]] — running an MLP forward
- [[backpropagation]] — training (gradient descent on weights and biases)
- [[relu]], [[sigmoid]], [[tanh]] — activation functions
- [[eee-404-exam-2-walkthrough]] — Problem 1 walks a 2-2-2 MLP
- [[eee-404-ec-ml-walkthrough]] — 3-9-6 MLP trained on STM32

## Practice
- Exam 2 Practice Problem 1
