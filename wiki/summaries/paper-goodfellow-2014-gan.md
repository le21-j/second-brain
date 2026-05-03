---
title: "Goodfellow et al. 2014 — Generative Adversarial Networks"
type: summary
source_type: article
source_path: raw/articles/ml-phy/pdfs/goodfellow-2014-gan.pdf
source_date: 2014-06-10
course:
  - "[[python-ml-wireless]]"
tags:
  - paper
  - gan
  - generative
  - goodfellow
  - foundational
  - phase-2
created: 2026-05-01
updated: 2026-05-01
---

# Goodfellow et al. 2014 — Generative Adversarial Networks

**Authors:** Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio (Université de Montréal). **arxiv:1406.2661**. Mirrored at `raw/articles/ml-phy/pdfs/goodfellow-2014-gan.pdf`.

## TL;DR
**The GAN paper.** Proposes a generative model trained via a **minimax game** between a **generator** $G$ (which maps noise $z$ to fake samples) and a **discriminator** $D$ (which tries to distinguish fake from real). At equilibrium, $G$ produces samples indistinguishable from the data distribution. **No likelihood, no variational bound — pure adversarial training.** The basis of the entire 2015–2020 generative-modeling boom (DCGAN, WGAN, StyleGAN, CycleGAN, etc.).

## Key contributions

1. **The adversarial training paradigm.** Generator $G$ tries to fool discriminator $D$; discriminator tries to detect $G$'s output. Two-player minimax game.
2. **The objective:**
   $$\min_G \max_D \, \mathbb{E}_{x \sim p_{\text{data}}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]$$
3. **Theoretical analysis.** At global optimum, $p_g = p_{\text{data}}$ and $D \equiv 1/2$. Game has a unique equilibrium.
4. **No likelihood.** Doesn't require $\log p(x)$ — works on intractable likelihoods.
5. **Sample quality.** Beats VAE / RBM on MNIST / CIFAR-10 in qualitative sample quality.

## Why it matters / where it sits in the roadmap

- **Phase 2 M6 reading.** [[python-ml-wireless]] M6 generative line — Prince Ch 14–15 + Kingma VAE + this paper (Lilian Weng's blog covers all three).
- **Wireless applications.** Conditional GANs for **channel-agnostic E2E learning** (Ye-Li-Juang-Sivanesan 2020 — generates synthetic channels for training); GAN-based modulation classification (data augmentation); generative channel models.
- **Sequels still relevant in 2026:** WGAN-GP (training stability), StyleGAN (face quality), CycleGAN (unpaired translation), DCGAN (the standard simple recipe).

## Common training tricks (necessary in practice)

| Trick | Reason |
|---|---|
| Use $\log D$ (not $1 - \log D$) for $G$'s gradient | Stronger gradients early in training |
| Spectral normalization on $D$ | Stabilizes training |
| Wasserstein-GP loss | Replaces JS-divergence; smoother gradients |
| Lower learning rate for $D$ than $G$ | Prevents $D$ saturating |

## Concepts grounded
- [[generative-adversarial-network]] — primary concept page.
- [[textbook-prince-understanding-deep-learning]] Ch 15 — modern treatment.

## Portfolio move (Phase 2 M6)
**Reproduce first** — non-negotiable gate before any wireless extension.
1. Implement DCGAN on MNIST in PyTorch; reproduce sample quality at known epoch counts; track $D$/$G$ losses for stability.
2. **Match published DCGAN FID on MNIST** before declaring the reproduction done — without this baseline, the extension has nothing to compare against.

**Extend (only after the FID gate).** Train a conditional GAN (cGAN) on DeepMIMO channels — generate synthetic channels for a held-out scenario; compare FID + reconstruction NMSE to ray-traced ground truth. Connects to the [[paper-morais-similarity-2026]] dataset-similarity framework.

## Related
- [[python-ml-wireless]]
- [[generative-adversarial-network]]
- [[paper-kingma-2013-vae]] — alternative paradigm.
- [[paper-ho-2020-ddpm]] — current SoTA generative paradigm (diffusion).
- [[goodfellow]] — first author.
