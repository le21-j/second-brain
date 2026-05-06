---
title: EEE 404 Module 6 — Neural Networks (slide deck summary)
type: summary
source_type: slides
source_path: raw/slides/eee-404/m6-nn-1-introduction.pdf
source_date: 2026-04-29
course:
  - "[[eee-404]]"
tags: [eee-404, neural-network, mlp, perceptron, backpropagation, training]
created: 2026-04-29
---

# EEE 404 Module 6 — Neural Networks

**Source:** 6 PDFs in `raw/slides/eee-404/m6-nn-*.pdf` (covering ~145 slides total):

| Slide deck | Path |
|---|---|
| Introduction to Neural Networks | `m6-nn-1-introduction.pdf` |
| Multi-Layer Perceptron (MLP) | `m6-nn-2-mlp.pdf` |
| MLP Example and Interpretation | `m6-nn-3-mlp-example-and-interpretation.pdf` |
| Training: Introduction | `m6-nn-4-training-introduction.pdf` |
| Forward vs Backward Propagation | `m6-nn-5-forward-vs-backward-propagation.pdf` |
| Execution and Training (worked example) | `m6-nn-6-execution-and-training.pdf` |

## TL;DR
The Machine Learning module of EEE 404 introduces the multi-layer perceptron (MLP), the forward-propagation computation, and how training adjusts weights via gradient descent (backprop). Activation function defaulted to ReLU. The lab follow-up is the **EC ML lab** — train a 3-9-6 MLP on STM32 to implement boolean functions.

## Key takeaways
- **Neuron model.** $\text{out} = f\!\left(\sum w_j x_j + b\right)$. Three steps: weighted sum, bias, activation. See [[neuron]].
- **MLP topology** notation: `[N_in, N_h, N_out]`. Parameter count: $N_i N_h + N_h N_o$ weights, $N_h + N_o$ biases. See [[mlp]].
- **Activations.** ReLU $\max(0, y)$ — default. Sigmoid $1/(1+e^{-y})$. Tanh. See [[relu]].
- **Forward propagation** = layer-by-layer evaluation, hidden first, then output. See [[forward-propagation]].
- **Backpropagation** = chain rule for gradients, propagated from output back to input. See [[backpropagation]].
- **Training loop:** sample mini-batch → forward pass → loss → backward pass → gradient-descent update on weights and biases.

## Concepts introduced
- [[neuron]] — atomic unit
- [[mlp]] — stacked layers
- [[relu]] — default activation in EEE 404
- [[forward-propagation]] — inference
- [[backpropagation]] — training (high-level only)

## Worked example (from slides)
The MLP slides include a 2-2-2 forward-pass example that mirrors **Exam 2 Practice Problem 1** almost exactly. See the [[eee-404-exam-2-walkthrough|walkthrough P1]] for a fully worked version.

## Lab tie-in
[[eee-404-ec-ml-walkthrough]] — train a 3-9-6 MLP for XOR-XOR on STM32 using these concepts.

## Questions raised
- Why ReLU over sigmoid in EEE 404? (Cheaper; no vanishing gradient; default in modern deep learning.)
- Is the 2000-epoch budget enough for non-trivial XOR variants? (Yes for XOR-XOR; harder problems would need 5000+.)
