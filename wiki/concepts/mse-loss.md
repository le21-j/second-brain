---
title: MSE loss
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - loss-function
  - regression
  - mse
  - foundations
  - dl
sources:
  - "[[textbook-prince-understanding-deep-learning]]"
created: 2026-05-01
updated: 2026-05-01
---

# Mean squared error (MSE) loss

## In one line
Average squared difference between predictions and targets — $L = \frac{1}{N}\sum_n (\hat y_n - y_n)^2$. The default loss for regression, the maximum-likelihood estimator under Gaussian noise, and the error metric in nearly every wireless-channel-estimation paper.

## Example first

Predict the next channel coefficient. Model outputs $\hat y = (1.2, -0.4, 0.8)$ for true $y = (1.0, -0.5, 1.0)$:

$$L = \frac{1}{3}\bigl[(1.2-1.0)^2 + (-0.4-(-0.5))^2 + (0.8-1.0)^2\bigr] = \frac{1}{3}(0.04 + 0.01 + 0.04) = 0.03.$$

In PyTorch:
```python
loss = F.mse_loss(y_hat, y)   # mean over all elements
loss = F.mse_loss(y_hat, y, reduction='sum')   # sum (no /N)
```

## The idea

For regression — predicting a continuous-valued target — the natural loss is "how far off, on average?" Squared difference penalizes large errors **quadratically**, which:
- Encourages the model to never be wildly wrong (one big error dominates the loss).
- Has a closed-form gradient $\partial L/\partial \hat y = 2(\hat y - y)/N$ — clean, never vanishes for non-zero error.
- Corresponds to **maximum likelihood under Gaussian noise**: if $y = \hat y + \varepsilon$ with $\varepsilon \sim \mathcal{N}(0, \sigma^2)$, then maximizing $\log p(y \mid \hat y)$ is equivalent to minimizing MSE (up to constants).

### MSE vs. MAE
- **MSE** $= \frac{1}{N}\sum (\hat y - y)^2$ — Gaussian-noise MLE, sensitive to outliers.
- **MAE** $= \frac{1}{N}\sum |\hat y - y|$ — Laplace-noise MLE, robust to outliers, gradient is $\pm 1$ (constant magnitude).

Choose MSE when outliers should be heavily penalized (CSI reconstruction); MAE when outliers should be tolerated (median-style estimation).

## Formal definition

For predictions $\hat{\mathbf{y}} = (\hat y_1, \dots, \hat y_N)$ and targets $\mathbf{y}$:
$$L_{\text{MSE}}(\hat{\mathbf{y}}, \mathbf{y}) = \frac{1}{N}\sum_{n=1}^{N} (\hat y_n - y_n)^2 = \frac{1}{N}\|\hat{\mathbf{y}} - \mathbf{y}\|_2^2.$$

Equivalent to the **squared $\ell_2$ distance** divided by $N$. The square-root version is **RMSE** = $\sqrt{L}$ and is reported because it has the same units as $y$.

### NMSE — the wireless workhorse
Wireless / channel-estimation papers report **normalized MSE**:
$$\text{NMSE} = \frac{\mathbb{E}\|\hat{\mathbf{H}} - \mathbf{H}\|^2}{\mathbb{E}\|\mathbf{H}\|^2}.$$
Plotted in dB ($10\log_{10}$). The CsiNet ([[paper-csinet-wen-2018]]) headline metric.

## Why it matters

- **Default for regression.** Channel estimation, CSI compression, beam-prediction-as-regression.
- **Maximum likelihood under Gaussian noise** — directly grounded in probability.
- **The "vanilla" loss** — every other regression loss is justified by reference to MSE (Huber for outliers, log-cosh as smooth approximation, etc.).

## Common mistakes

- **Using MSE for classification.** Soft-classification with MSE on softmax output works mathematically but converges much slower than [[cross-entropy-loss]]. Don't.
- **Forgetting to normalize.** Raw MSE depends on scale of $y$ — a model that predicts $y$ with units of meters has 1000× the loss of one with units of millimeters. Use NMSE or normalize $y$.
- **Reporting MSE instead of RMSE in papers.** Reviewers want intuitive units; RMSE is what they read.
- **Outlier sensitivity.** A single outlier with large error dominates the loss. If your data has outliers, consider Huber loss or MAE.

## Related
- [[cross-entropy-loss]] — the classification counterpart.
- [[gradient-descent]] — the optimizer that minimizes $L$.
- [[csi-feedback]], [[neural-receiver]], [[autoencoder-phy]] — all use MSE / NMSE for channel-related tasks.
- [[textbook-prince-understanding-deep-learning]] — Ch 5.3 derivation from MLE.
- [[python-ml-wireless]] — Phase 1, Prince Ch 5.

## Practice
- Show that minimizing MSE with $\hat y = \theta_0 + \theta_1 x$ gives the OLS least-squares estimator for $\theta$.
- Compute NMSE in dB for a CsiNet reconstruction at compression $\gamma = 1/16$ — replicate the headline figure of [[paper-csinet-wen-2018]].
