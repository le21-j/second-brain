---
title: Regret-Learning Distributed Power Control
type: concept
course: [[research]]
tags: [aircomp, regret-learning, game-theory, correlated-equilibrium, hart-mas-colell]
sources: [[paper-unregrettable-hpsr]], [[daily-2026-04-23-pluto-deployment-and-regret-learning]]
created: 2026-04-21
updated: 2026-04-26
---

# Regret-Learning Distributed Power Control

## In one line
Each ED iteratively adjusts its transmit-power selection probability based on the regret it experiences for not having played alternative actions — the joint action distribution provably converges to a Correlated Equilibrium (Hart & Mas-Colell 2000).

## Example first
Suppose ED #3 has 10 discrete power levels. It tried $P=0.4$ W last round. Now it computes:
- "If I had played $P=0.6$ W with everyone else fixed, my utility would have been $U_{\text{new}}$."
- "My actual utility was $U_{\text{actual}}$."
- Regret $R(0.4 \to 0.6) = \max(U_{\text{new}} - U_{\text{actual}}, 0)$.

It does this for **every alternative action**. Next round, the probability of switching to any given alternative is proportional to its regret: $\psi(0.6) = R(0.4 \to 0.6) / \mu$. Actions that would have been better are explored more. The probability of sticking with $0.4$ W is the residual.

Over many rounds, this converges to a stable joint distribution — the Correlated Equilibrium.

## The algorithm (from [[paper-unregrettable-hpsr]] Algorithm 1)

**Inputs:** $N$ devices, $L$ discrete power levels per device, inertia $\mu$, convergence threshold $\varepsilon$.

**Per-round for each ED $n$:**

1. **Action selection:** sample $P^t_n \in \mathcal{P}_n = \{0, P_{\max}/L, 2 P_{\max}/L, \ldots, P_{\max}\}$ from current probability vector $\psi^t_n$.
2. **Play:** all EDs transmit, ES receives superposed signal, broadcasts feedback (MSE $+$ aggregate from other EDs).
3. **Regret update:** for each alternative action $a_k \neq a_j = P^t_n$:

$$\Delta_U = U_n(a_k, P^t_{-n}) - U_n(P^t) \quad \text{(counterfactual utility delta)}$$

$$D^t_n[j,k] = \tfrac{t-1}{t} \cdot D^{t-1}_n[j,k] + \tfrac{1}{t} \cdot \Delta_U \quad \text{(running average regret)}$$

$$R^t_n[j,k] = \max(D^t_n[j,k], 0) \quad \text{(positive regret)}$$

4. **Strategy update:**

$$\psi^{t+1}_n(a_k) = R^t_n[j,k] / \mu, \quad \forall a_k \neq a_j$$

$$\psi^{t+1}_n(a_j) = 1 - \sum_{k \neq j} \psi^{t+1}_n(a_k)$$

5. **Convergence check:** empirical action distribution converged?

## The utility function (HPSR Eq 5-6)

