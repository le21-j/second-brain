# Pattern Recognition and Machine Learning — Christopher Bishop

**Category:** Machine Learning (probabilistic, rigorous)
**Status:** paid book — not yet in repo (PDFs widely available via Microsoft Research page; the author has posted a free copy at https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/)
**Publisher:** Springer, 2006
**Author:** Christopher Bishop (Microsoft Research; Director, Microsoft Research AI4Science)
**Roadmap phase:** reference throughout, mined selectively

## Topic coverage — chapters that matter
- **Ch 1**: Decision theory, information theory, bias-variance
- **Ch 2**: Probability distributions (Gaussian, exponential family, conjugate priors)
- **Ch 3**: Linear regression — **Bayesian linear regression = MMSE channel estimator** (this is the single most important identity for a DSP applicant to internalize)
- **Ch 4**: Linear classification (discriminants, logistic regression, generative vs. discriminative)
- **Ch 6**: Kernel methods, Gaussian processes
- **Ch 8**: Graphical models — directly underlies iterative decoders (LDPC, turbo)
- **Ch 9**: Mixture models and EM
- **Ch 10**: Variational inference (the ML flavor of approximate inference that shows up in VAE)
- **Ch 11**: Sampling methods (MCMC, Gibbs)
- **Ch 13**: Sequential data — **HMMs and Kalman filters**; the Kalman filter section is the exact one that justifies the claim "Bayesian linear Gaussian state-space = Kalman filter"

## Why it's on the roadmap
> "Your most valuable reference... Kalman filtering is a linear-Gaussian state-space model (Bishop PRML Ch 13)."

For a DSP-background applicant, Bishop is the bridge between what you already know (LS, MMSE, Kalman, Wiener) and the ML reformulation of it. You do not read it cover to cover. You **reach for it by chapter** when a paper name-drops "ridge regression," "Gaussian process," or "EM" and you want the first-principles derivation.

## DSP ↔ ML identities to take from PRML
- Ridge regression = MMSE estimator with Gaussian prior. (Ch 3.)
- Kernel regression = Gaussian process regression. (Ch 6.)
- EM = ML with hidden variables = generalized expectation-maximization. (Ch 9.)
- Kalman filter = forward message-passing in a linear-Gaussian HMM. (Ch 13.)
- Sum-product / belief propagation = the loopy generalization of these messages. (Ch 8.)

## Related wiki pages
- [[python-ml-wireless]]
- [[murphy-pml-intro]] — modern replacement
- [[christopher-bishop]]
- [[simeone-ml-for-engineers]]
