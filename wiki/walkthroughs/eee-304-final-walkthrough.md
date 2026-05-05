---
title: EEE 304 Final Exam — Per-Problem Walkthrough (8 problems, 350 pts, 150 min)
type: walkthrough
course: [[eee-304]]
tags: [eee-304, final, walkthrough, exam, transfer-function, steady-state, butterworth, roc, euler, tustin, bilinear, pam, tdm, fdm, feedback, sampled-data, sampling]
sources: [[slides-2026-05-04-eee-304-final-exam-preview]]
created: 2026-05-04
updated: 2026-05-04
---

# EEE 304 Final Exam — Walkthrough

> [!note] **Logistics.** Open-book online final, **available May 4, 10:00 AM → May 6, 11:59 PM**, **150 minutes** once started, **350 pts total**, **8 problems**. Source: [Final Exam Preview slides](../../raw/slides/eee-304/Final_slides.pdf), 8 pp.

> [!warning] **Use this as a roadmap, not a substitute for the actual problems.** Each problem on the exam will have *different* numbers from the slide examples. The slide examples show the **type** of question — your job is to know the technique cold so you can apply it to whatever transfer function, cutoff, or block diagram appears.

> [!tip] **Time budget.** $150 \text{ min} / 8 \text{ problems} \approx 18 \text{ min/problem}$, leaving ~6 min slack for the harder ones (Problem 8, the disguised PAM/TDM question). Keep an eye on the clock — open-book ≠ unlimited time.

---

## Problem 1 — System Responses (Steady-State)

> **Source:** Module 1 + Homework 1. Given a system (CT or DT), determine the **steady-state** response.
> **Slide example:** Filter with impulse response $h(t) = e^{-t}u(t-1) - e^{-2t}u(t)$. (1) Find $H(s)$. (2.1) Find $Y(s)$ for $x(t) = \sin(t)u(t)$.

### The concept — example first

A **stable** LTI system driven by a sinusoid eventually settles into a sinusoid at the **same frequency** but with amplitude scaled by $|H(j\omega)|$ and phase shifted by $\angle H(j\omega)$:

$$x(t) = A\cos(\omega t) \;\;\Longrightarrow\;\; y_{ss}(t) = A\,|H(j\omega)|\,\cos\!\bigl(\omega t + \angle H(j\omega)\bigr)$$

So computing the steady-state response collapses to **(a) finding $H(s)$, then (b) plugging in $s = j\omega$**.

### Walkthrough — slide example

**Step 1 — Find $H(s)$ by Laplace-transforming each piece of $h(t)$.**

The first term has a **time delay** of $1$, so it needs the time-shift property $\mathcal{L}\{f(t-a)u(t-a)\} = e^{-as}F(s)$. Pull out the constant first:

$$e^{-t}u(t-1) \;=\; \underbrace{e^{-1}}_{\text{constant}} \cdot e^{-(t-1)}u(t-1)$$

Now apply $\mathcal{L}\{e^{-(t-1)}u(t-1)\} = e^{-s}/(s+1)$:

$$\mathcal{L}\{e^{-t}u(t-1)\} \;=\; \frac{e^{-1}\,e^{-s}}{s+1} \;=\; \frac{1}{e}\cdot\frac{e^{-s}}{s+1}$$

Second term is the standard Laplace pair: $\mathcal{L}\{e^{-2t}u(t)\} = 1/(s+2)$.

> [!example] **Headline transfer function**
>
> $$\boxed{\,H(s) = \frac{1}{e}\cdot\frac{e^{-s}}{s+1} \;-\; \frac{1}{s+2}\,}$$

**Step 2 — Laplace transform of the input.** $\mathcal{L}\{\sin(t)u(t)\} = 1/(s^2 + 1)$.

> [!example] **Output Laplace transform**
>
> $$\boxed{\,Y(s) = H(s)\,X(s) = \left(\frac{1}{e}\cdot\frac{e^{-s}}{s+1} - \frac{1}{s+2}\right)\cdot\frac{1}{s^2+1}\,}$$

