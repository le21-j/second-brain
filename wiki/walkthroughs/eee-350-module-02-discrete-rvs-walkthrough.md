---
title: "EEE 350 Module 2 — Counting, Discrete RVs, Expectation, Variance Walkthrough"
type: walkthrough
course:
  - "[[eee-350]]"
tags:
  - eee-350
  - walkthrough
  - discrete-rvs
  - pmf
  - binomial
  - geometric
  - expectation
  - variance
sources:
  - "raw/textbook/Probability and Stochastic Processes_ Third Ed copy.pdf"
created: 2026-05-06
updated: 2026-05-06
---

# EEE 350 Module 2 — Counting, Discrete RVs, Expectation, Variance

> [!tip] **What this is.** Module 2 = discrete RVs and their machinery. Bernoulli, binomial, geometric, Poisson PMFs; CDFs; expectation and variance.

## Problem inventory

| Slot | 2nd ed | **3rd ed** | Topic |
|---|---|---|---|
| 1 | 2.2.3 | **3.2.2** | PMF normalization, even-prob, $P[V > 2]$ |
| 2 | 2.2.9 | **3.2.11** | Cell-phone setup tree, geometric-truncated PMF |
| 3 | 2.3.2 | **3.3.3** | "At least one success in $n$ trials" |
| 4 | 2.3.8 | **3.3.11** | Binomial $n=8$ + indicator |
| 5 | 2.3.10 | **3.3.14** | Negative binomial — 6th caller wins |
| 6 | 2.3.13 | **3.3.18** | Best-of-5 series PMF |
| 7 | 2.4.1 | **3.4.1** | Read CDF graph |
| 8 | 2.4.3 | **3.4.3** | CDF $\to$ PMF |
| 9 | 2.5.9 | **3.5.15** | Doubling strategy: $E[Y]$ |
| 10 | 2.6.6 | **3.6.6** | Cell-phone cost via geometric |
| 11 | 2.8.5 | **3.8.5** | Binomial — std-dev, prob within 1$\sigma$ |

## Framework

> [!tip] **What to internalize.**
>
> 1. **Bernoulli/binomial/geometric/Poisson PMFs.** Memorize: $\text{Bin}(n,p)$: $\binom{n}{k}p^k(1-p)^{n-k}$, mean $np$, variance $np(1-p)$. $\text{Geom}(p)$: $(1-p)^{k-1}p$ (start at $k=1$), mean $1/p$, variance $(1-p)/p^2$. Negative binomial: $r$th success on trial $n$.
> 2. **CDF $\Leftrightarrow$ PMF.** Heights of CDF jumps = PMF values; no jumps = PDF (continuous).
> 3. **Expectation = $\sum x P(x)$.** Variance = $E[X^2] - E[X]^2$.

---

## Problem 1 (3rd-ed 3.2.2) — Normalize a PMF

> [!example] $P_V(v) = cv^2$ for $v \in \{1,2,3,4\}$. Find $c$, $P[V \in \{u^2 : u = 1,2,3,\ldots\}]$, $P[V \text{ even}]$, $P[V > 2]$.

$\sum cv^2 = c(1 + 4 + 9 + 16) = 30c = 1 \Rightarrow c = 1/30$.

$P_V(v)$ = $\{1/30, 4/30, 9/30, 16/30\}$ for $v = 1, 2, 3, 4$.

$V \in \{1, 4, 9, ...\} \cap \{1, 2, 3, 4\} = \{1, 4\}$. Probability = $1/30 + 16/30 = 17/30$.

$V$ even ($v \in \{2, 4\}$) = $4/30 + 16/30 = 20/30 = 2/3$.

$P[V > 2] = P_V(3) + P_V(4) = 9/30 + 16/30 = 25/30 = 5/6$.

**Answer:** $c = 1/30$, $P[V \in \{u^2\}] = 17/30$, $P[V$ even$] = 2/3$, $P[V > 2] = 5/6$.

---

## Problem 2 (3rd-ed 3.2.11) — Cell-phone setup, truncated geometric

