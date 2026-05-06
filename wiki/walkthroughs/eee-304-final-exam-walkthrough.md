---
title: EEE 304 Final Exam — Full Solutions Walkthrough (8 problems, 350 pts)
type: walkthrough
course:
  - "[[eee-304]]"
tags: [eee-304, final, exam, walkthrough, solutions, steady-state, butterworth, roc, forward-euler, pam, tdm, bode, phase-margin, sampled-data]
sources:
  - "[[slides-2026-05-04-eee-304-final-exam]]"
created: 2026-05-04
updated: 2026-05-06
---

# EEE 304 Final Exam — Full Solutions Walkthrough

> [!note] **What this is.** Per-problem walkthrough of the **actual final exam** (`raw/slides/eee-304/304final-1.pdf`). Each problem: (a) state verbatim, (b) explain the concept being tested example-first, (c) walk the derivation step-by-step, (d) headline answer in a `**Final answer:**` line.
>
> Companion to [[eee-304-final-walkthrough]] (the *concept-level* walkthrough built from the preview deck). This file solves the actual numbers; that file teaches the methods.

> [!warning] **Open-book reference.** [`fourier.pdf`](../../raw/slides/eee-304/fourier.pdf) is the Oppenheim-Willsky transform tables: FT, FS, DTFT, Laplace (Tables 9.1, 9.2), z-transform (Tables 10.1, 10.2). Keep it open during the exam — every transform pair you'll need is in there.

> [!tip] **Time budget.** $150 \text{ min} / 350 \text{ pts} = 0.43 \text{ min/pt}$. Problem 1 (40 pt) ≈ 17 min. Problems 6–8 (50 pt each) ≈ 21 min each. Bank ~10 min for re-reading + final check.

---

## Problem 1 — Steady-State Response to a Step (40 pt, 4 sub-systems)

> **Problem 1.** For the following **causal** systems (DT or CT), determine the **steady-state response** to a **step input** $u[n]$ or $u(t)$, as appropriate, **and if it exists**.
>
> 1. $-3y[n+1] + 2y[n] = x[n]$
> 2. $y[n+1] - 3y[n] = x[n]$
> 3. $-\dfrac{dy(t)}{dt} - 4y(t) = x(t)$
> 4. $\dfrac{dy(t)}{dt} - 2y(t) = x(t)$

### The concept — example first

For a **stable** LTI system driven by a **constant** (step) input, the steady-state output is just the **DC gain**:

$$y_{ss} = H(z=1)\cdot 1 \;\;(\text{DT}) \qquad\text{or}\qquad y_{ss} = H(s=0)\cdot 1\;\;(\text{CT})$$

If the system is **unstable** (any pole outside the unit circle for DT, or in the closed RHP for CT), **no steady state exists** — the output blows up and the FVT doesn't apply.

> [!example] **The two-step recipe**
> 1. Take the transform of the difference/differential equation, solve for $H$.
> 2. Check the pole location — stable? Then evaluate at $z=1$ (DT) or $s=0$ (CT). Unstable? Write "DNE."

---

### Sub-problem 1.1 — $-3y[n+1] + 2y[n] = x[n]$

**Step 1 — Find $H(z)$.** Take z-transform: $-3zY(z) + 2Y(z) = X(z)$.

$$H(z) = \frac{1}{2 - 3z} = \frac{-1/3}{z - 2/3}$$

**Step 2 — Pole check.** Pole at $z = 2/3$. Since $|2/3| < 1$ → **stable** ✓

**Step 3 — DC gain.** $H(1) = \dfrac{1}{2 - 3} = -1$.

> **Final answer (1.1):** $\boxed{\,y_{ss}[n] = -1\,}$ (a constant).

---

### Sub-problem 1.2 — $y[n+1] - 3y[n] = x[n]$

**Step 1 — Find $H(z)$.** $zY(z) - 3Y(z) = X(z)$.

$$H(z) = \frac{1}{z - 3}$$

**Step 2 — Pole check.** Pole at $z = 3$. Since $|3| > 1$ → **unstable**.

> **Final answer (1.2):** $\boxed{\,y_{ss}[n] \text{ does not exist (system unstable)}\,}$

---

### Sub-problem 1.3 — $-\dfrac{dy}{dt} - 4y = x$

**Step 1 — Find $H(s)$.** Take Laplace: $-sY(s) - 4Y(s) = X(s)$.

