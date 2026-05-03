---
title: Adam optimizer
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - optimization
  - adam
  - foundations
  - dl
sources:
  - "[[textbook-prince-understanding-deep-learning]]"
created: 2026-05-01
updated: 2026-05-01
---

# Adam optimizer

## In one line
**SGD with momentum + per-parameter adaptive learning rates.** Tracks two running averages — first moment (mean) and second moment (squared mean) — of past gradients, then divides the step by the root second moment so frequently-updated parameters get smaller steps and rarely-updated parameters get bigger ones. The default optimizer for almost all deep learning since 2014.

## Example first

Single parameter $\theta$, loss $L$, gradient $g_t = \partial L/\partial\theta$ at step $t$, hyperparameters $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\eta = 0.001$, $\epsilon = 10^{-8}$:

| Step $t$ | $g_t$ | $m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t$ | $v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2$ | $\hat m_t / \hat v_t$ | $\theta$ update |
|---|---|---|---|---|---|
| 1 | -2.0 | -0.20 | 0.004 | -2.0 / 2.0 | $\theta \leftarrow \theta - 0.001 \cdot (-1) = \theta + 0.001$ |
| 2 | -2.0 | -0.38 | 0.0080 | -2.0 / 2.0 | $\theta + 0.001$ |
| 3 | -1.0 | -0.46 | 0.0090 | -1.69 / 1.69 | $\theta + 0.001$ |
| 4 | 0.5 | -0.36 | 0.0094 | -1.18 / 1.30 | $\theta + 0.0009$ |

After **bias correction** $\hat m = m/(1-\beta_1^t)$, $\hat v = v/(1-\beta_2^t)$, the step is $-\eta \cdot \hat m_t / (\sqrt{\hat v_t} + \epsilon)$.

Notice: the step magnitude is roughly **$\eta = 0.001$** regardless of how big $g$ is. That's the magic — Adam **scales** every parameter to a known step size.

In PyTorch:
```python
opt = torch.optim.Adam(model.parameters(), lr=1e-3, betas=(0.9, 0.999), eps=1e-8)
```

## The idea

Plain SGD has one global learning rate $\eta$. But different parameters in a deep network see gradients of **wildly different scales** — a parameter in an output layer might see gradients $10^4\times$ larger than one in an early layer.

Adam tracks two **exponential moving averages** of the gradient:
- $m_t$ — first moment (mean) — like momentum, smooths the direction.
- $v_t$ — second moment (mean of $g^2$) — measures the historical magnitude.

The step is $-\eta \cdot \hat m_t / (\sqrt{\hat v_t} + \epsilon)$:
- If a parameter has had **large gradients consistently**, $\sqrt{v}$ is large → step size shrinks.
- If a parameter has had **small or sporadic gradients**, $\sqrt{v}$ is small → step size stays at $\sim\eta$.

This makes Adam **scale-invariant** per parameter — much less sensitive to the choice of $\eta$ than plain SGD.

## Formal definition (Kingma & Ba 2014)

At each step $t$ given gradient $g_t$:
$$
\begin{aligned}
m_t &= \beta_1 m_{t-1} + (1-\beta_1) g_t \quad \text{(first moment)}\\
v_t &= \beta_2 v_{t-1} + (1-\beta_2) g_t^2 \quad \text{(second moment)}\\
\hat m_t &= m_t / (1 - \beta_1^t) \quad \text{(bias-corrected)}\\
\hat v_t &= v_t / (1 - \beta_2^t)\\
\theta_{t+1} &= \theta_t - \eta\, \frac{\hat m_t}{\sqrt{\hat v_t} + \epsilon}
\end{aligned}
$$

Defaults: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$, $\eta = 10^{-3}$.

## Why it matters

- **The default for almost all DL since 2014.** Transformers, GANs, VAEs — all use Adam or AdamW.
- **Robust to hyperparameter choice.** $\eta = 10^{-3}$ works across a remarkable range of problems.
- **Faster early convergence than SGD.** Because adaptive scaling immediately puts every parameter at a usable step size.

## Common mistakes

- **Using vanilla Adam with weight decay.** Vanilla Adam's "weight decay" is implemented as L2 penalty in the loss, but the adaptive scaling distorts it. Use **AdamW** (Loshchilov & Hutter 2017), which decouples weight decay from the gradient — the single most important practical refinement.
- **Tuning $\beta_2$.** Don't. The defaults work. The exception: $\beta_2 = 0.95$ or $0.98$ for very long training (LLMs).
- **Forgetting bias correction.** PyTorch's Adam handles this for you, but homemade implementations frequently skip it — gives bad early-training behavior.
- **Late-training generalization gap.** Adam famously generalizes slightly worse than SGD on some image-classification benchmarks. This is why ResNet papers historically use SGD+momentum + step LR schedule. For most other tasks, Adam wins.

## Variants worth knowing
- **AdamW** — decoupled weight decay; the modern default.
- **Lion** (Chen 2023) — sign-based optimizer, less memory; emerging.
- **LAMB** — layerwise-adaptive Adam; for very large batches.
- **Adafactor** — memory-efficient (no $v$ tensor), used in T5/PaLM.

## Related
- [[gradient-descent]] — the parent algorithm.
- [[stochastic-gradient-descent]] — the simpler cousin.
- [[backpropagation]] — provides the gradients Adam consumes.
- [[regularization]] — AdamW's decoupled weight decay matters here.
- [[python-ml-wireless]] — Phase 1, Prince Ch 6.4.

## Practice
- Compare SGD ($\eta = 0.01$, momentum 0.9) vs. Adam ($\eta = 10^{-3}$) vs. AdamW on CIFAR-10 ResNet-18. Plot val-acc-vs-epoch.
- Use a learning-rate finder (Smith 2017) to identify the optimal $\eta$ for each.
