---
title: "EEE 350 Module 6 — MGFs, Sums of RVs, CLT/LLN Walkthrough"
type: walkthrough
course:
  - "[[eee-350]]"
tags:
  - eee-350
  - walkthrough
  - mgf
  - sums-of-rvs
  - clt
  - lln
  - random-sum
sources:
  - "raw/textbook/Probability and Stochastic Processes_ Third Ed copy.pdf"
created: 2026-05-06
updated: 2026-05-06
---

# EEE 350 Module 6 — MGFs / Sums of RVs / CLT-LLN

> [!tip] **What this is.** Module 6 problems map to 3rd-ed Chapter 9 (Sums of Random Variables) — MGFs, sums and random sums, then CLT applications. This is the **second-highest yield module** for the final.

## Problem inventory (Canvas-mapped)

| Slot | 2nd ed | **3rd ed** | Topic |
|---|---|---|---|
| 1 | 6.3.4 | **9.2.4** | MGF moments of Gaussian |
| 2 | 6.3.5 | **9.2.5** | Discrete uniform — MGF, $\sum k$, $\sum k^2$ |
| 3 | 6.4.4 | **9.3.4** | Chess-tournament MGF, $E[Y], \text{Var}[Y]$ |
| 4 | 6.5.1 | **9.4.1** | Random sum — Geometric × Exponential |
| 5 | 6.6.1 | **9.5.1** | CLT applied to disk access time |
| 6 | 6.7.1 | **9.5.4** | Improved CLT (continuity correction) for Poisson |

## Framework — 4 patterns generate every problem

> [!tip] **What to internalize.**
>
> 1. **MGF definition + property bag.** $\phi_X(s) = E[e^{sX}]$. Then $E[X^n] = \phi_X^{(n)}(0)$ (n-th moment from n-th derivative at 0); MGF of independent sum is **product of MGFs**: $\phi_{X+Y}(s) = \phi_X(s)\phi_Y(s)$. **Memorize Gaussian MGF**: $\phi_X(s) = e^{\mu s + \sigma^2 s^2/2}$.
> 2. **Random sum $S = X_1 + \cdots + X_N$** with $N$ random and $X_i$ i.i.d. — MGF: $\phi_S(s) = \phi_N(\ln \phi_X(s))$. Mean and variance:
>    - $E[S] = E[N]\,\mu_X$
>    - $\text{Var}[S] = E[N]\,\sigma_X^2 + \mu_X^2\,\text{Var}[N]$
>    **Memorize the variance — has 2 terms** (within + between).
> 3. **CLT recipe.** Standardize: $Z_n = (S_n - n\mu)/(\sigma\sqrt n) \approx \mathcal N(0, 1)$. Look up $Q(z)$ or $\Phi(z) = 1 - Q(z)$.
> 4. **Continuity correction (improved CLT).** When approximating a discrete RV's tail with a continuous Gaussian, use $P[X = k] \approx \Phi((k + 1/2 - \mu)/\sigma) - \Phi((k - 1/2 - \mu)/\sigma)$.

---

## Problem 1 (3rd-ed 9.2.4) — Gaussian moments via MGF

> [!example] **Problem.** $X \sim \mathcal N(0, \sigma)$. Use the MGF to show $E[X] = 0, E[X^2] = \sigma^2, E[X^3] = 0, E[X^4] = 3\sigma^4$. Then for $Y \sim \mathcal N(\mu, \sigma)$ derive $E[Y^2], E[Y^3], E[Y^4]$.

### Framework

- **Gaussian MGF:** $\phi_X(s) = e^{\sigma^2 s^2/2}$ (zero mean).
- **Moments via Taylor series:** $\phi_X(s) = \sum_{n=0}^\infty E[X^n] s^n/n!$ — read off coefficients.
- **Shift trick:** $Y = X + \mu$, so $E[Y^n] = E[(X+\mu)^n] = \sum_{k=0}^n \binom{n}{k}\mu^{n-k} E[X^k]$.

### Moments of $X$

