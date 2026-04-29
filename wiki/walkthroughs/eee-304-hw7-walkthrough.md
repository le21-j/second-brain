---
title: EEE 304 HW7 — Cascaded Modulation, TDM-PAM, Chopper Amplifier (Walkthrough)
type: example
course: [[eee-304]]
tags: [eee-304, homework, walkthrough, am, modulation, demodulation, pam, tdm, chopper-amplifier, fourier]
sources: [[homework-2026-04-26-eee-304-hw7]]
created: 2026-04-26
updated: 2026-04-26
---

# EEE 304 HW7 — Walkthrough

> [!note] **What this is.** A per-problem walkthrough of HW7. For every problem I (a) **state it** verbatim, (b) **explain the overarching concept** so you understand what's being tested, (c) **walk through the derivation step by step** so you can reproduce it on paper, and (d) **cross-check** against the worked sample at `raw/homework/304_hw7_sample25.pdf`.
>
> The **highlighted lines** (like this) are the headline answers — what to write down on the submission.

> [!warning] **Use the sample as a check, not a shortcut.** The sample HW from 2024 has fully-worked answers; the 2026 assignment is the same three problems. Walk through the steps yourself, then verify against the sample. The grader cares about your **derivation**, not just your final number.

---

## Problem 1 — Double-Modulated AM, Find the Demod Frequencies

> **Problem 1.** An AM modulation process uses a carrier frequency of **100 kHz**. Suppose that the modulated signal is used to modulate a **300 kHz** carrier. Find the frequencies of the demodulation process that can be used to recover the original signal.

### The concept

Each multiplication by $\cos(\omega t)$ shifts the spectrum by $\pm\omega$ — that's the modulation property of the Fourier transform. **Cascaded** modulators therefore create copies at **sum and difference** frequencies of the carriers used. To recover the message, the demodulator must shift one of those replicas back to baseband — which means the demod carrier must equal **the center frequency of one of the replicas**.

> [!tip] **Shortcut intuition.** Multiplying by $\cos(\omega_a t)$ *then* multiplying by $\cos(\omega_b t)$ is the same as multiplying by
>
> $$\cos(\omega_a t)\cos(\omega_b t) = \tfrac{1}{2}\bigl[\cos((\omega_a-\omega_b)t) + \cos((\omega_a+\omega_b)t)\bigr].$$
>
> So a double modulation effectively places replicas at $\omega_a + \omega_b$ and $\omega_a - \omega_b$ (and their negatives). Either of these is a valid demod frequency.

### Walkthrough

Let $\omega_1 = 2\pi(100\text{ kHz})$ and $\omega_2 = 2\pi(300\text{ kHz})$.

> [!example] **Step-by-step**
>
> **Step 1 — First modulation by 100 kHz.** Starting from $X(j\omega)$ (baseband, bandlimited to some $B$), multiplication by $\cos(\omega_1 t)$ yields
>
> $$X_1(j\omega) = \tfrac{1}{2}\bigl[X(j(\omega + \omega_1)) + X(j(\omega - \omega_1))\bigr]$$
>
> i.e., **replicas centered at $\pm 100$ kHz**.
>
> **Step 2 — Second modulation by 300 kHz.** Multiplying $X_1(j\omega)$ by $\cos(\omega_2 t)$ shifts each replica by $\pm 300$ kHz:
>
> | Existing replica center | After $\pm 300$ kHz shift |
> |---|---|
> | $+100$ kHz | $+400$ kHz **and** $-200$ kHz |
> | $-100$ kHz | $+200$ kHz **and** $-400$ kHz |
>
> So after the cascade, copies of $X(j\omega)$ live at $\pm 200$ kHz and $\pm 400$ kHz.
>
> **Step 3 — Pick a demod frequency.** To recover $X(j\omega)$ at baseband, multiply once more by $\cos(\omega_{\text{demod}} t)$ so that one of those replicas lands on $\omega = 0$. The two valid choices:
>
> - $\omega_{\text{demod}} = 2\pi(200\text{ kHz})$ — picks up the $\pm 200$ kHz replicas.
> - $\omega_{\text{demod}} = 2\pi(400\text{ kHz})$ — picks up the $\pm 400$ kHz replicas.
>
> (Then a lowpass filter rejects the other shifted copies that land at $\pm 400$ kHz or $\pm 600$ kHz, etc.)

### Answer

**Demodulation can use either $f_{\text{demod}} = 200$ kHz or $f_{\text{demod}} = 400$ kHz** to recover the original signal. (Pick either one; both work.)

