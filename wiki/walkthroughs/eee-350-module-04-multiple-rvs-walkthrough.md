---
title: "EEE 350 Module 4 — Multiple Random Variables Walkthrough"
type: walkthrough
course:
  - "[[eee-350]]"
tags:
  - eee-350
  - walkthrough
  - joint-distributions
  - conditional-rvs
  - independence
sources:
  - "raw/textbook/Probability and Stochastic Processes_ Third Ed copy.pdf"
created: 2026-05-06
updated: 2026-05-06
---

# EEE 350 Module 4 — Multiple Random Variables

> [!tip] **What this is.** Module 4 = joint distributions, marginals, conditioning, independence, derived RVs (max, min, ratios). 15 problems — the **biggest module** in the syllabus.

## Problem inventory (Canvas-mapped)

| Slot | 2nd ed | **3rd ed** | Topic |
|---|---|---|---|
| 1 | 4.1.1 | **5.1.1** | Joint CDF — marginals + a probability |
| 2 | 4.2.4 | **5.2.4** | Joint PMF — coin flip example |
| 3 | 4.3.4 | **5.3.5** | Marginal PMFs from joint |
| 4 | 4.4.2 | **5.4.2** | Joint PDF — find $c$, compute probabilities |
| 5 | 4.5.4 | **5.5.5** | Marginal PDFs from joint with non-rect support |
| 6 | 4.6.4 | **6.1.5** | PMF of min over discrete uniforms |
| 7 | 4.6.6 | **6.4.4** | $W = \max(X, Y)$ from joint PDF |
| 8 | 4.6.8 | **6.4.6** | $W = Y/X$ — range, CDF/PDF, $E[W]$ |
| 9 | 4.8.1 | **(no 3rd-ed)** | Skipped — Canvas marks ✗ |
| 10 | 4.8.5 | **7.3.5** | Conditional PDF given event $A$ |
| 11 | 4.9.1 | **7.4.5** | Joint PMF — travel days vs weight |
| 12 | 4.9.11 | **7.5.6** | Conditional PDF, conditional expectation |
| 13 | 4.10.2 | **5.7.4** | Independence — moments of $X + Y$, $XY$ |
| 14 | 4.10.6 | **5.7.7** | Independence + geometric — $E$, $\text{Var}$ of difference |
| 15 | 6.1.2 | **9.1.1** | i.i.d. — $E[X_1 - X_2], \text{Var}[X_1 - X_2]$ |

## Framework — the patterns

> [!tip] **What to internalize.**
>
> 1. **Joint $\Rightarrow$ marginal $\Rightarrow$ conditional.** $f_X(x) = \int f_{X,Y}\, dy$; $f_{X\mid Y}(x\mid y) = f_{X,Y}(x,y)/f_Y(y)$. Always integrate **over the support** — non-rectangular supports change the limits.
> 2. **Independence test:** $f_{X,Y}(x,y) = f_X(x)f_Y(y)$ for **all** $(x,y)$ in the support **and** the support must be **rectangular**. Triangular support $\Rightarrow$ dependent (always).
> 3. **Derived RV via CDF:** $F_W(w) = P[g(X,Y) \leq w]$ — integrate the joint over the region. **Differentiate** for $f_W$. Variants: $\max, \min, X+Y, X/Y$, ratio, etc.
> 4. **Conditional moments:** $E[X\mid Y = y] = \int x f_{X\mid Y}(x\mid y)\, dx$; tower rule $E[X] = E[E[X\mid Y]]$.

---

## Problem 1 (3rd-ed 5.1.1) — Joint CDF, marginals

> [!example] **Problem.** $F_{X,Y}(x,y) = (1 - e^{-x})(1 - e^{-y})$ for $x, y > 0$, else 0.
> (a) $P[X < 2, Y < 3]$. (b) Marginal $F_X(x)$. (c) Marginal $F_Y(y)$.

This factors: $F_{X,Y}$ is the product of two CDFs $\Rightarrow$ $X, Y$ are **independent**, each $\text{Exp}(1)$.

**(a)** $P[X < 2, Y < 3] = (1 - e^{-2})(1 - e^{-3}) \approx 0.864 \times 0.950 \approx 0.821$.

**(b)** $F_X(x) = \lim_{y \to \infty} F_{X,Y}(x, y) = 1 - e^{-x}$ for $x > 0$.