**Step 3 — Steady-state response (the part the slide doesn't write out, but the topic asks for).** With $\omega = 1$ rad/s, evaluate $H(j1)$:

$$H(j1) = \frac{e^{-j(1)}}{e\,(j+1)} - \frac{1}{j+2}$$

> [!info]- 📐 Show derivation — magnitude and phase of $H(j1)$
>
> Term A: $\dfrac{e^{-j}}{e(j+1)} = \dfrac{e^{-j}}{e\sqrt{2}\,e^{j\pi/4}} = \dfrac{1}{e\sqrt{2}}\,e^{-j(1+\pi/4)}$. Magnitude $= 1/(e\sqrt{2}) \approx 0.260$, phase $\approx -1.785$ rad.
>
> Term B: $\dfrac{1}{j+2} = \dfrac{1}{\sqrt{5}\,e^{j\arctan(1/2)}} = \dfrac{1}{\sqrt{5}}\,e^{-j\arctan(1/2)}$. Magnitude $\approx 0.447$, phase $\approx -0.464$ rad.
>
> Subtract Term B from Term A as complex numbers; convert back to polar to get $|H(j1)|$ and $\angle H(j1)$.

**Then** $y_{ss}(t) = |H(j1)|\sin\!\bigl(t + \angle H(j1)\bigr)$.

### Common mistakes

- **Forgetting to factor $e^{-1}$ out** when applying time-shift to $e^{-t}u(t-1)$. The shift property requires $f(t-a)u(t-a)$ — your function must be expressed as the *delayed* version of itself.
- **Plugging $s = \omega$ instead of $s = j\omega$.** Steady-state needs the imaginary axis.
- **Computing the *full* output $y(t)$ when only the steady-state piece is asked.** Steady-state ignores the transient (the part that decays from initial conditions / impulse-response startup).

> [!tip] **DT version of the same problem.** For a DT system $H(z)$ driven by $x[n] = A\cos(\Omega n)$, the steady-state output is $A\,|H(e^{j\Omega})|\,\cos(\Omega n + \angle H(e^{j\Omega}))$ — same idea, evaluate on the **unit circle** instead of the $j\omega$-axis.

---

## Problem 2 / Problem 3 — Filtering (Determine Parameters from Cutoff)

> **Source:** Module 2 slides. Given a cutoff frequency, determine the filter parameters (CT or DT).
> **Slide example:** Separate $1$ Hz signal from $100$ Hz noise using a DT filter at $f_s = 2$ kHz sampling. Use a first-order Butterworth.

### The concept — example first

You're handed a "noise above $f_n$, signal below $f_s$" situation and told to design a low-pass filter. The standard recipe:

1. **Pick the cutoff $\omega_c$** — common rule of thumb: place it about **one decade below the noise** so the noise gets a healthy $-20$ dB/decade attenuation past the corner.
2. **Write the CT prototype.** First-order Butterworth: $H(s) = \dfrac{1}{\tau s + 1}$ with $\tau = 1/\omega_c$.
3. **(If DT)** Map $s \to z$ using Forward Euler, Backward Euler, or Tustin (see Problem 5).
4. **Sanity-check**: pole magnitude (DT pole inside unit circle = stable) and pole location ($z_{\text{pole}} \approx 1 - \omega_c T$ for FE on slow systems).

### Walkthrough — slide example

**Given:** $f_n = 100$ Hz, $f_s = 1$ Hz, sampling rate $= 2$ kHz, target $-20$ dB attenuation at the noise.

**Step 1 — Pick the cutoff.** One decade below the noise: $f_c = 10$ Hz $\Rightarrow \omega_c = 2\pi(10) \approx 62.8$ rad/s.

**Step 2 — Write the CT first-order LPF.** With $\tau = 1/\omega_c = 1/62.8 \approx 0.01592$ s:

$$F_{B1}(s) = \frac{1}{\tau s + 1} = \frac{1}{0.01592\,s + 1}$$

CT corner: $\omega_c = 1/\tau = 1/0.01592 \approx 62.8$ rad/s ✓

**Step 3 — Map to DT using Forward Euler.** Sampling period $T = 1/f_s^{(\text{sample})} = 1/2000 = 0.5$ ms. The slide uses the FE-equivalent first-order pole expression:

$$H_{DT}(z) \;\approx\; \frac{\lambda}{z - (1 - \lambda)}, \qquad \lambda = \omega_c T$$

$$\lambda = (62.8)(0.0005) = 0.0314 \;\;\Longrightarrow\;\; 1 - \lambda = 0.9686$$

So the DT pole sits at $z \approx 0.969$ (the slide writes this as $\approx 0.9691$, which agrees with the more accurate $e^{-\omega_c T} = e^{-0.0314} \approx 0.9691$ — for small $\omega_c T$, FE and exact match closely).

> [!example] **Headline DT filter**
>
> $$\boxed{\;DB1(z) = \frac{0.01547\,z + 0.01547}{z - 0.9691}\;}$$
>
> (The numerator $0.01547$ comes from normalizing the DC gain to $1$: $H_{DT}(1) = 1$ requires numerator $= (1 - 0.9691)/2 \approx 0.01547$ each, when the bilinear gives a numerator of the form $\beta(z + 1)$.)

**Step 4 — Sanity-check at DC and at the noise.**

- **DC** ($z = 1$): $H_{DT}(1) = (0.01547 + 0.01547)/(1 - 0.9691) = 0.0309/0.0309 = 1$ ✓
- **At $f_n = 100$ Hz** ($\Omega = 2\pi \cdot 100 / 2000 = \pi/10$ rad/sample): $|H_{DT}(e^{j\pi/10})|$ should be roughly $-20$ dB ($\approx 0.1$). The slide's Bode plot confirms this — the FE and exact-match curves overlap nearly perfectly through the band.

### Common mistakes

- **Forgetting the $2\pi$** when converting $f$ (Hz) to $\omega$ (rad/s).
- **Mixing rad/s and rad/sample.** The CT design uses $\omega$ (rad/s); after sampling, the DT design uses $\Omega = \omega T$ (rad/sample). Always label units.
- **Using FE on a fast system** ($\omega_c T$ not $\ll 1$). FE only matches well when the CT corner is **much** slower than the sample rate. Here $\omega_c T = 0.0314 \ll 1$ ✓ — FE is appropriate. If $\omega_c T \approx 1$, switch to Tustin (warping handled).

> [!tip] **Why "one decade below"?** A first-order LPF rolls off at $-20$ dB/decade past its corner. So if the corner is at $f_n / 10$, attenuation at $f_n$ is exactly $-20$ dB ($\approx 10\times$ amplitude reduction). For sharper rejection, increase the order (Butterworth-2 gives $-40$ dB/dec, etc.) — at the cost of more group delay.

---

## Problem 4 — Region of Convergence (ROC)

> **Source:** Module 1 + Module 4. Find the region of convergence of a transform.

### The concept — example first

The **ROC** is the set of $s$-values (CT) or $z$-values (DT) for which the transform integral/sum converges. The pole locations don't *uniquely* determine the time-domain signal — the **ROC + poles together** do. Three rules cover almost every exam case:

| signal type | CT ROC ($X(s)$) | DT ROC ($X(z)$) |
|---|---|---|
| **causal** ($x(t) = 0$ for $t < 0$, or $x[n] = 0$ for $n < 0$) | right of the rightmost pole | outside the outermost pole |
| **anticausal** | left of the leftmost pole | inside the innermost pole |
| **two-sided** | strip between two poles | annulus between two poles |
| **stable** (BIBO) | ROC must contain the **$j\omega$-axis** | ROC must contain the **unit circle** |

### Walkthrough — generic example

Suppose $H(s) = \dfrac{1}{(s+1)(s-2)}$. Poles at $s = -1$ and $s = +2$.

**Three possible interpretations** depending on which ROC you assign:

1. **Causal:** ROC is $\text{Re}\{s\} > 2$. Stable? No — doesn't include the $j\omega$-axis.
2. **Anticausal:** ROC is $\text{Re}\{s\} < -1$. Stable? No — doesn't include the $j\omega$-axis.
3. **Two-sided:** ROC is the strip $-1 < \text{Re}\{s\} < 2$. Stable? **Yes** — contains the $j\omega$-axis.

> [!example] **Headline answer (this example)**
>
> The system is **stable iff** the ROC is the two-sided strip $-1 < \text{Re}\{s\} < 2$. The corresponding $h(t)$ has a right-sided piece from the $s = -1$ pole and a left-sided piece from the $s = +2$ pole.

### DT version

For $H(z) = \dfrac{z}{(z - 0.5)(z - 2)}$ — poles at $z = 0.5, 2$:

| interpretation | ROC | stable? |
|---|---|---|
| causal | $|z| > 2$ | no (excludes unit circle) |
| anticausal | $|z| < 0.5$ | no (excludes unit circle) |
| two-sided | $0.5 < |z| < 2$ | **yes** |

### Common mistakes

- **Assuming causal automatically.** Two-sided systems are perfectly valid; the question often probes whether you check.
- **Confusing "ROC contains origin" with stability.** Stability needs the $j\omega$-axis (CT) or unit circle (DT), not the origin.
- **Forgetting that ROC never contains a pole.** The pole is exactly where the transform blows up.

See [[region-of-convergence]] for the full ROC concept page.

---

## Problem 5 — Euler / Tustin Approximations (DT-CT Filter Equivalence)

> **Source:** Module 1 + Module 4. Approximating $z = e^{sT}$ for finite-dimensional implementation.
> **Slide example:** Forward Euler $z = 1 + sT$ — the first two terms of the Taylor expansion of $e^{sT}$.

### The concept — example first

The exact CT-to-DT mapping is $z = e^{sT}$ (where $T$ is the sample period). This is **transcendental** — you can't realize it with a finite difference equation. Three practical approximations:

| method | $z \leftarrow$ | $s \leftarrow$ | stability preserved? | freq match |
|---|---|---|---|---|
| **Forward Euler (FE)** | $1 + sT$ | $(z - 1)/T$ | **NO** — stable CT pole can map outside unit circle | good only at $|sT| \ll 1$ |
| **Backward Euler (BE)** | $1/(1 - sT)$ | $(z - 1)/(zT)$ | yes | poor (asymmetric warping) |
| **Tustin (Bilinear)** | $\dfrac{1 + sT/2}{1 - sT/2}$ | $\dfrac{2}{T}\dfrac{z - 1}{z + 1}$ | **yes** (LHP $\to$ inside unit circle one-to-one) | best (slight freq warping near Nyquist) |

### Walkthrough — what the slide is showing

The slide presents **Forward Euler**: $z = 1 + sT$. This comes from the truncated Taylor series of $e^{sT} = 1 + sT + (sT)^2/2! + \ldots$

**Equivalent rearrangement:** $sT = z - 1 \;\Longrightarrow\; s = (z - 1)/T$. So in any CT transfer function, **substitute $s \to (z-1)/T$** to get the DT approximation.

> [!example] **Worked FE conversion** — apply FE to $H(s) = \dfrac{a}{s + a}$ (first-order LPF with corner $\omega_c = a$).
>
> Substitute $s = (z-1)/T$:
> $$H_{DT}(z) = \frac{a}{(z-1)/T + a} = \frac{aT}{z - 1 + aT} = \frac{aT}{z - (1 - aT)}$$
>
> So the DT pole sits at $z = 1 - aT$. **Stable** iff $|1 - aT| < 1$ — fails if $aT > 2$. So FE breaks for fast CT systems sampled slowly.

### When to pick which

- **Slow filter, lots of oversampling** ($\omega_c T \ll 1$) → FE is fine and simplest.
- **Critical stability or frequency response** → use Tustin. Pre-warp the cutoff if the CT spec is exact.
- **Backward Euler** is rarely the answer on this exam — listed for completeness.

> [!warning] **FE can destabilize.** If the slide gives you $H(s) = 100/(s + 50)$ and asks you to discretize at $T = 0.05$ (i.e. $20$ Hz sample rate), then FE pole = $1 - 50(0.05) = -1.5$ — outside the unit circle. The DT system is **unstable** even though the CT one was stable. Tustin would have been safe.

### Common mistakes

- **Forgetting the $T$** when substituting $s = (z-1)/T$ (or any of the other mappings).
- **Pre-warping confusion**: pre-warping is only relevant for Tustin when you need exact frequency match at a specified critical frequency. FE doesn't get pre-warped.
- **Mixing the two directions**: $z \leftarrow$ formulas convert *poles* (numerical $s$ values $\to$ numerical $z$ values); $s \leftarrow$ formulas convert *transfer functions*. Don't apply $z = 1 + sT$ to a transfer function literally.

---

## Problem 6 — Pulse Amplitude Modulation (TDM vs FDM Bandwidth)

> **Source:** Homework 7. Given $N$ voice signals of bandwidth $B$, compute the channel bandwidth required by a TDM-PAM system vs an FDM system.
> **Slide example:** $N = 4$ voice signals, each bandlimited to $B = 4$ kHz.

### The concept — example first

**TDM** (time-division multiplexing) shares one wide channel by **interleaving samples** in time — each signal gets a thin time-slot inside every sampling frame. Bandwidth scales with the *pulse rate*, which scales with $N$.

**FDM** (frequency-division multiplexing) gives each signal its own slice of the spectrum — bandwidth scales with $\sum B_i$.

Same total bandwidth budget; very different implementation.

### Walkthrough — slide example

**TDM-PAM side** (with $N + 1 = 5$ slots per frame, the $+1$ being a sync pulse).

**Step 1 — Frame rate (sample rate per channel).** Nyquist requires sampling each $4$ kHz signal at $\geq 8$ kHz. Pick the minimum $f_{\text{frame}} = 8$ kHz $\Rightarrow$ frame period $T_{\text{frame}} = 1/8000 = 125 \mu\text{s}$.

**Step 2 — Slot duration.** $5$ slots per frame: $T_{\text{slot}} = 125\,\mu\text{s} / 5 = 25\,\mu\text{s}$.

**Step 3 — Channel bandwidth.** Each slot contains a pulse roughly $T_{\text{slot}}$ wide, so the required channel bandwidth (taking the first-null bandwidth of a rectangular pulse) is:

$$B_{TDM} = \frac{1}{T_{\text{slot}}} = \frac{1}{25\,\mu\text{s}} = 40\text{ kHz}$$

> [!example] **Headline (TDM)** — $\boxed{\,B_{TDM} = 40\text{ kHz}\,}$

**FDM side**

Each signal occupies $4$ kHz; with $4$ signals in adjacent slots:

$$B_{FDM} = N \cdot B = 4 \cdot 4\text{ kHz} = 16\text{ kHz}$$

> [!example] **Headline (FDM)** — $\boxed{\,B_{FDM} = 16\text{ kHz}\,}$

### Common mistakes

- **Forgetting the sync slot.** TDM frames usually carry $N + 1$ slots (or more for headers/CRCs). The slide's example uses **$N + 1 = 5$**.
- **Using the signal bandwidth as the slot width.** Wrong. The slot width is $T_{\text{frame}}/(N+1)$; the channel bandwidth is $1/T_{\text{slot}}$.
- **Confusing sampling rate with channel bandwidth.** Sampling rate is $8$ kHz/channel. Channel BW is much higher because each frame holds $N+1$ pulses, not $1$.
- **FDM gotcha**: practical FDM also needs **guard bands** between slices for filter roll-off, so the real bandwidth is slightly more than $N \cdot B$. The slide's footnote calls this out.

> [!tip] **Why TDM > FDM in bandwidth here.** TDM compresses each sample into a thin pulse, which by Fourier reciprocity needs a wide spectrum. FDM stays bandwidth-efficient but needs precise filters and tunable carriers per channel.

See [[pulse-amplitude-modulation]], [[time-division-multiplexing]], and the existing [[eee-304-hw7-walkthrough]] (Problems 2 & 3) for fully-worked variants.

---

## Problem 7 — Feedback Control System (Closed-Loop TFs)

> **Source:** Lab 3 Problem 1. Standard unity-feedback block diagram with controller $C(s)$, plant $P(s)$, reference $r$, disturbance $d$ entering at the plant input, output $y$.

### The concept — example first

The block diagram on the slide is the **canonical unity-feedback loop with input disturbance**:

```
         d
         |
r ─⊕──→ C(s) ──→⊕──→ P(s) ──→ y
   ↑-              |
   |               |
   └───── y ←──────┘
```

Two transfer functions of interest from the two inputs:

$$T_{ry}(s) = \frac{Y(s)}{R(s)}\bigg|_{D=0} = \frac{C(s)\,P(s)}{1 + C(s)\,P(s)} \qquad\text{(complementary sensitivity)}$$

$$T_{dy}(s) = \frac{Y(s)}{D(s)}\bigg|_{R=0} = \frac{P(s)}{1 + C(s)\,P(s)} \qquad\text{(disturbance-to-output)}$$

And the **error sensitivity** (often what's actually graded):

$$T_{re}(s) = \frac{E(s)}{R(s)}\bigg|_{D=0} = \frac{1}{1 + C(s)\,P(s)} \qquad\text{(sensitivity)}$$

### Walkthrough — derive $T_{ry}$ from the diagram

**Step 1 — Write the loop equations.**

$$Y = P\,(U + D), \qquad U = C\,E, \qquad E = R - Y$$

**Step 2 — Substitute $E$ then $U$.**

$$Y = P\bigl(C(R - Y) + D\bigr) = PCR - PCY + PD$$

**Step 3 — Solve for $Y$.**

$$Y + PCY = PCR + PD \;\Longrightarrow\; Y(1 + PC) = PCR + PD$$

$$\boxed{\,Y = \frac{PC}{1+PC}\,R \;+\; \frac{P}{1+PC}\,D\,}$$

### Steady-state error from the **Final Value Theorem**

For a stable closed loop and a step reference $R(s) = 1/s$ with $D = 0$:

$$E(s) = \frac{1}{1 + C(s)P(s)} \cdot \frac{1}{s}$$

$$e_{ss} = \lim_{s\to 0} s\cdot E(s) = \lim_{s\to 0}\frac{1}{1 + C(s)P(s)} = \frac{1}{1 + K_p}, \quad K_p = \lim_{s\to 0} C(s)P(s)$$

| **system type** $N$ (# of free integrators in $L = CP$) | step error $e_{ss}^{(\text{step})}$ | ramp error $e_{ss}^{(\text{ramp})}$ | parabolic error |
|---|---|---|---|
| 0 | $1/(1+K_p)$ | $\infty$ | $\infty$ |
| 1 | $0$ | $1/K_v$ | $\infty$ |
| 2 | $0$ | $0$ | $1/K_a$ |

where $K_v = \lim_{s\to 0} sL(s)$ and $K_a = \lim_{s\to 0} s^2 L(s)$.

> [!example] **Worked example (typical exam phrasing).** "$P(s) = 1/(s+1)$, $C(s) = K$. Find the steady-state error to a unit step."
>
> $L(s) = K/(s+1)$, $K_p = L(0) = K$. Therefore $e_{ss} = 1/(1+K)$. Increase $K$ to shrink the error — at the cost of stability margin.

### Common mistakes

- **Forgetting the negative sign at the summing junction.** $E = R - Y$, not $R + Y$.
- **Applying FVT to an unstable closed loop.** FVT only gives a meaningful answer when $sE(s)$ has all poles in the open LHP. Always check stability of $1 + CP$ first.
- **Computing $T_{ry}$ but forgetting $T_{dy}$**, or vice-versa. Disturbance rejection is a separate transfer function — read the question carefully.

---

## Problem 8 — Sampling and DT Processing (Find CT Equivalent)

> **Source:** Homework 4 Problem 2. Given the DT-equivalent of a sampled-data system, find the CT filter that the system implements (using FE and Tustin to invert the discretization).
> **Slide example:** $H_{DT}(z) = \dfrac{0.1}{z - 0.95}$ at $1$ kHz sampling. AAF cutoff $500$ Hz. Find the CT filter via FE and Tustin.

### The concept — example first

A sampled-data filter is the *DT cousin* of the CT filter you wanted to implement. To **reverse-engineer** the CT filter from the DT one, you substitute the same approximation that was originally used to discretize:

- If FE was used: substitute $z \to 1 + sT$ into $H_{DT}(z)$ → get $H_{FE}(s)$.
- If Tustin was used: substitute $z \to (1 + sT/2)/(1 - sT/2)$ → get $H_{Tustin}(s)$.

The two will differ — Tustin is more accurate at higher frequencies, FE is simpler.

### Walkthrough — slide example

**Given:** $H_{DT}(z) = \dfrac{0.1}{z - 0.95}$, $T = 1/1000 = 1$ ms.

#### FE inversion

Substitute $z = 1 + sT = 1 + 0.001s$:

$$H_{FE}(s) = \frac{0.1}{(1 + 0.001s) - 0.95} = \frac{0.1}{0.001s + 0.05}$$

Multiply numerator and denominator by $1000$:

$$\boxed{\,H_{FE}(s) = \text{(AAF)}\cdot\frac{100}{s + 50}\,}$$

**CT corner:** $50$ rad/s $\approx 8.0$ Hz. (The AAF in front bandlimits to $500$ Hz; the DT filter then provides the slow rolloff at ~$8$ Hz.)

#### Tustin inversion

Substitute $z = \dfrac{1 + sT/2}{1 - sT/2} = \dfrac{1 + 0.0005s}{1 - 0.0005s}$:

> [!info]- 📐 Show derivation — Tustin substitution
>
> $$H_{Tustin}(s) = \frac{0.1}{\dfrac{1 + 0.0005s}{1 - 0.0005s} - 0.95}$$
>
> Multiply numerator and denominator by $(1 - 0.0005s)$:
>
> $$= \frac{0.1\,(1 - 0.0005s)}{(1 + 0.0005s) - 0.95(1 - 0.0005s)}$$
>
> Expand the denominator:
>
> $$(1 + 0.0005s) - (0.95 - 0.000475s) = 0.05 + 0.000975s$$
>
> So:
>
> $$H_{Tustin}(s) = \frac{0.1(1 - 0.0005s)}{0.05 + 0.000975s} = \frac{0.1 - 0.00005s}{0.05 + 0.000975s}$$
>
> Multiply num + den by $1/0.000975 \approx 1025.6$ to put it in monic form ($s + a$ in the denominator):
>
> Den: $(0.05 + 0.000975s)/0.000975 = 51.28 + s$.
> Num: $(0.1 - 0.00005s)/0.000975 = 102.56 - 0.05128s$.

$$\boxed{\,H_{Tustin}(s) = \text{(AAF)}\cdot\frac{-0.05128\,s + 102.6}{s + 51.28}\,}$$

**CT corner:** $51.28$ rad/s $\approx 8.16$ Hz. Very close to the FE answer — Tustin and FE agree well here because $\omega_c T \approx 0.05 \ll 1$.

> [!note] **Why is Tustin's numerator different?** Tustin maps the DT zero at $z = 0$ to a CT zero at $s = +2/T = +2000$ rad/s — a **right-half-plane (non-minimum-phase)** zero. That's the $-0.05128 s$ term. FE's substitution doesn't introduce extra zeros because $z = 1 + sT$ is a polynomial (no $s$ in the denominator), while Tustin's $z(s)$ is rational. The DC gains agree: $H_{FE}(0) = 100/50 = 2$ vs $H_{Tustin}(0) = 102.6/51.28 = 2.001$ ✓.

### Common mistakes

- **Forgetting to bring the AAF along**. The full system is `AAF → sample → H_DT → reconstruct`. The CT equivalent is `AAF × H_eq(s)`, not just $H_{eq}(s)$.
- **Sign errors in Tustin algebra.** Watch the sign on $0.95(1 - 0.0005s)$ — both terms get the negative.
- **Mixing up the direction**: this problem goes **DT → CT** (substitute $z(s)$ into $H(z)$). The companion problem (CT → DT) goes the other way (substitute $s(z)$ into $H(s)$). The exam might ask either direction.
- **Using the wrong $T$.** Read the sampling rate carefully. $1$ kHz $\Rightarrow T = 0.001$ s. $2$ kHz $\Rightarrow T = 0.0005$ s.

---

## Master cheat sheet (one-page recall)

| topic | killer formula | gotcha |
|---|---|---|
| **Steady-state to sinusoid** | $y_{ss} = \|H(j\omega)\|\sin(\omega t + \angle H(j\omega))$ | use $j\omega$, not $\omega$ |
| **Time-shift Laplace** | $\mathcal{L}\{f(t-a)u(t-a)\} = e^{-as}F(s)$ | factor constant out first |
| **First-order LPF (CT)** | $H(s) = 1/(\tau s + 1)$, $\tau = 1/\omega_c$ | $\omega_c$ in rad/s, not Hz |
| **Forward Euler** | $z = 1 + sT$, equivalently $s = (z-1)/T$ | can destabilize |
| **Tustin** | $z = \frac{1 + sT/2}{1 - sT/2}$, $s = \frac{2}{T}\frac{z-1}{z+1}$ | safe; pre-warp if needed |
| **ROC stability** | CT: contains $j\omega$-axis. DT: contains unit circle. | causality + stability often conflict |
| **TDM channel BW** | $B_{TDM} = (N+1) \cdot 2B$ for $N$ signals | include sync slot |
| **FDM channel BW** | $B_{FDM} = N \cdot B$ | plus guard bands in practice |
| **Closed-loop TF (unity FB)** | $T_{ry} = \dfrac{CP}{1+CP}$, $T_{dy} = \dfrac{P}{1+CP}$ | $E = R - Y$ (negative FB) |
| **FVT for $e_{ss}$** | $e_{ss} = \lim_{s\to 0} sE(s) = \dfrac{1}{1 + K_p}$ for type-0 step | only if closed loop is stable |

---

## Problem-by-problem time budget

| # | topic | ~min | source to review night-before |
|---|---|---|---|
| 1 | Steady-state response | 15 | Module 1, HW1 |
| 2–3 | Filtering (CT or DT) | 18 + 18 | Module 2 slides |
| 4 | ROC | 10 | Module 1 |
| 5 | Euler / Tustin | 12 | Module 4 |
| 6 | PAM (TDM/FDM) | 15 | HW7 + [[eee-304-hw7-walkthrough]] |
| 7 | Feedback closed-loop | 20 | Lab 3 Problem 1 |
| 8 | Sampling + DT processing | 25 | HW4 Problem 2 |
| — | reading + check | 17 | — |
| **total** | | **150** | |

---

## Related

- [[eee-304]] — course page (this walkthrough is now linked from the Walkthroughs section there).
- [[eee-304-hw7-walkthrough]] — fully-worked TDM/PAM/chopper-amplifier examples (Problem 6 prep).
- [[eee-304-lab-4-walkthrough]] — AM modulation/demodulation in Simulink (background for Problem 1's filter intuition).
- [[eee-304-lab-ec1-walkthrough]] — `butter` filter design with MATLAB at $f_s = 5$ kHz (Problem 2/3 prep).
- [[eee-304-lab-ec2-walkthrough]] — discrete-time integral controller (Problem 7 prep).
- [[butterworth-filter]] — the workhorse first-order LPF used in Problems 2 & 3.
- [[region-of-convergence]] — full ROC concept page (Problem 4).
- [[pulse-amplitude-modulation]], [[time-division-multiplexing]] — Problem 6.
- [[z-transform]] — Problems 4, 5, 8 background.

**Sources used to write this walkthrough:**
- [Final Exam Preview slides (8 pp)](../../raw/slides/eee-304/Final_slides.pdf) — primary source.
- [HW7 sample with worked answers](../../raw/homework/304_hw7_sample25.pdf) — cross-check for Problem 6.
- [Lab EC1 PDF](../../raw/labs/EEE_304_Lab_EC1.pdf), [Lab EC2 PDF](../../raw/labs/EEE_304_Lab_EC2.pdf) — Problems 2/3 and Problem 7 background.
