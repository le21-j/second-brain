---
title: EEE 350 HW7 — Significance Testing & MMSE/LMSE Estimation (Walkthrough)
type: example
course: [[eee-350]]
tags: [eee-350, homework, walkthrough, significance-test, lmse, mmse, estimation, hypothesis-testing]
sources: [[homework-2026-04-23-eee-350-hw7]]
created: 2026-04-26
updated: 2026-04-26
---

# EEE 350 HW7 — Walkthrough

> [!note] **What this is.** A per-problem walkthrough of HW7. For every problem I (a) **state it** verbatim, (b) **explain the overarching concept** so you understand what's being tested, (c) **walk through the derivation step by step** so you can reproduce it on paper, and (d) **link** to the standalone worked-example page for full algebraic detail.
>
> The **highlighted lines** (like this) are the headline answers — what to write down on the submission.

> [!warning] **Format mirrors the EEE 304 HW7 walkthrough.** Concept-first then steps, bold + Obsidian `highlights` + callout blocks. Companion pages for each problem live in `wiki/examples/` already; this page is the unified entry point.

---

## Problem 11.1.6 — Significance Test for a Fair Coin

> **Problem 11.1.6.** Let $K$ be the number of heads in $n = 100$ flips of a coin. Devise a significance test for the hypothesis $H$ that the coin is fair, with significance level $\alpha = 0.05$ and rejection set of the form $R = \{|K - E[K]| > c\}$.

### The concept

A **significance test** budgets the probability of falsely rejecting a default hypothesis (Type I error) at level $\alpha$. The decision rule is: reject $H$ if the observed test statistic falls in a rejection region $R$ chosen so that $P(K \in R \mid H) \leq \alpha$. The test "looks at" $K$ and decides whether $K$ deviates from its $H$-implied mean by more than the budget allows.

> [!tip] **Two-sided z-score memo.** $z_{0.025} = 1.96$. This pops out for any $\alpha = 0.05$ two-tailed test. See [[standard-normal-table]].

### Walkthrough

> [!example] **Step-by-step**
>
> **Step 1 — Distribution under $H$.** If the coin is fair, $K \sim \text{Binomial}(100, 0.5)$:
> $$E[K] = np = 50, \qquad \text{Var}(K) = np(1 - p) = 25, \qquad \sigma_K = 5.$$
>
> **Step 2 — Write the budget constraint.**
> $$P(|K - 50| > c \mid H) \leq 0.05.$$
>
> **Step 3 — Apply CLT + standardize.** $n = 100$ is large; the [[central-limit-theorem|CLT]] approximation is excellent. [[standardization|Standardize]] $K$:
> $$Z = \frac{K - 50}{5} \approx \mathcal{N}(0, 1) \;\;\Longrightarrow\;\; P(|K - 50| > c) \approx 2\bigl(1 - \Phi(c/5)\bigr).$$
>
> **Step 4 — Solve for $c$.**
> $$2\bigl(1 - \Phi(c/5)\bigr) = 0.05 \;\Longrightarrow\; \Phi(c/5) = 0.975 \;\Longrightarrow\; c/5 = 1.96 \;\Longrightarrow\; c = 9.8.$$
>
> **Step 5 — State the rule.** Reject $H$ if $|K - 50| > 9.8$, i.e. $K \leq 40$ or $K \geq 60$ (integer-rounded conservatively).

### Answer

**Significance test:** reject $H$ if $|K - 50| > 9.8$ (equivalently $K \leq 40$ or $K \geq 60$). The critical constant is $c = 9.8$, and the integer-snap rejection region is conservative ($P(\text{reject} \mid H) \approx 0.0455 \leq 0.05$).

> [!warning] **$\alpha$ refers to *experiments*, not to individual flips.** The 5% describes how often the *whole 100-flip experiment* would falsely reject $H$ if you repeated it many times. It is **not** "5% of the flips disagree." See [[prob-gotchas]] entry on this — it's the most common conceptual slip.

> [!example] **Full derivation:** see [[fair-coin-significance-test]].

---

## Problem 12.2.3 — Linear MMSE from a Discrete Joint PMF