**(c)** $F_Y(y) = 1 - e^{-y}$ for $y > 0$.

**Answer:** $P[X<2,Y<3] = (1-e^{-2})(1-e^{-3}) \approx 0.821$. Marginals are $\text{Exp}(1)$ each.

> [!tip] **What to internalize.** **Factored joint CDF $\Leftrightarrow$ independence.** If $F_{X,Y}(x,y) = g(x)h(y)$ with $g, h$ valid CDFs, $X \perp Y$. Marginal CDF = limit as the other variable $\to \infty$.

---

## Problem 2 (3rd-ed 5.2.4) — Joint PMF from coin flips

> [!example] **Problem.** Two independent flips of a fair coin. $X$ = total tails. $Y$ = heads on **last** flip ($Y = 1$ if last flip is H, 0 else). Find $P_{X,Y}(x,y)$.

### Enumerate

Outcomes equally likely (each prob $1/4$):

| Outcome | $X$ | $Y$ | Prob |
|---|---|---|---|
| HH | 0 | 1 | 1/4 |
| HT | 1 | 0 | 1/4 |
| TH | 1 | 1 | 1/4 |
| TT | 2 | 0 | 1/4 |

So:

| | $y = 0$ | $y = 1$ |
|---|---|---|
| $x = 0$ | 0 | 1/4 |
| $x = 1$ | 1/4 | 1/4 |
| $x = 2$ | 1/4 | 0 |

> [!tip] **Internalize.** When the sample space is small, **enumerate**. Don't try to derive a closed form for tiny $n$.

> [!warning] **Gotcha — independence here?** $X$ and $Y$ are **not independent**: the marginal of $X$ is $\text{Bin}(2, 1/2)$, marginal of $Y$ is $\text{Ber}(1/2)$, but $P[X = 0, Y = 0] = 0 \neq 1/4 \cdot 1/2 = 1/8$.

---

## Problem 3 (3rd-ed 5.3.5) — Marginal PMFs

> [!example] **Problem.** $P_{N,K}(n, k) = \dfrac{(1 - p)^{n-1} p}{n}$ for $k = 1, \ldots, n$ and $n = 1, 2, \ldots$. Find $P_N(n)$ and $P_K(k)$.

### Marginal of $N$

Sum over $k = 1, \ldots, n$:

$$P_N(n) = \sum_{k=1}^n \frac{(1-p)^{n-1}p}{n} = n\cdot\frac{(1-p)^{n-1}p}{n} = (1-p)^{n-1}p, \quad n \geq 1.$$

This is **Geometric($p$)** — $N$ is geometric.

### Marginal of $K$

Sum over all $n \geq k$ (since $k \leq n$):

$$P_K(k) = \sum_{n = k}^\infty \frac{(1-p)^{n-1}p}{n}.$$

Let $m = n - 1$ (so $m \geq k - 1$):

$$= p\sum_{m = k-1}^\infty \frac{(1-p)^m}{m+1}.$$

Hmm — not closed-form generally. But notice $-\ln(1 - x) = \sum_{m=1}^\infty x^m/m$ for $|x| < 1$. Reindex with $j = m + 1$:

$$= p\sum_{j = k}^\infty \frac{(1-p)^{j-1}}{j} = \frac{p}{1-p}\sum_{j=k}^\infty \frac{(1-p)^j}{j}.$$

Use $\sum_{j=1}^\infty (1-p)^j/j = -\ln(p)$:

$$\sum_{j=k}^\infty \frac{(1-p)^j}{j} = -\ln p - \sum_{j=1}^{k-1}\frac{(1-p)^j}{j}.$$

So **for $k \geq 1$:**

$$P_K(k) = \frac{p}{1-p}\left[-\ln p - \sum_{j=1}^{k-1}\frac{(1-p)^j}{j}\right].$$

> [!tip] **Internalize.** When summing a discrete joint PMF gives a **logarithmic series** (here $-\ln p$), recognize it as the **logarithmic distribution** — $P_K(k)$ has a non-elementary closed form.

---

## Problem 4 (3rd-ed 5.4.2) — Joint PDF: find $c$ + probabilities

> [!example] **Problem.** $f_{X,Y}(x,y) = c x y^2$ for $0 < x, y < 1$, else 0.
> (a) Find $c$. (b) $P[X > Y]$ and $P[Y < X^2]$. (c) $P[\min(X,Y) < 1/2]$. (d) $P[\max(X,Y) < 3/4]$.

