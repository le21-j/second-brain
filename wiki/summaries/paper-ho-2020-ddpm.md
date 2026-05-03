---
title: "Ho, Jain, Abbeel 2020 — Denoising Diffusion Probabilistic Models (DDPM)"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/ho-2020-ddpm.pdf
source_date: 2020-06-19
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - ddpm
  - diffusion
  - generative
  - foundational
  - phase-2
created: 2026-05-01
updated: 2026-05-01
---

# Ho, Jain, Abbeel 2020 — Denoising Diffusion Probabilistic Models (DDPM)

**Authors:** Jonathan Ho, Ajay Jain, Pieter Abbeel (UC Berkeley). **arxiv:2006.11239** (NeurIPS 2020). Mirrored at `raw/articles/ml-phy/pdfs/ho-2020-ddpm.pdf`.

## TL;DR
**The DDPM paper that started the diffusion-model era.** Trains a neural net to **denoise** at progressively-noisier stages of a fixed Gaussian-noise schedule. Sampling reverses the noising chain: start from pure noise, iteratively denoise, end with a clean sample. Beats GANs on FID; trains stably (no minimax instability). Now the dominant generative paradigm (Stable Diffusion, DALL-E 3, Sora).

## Key contributions

1. **Forward diffusion process** — fixed: $q(x_t \mid x_{t-1}) = \mathcal{N}(\sqrt{1-\beta_t} x_{t-1}, \beta_t I)$. Adds Gaussian noise over $T$ steps until $x_T \approx \mathcal{N}(0, I)$.
2. **Reverse denoising** — learned: $p_\theta(x_{t-1} \mid x_t) = \mathcal{N}(\mu_\theta(x_t, t), \Sigma_t)$. A neural network predicts the mean (or equivalently, the noise that was added).
3. **Simplified noise-prediction loss** — equivalent to a re-weighted ELBO:
   $$\mathcal{L}_{\text{simple}} = \mathbb{E}_{t, x_0, \epsilon}\bigl[\|\epsilon - \epsilon_\theta(\sqrt{\bar\alpha_t}x_0 + \sqrt{1-\bar\alpha_t}\epsilon, t)\|^2\bigr]$$
4. **Connection to score matching.** $\epsilon_\theta$ predicting the noise is equivalent to score-matching $\nabla_x \log p(x)$.
5. **Sample quality.** New SoTA on CIFAR-10; rivals GANs on faces.

## Why it matters / where it sits in the roadmap

- **Phase 2 M6 reading.** [[python-ml-wireless]] M6 generative line — closes the trio with [[paper-kingma-2013-vae]] + [[paper-goodfellow-2014-gan]].
- **The current SoTA generative paradigm.** Most 2024–2026 generative papers are diffusion-based.
- **Wireless applications.** Generative channel synthesis (replacing GANs); diffusion-based denoising channel estimation (Khosravirad et al. 2026 ["Generative Decompression"]); diffusion priors for inverse problems in MIMO detection.
- **Score-matching connection.** Bridges classical statistics (Hyvärinen 2005) and modern generative modeling — DSP-prior superpower territory.

## Sampling procedure (Algorithm 2 of the paper)

```python
x_t = torch.randn_like(target)              # start from pure noise
for t in reversed(range(T)):
    eps_pred = model(x_t, t)
    z = torch.randn_like(x_t) if t > 0 else 0
    x_t = (1 / sqrt(alpha_t)) * (
        x_t - (beta_t / sqrt(1 - alpha_bar_t)) * eps_pred
    ) + sigma_t * z
return x_t
```

## Concepts grounded
- [[diffusion-model]] — primary concept page.
- [[paper-kingma-2013-vae]] — VAE is diffusion's "single-step" cousin.

## Portfolio move (Phase 2 M6)
**Reproduce first** — non-negotiable gate before any wireless extension.
1. Implement DDPM on MNIST (~150 lines PyTorch); reproduce sample quality at $T=1000$; profile training time.
2. **Match published FID on CIFAR-10** before declaring the reproduction done.
3. Compare against a DCGAN baseline ([[paper-goodfellow-2014-gan]]) at the same FID metric — both must train to convergence on the same dataset.

**Extend (only after reproduce passes the FID gate).** Apply to **wireless channel synthesis** — train DDPM on DeepMIMO channels; compare quality to ray-traced ground truth and to the GAN baseline. (Khosravirad's 2026 "Generative Decompression" is the precedent.)

## Related
- [[python-ml-wireless]]
- [[diffusion-model]]
- [[paper-kingma-2013-vae]] — VAE.
- [[paper-goodfellow-2014-gan]] — GAN.
- [[textbook-prince-understanding-deep-learning]] Ch 18 — diffusion treatment.
