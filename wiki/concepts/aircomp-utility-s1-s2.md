---
title: AirComp Utility — $S_1$ (Gain) and $S_2$ (Penalty) Aggregates
type: concept
course: [[research]]
tags: [research, aircomp, regret-learning, utility, feedback, bandwidth, privacy, hpsr]
sources: [[daily-2026-04-23-pluto-deployment-and-regret-learning]], [[paper-unregrettable-hpsr]]
created: 2026-04-24
updated: 2026-04-26
---

# AirComp Utility — $S_1$ and $S_2$ Aggregates

## In one line
Each ED's regret-learning utility is a difference of two terms $u_n = \text{term}_1 - \text{term}_2$, where each term is $(\text{something local to ED } n) \times (\text{a single scalar summarizing everyone else})$ — the two scalars are $S_1^{(n)}$ (linear) and $S_2^{(n)}$ (quadratic) and they carry the network's global state in constant bandwidth per ED, per epoch.

## Example first — hand calculation for ED 0 at round 0

Golden-vector scenario, $L = 4$, $N = 4$, $P_{\max} = 1$ mW, channel magnitudes drawn from the seed $= 42$ realization:

$$|h_0| = 1.034, \quad |h_1| = 0.925, \quad |h_2| = 1.117, \quad |h_3| = 0.841$$

$$g(|h|) = 1/\bigl|\log|h|\bigr|^\alpha \text{ with } \alpha = 0.1 \quad\Rightarrow\quad g(|h_1|) \approx 0.62,\; g(|h_2|) \approx 0.58,\; g(|h_3|) \approx 0.65$$

Chosen powers last round: $P_1 = 0.25$ mW, $P_2 = 0.50$ mW, $P_3 = 0.75$ mW, $P_n = 0.50$ mW (ED $0$). $\eta = 0.5$.

$$S_1^{(0)} = g(|h_1|)\sqrt{P_1/\eta} + g(|h_2|)\sqrt{P_2/\eta} + g(|h_3|)\sqrt{P_3/\eta}$$

$$\phantom{S_1^{(0)}} \approx 0.62 \cdot 0.0224 + 0.58 \cdot 0.0316 + 0.65 \cdot 0.0387$$

$$\phantom{S_1^{(0)}} \approx 0.0139 + 0.0183 + 0.0252 \approx 0.134 \quad\text{("chorus amplitude" felt by ED 0)}$$

$$S_2^{(0)} = g(|h_1|)^2 (P_1/\eta) + g(|h_2|)^2 (P_2/\eta) + g(|h_3|)^2 (P_3/\eta)$$

$$\phantom{S_2^{(0)}} \approx 0.384 \cdot 0.0005 + 0.336 \cdot 0.001 + 0.423 \cdot 0.0015$$

$$\phantom{S_2^{(0)}} \approx 0.00019 + 0.00034 + 0.00063 \approx 0.006 \quad\text{("chorus energy")}$$

The ES computes these two numbers per ED per epoch (one row per ED in the feedback frame) and broadcasts them. ED $0$ receives $(S_1^{(0)}, S_2^{(0)}) = (0.134, 0.006)$ and plugs them into its utility function **without ever seeing another ED's channel or power level**.

## The idea

The HPSR utility (Eq 5–6 in [[paper-unregrettable-hpsr]]) happens to **decompose** into a product structure:

$$u_n(P_n, P_{-n}) = g(|h_n|)\sqrt{P_n/\eta} \cdot \sum_{n' \neq n} g(|h_{n'}|)\sqrt{P_{n'}/\eta} \;-\; g(|h_n|)^2 (P_n/\eta) \cdot \sum_{n' \neq n} g(|h_{n'}|)^2 (P_{n'}/\eta)$$

$$= g(|h_n|)\sqrt{P_n/\eta} \cdot S_1^{(n)} \;-\; g(|h_n|)^2 (P_n/\eta) \cdot S_2^{(n)}.$$

Once you define $S_1^{(n)}$ and $S_2^{(n)}$ as the two sums, the utility is a function of **three numbers known at ED $n$**: $|h_n|$ (measured locally from the downlink beacon, see [[channel-estimation]]), $P_n$ (chosen locally), and the pair $(S_1^{(n)}, S_2^{(n)})$ (broadcast by the ES).

## The two terms, physically

- **Term 1 — gain from coherent contribution.** $g(|h_n|)\sqrt{P_n/\eta} \cdot S_1^{(n)}$. Rises with $\sqrt{P_n}$ — doubling your power multiplies term 1 by $\sim 1.41$. Rewards ED $n$ for boosting the sum when others are also boosting.
- **Term 2 — penalty for excess power.** $g(|h_n|)^2 (P_n/\eta) \cdot S_2^{(n)}$. Rises with $P_n$ — doubling your power multiplies term 2 by $2$. Punishes you for outpacing others and wasting energy that doesn't land in coherent superposition.

The **asymmetry** — term 1 scales as $\sqrt{P}$, term 2 as $P$ — creates a sweet-spot optimum at some finite $P_n$. That's exactly the point regret matching finds through counterfactual sampling: what $P_n$ maximizes $u_n$ *against today's* $(S_1^{(n)}, S_2^{(n)})$?

## Bandwidth win — feedback size is $\mathcal{O}(N)$, not $\mathcal{O}(N^2)$

Alternative designs you might reach for first:

| Design | Feedback per epoch | For $N = 100$ |
|---|---|---|
| Broadcast all $\{|h_{n'}|\}$ and all $\{P_{n'}\}$ | $(N \cdot 16 \text{ bits}) + (N \cdot 8 \text{ bits}) = 24N$ | $2400$ bits |
| Per-ED $(S_1^{(n)}, S_2^{(n)})$, 32-bit floats | $2 \cdot 32 \cdot N$ | $6400$ bits |
| Per-ED $(S_1^{(n)}, S_2^{(n)})$, 16-bit fixed-point | $2 \cdot 16 \cdot N$ | $3200$ bits |

At $N = 4$ both options are tiny ($\sim 100$ bits). At $N = 100+$ the full-vector broadcast actually wins for this specific calculation. **The real argument for $(S_1, S_2)$ isn't bandwidth — it's privacy and compute placement:**

- ED doesn't need to know anyone else's channel or power.
- ED doesn't have to re-sum the full vector every counterfactual evaluation (HMC regret evaluates $u_{\text{cf}}[k]$ for every candidate $k \neq j$, so the inner sum would repeat $L$ times per round without the aggregates).

## Privacy win — EDs stay anonymous to each other

$(S_1^{(n)}, S_2^{(n)})$ are scalars computed at the ES; no individual neighbor's channel or power leaks to ED $n$. This matters for any deployment where the EDs belong to different users and the channel state is sensitive (position-correlated, device-fingerprintable). Compare: broadcasting $\{|h_{n'}|\}$ leaks everyone's channel magnitudes to everyone.

