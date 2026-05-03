---
title: "Murphy — Probabilistic Machine Learning: An Introduction"
type: summary
source_type: other
source_path: raw/textbook/murphy-pml-intro.md
source_date: 2022
course:
  - "[[python-ml-wireless]]"
tags:
  - textbook
  - ml
  - probabilistic
  - murphy
  - reference
  - reference-card-stub
created: 2026-05-01
updated: 2026-05-01
---

# Murphy — Probabilistic Machine Learning: An Introduction

**Status:** stub — free at https://probml.github.io/pml-book/book1.html. Reference card at `raw/textbook/murphy-pml-intro.md`.

## TL;DR
**The modern encyclopedic replacement for [[textbook-bishop-prml]].** Use as reference, not linear read. Keep HTML in a tab; CTRL-F when needed. A second volume (**Advanced Topics**, https://probml.github.io/pml-book/book2.html) covers graphical models, causality, advanced generative.

## Topic coverage (4 parts)

| Part | Topic |
|---|---|
| I | Foundations (probability, statistics, linear algebra, optimization) |
| II | Linear models, deep learning basics |
| III | Beyond (clustering, dim reduction, GNNs, graphical models, RL) |
| IV | Beyond supervised (generative, structured prediction) |

## Where it's used in the roadmap
**Reference throughout — but anchor at specific milestones (Bishop covers what's old; Murphy covers what's new):**

| When | Section | Why |
|---|---|---|
| **Phase 2 M6** (generative reproduction) | **Part IV — generative models** | Modern VAE / diffusion treatment Bishop predates |
| **Phase 3 M7** (CS224W + Sionna RL line) | **Part III — GNN chapter** | The first place a DSP applicant should encounter modern GNNs systematically |
| **Phase 3 M8** (Sutton-Barto + HF Deep RL) | **Part III — RL chapter** | Concise modern RL reference complementing Sutton-Barto |
| **Phase 4 M11** (LWM extension) | **Part IV — structured prediction** | Foundation-model-style sequence/structure modeling |

## Why both Bishop and Murphy
- **Bishop** = clearer prose for the DSP↔ML identities (ridge=MMSE, Kalman=HMM-message-passing, EM, BP). Use Bishop first.
- **Murphy** = broader scope, more recent (covers what Bishop doesn't — GNNs, modern attention).

## Concepts grounded
- [[graph-neural-network]] (Part III)
- [[reinforcement-learning]] (Part III)
- [[variational-autoencoder]] (Part IV)
- [[bayesian-inference]], [[map-estimation]] — already in [[eee-350]]

## Related
- [[python-ml-wireless]]
- [[murphy]] — author
- [[textbook-bishop-prml]] — older but clearer for fundamentals
- [[textbook-prince-understanding-deep-learning]] — DL-specific complement
