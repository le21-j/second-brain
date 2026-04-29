---
title: HMC $\psi$ Rebuild (vs Hedge-Style Additive Update)
type: concept
course: [[research]]
tags: [research, regret-learning, hart-mas-colell, hedge, no-regret, game-theory, aircomp]
sources: [[daily-2026-04-23-pluto-deployment-and-regret-learning]], [[paper-unregrettable-hpsr]]
created: 2026-04-24
updated: 2026-04-26
---

# HMC $\psi$ Rebuild (vs Hedge Additive Update)

## In one line
Hart-Mas-Colell regret matching does **not** maintain $\psi$ as a running average with regret added each round — it **rebuilds $\psi$ from scratch** every round as $\psi[k] = \max(0,\,D[j,k])/\mu$ with $\psi[j] = 1 - \sum_{k \neq j}\psi[k]$ — memory of past epochs lives in $D$, not $\psi$.

## Example first — a misconception corrected

You might intuit the update as "start from a uniform baseline and accumulate":

$$\psi_{\text{round 0}} = [0.25,\,0.25,\,0.25,\,0.25] \quad\text{(uniform over $L = 4$ actions)}$$

$$\psi_{\text{round 1}} = \psi_{\text{round 0}} + \frac{\text{regret}_{\text{round 0}}}{\mu} \quad\Longleftarrow\textbf{ WRONG for HMC, this is Hedge-flavored}$$

$$\psi_{\text{round 2}} = \psi_{\text{round 1}} + \frac{\text{regret}_{\text{round 1}}}{\mu} \quad\Longleftarrow\textbf{ WRONG}$$

That's **exponential weights (Hedge)** — a different no-regret algorithm family. It's valid, just not what HPSR or our `asset_spec/regret_matching.py` implements.

The actual HMC update, written out for chosen action $j$ on round $t$:

```python
# Running-average regret matrix D (this is where memory lives)
for k != j:
    D[j, k] = ((t - 1) / t) * D_prev[j, k]  +  (1 / t) * (u_cf[k] - u_played)

# Rebuild psi from scratch (NOT additive!)
psi_new = zeros(L)
for k != j:
    psi_new[k] = max(0, D[j, k]) / mu        # assignment, not +=
psi_new[j]    = 1 - sum(psi_new[k] for k != j)   # residual
psi_new[k]    = max(psi_new[k], 1e-6)        # exploration floor
```

**Key move:** `psi_new = zeros()` at the top. Whatever $\psi$ was last round is discarded. The only thing carried forward is $D$, and even $D$ is a running average (scaled by $(t-1)/t$), not a sum.

## The idea

HMC and Hedge both belong to the **no-regret learning** family, but they manage state differently:

| Family | State carried round-to-round | $\psi$ update | Reference |
|---|---|---|---|
| **Hedge / Exponential Weights** | log-potentials that *accumulate* the loss history | $\psi_{\text{new}}[k] \propto \psi_{\text{old}}[k] \cdot e^{-\eta\,\text{loss}_k}$ — multiplicative on the old $\psi$ | Freund & Schapire 1997 |
| **Hart-Mas-Colell** | running-average regret matrix $D$ (no $\psi$ memory) | $\psi_{\text{new}}[k] = \max(0,\,D[j,k])/\mu$ — rebuilt each round from $D$ | Hart & Mas-Colell 2000 |

Both converge to correlated equilibrium under the right conditions. HPSR picks HMC because the update is **unconditionally mixing** — $\psi$ is derived from $\psi$-independent regret data — which matches how the paper wants to reason about convergence.

## Formal definition

From `python_reference/asset_spec/regret_matching.py` (the canonical ground truth — not `ed/regret_learning.py`, which was rewritten as a thin wrapper):

```python
# Line 117 (conceptually):
psi = np.zeros(L)

# Lines 120-135: for each non-chosen action k
for k in range(L):
    if k == j: continue
    psi[k] = max(0.0, D[j, k]) / mu

# Line 159: residual for the chosen action
psi[j] = 1.0 - psi[:].sum()

# Line 172 (AFTER psi rebuild, see "one-round mu delay" below)
mu = 0.01 / total_regret   # adaptive mu for NEXT round
```

Three consequences of this structure, all visible in golden-vector traces:

### 1. One-round $\mu$ delay

