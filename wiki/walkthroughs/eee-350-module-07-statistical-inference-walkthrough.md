---
title: "EEE 350 Module 7 — Statistical Inference (MLE / MAP / LMSE / NP) Walkthrough"
type: walkthrough
course:
  - "[[eee-350]]"
tags:
  - eee-350
  - walkthrough
  - statistical-inference
  - mle
  - map-estimation
  - mmse
  - lmse
  - hypothesis-testing
  - significance-test
  - neyman-pearson
sources:
  - "raw/textbook/Probability and Stochastic Processes_ Third Ed copy.pdf"
created: 2026-05-06
updated: 2026-05-06
---

# EEE 350 Module 7 — Statistical Inference Walkthrough

> [!tip] **What this is.** Per-problem walkthroughs for the **2nd-edition problems listed in the Canvas Module 7 lecture-materials page**, mapped to their **3rd-edition equivalents** in the Yates & Goodman PDF on disk. This is the **highest-yield module** for the EEE 350 final — Bayesian/MLE/NP estimation and hypothesis testing — built from the 5 inference patterns in [[eee-350-final-walkthrough]] §4.
>
> **Edition mapping.** The mapping is given verbatim by the instructor on the Canvas lecture page: 2nd-ed (3rd-ed in parens). One problem (8.1.4) has no 3rd-ed equivalent; it's flagged below with a placeholder.

## Module 7 problem inventory

| Slot | 2nd ed | **3rd ed** | Topic | Status |
|---|---|---|---|---|
| 1 | 7.1.2 | **10.1.2** | sample mean, CLT estimate | solved |
| 2 | 7.4.2 | **10.3.1** | sample-size from Chebyshev / CLT | solved |
| 3 | 7.1.4 | **10.1.4** | mean & variance of sample mean of differences | solved |
| 4 | 8.1.1 | **11.1.1** | significance test for fair coin (geometric) | solved |
| 5 | 8.1.4 | **(no 3rd-ed equivalent)** | placeholder — see below | placeholder |
| 6 | 8.3.1 | **11.3.1** | MAP/ML decoding ternary ASK in AWGN | solved |
| 7 | 9.1.3 | **12.1.3** | blind / conditional MMSE — uniform triangle | solved |
| 8 | 9.1.4 | **12.1.4** | MMSE estimates from joint PDF $6(y-x)$ | solved |
| 9 | 9.1.5 | **12.1.5** | MMSE conditional MSE — uniform triangle | solved |
| 10 | 9.2.7 | **12.2.6** | MMSE / LMSE — Erlang-2 then conditional uniform | solved |
| 11 | 9.3.3 | **12.3.3** | MMSE / MAP / ML for exponential rate from Poisson count | solved |

## Framework — the 5 patterns that generate every Module 7 problem

> [!tip] **What to internalize vs memorize.**
>
> 1. **Sample-mean variance** — $\text{Var}[M_n(X)] = \sigma^2/n$. **Memorize.** Used in problems 1–3.
> 2. **Concentration-bound dispatch** — Chebyshev (any distribution) vs. CLT (Gaussian via standardization, tighter bound when $\sigma$ small or $n$ large). Use **Chebyshev when no distribution given**; use **CLT/Gaussian when distribution Gaussian or you've been asked for a normal approximation**. Used in problem 2.
> 3. **Significance test scaffold** — pick a **statistic** $T$, fix $\alpha$, derive **rejection region** so that $P[T \in R \mid H_0] \leq \alpha$. Used in problem 4.
> 4. **Bayesian estimator triad** — three optimal-under-different-loss estimators: $\hat\theta_{\text{MAP}} = \arg\max f_{\theta\mid X}$ (0-1 loss), $\hat\theta_M = E[\theta\mid X]$ (squared-error MMSE = LMS), $\hat\theta_L = aX + b$ with $a^* = \text{Cov}/\text{Var}, b^* = \mu_\theta - a^*\mu_X$ (LMSE — best linear under squared-error). **Memorize the $a^*, b^*$ formula** — derive the MMSE integral. Used in problems 7–11.
> 5. **MLE for an exponential family** — $\hat\theta_{\text{ML}} = \arg\max f_{X\mid\theta}$. For Poisson($rT$) given count $n$: $\hat r_{\text{ML}} = n/T$. Used in problem 11.
>
> **One detection problem (problem 6)** uses the MAP-decoding framework for AWGN: split the real line at midpoints between adjacent signal amplitudes, compute pairwise error using $Q$-function, sum.

---

## Problem 1 (3rd-ed 10.1.2) — Sample-mean variance and CLT estimate

> [!example] **Problem.** $X_1, \ldots, X_n$ are i.i.d. uniform with $E[X] = \mu_X = 7$ and $\text{Var}[X] = 3$.
> (a) PDF of $X_1$.
> (b) $\text{Var}[M_{16}(X)]$.
> (c) $P[X_1 > 9]$.
> (d) Compare $P[M_{16}(X) > 9]$ to $P[X_1 > 9]$ (use CLT to estimate).

### Framework

- **Building blocks.** Uniform-on-interval mean/variance identities, sample-mean variance scaling $\sigma^2/n$, CLT standardization.

### (a) PDF of $X_1$

For continuous uniform on $[a,b]$: $\mu = (a+b)/2$, $\sigma^2 = (b-a)^2/12$. Solve the system:

$$\frac{a+b}{2} = 7 \Rightarrow a+b = 14, \qquad \frac{(b-a)^2}{12} = 3 \Rightarrow (b-a)^2 = 36 \Rightarrow b-a = 6.$$