> [!example] Phone tries $n=6$ times. Each independent, prob $p$ of success. $K$ = number transmitted. Find PMF of $K$. Probability of busy signal. Min $n$ for $P[\text{busy}] < 0.02$ when $p = 0.9$.

### PMF of $K$

$K = k$ for $k = 1, \ldots, n-1$ means: first $k-1$ failures, then success on $k$-th. $P[K = k] = (1-p)^{k-1}p$.

$K = n$ means: either first $n-1$ failures + success on $n$-th, OR $n$ failures (busy signal). Since the phone stops after $n$ attempts whether or not the $n$-th succeeded:

$$P[K = n] = (1-p)^{n-1}p + (1-p)^n = (1-p)^{n-1}.$$

Wait — re-check: $K$ is "number of messages transmitted in a call attempt." If the phone gets through on $k$-th attempt, $K = k$. If all $n$ attempts fail, the phone still transmitted $n$ messages, so $K = n$. So:

$$P_K(k) = \begin{cases} (1-p)^{k-1} p & k = 1, \ldots, n-1, \\ (1-p)^{n-1} & k = n. \end{cases}$$

(Last case: either success on $n$-th attempt or all $n$ fail, which combines $(1-p)^{n-1}p + (1-p)^n = (1-p)^{n-1}$.)

### Busy signal probability

$P[\text{busy}] = P[\text{all $n$ fail}] = (1-p)^n$.

### Min $n$ for $p = 0.9$, $P[\text{busy}] \leq 0.02$

$(0.1)^n \leq 0.02 \Rightarrow n \geq \log(0.02)/\log(0.1) = -1.699/-1 = 1.699$. So $n \geq 2$.

**Answer:** $n_{\min} = 2$. (With $p = 0.9$, even 2 tries gives $P[\text{busy}] = 0.01 \leq 0.02$.)

---

## Problem 3 (3rd-ed 3.3.3) — At least one success

> [!example] Each transmission independent, prob $p$. Pager receives at least one message in $n$ tries.
> (a) PMF of $K$ = number received successfully. (b) For $p = 0.8$, min $n$ for $P[K \geq 1] \geq 0.95$.

(a) $K \sim \text{Bin}(n, p)$.

(b) $P[K \geq 1] = 1 - (1 - p)^n = 1 - 0.2^n \geq 0.95 \Rightarrow 0.2^n \leq 0.05$. $n \log 0.2 \leq \log 0.05$. $\log 0.2 = -0.699$, $\log 0.05 = -1.301$. $n \geq 1.86$, so $n_{\min} = 2$.

**Answer:** Binomial with parameter $(n, p)$. $n_{\min} = 2$.

---

## Problem 4 (3rd-ed 3.3.11) — Binomial + indicator

> [!example] 8 transmissions, each succeeds with prob $p$. $N$ = successful, $I = \mathbf 1\{N \geq 1\}$.

(a) $N \sim \text{Bin}(8, p)$.

(b) $P[I = 0] = P[N = 0] = (1-p)^8$. $P[I = 1] = 1 - (1-p)^8$.

**Answer:** $N \sim \text{Bin}(8, p)$; $I$ is Bernoulli with parameter $1 - (1-p)^8$.

---

## Problem 5 (3rd-ed 3.3.14) — Negative binomial

> [!example] 6th caller who knows wins. Each caller knows w.p. $p = 0.75$. $L$ = number of calls.
> (a) PMF of $L$. (b) $P[L = 10]$. (c) $P[L \geq 9]$.

### (a) Negative binomial PMF — $L = \ell$ means 5 knowers in first $\ell - 1$ calls, then knower on $\ell$-th:

$$P_L(\ell) = \binom{\ell - 1}{5} p^6 (1-p)^{\ell - 6}, \quad \ell \geq 6.$$

### (b) $P[L = 10]$

$$\binom{9}{5}(0.75)^6(0.25)^4 = 126 \cdot 0.1780 \cdot 0.00391 \approx 0.0876.$$

Let me redo: $\binom{9}{5} = 126$. $0.75^6 = 0.17798$. $0.25^4 = 0.003906$. Product: $126 \times 0.17798 \times 0.003906 \approx 0.0876$.

