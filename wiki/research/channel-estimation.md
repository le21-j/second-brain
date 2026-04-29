---
title: Channel Estimation via Least Squares (Beacon-based)
type: concept
course: [[research]]
tags: [channel-estimation, least-squares, beacon, aircomp]
sources: [[paper-unregrettable-hpsr]], [[paper-aircomp-feel-demo]]
created: 2026-04-21
updated: 2026-04-26
---

# Channel Estimation via Least Squares

## In one line
Each ED listens to a known beacon from the ES, correlates against the reference, and uses least-squares to estimate the magnitude $|h_n|$ of its own channel — which is what the [[regretful-learning]] utility function needs.

## Example first
ES transmits a known pilot sequence $p = [p_1, \ldots, p_L]$ (e.g., Zadoff-Chu, length 64). ED $n$ receives:

$$r_n[i] = h_n \cdot p_i + w[i], \quad i = 1 \ldots L$$

Stacked: $r_n = h_n \cdot p + w$. LS estimator:

$$\hat{h}_n = (p^H p)^{-1} p^H r_n = (p^H r_n) / L \quad \text{(if } p \text{ is unit-norm per sample)}$$

$$|\hat{h}_n|^2 = |p^H r_n|^2 / L^2$$

Take the magnitude. Done. Variance scales as $\sigma^2/L$.

## Why LS (vs MMSE, ML)
- **LS** needs no channel prior — just the pilot. Unbiased.
- **MMSE** is better if you have a reliable channel covariance model, but adds complexity.
- **ML** requires knowing the noise distribution; for Gaussian noise ML $=$ LS.

For a one-shot magnitude estimate from a single beacon, **LS is the right default.** Good enough for HPSR's utility function, which uses $|h_n|$ via a logarithmic projection $g(|h_n|)$ — that projection is insensitive to small estimation errors.

## Where this fits in the pipeline
**[[system-pipeline]] Stage 1** — the ES transmits the first beacon, each ED runs LS, stores $|\hat{h}_n|$. Used locally for utility computation and also reported back to the ES in Stage 2 so the ES can compute the aggregate feedback sums.

## Practical considerations
- **Pilot choice:** Zadoff-Chu sequences have constant amplitude + ideal autocorrelation $\to$ good for LS with no noise amplification. Demo paper uses ZC-97 in CHEST field and Golay-32 for frame sync (see [[paper-aircomp-feel-demo]]).
- **Pilot-to-data ratio:** longer pilot $\to$ more accurate estimate but more overhead. Demo paper uses one OFDM symbol for CHEST.
- **Channel coherence:** estimate is only valid for the coherence time $T_c$. For 2.4 GHz indoor @ pedestrian speed, $T_c \approx 10$–$100$ ms — fine for one epoch.
- **Reciprocity assumption:** estimating the DL channel and assuming UL $\approx$ DL requires a TDD system with short turnaround vs coherence time. HPSR implicitly assumes this since it uses $|h_n|$ interchangeably for UL (AirComp transmission) and DL (beacon reception).

## Common mistakes
- **Using complex $\hat{h}_n$ when only magnitude is needed.** The regret-learning utility only cares about $|h_n|$. Phase info is wasted — and noisier to estimate anyway.
- **Ignoring noise floor.** If $|\hat{h}_n|^2$ is below $\sigma^2/L$ the estimate is dominated by noise. Should set a threshold and drop EDs below it (matches the user's Stage 2 dropout behavior).
- **Over-trusting LS in deep fade.** When $|h_n|$ is very small, $g(|h_n|) = 1/|\log|h_n||^\alpha$ is still well-behaved thanks to the log compression — so even noisy LS estimates of deep-fade users don't break utility computation catastrophically.

## Related
- [[aircomp-basics]]
- [[regretful-learning]] — consumer of $|h_n|$
- [[system-pipeline]] — Stage 1
- [[least-squares]] — the general estimation technique (EEE 350)
