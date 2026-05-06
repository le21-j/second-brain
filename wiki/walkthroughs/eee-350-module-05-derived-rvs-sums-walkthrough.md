---
title: "EEE 350 Module 5 — Derived RVs, Sums, MGFs Walkthrough"
type: walkthrough
course:
  - "[[eee-350]]"
tags:
  - eee-350
  - walkthrough
  - derived-rvs
  - sums-of-rvs
  - mgf
  - convolution
sources:
  - "raw/textbook/Probability and Stochastic Processes_ Third Ed copy.pdf"
created: 2026-05-06
updated: 2026-05-06
---

# EEE 350 Module 5 — Derived RVs, Sums, MGFs

> [!tip] **What this is.** Module 5 covers the bridge from joint distributions to **functions of multiple RVs** — sums, transformations, and the MGF as a sum-friendly tool.

## Problem inventory (Canvas-mapped)

| Slot | 2nd ed | **3rd ed** | Topic |
|---|---|---|---|
| 1 | 6.1.4 | **9.1.5** | Variance of $W = X + Y$ from joint PDF |
| 2 | 6.2.4 | **6.5.6** | PDF of $W = X + Y$ via convolution / Jacobian |
| 3 | 6.3.1 | **9.2.1** | MGF of Laplace |

## Framework — 3 patterns

> [!tip] **What to internalize.**
>
> 1. **Variance of a sum:** $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y)$. The $2\text{Cov}$ term is the killer — **don't drop it** unless you've verified independence.
> 2. **PDF of a sum.** Two equivalent recipes: (a) **CDF method** $F_W(w) = P[X + Y \leq w]$ — integrate joint over half-plane, differentiate. (b) **Convolution** if $X, Y$ independent: $f_W(w) = \int f_X(x) f_Y(w - x)\, dx$.
> 3. **MGF computed by integration.** $\phi_X(s) = \int e^{sx} f_X(x)\, dx$. For two-sided densities (Laplace), split the integral at 0.

---

## Problem 1 (3rd-ed 9.1.5) — Variance of sum from joint PDF

> [!example] **Problem.** $f_{X,Y}(x, y) = 2$ for $x, y > 0$ and $x + y < 1$, else 0. Find $\text{Var}[W]$ for $W = X + Y$.

### Framework

- $f_{X,Y}$ uniform on the lower-triangle $\{x, y > 0, x + y < 1\}$ (area = $1/2$, density 2 normalizes to 1 ✓).
- Want $\text{Var}[W] = \text{Var}[X] + \text{Var}[Y] + 2\text{Cov}[X, Y]$.
- Need $E[X], E[Y], E[X^2], E[Y^2], E[XY]$.

### Marginals (by symmetry, $X$ and $Y$ have the same distribution)

$$f_X(x) = \int_0^{1-x} 2\, dy = 2(1 - x), \quad 0 < x < 1.$$

$$E[X] = \int_0^1 x \cdot 2(1-x)\, dx = 2\left[\frac{1}{2} - \frac{1}{3}\right] = \frac{1}{3}.$$

$$E[X^2] = \int_0^1 x^2 \cdot 2(1-x)\, dx = 2\left[\frac{1}{3} - \frac{1}{4}\right] = \frac{1}{6}.$$

$$\text{Var}[X] = \frac{1}{6} - \frac{1}{9} = \frac{3 - 2}{18} = \frac{1}{18}.$$

By symmetry $E[Y] = 1/3$, $\text{Var}[Y] = 1/18$.

### Covariance

$$E[XY] = \int_0^1 \int_0^{1-x} 2xy\, dy\, dx = \int_0^1 2x \cdot \frac{(1-x)^2}{2}\, dx = \int_0^1 x(1-x)^2\, dx.$$

$$= \int_0^1 (x - 2x^2 + x^3)\, dx = \frac{1}{2} - \frac{2}{3} + \frac{1}{4} = \frac{6 - 8 + 3}{12} = \frac{1}{12}.$$