### (c) $P[L \geq 9] = 1 - P[L \leq 8]$ — sum $\ell = 6, 7, 8$:

$P[L=6] = (0.75)^6 = 0.1780$.
$P[L=7] = 6 \cdot (0.75)^6 \cdot 0.25 = 6 \cdot 0.1780 \cdot 0.25 = 0.267$.
$P[L=8] = 21 \cdot (0.75)^6 \cdot (0.25)^2 = 21 \cdot 0.1780 \cdot 0.0625 = 0.234$.

Sum = $0.679$. So $P[L \geq 9] = 1 - 0.679 = 0.321$.

**Answer:** PMF as above. $P[L = 10] \approx 0.088$. $P[L \geq 9] \approx 0.32$.

---

## Problem 6 (3rd-ed 3.3.18) — Best-of-5 series

> [!example] Best-of-5; either team equally likely to win each game (prob $1/2$). $N$ = total games played, $W$ = Celtics wins, $L$ = Celtics losses.

### (a) PMF of $N$

$N = 3$: One team sweeps. $P[N = 3] = 2 \cdot (1/2)^3 = 1/4$.
$N = 4$: 4 games end with $3-1$. Whichever team wins must win game 4 and 2 of first 3. $P = 2 \cdot \binom{3}{2}(1/2)^4 = 6/16 = 3/8$.
$N = 5$: $P = 1 - 1/4 - 3/8 = 3/8$.

| $n$ | $P_N(n)$ |
|---|---|
| 3 | 1/4 |
| 4 | 3/8 |
| 5 | 3/8 |

### (b) PMF of $W$

$W = 0$: Celtics lose 3-0 = $(1/2)^3 = 1/8$.
$W = 1$: Celtics lose 3-1. Possible orderings: Celtics win exactly one of first 3, Sixers win game 4. $P = \binom{3}{1}(1/2)^4 = 3/16$.
$W = 2$: Celtics lose 3-2. Both teams 2-2 after 4 games (Celtics win 2 of 4), Sixers win game 5. $P = \binom{4}{2}(1/2)^5 = 6/32 = 3/16$.
$W = 3$: Celtics win 3-anything. By symmetry with $W \leq 2$: $P[W = 3] = 1 - 1/8 - 3/16 - 3/16 = 16/16 - 2/16 - 3/16 - 3/16 = 8/16 = 1/2$.

Wait, let me recheck: $P[W \leq 2] = 1/8 + 3/16 + 3/16 = 2/16 + 3/16 + 3/16 = 8/16 = 1/2$. So $P[W = 3] = 1/2$. ✓ (By symmetry with the equal-prob, $P[W = 3] = P[L = 3]$ where $L$ is Sixers wins, but actually $P[W = 3]$ is the prob that Celtics win the series, which by symmetry is $1/2$.)

| $w$ | $P_W(w)$ |
|---|---|
| 0 | 1/8 |
| 1 | 3/16 |
| 2 | 3/16 |
| 3 | 1/2 |

### (c) PMF of $L$

By symmetry $P_L = P_W$ (same form swapped roles).

**Answer:** As above.

---

## Problem 7 (3rd-ed 3.4.1) — Read CDF graph

> [!example] CDF jumps at $y = 1, 2, 3$ to heights $0.25, 0.5, 0.75, 1$.

PMF jumps: $P_Y(1) = 0.25, P_Y(2) = 0.25, P_Y(3) = 0.25, P_Y(4) = 0.25$. (Uniform over $\{1, 2, 3, 4\}$.)

(a) $P[Y \leq 1] = F_Y(1) = 0.25$. $P[Y < 1] = 0$.
(b) $P[Y > 2] = 1 - F_Y(2) = 0.5$. $P[Y \geq 2] = 1 - F_Y(2^-) = 1 - 0.25 = 0.75$.
(c) $P[Y = 3] = 0.25$. $P[Y > 3] = 1 - F_Y(3) = 0.25$.
(d) Uniform over $\{1, 2, 3, 4\}$, each with probability $0.25$.

---

## Problem 8 (3rd-ed 3.4.3) — CDF to PMF

> [!example] $F_X$: 0 below $-3$, $0.4$ on $[-3, 5)$, $0.8$ on $[5, 7)$, 1 on $[7, \infty)$.