So $a = 4, b = 10$.

$$f_{X_1}(x) = \begin{cases} 1/6 & 4 \leq x \leq 10 \\ 0 & \text{otherwise} \end{cases}.$$

### (b) Variance of sample mean

For i.i.d. samples, $\text{Var}[M_n(X)] = \sigma^2/n$:

$$\text{Var}[M_{16}(X)] = \frac{3}{16} = 0.1875.$$

### (c) $P[X_1 > 9]$

Direct integration of the uniform PDF:

$$P[X_1 > 9] = \int_9^{10} \frac{1}{6}\,dx = \frac{1}{6} \approx 0.1667.$$

### (d) Compare to $P[M_{16}(X) > 9]$ via CLT

Sample mean $M_{16}$ has $E[M_{16}] = 7$, $\text{Var}[M_{16}] = 3/16$, so $\sigma_{M_{16}} = \sqrt{3/16} = \sqrt{3}/4 \approx 0.433$. By CLT, $M_{16}(X) \approx \mathcal N(7, 3/16)$. Standardize:

$$P[M_{16} > 9] \approx Q\!\left(\frac{9 - 7}{\sqrt{3/16}}\right) = Q\!\left(\frac{2}{\sqrt{3}/4}\right) = Q\!\left(\frac{8}{\sqrt{3}}\right) = Q(4.62).$$

$Q(4.62) \approx 1.9 \times 10^{-6}$.

**Answer:** $P[M_{16}(X) > 9] \approx Q(4.62) \approx 1.9 \times 10^{-6}$, **vastly smaller** than $P[X_1 > 9] \approx 1/6$, exactly because the sample mean concentrates: sampling-mean variance is $1/16$ of the single-sample variance, so the tail above 9 is far less likely.

> [!warning] **Gotcha.** This is the problem with the instructor's video errata — Tepedelenlioglu's slide gives the wrong number for $Q$ at the standardized argument. The standardized argument is $8/\sqrt{3} \approx 4.62$ (not whatever the slides claim). $Q(4.62)$ is off-table for most $z$-tables; quote it as $\approx 1.9 \times 10^{-6}$ from the standard-normal density tail or via a tail expansion.

> [!tip] **What to internalize.** Two-step recipe: $\text{Var}[M_n] = \sigma^2/n$, then standardize against the **sample-mean** standard deviation $\sigma/\sqrt{n}$, not the single-sample $\sigma$. Forgetting the $/\sqrt n$ is the most common Module-6/7 mistake.

---

## Problem 2 (3rd-ed 10.3.1) — Sample size from Chebyshev vs. CLT

> [!example] **Problem.** $X_1, X_2, \ldots$ i.i.d. with $E[X] = 75, \sigma_X = 15$.
> (a) How many samples $n$ to guarantee $P[74 \leq M_n(X) \leq 76] \geq 0.99$?
> (b) If each $X_i$ is Gaussian, how many samples $n'$?

### Framework

- **(a) Chebyshev** because we don't know the distribution.
- **(b) CLT/Gaussian standardization** because we know it's Gaussian (so the sample mean is exactly Gaussian — no approximation needed).

### (a) Chebyshev

Chebyshev: $P[|M_n - \mu| \geq c] \leq \sigma_{M_n}^2/c^2 = \sigma^2/(nc^2)$.

We want $P[|M_n - 75| < 1] \geq 0.99$, i.e. $P[|M_n - 75| \geq 1] \leq 0.01$. Set $c = 1$:

$$\frac{15^2}{n \cdot 1^2} \leq 0.01 \implies n \geq \frac{225}{0.01} = 22{,}500.$$

**Answer:** $n \geq 22{,}500$ samples (Chebyshev bound).

### (b) Gaussian / exact

If $X_i \sim \mathcal N(75, 15^2)$, then $M_n \sim \mathcal N(75, 15^2/n)$. With $\sigma_{M_n} = 15/\sqrt n$:

$$P[|M_n - 75| < 1] = 1 - 2Q\!\left(\frac{1}{15/\sqrt n}\right) = 1 - 2Q(\sqrt n / 15).$$

We want $\geq 0.99$, i.e. $2Q(\sqrt n/15) \leq 0.01$, i.e. $Q(\sqrt n/15) \leq 0.005$. From the $Q$-table, $Q(2.576) = 0.005$, so

$$\frac{\sqrt n}{15} \geq 2.576 \implies n \geq (2.576 \times 15)^2 = 38.64^2 \approx 1493.$$

**Answer:** $n' \geq 1493$ samples (Gaussian / CLT bound).

> [!tip] **What to internalize.** **Chebyshev / CLT ratio is the punchline** — same problem, but knowing the distribution gives a **15× tighter** sample-size requirement. The $z_{0.005} = 2.576$ critical value is worth memorizing alongside $z_{0.025} = 1.96, z_{0.05} = 1.645$.

> [!warning] **Gotcha.** Two-tail confidence interval: probability $0.99$ means $\alpha = 0.01$ split into two tails of $0.005$ each, so use $z_{0.005} = 2.576$ — **not** $z_{0.01} = 2.33$. The "two-tail" framing is hidden inside $|M_n - \mu| < c$.

---

## Problem 3 (3rd-ed 10.1.4) — Sample mean of differenced sequence