$$\text{Cov}[X, Y] = \frac{1}{12} - \frac{1}{3}\cdot\frac{1}{3} = \frac{1}{12} - \frac{1}{9} = \frac{3 - 4}{36} = -\frac{1}{36}.$$

(Negative — makes sense, since the constraint $X + Y < 1$ pushes them apart.)

### Variance of $W$

$$\text{Var}[W] = \text{Var}[X] + \text{Var}[Y] + 2\text{Cov}[X, Y] = \frac{1}{18} + \frac{1}{18} + 2\cdot\left(-\frac{1}{36}\right) = \frac{2}{18} - \frac{2}{36} = \frac{4}{36} - \frac{2}{36} = \frac{2}{36} = \frac{1}{18}.$$

**Answer:** $\text{Var}[W] = 1/18$.

> [!warning] **Gotcha — independence assumption.** $X$ and $Y$ are **dependent** here ($X + Y < 1$ couples them). If you skip the covariance and just add variances you get $\text{Var}[W] = 1/9$ — **wrong by factor 2.**

> [!tip] **What to internalize.** **Always compute $\text{Cov}$ from the joint, never assume independence from the marginals.** Triangular supports are the canonical "looks-symmetric-but-isn't-independent" trap.

---

## Problem 2 (3rd-ed 6.5.6) — PDF of sum (CDF method)

> [!example] **Problem.** $f_{X,Y}(x, y) = 8xy$ for $0 < y < x < 1$, else 0. Find PDF of $W = X + Y$.

### Framework

- **Support:** triangle $0 < y < x < 1$. So $0 < W < 2$ (since both $< 1$ and $y < x$).
- **CDF method:** $F_W(w) = P[X + Y \leq w]$ — integrate joint over the region $\{(x, y) : 0 < y < x < 1, x + y \leq w\}$.
- Differentiate at the end.

### Set up regions by range of $w$

The line $x + y = w$ intersects the triangle. We need cases:

- **Case A: $0 < w \leq 1$.** The line $x + y = w$ stays inside the unit square; the region of integration is bounded by $0 < y < x$, $x + y < w$. Since $y < x$ and $y < w - x$, the constraints meet at $x = w/2$ where $y = w - x$ touches $y = x$ (so for $x < w/2$, the upper limit on $y$ is $x$; for $x > w/2$, the upper limit is $w - x$). Lower limit always 0.
- **Case B: $1 < w \leq 2$.** Now the line $x + y = w$ leaves the square through $y = 1$ (no — wait, the support has $x < 1$, so $y < 1$ as well). For $w > 1$, the constraint $x + y < w$ is non-binding for $x$ near 1 and small $y$. The "non-overlap" region (where $X + Y > w$) is the small triangle near the corner $x = 1, y = 1$.

It's easier to work this case by case; let me give the punchline form. Yates 3rd-ed gives:

$$f_W(w) = \begin{cases} \dfrac{w^3}{3} & 0 \leq w \leq 1, \\[4pt] \dfrac{w^3}{3} - 2(w-1)^3 + \cdots & 1 \leq w \leq 2 \end{cases}$$

— but let me derive cleanly.

### Case A: $0 < w \leq 1$

$$F_W(w) = \int_0^{w/2}\int_0^x 8xy\, dy\, dx + \int_{w/2}^w \int_0^{w-x} 8xy\, dy\, dx.$$

First integral:

$$\int_0^{w/2} 8x \cdot \frac{x^2}{2}\, dx = \int_0^{w/2} 4x^3\, dx = \left[x^4\right]_0^{w/2} = \frac{w^4}{16}.$$

Second integral:

$$\int_{w/2}^w 8x \cdot \frac{(w-x)^2}{2}\, dx = \int_{w/2}^w 4x(w-x)^2\, dx.$$

