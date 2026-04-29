---
title: Diffusion model
type: concept
course: [[python-ml-wireless]]
tags: [diffusion, generative, dl, ddpm, score-matching]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# Diffusion model

## In one line
Train a network to **denoise** a progressively more-noised version of data; at inference, start from pure noise and iteratively denoise back to a clean sample — turning generation into a sequence of small, locally-reasonable denoising steps.

## Example first

Take a clean image $\mathbf{x}_0$. Apply Gaussian noise in $T$ small steps:

$$
\mathbf{x}_t = \sqrt{\bar\alpha_t}\,\mathbf{x}_0 + \sqrt{1 - \bar\alpha_t}\,\boldsymbol{\epsilon}, \quad \boldsymbol{\epsilon} \sim \mathcal{N}(0, I)
$$

where $\bar\alpha_t$ is a schedule from $1$ (all signal) at $t=0$ to $0$ (all noise) at $t=T$. At $t=T$, $\mathbf{x}_T$ is essentially pure noise.

**Train** a neural net $\epsilon_\theta(\mathbf{x}_t, t)$ to predict the added noise from the noised image $+$ timestep:

$$
\mathcal{L}(\theta) = \mathbb{E}_{t, \mathbf{x}_0, \boldsymbol{\epsilon}}\, \| \boldsymbol{\epsilon} - \epsilon_\theta(\mathbf{x}_t, t) \|^2
$$

**Sample** by starting from $\mathbf{x}_T \sim \mathcal{N}(0, I)$ and running the reverse process $T$ times — each step denoises a little. You get a realistic sample.

That's all DDPM is. Latent diffusion (Stable Diffusion) runs the same process in a VAE's latent space for compute efficiency.

## The idea

**Ho, Jain, Abbeel 2020** — "Denoising Diffusion Probabilistic Models" (arxiv:2006.11239). The mental model:

- **Forward process:** a fixed Markov chain that adds noise.
- **Reverse process:** a *learned* Markov chain that denoises.
- **Training = denoising.** Instead of matching a likelihood or a discriminator, train the network to predict the noise at each step. Simple MSE loss.

### Why it's winning

- **Stable training.** Pure MSE, no minimax.
- **High fidelity.** State-of-the-art on most image-generation benchmarks since 2022.
- **Flexible conditioning.** Classifier guidance, classifier-free guidance, text-to-image via CLIP/T5 cross-attention.
- **Strong likelihood estimation.** Beats GANs and often VAEs on log-likelihood metrics.

### Mathematical equivalence

Diffusion can be derived as:
- A Markov chain (the DDPM picture above).
- A **score-based model** — train a network to estimate $\nabla_\mathbf{x} \log p_t(\mathbf{x})$, the score of the noised distribution at level $t$ (Song & Ermon 2019).
- A **stochastic differential equation** (SDE) (Song et al. 2021). The discrete DDPM is a specific time discretization.

These are three views of the same object.

### Wireless applications (emerging, 2024–2026)

- **Generative channel models.** Train a diffusion model to sample from a channel distribution; use as a data source for neural-receiver pretraining.
- **Semantic communication.** Ship a compact latent over the channel; diffusion decoder reconstructs. Active research area.
- **Channel estimation priors.** Diffusion prior $+$ measurement consistency $\to$ MMSE-like channel estimator that captures real statistics.
- **Khosravirad et al. 2026** "Generative Decompression" (arxiv:2602.03505) is an Alkhateeb-collab paper using generative priors for decompression at the physical layer.

## Formal definition (DDPM)

Forward process (fixed, no learning):

$$
q(\mathbf{x}_t | \mathbf{x}_0) = \mathcal{N}(\mathbf{x}_t; \sqrt{\bar\alpha_t}\,\mathbf{x}_0, (1 - \bar\alpha_t)\,I)
$$

Parameterized reverse (learned):

$$
p_\theta(\mathbf{x}_{t-1} | \mathbf{x}_t) = \mathcal{N}(\mathbf{x}_{t-1}; \mu_\theta(\mathbf{x}_t, t), \Sigma_\theta(\mathbf{x}_t, t))
$$

The **noise-prediction parameterization** is the one people use:

$$
\mu_\theta(\mathbf{x}_t, t) = \frac{1}{\sqrt{\alpha_t}}\left(\mathbf{x}_t - \frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\,\epsilon_\theta(\mathbf{x}_t, t)\right)
$$

Training loss:

$$
\mathcal{L}_\text{simple}(\theta) = \mathbb{E}_{t, \mathbf{x}_0, \boldsymbol{\epsilon}}\, \| \boldsymbol{\epsilon} - \epsilon_\theta(\sqrt{\bar\alpha_t}\,\mathbf{x}_0 + \sqrt{1-\bar\alpha_t}\,\boldsymbol{\epsilon}, t) \|^2
$$

## Why it matters / when you use it

- **Current SOTA generative family** — image, audio, video, protein structure.
- **Emerging in wireless** — Alkhateeb-collab + NVIDIA research are both exploring generative priors.
- **Long-term bet** for 6G semantic communication.

## Common mistakes

- **Too few sampling steps.** Classic DDPM uses $1000$ steps. DDIM accelerates to $50$. Below $\sim 20$, quality drops.
- **Training on normalized inputs but sampling from $\mathcal{N}(0,1)$.** Have to match distributions.
- **Ignoring classifier-free guidance.** For any conditional diffusion model post-2022, CFG is the default.

## Reading order (per roadmap)

1. [Lilian Weng's diffusion post](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/).
2. Ho, Jain, Abbeel 2020 — DDPM.
3. Hugging Face Diffusion Course — https://huggingface.co/learn/diffusion-course.
4. Prince Ch 18 ([[prince-understanding-deep-learning]]) — the clearest textbook treatment.

## Related
- [[variational-autoencoder]]
- [[generative-adversarial-network]]
- [[python-ml-wireless]]
