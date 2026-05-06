---
title: "Tutor Session — 2026-05-06 (Live Turn — Lecture 2: MAP)"
type: tutor-session
date: 2026-05-06
tags:
  - tutor-session
  - tutor-live
  - eee-350
  - final-exam
  - map
  - bayesian-inference
created: 2026-05-06
updated: 2026-05-06
---

# Lecture 2 — Maximum A Posteriori (MAP)

> **Mode: LEARNING PHASE.** Direct explanation, no Socratic questions. Connects directly to Lecture 1 (Bayes + MLE) preserved in [[tutor-2026-05-06]] Q4. Marginal-vs-joint Gaussian gotcha (Q5) preserved in [[tutor-2026-05-06]].
>
> Anchor concept pages: [[map-detection]] (discrete $\theta$), [[map-estimation]] (continuous $\theta$). Source slides: [[slides-43.5-bayesian-inference]].
>
> > [!warning] **No EEE 350 HW problems on MAP exist in your `raw/`.** I checked `/Users/smallboi/Documents/second-brain/raw/homework/`: only EEE350_HW7 / HW7.pdf are there, and they cover significance testing + MMSE/LMSE — not MAP. The EEE 350 slides ([[slides-43.5-bayesian-inference]]) flag the **antipodal-signaling AWGN detector** as the canonical worked example, so I'm using that as Section 1, plus a Bernoulli-prior binary-channel problem as Section 3. **If you have a HW PDF with MAP problems somewhere else, drop the path and I'll redo this with the actual problem.**

---

## Section 0 — Connect back to Lecture 1

MAP builds on the Bayes refresher in Lecture 1 — same posterior, but instead of just *computing* the posterior, we now **pick the value of $\theta$ that maximizes it**. That single extra step is all "MAP" is. Everything else (likelihood, prior, posterior, the flip from $p(x \mid \theta)$ to $p(\theta \mid x)$) is identical to what you already saw.

Pictorially:

| | Lecture 1 (Bayes) | Lecture 2 (MAP) |
|---|---|---|
| Output | The full posterior $p(\theta \mid x)$ | A single $\hat\theta$ |
| Operation | Compute Bayes' rule | Bayes' rule, **then $\arg\max$** over $\theta$ |
| Used when | You want to report uncertainty | You have to commit to one decision |

---

## Section 1 — Worked example: antipodal signaling over AWGN (canonical EEE 350 MAP problem)

This is the example the [[slides-43.5-bayesian-inference|EEE 350 Bayesian-inference slides]] use. It's the **digital communications** flavor of MAP — and it's the most likely shape your final-exam MAP question will take.

### Problem statement

A binary symbol $\theta \in \{+1, -1\}$ is transmitted over a channel that adds Gaussian noise:

$$X = \theta + N, \qquad N \sim \mathcal{N}(0, \sigma^2)$$

Receiver sees $X$ (a real number). Priors are **not** equal:

$$P(\theta = +1) = \pi_0, \qquad P(\theta = -1) = \pi_1, \qquad \pi_0 + \pi_1 = 1$$

(Numbers for the worked case: $\sigma^2 = 1$, $\pi_0 = 0.7$, $\pi_1 = 0.3$, observed $X = 0.4$.)

**Find the MAP decision rule** and apply it to the observation.

### Step 1 — Identify the four pieces

| Piece | Symbol | Value here |
|---|---|---|
| Parameter (what we're estimating) | $\theta$ | $\in \{+1, -1\}$ — discrete, so this is **MAP detection** |
| Prior | $P(\theta)$ | $\pi_0 = 0.7$ for $+1$, $\pi_1 = 0.3$ for $-1$ |
| Likelihood | $p(x \mid \theta)$ | $\mathcal{N}(\theta, \sigma^2)$ — Gaussian centered at $\theta$ |
| Observation | $X = x$ | $x = 0.4$ |

> [!tip] Recognition cue
> The word "**prior**" or any explicit numerical $P(\theta)$ in the problem statement is your MAP signal. If priors are not given, you're doing MLE — not MAP.

### Step 2 — Write the posterior (unnormalized)

By Bayes' rule:

$$P(\theta \mid x) \propto p(x \mid \theta)\, P(\theta)$$

We don't need the normalizer $p(x)$ — it's the **same** for both $\theta = +1$ and $\theta = -1$, so it drops out of the $\arg\max$.

For each hypothesis:

$$P(+1 \mid x) \propto \frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{(x - 1)^2}{2\sigma^2}\right) \cdot \pi_0$$