> [!note] **Why not 100 kHz or 300 kHz?** Because the cascaded carriers don't leave any spectral content centered at those frequencies — only at their sum (400 kHz) and difference (200 kHz). Multiplying by $\cos(\omega_1 t)$ again would shift the 200 kHz and 400 kHz replicas to $\pm 100, \pm 300, \pm 300, \pm 500$ kHz — none of which lands at baseband.

> [!example] **Cross-check against `304_hw7_sample25.pdf`** ✅ Sample answer: "a demodulation can use either the 200kHz frequency or the 400kHz frequency." Matches.

---

## Problem 2 — TDM-PAM, Minimum Pulse Frequency for 20 Audio Signals

> **Problem 2.** Audio signals, bandlimited to **20 kHz**, are sampled and time-division multiplexed using PAM. What is the minimum frequency of the PAM pulses to enable the simultaneous transmission of **20 audio signals**?

### The concept

This problem chains two ideas: the **sampling theorem** (each audio channel must be sampled at $f_s \geq 2B$ per Nyquist — see [[pulse-amplitude-modulation]]) and **time-division multiplexing** (squeeze $N$ channels + 1 sync into each sample period — see [[time-division-multiplexing]]).

The pulse rate on the wire is **how often a slot starts**. With $N$ channels, you need $N + 1$ slots per frame (the $+1$ is for the **sync slot** so the receiver knows which pulse is channel 1). The frame must repeat at the per-channel sample rate.

### Walkthrough

> [!example] **Step-by-step**
>
> **Step 1 — Find the per-channel sample rate.** Audio bandwidth $B = 20$ kHz $\Rightarrow$ Nyquist requires
>
> $$f_s \geq 2B = 40 \text{ kHz} \qquad \Rightarrow \qquad T_s \leq \frac{1}{40\text{ kHz}} = 25\,\mu\text{s}.$$
>
> Each audio channel must be sampled **at least every $25\,\mu\text{s}$**.
>
> **Step 2 — Count slots per frame.** 20 audio channels + 1 sync slot = **21 slots per frame**.
>
> > [!tip] **Don't forget the sync.** The receiver sees a stream of pulses with no labels. The sync slot — typically a known pattern unique to the framing — is what tells the receiver "this is the start of a new frame, the next pulse is channel 1." Skipping it makes the receiver unable to de-interleave.
>
> **Step 3 — Compute slot duration.** The 21 slots must fit inside the $25\,\mu\text{s}$ frame:
>
> $$\text{slot duration} = \frac{25\,\mu\text{s}}{21} \approx 1.19\,\mu\text{s}.$$
>
> **Step 4 — Convert to pulse rate.** Pulse rate $=$ $1\,/\,$slot duration:
>
> $$f_{\text{PAM}} = \frac{1}{1.19\,\mu\text{s}} = \frac{21}{25\,\mu\text{s}} = 21 \cdot 40 \text{ kHz} = 840 \text{ kHz}.$$

### Answer

**Minimum PAM pulse frequency: $f_{\text{PAM}} = 840$ kHz.**

Equivalently: 21 pulses per $25\,\mu\text{s}$ frame $\times$ 40,000 frames per second.

> [!warning] **Off-by-one trap.** Tempting wrong answer: $20 \cdot 40 \text{ kHz} = 800$ kHz. That's the bare-minimum pulse rate **assuming you already had perfect framing for free** — i.e., ignoring the sync slot. Always include the sync overhead unless the problem explicitly says "ideal framing."

> [!example] **Cross-check against `304_hw7_sample25.pdf`** ✅ Sample answer: "the PAM pulse should be at most 25/21 us = 1.19 us, or the minimum PAM frequency is 840 kHz." Matches.

---

## Problem 3 — Chopper Amplifier: Sketch Spectra and Derive the Gain

> **Problem 3.** Sketch the frequency-domain representation of the intermediate signals involved in the **Chopper Amplifier** application. If the chopper frequency is **100 kHz**, and the chopper duty cycle is **100D%** (or, its fraction is $D$, a number 0–1), determine the signal amplification as a function of the bandpass amplifier gain $A$ and the duty cycle $D$.

### The concept

Chopper amplifier = "amplify low-frequency / DC signals **without** the $1/f$ noise and op-amp drift that contaminate direct DC amplification". The trick: **shift the signal up to high frequency** with a square-wave chopper, **amplify** in a narrow band where the amplifier is clean, **shift back down** with a second chopper, **lowpass** the leftover junk. Read [[chopper-amplifier]] for the full background; here we work the derivation that produces the gain $G = 2A\sin^2(\pi D)/\pi^2$.

The four signal stages we need to sketch:

```
x(t)  →  [×]  →  x_m(t)  →  [H_BP, gain A]  →  x_bp(t)  →  [×]  →  x_d(t)  →  [H_LP]  →  x_a(t)
          ▲                                                    ▲
          │                                                    │
       s(ω_c·t)                                            s(ω_c·t)
```

