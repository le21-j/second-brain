---
title: Belief propagation (BP)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - decoding
  - factor-graph
  - ldpc
  - gnn
  - dsp-ml-identity
sources:
  - "[[textbook-mackay-itila]]"
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-05-01
updated: 2026-05-01
---

# Belief propagation (BP)

## In one line
**Belief propagation is message-passing on a factor graph that computes (approximate) marginal posteriors — and the same algorithm is what graph neural networks do.** It's the canonical DSP↔ML identity for decoders.

## Example first

**Decoding a tiny LDPC code.** Suppose we transmit a 3-bit codeword $\mathbf{c} = (c_1, c_2, c_3)$ subject to one parity-check constraint $c_1 \oplus c_2 \oplus c_3 = 0$, over a binary symmetric channel with flip probability $p = 0.1$. The receiver gets $\mathbf{y} = (1, 0, 0)$. What was sent?

Build the factor graph: 3 **variable nodes** (one per bit) + 1 **check node** (the parity constraint) + a **channel factor** at each variable that encodes the likelihood from $y_i$.

Run BP for a few iterations:

1. **Variable → check**: each variable sends its current belief (initialized from the channel) to the check node.
2. **Check → variable**: the check node enforces the parity constraint by sending each variable a "what the others think you should be" message — formally, $\tanh(L_{\text{out}}/2) = \prod_{j\neq i} \tanh(L_{j\to c}/2)$ in log-likelihood-ratio form.
3. **Variable update**: each variable sums incoming LLRs (channel + check) → new belief.
4. **Repeat**.

After 2–3 iterations the LLRs converge and we read off $\hat{\mathbf{c}} = (1, 0, 1)$ — the parity check has corrected the second bit. **This is exactly what a 5G LDPC decoder does, just with thousands of nodes.**

## The idea

A **factor graph** decomposes a global function (a posterior, a code constraint, a Markov random field) into local factors connected to the variables they depend on. **BP exchanges messages along graph edges** — each message is a local "what I believe about you, given everything else I know" summary. After enough rounds, the messages converge to the correct marginal posteriors **on tree-structured graphs** and to a useful approximation on loopy graphs (which all real codes have).

Two flavors:
- **Sum-product BP** — computes marginal probabilities. For LDPC: bit-error decoding.
- **Max-product BP (Viterbi)** — computes MAP assignments. For convolutional codes: ML sequence decoding.

## Formal definition

Given a factor graph with variables $\{x_i\}$ and factors $\{f_a\}$, BP iterates two message types:

$$\mu_{x_i \to f_a}(x_i) = \prod_{b \in N(i)\setminus a} \mu_{f_b \to x_i}(x_i)$$

$$\mu_{f_a \to x_i}(x_i) = \sum_{\mathbf{x}_a \setminus x_i} f_a(\mathbf{x}_a) \prod_{j \in N(a)\setminus i} \mu_{x_j \to f_a}(x_j)$$

Marginal estimate: $b_i(x_i) \propto \prod_{a \in N(i)} \mu_{f_a \to x_i}(x_i)$. In log-likelihood-ratio form for binary variables, sums become LLR additions and products of $\tanh$ enforce parity at check nodes.

## Why it matters / when you use it

- **5G LDPC decoder.** Standard 3GPP NR uses LDPC for the data channel; the receiver runs sum-product BP on the parity-check graph. See [[ldpc-codes]].
- **Polar code decoders.** Successive-cancellation list decoders are essentially BP-on-a-tree variants.
- **Factor graphs are ubiquitous** in inference: HMMs (forward-backward = BP), Kalman filters (BP on a chain), Bayesian networks.
- **DSP↔ML identity (the load-bearing one for the NVIDIA-intern story).** A graph neural network's message-passing layer **is BP** — both compute aggregated messages from neighbors then update node states. **Nachmani et al. 2018** ("DL Methods for Improved Decoding of Linear Codes", IEEE JSTSP) showed you can train the BP messages with neural-network weights and outperform classical BP on short codes; **Buchberger et al. 2020** (arxiv:2001.07464) extended this to pruning + quantizing learned BP decoders. This is the reference architecture for "neural decoders."
- **Phase 3 M7 / Phase 4 M10–M12 reading.** [[python-ml-wireless]] flags neural BP as a comparison-baseline pillar — anyone building an end-to-end neural receiver (M7 Sionna NRX, M10 Wiesmayr standard-compliant NRX) must beat (or match) classical BP at the same SNR or the result is uninteresting.

## Common mistakes

- **Treating BP as exact on loopy graphs.** It's an approximation on real codes; convergence and accuracy depend on graph girth.
- **Forgetting normalization in LLR domain.** LLRs are unnormalized log-ratios but the message updates are not arbitrary — products and tanh keep the algebra consistent.
- **Confusing min-sum with sum-product.** Min-sum is a max-product approximation that's cheaper in hardware; gives slightly worse BER. 5G LDPC chips usually run *normalized min-sum*, not pure sum-product.
- **Neural BP without baseline.** A learned decoder that doesn't beat classical BP at the same SNR is not a publishable result. Always include the classical BP curve.

## Related

- [[ldpc-codes]] — the wireless code where BP is the workhorse decoder.
- [[polar-codes]] — BP-on-polar is one alternative to SC/SCL; Nachmani 2018 line works on polar before LDPC.
- [[graph-neural-network]] — the ML-side cousin; **message-passing layer is BP in expectation** (the load-bearing DSP↔ML identity for neural decoders).
- [[textbook-mackay-itila]] — Ch 16 on message passing, Ch 47 on LDPC, Ch 25 on Viterbi as max-product. **Primary reference**.
- [[ber-bler]] — what BP outputs improve.
- [[python-ml-wireless]] — neural BP is a Phase 3 M8 / Phase 4 M12 reading line.

## Practice
- **TODO** — BP-on-tiny-LDPC by hand (3-bit, 1 parity check); LLR table iteration. Defer to Phase 3 study session.
