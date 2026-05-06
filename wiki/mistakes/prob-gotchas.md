---
title: Probability & Statistics — Common Mistakes
type: mistake
course:
  - "[[eee-350]]"
tags: [mistakes, probability, statistics]
concept:
  - "[[covariance]]"
  - "[[bayesian-inference]]"
  - "[[central-limit-theorem]]"
created: 2026-04-21
updated: 2026-05-06
---

# Probability & Statistics — Common Mistakes

## Known gotchas (general — from lecture material + classical sources)

### Moments & dependence
- **Uncorrelated $\neq$ independent.** $\text{Cov} = 0$ doesn't imply independence (except for jointly Gaussian). Classic counter-example: $X \sim \text{Uniform}(-1, 1)$, $Y = X^2$. See [[independent-vs-uncorrelated]].
- **Marginally Gaussian $\neq$ jointly Gaussian.** Two RVs can both be Gaussian on the margin but have a non-Gaussian joint distribution.
- **Variance of sum $\neq$ sum of variances** when there's covariance. Missing the $2\cdot\text{Cov}$ term gives wrong answers.
- **$\rho$ measures LINEAR dependence only.** Non-linear relationships (e.g. $y = x^2$) can have $\rho \approx 0$ while $Y$ is determined by $X$.

### Conditional expectation
- **$E[X \mid Y]$ is a random variable**, not a number. $E[X \mid Y = y]$ for specific $y$ is a number.
- **Forgetting iterated expectations.** When a problem has two stages of randomness, condition on the inner RV first — often dramatically simplifies.
- **Law of total variance has TWO terms.** $\text{Var}(X) = E[\text{Var}(X \mid Y)] + \text{Var}(E[X \mid Y])$. Missing the second (or first) term is common.
- **Random sum variance has two terms:** $E[N]\cdot\sigma^2 + \mu^2\cdot\text{Var}(N)$. Forgetting the second term gives a wrong answer.

### Asymptotic theorems
- **Gambler's Fallacy.** WLLN is about averages, NOT short-run compensation. 5 heads in a row doesn't make tails "due". See [[gamblers-fallacy]].
- **Confusing WLLN with CLT.** WLLN: $\bar X_n \to \mu$ (a constant). CLT: $(\bar X_n - \mu)\sqrt{n} \to N(0, \sigma^2)$ (a distribution). Different scalings, different conclusions.
- **Using CLT on very small $n$ or very skewed data.** The approximation can be poor.
- **Forgetting continuity correction** when approximating a discrete distribution by Gaussian via CLT. Adds 0.5 to the boundary.
- **Chebyshev is always loose** but universal — don't expect it to be tight for well-behaved distributions.

### Inference (Bayesian & classical)
- **Confusing $p(x \mid \theta)$ with $p(\theta \mid x)$.** Likelihood vs. posterior. Related by Bayes' rule but different objects.
- **MAP vs LMS:** MAP = posterior mode (minimizes 0–1 loss). LMS = posterior mean (minimizes MSE). Different for skewed posteriors; coincide for symmetric (like Gaussian).
- **MLE not always unbiased.** Classic example: MLE of Gaussian variance uses $1/n$ $\to$ biased. Use $1/(n-1)$ for unbiased sample variance.
- **Confidence intervals are NOT Bayesian credible intervals.** "95% CI contains $\mu$" is a statement about the *procedure*, not about a specific realized interval.
- **$\alpha$ is NOT $P(H_0 \text{ is true given rejection})$.** $\alpha = P(\text{reject } H_0 \mid H_0 \text{ true})$. Reversed conditional.
- **"Trials" inside one experiment vs repetitions of the experiment.** For the 100-flip significance test, $\alpha = 0.05$ refers to repeating the whole 100-flip experiment, not to the 100 flips themselves. See [[significance-test]].
- **LMSE $\neq$ LMS in naming.** HW7 uses LMSE (Linear MMSE, i.e. $aX + b$). The Wiley/MIT tradition uses LMS for the unrestricted MMSE $= E[X \mid Y]$ and LLS for the linear version. Same math, different abbreviations. See [[linear-mmse-estimation]] § Naming.
- **Forgetting that LMSE uses only 5 numbers.** $E[X]$, $E[Y]$, $\text{Var}(X)$, $\text{Var}(Y)$, $\text{Cov}(X,Y)$. If you find yourself computing the whole joint distribution for a linear-MSE question, step back.