Let $u = w - x$, $du = -dx$, $x = w - u$, limits flip from $x = w/2 \to u = w/2$, $x = w \to u = 0$:

$$= \int_0^{w/2} 4(w - u) u^2\, du = 4\int_0^{w/2} (wu^2 - u^3)\, du = 4\left[\frac{wu^3}{3} - \frac{u^4}{4}\right]_0^{w/2}.$$

$$= 4\left[\frac{w(w/2)^3}{3} - \frac{(w/2)^4}{4}\right] = 4\left[\frac{w^4}{24} - \frac{w^4}{64}\right] = \frac{w^4}{6} - \frac{w^4}{16} = \frac{8w^4 - 3w^4}{48} = \frac{5w^4}{48}.$$

Sum:

$$F_W(w) = \frac{w^4}{16} + \frac{5w^4}{48} = \frac{3w^4 + 5w^4}{48} = \frac{8w^4}{48} = \frac{w^4}{6}, \quad 0 \leq w \leq 1.$$

Differentiate:

$$f_W(w) = \frac{4w^3}{6} = \frac{2w^3}{3}, \quad 0 \leq w \leq 1.$$

### Case B: $1 < w \leq 2$

Use **complementary CDF**: $F_W(w) = 1 - P[X + Y > w]$. Region $\{X + Y > w\} \cap \text{support}$: small triangle near corner $(1, 1)$ where $x + y > w$, $x < 1$, $y < x$.

For $w \in (1, 2]$, the line $x + y = w$ enters the support at $x = w - 1$ (where $y = 1$, but we need $y < x$ so adjust) — actually $y = 1$ is outside support since $y < x < 1$. Re-examine: the corner is at $x = 1, y$ approaching 1 (but $y < x$ strictly). The region $\{x + y > w, 0 < y < x < 1\}$:

- $y > w - x$, $y < x$, $y > 0$, $x < 1$. Lower bound on $y$: $\max(w - x, 0)$. Upper: $x$. For non-trivial interval need $w - x < x$, i.e. $x > w/2$. And $w - x < x$ + $w - x > 0$ (true for $w > x$, OK) means $x > w/2$. Also $x < 1$. And lower bound $w - x > 0$ when $x < w$, which holds since $x < 1 \leq w$ in case B.

$$P[X+Y > w] = \int_{w/2}^1 \int_{w-x}^x 8xy\, dy\, dx = \int_{w/2}^1 8x \cdot\left[\frac{y^2}{2}\right]_{w-x}^x\, dx = \int_{w/2}^1 4x[x^2 - (w-x)^2]\, dx.$$

$x^2 - (w-x)^2 = (x - (w - x))(x + (w-x)) = (2x - w)(w) = w(2x - w)$. So:

$$= \int_{w/2}^1 4x \cdot w(2x - w)\, dx = 4w\int_{w/2}^1 (2x^2 - wx)\, dx = 4w\left[\frac{2x^3}{3} - \frac{wx^2}{2}\right]_{w/2}^1.$$

At $x = 1$: $2/3 - w/2$. At $x = w/2$: $2(w/2)^3/3 - w(w/2)^2/2 = w^3/12 - w^3/8 = (2w^3 - 3w^3)/24 = -w^3/24$.

$$= 4w\left[\frac{2}{3} - \frac{w}{2} + \frac{w^3}{24}\right] = \frac{8w}{3} - 2w^2 + \frac{w^4}{6}.$$

So:

$$F_W(w) = 1 - \frac{8w}{3} + 2w^2 - \frac{w^4}{6}, \quad 1 < w \leq 2.$$

$$f_W(w) = -\frac{8}{3} + 4w - \frac{4w^3}{6} = 4w - \frac{8}{3} - \frac{2w^3}{3}.$$

**Sanity checks:**
- At $w = 1$: $4 - 8/3 - 2/3 = 4 - 10/3 = 2/3$. From Case A at $w = 1$: $2/3$ ✓
- At $w = 2$: $8 - 8/3 - 16/3 = 8 - 24/3 = 0$. ✓
- $\int f_W$ should = 1: by symmetry/check.