### (a) Normalization

$$1 = \int_0^1\int_0^1 cxy^2\, dx\, dy = c\cdot\frac{1}{2}\cdot\frac{1}{3} = \frac{c}{6} \implies c = 6.$$

So $f_{X,Y}(x,y) = 6xy^2$. **Note: support is rectangular, $f_{X,Y}$ factors as $(2x)(3y^2)$, so $X \perp Y$ with $X \sim 2x$, $Y \sim 3y^2$ on $[0,1]$.**

### (b) $P[X > Y]$

$$\int_0^1\int_0^x 6xy^2\, dy\, dx = \int_0^1 6x\cdot\frac{x^3}{3}\, dx = \int_0^1 2x^4\, dx = \frac{2}{5}.$$

$P[Y < X^2]$:

$$\int_0^1\int_0^{x^2} 6xy^2\, dy\, dx = \int_0^1 6x\cdot\frac{x^6}{3}\, dx = \int_0^1 2x^7\, dx = \frac{1}{4}.$$

### (c) $P[\min(X,Y) < 1/2] = 1 - P[\min \geq 1/2] = 1 - P[X \geq 1/2, Y \geq 1/2]$

By independence: $P[X \geq 1/2] = \int_{1/2}^1 2x\, dx = 1 - 1/4 = 3/4$. $P[Y \geq 1/2] = \int_{1/2}^1 3y^2\, dy = 1 - 1/8 = 7/8$.

$$P[\min < 1/2] = 1 - \frac{3}{4}\cdot\frac{7}{8} = 1 - \frac{21}{32} = \frac{11}{32}.$$

### (d) $P[\max(X,Y) < 3/4] = P[X < 3/4, Y < 3/4]$

By independence: $P[X < 3/4] = (3/4)^2 = 9/16$. $P[Y < 3/4] = (3/4)^3 = 27/64$.

$$P[\max < 3/4] = \frac{9}{16}\cdot\frac{27}{64} = \frac{243}{1024} \approx 0.237.$$

**Answers:** (a) $c = 6$. (b) $P[X>Y] = 2/5$, $P[Y<X^2] = 1/4$. (c) $11/32$. (d) $243/1024$.

> [!tip] **Internalize.** **$\max < a \Leftrightarrow$ both $< a$**, **$\min < a \Leftrightarrow$ at least one $< a$**. Use complement: $P[\min < a] = 1 - P[\min \geq a]$.

---

## Problem 5 (3rd-ed 5.5.5) — Marginal PDFs with non-rect support

> [!example] **Problem.** $f_{X,Y}(x,y) = 5x^2/2$ for $-1 < x < 1, 0 < y < x^2$. Find $f_X(x)$ and $f_Y(y)$.

### Marginal $f_X$

$$f_X(x) = \int_0^{x^2} \frac{5x^2}{2}\, dy = \frac{5x^2}{2}\cdot x^2 = \frac{5x^4}{2}, \quad -1 < x < 1.$$

### Marginal $f_Y$

For fixed $y \in (0, 1)$, $x$ must satisfy $x^2 > y$ AND $-1 < x < 1$. So $x \in (-1, -\sqrt y) \cup (\sqrt y, 1)$.

$$f_Y(y) = \int_{-1}^{-\sqrt y}\frac{5x^2}{2}\, dx + \int_{\sqrt y}^1 \frac{5x^2}{2}\, dx.$$

By symmetry, both integrals equal:

$$\int_{\sqrt y}^1 \frac{5x^2}{2}\, dx = \frac{5}{6}(1 - y^{3/2}).$$

$$f_Y(y) = 2\cdot\frac{5}{6}(1 - y^{3/2}) = \frac{5}{3}(1 - y^{3/2}), \quad 0 < y < 1.$$

**Answer:** $f_X(x) = 5x^4/2$ on $(-1, 1)$; $f_Y(y) = (5/3)(1 - y^{3/2})$ on $(0, 1)$.

> [!warning] **Gotcha — disconnected $x$-region.** When marginalizing $Y$, the constraint $x^2 > y$ gives **two disjoint intervals** for $x$. Don't integrate just one — sum both.

---

## Problem 6 (3rd-ed 6.1.5) — PMF of min over discrete uniforms