### Walkthrough

> [!example] **Step 1 — Fourier transform of the square-wave chopper $s(\omega_c t)$.**
>
> A square wave of period $T = 2\pi/\omega_c$, high for time $T_1 = D \cdot T/2$ per period (so $\omega_c T_1 = \pi D$), has Fourier transform
>
> $$S(j\omega) = \sum_k \frac{2\sin(k\pi D)}{k}\,\delta(\omega - k\omega_c).$$
>
> An impulse train at every harmonic of $\omega_c$, weights determined by $\sin(k\pi D)/k$. Note that for $D = 0.5$, the even-$k$ terms vanish ($\sin(k\pi/2) = 0$ for even $k$).

> [!example] **Step 2 — Modulate up: $x_m(t) = s(\omega_c t)\,x(t)$.**
>
> Multiplication in time = convolution in frequency, divided by $2\pi$:
>
> $$X_m(j\omega) = \frac{1}{2\pi}\,X(j\omega) * S(j\omega) = \sum_k \frac{\sin(k\pi D)}{k\pi}\,X(j(\omega - k\omega_c)).$$
>
> So $X_m$ is **a stack of replicas of $X(j\omega)$** centered at every harmonic $k\omega_c$, each scaled by $\sin(k\pi D)/(k\pi)$.
>
> **Sketch (for $D = 0.5$, schematic):** triangles centered at $0, \pm\omega_c, \pm 2\omega_c, \pm 3\omega_c, \ldots$. The $k = 0$ term has amplitude proportional to $\sin(0)/0 \to D$ (use l'Hôpital, or note the DC component is just $D \cdot X(j\omega)$ — there's also some careful bookkeeping about the DC term that the HW7 sample skirts). The $k = \pm 1$ blocks dominate at $1/\pi$.

> [!example] **Step 3 — Bandpass-amplify around $\pm\omega_c$.**
>
> The bandpass $H_{\text{BP}}$ is tuned to $\pm\omega_c$ and has gain $A$. It **kills every replica except $k = \pm 1$**:
>
> $$X_{\text{bp}}(j\omega) = A \cdot \frac{\sin(\pi D)}{\pi}\bigl[X(j(\omega - \omega_c)) + X(j(\omega + \omega_c))\bigr]$$
>
> (the $k = +1$ and $k = -1$ contributions have equal weight by parity of $\sin$).
>
> **Sketch:** two scaled, shifted copies of $X(j\omega)$, one at $+\omega_c$, one at $-\omega_c$, each with peak amplitude $A\sin(\pi D)/\pi$. All other replicas are gone.

> [!example] **Step 4 — Modulate down: $x_d(t) = s(\omega_c t)\,x_{\text{bp}}(t)$.**
>
> Convolve again with $S(j\omega)$:
>
> $$X_d(j\omega) = \frac{1}{2\pi}\,X_{\text{bp}}(j\omega) * S(j\omega) = \sum_m \frac{\sin(m\pi D)}{m\pi}\,X_{\text{bp}}(j(\omega - m\omega_c)).$$
>
> For each existing replica at $\pm\omega_c$, the convolution scatters it to all $\pm m\omega_c$ offsets. The two combinations that **land at baseband** ($\omega = 0$):
>
> - $+\omega_c$ shifted by $m = -1 \to 0$
> - $-\omega_c$ shifted by $m = +1 \to 0$
>
> Both contribute $A \cdot [\sin(\pi D)/\pi]^2 \cdot X(j\omega)$. Adding them:
>
> $$X_d(j\omega)\bigr|_{\text{baseband}} = 2A\left[\frac{\sin(\pi D)}{\pi}\right]^2 X(j\omega) \;+\; \sum_{k \neq 0} a_k\,X(j(\omega - k\omega_c)).$$
>
> The $k \neq 0$ terms are byproducts that lie far from baseband and will be killed in step 5.

> [!example] **Step 5 — Lowpass filter $H_{\text{LP}}$ to keep only the baseband copy.**
>
> The LPF cutoff sits well below $\omega_c = 2\pi(100\text{ kHz})$. Result:
>
> $$X_a(j\omega) = \frac{2A\sin^2(\pi D)}{\pi^2}\,X(j\omega).$$

### Answer

**Overall amplifier gain:** $\;G(A, D) = \dfrac{2A\sin^2(\pi D)}{\pi^2}$.

| Duty cycle $D$ | $\sin^2(\pi D)$ | Gain $G(A, D)$ |
|---|---|---|
| $0.1$ | $0.0955$ | $0.0193\,A$ |
| $0.25$ | $0.5$ | $0.101\,A$ |
| $0.5$ | $1$ | $0.203\,A$ *(peak)* |
| $0.75$ | $0.5$ | $0.101\,A$ |
| $0.9$ | $0.0955$ | $0.0193\,A$ |