> **Problem 12.2.3.** Random variables $X$ and $Y$ have a joint PMF given by a $3 \times 3$ table over $x, y \in \{-1, 0, 1\}$ (cells: $3/16, 1/16, 0$ in row $x = -1$; $1/6, 1/6, 1/6$ in row $x = 0$; $0, 1/8, 1/8$ in row $x = 1$). Estimate $Y$ by $\hat Y_L(X) = aX + b$. **(a)** Find $a, b$ minimizing MSE. **(b)** Find the minimum MSE $e_L^*$.

### The concept

**Linear MMSE (LMSE)** restricts the estimator to the form $aX + b$. The optimal $(a, b)$ depends on **only five numbers**: $E[X], E[Y], \text{Var}(X), \text{Var}(Y), \text{Cov}(X,Y)$. Every other detail of the joint distribution is irrelevant to the linear estimator.

**The formulas (memorize):**
$$a^* = \frac{\text{Cov}(X,Y)}{\text{Var}(X)}, \qquad b^* = E[Y] - a^*\,E[X].$$
$$\hat Y_L(X) = E[Y] + \frac{\text{Cov}(X,Y)}{\text{Var}(X)}\bigl(X - E[X]\bigr), \qquad e_L^* = \text{Var}(Y)\bigl(1 - \rho_{X,Y}^2\bigr).$$

> [!tip] **Geometric picture.** Treat random variables as vectors in a Hilbert space with inner product $\langle U, V\rangle = E[UV]$. LMSE is the **orthogonal projection** of $Y$ onto the 2-D subspace $\text{span}\{1, X\}$. The two orthogonality conditions (residual $\perp 1$, residual $\perp X$) yield the formulas above.

### Walkthrough

> [!example] **Step-by-step**
>
> **Step 1 — Marginals.** Row sums give $P_X(-1) = 1/4$, $P_X(0) = 1/2$, $P_X(1) = 1/4$. Column sums (common denominator $48$) give $P_Y(-1) = 17/48$, $P_Y(0) = 17/48$, $P_Y(1) = 14/48$.
>
> **Step 2 — Moments of $X$.** By symmetry, $E[X] = 0$. Then $E[X^2] = 1/2$, so $\text{Var}(X) = 1/2$.
>
> **Step 3 — Moments of $Y$.** $E[Y] = -3/48 = -1/16$. $E[Y^2] = 31/48$. $\text{Var}(Y) = 31/48 - 1/256 = 493/768$.
>
> **Step 4 — $E[XY]$.** Only cells with both $x \neq 0$ and $y \neq 0$ contribute:
> $$E[XY] = (-1)(-1)\tfrac{3}{16} + (1)(1)\tfrac{1}{8} = \tfrac{5}{16}.$$
> So $\text{Cov}(X,Y) = 5/16 - 0 \cdot (-1/16) = 5/16$.
>
> **Step 5 — LMSE coefficients.**
> $$a^* = \frac{5/16}{1/2} = \tfrac{5}{8}, \qquad b^* = -\tfrac{1}{16} - \tfrac{5}{8}\cdot 0 = -\tfrac{1}{16}.$$
>
> **Step 6 — Minimum MSE.**
> $$e_L^* = \tfrac{493}{768} - \frac{(5/16)^2}{1/2} = \tfrac{493}{768} - \tfrac{150}{768} = \tfrac{343}{768} \approx 0.447.$$

### Answer

**(a)** $\hat Y_L(X) = \tfrac{5}{8}X - \tfrac{1}{16}$. **(b)** $e_L^* = \tfrac{343}{768} \approx 0.447$.

> [!note] **Sanity check.** $\rho^2 = (5/16)^2 / [(1/2)(493/768)] = 150/493 \approx 0.30$. So $X$ explains 30% of $\text{Var}(Y)$ linearly — consistent with $e_L^* / \text{Var}(Y) = 343/493 \approx 0.70$.

> [!example] **Full derivation:** see [[lmse-discrete-pmf]].

---

## Problem 12.2.4 — Linear MMSE for Continuous Joint PDF

