---
title: Belief Propagation — Practice Set 01
type: practice
course:
  - "[[python-ml-wireless]]"
tags:
  - practice
  - belief-propagation
  - ldpc
  - polar-codes
  - dsp-ml-identity
concept:
  - "[[belief-propagation]]"
  - "[[ldpc-codes]]"
difficulty: mixed
created: 2026-05-01
updated: 2026-05-01
---

# Belief Propagation — Practice Set 01

> **Attempt each problem before scrolling to the solution.** The DSP↔ML identity (BP = GNN message-passing) only clicks once you've run sum-product by hand at least once. For each problem, log your attempt at the bottom; if you get it wrong, add an entry to [[mistakes/belief-propagation-gotchas|wiki/mistakes/belief-propagation-gotchas.md]] (create the page if it doesn't exist).

## Problems

### 1. Tiny LDPC by hand — easy

The (4,2) LDPC code with parity-check matrix:

$$\mathbf{H} = \begin{pmatrix} 1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1 \end{pmatrix}$$

Two check nodes ($c_1, c_2$); four variable nodes ($v_1, v_2, v_3, v_4$).

Channel LLRs received: $L = (-2, +1, +3, -1)$ (interpret: positive LLR = bit-0 more likely).

**(a)** Draw the factor graph (nodes + edges).
**(b)** Compute the variable-to-check messages **after one BP iteration**, in LLR domain.
**(c)** Compute the check-to-variable messages.
**(d)** Compute the **updated belief** for each $v_i$ after this iteration: $b_i = L_i + \sum_{c \in N(i)} \mu_{c \to v_i}$.
**(e)** Hard-decide: what's the decoded codeword $\hat c$? Does it satisfy $\mathbf{H}\hat c^T = \mathbf{0}$?

<details><summary>Solution</summary>

**(a) Factor graph:**
- $v_1$ connects to $c_1$ only.
- $v_2$ connects to $c_1$ and $c_2$.
- $v_3$ connects to $c_1$ and $c_2$.
- $v_4$ connects to $c_2$ only.

**(b) Variable→check messages (initialized from channel LLRs):**

For first iteration, $\mu_{v_i \to c_a} = L_i$ (since no other check messages yet):
- $\mu_{v_1 \to c_1} = -2$
- $\mu_{v_2 \to c_1} = +1$, $\mu_{v_2 \to c_2} = +1$
- $\mu_{v_3 \to c_1} = +3$, $\mu_{v_3 \to c_2} = +3$
- $\mu_{v_4 \to c_2} = -1$

**(c) Check→variable messages (sum-product on parity in LLR domain):**

Use $\mu_{c \to v} = 2\,\mathrm{atanh}\!\left(\prod_{u \in N(c)\setminus v}\tanh(\mu_{u \to c}/2)\right)$.

For $c_1$ (parity over $v_1, v_2, v_3$):
- $\mu_{c_1 \to v_1} = 2\,\mathrm{atanh}(\tanh(0.5) \cdot \tanh(1.5)) \approx 2\,\mathrm{atanh}(0.462 \cdot 0.905) \approx 2 \cdot 0.448 = +0.896$
- $\mu_{c_1 \to v_2} = 2\,\mathrm{atanh}(\tanh(-1) \cdot \tanh(1.5)) \approx 2\,\mathrm{atanh}(-0.762 \cdot 0.905) \approx -1.43$
- $\mu_{c_1 \to v_3} = 2\,\mathrm{atanh}(\tanh(-1) \cdot \tanh(0.5)) \approx 2\,\mathrm{atanh}(-0.352) \approx -0.736$

For $c_2$ (parity over $v_2, v_3, v_4$):
- $\mu_{c_2 \to v_2} = 2\,\mathrm{atanh}(\tanh(1.5) \cdot \tanh(-0.5)) \approx 2\,\mathrm{atanh}(-0.420) \approx -0.895$
- $\mu_{c_2 \to v_3} = 2\,\mathrm{atanh}(\tanh(0.5) \cdot \tanh(-0.5)) \approx 2\,\mathrm{atanh}(-0.213) \approx -0.432$
- $\mu_{c_2 \to v_4} = 2\,\mathrm{atanh}(\tanh(0.5) \cdot \tanh(1.5)) \approx 2\,\mathrm{atanh}(0.418) \approx +0.890$

**(d) Updated beliefs $b_i = L_i + \sum_c \mu_{c \to v_i}$:**

- $b_1 = -2 + 0.896 = -1.104$ → bit 1
- $b_2 = +1 - 1.43 - 0.895 = -1.325$ → bit 1
- $b_3 = +3 - 0.736 - 0.432 = +1.832$ → bit 0
- $b_4 = -1 + 0.890 = -0.110$ → bit 1

**(e) Decoded $\hat c = (1, 1, 0, 1)$.**

Check: $\mathbf{H}\hat c^T = ?$
- Row 1: $1+1+0+0 = 0$ ✓ (mod 2)
- Row 2: $0+1+0+1 = 0$ ✓ (mod 2)

Codeword is valid; BP converged in 1 iteration. ✓

</details>

---