### CLT / standardization / variance scaling
- **CLT is not standardization.** CLT is a shape theorem — the sum becomes Gaussian with its natural mean and variance ($N(n\mu, n\sigma^2)$ or $N(\mu, \sigma^2/n)$). Standardization is the rescaling step $(X - \mu)/\sigma$ that makes a Gaussian into $N(0,1)$. Don't conflate the two. See [[standardization]].
- **Three scalings of CLT.** Raw sum $N(n\mu, n\sigma^2)$, sample mean $N(\mu, \sigma^2/n)$, standardized $N(0,1)$. Only the standardized form gives you a z-table lookup. Pick the form that matches the problem.
- **Gaussian and Normal are the same thing.** Two names, one distribution. Standard Normal $N(0,1)$ is the specific member.
- **$\text{Var}(cX) = c^2\cdot\text{Var}(X)$, not $c\cdot\text{Var}(X)$.** Variance scales with the **square** of the constant; std dev scales linearly. Missing the square is the most common variance slip. See [[variance-scaling-rule]].
- **$\sigma^2$ in the standardization denominator is engineered.** Dividing by $\sigma$ (not some other constant) is exactly what makes $\text{Var}(Z) = 1$. It's not a guess.

### Regression
- **Extrapolation.** Linear fit in one range doesn't necessarily hold outside it.
- **Correlation $\neq$ causation.** Strong $\rho$ doesn't imply one causes the other.
- **Heteroskedasticity.** LS assumes constant noise variance. If it varies, standard errors are wrong.
- **Outliers.** Squared loss is sensitive to extreme points. Consider robust regression.

### Descriptive stats
- **Mean sensitive to outliers, median not.** For skewed data (income, waiting times), median is often more informative.
- **Using mode for continuous data** — ill-defined without binning.

### Stochastic processes
- **"Poisson" vs "Poisson process".** A distribution vs a process with that distribution for counts.
- **Markov property vs independence.** Markov chains have dependence — limited to one-step memory.
- **Stationarity is an idealization.** Real signals are usually only locally stationary (hence STFT).

## Jayden's personal log

_(Log dated entries here as you miss practice problems or catch yourself on a slip. The more specific, the more useful. Pattern > feeling.)_

- `2026-05-06` — *Final-exam diagnostic, Q1: said "$\text{Cov} = 0$ means fully dependent."* Right answer was **uncorrelated** (no linear comovement); independence $\Rightarrow \text{Cov} = 0$, **never the reverse** except for jointly Gaussian. Counter-example to remember: $X \sim \text{Uniform}(-1,1)$, $Y = X^2$ — $Y$ is a **deterministic** function of $X$ yet $\text{Cov}(X,Y) = 0$. Pattern: "covariance = 0" is a statement about a **linear** trend, nothing more.
- `2026-05-06` — *Final-exam diagnostic, Q2: tried to split $\text{Var}(X+Y)$ as $\text{Var}(X) + \text{Var}(Y)$ when $X, Y$ correlated.* Right answer was $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X,Y)$. Pattern: the cross term is **the whole reason** the formula isn't trivial — drop it only when independence is **stated**, not assumed. Sanity check: $\text{Var}(X+X) = 4\text{Var}(X)$, not $2\text{Var}(X)$, exposes the missing $2\,\text{Cov}$.
- `2026-05-06` — *Final-exam diagnostic, Q3: marked "$E[X \mid Y]$ is a number" as TRUE.* Right answer is **FALSE** — $E[X \mid Y]$ is a **random variable** (a function of $Y$); $E[X \mid Y = y]$ for a specific $y$ is a number. Pattern: capital $Y$ in the conditioning slot $\Rightarrow$ random variable; lowercase $y$ $\Rightarrow$ number. The tower rule $E[E[X \mid Y]] = E[X]$ only makes sense if the inner object is a random variable — that's the tell.
- `2026-05-06` — *Marginally Gaussian doesn't imply jointly Gaussian.* Right answer: marginal Gaussian + joint Gaussian are different conditions; "both marginals Gaussian" is necessary but **not sufficient** for the pair to be bivariate Gaussian. Pattern to remember: bivariate Gaussian needs joint Gaussianity (covariance-matrix density on $\mathbb{R}^2$), not just two Gaussian marginals. Canonical counterexample: $X \sim \mathcal{N}(0,1)$, $Z = \pm 1$ fair coin independent of $X$, $Y = ZX$. Both marginals are $\mathcal{N}(0,1)$ and $\text{Cov}(X,Y) = E[Z]E[X^2] = 0$, but the joint is supported on the two lines $y = \pm x$ — NOT bivariate Gaussian, and $X, Y$ are dependent ($|Y| = |X|$). **Load-bearing consequence:** LMSE $=$ MMSE only under JOINT Gaussianity, not marginal.