Adaptive $\mu$ ($\mu = 0.01 / \sum|D|$) is updated **after** $\psi$ has been rebuilt. So round-0's $\psi$ is computed with the **initial** $\mu = 3000$, making all regrets look tiny ($\text{regret}/3000 \approx 10^{-5}$). The freshly-adapted $\mu$ from round 0 first influences $\psi$ on **round 1**.

Look at the classic golden-vector trace for $L = 4$, seed $= 42$:

```
Round 0:  psi = [~0, 1, ~0, ~0]           # rebuild used OLD mu=3000 -> near-zero switch probs
          Adaptive mu then updated to ~0.2390 for next round.
Round 1:  psi = [~0, 0.83, 0.06, 0.11]    # rebuild used NEW mu=0.2390 -> real switch probs
```

**This is intentional** — it decouples $\psi$ from the $\psi$-generating process and prevents oscillation. Matches asset_spec lines 135 vs 172 exactly.

### 2. Exploration floor $\texttt{PSI\_EXPLORATION\_FLOOR} = 10^{-6}$

Without a floor, $\psi[k] = 0$ would permanently lock out action $k$ — can't sample it $\to$ can't observe its counterfactual regret $\to$ can't ever come back. The $10^{-6}$ floor guarantees every action has $\geq$ 1-in-a-million sampling probability, which preserves the HMC convergence guarantee under environmental change (e.g., channel moves between epochs). See `firmware/ed/regret_learning.h` for the constant.

### 3. $D$ is a running average, not a sum

The $(t-1)/t$ decay makes $D[j,k]$ converge to the **mean counterfactual regret** — not a cumulative regret. This is deliberately bounded: you can re-apply the "divide by $\mu$" step without $D$ blowing up over long runs. Papers that present HMC with a cumulative regret usually normalize by $t$ implicitly at the $\psi$ step; asset_spec folds the $1/t$ into $D$ itself. Equivalent outcome.

## Why it matters / when you use it

When debugging the learner:

- "Why does $\psi$ look uniform after round 0?" — $\mu$ was still $3000$. Check round 1.
- "Why does action $k = 2$ never get sampled?" — check the floor; if $\psi[2] = 0$ exactly, the floor clamp was skipped.
- "Regret is huge but $\psi$ barely budges" — you're watching $D$ grow; the effect shows when $\max(0, D)/\mu$ finally exceeds $\mu$.

When cross-checking C $\leftrightarrow$ Python: bit-exact agreement on $D$ and $\psi$ after the same (non-PRNG-dependent) inputs is the contract. The `test_asset_golden.py` $\to$ JSON $\to$ `firmware/ed/tests/test_regret_vs_asset.c` pipeline enforces this (JSON-parser TODO still open).

## Common mistakes

- **"Additive on a 25% baseline."** That's Hedge intuition. HMC rebuilds from zero each round. See example above.
- **Thinking $D$ grows without bound.** It doesn't — the $(t-1)/t$ decay makes $D$ a running average. It's bounded by the utility range.
- **Confusing $\psi[j]$ (stay-put) with $1$.** It's $1 - \sum_{k \neq j}\psi[k]$, which can be less than $1$ only if the sum is nonzero. On round $0$ with tiny regrets / huge $\mu$, $\psi[j] \approx 1$ as expected.
- **Thinking the exploration floor biases the estimator.** It adds $\mathcal{O}(10^{-6} \cdot L)$ probability mass, which is negligible next to any real regret signal. Its job is tail-risk coverage, not accuracy correction.
- **Expecting adaptive $\mu$ to take effect on the same round.** It doesn't — one-round delay, always.

## Related
- [[regretful-learning]] — the full algorithm
- [[aircomp-utility-s1-s2]] — how $u_{\text{cf}}$ (counterfactual utility) is computed per candidate action
- [[pre-flash-test-pyramid]] — where the asset_spec $\leftrightarrow$ C equivalence is verified
- [[paper-unregrettable-hpsr]] — the paper this implements
- [[system-pipeline]] — Stage 6/7 of the epoch that triggers each $\psi$ rebuild

## Sources / further reading
- Hart & Mas-Colell (2000), *A Simple Adaptive Procedure Leading to Correlated Equilibrium*, Econometrica 68(5).
- Freund & Schapire (1997), *A Decision-Theoretic Generalization of On-Line Learning* — for contrast (Hedge).
- `aircomp-regret-pluto/python_reference/asset_spec/regret_matching.py` — the canonical 200-line implementation.
