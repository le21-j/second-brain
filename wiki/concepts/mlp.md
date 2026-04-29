---
title: Multi-Layer Perceptron (MLP)
type: concept
course: [[eee-404]]
tags: [neural-network, mlp, perceptron, deep-learning, eee-404]
sources: [[summary-eee-404-m6-neural-networks]]
created: 2026-04-29
updated: 2026-04-29
---

# Multi-Layer Perceptron (MLP)

## In one line
An **MLP** is a feed-forward neural network: an input layer, one or more hidden layers of [[neuron|neurons]], and an output layer — every neuron in layer $\ell$ connects to every neuron in layer $\ell+1$.

## Example first

A **2-2-2 MLP** (2 inputs, 1 hidden layer with 2 neurons, 2 outputs). With weights $w_{ih}$ from input $i$ to hidden $h$, biases $b_h$ on each hidden neuron, then $w_{ho}$ and $b_o$ for the output layer:

1. **Hidden layer:** $H_1 = f(w_{1,1} X_1 + w_{2,1} X_2 + b_{H_1})$, $H_2 = f(w_{1,2} X_1 + w_{2,2} X_2 + b_{H_2})$.
2. **Output layer:** $Y_1 = f(w_{1,1}' H_1 + w_{2,1}' H_2 + b_{O_1})$, $Y_2 = f(w_{1,2}' H_1 + w_{2,2}' H_2 + b_{O_2})$.

This is exactly Exam 2 Practice Problem 1. With ReLU activations and the weights from the diagram, the answer is $H_1 = 0.185, H_2 = 0.3, Y_1 = 0.6025, Y_2 = 0$.

## The idea

Each layer applies $\vec h = f(W \vec x + \vec b)$ to its inputs, and the output of one layer feeds the next. Stacking nonlinear transformations is what lets the network learn complex input-output mappings.

**Notation:**
- Topology $[N_\text{in}, N_\text{h}, N_\text{out}]$ — e.g., $[3, 9, 6]$ in the EEE 404 EC ML lab.
- $W^{(\ell)}$ — weight matrix between layer $\ell-1$ and layer $\ell$. Shape $N_\ell \times N_{\ell-1}$.
- $\vec b^{(\ell)}$ — bias vector for layer $\ell$. Length $N_\ell$.

## Formal definition

For an $L$-layer MLP (input + $L-1$ hidden + 1 output):
$$\vec h^{(\ell)} = f^{(\ell)}\!\left(W^{(\ell)} \vec h^{(\ell-1)} + \vec b^{(\ell)}\right), \quad \ell = 1, 2, \dots, L$$
with $\vec h^{(0)} = \vec x$ (the input).

**Parameter count for a 1-hidden-layer MLP** with topology $[N_i, N_h, N_o]$:
- Weights: $N_i \cdot N_h + N_h \cdot N_o$
- Biases: $N_h + N_o$

For the EC ML lab ([3, 9, 6]): $3 \cdot 9 + 9 \cdot 6 = 81$ weights, $9 + 6 = 15$ biases.

## Why it matters / when you use it

- **Universal approximator.** A 1-hidden-layer MLP with enough neurons can approximate any continuous function (Cybenko 1989).
- **The Exam 2 forward-pass problem** is one neuron-per-neuron evaluation of an MLP.
- **The EC ML lab** trains an MLP on the STM32 to learn boolean functions (XOR-AND, XOR-XOR).
- **Practical role in wireless ML:** [[neural-receiver]], [[autoencoder-phy]], [[csi-feedback]] — all built from MLPs (sometimes layered as transformers or CNNs).

## Common mistakes

- **Skipping the hidden activation.** The whole point of the MLP is the nonlinearity in the hidden layer; without it the MLP collapses to a linear map.
- **Using output values from layer $\ell+1$ as inputs to layer $\ell+2$ before applying the activation.** The output of layer $\ell+1$ is the *post-activation* value.
- **Mismatching weight indexing convention** — different textbooks use opposite conventions for $w_{ij}$. Always check whether $i$ refers to the source neuron or the target neuron.

## Related

- [[neuron]] — the atomic building block
- [[forward-propagation]] — the MLP forward computation
- [[backpropagation]] — the training algorithm
- [[relu]], [[sigmoid]], [[tanh]] — activation functions
- [[convolutional-neural-network]] — variant for spatial inputs
- [[eee-404-exam-2-walkthrough]] — P1: 2-2-2 MLP forward pass
- [[eee-404-ec-ml-walkthrough]] — 3-9-6 MLP trained on STM32

## Practice
- Exam 2 Practice Problem 1
