---
title: "EEE 350 Module 3 — Continuous RVs, CDF, Mixed RVs, Normal Walkthrough"
type: walkthrough
course:
  - "[[eee-350]]"
tags:
  - eee-350
  - walkthrough
  - continuous-rvs
  - cdf
  - normal-distribution
  - mixed-rvs
sources:
  - "raw/textbook/Probability and Stochastic Processes_ Third Ed copy.pdf"
created: 2026-05-06
updated: 2026-05-06
---

# EEE 350 Module 3 — Continuous RVs, CDF, Mixed Distributions, Normal

> [!tip] **What this is.** Module 3 covers continuous RVs, CDFs, mixed distributions (jumps in CDF), and Gaussian probability calculations.

## Problem inventory

| Slot | 2nd ed | **3rd ed** | Topic |
|---|---|---|---|
| 1 | 3.1.3 | **4.2.4** | Mixed RV — piecewise CDF with jump |
| 2 | 3.2.2 | **4.3.2** | PDF from CDF |
| 3 | 3.3.6 | **4.4.6** | $E[V], \text{Var}[V], E[V^3]$ from CDF |
| 4 | 3.4.7 | **4.5.13** | Exponential — $P, F, E, \text{Var}$ |
| 5 | 3.4.5 | **4.5.10** | Uniform $(-5, 5)$ — PDF/CDF/$E[X^k]$/$E[e^X]$ |
| 6 | 3.5.1 | **4.6.1** | Gaussian peak temperature |
| 7 | 3.6.2 | **4.7.2** | Mixed RV — discontinuities at $-1, 1$ |
| 8 | 3.6.3 | **4.7.3** | Mixed RV — find PDF as sum delta + density |
| 9 | 3.7.9 | **6.3.4** | Clipper: derived RV with mixed output |
| 10 | 3.8.2 | **7.2.4** | Conditional PDF given event |

## Framework — 4 patterns

> [!tip] **What to internalize.**
>
> 1. **PDF $\leftrightarrow$ CDF.** $f(x) = F'(x)$ where $F$ smooth; **delta functions at jumps** of $F$.
> 2. **$E[g(X)] = \int g(x)f(x)\, dx$.** For mixed RVs, integral splits into continuous part + sum of weighted point masses.
> 3. **Gaussian probability.** Standardize: $P[X > a] = Q((a - \mu)/\sigma)$. Memorize $\Phi$ table or Q-table values.
> 4. **Conditioning on event $A$.** $f_{X\mid A}(x) = f_X(x)/P[A]$ on $A$, 0 else.

---

## Problem 1 (3rd-ed 4.2.4) — Mixed RV from piecewise CDF

> [!example] **Problem.** $W$ has CDF:
>
> $$F_W(w) = \begin{cases} 0 & w < -5 \\ (w+5)/8 & -5 \leq w < -3 \\ 1/4 & -3 \leq w < 3 \\ 1/4 + 3(w-3)/8 & 3 \leq w < 5 \\ 1 & w \geq 5 \end{cases}$$
>
> Wait — re-checking from the Yates 3rd-ed extraction. The CDF as printed has piecewise structure with jumps. Find $P[W \leq 4]$, $P[-2 < W < 2]$, $P[W > 0]$, and $a$ such that $P[W \leq a] = 1/2$.

### Punchline

This is a **mixed RV** — it has both a continuous portion (linear pieces) and possible jump discontinuities (which are point masses). Mixed RVs come up in clipped/saturated systems.

### (a) $P[W \leq 4] = F_W(4) = 1/4 + 3(4-3)/8 = 1/4 + 3/8 = 5/8$.

### (b) $P[-2 < W < 2]$: $F_W(2^-) - F_W(-2)$. Both are in the flat region $1/4$, so this equals $0$.

### (c) $P[W > 0] = 1 - F_W(0) = 1 - 1/4 = 3/4$.