$$P(-1 \mid x) \propto \frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{(x + 1)^2}{2\sigma^2}\right) \cdot \pi_1$$

### Step 3 — Form the MAP decision rule (likelihood ratio test)

Decide $\theta = +1$ if $P(+1 \mid x) > P(-1 \mid x)$, equivalently:

$$\frac{p(x \mid +1)}{p(x \mid -1)} \;\overset{+1}{\underset{-1}{\gtrless}}\; \frac{\pi_1}{\pi_0}$$

> [!warning] Ratio direction — easy to flip on the exam
> The **likelihood ratio** has $H_1$ (or $+1$) on top, but the **prior ratio threshold** has $\pi_1$ (the prior of the *other* hypothesis) on top. This crossover is structural — it comes from rearranging $p(x \mid +1)\pi_0 > p(x \mid -1)\pi_1$.

Plugging in the Gaussian likelihoods and taking $\log$ on both sides:

$$\log\frac{p(x \mid +1)}{p(x \mid -1)} = -\frac{(x-1)^2}{2\sigma^2} + \frac{(x+1)^2}{2\sigma^2} = \frac{(x+1)^2 - (x-1)^2}{2\sigma^2} = \frac{4x}{2\sigma^2} = \frac{2x}{\sigma^2}$$

So the rule becomes:

$$\frac{2x}{\sigma^2} \;\overset{+1}{\underset{-1}{\gtrless}}\; \log\frac{\pi_1}{\pi_0} \;\;\Longleftrightarrow\;\; x \;\overset{+1}{\underset{-1}{\gtrless}}\; \underbrace{\frac{\sigma^2}{2}\log\frac{\pi_1}{\pi_0}}_{\tau \text{ (threshold)}}$$

$$\boxed{\;\hat\theta_{\text{MAP}} = +1 \text{ if } x > \tau, \quad -1 \text{ otherwise}, \quad \tau = \frac{\sigma^2}{2}\log\frac{\pi_1}{\pi_0}\;}$$

### Step 4 — Plug in the numbers

With $\sigma^2 = 1$, $\pi_0 = 0.7$, $\pi_1 = 0.3$:

$$\tau = \frac{1}{2}\log\frac{0.3}{0.7} = \frac{1}{2}\log(0.4286) = \frac{1}{2}(-0.8473) \approx -0.424$$

Observation is $x = 0.4 > -0.424 = \tau$, so:

$$\boxed{\hat\theta_{\text{MAP}} = +1}$$

### Step 5 — Sanity-check the threshold direction

The prior favors $+1$ ($\pi_0 = 0.7 > \pi_1 = 0.3$), so the threshold should **shift toward the less-likely hypothesis** ($-1$ side, i.e., negative $x$). It did: $\tau \approx -0.424 < 0$. The receiver is now more willing to declare $+1$ even when $x$ is mildly negative — exactly because $+1$ was a priori more likely.

> [!example] Equal-prior special case
> If $\pi_0 = \pi_1 = 0.5$, then $\log(\pi_1/\pi_0) = \log 1 = 0$, so $\tau = 0$. The classic "**threshold at zero**" sign detector — and this is exactly the MLE / ML rule. **MAP $=$ MLE when priors are equal.**

---

## Section 2 — The framework (5 building blocks)

Every MAP problem decomposes into the same five blocks. Once you can name them on sight, MAP is solved.

### Block 1 — Posterior $\propto$ likelihood $\times$ prior

$$P(\theta \mid x) = \frac{p(x \mid \theta)\,P(\theta)}{p(x)} \;\propto\; p(x \mid \theta)\,P(\theta)$$

The denominator $p(x)$ does NOT depend on $\theta$, so for $\arg\max$ purposes you can drop it. Compute the unnormalized posterior; never bother computing $p(x)$ unless the problem asks for the actual probability.

### Block 2 — Argmax over $\theta$

$$\hat\theta_{\text{MAP}} = \arg\max_\theta P(\theta \mid x) = \arg\max_\theta \bigl[\,p(x \mid \theta)\,P(\theta)\,\bigr]$$

For **discrete** $\theta$ (hypotheses $H_0, H_1, \ldots$): compare the unnormalized posterior of each, pick the largest. This is **MAP detection**.