### 2. Why BP works on trees, breaks on loops — medium

**(a)** Why is BP **exact** on tree-structured factor graphs?
**(b)** Why does BP only **approximate** the marginals on loopy graphs (real LDPC codes)?
**(c)** Define the **girth** of a factor graph. Why does it matter for LDPC code design?
**(d)** Real 5G LDPC matrices are designed to maximize girth. What's the typical girth of a 5G LDPC base graph?

<details><summary>Solution</summary>

**(a)** On a tree, every path between two nodes is unique. Each message from a subtree carries unbiased information about that subtree, independent of every other subtree. The product of these independent messages is a **valid factorization** of the joint marginal — BP is exact.

**(b)** On a loopy graph, two messages converging at a variable node have shared sub-information (a cycle), but BP treats them as independent and **double-counts** that information. Beliefs become overconfident.

**(c)** Girth = length of the **shortest cycle** in the graph. Larger girth → fewer short loops → BP behaves more "tree-like" → better convergence and BLER.

**(d)** 5G LDPC base graphs are designed for **girth ≥ 6**. The lifted graphs (after expanding by the lifting size $Z$) typically achieve girth 8–10 in deployed configurations.

</details>

---

### 3. Neural BP as a GNN — medium-hard

**(a)** State the formal correspondence: **a GNN's message-passing layer = one BP iteration with learnable parameters**. What's added vs. classical BP?
**(b)** In Nachmani et al. 2018 (weighted-BP), a learnable scalar $w_e$ is attached to each edge $e$. Why does this generalize classical BP?
**(c)** Why doesn't a vanilla feedforward NN work as a decoder for long codes (the [[paper-gruber-2017-channel-decoding]] curse-of-dimensionality result)?

<details><summary>Solution</summary>

**(a)** Classical BP: at each iteration, every message-passing edge applies the **same fixed update rule** (sum-product or min-sum). A GNN: each edge has **learnable weights**, the AGGREGATE function is parameterized (sum/mean/max/attention with learnable params), and the UPDATE function is a learned MLP/GRU. **Same dataflow, learned weights.**

**(b)** Nachmani's $w_e$ corrects for cycle-induced errors in loopy graphs. Classical BP overcounts shared info via cycles; weighted-BP can **down-weight** problematic edges. The classical decoder is the special case $w_e = 1 \forall e$.

**(c)** Curse of dimensionality: for code length $N$, $K$ info bits, there are $2^K$ codewords. A vanilla NN must memorize the **entire codebook** to decode unseen noisy receptions. With $K = 32$, $2^K = 4 \cdot 10^9$ codewords — completely infeasible. **Structured codes (polar, LDPC) have a recursive structure that BP/neural-BP can exploit; vanilla NNs can't.**

</details>

---

### 4. Connect to NVIDIA's NRX — hard

**(a)** Where does belief propagation appear in [[paper-nrx-cammerer-2023]]'s NRX architecture?
**(b)** [[paper-nrx-wiesmayr-2024]] is **standard-compliant**. What does that mean about its decoder?
**(c)** If you wanted to extend NRX with a **learned BP decoder** (Nachmani-style), where in the pipeline would the weighted-BP block sit?
**(d)** Cite the **specific Cammerer paper** that started his BP-decoder line. Why is it the mandatory pre-cold-email read?

<details><summary>Solution</summary>

**(a)** NRX outputs LLRs; the LLRs are then fed into a **classical 5G NR LDPC decoder** that uses BP (sum-product or normalized min-sum) internally. **The BP step happens AFTER the NRX**, not inside it.

**(b)** Standard-compliant means the decoder uses the **same 3GPP NR LDPC base graph + lifting size** as a real cellular deployment — not a researcher-friendly toy code. That constrains BP behavior to the standard's specific girth/density profile.

**(c)** The weighted-BP block would replace the classical BP decoder block — **between the NRX and the bit-output**. Architecture: `received_grid → NRX → LLRs → weighted-BP → bits`. End-to-end training would back-prop loss through both NRX and weighted-BP simultaneously.

**(d)** [[paper-gruber-2017-channel-decoding]] (Gruber, Cammerer, Hoydis, ten Brink 2017, CISS). It's where Cammerer's PhD line starts — a cold email to him that doesn't reference this paper signals you only know his recent work. **Mandatory read.**

</details>

---

### 5. Implementation challenge (open-ended) — hard / Phase 3 M7

Implement a **weighted-BP decoder** for the (15, 11) Hamming code in PyTorch. Train weights on a synthetic AWGN dataset; compare BLER vs classical BP at $E_b/N_0 \in \{1, 2, 3, 4\}$ dB.

> [!tip] Tier-3 reproduction discipline
> First reproduce CleanRL-style: vanilla classical BP, then Nachmani's weighted-BP. **Do not extend** (e.g. to LDPC, polar, attention-BP) until classical+weighted both work and you've reproduced Nachmani's headline gain on the (15,11) Hamming.

---

## Jayden's attempts log

> Date format: `YYYY-MM-DD`. Log each attempt with what worked / didn't / what to fix next time.

- **TBD** — first attempt log entry.