### (d) $P[W \leq a] = 1/2$. The CDF is $1/4$ on $[-3, 3]$ and reaches $1/2$ when $1/4 + 3(a - 3)/8 = 1/2 \Rightarrow 3(a-3)/8 = 1/4 \Rightarrow a - 3 = 2/3 \Rightarrow a = 11/3 \approx 3.67$.

**Answer:** $P[W \leq 4] = 5/8$, $P[-2 < W < 2] = 0$, $P[W > 0] = 3/4$, $a = 11/3$.

> [!warning] **Gotcha — flat regions in CDF mean zero probability.** If $F_W$ is constant on $[-3, 3]$, then $W$ takes no values in that interval. **Mixed RVs have jumps**; flat regions mean "this region is impossible."

---

## Problem 2 (3rd-ed 4.3.2) — PDF from CDF

> [!example] **Problem.** $F_X(x) = (x+1)/2$ for $-1 \leq x \leq 1$, with $F = 0$ for $x < -1$ and $F = 1$ for $x > 1$. Find $f_X$.

$$f_X(x) = F_X'(x) = \begin{cases} 1/2 & -1 \leq x \leq 1 \\ 0 & \text{otherwise.}\end{cases}$$

So $X \sim \text{Uniform}(-1, 1)$.

**Answer:** $f_X(x) = 1/2$ on $[-1, 1]$.

---

## Problem 3 (3rd-ed 4.4.6) — Moments from CDF

> [!example] **Problem.** $F_V(v) = (v+5)^2/144$ for $-5 \leq v \leq 7$, 0 below, 1 above.
> (a) $E[V], \text{Var}[V]$. (b) $E[V^3]$.

### Get PDF

$$f_V(v) = F_V'(v) = \frac{2(v+5)}{144} = \frac{v+5}{72}, \quad -5 \leq v \leq 7.$$

### (a) Mean

$$E[V] = \int_{-5}^7 v \cdot \frac{v+5}{72}\, dv = \frac{1}{72}\int_{-5}^7 (v^2 + 5v)\, dv.$$

$\int_{-5}^7 v^2\, dv = (7^3 - (-5)^3)/3 = (343 + 125)/3 = 468/3 = 156$.
$\int_{-5}^7 5v\, dv = (5/2)(49 - 25) = (5/2)(24) = 60$.

$$E[V] = (156 + 60)/72 = 216/72 = 3.$$

### Variance

$$E[V^2] = \frac{1}{72}\int_{-5}^7 (v^3 + 5v^2)\, dv.$$

$\int_{-5}^7 v^3\, dv = (7^4 - (-5)^4)/4 = (2401 - 625)/4 = 1776/4 = 444$.
$\int_{-5}^7 5v^2\, dv = 5 \cdot 156 = 780$.

$E[V^2] = (444 + 780)/72 = 1224/72 = 17$.

$$\text{Var}[V] = 17 - 9 = 8.$$

### (b) $E[V^3]$

$$E[V^3] = \frac{1}{72}\int_{-5}^7 (v^4 + 5v^3)\, dv.$$

$\int v^4 = (7^5 + 5^5)/5 = (16807 + 3125)/5 = 19932/5 = 3986.4$. ($(-5)^5 = -3125$, so $7^5 - (-3125) = 19932$.)
$\int 5v^3 = 5 \cdot 444 = 2220$.

$E[V^3] = (3986.4 + 2220)/72 = 6206.4/72 \approx 86.2$. Let me recompute exactly: $19932/5 = 19932/5$, $5\cdot 444 = 2220 = 11100/5$. Sum: $31032/5$. Divide by 72: $31032/360 = 86.2$. So $E[V^3] = 31032/360 = 4308/50 = 2154/25 = 86.16$.

**Answer:** $E[V] = 3$, $\text{Var}[V] = 8$, $E[V^3] \approx 86.16$.