> [!example] **Problem.** $P_{X,Y}(x,y) = 0.01$ for $x, y \in \{1, \ldots, 10\}$, else 0. Find PMF of $W = \min(X, Y)$.

### Recipe — CCDF for min

$$P[W \geq w] = P[X \geq w, Y \geq w] = P[X \geq w]^2 = \left(\frac{11 - w}{10}\right)^2$$

for $w \in \{1, \ldots, 10\}$ (since $P[X \geq w] = (10 - w + 1)/10 = (11 - w)/10$).

Then:

$$P_W(w) = P[W \geq w] - P[W \geq w + 1] = \left(\frac{11 - w}{10}\right)^2 - \left(\frac{10 - w}{10}\right)^2.$$

$$= \frac{(11 - w)^2 - (10 - w)^2}{100} = \frac{(11 - w + 10 - w)(11 - w - 10 + w)}{100} = \frac{21 - 2w}{100}.$$

For $w = 1, 2, \ldots, 10$:

| $w$ | $P_W(w)$ |
|---|---|
| 1 | 19/100 |
| 2 | 17/100 |
| 3 | 15/100 |
| ... | ... |
| 10 | 1/100 |

(Decreases by 2/100 each step. Sum: 19+17+15+...+1 = 100/100 ✓)

**Answer:** $P_W(w) = (21 - 2w)/100$ for $w = 1, \ldots, 10$.

> [!tip] **Internalize.** **Min via CCDF, max via CDF.** $P[\min \geq w] = P[X \geq w]P[Y \geq w]$; $P[\max \leq w] = P[X \leq w]P[Y \leq w]$ (independence required).

---

## Problem 7 (3rd-ed 6.4.4) — $W = \max(X, Y)$ from joint PDF

> [!example] **Problem.** $f_{X,Y}(x,y) = x + y$ for $0 < x, y < 1$. $W = \max(X, Y)$.
> (a) Range $S_W$. (b) $F_W(w), f_W(w)$.

**Note:** $X, Y$ **not independent** here — joint $\neq$ product. But max-via-CDF still works because we integrate the joint over the right region.

### (a) Range $S_W$

$\max(X, Y) \in [0, 1)$ since $X, Y \in [0, 1]$.

### (b) $F_W(w)$

$F_W(w) = P[\max(X, Y) \leq w] = P[X \leq w, Y \leq w]$:

$$F_W(w) = \int_0^w\int_0^w (x + y)\, dx\, dy = \int_0^w\left[\frac{x^2}{2} + xy\right]_0^w\, dy = \int_0^w\left(\frac{w^2}{2} + wy\right)\, dy.$$

$$= \frac{w^3}{2} + \frac{w^3}{2} = w^3, \quad 0 \leq w \leq 1.$$

$$f_W(w) = 3w^2, \quad 0 \leq w \leq 1.$$

**Answer:** $F_W(w) = w^3$, $f_W(w) = 3w^2$ on $[0, 1]$.

> [!tip] **Internalize.** **Max-via-CDF** works even when $X, Y$ are dependent — just integrate the joint over the box $[0, w] \times [0, w]$. Independence shortcut is $F_W(w) = F_X(w)F_Y(w)$ — does not apply here.

---

## Problem 8 (3rd-ed 6.4.6) — $W = Y/X$ ratio

> [!example] **Problem.** $f_{X,Y}(x,y) = 2$ for $0 < y < x < 1$, else 0. $W = Y/X$.
> (a) Range $S_W$. (b) $F_W(w), f_W(w), E[W]$.

### (a) Range

For $(x, y)$ in support, $0 < y < x < 1 \Rightarrow 0 < y/x < 1$. So $S_W = (0, 1)$.

### (b) CDF

$F_W(w) = P[Y/X \leq w] = P[Y \leq wX]$. Region: $0 < y < x < 1$ and $y < wx$.

For $w \in (0, 1)$: the line $y = wx$ has slope $< 1$, so for any $x \in (0, 1)$ the constraint $y < wx$ is tighter than $y < x$. Region: $\{0 < x < 1, 0 < y < wx\}$.

$$F_W(w) = \int_0^1 \int_0^{wx} 2\, dy\, dx = \int_0^1 2wx\, dx = w.$$

So $W \sim \text{Uniform}(0, 1)$:

