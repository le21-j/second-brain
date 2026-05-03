---
title: "MacKay — Information Theory, Inference, and Learning Algorithms"
type: summary
source_type: textbook
source_path: raw/textbook/pdfs/mackay-itila.pdf
source_date: 2003
course:
  - "[[python-ml-wireless]]"
tags:
  - textbook
  - information-theory
  - mackay
  - ldpc
  - inference
created: 2026-05-01
updated: 2026-05-01
---

# MacKay — Information Theory, Inference, and Learning Algorithms (ITILA)

**Author:** David J.C. MacKay (1967–2016, Cavendish Lab, Cambridge). **Cambridge University Press, 2003**; free PDF (on-screen viewing only) at https://www.inference.org.uk/itprnn/book.pdf. 50 chapters, ~640 pages, mirrored locally at `raw/textbook/pdfs/mackay-itila.pdf`.

## TL;DR
The book that **unifies information theory and machine learning** — written from the conviction that "they are two sides of the same coin." For [[python-ml-wireless]], the load-bearing chapters are **Ch 47–50 on sparse graph codes (LDPC, turbo, fountain)** — these are the codes 5G NR actually deploys, and modern neural-decoder research (Nachmani et al. 2018, GNN belief-propagation) builds directly on the message-passing framework MacKay laid out.

## Confirmed table of contents (7 parts)

### Part I — Data Compression (Ch 1–7)
Source coding theorem, symbol codes, stream codes (Huffman, arithmetic), integer codes.

### Part II — Noisy-Channel Coding (Ch 8–11)
| Ch | Title | Roadmap relevance |
|---|---|---|
| 8 | Dependent Random Variables | conditional/joint entropy, mutual info |
| 9 | Communication over a Noisy Channel | channel capacity definition |
| 10 | The Noisy-Channel Coding Theorem | **Shannon's 2nd theorem — the bedrock** |
| 11 | Error-Correcting Codes and Real Channels | Hamming, BCH, Reed-Solomon |

### Part III — Further Topics in Information Theory (Ch 12–19)
Hash codes, binary codes, **Ch 16 Message Passing** (sum-product, max-product) — directly relevant to modern neural decoders.

### Part IV — Probabilities and Inference (Ch 20–37)
Bayesian inference, Monte Carlo, Markov-chain Monte Carlo, variational methods, Occam's razor. **Ch 28 Model comparison** is the cleanest Bayesian-vs-frequentist treatment in any book.

### Part V — Neural Networks (Ch 38–46)
Single neuron, capacity, learning as inference, Hopfield, Boltzmann, multilayer networks, **Ch 45 Gaussian Processes**.

### Part VI — **Sparse Graph Codes (Ch 47–50)** — the wireless gold
| Ch | Title | Roadmap relevance |
|---|---|---|
| **47** | **Low-Density Parity-Check Codes** | **5G NR data-channel code** — the chapter that grounds [[ldpc-codes]] |
| **48** | **Convolutional Codes and Turbo Codes** | LTE workhorses; turbo BP is GNN-decoding's ancestor |
| **49** | **Repeat-Accumulate Codes** | bridge between LDPC and turbo |
| **50** | **Digital Fountain Codes** | rateless coding (LT, Raptor) |

### Part VII — Appendices
Notation, physics, mathematics.

## Why it's load-bearing for the roadmap

> "Chapters 47–50 on LDPC/turbo/fountain are especially valuable." — roadmap §3.

Three reasons:

1. **5G NR uses LDPC for data channels and polar codes for control channels.** Understanding LDPC at MacKay's level is mandatory for any neural-decoder or differentiable-receiver work — the architectures in [[neural-receiver]] (Cammerer 2023, Wiesmayr 2024) feed an unchanged LDPC decoder, and the GNN-decoder thread (Nachmani 2018, Buchberger 2020) replaces BP message-passing with a learned GNN.
2. **Belief propagation = sum-product on a factor graph = GNN message-passing.** This is one of the highest-leverage **DSP↔ML identities** the persona reaches for. MacKay Ch 16 + Ch 47 → Bishop PRML Ch 8 → Nachmani et al. 2018 is the canonical reading chain.
3. **Information-theoretic loss-function intuition.** Cross-entropy loss = $-\log p(\text{data} \mid \theta)$ = the negative log-likelihood = the source-coding rate to encode the labels given the model. MacKay Ch 4–5 is the cleanest grounding for [[cross-entropy-loss]].

## Roadmap reading order

Per [[python-ml-wireless]]:
- **Phase 1–2 (selectively):** Ch 2–3 (probability + inference) as Bayesian backbone for [[bayesian-inference]] (already on the wiki).
- **Phase 2 M5 (Sep 2026):** Ch 8–11 alongside the autoencoder reproduction — gives information-theoretic grounding for E2E learning.
- **Phase 3 M8–9 (Dec 2026 – Jan 2027):** **Ch 47–50** when working on neural decoders / GNN-BP / [[csi-feedback]] compression bounds. **This is the must-read block.**
- **Phase 4 (optional):** Ch 38–46 (NN chapters) only if interested in MacKay's "learning as inference" framing — Bayesian deep learning.

## Concepts grounded by this textbook

**Already exists in the wiki:**
- [[bayesian-inference]] — Ch 2–3, 28 will be cross-linked.

**To be created** (deferred — these are mostly Phase 3+ topics):
- ldpc-codes (Ch 47) — *creating in this session*
- turbo-codes (Ch 48)
- belief-propagation (Ch 16, 47) — referenced in roadmap as DSP↔ML identity, on the to-do list
- channel-capacity (Ch 9–10)
- mutual-information (Ch 8)
- sum-product-algorithm (Ch 16)

## Worked examples worth remembering
- **Ch 1.2 noisy typewriter** — the cleanest channel-capacity example in the literature.
- **Ch 47.1 LDPC parity-check matrix → Tanner graph → BP iterations** — the picture-driven derivation that makes BP click.
- **Ch 16.1 sum-product on a chain** — message-passing visualized for the simplest case.
- **Ch 28 Occam's razor as marginal-likelihood** — the figure that converts skeptics to Bayesians.

## Questions this source raises (open)
- **Polar codes** (Arıkan 2009) post-date this book entirely — for 5G NR control-channel coding, supplement with separate references.
- The neural-network chapters (38–46) are pre-AlexNet (2003-vintage) — useful for inference-theoretic framing but obsolete for modern DL practice. Use Prince UDL instead.

## Related
- [[python-ml-wireless]] — the course page driving the reading order.
- [[textbook-prince-understanding-deep-learning]] — Prince Ch 5 grounds cross-entropy in MacKay's likelihood framework.
- [[bayesian-inference]] — wiki concept; will be cross-linked.
- [[csi-feedback]] — compression bound theory traces back to Shannon source-coding (Ch 4).
- [[mackay]] — author page.
