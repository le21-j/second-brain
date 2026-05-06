---
title: Generative adversarial network (GAN)
type: concept
course:
  - "[[python-ml-wireless]]"
tags: [gan, generative, dl, goodfellow]
sources:
  - "[[paper-goodfellow-2014-gan]]"
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-04-23
updated: 2026-05-06
---

# Generative adversarial network (GAN)

## In one line
Train two networks against each other: a **generator** $G$ that makes fake samples from noise, and a **discriminator** $D$ that tries to tell fake from real — at equilibrium, $G$ produces samples indistinguishable from the true data distribution.

## Example first

Train a GAN on CelebA faces. $G$ takes $\mathbf{z} \sim \mathcal{N}(0, I)$ in $\mathbb{R}^{128}$ and outputs a $64\times 64$ RGB image. $D$ takes a $64\times 64$ image and outputs a real/fake score. Training alternates:

1. **D-step:** draw a batch of real images $+$ a batch of $G(\mathbf{z})$ fakes; train $D$ to classify real$=1$, fake$=0$.
2. **G-step:** draw a batch of fakes; train $G$ so that $D$ labels them real$=1$ (i.e., maximize $D$'s error).

At equilibrium, $D \to 0.5$ everywhere (can't tell the difference), and $G$'s samples look like faces.

## The idea

**Goodfellow et al. 2014** (arxiv:1406.2661). The objective is a minimax two-player game:

$$
\min_G \max_D \; \mathbb{E}_{\mathbf{x} \sim p_\text{data}}[\log D(\mathbf{x})] + \mathbb{E}_{\mathbf{z} \sim p_\mathbf{z}}[\log(1 - D(G(\mathbf{z})))]
$$

If both networks are flexible enough, the optimal $D$ is $p_\text{data} / (p_\text{data} + p_G)$ and the global minimum is reached when $p_G = p_\text{data}$.

### Why it works (and why it's hard)

- **Implicit density.** Unlike VAEs, GANs never write down a likelihood. They just learn to sample.
- **Mode collapse.** G can learn to produce a few very convincing samples and ignore the rest of the data distribution. The discriminator can't easily penalize it.
- **Training instability.** The minimax optimization is notoriously unstable — GAN training is an art.

### The zoo of GAN variants (read in order)

1. **Original GAN** (Goodfellow 2014) — the idea.
2. **DCGAN** (Radford 2015) — architectural guidelines for stable training: transpose convs, batch-norm, LeakyReLU.
3. **WGAN / WGAN-GP** (Arjovsky 2017) — Wasserstein distance instead of JS-divergence; much more stable training.
4. **StyleGAN / StyleGAN2 / StyleGAN3** (Karras et al. 2018–2021) — face/image synthesis at very high resolution.
5. **Conditional GAN (cGAN)** — condition on class labels or other inputs.
6. **CycleGAN** — unpaired image-to-image translation.

### Wireless applications

- **Channel surrogate.** Ye, Li, Juang, Sivanesan 2020 — use a conditional GAN to learn a differentiable channel model when the real channel is unknown (arxiv:1903.01391). Key for [[autoencoder-phy]] without a differentiable channel.
- **Augmentation** — generating synthetic signal samples for training in low-data regimes.

## Why it matters / when you use it

- **When you need implicit generative modeling.** GANs sidestep likelihoods; sometimes what you want is a good sampler, not a density.
- **Channel modeling.** The Ye et al. 2020 trick for channel-agnostic E2E learning is a staple citation.
- **As context.** The roadmap flags GANs for "working knowledge" — you read Goodfellow 2014 and skim DCGAN/WGAN-GP; you do not need to implement StyleGAN.

## Common mistakes

- **Training too long.** After $D$ becomes too strong, $G$ gets no gradient.
- **Not using gradient penalty.** WGAN-GP is the default modern recipe; without GP or spectral norm, training is very flaky.
- **Comparing FIDs computed with different feature extractors.** FID depends on the Inception network used; report configuration.

## Reading order

1. **[[paper-goodfellow-2014-gan]]** — the paper.
2. DCGAN + WGAN-GP skim.
3. Prince Ch 15 ([[textbook-prince-understanding-deep-learning]]).

## Related
- [[variational-autoencoder]]
- [[diffusion-model]]
- [[goodfellow]]
- [[python-ml-wireless]]
