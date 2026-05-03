---
title: "Kingma & Welling 2013 — Auto-Encoding Variational Bayes (VAE)"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/kingma-2013-vae.pdf
source_date: 2013-12-20
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - vae
  - generative
  - variational-inference
  - kingma
  - foundational
  - phase-2
created: 2026-05-01
updated: 2026-05-01
---

# Kingma & Welling 2013 — Auto-Encoding Variational Bayes (VAE)

**Authors:** Diederik P. Kingma, Max Welling (Universiteit van Amsterdam). **arxiv:1312.6114**. Mirrored at `raw/articles/ml-phy/pdfs/kingma-2013-vae.pdf`.

## TL;DR
**The VAE paper.** Combines variational inference with deep neural networks via the **reparameterization trick** — making the variational lower bound (ELBO) differentiable end-to-end and trainable with vanilla SGD. The architecture pairs a learned **encoder** $q_\phi(z \mid x)$ (a.k.a. recognition model) with a learned **decoder** $p_\theta(x \mid z)$ — **the auto-encoding variational Bayes (AEVB)** algorithm.

## Key contributions

1. **Reparameterization trick.** Express $z \sim q_\phi(z|x)$ as $z = g_\phi(\epsilon, x)$ with $\epsilon \sim p(\epsilon)$ noise. Now $z$ is a deterministic function of $\phi$ and reparameterized noise — gradients flow through it.
2. **SGVB estimator** — Stochastic Gradient Variational Bayes. Differentiable unbiased estimate of the ELBO.
3. **AEVB algorithm.** Joint optimization of encoder + decoder via SGVB. The encoder is "amortized" — one neural net for all data points, vs. classical VI's per-point inference.
4. **No iterative inference per-point.** Unlike MCMC or mean-field VI, AEVB amortizes inference: cheap forward pass per new data point.

## ELBO (the cornerstone)

$$\log p_\theta(x) \geq \mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x|z)] - D_{\text{KL}}\bigl(q_\phi(z|x) \,\|\, p(z)\bigr)$$

The first term is a **reconstruction loss** (decoder accuracy); the second is the **regularizer** (encoder posterior should stay close to prior $p(z) = \mathcal{N}(0, I)$).

For Gaussian $q_\phi$ and $p$, the KL has a closed form, and the reconstruction is sampled via reparameterization.

## Why it matters / where it sits in the roadmap

- **Phase 2 M6 reading.** [[python-ml-wireless]] M6 lists "Generative models (Prince Ch 14–15; Kingma VAE; Lilian Weng)" as primary study; this is **the** VAE paper.
- **DSP↔ML identity.** The encoder $q_\phi(z|x)$ is **MMSE estimation when** $p(z)$ is Gaussian and $p(x|z)$ is linear-Gaussian — the same identity Bishop PRML Ch 13 anchors. Reach for this when explaining VAEs to a DSP audience.
- **Wireless applications.** CsiNet+ and several CSI-feedback variants are essentially VAEs; LWM's MCM objective is a variational analogue.
- **Foundation for diffusion.** [[paper-ho-2020-ddpm|DDPM]] (Ho 2020) generalizes VAE's variational lower bound to a Markov chain.

## Concepts grounded
- [[variational-autoencoder]] — primary concept page.
- [[backpropagation]] — reparameterization makes it work.
- [[gradient-descent]] — SGVB optimization.
- [[textbook-bishop-prml]] Ch 9–10 — variational inference foundations.

## Portfolio move (Phase 2 M6)
**Reproduce first.** Implement a basic VAE on MNIST (PyTorch, ~50 lines); reproduce the ELBO trajectories and sample reconstructions in the Kingma-Welling paper.

**Extend.** Apply to CsiNet-style CSI compression — train a VAE encoder/decoder pair on DeepMIMO channels; compare reconstruction NMSE vs CsiNet. (This is essentially what CsiNet+ does.)

## Related
- [[python-ml-wireless]]
- [[variational-autoencoder]]
- [[paper-goodfellow-2014-gan]] — adversarial alternative.
- [[paper-ho-2020-ddpm]] — diffusion (variational-cousin).
- [[textbook-prince-understanding-deep-learning]] Ch 14 — modern treatment.
- [[textbook-bishop-prml]] Ch 9–10 — variational-inference foundations.
