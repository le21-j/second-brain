---
title: Attention mechanism
type: concept
course: [[python-ml-wireless]]
tags: [attention, dl, transformer, soft-lookup]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# Attention mechanism

## In one line
A **soft, differentiable lookup table**: given a query, compute a similarity-weighted average over a set of (key, value) pairs — weights given by $\text{softmax}(\mathbf{Q} \cdot \mathbf{K}^\top / \sqrt{d})$.

## Example first

A toy lookup: you have a dictionary `{red: [1,0,0], green: [0,1,0], blue: [0,0,1]}` and a query "reddish." A hard lookup fails (no exact key). A soft lookup:

```python
keys   = [[1,0,0], [0,1,0], [0,0,1]]    # red, green, blue in some embedding
values = [[255,0,0],[0,255,0],[0,0,255]] # RGB triples
query  = [0.9, 0.1, 0.0]                 # "reddish"

scores = query @ keys.T                   # [0.9, 0.1, 0.0]
weights = softmax(scores)                 # [0.56, 0.22, 0.22] (say)
out     = weights @ values                # returns mostly red, hints of green/blue
```

That's all attention is — a fuzzy dictionary lookup with softmax-normalized weights, made differentiable so you can learn the keys, values, and queries.

## The idea

Attention predates transformers — Bahdanau et al. 2014 introduced it for neural machine translation. The generalization that transformers popularized: **queries, keys, and values are all linear projections of the same input**, so attention becomes **self-attention**, and a single layer can let every token query every other token.

### Three attention flavors

1. **Self-attention** — Q, K, V all come from the same sequence. Captures intra-sequence relationships. Used in encoder-only (BERT, LWM).
2. **Cross-attention** — Q comes from one sequence, K and V from another. The decoder's attention to the encoder in seq2seq; used in speech recognition and image captioning.
3. **Causal (masked) self-attention** — Q and K both come from the same sequence but the softmax is masked to prevent attending to future positions. Used in autoregressive decoders (GPT).

### Scaling factor

The $\sqrt{D_k}$ in the denominator is not arbitrary — without it, dot products grow with dimension and softmax saturates (gradients vanish). Dividing by $\sqrt{D_k}$ keeps dot products at unit variance.

### Multi-head

One attention op captures one relationship type; multi-head attention runs $h$ parallel heads so different heads can learn different relations (syntactic, semantic, positional, etc.). Standard: $h = 8$ or $16$, each head has $D_k = D / h$.

### Efficient variants

Vanilla attention is $O(T^2)$ in time and memory. Modern options:

- **FlashAttention** — tiled on-chip computation; same math, $2$–$10\times$ faster, less memory.
- **Linear attention** — factor the softmax kernel to get $O(T)$ — cheaper but often weaker.
- **Sparse attention** (Longformer, BigBird) — attend to local windows $+$ a few global tokens.
- **Grouped-query attention (GQA)** — shared K, V across groups of heads — used in Llama 2/3 for inference speed.

## Formal definition

Attention function:

$$
\mathrm{Attn}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \mathrm{softmax}\!\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{D_k}}\right)\mathbf{V}
$$

For self-attention on input $\mathbf{X}$:

$$
\mathbf{Q} = \mathbf{X}\mathbf{W}_Q,\quad \mathbf{K} = \mathbf{X}\mathbf{W}_K,\quad \mathbf{V} = \mathbf{X}\mathbf{W}_V
$$

Masked (causal) variant: add $-\infty$ to upper-triangular entries of $\mathbf{Q}\mathbf{K}^\top$ before softmax.

## Why it matters / when you use it

- **Attention is the universal relation operator.** It replaces recurrence (RNNs) and constrains relational reasoning (graph pooling, set functions).
- **Wireless applications.** Cross-modal fusion in [[beam-prediction]] — RGB, GPS, sub-6 CSI embedded as tokens, attention fuses them. Channel-prediction (LWM-Temporal) — attention across time for Doppler estimation.

## Common mistakes

- **Forgetting the scaling factor.** Works for small $D$, fails at $D > \sim 64$.
- **Wrong mask.** Swap rows and columns; leak future into past; debugging nightmare.
- **$O(T^2)$ memory shock.** Naive attention at $T=8192$ and batch$=32$ needs $\sim 20$ GB of attention-matrix memory alone. Use FlashAttention or chunked attention.

## Related
- [[transformer]]
- [[large-wireless-model]]
- [[convolutional-neural-network]] — the architectural alternative
- [[python-ml-wireless]]