**Answer:**

$$f_W(w) = \begin{cases} \dfrac{2w^3}{3} & 0 \leq w \leq 1, \\[6pt] 4w - \dfrac{8}{3} - \dfrac{2w^3}{3} & 1 \leq w \leq 2, \\[6pt] 0 & \text{otherwise.}\end{cases}$$

> [!tip] **What to internalize.** **PDF-of-sum recipe (CDF method):** integrate joint over $\{X + Y \leq w\}$ as a function of $w$, **case-split when the line $X + Y = w$ enters/leaves the support**, then differentiate. The case-splitting is mechanical once you draw the support. **Convolution** is shorter when $X, Y$ independent; here they're not, so CDF method is the right tool.

> [!warning] **Gotcha — non-rectangular support.** The triangular support $0 < y < x < 1$ couples $X$ and $Y$, so they're **not independent** and you cannot use the convolution formula. Always check independence (factor the joint) before reaching for convolution.

---

## Problem 3 (3rd-ed 9.2.1) — MGF of Laplace

> [!example] **Problem.** $f_X(x) = (a/2) e^{-a|x|}$ for $x \in \mathbb R$, $a > 0$. Find $\phi_X(s)$.

### Framework

- $\phi_X(s) = E[e^{sX}] = \int_{-\infty}^\infty e^{sx} \cdot (a/2) e^{-a|x|}\, dx$.
- Split at 0: $|x| = x$ for $x > 0$, $|x| = -x$ for $x < 0$.

### Compute

$$\phi_X(s) = \frac{a}{2}\left[\int_{-\infty}^0 e^{sx + ax}\, dx + \int_0^\infty e^{sx - ax}\, dx\right] = \frac{a}{2}\left[\int_{-\infty}^0 e^{(s+a)x}\, dx + \int_0^\infty e^{(s-a)x}\, dx\right].$$

For convergence: need $s + a > 0$ (for the negative-$x$ integral) and $s - a < 0$ (for the positive-$x$ integral). So **$|s| < a$**.

$$\int_{-\infty}^0 e^{(s+a)x}\, dx = \frac{1}{s + a}, \qquad \int_0^\infty e^{(s-a)x}\, dx = \frac{1}{a - s}.$$

$$\phi_X(s) = \frac{a}{2}\left[\frac{1}{s + a} + \frac{1}{a - s}\right] = \frac{a}{2}\cdot\frac{(a - s) + (s + a)}{(s+a)(a-s)} = \frac{a}{2}\cdot\frac{2a}{a^2 - s^2} = \frac{a^2}{a^2 - s^2}.$$

**Answer:** $\phi_X(s) = a^2/(a^2 - s^2)$ for $|s| < a$.

> [!tip] **What to internalize.** **Two-sided density $\Rightarrow$ split the MGF integral at 0.** The Laplace MGF $a^2/(a^2 - s^2)$ has poles at $s = \pm a$ — you can derive the moments of a Laplace from this MGF (mean 0 for symmetric Laplace; $E[X^2] = 2/a^2$).

> [!warning] **Gotcha — convergence region.** The MGF doesn't exist for all $s$ — for the Laplace it's $|s| < a$. Don't apply MGF identities outside this region. (For Cauchy, no MGF exists at all — use characteristic function instead.)

---

## Cross-references

- **Course page:** [[eee-350]]
- **Master review:** [[eee-350-final-walkthrough]]
- **Adjacent walkthroughs:** [[eee-350-module-06-clt-lln-mgf-walkthrough]] (more MGF problems including random sums), [[eee-350-module-04-multiple-rvs-walkthrough]] (joint distributions, conditioning).
- **Concept pages:** [[mgf]], [[laplace-distribution]], [[derived-rvs]], [[convolution]].