PMF: $P_X(-3) = 0.4, P_X(5) = 0.4, P_X(7) = 0.2$.

---

## Problem 9 (3rd-ed 3.5.15) — Doubling strategy

> [!example] You have $63$. Bet $1, 2, 4, 8, 16, 32$. Stop on win. $Y$ = take-home money.

Bets: $1, 2, 4, 8, 16, 32 = 63$ total. After 6 losses, money exhausted, $Y = 0$.

If you win on bet $k$ (after $k-1$ losses), profit = (bet $k$) - (sum of previous bets) = $2^{k-1} - (2^{k-1} - 1) = 1$. So $Y = 64$ on any win.

$P[\text{win on bet }k] = (1/2)^{k-1} \cdot (1/2) = (1/2)^k$ for $k = 1, \ldots, 6$.

$P[\text{6 losses}] = (1/2)^6 = 1/64$.

| $y$ | $P_Y(y)$ |
|---|---|
| 64 | $\sum_{k=1}^6 (1/2)^k = 1 - 1/64 = 63/64$ |
| 0 | $1/64$ |

$$E[Y] = 64 \cdot 63/64 + 0 \cdot 1/64 = 63.$$

**Answer:** $P_Y(64) = 63/64, P_Y(0) = 1/64$. $E[Y] = 63 = $ your starting bankroll. **Game is fair on average — you neither gain nor lose.** Don't play.

> [!warning] **Gotcha — the gambler's ruin.** $E[Y] = $ starting capital is the inevitable result for any fair game. The doubling strategy gives you "small probability of large loss" — high chance to win a tiny amount, tiny chance to lose everything.

---

## Problem 10 (3rd-ed 3.6.6) — Cell-phone cost (geometric)

> [!example] $20/month + 0.50/extra-min beyond 30. $M \sim \text{Geometric}(p = 1/30)$.
> Find PMF of $C$ = cost per month.

$C = 20$ if $M \leq 30$. $C = 20 + 0.5(M - 30)$ if $M > 30$.

$P[M = m] = (1 - p)^{m-1} p = (29/30)^{m-1}(1/30)$ for $m \geq 1$.

$P[C = 20] = P[M \leq 30] = 1 - (29/30)^{30} \approx 1 - 0.362 \approx 0.638$.

For $c > 20$, $c = 20 + 0.5(m - 30)$ means $m = 30 + 2(c - 20)$. The cost goes up by $0.50$ for each minute, so for integer $m > 30$:

$$P[C = 20 + 0.5(m - 30)] = (29/30)^{m-1}(1/30), \quad m = 31, 32, \ldots$$

**Answer:** $P_C(20) = 1 - (29/30)^{30}$. For $c = 20.5, 21, 21.5, \ldots$: $P_C(c) = (29/30)^{2c - 11} (1/30)$.

---

## Problem 11 (3rd-ed 3.8.5) — Binomial std-dev

> [!example] $X \sim \text{Bin}(4, 1/2)$. Find $\sigma_X$ and $P[\mu - \sigma < X < \mu + \sigma]$.

$\mu_X = np = 2$. $\sigma_X^2 = np(1-p) = 1$. $\sigma_X = 1$.

So $P[1 < X < 3] = P[X = 2] = \binom{4}{2}(1/2)^4 = 6/16 = 3/8$.

**Answer:** $\sigma_X = 1$. Probability $= 3/8$.

> [!warning] **Gotcha — strict vs. weak inequality.** "Within one std-dev" usually means $|X - \mu| < \sigma$, strict; check whether the problem means $\leq$. With strict, $X = 1$ and $X = 3$ are excluded; $X = 2$ included.

---

## Cross-references

- **Course page:** [[eee-350]]
- **Master review:** [[eee-350-final-walkthrough]]
- **Adjacent walkthroughs:** [[eee-350-module-03-continuous-rvs-walkthrough]] (continuous-RV counterpart).
- **Concept pages:** [[discrete-rv]], [[pmf]], [[binomial-distribution]], [[geometric-distribution]], [[negative-binomial]], [[poisson-distribution]].