$$U_n(P_n, P_{-n}) = \left[\frac{g(|h_n|) \cdot \sqrt{P_n}}{\sqrt{\eta}}\right] \cdot \sum_{n' \neq n} \left[\frac{g(|h_{n'}|) \cdot \sqrt{P_{n'}}}{\sqrt{\eta}}\right] - \left[\frac{g(|h_n|)^2 \cdot P_n}{\eta}\right] \cdot \sum_{n' \neq n} \left[\frac{g(|h_{n'}|)^2 \cdot P_{n'}}{\eta}\right]$$

$$\text{where } g(|h_n|) = \frac{1}{|\log|h_n||^\alpha}, \quad \alpha > 0$$

**Physical meaning:**
- First term rewards ED $n$ for having its weighted signal magnitude align with the aggregate of others — pushes toward magnitude coherence at receiver.
- Second term penalizes excessive power — prevents runaway amplification.
- $g(|h_n|)$ is a **channel-aware projection** that compresses the dynamic range: a very small $|h_n|$ (which would need enormous $P_n$ for TCI) gets a manageable $g(|h_n|)$ value. Prevents the utility from exploding for deep-fade users.

**What ED $n$ needs to compute $U_n$:**
- Its own $|h_n|$ (measured locally from DL beacon).
- Its own $P_n$ (trivially known).
- The aggregate $\sum_{n' \neq n} g(|h_{n'}|) \cdot \sqrt{P_{n'}}$ **and** $\sum_{n' \neq n} g(|h_{n'}|)^2 \cdot P_{n'}$ (broadcast by ES).

The ES can compute these two scalars from the full network state and broadcast them — the EDs **do not need individual per-ED channel gains**. (HPSR is explicit on this in Sec III.)

## Why it converges (Hart & Mas-Colell Theorem 1)

If every player follows the regret-matching procedure, the empirical joint action distribution $x^t(P) = (1/t) \sum_{\tau \leq t} \mathbb{I}[P^\tau = P]$ converges almost surely to the set of Correlated Equilibria of the game.

Intuition: regret measures "how much better could I have done against history?" When all players drive their regret to zero, no one unilaterally benefits from deviating — the definition of equilibrium.

## Inertia parameter $\mu$

$\mu > 0$ controls step size. Must be large enough that $\psi^{t+1}_n(a_j) > 0$ — i.e., each action keeps nonzero probability of being retained.

- **Constant $\mu$:** stable but slow.
- **Adaptive $\mu$ (HPSR Sec IV-D):** $\mu^t = 1/(\text{total regret at time } t)$ — small early (exploration), large late (exploitation). $2$–$3\times$ faster convergence to similar MSE.

**One-round delay.** Adaptive $\mu$ is updated **after** $\psi$ is rebuilt inside `regret_update()`. So round 0's $\psi$ uses the initial $\mu = 3000$, round 1 is the first $\psi$ built with the adapted $\mu$. See [[hmc-psi-rebuild]] § "one-round $\mu$ delay" for the asset_spec line pointers.

## Implementation notes (project-specific)

### Canonical source lives only in `asset_spec/`

The algorithmic ground truth is `python_reference/asset_spec/regret_matching.py`. Everything else — `python_reference/common/`, `ed/`, `es/`, the C port at `firmware/ed/regret_learning.c`, the HDL package in `aircomp_pkg.sv` — points to `asset_spec/` as canonical. `ed/regret_learning.py` and `ed/utility.py` were previously divergent sketches; they are now **thin wrappers** over asset_spec semantics. When in doubt, diff against `asset_spec/`.

### Benchtop config — $L = 4$, $P_{\max} = 1$ mW

For the 4-Pluto bench bring-up we shrink the HPSR paper's $L = 100$ down to $L = 4$:

$$\text{action set} = \texttt{linspace}(P_{\max}/L,\,P_{\max},\,L) = \{0.25,\,0.50,\,0.75,\,1.00\}\text{ mW}$$

Consequences:
- Convergence in $\sim 3$ rounds vs $\sim 50$ at paper scale — useful for fast iteration.
- Regret state scales as $L \times L = 16$ cells $\times\,8$ bytes $\approx 150$ bytes per ED — trivial.
- `config.h` / `config.py` / `aircomp_pkg.sv` all mirror these values via shared macros; don't change $L$ in one place without the others.
- Scale back up to $L = 100$ once studying algorithmic limits rather than hardware bring-up.

### $\psi$ rebuild is not additive

Each round, $\psi$ is rebuilt from zero as $\psi[k] = \max(0,\,D[j,k])/\mu$ for $k \neq j$, then $\psi[j] = 1 - \sum_{k \neq j}\psi[k]$. History lives in $D$ (running average, decayed by $(t-1)/t$), **not in $\psi$**. The common "additive on $25\%$ baseline" intuition describes **Hedge / exponential weights**, a different no-regret family — see [[hmc-psi-rebuild]] for the comparison.

### Exploration floor $\texttt{PSI\_EXPLORATION\_FLOOR} = 10^{-6}$

Without it, $\psi[k] = 0$ permanently locks action $k$ out — can't sample $\to$ can't observe regret $\to$ stuck. The $10^{-6}$ floor keeps HMC convergence valid under environmental change. Constant lives in `firmware/ed/regret_learning.h`.

### Counterfactual utility decomposes via $(S_1, S_2)$

`regret_update()` evaluates $u_{\text{cf}}[k]$ for every candidate $k$ using the per-ED aggregate scalars $S_1^{(n)}$, $S_2^{(n)}$ broadcast by the ES — **never** individual neighbor channels. See [[aircomp-utility-s1-s2]] for the decomposition and privacy/bandwidth implications.

### Pre-flash test pyramid

See [[pre-flash-test-pyramid]] for the 6-layer test hierarchy used to verify this algorithm before reflashing hardware. Current status: Layer 1 (pytest) ✓, Layer 3 (WSL gcc + `test_regret_standalone`) ✓, Layer 2 (HDL sim) deferred to home PC.

## Common mistakes
- **Thinking the ED needs all other EDs' channel gains.** It only needs the two aggregate scalars. Broadcasting N-1 channel values per feedback round wastes bandwidth.
- **Confusing regret with loss.** Regret is *counterfactual* — "how much did I leave on the table by not playing `a_k`?" — not absolute loss.
- **Using Pure Nash Equilibrium instead.** PNE may not exist, may not be reachable. Correlated Equilibrium always exists (Aumann 1974) and is reached by regret matching.

## Related
- [[aircomp-basics]] — the system this is solving
- [[federated-learning]] — the broader ML paradigm this work specializes (OTA-FL flavor of FL).
- [[bandit-regret]] — the **single-agent special case**; Sutton-Barto Ch 2 ancestor; the path Jayden's research lives on
- [[correlated-equilibrium]] — the equilibrium concept
- [[system-pipeline]] — the end-to-end implementation
- [[hmc-psi-rebuild]] — $\psi$ rebuild semantics (vs Hedge additive); $\mu$ delay; exploration floor
- [[aircomp-utility-s1-s2]] — `(S1, S2)` decomposition of the utility used in counterfactual evaluation
- [[pre-flash-test-pyramid]] — how this algorithm is validated across Python / HDL / C layers
- [[pluto-experiment-lifecycle]] — where in the epoch the regret update fires (Stages 6–7)
- [[paper-unregrettable-hpsr]] — the source paper
