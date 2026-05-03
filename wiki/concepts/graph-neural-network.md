---
title: Graph neural network (GNN)
type: concept
course: [[python-ml-wireless]]
tags: [gnn, dl, graphs, message-passing, wireless-graphs]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# Graph neural network (GNN)

## In one line
A neural network that takes a **graph** (nodes $+$ edges with features) as input and updates each node's embedding by aggregating messages from its neighbors — iterate a few rounds and each node "knows" its local neighborhood.

## Example first

Wireless network as a graph: BSs and UEs are nodes, edges represent channel quality (or interference) between pairs. You want to predict "which UE should each BS schedule this slot?"

A GNN:
1. Embed each node's features (BS: location, queue length; UE: CQI, QoS class).
2. For $L$ rounds: each node gathers messages from its neighbors (their current embeddings, weighted by edge features) and updates itself.
3. A classifier head on each (BS, UE) pair predicts schedule/don't-schedule.

Because the rule "aggregate from neighbors" is the same at every node and for any graph, a GNN trained on $20$-node networks generalizes to $200$-node networks with no architecture change — a property MLPs and CNNs cannot match.

## The idea

GNNs are the DL family for **irregular graph-structured data**. Most architectures are instances of a **message-passing framework** (Gilmer et al. 2017):

$$
\mathbf{h}_v^{(l+1)} = \text{UPDATE}^{(l)}\left(\mathbf{h}_v^{(l)},\; \text{AGG}^{(l)}\{\mathbf{h}_u^{(l)} : u \in \mathcal{N}(v)\}\right)
$$

- AGG can be sum, mean, max, or attention.
- UPDATE is usually an MLP or a GRU.
- Read-out (for graph-level tasks): sum/mean/max over all nodes $\to$ classifier head.

### Popular instances

| Name | Aggregation | Notes |
| --- | --- | --- |
| **GCN** (Kipf & Welling 2017) | symmetric-normalized sum | the simplest; baseline |
| **GAT** (Veličković 2018) | attention-weighted sum | each edge gets a learned weight |
| **GraphSAGE** (Hamilton 2017) | sample neighbors $+$ MLP | scales to huge graphs |
| **MPNN** (Gilmer 2017) | anything | the general framework |
| **Graph Transformer** | full attention $+$ graph encoding | recent; beats vanilla GAT |

### Wireless applications — why GNNs matter here specifically

Wireless networks *are* graphs. Natural applications:

- **Resource allocation / scheduling** — Eisen et al. 2018 (arxiv:1807.08088) "Learning Optimal Resource Allocations in Wireless Systems" — GNN learns water-filling over interference graphs.
- **Spatial scheduling** — Cui, Shen, Yu 2018 (arxiv:1808.01486) "Spatial Deep Learning for Wireless Scheduling."
- **Neural BP decoders** — LDPC factor graphs are bipartite; message passing on them is exactly BP; **a GNN is the natural generalization of BP decoders**. See [[belief-propagation]], Nachmani 2018.
- **CSI feedback with graph structure** — multi-cell / multi-user CSI feedback treated as graph compression.
- **Beam selection across interference graphs** — cross-BS coordination.

## Formal definition (GCN)

For a graph with adjacency $A$ and features $X$:

$$
H^{(l+1)} = \sigma\!\left(\tilde D^{-1/2}\,\tilde A\,\tilde D^{-1/2}\, H^{(l)}\, W^{(l)}\right)
$$

where $\tilde A = A + I$ (self-loops), $\tilde D$ is the degree matrix, $\sigma$ is ReLU, $W^{(l)}$ is learned.

## Why it matters / when you use it

- **Translation invariance for graphs.** Same weights apply anywhere — the key property that makes GNNs generalize across graph sizes.
- **Wireless-networks-as-graphs.** The roadmap flags GNN as "highly relevant for wireless networks as graphs" and routes Phase 3 through Stanford CS224W.
- **Neural decoders.** GNNs generalize belief propagation; the modern neural decoder literature uses GNN message passing.

## Common mistakes

- **Over-smoothing.** Too many message-passing layers $\to$ all nodes converge to the same embedding. Typical budget: $2$–$6$ layers.
- **Ignoring edge features.** Most real graphs have important edge features (channel quality, interference level). GAT handles them; vanilla GCN ignores them.
- **Shuffling without permutation invariance.** The AGG operation must be permutation-invariant; max/mean/sum are, but if you sort neighbors and MLP them, you've broken the GNN's core property.

## Reading order (per roadmap)

1. **Stanford CS224W** (https://web.stanford.edu/class/cs224w/) — the canonical course.
2. Prince [[textbook-prince-understanding-deep-learning]] Ch 13 — GNN chapter.
3. PyTorch Geometric docs — https://pytorch-geometric.readthedocs.io/.
4. Eisen et al. 2018 (arxiv:1807.08088) — wireless-specific entry point.

## Related
- [[belief-propagation]] — GNNs generalize BP on factor graphs.
- [[neural-receiver]] — GNN variants exist for MIMO detection.
- [[python-ml-wireless]]
