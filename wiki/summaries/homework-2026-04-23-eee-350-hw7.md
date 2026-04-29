---
title: EEE 350 HW7 — Significance Testing & MMSE/LMSE Estimation
type: summary
source_type: homework
source_path: raw/homework/EEE350_HW7.md
source_date: 2026-04-23
course: [[eee-350]]
tags: [eee-350, homework, probability, statistics, estimation-theory, hypothesis-testing]
created: 2026-04-24
updated: 2026-04-26
---

# EEE 350 HW7 — Significance Testing & MMSE/LMSE Estimation

## TL;DR
Four problems spanning two topics: one significance test (fair-coin via CLT) and three MMSE/LMSE estimation problems (discrete joint PMF, continuous joint PDF, and an Erlang-Uniform pair where MMSE = LMSE). Plus five gotchas on CLT / standardization / variance scaling captured during the chat.

## Key takeaways
- **Significance testing recipe.** Under $H$, compute $(\mu_0, \sigma_0^2)$ of the test statistic; apply CLT + standardization; reject if $|(T - \mu_0)/\sigma_0| > z_{\alpha/2}$. For two-sided $\alpha = 0.05$, the magic number is $z =$ **1.96**.
- **LMSE from 5 numbers.** Linear MMSE needs only $E[X], E[Y], \text{Var}(X), \text{Var}(Y), \text{Cov}(X,Y)$. Every other detail of the joint distribution is irrelevant to the linear estimator.
- **LMSE vs MMSE.** LMSE is a 2-D projection onto $\text{span}\{1, X\}$; MMSE = $E[Y|X]$ uses the full conditional. LMSE = MMSE iff $E[Y|X]$ is affine — e.g. jointly Gaussian, or the HW7 Erlang/Uniform setup.
- **Naming conflict.** HW7 calls the linear version "LMSE"; the [[lms-estimation]] page (Wiley/MIT naming) calls it "LLS" and reserves "LMS" for the unrestricted $E[X|Y]$. Different names, same math. See the [[linear-mmse-estimation]] page's "Naming" section.
- **Standardization $\neq$ CLT.** Two separate operations. CLT makes things Gaussian; standardization rescales a Gaussian to be $N(0,1)$. Textbooks apply both in one breath — HW7's Gotcha #4 disentangles them.
- **$\text{Var}(cX) = c^2\cdot\text{Var}(X)$.** The squaring is why dividing $K$ by $\sigma_K = 5$ turns variance 25 into variance 1. See [[variance-scaling-rule]].

## Concepts introduced or reinforced

### New pages
- [[significance-test]] — decision rule for rejecting $H$ with budgeted false-alarm rate $\alpha$
- [[linear-mmse-estimation]] — the LMSE / LLS estimator $aX + b$, its formulas, and projection view
- [[standardization]] — the $Z = (X - \mu)/\sigma$ transformation
- [[variance-scaling-rule]] — $\text{Var}(cX) = c^2\cdot\text{Var}(X)$

### Reinforced
- [[central-limit-theorem]] — used to Normal-approximate Binomial$(100, 0.5)$
- [[lms-estimation]] — refreshed with a naming-clarity note for the HW7 convention
- [[prob-gotchas]] — five new entries from the chat
- [[standard-normal-table]] — the 1.96 / 0.975 entry
- [[iterated-expectations]] — tower property used in problem 12.2.6 (c)
- [[type-i-error]] — $\alpha$ as false-alarm rate

## Walkthrough

The full per-problem walkthrough is at [[eee-350-hw7-walkthrough]] — concept + step-by-step derivation for every one of the four problems, in the same `==highlight==` + callout-block format as [[eee-304-hw7-walkthrough]].

## Worked examples (each a full page)
- [[fair-coin-significance-test]] — 11.1.6, $n = 100$ flips, reject if $|K - 50| > 9.8$
- [[lmse-discrete-pmf]] — 12.2.3, $\hat Y_L(X) = (5/8)X - 1/16$
- [[lmse-continuous-pdf]] — 12.2.4, $\hat X_L(Y) = (5/9)Y$ on triangular support
- [[mmse-vs-lmse-erlang]] — 12.2.6, MMSE = LMSE for both directions (affine conditional means)

## Gotchas captured (added to [[prob-gotchas]])

1. **$\alpha$ is not the fraction of the 100 flips that reject.** A significance test treats the *whole 100-flip experiment* as one observation. $\alpha$ is the probability that one such experiment wrongly rejects $H$, as if we repeated the whole thing many times.
2. **CLT = shape theorem, not standardization.** CLT turns a sum into Gaussian with the sum's natural mean and variance. Getting $N(0,1)$ additionally requires the standardization step.
3. **Gaussian = Normal (terminology).** Just two names for the same distribution. The *standard* Normal $N(0,1)$ is one specific member.
4. **Three CLT scalings** (raw sum $N(n\mu, n\sigma^2)$, sample mean $N(\mu, \sigma^2/n)$, standardized $N(0,1)$) — pick whichever matches the problem.
5. **$\text{Var}(cX) = c^2\cdot\text{Var}(X)$.** Not $c$. Missing the square is the most common variance slip.

## Questions this source raised
- HW7 uses "LMSE" where the existing wiki uses "LLS" — reconciled by adding a naming note on both pages.
- The HW7's Mermaid concept map is reproduced conceptually in [[linear-mmse-estimation]]'s comparison table; Jayden may want to add a picture to the course page later.

## Formula cheat sheet

**Significance test (two-tailed, symmetric rejection):** under $H$, $T \sim N(\mu_0, \sigma_0^2)$ exactly or via CLT. Reject if $|T - \mu_0| > z_{\alpha/2}\cdot\sigma_0$, with $z_{0.025} = 1.96$.

**LMSE:**
$$\hat Y_L(X) = \mu_Y + \frac{\text{Cov}(X,Y)}{\text{Var}(X)}(X - \mu_X), \qquad e_L^* = \text{Var}(Y)(1 - \rho^2).$$

**MMSE:** $\hat Y_M(X) = E[Y | X]$. Always $\leq$ LMSE in MSE terms. Equality iff $E[Y|X]$ is affine in $X$.

**Tower shortcut:** $E[Y] = E[E[Y|X]], E[XY] = E[X\cdot E[Y|X]]$. Use when the conditional is simple (e.g. Uniform).

**Erlang$(k, \lambda)$:** $E[X] = k/\lambda$, $\text{Var}(X) = k/\lambda^2$. For $k = 2$: $E[X^2] = 6/\lambda^2$.

## Related
- [[eee-350]] — course page (this source is filed)
- [[inference-formulas]], [[asymptotic-formulas]] — related formula pages
- [[inference-set-01]] — existing practice set, can extend after this HW