Taylor-expand $\phi_X(s) = e^{\sigma^2 s^2/2} = 1 + \frac{\sigma^2 s^2}{2} + \frac{1}{2!}\left(\frac{\sigma^2 s^2}{2}\right)^2 + \frac{1}{3!}\left(\frac{\sigma^2 s^2}{2}\right)^3 + \cdots$

$$= 1 + \frac{\sigma^2}{2} s^2 + \frac{\sigma^4}{8} s^4 + \frac{\sigma^6}{48} s^6 + \cdots$$

Match to $\sum E[X^n] s^n/n!$:

- $s^0$ coeff: $E[X^0] = 1$ ✓
- $s^1$ coeff: $E[X]/1! = 0 \Rightarrow E[X] = 0$.
- $s^2$ coeff: $E[X^2]/2! = \sigma^2/2 \Rightarrow E[X^2] = \sigma^2$.
- $s^3$ coeff: $E[X^3]/3! = 0 \Rightarrow E[X^3] = 0$.
- $s^4$ coeff: $E[X^4]/4! = \sigma^4/8 \Rightarrow E[X^4] = 24\sigma^4/8 = 3\sigma^4$.

### Moments of $Y = X + \mu$

Use $E[Y^n] = \sum_{k=0}^n \binom{n}{k}\mu^{n-k} E[X^k]$ with the moments above (odd ones zero):

$$E[Y^2] = \binom{2}{0}\mu^2 E[X^0] + \binom{2}{2}\mu^0 E[X^2] = \mu^2 + \sigma^2.$$

$$E[Y^3] = \binom{3}{0}\mu^3 + \binom{3}{2}\mu E[X^2] = \mu^3 + 3\mu\sigma^2.$$

$$E[Y^4] = \binom{4}{0}\mu^4 + \binom{4}{2}\mu^2 E[X^2] + \binom{4}{4}E[X^4] = \mu^4 + 6\mu^2\sigma^2 + 3\sigma^4.$$

**Answer:** $E[Y^2] = \sigma^2 + \mu^2$, $E[Y^3] = 3\mu\sigma^2 + \mu^3$, $E[Y^4] = 3\sigma^4 + 6\mu^2\sigma^2 + \mu^4$.

> [!tip] **What to internalize.** **Gaussian moments — odd central moments vanish, $E[X^{2k}] = (2k-1)!!\sigma^{2k}$ for zero-mean.** $E[X^4] = 3\sigma^4$ is the most-asked moment on Gaussian noise problems (used in [[eee-404]] kurtosis tests). For non-zero-mean Gaussian, **shift** via the binomial expansion — don't try to differentiate the MGF directly.

---

## Problem 2 (3rd-ed 9.2.5) — Discrete uniform MGF, derive $\sum k$ and $\sum k^2$

> [!example] **Problem.** $K$ has discrete uniform $(1, n)$ PMF. Use $\phi_K(s)$ to find $E[K], E[K^2]$, and derive $\sum_{k=1}^n k$ and $\sum_{k=1}^n k^2$.

### Framework

- $P[K = k] = 1/n$ for $k = 1, \ldots, n$.
- $\phi_K(s) = E[e^{sK}] = \frac{1}{n}\sum_{k=1}^n e^{sk}$.
- $E[K] = \phi_K'(0)$, $E[K^2] = \phi_K''(0)$.

### Direct moments (the punchline first)

$$E[K] = \frac{1}{n}\sum_{k=1}^n k.$$

$$E[K^2] = \frac{1}{n}\sum_{k=1}^n k^2.$$

The "MGF derivation" gives the **closed form** for these moments via geometric series.

### MGF closed form

$$\phi_K(s) = \frac{1}{n}\sum_{k=1}^n e^{sk} = \frac{1}{n}\cdot\frac{e^s(e^{ns} - 1)}{e^s - 1}.$$