The peak is at $D = 0.5$ (50% duty), giving $G = 2A/\pi^2 \approx 0.20\,A$. So even at the optimal duty, the chopper architecture loses about a factor of 5 of gain compared to a hypothetical direct DC amplifier of gain $A$ — the trade you make to escape low-frequency noise.

> [!example] **Cross-check against `304_hw7_sample25.pdf`** ✅ Sample answer: "the requested amplifier gain function is $2A\sin^2(\pi D)/\pi^2$." Matches. The sample also includes a pictorial spectrum sketch for $D = 0.5$ worth re-drawing in your submission — see Page 2 of the sample for the layout.

### What to draw for the spectrum sketches

A complete Problem 3 submission needs **four spectrum sketches** (per the sample's pictorial answer). Use $D = 0.5$ for concreteness:

| Stage | Sketch contents |
|---|---|
| $X(j\omega)$ | one triangle at baseband, peak amplitude $1$, half-width $\omega_M$ (the max message frequency) |
| $X_m(j\omega)$ | triangles at $0, \pm\omega_c, \pm 2\omega_c, \pm 3\omega_c, \ldots$ (every harmonic), peak amplitudes scaled by $\sin(k\pi D)/(k\pi)$ — for $D = 0.5$ the $k = \pm 1$ peaks have height $1/\pi$ and the even-$k$ peaks are zero |
| $X_{\text{bp}}(j\omega)$ | only the two triangles at $\pm\omega_c$, peak amplitude $A/\pi$ each (everything else removed by the bandpass) |
| $X_d(j\omega)$ (after second chop) | a baseband triangle of amplitude $2A/\pi^2$ plus residual triangles at $\pm\omega_c, \pm 2\omega_c, \ldots$ (which the final LPF will kill) |
| $X_a(j\omega)$ (after LPF) | one triangle at baseband, amplitude $2A/\pi^2$ (i.e., $2A\sin^2(\pi D)/\pi^2$ with $D = 0.5$) |

> [!tip] **Pro tip for the sketches.** Don't try to plot exact harmonics ad-infinitum — show the first 2–3 on each side and label them; use ellipses for the rest. The grader wants to see you understand which $k$ values survive each block, not a perfectly proportioned sinc envelope.

---

## Cross-references

- [[amplitude-modulation]] — the modulation property used in Problem 1's cascade and Problem 3's chopper
- [[pulse-amplitude-modulation]] — Problem 2's PAM piece
- [[time-division-multiplexing]] — Problem 2's TDM piece
- [[chopper-amplifier]] — Problem 3's full background
- [[butterworth-filter]] — concrete LPF/BPF design used in lab counterparts
- [[homework-2026-04-26-eee-304-hw7]] — source summary (catalog entry)
- [[eee-304]] — course page

## Report template (copy-paste skeleton)

```
EEE 304 HW7
Name: Jayden Le      Date: 2026-04-30 (or whenever it's due)

Problem 1.
   Cascade of two carriers (100 kHz, then 300 kHz) creates spectral
   replicas of X(jω) at ±200 kHz and ±400 kHz. Either of these is a
   valid demodulation frequency.
   ANSWER: 200 kHz or 400 kHz.

Problem 2.
   Per-channel Nyquist rate: 2 × 20 kHz = 40 kHz → T_s = 25 μs.
   With 20 channels + 1 sync slot = 21 slots per frame:
       slot duration = 25 μs / 21 ≈ 1.19 μs
       pulse rate    = 21 × 40 kHz = 840 kHz.
   ANSWER: 840 kHz.

Problem 3.
   Step 1: S(jω) = Σ_k [2 sin(kπD) / k] · δ(ω − k ω_c)
   Step 2: X_m   = Σ_k [sin(kπD)/(kπ)] · X(ω − k ω_c)
   Step 3: X_bp  = A · [sin(πD)/π] · [X(ω − ω_c) + X(ω + ω_c)]
   Step 4: X_d (baseband) = 2A · [sin(πD)/π]² · X(jω) + (kicked-aside terms)
   Step 5: X_a   = (2A sin²(πD) / π²) · X(jω)
   ANSWER: G = 2A·sin²(πD) / π². Peak at D=0.5 → G_max = 2A/π².
   [+ five spectrum sketches as in the table above]
```

> [!note] **About the report template above.** It's intentionally written in plain ASCII (Greek letters as Unicode, no `$...$`) — it's a skeleton for you to copy into a Word doc / handwritten submission, not a wiki page. The wiki body above renders the same equations in proper LaTeX.