$$f_W(w) = 1 \quad \text{on } (0, 1), \qquad E[W] = \frac{1}{2}.$$

**Answer:** $W \sim \text{Uniform}(0, 1)$; $f_W(w) = 1$ on $(0, 1)$; $E[W] = 1/2$.

> [!tip] **Internalize.** **Ratio of two uniformly distributed-on-triangle RVs is uniform on (0, 1).** General principle: **integrate joint over the region $\{Y/X \leq w\}$** — case-split by sign of $X$ if needed (here $X > 0$ so no split).

---

## Problem 9 (2nd-ed 4.8.1) — Skipped

> [!warning] **No 3rd-ed equivalent on Canvas.** Move on.

---

## Problem 10 (3rd-ed 7.3.5) — Conditional PDF given event

> [!example] **Problem.** $f_{X,Y}(x,y) = (x+y)/3$ for $0 < x < 1, 0 < y < 2$. $A = \{Y < 1\}$.
> (a) $P[A]$. (b) $f_{X,Y\mid A}(x,y)$. (c) $f_{X\mid A}(x), f_{Y\mid A}(y)$.

### (a) $P[A]$

$$P[A] = \int_0^1\int_0^1 \frac{x+y}{3}\, dy\, dx = \int_0^1 \frac{x + 1/2}{3}\, dx = \frac{1}{3}\left[\frac{1}{2} + \frac{1}{2}\right] = \frac{1}{3}.$$

### (b) Conditional joint

$$f_{X,Y\mid A}(x, y) = \frac{f_{X,Y}(x,y)}{P[A]} = \frac{(x+y)/3}{1/3} = x + y, \quad 0 < x < 1, 0 < y < 1.$$

(Zero outside the conditioning region $A$.)

### (c) Marginals

$$f_{X\mid A}(x) = \int_0^1 (x+y)\, dy = x + 1/2, \quad 0 < x < 1.$$

$$f_{Y\mid A}(y) = \int_0^1 (x+y)\, dx = 1/2 + y, \quad 0 < y < 1.$$

**Answer:** $P[A] = 1/3$. $f_{X,Y\mid A}(x,y) = x + y$ on the unit square. Marginals $x + 1/2$ and $1/2 + y$.

> [!tip] **Internalize.** **Conditional PDF on event = joint / probability of event**, restricted to the event's support. Always renormalize.

---

## Problem 11 (3rd-ed 7.4.5) — Joint PMF (conditional + marginal)

> [!example] **Problem.** $D \in \{2, 3, 4\}$ equally likely (trip length). Given $D = d$, $W \sim \text{Uniform}(\{-d, -d+1, \ldots, d\})$ (integer weight change). Find $P_{D,W}(d, w)$.

### Recipe

$$P_{D,W}(d, w) = P_D(d) \cdot P_{W\mid D}(w\mid d) = \frac{1}{3}\cdot\frac{1}{2d+1}$$

for $d \in \{2,3,4\}$ and $w \in \{-d, -d+1, \ldots, d\}$.

So:

| $d$ | $w$ range | $P_{W\mid D}$ | $P_{D,W}$ |
|---|---|---|---|
| 2 | $\{-2, \ldots, 2\}$ | $1/5$ | $1/15$ |
| 3 | $\{-3, \ldots, 3\}$ | $1/7$ | $1/21$ |
| 4 | $\{-4, \ldots, 4\}$ | $1/9$ | $1/27$ |

**Answer:**

$$P_{D,W}(d,w) = \frac{1}{3(2d+1)} \quad \text{for } d \in \{2,3,4\}, w \in \{-d, \ldots, d\}.$$

> [!tip] **Internalize.** **Joint PMF = marginal × conditional**, with appropriate support.

---

## Problem 12 (3rd-ed 7.5.6) — Conditional PDF, conditional expectation

> [!example] **Problem.** $f_{X,Y}(x,y) = 1/2$ for $-1 < x < y < 1$, else 0.
> (a) $f_Y(y)$. (b) $f_{X\mid Y}(x\mid y)$. (c) $E[X\mid Y = y]$.

### (a)

$$f_Y(y) = \int_{-1}^y \frac{1}{2}\, dx = \frac{y + 1}{2}, \quad -1 < y < 1.$$

### (b)

