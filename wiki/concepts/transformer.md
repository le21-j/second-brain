---
title: Transformer
type: concept
course:
  - "[[python-ml-wireless]]"
tags: [transformer, attention, dl, nlp, lwm, vaswani]
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-04-23
updated: 2026-05-06
---

# Transformer

## In one line
A neural network architecture that processes a sequence of tokens by letting each token **directly attend to every other token** through scaled dot-product self-attention — no recurrence, no convolutions, and it scales almost arbitrarily well with compute.

## Example first

**What "attend to every other token" means in code:**

```python
# Inputs: a batch of sequences, each of length T, each token dim D.
# x: (B, T, D)
Q = x @ W_Q      # queries:  (B, T, D_k)
K = x @ W_K      # keys:     (B, T, D_k)
V = x @ W_V      # values:   (B, T, D_v)

scores = Q @ K.transpose(-1, -2) / sqrt(D_k)   # (B, T, T): token i <-> token j
attn = softmax(scores, axis=-1)                # each row sums to 1
out = attn @ V                                 # (B, T, D_v)
```

Token $i$'s output is a weighted sum of values from all tokens, weighted by how much query $i$ matches key $j$. Repeat this for 8 or 16 parallel **heads**, concatenate, add a feedforward network, a residual, and a LayerNorm — that's one transformer block. Stack 6 or 24 of them and you have GPT-2 / BERT / ViT / the [[large-wireless-model]].

## The idea

**"Attention Is All You Need" — Vaswani et al. 2017** (arxiv:1706.03762). Three claims, each radical at the time:

1. **Recurrence is unnecessary.** You don't need to process sequences left-to-right; attention reads everything in parallel.
2. **Convolutions are unnecessary.** Local receptive fields aren't the only way to get structured features; attention is a dense, data-dependent alternative.
3. **Attention is a universal layer.** It works for translation (the original task), language modeling (GPT), image classification (ViT), protein folding (AlphaFold), audio (Whisper), and wireless (LWM).

### Anatomy of one transformer block

```
x ─┬─► LayerNorm ─► Multi-Head Attention ─►(+)─┬─► LayerNorm ─► MLP ─►(+)─► out
   │                                          │                         │
   └──────────────────────────────────────────┘                         │
                                                                        │
   ─────────────────────────────────────────────────────────────────────┘
```

- **Multi-Head Attention** $=$ $h$ parallel attention ops, concatenated $\to$ linear projection.
- **MLP** $=$ two Linear layers with a GELU nonlinearity (`Linear -> GELU -> Linear`).
- **Residual connections** around each sublayer.
- **LayerNorm** — either "pre-LN" (inside the residual) or "post-LN" (after). Pre-LN is more stable for very deep networks.

### Encoder vs decoder vs encoder-decoder

- **Encoder-only (BERT, ViT, LWM):** full self-attention. Used for classification, representation learning, regression.
- **Decoder-only (GPT, LLaMA):** causal (triangular) attention mask — each token attends only to previous tokens. Used for autoregressive generation.
- **Encoder-decoder (original Vaswani, T5):** encoder reads source, decoder cross-attends to encoder while generating. Used for translation, summarization.

### Positional encoding

Attention is permutation-equivariant: shuffle the tokens, the output shuffles the same way. That's fine for sets but not for sequences, where order matters. So every transformer adds **positional information**:
- **Sinusoidal** (original paper) — fixed positional embedding.
- **Learned** — a trainable embedding per position.
- **Rotary (RoPE)** — rotation in the complex plane, current state of art for LLMs.
- **ALiBi** — linear bias in attention scores.

### Why transformers scale

Self-attention is $O(T^2 D)$ per layer in memory and compute — quadratic in sequence length $T$. The fix (2020+) is a zoo of "efficient attention" variants: Linear attention, Longformer, Performer, Flash-Attention. For RF research with short sequences ($< 2048$), vanilla attention is fine.

## Formal definition

Given $\mathbf{X} \in \mathbb{R}^{T \times D}$, projections $\mathbf{W}_Q, \mathbf{W}_K \in \mathbb{R}^{D \times D_k}$, $\mathbf{W}_V \in \mathbb{R}^{D \times D_v}$:

$$
\mathrm{Attn}(\mathbf{X}) = \mathrm{softmax}\!\left(\frac{\mathbf{X} \mathbf{W}_Q (\mathbf{X} \mathbf{W}_K)^\top}{\sqrt{D_k}}\right) \mathbf{X} \mathbf{W}_V
$$

Multi-head: concatenate $h$ independent heads, project to $D$:

$$
\mathrm{MHA}(\mathbf{X}) = [\mathrm{Attn}_1(\mathbf{X}); \ldots; \mathrm{Attn}_h(\mathbf{X})] \, \mathbf{W}_O
$$

## Why it matters / when you use it

- **Dominant DL architecture.** Language, vision, audio, protein structure, wireless foundation models all converged on transformers.
- **[[large-wireless-model]] is a transformer.** Wi-Lab's entire foundation-model program is built on BERT-style masked modeling.
- **Compositional.** Swap CNN for a small transformer block in a neural receiver (Phase 3 roadmap milestone) — often improves BLER $0.5$–$1$ dB with little extra compute.

## Common mistakes

- **Skipping LayerNorm/residuals** — training collapses at depth $> 6$.
- **Wrong attention mask.** Causal attention with no mask $=$ decoder cheating; full attention with a mask $=$ encoder underperforming.
- **Positional encoding confusion.** Mixing sinusoidal-added-at-input with rotary-in-attention silently destroys your position info.
- **Quadratic memory.** Sequence length $4096$ with batch $64$ and $12$ heads $=$ hundreds of GB of attention-matrix memory without FlashAttention or similar.

## Reading order (per the roadmap)

1. Jay Alammar's **"Illustrated Transformer"** — https://jalammar.github.io/illustrated-transformer/. Visual.
2. Karpathy's **"Let's build GPT from scratch"** — https://www.youtube.com/watch?v=kCc8FmEb1nY. Code-along.
3. **"Attention Is All You Need"** — https://arxiv.org/abs/1706.03762. Canon.
4. **The Annotated Transformer** — http://nlp.seas.harvard.edu/annotated-transformer/. Paper + PyTorch code side-by-side.
5. Prince [[textbook-prince-understanding-deep-learning]] Ch 12.

## Related
- [[attention-mechanism]]
- [[large-wireless-model]]
- [[pytorch]]
- [[convolutional-neural-network]]
- [[neural-receiver]] — transformer blocks can replace CNN blocks
- [[python-ml-wireless]]
