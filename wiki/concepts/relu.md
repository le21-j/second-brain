---
title: ReLU — Rectified Linear Unit
type: concept
course: [[eee-404]]
tags: [activation-function, neural-network, mlp, eee-404]
sources: [[summary-eee-404-m6-neural-networks]]
created: 2026-04-29
updated: 2026-04-29
---

# ReLU — Rectified Linear Unit

## In one line
The simplest nonlinear activation function: $\text{ReLU}(y) = \max(0, y)$ — pass through if positive, clamp to zero if negative.

## Example first

| input $y$ | $\text{ReLU}(y) = \max(0, y)$ |
|---|---|
| $-2.5$ | $0$ |
| $-0.049$ | $0$ |
| $0$ | $0$ |
| $0.185$ | $0.185$ |
| $1.7$ | $1.7$ |

The $-0.049 \to 0$ row is the **Exam 2 trap** in Problem 1 — the second output neuron's pre-activation is $-0.049$, so $Y_2 = 0$, not $-0.049$.

## The idea

A piecewise-linear function. Two pieces:
- **Active region** ($y \geq 0$): pass through. Slope = 1. Derivative = 1.
- **Inactive region** ($y < 0$): clamp to 0. Slope = 0. Derivative = 0.

The "kink" at $y = 0$ is what makes ReLU nonlinear. Without it, stacking ReLU neurons would just be stacking linear functions.

## Formal definition

$$\text{ReLU}(y) = \max(0, y) = \begin{cases} y, & y \geq 0 \\ 0, & y < 0 \end{cases}$$

**Derivative** (used in [[backpropagation]]):
$$\text{ReLU}'(y) = \begin{cases} 1, & y > 0 \\ 0, & y < 0 \end{cases}$$

(Undefined at $y = 0$; conventionally taken to be $0$ or $1$.)

## Why it matters / when you use it

- **Default activation** for hidden layers in modern MLPs and CNNs (replaces sigmoid/tanh in deep networks).
- **No vanishing gradient** in the active region (the derivative is exactly 1, not a small fraction like sigmoid's $\sigma(1-\sigma)$ that maxes at $0.25$).
- **Cheap to compute** — one comparison, no exponentials.
- **Used in EEE 404 lab** (3-9-6 NN) and Exam 2 Practice Problem 1.

### Failure mode: dead ReLU

If a neuron's weights and bias drive its pre-activation always negative, the neuron outputs 0 forever and its weights stop updating (gradient is 0). Variants like Leaky ReLU $\max(\alpha y, y)$ for small $\alpha$ avoid this.

## Common mistakes

- **Negative pre-activation passing through unclipped.** This is THE most common exam mistake.
- **Forgetting that the derivative is 0 in the inactive region.** This matters for gradient computations in backprop.
- **Mixing up "ReLU on the sum" vs. "ReLU on each input".** The activation is applied **after** the weighted sum and bias, not to each input separately.

## Related

- [[neuron]], [[mlp]] — where ReLU lives
- [[sigmoid]], [[tanh]] — alternative activations
- [[forward-propagation]], [[backpropagation]]
- [[eee-404-exam-2-walkthrough]] — P1 has the negative-pre-activation trap
- [[eee-404-ec-ml-walkthrough]] — `&relu` is the activation function used in the lab code

## Practice
- Exam 2 Practice Problem 1 (find which output is clipped to 0)