> [!example] **Problem.** $Y_n = X_{2n-1} - X_{2n}$ from i.i.d. $X_i$ with $\text{Var}[X]$.
> (a) Find $E[Y_n]$ and $\text{Var}[Y_n]$.
> (b) Find $E$ and $\text{Var}$ of $M_n(Y) = \frac{1}{n}\sum_{i=1}^n Y_i$.

### Framework

- **Linearity of expectation** for the mean.
- **Variance of independent sum/difference** — $\text{Var}[X_a - X_b] = \text{Var}[X_a] + \text{Var}[X_b]$ (the **+ not −** because variance of $-X_b$ is the same as of $X_b$).
- **Sample-mean scaling** for the second part.

### (a)

Each $Y_n = X_{2n-1} - X_{2n}$, with $X_i$ i.i.d.:

$$E[Y_n] = E[X_{2n-1}] - E[X_{2n}] = 0.$$

$$\text{Var}[Y_n] = \text{Var}[X_{2n-1}] + \text{Var}[X_{2n}] = 2\,\text{Var}[X].$$

### (b)

The $Y_i$ are independent (each uses a disjoint pair of $X$'s) and identically distributed. So $M_n(Y)$ is a sample mean of i.i.d. zero-mean RVs with variance $2\text{Var}[X]$:

$$E[M_n(Y)] = E[Y_1] = 0.$$

$$\text{Var}[M_n(Y)] = \frac{\text{Var}[Y_1]}{n} = \frac{2\,\text{Var}[X]}{n}.$$

**Answer:** $E[Y_n] = 0$, $\text{Var}[Y_n] = 2\,\text{Var}[X]$; $E[M_n(Y)] = 0$, $\text{Var}[M_n(Y)] = 2\,\text{Var}[X]/n$.

> [!tip] **What to internalize.** **Variance of a difference adds, never subtracts** ($\text{Var}[X-Y] = \text{Var}[X] + \text{Var}[Y]$ when independent). The construction $Y_n = X_{2n-1} - X_{2n}$ uses **disjoint pairs**, so the $Y$'s themselves are i.i.d. — that's why the sample-mean formula applies cleanly.

---

## Problem 4 (3rd-ed 11.1.1) — Significance test for fair coin from one geometric trial

> [!example] **Problem.** $L$ = number of flips up to and including first heads. Devise a significance test at $\alpha = 0.05$ for $H_0$: coin is fair. What are the test's limitations?

### Framework

- **Statistic:** under $H_0$, $L \sim \text{Geometric}(1/2)$, so $P[L = \ell \mid H_0] = (1/2)^\ell$ for $\ell = 1, 2, \ldots$.
- **Reject when $L$ is "extreme."** Large $L$ = many tails before a head = suggests coin biased toward tails.
- **Threshold:** smallest $\ell^*$ such that $P[L \geq \ell^* \mid H_0] \leq 0.05$.

### Build the rejection region

$$P[L \geq \ell^* \mid H_0] = \sum_{\ell = \ell^*}^{\infty} (1/2)^\ell = (1/2)^{\ell^* - 1}.$$

(geometric-tail formula). We want this $\leq 0.05$:

$$(1/2)^{\ell^* - 1} \leq 0.05 \implies \ell^* - 1 \geq \log_2(20) \approx 4.32 \implies \ell^* \geq 5.32.$$

So $\ell^* = 6$ — but check: with $\ell^* = 6$, $P[L \geq 6] = (1/2)^5 = 1/32 = 0.03125 \leq 0.05$. ✓ With $\ell^* = 5$, $P[L \geq 5] = (1/2)^4 = 1/16 = 0.0625 > 0.05$. ✗

**Test:** Reject $H_0$ if $L \geq 6$. Significance level $= 1/32 \approx 0.0313$.

**Answer:** Reject the fair-coin hypothesis if **$L \geq 6$ flips before getting heads**. Actual $\alpha = 1/32 \approx 0.03$ (≤ 0.05 as required).

### Limitations

> [!warning] **Gotcha — the "limitations" prompt.** This is a **one-sided test** that only catches **tails-biased** coins. If the coin is biased toward **heads** (so heads comes very fast), $L$ will be small — but $L = 1$ has probability $1/2$ under $H_0$, so heads-biased coins look unsuspicious in this test. The test has **zero power** against the alternative "$p_{\text{heads}} > 1/2$." Also: **only one trial**, so the test is statistically weak — many real coins would pass the test.

> [!tip] **What to internalize.** **Significance test recipe** — (1) choose statistic, (2) compute its $H_0$ distribution, (3) pick rejection region in the tail(s) where the alternative is more likely, (4) set the cutoff so the tail probability under $H_0$ equals $\alpha$. The $\alpha$ refers to the **probability of false rejection**, *not* the probability of any individual outcome.

---

## Problem 5 (2nd-ed 8.1.4) — Placeholder

> [!warning] **No 3rd-edition equivalent on the Canvas mapping.** The Canvas Module 7 page lists problem 8.1.4 (2nd ed) with a `✗` for the 3rd-ed slot, indicating no clean equivalent exists. If you find the video for this slot, the framework will almost certainly be **another significance test** (since 8.1 is the significance-test section in both editions). Same recipe as Problem 4 above.
>
> **Recommendation:** if the video covers a $\chi^2$ variance test, two-sided mean test, or Poisson-rate significance test, the recipe is identical: (1) statistic, (2) $H_0$ distribution, (3) rejection region from the $\alpha$ tail.

---

## Problem 6 (3rd-ed 11.3.1) — MAP detection in ternary ASK + AWGN

> [!example] **Problem.** Ternary ASK with three equally likely signals $\{s_0, s_1, s_2\}$ where if $s_i$ is sent, $X = a(i-1) + N$ with $N \sim \mathcal N(0, \sigma_N^2)$ and $a > 0$. Decode from $X$.
> (a) Acceptance sets $A_i$.
> (b) $P[D_e]$ — overall error probability.

### Framework

- **MAP decoder for equal priors = ML decoder.** Each $X \mid H_i \sim \mathcal N(a(i-1), \sigma_N^2)$ — three Gaussians with means $-a, 0, +a$ and equal variance.
- **For equal priors and equal variances, decision boundaries are midpoints** between adjacent means.

### (a) Acceptance sets

Means: $H_0 \to -a$, $H_1 \to 0$, $H_2 \to +a$. Midpoints: $-a/2$ between $H_0, H_1$ and $+a/2$ between $H_1, H_2$.

$$A_0 = (-\infty, -a/2], \quad A_1 = (-a/2, +a/2], \quad A_2 = (a/2, +\infty).$$

### (b) Error probability

By symmetry, errors from $H_0$ and $H_2$ are equal; $H_1$ has both sides.

**Error from $H_0$ ($X = -a + N$):** decode wrong iff $X > -a/2$, i.e. $N > a/2$:

$$P[D_e \mid H_0] = Q(a/(2\sigma_N)).$$

By symmetry, $P[D_e \mid H_2] = Q(a/(2\sigma_N))$.

**Error from $H_1$ ($X = N$):** decode wrong iff $|N| > a/2$:

$$P[D_e \mid H_1] = 2 Q(a/(2\sigma_N)).$$

Total (equal priors, weight by $1/3$):

$$P[D_e] = \frac{1}{3}\left[Q(a/(2\sigma_N)) + 2Q(a/(2\sigma_N)) + Q(a/(2\sigma_N))\right] = \frac{4}{3} Q\!\left(\frac{a}{2\sigma_N}\right).$$

**Answer:** $A_0 = (-\infty, -a/2]$, $A_1 = (-a/2, a/2]$, $A_2 = (a/2, \infty)$. $P[D_e] = \frac{4}{3} Q\!\left(\frac{a}{2\sigma_N}\right)$.

> [!tip] **What to internalize.** **Equal priors $\Rightarrow$ midpoint thresholds.** Inner constellation points (here $H_1$) have **two-sided error** so contribute $2Q(\cdot)$; edge points (here $H_0, H_2$) have **one-sided error** so contribute $Q(\cdot)$. The factor of $4/3$ in $P[D_e]$ comes from $(1+2+1)/3$, **not** any deeper magic — count the error tails.

> [!warning] **Gotcha — unequal priors.** If priors are unequal, push thresholds **toward the less-likely** signal: $\tau_{0,1} = -a/2 + (\sigma_N^2/a)\ln(\pi_0/\pi_1)$. Rare on this exam, but listed in the formula sheet.

---

## Problem 7 (3rd-ed 12.1.3) — Blind / conditional MMSE for uniform-triangle joint

> [!example] **Problem.** $f_{X,Y}(x,y) = 2$ for $0 < x < y < 1$, else 0.
> (a) $f_X(x)$.
> (b) Blind estimate $\hat x_B$.
> (c) MMSE estimate of $X$ given $X > 1/2$.
> (d) $f_Y(y)$.
> (e) Blind estimate $\hat y_B$.
> (f) MMSE estimate of $Y$ given $X > 1/2$.

### Framework

- **Marginalize** by integrating out the other variable over the support.
- **Blind estimate (no observation) = mean of the prior** — minimizes squared error.
- **Conditional MMSE on event** = conditional expectation given that event.

### (a) $f_X(x)$

Marginalize $y$ over $(x, 1)$:

$$f_X(x) = \int_x^1 2\, dy = 2(1 - x), \quad 0 < x < 1.$$

### (b) Blind estimate $\hat x_B = E[X]$

$$E[X] = \int_0^1 x \cdot 2(1-x)\, dx = 2\int_0^1 (x - x^2)\, dx = 2\left[\frac{1}{2} - \frac{1}{3}\right] = 2\cdot\frac{1}{6} = \frac{1}{3}.$$

$\boxed{\hat x_B = 1/3.}$

### (c) MMSE of $X$ given $X > 1/2$

$$E[X \mid X > 1/2] = \frac{\int_{1/2}^1 x \cdot 2(1-x)\, dx}{P[X > 1/2]}.$$

Numerator: $2\int_{1/2}^1 (x - x^2)\, dx = 2\left[\frac{x^2}{2} - \frac{x^3}{3}\right]_{1/2}^1 = 2\left[(1/2 - 1/3) - (1/8 - 1/24)\right] = 2\left[\frac{1}{6} - \frac{2}{24}\right] = 2\left[\frac{4 - 2}{24}\right] = \frac{4}{24} = \frac{1}{6}$.

Denominator: $P[X > 1/2] = \int_{1/2}^1 2(1-x)\, dx = 2\left[x - \frac{x^2}{2}\right]_{1/2}^1 = 2\left[(1 - 1/2) - (1/2 - 1/8)\right] = 2\left[\frac{1}{2} - \frac{3}{8}\right] = 2\cdot\frac{1}{8} = \frac{1}{4}$.

$$E[X \mid X > 1/2] = \frac{1/6}{1/4} = \frac{4}{6} = \frac{2}{3}.$$

### (d) $f_Y(y)$

Marginalize $x$ over $(0, y)$:

$$f_Y(y) = \int_0^y 2\, dx = 2y, \quad 0 < y < 1.$$

### (e) Blind estimate $\hat y_B = E[Y]$

$$E[Y] = \int_0^1 y \cdot 2y\, dy = 2\int_0^1 y^2\, dy = \frac{2}{3}.$$

### (f) MMSE of $Y$ given $X > 1/2$

$$E[Y \mid X > 1/2] = \frac{\int\int_{x > 1/2} y \cdot 2\, dy\, dx}{P[X > 1/2]}.$$

Numerator: integrate $y$ over the support intersected with $\{x > 1/2\}$, i.e. $1/2 < x < y < 1$:

$$\int_{1/2}^1 \int_x^1 2y\, dy\, dx = \int_{1/2}^1 \left[y^2\right]_x^1 dx = \int_{1/2}^1 (1 - x^2)\, dx.$$

$$= \left[x - \frac{x^3}{3}\right]_{1/2}^1 = \left(1 - \frac{1}{3}\right) - \left(\frac{1}{2} - \frac{1}{24}\right) = \frac{2}{3} - \frac{11}{24} = \frac{16 - 11}{24} = \frac{5}{24}.$$

Denominator: $P[X > 1/2] = 1/4$ (from part c).

$$E[Y \mid X > 1/2] = \frac{5/24}{1/4} = \frac{5}{6}.$$

**Answer:** $f_X(x) = 2(1-x)$ on $(0,1)$; $\hat x_B = 1/3$; $E[X \mid X > 1/2] = 2/3$. $f_Y(y) = 2y$ on $(0,1)$; $\hat y_B = 2/3$; $E[Y \mid X > 1/2] = 5/6$.

> [!tip] **What to internalize.** **Blind estimate is just the marginal mean.** Conditional-on-event MMSE = conditional expectation = (conditional density × variable, integrated) = (joint integrated over event, scaled by event probability). Watch the integration order — when conditioning on $X > 1/2$, the inner $y$-integral has limits $(x, 1)$ from the support constraint $x < y$.

---

## Problem 8 (3rd-ed 12.1.4) — MMSE estimates from joint $6(y-x)$

> [!example] **Problem.** $f_{X,Y}(x,y) = 6(y-x)$ for $0 < x < y < 1$, else 0.
> (a) $f_{X\mid Y}(x \mid y)$.
> (b) $\hat X_M(y)$ — MMSE estimate of $X$ given $Y = y$.
> (c) $f_{Y\mid X}(y \mid x)$.
> (d) $\hat Y_M(x)$ — MMSE estimate of $Y$ given $X = x$.

### Framework

- **MMSE estimate = conditional expectation.** $\hat X_M(y) = E[X \mid Y = y]$ minimizes $E[(X - g(Y))^2]$ over all functions $g$.
- **Conditional density:** $f_{X\mid Y}(x\mid y) = f_{X,Y}(x,y)/f_Y(y)$.

### (a) $f_{X\mid Y}(x\mid y)$

$f_Y(y) = \int_0^y 6(y-x)\, dx = 6\left[yx - \frac{x^2}{2}\right]_0^y = 6\left(y^2 - \frac{y^2}{2}\right) = 3y^2$ for $0 < y < 1$.

$$f_{X\mid Y}(x\mid y) = \frac{6(y-x)}{3y^2} = \frac{2(y-x)}{y^2}, \quad 0 < x < y.$$

### (b) $\hat X_M(y) = E[X \mid Y = y]$

$$E[X \mid Y = y] = \int_0^y x \cdot \frac{2(y - x)}{y^2}\, dx = \frac{2}{y^2}\int_0^y (xy - x^2)\, dx.$$

$$= \frac{2}{y^2}\left[\frac{x^2 y}{2} - \frac{x^3}{3}\right]_0^y = \frac{2}{y^2}\left[\frac{y^3}{2} - \frac{y^3}{3}\right] = \frac{2}{y^2}\cdot\frac{y^3}{6} = \frac{y}{3}.$$

$\boxed{\hat X_M(y) = y/3.}$

### (c) $f_{Y\mid X}(y\mid x)$

$f_X(x) = \int_x^1 6(y - x)\, dy = 6\left[\frac{y^2}{2} - xy\right]_x^1 = 6\left[\left(\frac{1}{2} - x\right) - \left(\frac{x^2}{2} - x^2\right)\right] = 6\left(\frac{1}{2} - x + \frac{x^2}{2}\right) = 3(1-x)^2$ for $0 < x < 1$.

$$f_{Y\mid X}(y\mid x) = \frac{6(y-x)}{3(1-x)^2} = \frac{2(y-x)}{(1-x)^2}, \quad x < y < 1.$$

### (d) $\hat Y_M(x) = E[Y \mid X = x]$

$$E[Y \mid X = x] = \int_x^1 y \cdot \frac{2(y - x)}{(1-x)^2}\, dy = \frac{2}{(1-x)^2}\int_x^1 (y^2 - xy)\, dy.$$

$$= \frac{2}{(1-x)^2}\left[\frac{y^3}{3} - \frac{xy^2}{2}\right]_x^1 = \frac{2}{(1-x)^2}\left[\left(\frac{1}{3} - \frac{x}{2}\right) - \left(\frac{x^3}{3} - \frac{x^3}{2}\right)\right].$$

$$= \frac{2}{(1-x)^2}\left[\frac{1}{3} - \frac{x}{2} + \frac{x^3}{6}\right] = \frac{2}{(1-x)^2}\cdot\frac{2 - 3x + x^3}{6} = \frac{2 - 3x + x^3}{3(1-x)^2}.$$

Factor numerator: $x^3 - 3x + 2 = (x - 1)(x^2 + x - 2) = (x - 1)(x - 1)(x + 2) = (x-1)^2(x+2)$, so $2 - 3x + x^3 = (1-x)^2(x+2)$. (Check: $(1-x)^2(x+2)$ at $x = 0$: $(1)(2) = 2$ ✓; at $x = 1$: 0 ✓.)

$$\hat Y_M(x) = \frac{(1-x)^2(x+2)}{3(1-x)^2} = \frac{x + 2}{3}.$$

**Answer:** $\hat X_M(y) = y/3$ and $\hat Y_M(x) = (x+2)/3$.

> [!tip] **What to internalize.** Three-step: (1) marginal density (integrate joint over the other), (2) conditional density (joint over marginal), (3) conditional expectation (integrate $x \cdot $ conditional). Algebra-heavy — practice the factoring step (here $(1-x)^2(x+2)$) so it doesn't eat 5 minutes on the exam.

> [!warning] **Gotcha — support limits.** The triangular support $0 < x < y < 1$ means the $X$-marginal limits are $(x, 1)$ for $y$ (not $(0, 1)$); the $Y$-marginal limits are $(0, y)$ for $x$. Misreading the support is the #1 source of integration errors here.

---

## Problem 9 (3rd-ed 12.1.5) — MMSE conditional MSE for uniform triangle

> [!example] **Problem.** $f_{X,Y}(x,y) = 2$ for $0 < x < y < 1$, else 0.
> (a) $f_{X\mid Y}(x\mid y)$.
> (b) $\hat X_M(y)$ — MMSE estimate.
> (c) $e^*(0.5) = E[(X - \hat X_M(0.5))^2 \mid Y = 0.5]$ — conditional MMSE at $y = 0.5$.

### Framework

- Same recipe as Problem 8.
- **Conditional MSE at $Y = y$** is the **conditional variance** $\text{Var}(X \mid Y = y)$.

### (a) $f_{X\mid Y}(x\mid y)$

$f_Y(y) = \int_0^y 2\, dx = 2y$ (computed in Problem 7).

$$f_{X\mid Y}(x\mid y) = \frac{2}{2y} = \frac{1}{y}, \quad 0 < x < y.$$

So $X \mid Y = y \sim \text{Uniform}(0, y)$.

### (b) $\hat X_M(y) = E[X \mid Y = y] = y/2$

(Mean of $\text{Uniform}(0, y)$.)

### (c) $e^*(0.5) = \text{Var}(X \mid Y = 0.5)$

For $\text{Uniform}(0, y)$: $\text{Var} = y^2/12$.

$$e^*(0.5) = \frac{(0.5)^2}{12} = \frac{0.25}{12} = \frac{1}{48} \approx 0.0208.$$

**Answer:** $f_{X\mid Y}(x\mid y) = 1/y$ on $(0,y)$; $\hat X_M(y) = y/2$; $e^*(0.5) = 1/48$.

> [!tip] **What to internalize.** **Conditional MSE = conditional variance** when the estimator is the conditional mean. For the MMSE problem in general, the **average MSE** is $E[\text{Var}(X\mid Y)]$ by **law of total variance**.

---

## Problem 10 (3rd-ed 12.2.6) — Erlang-2 / Conditional Uniform — MMSE & LMSE

> [!example] **Problem.** $X$ has Erlang-2 PDF $f_X(x) = \lambda^2 x e^{-\lambda x}$ for $x \geq 0$. Given $X = x$, $Y \mid X = x \sim \text{Uniform}(0, x)$. Find:
> (a) $\hat Y_M(x)$ — MMSE estimate of $Y$ given $X = x$.
> (b) $\hat X_M(y)$ — MMSE estimate of $X$ given $Y = y$.
> (c) $\hat Y_L(X)$ — LMSE estimate of $Y$ given $X$.
> (d) $\hat X_L(Y)$ — LMSE estimate of $X$ given $Y$.

### Framework

- **MMSE = conditional mean** (need conditional density).
- **LMSE = $aY + b$** with $a^* = \text{Cov}(X,Y)/\text{Var}(Y)$ and $b^* = E[X] - a^*E[Y]$ (and symmetric for $\hat Y_L$).
- For LMSE we need: $E[X], E[Y], \text{Var}(X), \text{Var}(Y), \text{Cov}(X,Y)$.

### Erlang-2 mean and variance

For Erlang-$k$ with rate $\lambda$: $E[X] = k/\lambda$, $\text{Var}[X] = k/\lambda^2$. So with $k = 2$:

$$E[X] = 2/\lambda, \qquad \text{Var}[X] = 2/\lambda^2, \qquad E[X^2] = \text{Var}[X] + E[X]^2 = 2/\lambda^2 + 4/\lambda^2 = 6/\lambda^2.$$

### (a) $\hat Y_M(x) = E[Y \mid X = x]$

$Y \mid X = x \sim \text{Uniform}(0, x) \Rightarrow E[Y \mid X = x] = x/2$.

### Compute $E[Y]$, $\text{Var}[Y]$, and $\text{Cov}(X, Y)$ (needed for parts b, c, d)

By tower:

$$E[Y] = E[E[Y\mid X]] = E[X/2] = \frac{1}{\lambda}.$$

By total variance:

$$\text{Var}[Y] = E[\text{Var}(Y\mid X)] + \text{Var}(E[Y\mid X]) = E[X^2/12] + \text{Var}(X/2).$$

$$= \frac{1}{12}\cdot\frac{6}{\lambda^2} + \frac{1}{4}\cdot\frac{2}{\lambda^2} = \frac{6}{12\lambda^2} + \frac{2}{4\lambda^2} = \frac{1}{2\lambda^2} + \frac{1}{2\lambda^2} = \frac{1}{\lambda^2}.$$

$\text{Cov}(X, Y)$: use $E[XY] = E[X \cdot E[Y\mid X]] = E[X \cdot X/2] = E[X^2]/2 = (6/\lambda^2)/2 = 3/\lambda^2$.

$$\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = \frac{3}{\lambda^2} - \frac{2}{\lambda}\cdot\frac{1}{\lambda} = \frac{3}{\lambda^2} - \frac{2}{\lambda^2} = \frac{1}{\lambda^2}.$$

### (b) $\hat X_M(y) = E[X \mid Y = y]$

Compute the joint PDF: $f_{X,Y}(x, y) = f_X(x) f_{Y\mid X}(y\mid x) = \lambda^2 x e^{-\lambda x} \cdot (1/x) = \lambda^2 e^{-\lambda x}$ for $0 < y < x$.

Marginal $f_Y(y) = \int_y^\infty \lambda^2 e^{-\lambda x}\, dx = \lambda^2 \cdot \frac{e^{-\lambda y}}{\lambda} = \lambda e^{-\lambda y}$ for $y \geq 0$.

So $Y \sim \text{Exp}(\lambda)$. Conditional density:

$$f_{X\mid Y}(x\mid y) = \frac{\lambda^2 e^{-\lambda x}}{\lambda e^{-\lambda y}} = \lambda e^{-\lambda(x - y)}, \quad x > y.$$

This says $X \mid Y = y$ is $y + \text{Exp}(\lambda)$. Therefore:

$$\hat X_M(y) = E[X \mid Y = y] = y + \frac{1}{\lambda}.$$

### (c) LMSE of $Y$ given $X$: $\hat Y_L(X) = aX + b$

$$a^* = \frac{\text{Cov}(X, Y)}{\text{Var}(X)} = \frac{1/\lambda^2}{2/\lambda^2} = \frac{1}{2}.$$

$$b^* = E[Y] - a^* E[X] = \frac{1}{\lambda} - \frac{1}{2}\cdot\frac{2}{\lambda} = 0.$$

$$\hat Y_L(X) = \frac{X}{2}.$$

**Note:** This **equals the MMSE estimate** $\hat Y_M(X) = X/2$. That's because $E[Y \mid X]$ is already linear in $X$ here — when the conditional mean is affine in the conditioning variable, LMSE = MMSE.

### (d) LMSE of $X$ given $Y$: $\hat X_L(Y) = cY + d$

$$c^* = \frac{\text{Cov}(X, Y)}{\text{Var}(Y)} = \frac{1/\lambda^2}{1/\lambda^2} = 1.$$

$$d^* = E[X] - c^* E[Y] = \frac{2}{\lambda} - 1\cdot\frac{1}{\lambda} = \frac{1}{\lambda}.$$

$$\hat X_L(Y) = Y + \frac{1}{\lambda}.$$

**This also equals the MMSE estimate** $\hat X_M(Y) = Y + 1/\lambda$ — because the conditional mean is affine in $Y$.

**Answer:** $\hat Y_M(X) = X/2 = \hat Y_L(X)$; $\hat X_M(Y) = Y + 1/\lambda = \hat X_L(Y)$.

> [!tip] **What to internalize.** **LMSE = MMSE iff conditional mean is affine.** This problem shows it explicitly — when $E[Y\mid X] = aX + b$ (linear), the optimal estimator is already linear, so LMSE matches MMSE. **Memorize the LMSE formula** $a^* = \text{Cov}/\text{Var}, b^* = \mu_X - a^*\mu_Y$ — comes up on every Bayesian-estimation problem on the exam.

> [!warning] **Gotcha — total-variance trap.** The first-pass mistake is to compute $\text{Var}[Y] = \text{Var}(X/2) = (1/4)\cdot(2/\lambda^2) = 1/(2\lambda^2)$, missing the $E[\text{Var}(Y\mid X)] = E[X^2/12] = 1/(2\lambda^2)$ term. Total-variance always has **two** terms; if you only get one, you missed the within-cell variance.

---

## Problem 11 (3rd-ed 12.3.3) — MMSE / MAP / ML for Poisson rate

> [!example] **Problem.** $R \sim \text{Exp}(\mu)$ (so $E[R] = 1/\mu$). Given $R = r$, $N \sim \text{Poisson}(rT)$. Find:
> (a) MMSE estimate of $R$ given $N$.
> (b) MAP estimate of $R$ given $N$.
> (c) ML estimate of $R$ given $N$.

### Framework

- **MMSE = $E[R \mid N]$** — needs the posterior density.
- **MAP = $\arg\max_r f_{R\mid N}(r\mid n) = \arg\max_r f_{R, N}(r, n)$** (denominator $P[N = n]$ is fixed).
- **ML = $\arg\max_r P[N = n \mid R = r]$** (no prior — drops $f_R$).

### Build the joint and posterior

$$f_R(r) = \mu e^{-\mu r}, \quad P[N = n \mid R = r] = \frac{(rT)^n e^{-rT}}{n!}.$$

$$f_{R, N}(r, n) = \mu e^{-\mu r}\cdot\frac{(rT)^n e^{-rT}}{n!} = \frac{\mu T^n}{n!} r^n e^{-(\mu + T) r}.$$

Marginal $P[N = n]$ obtained by integrating $r$ from 0 to $\infty$:

$$P[N = n] = \frac{\mu T^n}{n!}\int_0^\infty r^n e^{-(\mu + T)r}\, dr = \frac{\mu T^n}{n!}\cdot\frac{n!}{(\mu + T)^{n+1}} = \frac{\mu T^n}{(\mu + T)^{n+1}}.$$

(used $\int_0^\infty r^n e^{-\beta r}\, dr = n!/\beta^{n+1}$.)

Posterior:

$$f_{R\mid N}(r\mid n) = \frac{f_{R,N}(r,n)}{P[N=n]} = \frac{(\mu + T)^{n+1}}{n!} r^n e^{-(\mu + T) r}.$$

This is the **Erlang-$(n+1)$ density with rate $\mu + T$.**

### (a) MMSE: $\hat R_M(n) = E[R \mid N = n]$

Erlang-$k$ with rate $\beta$ has mean $k/\beta$. Here $k = n + 1$, $\beta = \mu + T$:

$$\hat R_M(n) = \frac{n + 1}{\mu + T}.$$

### (b) MAP: $\hat r_{\text{MAP}}(n) = \arg\max_r f_{R\mid N}(r\mid n)$

Maximize $r^n e^{-(\mu + T)r}$. Take log derivative: $n/r - (\mu + T) = 0 \Rightarrow r = n/(\mu + T)$.

(For $n = 0$: max is at $r = 0$.)

$$\hat r_{\text{MAP}}(n) = \frac{n}{\mu + T}.$$

### (c) ML: $\hat r_{\text{ML}}(n) = \arg\max_r P[N = n\mid R = r]$

Maximize $(rT)^n e^{-rT}/n! = (T^n/n!)\cdot r^n e^{-rT}$. Log derivative: $n/r - T = 0 \Rightarrow r = n/T$.

$$\hat r_{\text{ML}}(n) = \frac{n}{T}.$$

**Answer:** MMSE = $(n+1)/(\mu + T)$; MAP = $n/(\mu + T)$; ML = $n/T$.

> [!tip] **What to internalize — the asymptotic ladder.**
>
> 1. **ML** (no prior, just likelihood) = $n/T$ — the "naive" estimate.
> 2. **MAP** (with prior) = $n/(\mu + T)$ — pulls toward 0 because the exponential prior favors small $r$. The $\mu$ in the denominator is **prior weight**.
> 3. **MMSE** (posterior mean) = $(n+1)/(\mu + T)$ — adds 1 to the numerator (the **Laplace smoothing** or "+1 from the prior shape parameter").
>
> As $T \to \infty$ (lots of data), all three converge to $n/T$ — the prior washes out. As $T \to 0$ (no data), MMSE $\to 1/\mu = E[R]$ — falls back on the prior.

> [!warning] **Gotcha — log-derivative for MAP.** Always take $\partial/\partial r \log f_{R\mid N}(r\mid n) = n/r - (\mu + T)$, not $\partial/\partial r f$ directly. Forgetting the log makes the algebra harder. And for $n = 0$ the MAP is at $r = 0$ (boundary), not at any interior critical point.

---

## Master cheat sheet for Module 7

| Estimator | Formula | When |
|---|---|---|
| **Blind** | $E[\theta]$ | No observation. |
| **MMSE** | $E[\theta\mid X]$ | Squared-error loss. |
| **LMSE** | $aX + b$, $a = \frac{\text{Cov}(\theta, X)}{\text{Var}(X)}, b = E[\theta] - aE[X]$ | Linear restriction. |
| **MAP** | $\arg\max_\theta f_{\theta\mid X}$ | 0-1 loss / discrete priors. |
| **ML** | $\arg\max_\theta f_{X\mid\theta}$ | No prior (classical). |
| **Significance test** | Reject $H_0$ if $T(X) \in R_\alpha$, $P[T \in R_\alpha\mid H_0] \leq \alpha$ | Hypothesis test, fixed $\alpha$. |

| Concentration | Bound |
|---|---|
| **Chebyshev** | $P[|M_n - \mu| \geq c] \leq \sigma^2/(nc^2)$ |
| **CLT** | $(M_n - \mu)/(\sigma/\sqrt n) \approx \mathcal N(0, 1)$ |

**Critical $z$ values:** $z_{0.025} = 1.96$ (two-tail 95%), $z_{0.05} = 1.645$ (one-tail 95%), $z_{0.005} = 2.576$ (two-tail 99%).

**Erlang-$k$ with rate $\lambda$:** $f(x) = \lambda^k x^{k-1} e^{-\lambda x}/(k-1)!$, mean $k/\lambda$, variance $k/\lambda^2$.

---

## Cross-references

- **Course page:** [[eee-350]]
- **Master review:** [[eee-350-final-walkthrough]]
- **Adjacent walkthroughs:** [[eee-350-hw7-walkthrough]] (significance test 11.1.6 + LMSE/MMSE 12.2.3, 12.2.6).
- **Sibling module walkthrough:** [[eee-350-module-06-clt-lln-walkthrough]] (covariance, conditional expectation, LLN, CLT — same i.i.d.-sum framework, scaled differently).
- **Concept pages:** [[mle]], [[map-estimation]], [[lmse]], [[significance-test]], [[neyman-pearson-test]], [[clt]], [[wlln]], [[chebyshev-inequality]].

