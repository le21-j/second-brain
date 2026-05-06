---
title: EEE 404 EC Lab — Neural Network Training (XOR-XOR on STM32)
type: summary
source_type: lab
source_path: raw/labs/eee-404/ec-ml-lab_machine_learning.pdf
source_date: 2026-04-29
course:
  - "[[eee-404]]"
tags: [eee-404, lab, extra-credit, neural-network, mlp, embedded-ml, stm32]
created: 2026-04-29
---

# EC Lab — Neural Network Training (XOR-XOR)

**Source:** [`raw/labs/eee-404/ec-ml-lab_machine_learning.pdf`](../../raw/labs/eee-404/ec-ml-lab_machine_learning.pdf) (4 pages)
**Code:** `raw/labs/eee-404/ec-ml-code/code/{main.c, embeddedML.c, embeddedML.h}`
**Due:** 2026-05-02 06:59 UTC. **Worth: 10 EC points.**

## TL;DR
Train an MLP (3 inputs → 9 hidden ReLU → 6 output ReLU) on the STM32F407 board to implement a 3-input 2-output **XOR-XOR** boolean system ($\text{Out}_1 = X_1 \oplus X_2$, $\text{Out}_2 = X_2 \oplus X_3$). Provided code already trains for **XOR-AND**; the exercise is to modify the truth table. Uses Charles Zaloom's open-source [EmbeddedML](https://github.com/merrick7/EmbeddedML) library for forward-pass + backprop. Deliverable: PDF report with one IDE screenshot (breakpoint + Variables window + SWV trace) and the modified code excerpts.

## Key takeaways
- **Topology:** [3, 9, 6] = 81 weights + 15 biases.
- **Activation:** ReLU on both hidden and output layers.
- **Hyperparameters:** $\eta = 0.05, \beta = 0.01, \alpha = 0.25$ (don't change unless training fails).
- **Training loop:** 2000 epochs, 1 random pattern per epoch, all-8-pattern test every 200 epochs.
- **Modification scope:** rename `generate_xorand` → `generate_xorxor`, change `y[1]` per case; update 8 `ground_truth[1]` lines in the test block. Library files unchanged.
- **Convergence target:** `net_error_epoch < 0.05` after 2000 epochs.

## Concepts introduced or reinforced
- [[mlp]], [[neuron]], [[relu]], [[forward-propagation]] — same as Exam 2 Problem 1
- [[backpropagation]] — done by the EmbeddedML library; not derived
- **XOR is not linearly separable** — needs at least 1 hidden layer; this is why MLPs exist

## Walkthrough produced
[[eee-404-ec-ml-walkthrough]] — full per-section walkthrough + report skeleton.

## Questions this source raised
- Is the random seed reproducible? (Default: no — re-run if convergence is lucky/unlucky.)
- Could the same code train sigmoid-output for proper binary classification? (Yes — change `&relu` to `&sigmoid` in net.output_activation_function. But ReLU works for {0, 1} targets.)