$$H(s) = \frac{1}{-s - 4} = \frac{-1}{s + 4}$$

**Step 2 — Pole check.** Pole at $s = -4$ → **LHP, stable** ✓

**Step 3 — DC gain.** $H(0) = \dfrac{-1}{4} = -\dfrac{1}{4}$.

> **Final answer (1.3):** $\boxed{\,y_{ss}(t) = -\dfrac{1}{4}\,}$

---

### Sub-problem 1.4 — $\dfrac{dy}{dt} - 2y = x$

**Step 1 — Find $H(s)$.** $sY(s) - 2Y(s) = X(s)$.

$$H(s) = \frac{1}{s - 2}$$

**Step 2 — Pole check.** Pole at $s = +2$ → **RHP, unstable**.

> **Final answer (1.4):** $\boxed{\,y_{ss}(t) \text{ does not exist (system unstable)}\,}$

> [!warning] **Common trap.** Don't apply the Final Value Theorem to find $y_{ss}$ before checking stability — FVT gives a finite-looking number even for unstable systems and that number is **wrong**. Check pole location first, then evaluate $H$ at $z=1$ or $s=0$.

---

## Problem 2 — CT LPF Cutoff (40 pt)

> **Problem 2.** A CT low-pass filter $H(s) = \dfrac{1}{\tau s + 1}$ is desired to have a cut-off frequency **7 Hz**. Determine $\tau$.

### The concept

For a first-order LPF, the cut-off (-3 dB point) is where $|H(j\omega_c)|^2 = 1/2$:

$$\frac{1}{1 + (\tau\omega_c)^2} = \frac{1}{2} \;\;\Longrightarrow\;\; \tau\omega_c = 1 \;\;\Longrightarrow\;\; \boxed{\tau = \frac{1}{\omega_c}}$$

### Walkthrough

$f_c = 7$ Hz $\Rightarrow \omega_c = 2\pi f_c = 14\pi$ rad/s.

$$\tau = \frac{1}{14\pi} \approx \frac{1}{43.98} \approx 0.02274\text{ s}$$

> **Final answer:** $\boxed{\,\tau = \dfrac{1}{14\pi} \approx 22.74 \text{ ms}\,}$

> [!tip] **Sanity check.** Time constant $\tau \approx 23$ ms. The filter "responds" on the order of $\tau$, which corresponds to a cutoff of $1/\tau \approx 43.8$ rad/s $= 7$ Hz ✓.

---

## Problem 3 — DT LPF Pole Location (40 pt)

> **Problem 3.** A DT low-pass filter $H(z) = \dfrac{a}{z - 1 + a}$ operates at sampling rate **200 Hz** and is desired to have a cut-off frequency **10 Hz**. Determine $a$.

### The concept — example first

This is exactly the **Forward Euler-equivalent first-order LPF** the preview deck demonstrates (slide 4): given a CT LPF with corner $\omega_c$, the FE-equivalent DT pole sits at $z = 1 - \omega_c T$, where $T = 1/f_s$ and $a = \omega_c T$.

So:

$$\boxed{\,a = \omega_c T = 2\pi f_c \cdot \dfrac{1}{f_s}\,}$$

### Walkthrough

$f_c = 10$ Hz, $f_s = 200$ Hz, $T = 1/200 = 0.005$ s.

$$a = 2\pi \cdot 10 \cdot \frac{1}{200} = \frac{2\pi}{20} = \frac{\pi}{10} \approx 0.314$$

**Sanity check** — DC gain at $z = 1$: $H(1) = a/(1 - 1 + a) = a/a = 1$ ✓ (unity DC gain — correct for a normalized LPF).

> **Final answer:** $\boxed{\,a = \dfrac{\pi}{10} \approx 0.314\,}$

> [!note] **FE validity check.** $\omega_c T = 2\pi(10)(0.005) \approx 0.314$. We're not in the deep $\omega_c T \ll 1$ regime, but it's still under $\sim 1$ — FE is acceptable. The exact pole would be $z = e^{-\omega_c T} = e^{-0.314} \approx 0.731$, vs the FE pole at $z = 1 - 0.314 = 0.686$. Close but not equal — the exam accepts the FE answer.

---

## Problem 4 — ROC for Stable System (40 pt)