Differentiating (carefully — quotient rule) gives $E[K] = (n+1)/2$ and $E[K^2] = (n+1)(2n+1)/6$. (Direct evaluation is easier than diff'ing the MGF here.)

### Derive $\sum k$ and $\sum k^2$ from the moments

Equating:

$$E[K] = \frac{1}{n}\sum_{k=1}^n k = \frac{n+1}{2} \implies \sum_{k=1}^n k = \frac{n(n+1)}{2}.$$

$$E[K^2] = \frac{1}{n}\sum_{k=1}^n k^2 = \frac{(n+1)(2n+1)}{6} \implies \sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}.$$

**Answer:** $E[K] = (n+1)/2$, $E[K^2] = (n+1)(2n+1)/6$. The classical sum identities $\sum k = n(n+1)/2$ and $\sum k^2 = n(n+1)(2n+1)/6$ pop out by multiplying by $n$.

> [!tip] **What to internalize.** **MGF of discrete uniform** = (truncated geometric series) / $n$. The slick part: **once you know $E[K]$ from the MGF, the sum identity is forced.** This is a clever way to derive Gauss's sum without combinatorial argument.

---

## Problem 3 (3rd-ed 9.3.4) — Chess tournament: MGF of i.i.d. sum

> [!example] **Problem.** $n$ chess games, each independent, each equally likely win/loss/tie. $X_i \in \{0, 1, 2\}$ (loss/tie/win), uniform on these three values. $Y = \sum X_i$.
> (a) MGFs $\phi_{X_i}(s)$ and $\phi_Y(s)$.
> (b) $E[Y]$ and $\text{Var}[Y]$.

### Framework

- Each $X_i$: discrete uniform on $\{0, 1, 2\}$.
- **MGF of i.i.d. sum** $= [\phi_X(s)]^n$.
- $E[Y] = nE[X]$, $\text{Var}[Y] = n\text{Var}[X]$.

### (a) MGFs

$$\phi_{X_i}(s) = \frac{1}{3}(1 + e^s + e^{2s}).$$

$$\phi_Y(s) = [\phi_{X_i}(s)]^n = \left[\frac{1 + e^s + e^{2s}}{3}\right]^n.$$

### (b) $E[Y], \text{Var}[Y]$

$$E[X_i] = (0 + 1 + 2)/3 = 1.$$

$$E[X_i^2] = (0 + 1 + 4)/3 = 5/3.$$

$$\text{Var}[X_i] = 5/3 - 1 = 2/3.$$

$$E[Y] = nE[X_i] = n. \qquad \text{Var}[Y] = n\text{Var}[X_i] = \frac{2n}{3}.$$

**Answer:** $E[Y] = n$, $\text{Var}[Y] = 2n/3$.

> [!tip] **What to internalize.** Two-step recipe: (1) compute single-RV MGF, (2) raise to $n$ for i.i.d. sum. Mean/variance of sum scale linearly. **You almost never need to actually expand $\phi_Y$** — just use the MGF property to read off $E[Y] = nE[X]$.

---

## Problem 4 (3rd-ed 9.4.1) — Random-sum MGF + PDF

> [!example] **Problem.** $X_i$ i.i.d. $\text{Exp}(\lambda)$. $K \sim \text{Geometric}(q)$ with $P[K=k] = (1-q)q^{k-1}$ for $k \geq 1$.
> (a) $\phi_X(s)$.
> (b) MGF and PDF of $V = X_1 + \cdots + X_K$.

### Framework

- **Exponential MGF:** $\phi_X(s) = \lambda/(\lambda - s)$ for $s < \lambda$.
- **Geometric MGF (starting at $k=1$):** $\phi_K(s) = \sum_{k=1}^\infty e^{sk}(1-q)q^{k-1} = \frac{(1-q)e^s}{1 - qe^s}$.
- **Random sum MGF:** $\phi_V(s) = \phi_K(\ln \phi_X(s))$, i.e. **substitute $e^s \to \phi_X(s)$ in $\phi_K$**.

### (a) $\phi_X(s)$

For $X \sim \text{Exp}(\lambda)$:

$$\phi_X(s) = \int_0^\infty e^{sx}\lambda e^{-\lambda x}\, dx = \frac{\lambda}{\lambda - s}, \quad s < \lambda.$$