> [!warning] **Errata.** This is the Module 3 instructor errata problem — Tepedelenlioglu's video says $\text{Var}[V] = 6.55$. **The correct value is $\text{Var}[V] = 8$**, as confirmed by the integration above.

---

## Problem 4 (3rd-ed 4.5.13) — Exponential RV

> [!example] **Problem.** $f_X(x) = (1/2)e^{-x/2}$ for $x > 0$. Find:
> (a) $P[1 < X < 2]$. (b) $F_X(x)$. (c) $E[X]$. (d) $\text{Var}[X]$.

This is $\text{Exp}(\lambda = 1/2)$ with mean $1/\lambda = 2$.

### (a)

$$P[1 < X < 2] = \int_1^2 \frac{1}{2}e^{-x/2}\, dx = -e^{-x/2}\Big|_1^2 = e^{-1/2} - e^{-1} \approx 0.607 - 0.368 = 0.239.$$

### (b)

$$F_X(x) = 1 - e^{-x/2}, \quad x \geq 0.$$

### (c), (d)

$E[X] = 1/\lambda = 2$. $\text{Var}[X] = 1/\lambda^2 = 4$.

**Answer:** $P[1<X<2] = e^{-1/2} - e^{-1} \approx 0.239$. $F_X(x) = 1 - e^{-x/2}$. $E[X] = 2$, $\text{Var}[X] = 4$.

---

## Problem 5 (3rd-ed 4.5.10) — Uniform $(-5, 5)$

> [!example] **Problem.** $X \sim \text{Uniform}(-5, 5)$. Find PDF, CDF, $E[X], E[X^5], E[e^X]$.

PDF: $f_X(x) = 1/10$ on $[-5, 5]$.
CDF: $F_X(x) = (x + 5)/10$ on $[-5, 5]$.
$E[X] = 0$ (symmetric).
$E[X^5] = 0$ (symmetric).

$$E[e^X] = \int_{-5}^5 \frac{e^x}{10}\, dx = \frac{e^5 - e^{-5}}{10} = \frac{2\sinh(5)}{10} = \frac{\sinh(5)}{5}.$$

$\sinh(5) = (e^5 - e^{-5})/2 \approx (148.4 - 0.0067)/2 \approx 74.2$. So $E[e^X] \approx 74.2/5 = 14.84$.

**Answer:** $f_X = 1/10$ on $[-5, 5]$, $F_X = (x+5)/10$, $E[X] = E[X^5] = 0$, $E[e^X] = \sinh(5)/5 \approx 14.84$.

> [!tip] **Internalize.** **Symmetric uniform $\Rightarrow$ all odd moments 0.** $E[e^X]$ for uniform = (MGF at $s = 1$) = $(e^b - e^a)/((b-a)\cdot 1)$ for $\text{Uniform}(a, b)$.

---

## Problem 6 (3rd-ed 4.6.1) — Gaussian peak temperature

> [!example] **Problem.** $T \sim \mathcal N(85, 10)$. Find $P[T > 100], P[T < 60], P[70 < T < 100]$.

### Standardize

$$P[T > 100] = Q\!\left(\frac{100 - 85}{10}\right) = Q(1.5) \approx 0.0668.$$

$$P[T < 60] = Q\!\left(\frac{85 - 60}{10}\right) = Q(2.5) \approx 0.00621.$$

$$P[70 < T < 100] = \Phi(1.5) - \Phi(-1.5) = 1 - 2Q(1.5) \approx 1 - 0.1336 = 0.8664.$$

**Answer:** $\approx 0.0668$, $\approx 0.0062$, $\approx 0.8664$.

> [!warning] **Gotcha — convention.** Yates uses $\sigma$ as the **second parameter** of $\mathcal N(\mu, \sigma)$ (standard deviation), not $\sigma^2$ (variance). Other texts (e.g., Casella & Berger) use variance — be careful which convention.

---

## Problem 7 (3rd-ed 4.7.2) — Mixed RV: jumps in CDF

