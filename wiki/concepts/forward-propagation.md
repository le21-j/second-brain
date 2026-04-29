---
title: Forward Propagation
type: concept
course: [[eee-404]]
tags: [neural-network, mlp, forward-pass, eee-404]
sources: [[summary-eee-404-m6-neural-networks]]
created: 2026-04-29
updated: 2026-04-29
---

# Forward Propagation

## In one line
Running an MLP from input to output by evaluating each layer's neurons in order — the standard "use the trained network" computation.

## Example first

For a 2-2-2 MLP with ReLU and the weights from Exam 2 Practice Problem 1:

**Inputs:** $X_1 = 0.05, X_2 = 0.1$.

1. **Hidden layer** (compute $H_1$, $H_2$ in parallel — both depend only on $X_1, X_2$):
   $$H_1 = \text{ReLU}((0.1)(0.05) + (0.3)(0.1) + 0.15) = \text{ReLU}(0.185) = 0.185$$
   $$H_2 = \text{ReLU}((0.2)(0.05) + (0.4)(0.1) + 0.25) = \text{ReLU}(0.30) = 0.30$$
2. **Output layer** (now use $H_1$ and $H_2$ as the inputs):
   $$Y_1 = \text{ReLU}((0.5)(0.185) + (0.7)(0.30) + 0.3) = \text{ReLU}(0.6025) = 0.6025$$
   $$Y_2 = \text{ReLU}((0.6)(0.185) + (0.8)(0.30) - 0.4) = \text{ReLU}(-0.049) = 0$$

**Outputs:** $Y_1 = 0.6025, Y_2 = 0$.

## The idea

Layer-by-layer evaluation. The output of layer $\ell$ is the input to layer $\ell+1$. **You can't compute layer $\ell+1$ until layer $\ell$ is done**, but within a layer all neurons are independent (perfect for parallel hardware).

## Formal definition

For an $L$-layer MLP:
$$\vec h^{(0)} = \vec x \quad\text{(input)}$$
$$\vec h^{(\ell)} = f^{(\ell)}\!\left(W^{(\ell)} \vec h^{(\ell-1)} + \vec b^{(\ell)}\right), \quad \ell = 1, 2, \dots, L$$
$$\vec y = \vec h^{(L)} \quad\text{(output)}$$

In code (matches the EmbeddedML library used in the EC ML lab):
```c
// for each layer ell:
//     for each neuron j in layer ell:
//         z = bias[j];
//         for each input i to neuron j:
//             z += weight[i,j] * input[i];
//         output[j] = activation(z);
```

## Why it matters / when you use it

- **Inference / prediction.** Anytime you ask the network "what's the output?" — that's forward propagation.
- **Training preamble.** Backprop starts by running forward propagation to compute the loss.
- **Exam 2 Problem 1** is just forward propagation by hand.
- **EC ML lab** calls `run_ann()` (forward-only, no weight update) to test trained network.

## Common mistakes

- **Skipping a layer.** Don't compute the output layer using $\vec x$ directly — go through hidden first.
- **Forgetting to apply the activation** at intermediate layers.
- **Reusing the same activation for hidden and output** when the problem specifies different ones (e.g., ReLU hidden + sigmoid output for binary classification).

## Related

- [[neuron]], [[mlp]] — the components
- [[backpropagation]] — the gradient counterpart
- [[relu]], [[sigmoid]], [[tanh]]
- [[eee-404-exam-2-walkthrough]] — Problem 1
- [[eee-404-ec-ml-walkthrough]] — `run_ann()` = forward propagation

## Practice
- Exam 2 Practice Problem 1