## Counterfactual utility — why $(S_1, S_2)$ are held fixed per round

Inside `regret_update()` (see [[hmc-psi-rebuild]]), the learner computes $u_{\text{cf}}[k] = \texttt{ed\_utility}(|h_n|, P_{\text{level}}[k], S_1^{(n)}, S_2^{(n)})$ for **every candidate action $k$**, using the **same** $(S_1^{(n)}, S_2^{(n)})$. That's the counterfactual move — "what would my utility have been if I'd played $k$, with others behaving as they actually did this round?"

Holding $(S_1^{(n)}, S_2^{(n)})$ fixed is a simplification (it assumes others wouldn't have responded to your different choice), but it's exactly what the HMC theorem requires, and it's asymptotically correct: as $\psi$ converges, joint play converges to the correlated equilibrium regardless of the per-round counterfactual assumption.

## Why it matters / when you use it

- **Debugging feedback frames.** If ED $n$ sees $u_n$ collapse to zero, the first thing to check is the $(S_1, S_2)$ it received — did the ES broadcast real values, or did the frame CRC-fail and the ED saw stale zeros?
- **Tuning $\alpha$.** The channel-projection exponent $\alpha$ in $g(|h|) = 1/|\log|h||^\alpha$ shifts both $S_1$ and $S_2$ but nonuniformly; $\alpha = 0.1$ is HPSR's default and our current config.
- **Scaling $N$.** At $N = 4$ (benchtop), $S_2$ is nearly negligible compared to $S_1$ and the penalty term barely bites. At $N \geq 100$, $S_2$ dominates and the sweet-spot power drops significantly — this is why HPSR's paper plots ($N = 100$) show heavy regret at high-power actions.

## Common mistakes

- **Thinking the ED needs all individual channel gains.** It only needs the two aggregate scalars. See the bandwidth table.
- **Re-including ED $n$ in its own $S_1^{(n)}$/$S_2^{(n)}$.** The sum is $\sum_{n' \neq n}$ — over everyone except $n$ itself. Easy off-by-one at the ES.
- **Using the same $(S_1, S_2)$ across rounds.** They're epoch-specific and change every feedback broadcast. Cache only within a single `regret_update()` call.
- **Forgetting the $1/\sqrt{\eta}$ in $S_1$ (and the $1/\eta$ in $S_2$).** HPSR's formulation folds the denoising factor into each term; dropping it shifts the utility by a constant and breaks cross-check against golden vectors.

## Related
- [[regretful-learning]] — the outer algorithm that consumes $u_n$
- [[hmc-psi-rebuild]] — how $u_{\text{cf}}$ differences drive $D$ and then $\psi$
- [[channel-estimation]] — how $|h_n|$ gets into the ED in the first place
- [[system-pipeline]] — Stage 6 (ES broadcasts $(S_1^{(n)}, S_2^{(n)})$ per ED) and Stage 5 (ES computes them)
- [[aircomp-basics]] — the channel/MSE model these utilities are defined against
- [[paper-unregrettable-hpsr]] — Eqs 5–6 define the utility that decomposes this way

## Sources / further reading
- `aircomp-regret-pluto/python_reference/asset_spec/regret_matching.py` — reference implementation of $S_1$, $S_2$, $u_n$.
- `aircomp-regret-pluto/firmware/ed/regret_learning.c` — C port used on the ARM.