For **continuous** $\theta$ (real-valued unknown): take $\log$, differentiate, set to zero. This is **MAP estimation**.

### Block 3 — Binary form: likelihood ratio test

For binary hypotheses $H_0$ vs $H_1$, the MAP rule is **algebraically equivalent** to:

$$\Lambda(x) := \frac{p(x \mid H_1)}{p(x \mid H_0)} \;\overset{H_1}{\underset{H_0}{\gtrless}}\; \frac{P(H_0)}{P(H_1)}$$

Likelihood ratio on the left, prior ratio on the right, **flipped** (the threshold ratio has the priors of the *opposite* hypotheses to what's on top of the likelihood ratio). Take $\log$ to get the **log-likelihood ratio** form, which is usually easier when the likelihoods are exponentials/Gaussians.

### Block 4 — MAP vs MLE: the prior is the only difference

$$\hat\theta_{\text{MLE}} = \arg\max_\theta p(x \mid \theta) \qquad \hat\theta_{\text{MAP}} = \arg\max_\theta p(x \mid \theta)\,P(\theta)$$

When the prior is **uniform** (flat) over $\theta$, $P(\theta)$ is a constant in $\theta$ and drops out of the $\arg\max$. So **MLE = MAP under a flat prior**. The two estimators are the same machine; MLE is the special case where you have no prior information (or refuse to use it).

### Block 5 — Log-domain trick

Products of densities ($n$ Gaussians, $n$ Bernoullis) become unmanageable; sums are fine. Take $\log$ on both sides of the $\arg\max$:

$$\arg\max_\theta \bigl[\,p(x \mid \theta)\,P(\theta)\,\bigr] = \arg\max_\theta \bigl[\,\log p(x \mid \theta) + \log P(\theta)\,\bigr]$$

For Gaussian likelihoods this turns into a **quadratic in $\theta$** — solvable in closed form. For exponential likelihoods, into a sum. The $\arg\max$ location is preserved because $\log$ is monotone increasing.

---

## Section 3 — Second worked example: binary channel with Bernoulli prior (different angle)

Different problem shape — same five blocks. Shows the framework's reuse.

### Problem statement

A single bit $\theta \in \{0, 1\}$ is sent over a noisy channel. The channel **flips the bit with probability $p = 0.1$** (a binary symmetric channel). So:

$$P(X = 1 \mid \theta = 1) = 0.9, \quad P(X = 0 \mid \theta = 1) = 0.1$$
$$P(X = 1 \mid \theta = 0) = 0.1, \quad P(X = 0 \mid \theta = 0) = 0.9$$

The prior is biased: $P(\theta = 1) = 0.2$, $P(\theta = 0) = 0.8$ (the source rarely sends $1$).

**Receiver observes $X = 1$. What's the MAP decision?**

### Step 1 — Identify the four pieces

| Piece | Value |
|---|---|
| Parameter | $\theta \in \{0, 1\}$ — discrete, MAP detection |
| Prior | $P(\theta=1) = 0.2$, $P(\theta=0) = 0.8$ |
| Likelihood | $P(X \mid \theta)$ — bit-flip channel |
| Observation | $X = 1$ |

### Step 2 — Compute unnormalized posteriors

$$P(\theta = 1 \mid X = 1) \propto P(X=1 \mid \theta=1)\,P(\theta=1) = 0.9 \cdot 0.2 = 0.18$$

$$P(\theta = 0 \mid X = 1) \propto P(X=1 \mid \theta=0)\,P(\theta=0) = 0.1 \cdot 0.8 = 0.08$$

### Step 3 — Argmax

$0.18 > 0.08$, so:

$$\boxed{\hat\theta_{\text{MAP}} = 1}$$

### Step 4 — Compare to MLE (drop the prior)

MLE would just pick the $\theta$ that maximizes the likelihood:

$$P(X=1 \mid \theta=1) = 0.9, \qquad P(X=1 \mid \theta=0) = 0.1$$

$\hat\theta_{\text{MLE}} = 1$ trivially (also). Both estimators agree here because the likelihood evidence ($9{:}1$) overpowers the prior ratio ($1{:}4$ favoring $\theta = 0$).

> [!example] Same problem, weaker observation
> If the channel were noisier — say $p = 0.4$ flip prob — the likelihoods would be $P(X=1\mid\theta=1) = 0.6$ and $P(X=1\mid\theta=0) = 0.4$. Then:
> - MAP: $0.6 \cdot 0.2 = 0.12$ vs $0.4 \cdot 0.8 = 0.32$ $\to$ pick $\theta = 0$.
> - MLE: $0.6 > 0.4$ $\to$ pick $\theta = 1$.
>
> **They disagree.** This is when the prior earns its keep — when the data is weak enough that the prior tips the scale.

### Step 5 — Posterior form (if the problem asks)

To get the actual probability (not just the decision), normalize:

$$P(\theta = 1 \mid X = 1) = \frac{0.18}{0.18 + 0.08} = \frac{0.18}{0.26} \approx 0.692$$

So even after seeing $X = 1$, you're only ~69% sure the source sent $1$ — because the prior was so strongly against it. This is the **exact same Bayes' rule arithmetic from the Lecture 1 medical-test example** dressed up as a digital channel.

---

## Section 4 — Formal definition

### Generic form

$$\hat\theta_{\text{MAP}} = \arg\max_\theta P(\theta \mid x) = \arg\max_\theta \bigl[\,p(x \mid \theta)\,P(\theta)\,\bigr]$$

(Drop $p(x)$ since it's constant in $\theta$. For continuous $\theta$, swap $P$ for $p$ where appropriate.)

### Binary detection form (likelihood ratio test)

Decide $H_1$ over $H_0$ if:

$$\frac{p(x \mid H_1)}{p(x \mid H_0)} \;>\; \frac{P(H_0)}{P(H_1)}$$

> [!warning] **Ratio direction is the most-blown step on the exam.** Likelihood ratio numerator is $H_1$; threshold numerator is $P(H_0)$ — they are **flipped**. Re-derive from $p(x \mid H_1)P(H_1) > p(x \mid H_0)P(H_0)$ if you forget which is on top.

Equivalently in log form:

$$\log p(x \mid H_1) - \log p(x \mid H_0) \;>\; \log P(H_0) - \log P(H_1)$$

### Continuous estimation form

For continuous $\theta$ with prior density $p(\theta)$:

$$\hat\theta_{\text{MAP}} = \arg\max_\theta \bigl[\,\log p(x \mid \theta) + \log p(\theta)\,\bigr]$$

Differentiate, set to zero, solve. **Identical to MLE** plus the extra $+\log p(\theta)$ term.

---

## Section 5 — When to use it (recognition cues for the final)

MAP shows up on the EEE 350 final in three flavors:

1. **Signal detection over a noisy channel with known priors.** Words to look for: "transmitted symbol," "channel adds noise," "prior probability," "binary symmetric channel," "AWGN," "antipodal." This is your Section 1 problem shape.
2. **Classification with non-uniform class priors.** Words: "the prior probability of class $A$ is...," "given $P(\text{class}_i)$." Section 3 shape.
3. **Parameter estimation with a continuous prior.** Words: "$\theta$ has prior distribution $p(\theta)$," "Bayesian estimate," "posterior mode." Continuous-MAP form.

> [!tip] **The recognition trigger is the word "prior" in the problem statement.**
> - Problem says **"prior"** $\to$ MAP.
> - Problem says **"likelihood"** but no prior, or "estimate $\theta$ from data" with no prior $\to$ MLE.
> - Problem says **"$P(H_0) = P(H_1) = 0.5$"** or "**equally likely**" $\to$ MAP collapses to MLE; the prior ratio drops to 1.

---

## Section 6 — What to internalize vs memorize

You have a 2-page formula sheet. Use it.

| Memorize cold (recognition) | Look up on cheat sheet | Derive on the spot |
|---|---|---|
| **The recognition cue: "prior" in the problem $\to$ MAP** | The exact LRT form with ratio direction | The log-likelihood ratio for a Gaussian channel |
| **5-block framework** (posterior $\propto$ lik $\times$ prior; argmax; LRT; MAP$=$MLE w/ flat prior; log-trick) | Gaussian PDF, Bernoulli PMF | The threshold $\tau$ for an antipodal AWGN problem |
| **MAP $=$ MLE when priors are equal** | The Gaussian-Gaussian conjugate posterior weighted-average formula | Numerical answer once you have $\tau$ |

**Memorize NOTHING from MAP itself as a formula.** The $\arg\max$ rule and LRT direction are on your sheet. What you must recognize is the *structure* — the moment you spot a prior in the problem, your hand reaches for the MAP page of the cheat sheet.

---

## Section 7 — Gotchas (4 sharp ones)

1. **Likelihood-ratio direction.** $\Lambda = p(x \mid H_1)/p(x \mid H_0)$ on top has $H_1$; threshold $P(H_0)/P(H_1)$ on top has $H_0$. They are **flipped**. Most common exam slip.
2. **MAP collapses to MLE under equal priors.** Don't carry the prior ratio through pointlessly when $\pi_0 = \pi_1$. The $\log(\pi_1/\pi_0) = 0$ term just makes the algebra ugly. Spot the equal priors and zero out the threshold immediately.
3. **"Maximum a posteriori" maximizes the *posterior*, not the *likelihood*.** If you forget the prior, you're doing MLE. The whole point of MAP is that it includes $P(\theta)$.
4. **Continuous-$\theta$ MAP needs the $\log$-derivative trick.** Take $\log$ of $p(x \mid \theta)\,p(\theta)$, differentiate w.r.t. $\theta$, set to zero. This is the same calculus as MLE — but with an extra $+\log p(\theta)$ term contributing to the derivative. **If you drop the extra term, you've silently switched back to MLE.**

> [!example] Continuous MAP — Gaussian–Gaussian (preview)
> If $\theta \sim \mathcal{N}(\mu_0, \tau^2)$ and $X \mid \theta \sim \mathcal{N}(\theta, \sigma^2)$, the posterior is also Gaussian, and the MAP estimate is the **weighted average**:
> $$\hat\theta_{\text{MAP}} = \frac{\tau^2}{\sigma^2 + \tau^2}\,x + \frac{\sigma^2}{\sigma^2 + \tau^2}\,\mu_0$$
> Data dominates when $\sigma^2$ is small (low noise); prior dominates when $\tau^2$ is small (strong prior). Full derivation in [[map-estimation]].

---

## Section 8 — Cross-links

- [[map-detection]] — concept page for discrete-$\theta$ MAP (the binary-channel and antipodal-AWGN problems live here).
- [[map-estimation]] — concept page for continuous-$\theta$ MAP (Gaussian-Gaussian conjugate).
- [[maximum-likelihood-estimation]] (`[[mle]]` synonym) — the no-prior limit of MAP.
- [[bayesian-inference]] — the parent framework; MAP is one of three Bayesian estimators (MAP, LMS, posterior median).
- [[posterior-distribution]] / [[prior-distribution]] / [[likelihood-ratio-test]] — the supporting cast.
- [[significance-test]] — the *frequentist* cousin of detection (no priors, just $\alpha$ budget). Lecture 5.
- [[lms-estimation]] — the **mean** of the posterior (not the mode). Tutored next as Lecture 3 (LMSE).
- [[slides-43.5-bayesian-inference]] — source slides where antipodal-AWGN example originates.
- [[eee-350-hw7-walkthrough]] — your HW7 covers MMSE/LMSE (next lecture's territory), not MAP.

---

## Pause point — your turn

Read above at your pace. When ready, send back **one** of:

- **"continue to LMSE"** $\Rightarrow$ Lecture 3 starts. The joint-Gaussian assumption from the Q5 gotcha will become load-bearing for the $\hat X_{\text{LMSE}} = \hat X_{\text{MMSE}}$ identity.
- **"continue to significance"** $\Rightarrow$ skip ahead to Lecture 5 (frequentist hypothesis testing). MAP and significance are siblings — same structure, no priors in significance.
- **"re-explain X"** $\Rightarrow$ different angle on any section above (concrete numbers, code, derivation, analogy).
- **"give me a problem"** $\Rightarrow$ exit lecture mode for MAP; walkthrough on a fresh MAP problem. I'll generate an antipodal-AWGN problem with new numbers.
- **"got it / wrap"** $\Rightarrow$ closing recap appended to [[tutor-2026-05-06]] daily log; spaced revisit plan logged.

---

## Anchors

- Daily log: [[tutor-2026-05-06]] (Q4 = Bayes+MLE Lecture 1; Q5 = marginal-vs-joint Gaussian gotcha; Q6 = this MAP lecture, appended below).
- Course: [[eee-350]].
- Final-exam topic 6 — **statistical inference**. MAP is one of four blocks here (MAP, MLE, LMSE, significance test).
- Source slides: [[slides-43.5-bayesian-inference]] — antipodal-AWGN MAP detector originates here.
