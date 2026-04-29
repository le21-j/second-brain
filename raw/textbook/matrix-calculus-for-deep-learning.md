# The Matrix Calculus You Need For Deep Learning — Parr & Howard

**Category:** Math (derivative mechanics for DL)
**Status:** FREE
**URL:** https://explained.ai/matrix-calculus/
**arXiv:** https://arxiv.org/abs/1802.01528
**Authors:** Terence Parr (USF), Jeremy Howard (fast.ai)
**Roadmap phase:** Phase 1 Month 4 — read in one sitting

## Topic coverage
- Scalar-to-scalar derivatives refresher.
- The Jacobian: vector-to-vector derivatives.
- Chain rule for vector functions.
- Element-wise operations, Hadamard, broadcasting.
- Matrix derivatives: the identities you actually use in backprop.
- The full derivation of the neuron's weight gradient.

## Why it's on the roadmap
> "Read in one sitting."

For a DSP applicant, most of what's in here is already known (the scalar version). The value is the **index convention + chain rule for batched tensors**, which is the mental model you'll use every time you debug a PyTorch shape error in a custom loss.

## Companion media
- 3Blue1Brown's Neural Networks playlist (the first 4 videos cover most of this visually).

## Related wiki pages
- [[python-ml-wireless]]
- [[autograd]]
- [[backpropagation]]