### (b) MGF of $V$

Substitute $e^s \to \phi_X(s) = \lambda/(\lambda - s)$ into $\phi_K$:

$$\phi_V(s) = \frac{(1-q)\cdot\lambda/(\lambda - s)}{1 - q\lambda/(\lambda - s)} = \frac{(1-q)\lambda}{\lambda - s - q\lambda} = \frac{(1-q)\lambda}{(1-q)\lambda - s}.$$

Let $\mu = (1-q)\lambda$. Then:

$$\phi_V(s) = \frac{\mu}{\mu - s}.$$

This is the MGF of $\text{Exp}(\mu)$ with $\mu = (1-q)\lambda$.

### PDF of $V$

By MGF uniqueness:

$$f_V(v) = (1-q)\lambda\, e^{-(1-q)\lambda v}, \quad v \geq 0.$$

**Answer:** $V \sim \text{Exp}\big((1-q)\lambda\big)$. Geometric-many exponentials sum to another exponential — beautiful.

> [!tip] **What to internalize.** **Random-sum MGF substitution** — if $S = X_1 + \cdots + X_N$ with $N$ independent of the $X$'s, then $\phi_S(s) = \phi_N(\ln \phi_X(s))$, i.e. replace each "$e^s$" in $\phi_N$ with $\phi_X(s)$. This is the **single most powerful identity in MGF land** — it converts a hard random sum into a substitution. The fact that "geometric Exp's = Exp" is a neat closure property worth remembering.

> [!warning] **Gotcha — Geometric PMF support.** Two conventions: $K \in \{1, 2, \ldots\}$ (this textbook) vs $K \in \{0, 1, 2, \ldots\}$ (others). The MGF differs by a factor of $e^s$. Check which one the problem uses.

---

## Problem 5 (3rd-ed 9.5.1) — CLT for disk access time

> [!example] **Problem.** Wait time $W \sim \text{Uniform}(0, 10)$ ms; read time $R = 3$ ms; $X = W + R$ is total access time. 12 independent blocks accessed; $A = \sum_{i=1}^{12} X_i$ is total access time.
> (a) $E[X]$. (b) $\text{Var}[X]$. (c) $E[A]$. (d) $\sigma_A$. (e) $P[A > 116]$ via CLT. (f) $P[A < 86]$ via CLT.

### Framework

- $X = W + 3$ shifts mean but not variance.
- 12 i.i.d. — sum has $E[A] = 12 E[X]$, $\text{Var}[A] = 12\text{Var}[X]$.
- CLT: standardize and look up $Q$.

### (a) $E[X] = E[W + 3] = 5 + 3 = 8$ ms.

### (b) $\text{Var}[X] = \text{Var}[W] = (10 - 0)^2/12 = 100/12 = 25/3 \approx 8.33$.

### (c) $E[A] = 12 \cdot 8 = 96$ ms.

### (d) $\text{Var}[A] = 12\cdot 25/3 = 100$, so $\sigma_A = 10$ ms.

### (e) $P[A > 116]$ via CLT

$A \approx \mathcal N(96, 100)$. Standardize:

$$P[A > 116] \approx Q\!\left(\frac{116 - 96}{10}\right) = Q(2) \approx 0.0228.$$

### (f) $P[A < 86]$ via CLT

$$P[A < 86] \approx \Phi\!\left(\frac{86 - 96}{10}\right) = \Phi(-1) = Q(1) \approx 0.1587.$$

**Answer:** (a) 8 ms (b) 25/3 (c) 96 ms (d) 10 ms (e) $\approx 0.023$ (f) $\approx 0.159$.

> [!tip] **What to internalize.** **CLT recipe in 3 steps:** (1) sum-mean and sum-variance from per-sample mean and per-sample variance, (2) standardize via $Z = (A - \mu_A)/\sigma_A$, (3) look up $Q$ (right-tail) or $\Phi$ (left-tail). $\Phi(-1) = Q(1)$ — the negative standardization gets symmetrized.