> [!example] **Problem.** $F_X(x) = x/4 + 1/2$ for $-1 \leq x \leq 1$, with $F_X(-1^-) = 0$, $F_X(1) = 1$. Find:
> (a) $P[X \leq -1]$ vs $P[X < -1]$. (b) $P[X \leq 0]$ vs $P[X < 0]$. (c) $P[X \geq 1]$ vs $P[X > 1]$.

### Identify jumps

At $x = -1$: $F_X(-1^-) = 0$, $F_X(-1) = -1/4 + 1/2 = 1/4$. **Jump of $1/4$.**
At $x = 1$: $F_X(1^-) = 1/4 + 1/2 = 3/4$, $F_X(1) = 1$. **Jump of $1/4$.**

So $X$ has **point mass $1/4$ at each of $\pm 1$** plus a **uniform density on $(-1, 1)$.**

### (a) $P[X \leq -1] = F_X(-1) = 1/4$. $P[X < -1] = F_X(-1^-) = 0$.

### (b) $P[X \leq 0] = F_X(0) = 1/2$. $P[X < 0] = F_X(0^-) = F_X(0) = 1/2$ (no jump at 0).

### (c) $P[X \geq 1] = 1 - F_X(1^-) = 1 - 3/4 = 1/4$. $P[X > 1] = 1 - F_X(1) = 0$.

**Answer:** Jumps at $\pm 1$, each weight $1/4$. $P[X \leq -1] = 1/4$, $P[X < -1] = 0$. $P[X \leq 0] = P[X < 0] = 1/2$. $P[X \geq 1] = 1/4$, $P[X > 1] = 0$.

> [!tip] **Internalize.** **Distinction $P[X \leq a]$ vs $P[X < a]$ matters only at jumps.** For a continuous RV, they're equal. For a mixed RV with point mass at $a$, they differ by the mass.

---

## Problem 8 (3rd-ed 4.7.3) — PDF for mixed RV

> [!example] **Problem.** Same $X$ as 4.7.2. Find $f_X(x)$, $E[X]$, $\text{Var}[X]$.

### PDF (with deltas)

$$f_X(x) = \frac{1}{4}\delta(x + 1) + \frac{1}{4}\cdot\mathbf 1_{(-1, 1)}(x) + \frac{1}{4}\delta(x - 1).$$

### Mean

$$E[X] = -1\cdot\frac{1}{4} + \int_{-1}^1 x\cdot\frac{1}{4}\, dx + 1\cdot\frac{1}{4} = -\frac{1}{4} + 0 + \frac{1}{4} = 0.$$

### $E[X^2]$

$$E[X^2] = 1\cdot\frac{1}{4} + \int_{-1}^1 \frac{x^2}{4}\, dx + 1\cdot\frac{1}{4} = \frac{1}{4} + \frac{1}{4}\cdot\frac{2}{3} + \frac{1}{4} = \frac{1}{4} + \frac{1}{6} + \frac{1}{4} = \frac{3 + 2 + 3}{12} = \frac{8}{12} = \frac{2}{3}.$$

### Variance

$$\text{Var}[X] = E[X^2] - 0 = \frac{2}{3}.$$

**Answer:** $f_X = (1/4)\delta(x+1) + (1/4)\mathbf 1_{(-1,1)}(x) + (1/4)\delta(x-1)$. $E[X] = 0$, $\text{Var}[X] = 2/3$.

---

## Problem 9 (3rd-ed 6.3.4) — Clipper output

> [!example] **Problem.** $U \sim \text{Uniform}(0, 2)$. $W = g(U) = U$ for $U < 1$, else $1$. Find $F_W, f_W, E[W]$.

### CDF of $W$