> **Problem 12.2.4.** Random variables $X$ and $Y$ have joint PDF $f_{X,Y}(x,y) = 2(y + x)$ on the triangular region $0 \leq x \leq y \leq 1$ (and $0$ elsewhere). Find $\hat X_L(Y)$, the linear MMSE estimate of $X$ given $Y$.

### The concept

Same LMSE machinery as 12.2.3, but now we **estimate $X$ from $Y$** (roles swapped — the formula uses $\text{Var}(Y)$ in the denominator):
$$\hat X_L(Y) = E[X] + \frac{\text{Cov}(X,Y)}{\text{Var}(Y)}\bigl(Y - E[Y]\bigr).$$
The continuous version replaces sums with integrals over the support.

> [!warning] **Sketch the support first.** $0 \leq x \leq y \leq 1$ is a **triangle** with corners $(0,0), (0,1), (1,1)$. For fixed $y$, $x$ ranges over $[0, y]$. For fixed $x$, $y$ ranges over $[x, 1]$. Getting the integration limits wrong is the **#1 error source** on these problems.

### Walkthrough

> [!example] **Step-by-step**
>
> **Step 1 — Marginal of $Y$.** For fixed $y$, $x$ ranges over $[0, y]$:
> $$f_Y(y) = \int_0^y 2(y + x)\,dx = 2y^2 + y^2 = 3y^2, \quad 0 \leq y \leq 1.$$
>
> **Step 2 — Moments of $Y$.**
> $$E[Y] = \int_0^1 3y^3\,dy = \tfrac{3}{4}, \qquad E[Y^2] = \int_0^1 3y^4\,dy = \tfrac{3}{5}, \qquad \text{Var}(Y) = \tfrac{3}{5} - \tfrac{9}{16} = \tfrac{3}{80}.$$
>
> **Step 3 — Marginal of $X$.** For fixed $x$, $y$ ranges over $[x, 1]$:
> $$f_X(x) = \int_x^1 2(y + x)\,dy = 1 + 2x - 3x^2.$$
>
> **Step 4 — Mean of $X$.**
> $$E[X] = \int_0^1 x(1 + 2x - 3x^2)\,dx = \tfrac{1}{2} + \tfrac{2}{3} - \tfrac{3}{4} = \tfrac{5}{12}.$$
>
> **Step 5 — $E[XY]$.** Inner integral in $x$ over $[0, y]$ gives $\tfrac{5}{3}y^4$; outer integral in $y$ over $[0, 1]$ gives $\tfrac{1}{3}$.
>
> **Step 6 — Covariance.**
> $$\text{Cov}(X,Y) = \tfrac{1}{3} - \tfrac{5}{12}\cdot\tfrac{3}{4} = \tfrac{1}{48}.$$
>
> **Step 7 — Coefficients.**
> $$a^* = \frac{1/48}{3/80} = \tfrac{5}{9}, \qquad b^* = \tfrac{5}{12} - \tfrac{5}{9}\cdot\tfrac{3}{4} = 0.$$

### Answer

$\hat X_L(Y) = \tfrac{5}{9}\,Y$. ($b^* = 0$ — the regression line passes through the origin.)

> [!tip] **Why $b^* = 0$ here.** The geometry of the triangular support ties the means: $E[X] = 5/12 = (5/9)\cdot(3/4) = (5/9)\,E[Y]$. Whenever the means already lie on the optimal regression line through the origin, $b^*$ is zero.

> [!example] **Full derivation:** see [[lmse-continuous-pdf]].

---

## Problem 12.2.6 — MMSE vs LMSE with an Erlang Prior

> **Problem 12.2.6.** $X$ has second-order Erlang PDF $f_X(x) = \lambda^2 x e^{-\lambda x}$ for $x \geq 0$. Given $X = x$, $Y$ is Uniform on $(0, x)$. Find: **(a)** $\hat y_M(x) = E[Y \mid X = x]$. **(b)** $\hat x_M(y) = E[X \mid Y = y]$. **(c)** $\hat Y_L(X)$. **(d)** $\hat X_L(Y)$.

### The concept

**MMSE vs LMSE — the cleanest comparison in estimation theory.** This is the table to memorize:

| | **MMSE (unrestricted)** | **LMSE (linear only)** |
|:---|:---|:---|
| Form | Any function $g(\cdot)$ — typically $E[\cdot \mid \cdot]$ | $aX + b$ |
| Needs | Full conditional distribution | First + second moments only |
| Error | Smallest possible MSE | $\geq$ MMSE error |
| When equal | When $E[Y \mid X]$ is **affine in $X$** (e.g. jointly Gaussian) | — |

> [!important] **Spoiler.** Both conditional means in this problem turn out to be affine, so MMSE $=$ LMSE in both directions. That's the lesson — recognize the affine-conditional-mean condition.

**Erlang $(2, \lambda)$ facts (used throughout):**
$$E[X] = \tfrac{2}{\lambda}, \quad \text{Var}(X) = \tfrac{2}{\lambda^2}, \quad E[X^2] = \tfrac{6}{\lambda^2}.$$

### Walkthrough

> [!example] **Part (a) — MMSE of $Y$ given $X$.**
>
> Conditional distribution given directly: $Y \mid X = x \sim \text{Uniform}(0, x)$. Therefore
> $$\hat y_M(x) = E[Y \mid X = x] = \tfrac{x}{2}.$$
> No integration needed.

> [!example] **Part (b) — MMSE of $X$ given $Y$ (via Bayes).**
>
> **Step 1 — Joint PDF.** $f_{X,Y}(x,y) = f_{Y\mid X}(y\mid x)\,f_X(x) = \tfrac{1}{x}\cdot\lambda^2 x e^{-\lambda x} = \lambda^2 e^{-\lambda x}$ on $0 \leq y \leq x$.
>
> **Step 2 — Marginal of $Y$.** $f_Y(y) = \int_y^\infty \lambda^2 e^{-\lambda x}\,dx = \lambda e^{-\lambda y}$. **So $Y \sim \text{Exp}(\lambda)$** — neat byproduct.
>
> **Step 3 — Conditional of $X$ given $Y$.** $f_{X\mid Y}(x \mid y) = \lambda e^{-\lambda(x - y)}$ for $x \geq y$. So $(X - y) \mid Y = y \sim \text{Exp}(\lambda)$ — **memorylessness**.
>
> **Step 4 — Conditional mean.** $\hat x_M(y) = y + 1/\lambda$ — **linear in $y$**.

> [!example] **Part (c) — LMSE of $Y$ given $X$.**
>
> **Tower trick for $E[Y]$:** $E[Y] = E[E[Y \mid X]] = E[X/2] = 1/\lambda$.
> **Tower trick for $E[XY]$:** $E[XY] = E[X\cdot E[Y \mid X]] = E[X^2/2] = 3/\lambda^2$.
> **Covariance:** $\text{Cov}(X,Y) = 3/\lambda^2 - (2/\lambda)(1/\lambda) = 1/\lambda^2$.
> **Coefficients:** $a^* = (1/\lambda^2) / (2/\lambda^2) = 1/2$, $b^* = 1/\lambda - (1/2)(2/\lambda) = 0$.
>
> $$\hat Y_L(X) = \tfrac{X}{2}.$$
>
> **Matches part (a) exactly** — as expected since (a) was already linear.

> [!example] **Part (d) — LMSE of $X$ given $Y$.**
>
> **Variance of $Y$:** $\text{Var}(Y) = 1/\lambda^2$ (since $Y \sim \text{Exp}(\lambda)$).
> **Coefficients:** $a^* = (1/\lambda^2) / (1/\lambda^2) = 1$, $b^* = 2/\lambda - 1\cdot 1/\lambda = 1/\lambda$.
>
> $$\hat X_L(Y) = Y + \tfrac{1}{\lambda}.$$
>
> **Matches part (b) exactly** — confirming that whenever $E[X \mid Y]$ is affine, LMSE catches up to MMSE without restriction.

### Answer

