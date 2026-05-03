---
title: Variational autoencoder (VAE)
type: concept
course: [[python-ml-wireless]]
tags: [vae, generative, dl, latent, kingma]
sources: [[paper-kingma-2013-vae]], [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# Variational autoencoder (VAE)

## In one line
An autoencoder trained to compress each input into a *distribution* (Gaussian with learned mean and variance) instead of a single point, with a KL-divergence penalty that keeps that distribution close to a standard Gaussian — giving you a generative model with a smoothly interpretable latent space.

## Example first

Train a VAE on MNIST. After training, pick any point $\mathbf{z} \in \mathbb{R}^{16}$ in latent space and ask the decoder to generate an image. Because the latent space was regularized to look like a standard Gaussian, **any random draw from $\mathcal{N}(0, I)$ produces a plausible digit**. Interpolating between the latents of a "3" and an "8" produces a smooth morph through realistic intermediate digits.

Contrast with a plain autoencoder: its latent space has no prior, so random latents produce garbage, and interpolations are arbitrary.

## The idea

**Kingma & Welling 2013**, "Auto-Encoding Variational Bayes" (arxiv:1312.6114). The VAE is the marriage of two things:
- **Variational inference** (from Bayesian statistics — approximate an intractable posterior with a tractable family).
- **Stochastic gradient descent** (via the reparameterization trick).

### The generative model

Assume data $\mathbf{x}$ is generated from latent $\mathbf{z}$:

$$
\mathbf{z} \sim p(\mathbf{z}) = \mathcal{N}(0, I), \qquad \mathbf{x} \sim p_\theta(\mathbf{x} \mid \mathbf{z})
$$

$p_\theta(\mathbf{x} \mid \mathbf{z})$ is the **decoder** — a neural network that parameterizes the likelihood. But we don't know $p(\mathbf{z} \mid \mathbf{x})$ — the posterior — because it's intractable.

### The trick: approximate the posterior with a neural encoder

$$
q_\phi(\mathbf{z} \mid \mathbf{x}) = \mathcal{N}(\mu_\phi(\mathbf{x}), \sigma^2_\phi(\mathbf{x}))
$$

The encoder network outputs $\mu_\phi$ and $\log \sigma^2_\phi$ per example.

### The ELBO

The evidence lower bound (ELBO) on $\log p(\mathbf{x})$:

$$
\mathcal{L}(\theta, \phi; \mathbf{x}) = \underbrace{\mathbb{E}_{q_\phi(\mathbf{z}|\mathbf{x})}[\log p_\theta(\mathbf{x}|\mathbf{z})]}_{\text{reconstruction}} - \underbrace{\mathrm{KL}(q_\phi(\mathbf{z}|\mathbf{x})\,\|\,p(\mathbf{z}))}_{\text{regularizer}}
$$

Maximize the ELBO $\to$ train the encoder and decoder jointly. The KL term has a closed form when both $q_\phi$ and $p$ are Gaussian.

### Reparameterization trick

Sampling $\mathbf{z} \sim q_\phi(\mathbf{z}|\mathbf{x})$ is not differentiable. Trick:
$$
\mathbf{z} = \mu_\phi(\mathbf{x}) + \sigma_\phi(\mathbf{x}) \odot \boldsymbol{\epsilon}, \quad \boldsymbol{\epsilon} \sim \mathcal{N}(0, I)
$$
Now the stochasticity is in $\boldsymbol{\epsilon}$ (external to the graph); $\mu$ and $\sigma$ are differentiable w.r.t. $\phi$.

## Why it matters / when you use it

- **Principled latent-space generative model.** Cleaner than GANs for learning a structured representation.
- **Wireless applications:** CSI compression with probabilistic reconstruction, denoising autoencoders for channel estimation, learned priors for sparse channel estimation.
- **Precursor to diffusion.** Diffusion models generalize VAEs by iterating the latent step many times — the intuition transfers.

## Common mistakes

- **Posterior collapse.** When the decoder is too powerful, it ignores $\mathbf{z}$; the KL term pushes $q(\mathbf{z}|\mathbf{x}) \to p(\mathbf{z})$ and the encoder becomes uninformative. Fixes: KL annealing, $\beta$-VAE, skip connections.
- **Overly simple prior.** $\mathcal{N}(0,I)$ is often too restrictive. Normalizing flows as the prior help.
- **Treating $\sigma$ as a free parameter without a prior.** Watch for collapsed variances.

## Reading order

1. [Lilian Weng's VAE post](https://lilianweng.github.io/posts/2018-08-12-vae/) — the best pedagogical treatment.
2. Kingma & Welling 2013 (arxiv:1312.6114).
3. Prince Ch 17 ([[textbook-prince-understanding-deep-learning]]).
4. PyTorch-VAE reference implementations: https://github.com/AntixK/PyTorch-VAE.

## Related
- [[diffusion-model]] — the natural successor.
- [[generative-adversarial-network]] — the other 2014-era generative family.
- [[csi-feedback]] — VAE/autoencoder are the parent family.
- [[python-ml-wireless]]