$$f_{X\mid Y}(x\mid y) = \frac{1/2}{(y+1)/2} = \frac{1}{y+1}, \quad -1 < x < y.$$

So $X \mid Y = y \sim \text{Uniform}(-1, y)$.

### (c)

$$E[X\mid Y = y] = \frac{-1 + y}{2} = \frac{y - 1}{2}.$$

**Answer:** $f_Y(y) = (y+1)/2$, $f_{X\mid Y}(x\mid y) = 1/(y+1)$ on $(-1, y)$, $E[X\mid Y=y] = (y-1)/2$.

> [!tip] **Internalize.** Conditional density is $f_{X,Y}/f_Y$ — **on the conditional support.** When conditional density is uniform, conditional mean is midpoint of support.

---

## Problem 13 (3rd-ed 5.7.4) — Independence + moments

> [!example] **Problem.** $X, Y$ i.i.d. with $P[X = 0] = 3/4$, $P[X = 20] = 1/4$. Find $E[X], \text{Var}[X], E[X+Y], \text{Var}[X+Y], E[XY 2^{XY}]$.

### Compute

$$E[X] = 0\cdot 3/4 + 20\cdot 1/4 = 5.$$

$$E[X^2] = 0 + 400/4 = 100. \qquad \text{Var}[X] = 100 - 25 = 75.$$

$$E[X + Y] = 10. \qquad \text{Var}[X + Y] = \text{Var}[X] + \text{Var}[Y] = 150.$$

For $E[XY 2^{XY}]$: $XY \in \{0, 0, 0, 400\}$ with probs $\{9/16, 3/16, 3/16, 1/16\}$. Only the $XY = 400$ outcome contributes:

$$E[XY 2^{XY}] = \frac{1}{16}\cdot 400\cdot 2^{400}.$$

That's a wild number — but the structure is what's asked.

**Answer:** $E[X]=5$, $\text{Var}[X]=75$, $E[X+Y]=10$, $\text{Var}[X+Y]=150$, $E[XY 2^{XY}] = (1/16)(400)(2^{400})$.

> [!tip] **Internalize.** **Independence $\Rightarrow$ variances add.** For functions of $X, Y$ when $X = Y = 0$ on most of the sample space, **only the non-zero outcomes contribute** — enumerate, don't try to find a closed form for $E[g(XY)]$.

---

## Problem 14 (3rd-ed 5.7.7) — Difference of geometrics

> [!example] **Problem.** $X_1$ = flips up to 1st H. $X_2$ = additional flips up to 2nd H. $Y = X_1 - X_2$. Find $E[Y], \text{Var}[Y]$.

$X_1, X_2$ i.i.d. $\text{Geometric}(1/2)$. $E[X_i] = 2$, $\text{Var}[X_i] = (1 - 1/2)/(1/2)^2 = 2$.

$$E[Y] = E[X_1] - E[X_2] = 0.$$

$$\text{Var}[Y] = \text{Var}[X_1] + \text{Var}[X_2] = 4.$$

**Answer:** $E[Y] = 0$, $\text{Var}[Y] = 4$.

> [!warning] **Gotcha.** Variance of difference of independent RVs **adds**, doesn't subtract: $\text{Var}[X_1 - X_2] = \text{Var}[X_1] + \text{Var}[X_2]$ when independent.

---

## Problem 15 (3rd-ed 9.1.1) — i.i.d. difference

> [!example] **Problem.** $X_1, X_2$ i.i.d. with $\text{Var}[X]$. Find $E[X_1 - X_2], \text{Var}[X_1 - X_2]$.

$E[X_1 - X_2] = 0$. $\text{Var}[X_1 - X_2] = \text{Var}[X_1] + \text{Var}[X_2] = 2\text{Var}[X]$.

**Answer:** Mean 0, variance $2\text{Var}[X]$. (Same identity as Problem 3 in Module 7.)

---

## Cross-references

- **Course page:** [[eee-350]]
- **Master review:** [[eee-350-final-walkthrough]]
- **Adjacent walkthroughs:** [[eee-350-module-05-derived-rvs-sums-walkthrough]], [[eee-350-module-06-clt-lln-mgf-walkthrough]] (more on sums and MGFs).
- **Concept pages:** [[joint-distribution]], [[marginal-distribution]], [[conditional-rvs]], [[independence-rvs]], [[derived-rvs]], [[max-of-iid]], [[min-of-iid]].

