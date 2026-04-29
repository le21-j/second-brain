# Information Theory, Inference, and Learning Algorithms — David J. C. MacKay

**Category:** Math / Coding theory / ML (crossover)
**Status:** FREE
**URL:** https://www.inference.org.uk/mackay/itila/book.html
**Author:** David MacKay (Cambridge; deceased 2016)
**Publisher:** Cambridge University Press, 2003
**Roadmap phase:** reference — critical for wireless

## Topic coverage (chapters that matter)
- Part I: Data compression (arithmetic coding, Huffman, Lempel-Ziv)
- Part II: Noisy-channel coding — **Ch 8–11: entropy, mutual information, channel capacity, Shannon's theorems**
- Part III: Further topics on inference (EM, variational, MCMC)
- Part IV: Probabilities and inference (not linear — pick and choose)
- **Part VI, Ch 47–50**: LDPC codes, turbo codes, fountain codes, arithmetic coding. **This is the part the roadmap calls out as "especially valuable."**

## Why it's on the roadmap
> "Chapters 47–50 on LDPC/turbo/fountain codes are especially valuable."

MacKay is the reason LDPC codes are in 5G. His treatment is **uncommonly intuitive**: rather than the algebraic definition, he derives LDPC codes as belief propagation on a factor graph — which directly connects to:
- [[belief-propagation]]
- [[nachmani-deep-decoding]] — "Deep Learning Methods for Improved Decoding of Linear Codes" (neural-BP decoders for LDPC)
- Bishop PRML Ch 8 (graphical models).

The LDPC→BP→graphical-models→neural-BP-decoders thread is one of the cleanest model-based DL stories in physical-layer ML.

## Wireless-relevant claim
The identity "LDPC decoding = loopy belief propagation = a GNN inference loop" is the reason GNNs are now a live area for decoders (Nachmani 2018; Buchberger 2020). If you can articulate this identity, it's a strong answer to a Wi-Lab or NVIDIA interview question.

## Related wiki pages
- [[python-ml-wireless]]
- [[belief-propagation]]
- [[ldpc-codes]]
- [[david-mackay]]