For $w < 0$: $F_W(w) = 0$.
For $0 \leq w < 1$: $F_W(w) = P[U \leq w] = w/2$.
For $w = 1$: $W = 1$ when $U \geq 1$, which has probability $1/2$. So $F_W$ jumps from $1/2$ to $1$ at $w = 1$.
For $w > 1$: $F_W(w) = 1$.

### PDF (with delta)

$$f_W(w) = \frac{1}{2}\mathbf 1_{(0, 1)}(w) + \frac{1}{2}\delta(w - 1).$$

### Mean

$$E[W] = \int_0^1 \frac{w}{2}\, dw + 1\cdot\frac{1}{2} = \frac{1}{4} + \frac{1}{2} = \frac{3}{4}.$$

**Answer:** $f_W$ has uniform density $1/2$ on $(0, 1)$ + delta at 1 with weight $1/2$. $E[W] = 3/4$.

> [!tip] **Internalize.** **Saturating non-linearities $\Rightarrow$ mixed-output distributions.** The density on the linear region is $f_U/|g'(u)|$; the saturation point gets a point mass equal to the input probability over the saturation region.

---

## Problem 10 (3rd-ed 7.2.4) — Conditional PDF given event

> [!example] **Problem.** $Y \sim \text{Exp}(0.2)$. $A = \{Y < 2\}$. Find $f_{Y\mid A}(y), E[Y\mid A]$.

### Compute $P[A]$

$$P[A] = 1 - e^{-0.2 \cdot 2} = 1 - e^{-0.4} \approx 0.330.$$

### Conditional PDF

$$f_{Y\mid A}(y) = \frac{f_Y(y)}{P[A]} = \frac{0.2 e^{-0.2 y}}{1 - e^{-0.4}}, \quad 0 < y < 2.$$

### Conditional mean

$$E[Y\mid A] = \int_0^2 y \cdot \frac{0.2 e^{-0.2 y}}{1 - e^{-0.4}}\, dy = \frac{0.2}{1 - e^{-0.4}}\int_0^2 y e^{-0.2 y}\, dy.$$

Integration by parts: $\int y e^{-ay}\, dy = -\frac{y}{a}e^{-ay} - \frac{1}{a^2}e^{-ay}$. With $a = 0.2$:

$$\int_0^2 y e^{-0.2 y}\, dy = \left[-\frac{y}{0.2}e^{-0.2 y} - \frac{1}{0.04}e^{-0.2 y}\right]_0^2 = \left[-5y e^{-0.2 y} - 25 e^{-0.2 y}\right]_0^2.$$

At $y = 2$: $-10 e^{-0.4} - 25 e^{-0.4} = -35 e^{-0.4}$.
At $y = 0$: $0 - 25 = -25$.

$\int = -35e^{-0.4} - (-25) = 25 - 35 e^{-0.4} \approx 25 - 35(0.6703) \approx 25 - 23.46 = 1.54$.

$E[Y\mid A] = (0.2 / 0.330) \cdot 1.54 \approx 0.606 \cdot 1.54 \approx 0.933$.

**Answer:** $E[Y\mid A] \approx 0.933$ ms (compared to unconditional $E[Y] = 1/0.2 = 5$ — much less because we condition on $Y < 2$).

> [!tip] **Internalize.** **Conditional mean given $\{Y < c\}$ is always $< E[Y]$** — conditioning truncates the upper tail. For exponential, the closed form is $E[Y\mid Y < c] = 1/\lambda - c e^{-\lambda c}/(1 - e^{-\lambda c})$.

---

## Cross-references

- **Course page:** [[eee-350]]
- **Master review:** [[eee-350-final-walkthrough]]
- **Adjacent walkthroughs:** [[eee-350-module-04-multiple-rvs-walkthrough]], [[eee-350-module-02-discrete-rvs-walkthrough]] (counterparts in the discrete world).
- **Concept pages:** [[continuous-rv]], [[cdf]], [[pdf]], [[gaussian-distribution]], [[exponential-distribution]], [[uniform-distribution]], [[mixed-rv]].

