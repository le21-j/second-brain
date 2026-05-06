---
title: Bivariate Gaussian
type: concept
course:
  - "[[eee-350]]"
tags: [gaussian, bivariate, joint-distribution]
sources:
  - "[[slides-38-covariance]]"
  - "[[slides-39-multivariate-vectors]]"
created: 2026-04-21
updated: 2026-05-06
---

# Bivariate Gaussian

## In one line
The joint distribution of two RVs parameterized by 5 numbers: $\mu_X$, $\mu_Y$, $\sigma_X$, $\sigma_Y$, and the correlation $\rho$.

## Example first
Heights and weights of adults approximate a bivariate Gaussian: $\mu_H = 170$ cm, $\mu_W = 70$ kg, $\sigma_H = 10$ cm, $\sigma_W = 15$ kg, $\rho \approx 0.75$. Density "mountain" is an ellipse tilted along the diagonal (because $\rho > 0$). Contours of equal density are ellipses whose tilt and aspect ratio are set by $\rho$ and the $\sigma$'s.

If $\rho = 0$ and $\sigma_H = \sigma_W$, the contours become circles. If $\rho = \pm 1$, the "ellipse" collapses to a line — the two variables are linearly dependent.

## The idea
A bivariate Gaussian is completely characterized by:
- means $(\mu_X, \mu_Y)$
- variances $(\sigma_X^2, \sigma_Y^2)$
- covariance or equivalently correlation ($\text{Cov}(X, Y) = \rho \cdot \sigma_X \cdot \sigma_Y$)

That's 5 parameters total. No higher moments add information.

## Formal PDF

$$f_{X,Y}(x, y) = \frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}} \exp\!\left[-\frac{1}{2(1-\rho^2)}\left(\frac{(x-\mu_X)^2}{\sigma_X^2} - 2\rho\frac{(x-\mu_X)(y-\mu_Y)}{\sigma_X\sigma_Y} + \frac{(y-\mu_Y)^2}{\sigma_Y^2}\right)\right]$$

Looks scary. Key things to read off:
- **Quadratic form in the exponent** (elliptical contours).
- Normalization $1/(2\pi \sigma_X \sigma_Y \sqrt{1-\rho^2})$ ensures integral $= 1$.
- When $\rho = 0$, the exponent separates into $f_X(x) \cdot f_Y(y)$ — independence.

## Key properties
- **Marginals are Gaussian:** $X \sim N(\mu_X, \sigma_X^2)$, $Y \sim N(\mu_Y, \sigma_Y^2)$.
- **Linear combinations are Gaussian:** $aX + bY \sim N(a\mu_X + b\mu_Y, a^2 \sigma_X^2 + b^2 \sigma_Y^2 + 2ab \cdot \text{Cov}(X, Y))$.
- **Uncorrelated $\Longleftrightarrow$ Independent.** Special to the Gaussian family. See [[independent-vs-uncorrelated]].
- **Conditional is Gaussian and linear:**
  $$E[Y | X = x] = \mu_Y + \rho\frac{\sigma_Y}{\sigma_X}(x - \mu_X)$$
  $$\text{Var}(Y | X = x) = \sigma_Y^2(1 - \rho^2)$$
  Note the conditional variance **doesn't depend on $x$**.

## Interpreting the conditional mean
- It's a **line** in $x$ — slope $\rho \cdot \sigma_Y / \sigma_X$, intercept $\mu_Y - \rho \cdot \sigma_Y \cdot \mu_X / \sigma_X$.
- The slope equals the [[linear-regression]] slope (not a coincidence — LMS estimator for Gaussians is exactly the regression line).
- The conditional variance $\sigma_Y^2 (1 - \rho^2)$ shrinks as $|\rho| \to 1$: knowing $X$ tells you a lot about $Y$.

## Geometry of contours
- Level sets $\{f(x, y) = c\}$ are ellipses.
- **Axes of the ellipse** are the eigenvectors of the covariance matrix:
  $$\Sigma = \begin{pmatrix}\sigma_X^2 & \rho\sigma_X\sigma_Y \\ \rho\sigma_X\sigma_Y & \sigma_Y^2\end{pmatrix}$$
- Tilt angle = angle of the larger eigenvector.

## Marginally Gaussian $\neq$ jointly Gaussian

**Both marginals being Gaussian is NOT enough to make $(X, Y)$ bivariate Gaussian.** Joint Gaussianity is strictly stronger; all the clean bivariate-Gaussian properties (linear conditional mean, constant conditional variance, uncorrelated $\Rightarrow$ independent, LMSE $=$ MMSE) require it.

**Canonical counterexample.** Let $X \sim \mathcal{N}(0, 1)$ and $Z$ be a fair sign coin ($P(Z = \pm 1) = 1/2$) with $Z \perp X$. Define $Y = ZX$. Then:

- $Y \sim \mathcal{N}(0, 1)$ (because $-X \stackrel{d}{=} X$ for symmetric Gaussian, so a half-half mix of $X$ and $-X$ is still $\mathcal{N}(0,1)$). **Both marginals standard Gaussian.**
- $E[XY] = E[ZX^2] = E[Z]E[X^2] = 0 \cdot 1 = 0$, so $\text{Cov}(X, Y) = 0$. **Uncorrelated.**
- The joint $(X, Y)$ is supported on $\{y = x\} \cup \{y = -x\}$ — two lines, measure zero in $\mathbb{R}^2$. **NOT bivariate Gaussian** (true bivariate Gaussian has elliptical contours filling the plane).
- $|Y| = |X|$ always: $X$ and $Y$ are wildly dependent, not independent.

So the pair has Gaussian marginals, zero covariance, but is neither independent nor jointly Gaussian.

**Exam tell.** "$X$ and $Y$ are both Gaussian" alone does NOT license bivariate-Gaussian formulas. Only "$(X, Y)$ is bivariate / jointly Gaussian" does.

**LMSE consequence.** The identity $\hat{X}_{\text{LMSE}} = \hat{X}_{\text{MMSE}} = E[X \mid Y]$ requires JOINT Gaussianity, not just marginal — see [[linear-mmse-estimation]].

See [[tutor-2026-05-06-live]] for full derivation; gotcha logged in [[prob-gotchas]].

## Common mistakes
- **$X$ and $Y$ marginal-Gaussian $\Rightarrow$ jointly Gaussian.** False. See "Marginally Gaussian $\neq$ jointly Gaussian" section above for the $Y = ZX$ counterexample.
- Plugging $\rho = \pm 1$ into the density formula — you get $0/0$; the distribution degenerates onto a line and doesn't have a density in 2D.
- Forgetting that the conditional **variance** is constant in $x$; people try to make it depend on $x$.

## Related
- [[multivariate-gaussian]] — generalization to $n$ dimensions
- [[correlation-coefficient]]
- [[covariance]]
- [[independent-vs-uncorrelated]]
- [[conditional-expectation]] — Gaussian case is the marquee example
- [[linear-regression]] — regression slope $= \rho \cdot \sigma_Y / \sigma_X$

## Practice
- [[prob-fundamentals-set-01]]