**(a)** $\hat y_M(x) = x/2$. **(b)** $\hat x_M(y) = y + 1/\lambda$. **(c)** $\hat Y_L(X) = X/2$ (matches a). **(d)** $\hat X_L(Y) = Y + 1/\lambda$ (matches b). The takeaway: **affine conditional mean $\Rightarrow$ LMSE = MMSE**.

> [!tip] **Pattern to remember.** If your computed MMSE turns out linear in the observation, you've gained nothing by restricting to LMSE — the two estimators coincide. This is also the structural reason LMSE is optimal under joint Gaussianity (where $E[Y \mid X]$ is automatically linear).

> [!example] **Full derivation:** see [[mmse-vs-lmse-erlang]].

---

## Cross-references

- [[significance-test]] — Problem 11.1.6's framework
- [[linear-mmse-estimation]] — the LMSE formulas used in 12.2.3, 12.2.4, 12.2.6 (c, d)
- [[lms-estimation]] — the unrestricted MMSE used in 12.2.6 (a, b); see naming-conflict table
- [[iterated-expectations]] — the tower property used heavily in 12.2.6 (c)
- [[standardization]], [[central-limit-theorem]], [[standard-normal-table]] — used in 11.1.6
- [[variance-scaling-rule]] — the $\text{Var}(cX) = c^2\text{Var}(X)$ identity behind the $\sigma_K = 5$ standardization
- [[homework-2026-04-23-eee-350-hw7]] — source summary (catalog entry)
- [[eee-350]] — course page
- [[prob-gotchas]] — running list of mistakes flagged from this HW

## Report template (copy-paste skeleton)

```
EEE 350 HW7
Name: Jayden Le      Date: <due date>

Problem 11.1.6 (significance test)
   K ~ Binomial(100, 0.5) under H => E[K]=50, Var(K)=25, sigma_K=5.
   CLT + standardize => P(|K-50| > c) ≈ 2(1 - Phi(c/5)).
   Set 2(1 - Phi(c/5)) = 0.05 => Phi(c/5) = 0.975 => c/5 = 1.96 => c = 9.8.
   ANSWER: reject H if |K - 50| > 9.8 (i.e. K <= 40 or K >= 60).

Problem 12.2.3 (LMSE from discrete joint PMF)
   E[X]=0, Var(X)=1/2, E[Y]=-1/16, Var(Y)=493/768, Cov(X,Y)=5/16.
   a* = Cov/Var(X) = 5/8.    b* = E[Y] - a*·E[X] = -1/16.
   e_L* = Var(Y) - Cov^2/Var(X) = 343/768 ≈ 0.447.
   ANSWER: Y_L(X) = (5/8)X - 1/16.   e_L* = 343/768.

Problem 12.2.4 (LMSE from continuous joint PDF on triangle)
   f_Y(y) = 3y^2,  E[Y] = 3/4,  Var(Y) = 3/80.
   E[X] = 5/12,    E[XY] = 1/3,  Cov(X,Y) = 1/48.
   a* = (1/48)/(3/80) = 5/9.    b* = 5/12 - (5/9)(3/4) = 0.
   ANSWER: X_L(Y) = (5/9) Y.

Problem 12.2.6 (MMSE vs LMSE with Erlang(2, lambda))
   (a) y_M(x) = E[Y|X=x] = x/2.
   (b) Joint => f_Y(y) = lambda·exp(-lambda·y) (Y is Exp(lambda));
       f_{X|Y} => (X - y) | Y ~ Exp(lambda) => x_M(y) = y + 1/lambda.
   (c) Tower => E[Y] = 1/lambda,  E[XY] = 3/lambda^2,  Cov = 1/lambda^2.
       a* = 1/2, b* = 0  =>  Y_L(X) = X/2  (matches (a)).
   (d) Var(Y) = 1/lambda^2.
       a* = 1, b* = 1/lambda  =>  X_L(Y) = Y + 1/lambda  (matches (b)).
   ANSWER: in both directions MMSE = LMSE because both conditional
           means are affine in the observation.
```

> [!note] **About the report template above.** It's intentionally written in plain ASCII (Greek letters as words, no `$...$`) — it's a skeleton for a Word doc / handwritten submission, not a wiki page. The wiki body above renders the same equations in proper LaTeX.