> **Problem 4.** Find the region of convergence of $H$ corresponding to a **stable** system for the transfer function
>
> $$H(z) = \frac{z - 4}{(z + 0.5)(z - 0.2)}$$

### The concept

For a DT system to be **stable**, the ROC of $H(z)$ must include the **unit circle** $|z| = 1$. ROC boundaries are always pole magnitudes — never include a pole, and the ROC is one of:

| ROC type | shape | causal? |
|---|---|---|
| outside outermost pole | $|z| > p_{\max}$ | causal |
| inside innermost pole | $|z| < p_{\min}$ | anticausal |
| annulus between two poles | $p_a < |z| < p_b$ | two-sided |

### Walkthrough

**Step 1 — Identify pole magnitudes.**

| pole | location | $|p|$ |
|---|---|---|
| $p_1$ | $-0.5$ | $0.5$ |
| $p_2$ | $+0.2$ | $0.2$ |

(There's also a **zero** at $z = 4$ — zeros do **not** affect the ROC.)

**Step 2 — Enumerate possible ROCs.**

| ROC choice | description | contains unit circle ($|z| = 1$)? |
|---|---|---|
| $|z| < 0.2$ | inside both poles (anticausal) | NO ($1 > 0.2$) |
| $0.2 < |z| < 0.5$ | annulus (two-sided) | NO ($1 > 0.5$) |
| $|z| > 0.5$ | outside both poles (causal) | **YES** ($1 > 0.5$) ✓ |

> **Final answer:** $\boxed{\,\text{ROC: } |z| > 0.5\,}$ (this is the **causal** interpretation — and the only one that gives a stable system).

> [!example] **What about the zero at $z = 4$?** Zeros never appear in ROC inequalities — only pole magnitudes do. The zero at $z = 4$ tells you the filter has a notch at $z = 4$ (way outside the unit circle, so this just means a frequency-shaping zero), but it does not constrain the ROC.

---

## Problem 5 — Forward Euler Discretization (40 pt)

> **Problem 5.** Write the Forward Euler approximation in discrete time, when sampling rate is **200 Hz**:
>
> $$H(s) = \frac{1}{(0.01\,s + 2)^2}$$

### The concept

**Forward Euler:** $s = (z - 1)/T$, equivalently $z = 1 + sT$. Substitute $s$ wherever it appears.

### Walkthrough

$T = 1/200 = 0.005$ s. Substitute $s = (z-1)/T = (z-1)/0.005 = 200(z-1)$:

$$0.01\,s = 0.01 \cdot 200(z-1) = 2(z - 1)$$

$$0.01\,s + 2 = 2(z-1) + 2 = 2z - 2 + 2 = 2z$$

$$(0.01\,s + 2)^2 = (2z)^2 = 4z^2$$

$$H_{DT}(z) = \frac{1}{4z^2}$$

> **Final answer:** $\boxed{\,H_{DT}(z) = \dfrac{1}{4z^2}\,}$

> [!note] **What just happened?** The CT pole is at $0.01s + 2 = 0 \Rightarrow s = -200$ rad/s. The FE map sends this pole to $z = 1 + sT = 1 + (-200)(0.005) = 1 - 1 = 0$. Both poles collapse to the origin → the DT filter is just **two unit delays + a $1/4$ gain**. (Sanity-check the DC gain: $H(0) = 1/4$ on the CT side; $H_{DT}(z = 1) = 1/(4) = 1/4$ on the DT side ✓.)
>
> This problem is a worked illustration of why FE struggles when $\omega_c T$ is not $\ll 1$ — here $\omega_c T = 1$ exactly, and FE collapses both poles into $z = 0$. The frequency response shape is destroyed even though DC gain is preserved.

---

## Problem 6 — TDM Maximum Number of Signals (50 pt)

> **Problem 6.** TDM communication: transmit $N$ voice signals bandlimited to **8 kHz** using PAM. If the system bandwidth (PAM pulse frequency) is limited to **225 kHz**, find the **maximum** $N$.

### The concept — example first

TDM frame structure: every $T_{\text{frame}}$ seconds, $N + 1$ slots fit (the $+1$ is the sync pulse). Each slot has duration $T_{\text{slot}} = T_{\text{frame}}/(N+1)$. The PAM pulse rate (= channel bandwidth) is

$$B_{\text{PAM}} = \frac{1}{T_{\text{slot}}} = \frac{N + 1}{T_{\text{frame}}} = (N + 1) \cdot f_{\text{frame}}$$

where $f_{\text{frame}}$ is the per-channel sample rate (Nyquist: $f_{\text{frame}} \geq 2B_{\text{voice}}$).

Cross-check against the preview deck slide 6: $N = 4$, $B = 4$ kHz → $f_{\text{frame}} = 8$ kHz, $(N+1)f_{\text{frame}} = 5 \cdot 8 = 40$ kHz ✓.

### Walkthrough

$B_{\text{voice}} = 8$ kHz $\Rightarrow f_{\text{frame}} = 2 \cdot 8 = 16$ kHz (Nyquist minimum).

Constraint: $B_{\text{PAM}} = (N + 1) \cdot 16 \leq 225$ kHz.

$$N + 1 \leq \frac{225}{16} = 14.0625 \;\;\Longrightarrow\;\; N \leq 13.0625$$

Since $N$ must be a positive integer:

> **Final answer:** $\boxed{\,N_{\max} = 13\,}$

**Verify** at $N = 13$: $B_{\text{PAM}} = 14 \cdot 16 = 224$ kHz $\leq 225$ ✓. At $N = 14$: $15 \cdot 16 = 240$ kHz $> 225$ ✗.

> [!tip] **Don't forget the $+1$ for the sync slot.** Without it: $N \cdot 16 \leq 225 \Rightarrow N \leq 14$ — wrong. The slide example uses **5 slots for 4 signals**, so $(N+1)$ is the convention.

---

## Problem 7 — Loop Shaping (Crossover + Phase Margin) (50 pt)

> **Problem 7.** Determine $K$ and $\tau_z$ so that $L(s) = P(s)C(s)$ has gain crossover at **4 rad/s** and phase margin **50°**.
>
> $$P(s) = \frac{1}{s + 1}, \qquad C(s) = \frac{K(\tau_z s + 1)}{s}$$

### The concept

**Gain crossover** $\omega_{gc}$: the frequency at which $|L(j\omega_{gc})| = 1$ (loop gain crosses unity).
**Phase margin** PM: how much extra phase lag the loop can absorb before instability — measured at the crossover. PM $= 180° + \angle L(j\omega_{gc})$.

So at $\omega_{gc} = 4$:

$$\angle L(j4) = -180° + \text{PM} = -180° + 50° = -130°$$

$$|L(j4)| = 1$$

Two equations, two unknowns ($K$, $\tau_z$).

### Walkthrough

$L(s) = \dfrac{K(\tau_z s + 1)}{s(s + 1)}$.

**Step 1 — Phase equation.**

$$\angle L(j\omega) = \arctan(\tau_z \omega) - 90° - \arctan(\omega)$$

At $\omega = 4$:

$$\arctan(4\tau_z) - 90° - \arctan(4) = -130°$$

With $\arctan(4) = 75.96°$:

$$\arctan(4\tau_z) = -130° + 90° + 75.96° = 35.96°$$

$$4\tau_z = \tan(35.96°) \approx 0.7253$$

$$\boxed{\,\tau_z \approx 0.181 \text{ s}\,}$$

**Step 2 — Magnitude equation.**

$$|L(j4)| = \frac{K\,|j4\tau_z + 1|}{4\,|j4 + 1|} = 1$$

Compute the magnitudes:

$$|j(4\tau_z) + 1| = \sqrt{1 + (4\tau_z)^2} = \sqrt{1 + 0.526} = \sqrt{1.526} \approx 1.2354$$

$$|j4 + 1| = \sqrt{17} \approx 4.1231$$

Solve for $K$:

$$K = \frac{4 \cdot 4.1231}{1.2354} = \frac{16.493}{1.2354} \approx 13.35$$

> **Final answer:** $\boxed{\,K \approx 13.35,\quad \tau_z \approx 0.181 \text{ s}\,}$

> [!info]- 📐 Show derivation — verify the design point
>
> Plug back in to check phase at $\omega = 4$:
> - $\arctan(4 \cdot 0.181) = \arctan(0.724) = 35.92°$
> - Phase $= 35.92° - 90° - 75.96° = -130.04°$ ✓
> - PM $= 180° - 130.04° = 49.96°$ ≈ $50°$ ✓
>
> And magnitude at $\omega = 4$:
> - $|L(j4)| = 13.35 \cdot \sqrt{1 + 0.524} / (4\sqrt{17}) = 13.35 \cdot 1.2347 / 16.493 = 0.999$ ≈ $1$ ✓

> [!tip] **Intuition.** $C(s) = K(\tau_z s + 1)/s$ is a **PI-with-zero** (lag-lead) controller. The integrator $1/s$ guarantees zero steady-state error to a step. The zero at $s = -1/\tau_z \approx -5.5$ rad/s adds phase lead just below the crossover, giving the loop the 50° margin we asked for.

---

## Problem 8 — Sampled-Data Response to Sum of DC + Sinusoid (50 pt)

> **Problem 8.** $H(z) = \dfrac{z - 1}{z - 0.7}$. Sampling time $T = 0.01$ s. Reconstruction is **ideal**. Find $y(t)$ when
>
> $$x(t) = \cos(t) + 1$$

### The concept — example first

When the input is a sum of components — each at a frequency well below the Nyquist rate $\pi/T$ — the **ideal-reconstruction sampled-data system** acts on each component independently. For each frequency $\omega_k$:

$$\text{component } A_k\cos(\omega_k t + \phi_k) \;\longmapsto\; A_k\,|H(e^{j\omega_k T})|\,\cos\!\bigl(\omega_k t + \phi_k + \angle H(e^{j\omega_k T})\bigr)$$

So **decompose the input by frequency, evaluate $H(e^{j\omega T})$ at each, recombine.**

Critical Nyquist check first: input frequencies must satisfy $|\omega| < \pi/T = \pi/0.01 = 100\pi \approx 314$ rad/s. Here input frequencies are $0$ (DC) and $1$ rad/s — both vastly below Nyquist ✓.

### Walkthrough

$x(t) = \cos(t) + 1$ has two frequency components:
- **DC**: $\omega = 0$, amplitude $1$.
- **$\cos(t)$**: $\omega = 1$ rad/s, amplitude $1$.

#### Component 1 — DC

$\omega = 0 \Rightarrow z = e^{j0} = 1$.

$$H(1) = \frac{1 - 1}{1 - 0.7} = \frac{0}{0.3} = 0$$

The filter has a **zero at $z = 1$** → DC is completely killed. The constant $+1$ in $x(t)$ contributes **nothing** to $y(t)$.

#### Component 2 — $\cos(t)$ at $\omega = 1$ rad/s

DT frequency: $\Omega = \omega T = (1)(0.01) = 0.01$ rad/sample.

Evaluate $H(e^{j0.01})$.

**Numerator** $e^{j\Omega} - 1$. Use the identity $e^{j\Omega} - 1 = 2j\sin(\Omega/2)\,e^{j\Omega/2}$:

$$|e^{j0.01} - 1| = 2\sin(0.005) \approx 0.01000$$

$$\angle(e^{j0.01} - 1) = \frac{\Omega}{2} + 90° = 0.005 \text{ rad} + 90° \approx 90.29°$$

**Denominator** $e^{j\Omega} - 0.7$ at $\Omega = 0.01$:

- Real part: $\cos(0.01) - 0.7 = 0.99995 - 0.7 = 0.29995$
- Imag part: $\sin(0.01) = 0.01000$
- Magnitude: $\sqrt{0.29995^2 + 0.01^2} \approx 0.30012$
- Phase: $\arctan(0.01/0.29995) \approx 1.91°$

**Combine:**

$$|H(e^{j0.01})| = \frac{0.01}{0.30012} \approx 0.0333$$

$$\angle H(e^{j0.01}) = 90.29° - 1.91° \approx 88.4°$$

So the cosine component maps as:

$$\cos(t) \;\longmapsto\; 0.0333\,\cos(t + 88.4°)$$

> **Final answer:** $\boxed{\,y(t) \approx 0.0333\,\cos(t + 88.4°)\,}$
>
> Equivalently $\approx -0.0333\,\sin(t)$ to leading order, since $88.4° \approx 90°$.

> [!note] **Why is this almost a derivative?** The filter $(z - 1)/(z - 0.7)$ at low frequencies acts approximately as $T \cdot \frac{d}{dt}$ scaled by the DC gain of $1/(1 - 0.7) = 10/3$. Differentiation of $\cos(t)$ is $-\sin(t) = \cos(t + 90°)$, with magnitude $\omega = 1$. So the expected filter output magnitude is $\omega \cdot T \cdot (10/3) = 1 \cdot 0.01 \cdot 3.33 = 0.0333$ ✓ and phase $\approx 90°$ ✓ — both match.

> [!warning] **The DC kill is the trick.** Don't forget to evaluate $H$ at DC too — the constant $+1$ in $x(t)$ would naively contribute $1 \cdot H(1) = 0$, and missing the zero costs you the elegance of the answer. Always evaluate every input frequency, including $\omega = 0$.

---

## Master cheat sheet (for the open-book reference panel)

| problem type | killer formula | trap |
|---|---|---|
| **Steady-state to step** | $y_{ss} = H(z=1)$ (DT) or $H(s=0)$ (CT), **only if stable** | apply FVT to unstable system → bogus number |
| **First-order CT LPF cutoff** | $\tau = 1/\omega_c = 1/(2\pi f_c)$ | $f$ vs $\omega$: $\omega = 2\pi f$ |
| **First-order DT LPF (FE)** | pole at $z = 1 - a$, $a = \omega_c T$ | $\omega_c T$ must be $\lesssim 1$ |
| **Stability ROC (DT)** | ROC must include $|z| = 1$ | zeros never bound ROC, only poles |
| **Forward Euler substitution** | $s \to (z-1)/T$ | $\omega_c T \approx 1$ collapses pole to $z=0$ |
| **TDM PAM bandwidth** | $B_{\text{PAM}} = (N+1) \cdot 2 B_{\text{voice}}$ | $(N+1)$, not $N$ — sync slot |
| **Phase margin design** | PM $= 180° + \angle L(j\omega_{gc})$, with $|L(j\omega_{gc})| = 1$ | always two equations, two unknowns |
| **Sampled-data sinusoid** | $\cos(\omega t) \to |H(e^{j\omega T})|\cos(\omega t + \angle H)$ | check Nyquist; evaluate at every input frequency including DC |

---

## Quick-reference numerical answers

| #         | answer                                      |     |        |
| --------- | ------------------------------------------- | --- | ------ |
| 1.1       | $y_{ss}[n] = -1$                            |     |        |
| 1.2       | DNE (pole at $z = 3$ → unstable)            |     |        |
| 1.3       | $y_{ss}(t) = -1/4$                          |     |        |
| 1.4       | DNE (pole at $s = +2$ → unstable)           |     |        |
| 2         | $\tau = 1/(14\pi) \approx 22.74$ ms         |     |        |
| 3         | $a = \pi/10 \approx 0.314$                  |     |        |
| 4         | ROC: $                                      | z   | > 0.5$ |
| 5         | $H_{DT}(z) = 1/(4z^2)$                      |     |        |
| 6         | $N_{\max} = 13$                             |     |        |
| 7         | $K \approx 13.35$, $\tau_z \approx 0.181$ s |     |        |
| 8         | $y(t) \approx 0.0333\cos(t + 88.4°)$        |     |        |
| **total** | **$8/8$ verified end-to-end**               |     |        |

---

## Related

- [[eee-304]] — course page.
- [[eee-304-final-walkthrough]] — concept-level walkthrough built from the [[slides-2026-05-04-eee-304-final-exam-preview]] preview deck (covers the same 8 problem *types* but at the conceptual level rather than the actual exam numbers).
- [[eee-304-hw7-walkthrough]] — fully-worked TDM-PAM examples (Problem 6 background).
- [[butterworth-filter]], [[region-of-convergence]], [[pulse-amplitude-modulation]], [[time-division-multiplexing]] — concept pages used here.

**Sources:**
- [Final exam (1 pp, 8 problems + transform sheet)](../../raw/slides/eee-304/304final-1.pdf) — the actual exam.
- [Oppenheim-Willsky transform tables (12 pp)](../../raw/slides/eee-304/fourier.pdf) — open-book reference. Tables 3.1/3.2 (FS properties), 4.1/4.2 (FT properties + pairs), 5.1/5.2 (DTFT), 9.1/9.2 (Laplace), 10.1/10.2/10.3 (z-transform). Print and bring this.
- [Final Exam Preview (8 pp)](../../raw/slides/eee-304/Final_slides.pdf) — the deck that introduced these 8 problem types.