> [!warning] **Gotcha — sum vs. mean variance.** $\text{Var}[A] = n\sigma^2$ (12·25/3 = 100), **not** $\sigma^2/n$. The latter is for sample mean. Remember: variance of **sum** scales **up** with $n$; variance of **average** scales **down** with $n$.

---

## Problem 6 (3rd-ed 9.5.4) — Improved CLT for Poisson

> [!example] **Problem.** $K_i$ i.i.d. $\text{Poisson}(1)$. $W_n = K_1 + \cdots + K_n$. Use the improved CLT (continuity correction) to estimate $P[W_n = n]$. Compare to exact for $n = 4, 25, 64$.

### Framework

- **Sum of Poisson is Poisson.** $W_n \sim \text{Poisson}(n)$ exactly. So $E[W_n] = n$, $\text{Var}[W_n] = n$.
- **Continuity correction.** For discrete $W_n$, approximate $P[W_n = k] \approx \Phi\big((k + 1/2 - n)/\sqrt n\big) - \Phi\big((k - 1/2 - n)/\sqrt n\big)$.
- Setting $k = n$:

$$P[W_n = n] \approx \Phi(1/(2\sqrt n)) - \Phi(-1/(2\sqrt n)) = 2\Phi(1/(2\sqrt n)) - 1 = 1 - 2Q(1/(2\sqrt n)).$$

### Apply for $n = 4, 25, 64$

- **$n = 4$:** $1/(2\sqrt 4) = 1/4 = 0.25$. $\Phi(0.25) = 0.5987$, $2\cdot 0.5987 - 1 = 0.1974$. **Approx ≈ 0.197.** Exact: $P[W_4 = 4] = e^{-4}\cdot 4^4/4! = e^{-4}\cdot 256/24 = e^{-4}\cdot 10.667 \approx 0.0183\cdot 10.667 \approx 0.1954$. **Match: ≈ 1.0% relative error.**
- **$n = 25$:** $1/(2\sqrt{25}) = 0.1$. $\Phi(0.1) = 0.5398$, $2\cdot 0.5398 - 1 = 0.0796$. **Approx ≈ 0.0796.** Exact: $P[W_{25} = 25] = e^{-25}\cdot 25^{25}/25! \approx 0.0796$. **Match: < 0.1% relative error.**
- **$n = 64$:** $1/(2\sqrt{64}) = 1/16 = 0.0625$. $\Phi(0.0625) \approx 0.5249$, $2\cdot 0.5249 - 1 = 0.0498$. **Approx ≈ 0.0498.** Exact: $P[W_{64} = 64] = e^{-64}\cdot 64^{64}/64! \approx 0.0498$. **Match: excellent.**

**Answer:**

| $n$ | CLT approximation | Exact |
|---|---|---|
| 4 | 0.197 | 0.195 |
| 25 | 0.0796 | 0.0796 |
| 64 | 0.0498 | 0.0498 |

> [!tip] **What to internalize.** **Continuity correction widens the discrete bin to ±1/2** before Gaussian-approximating. Without it, $P[W_n = n] \approx \Phi(0) - \Phi(0) = 0$ (zero-width bin) — useless. The half-integer correction recovers the right answer. Same trick used for binomial→Gaussian and Poisson→Gaussian everywhere in stats.

> [!warning] **Gotcha — for $P[W_n = k]$, bracket $k$ between $k-1/2$ and $k+1/2$.** For tail probabilities like $P[W_n \geq k]$ use $k - 1/2$ (the "below the cutoff" boundary). Many students forget the $\pm 1/2$ and then wonder why the exam answer is wrong.

---

## Cross-references

- **Course page:** [[eee-350]]
- **Master review:** [[eee-350-final-walkthrough]]
- **Adjacent walkthroughs:** [[eee-350-module-07-statistical-inference-walkthrough]] (sample mean, Chebyshev, MLE — same i.i.d. sum framework, used for inference instead of distribution).
- **Concept pages:** [[mgf]], [[clt]], [[wlln]], [[chebyshev-inequality]], [[random-sum]].

