---
title: EEE 404 Exam 2 — Study Guide & Cheat Sheet Skeleton
type: walkthrough
course:
  - "[[eee-404]]"
tags: [eee-404, exam, study-guide, formula-sheet, cheat-sheet, mlp, dtft, dft, fft, z-transform, windowing]
sources:
  - "[[summary-eee-404-exam-2-review]]"
created: 2026-04-29
updated: 2026-05-06
---

# EEE 404 Exam 2 — Study Guide

> [!note] **What this is.** A topic-by-topic study guide for Exam 2 (Thursday 2026-04-30). The exam allows **one 8.5×11 sheet** — this page is the source-of-truth list of equations and topics to put on it. Skim the topic checklist first; then drill the formulas; then do the [[eee-404-exam-2-walkthrough|practice walkthrough]].
>
> **Companion:** [[eee-404-exam-2-walkthrough]] — every practice problem solved with derivations.

> [!tip] **The 4 buckets and what's in each.** Every exam question fits in one of these. Spend ~25% of your prep time on each.

| Bucket | Module | What you'll be asked | Walkthrough section |
|---|---|---|---|
| **MLP feed-forward** | M6 | Compute neuron / network outputs given weights, biases, activation | P1 |
| **Z-transform / difference equations / block diagrams** | M7 + M8 | $H(z) \leftrightarrow y[n]$ ; ROC ; FIR vs IIR ; DF-I/DF-II/cascade/parallel | P2 |
| **Sampling / DFT / FFT sizing / multiplication count / resolution** | M7 + M10 | Pick formula from $\{T \cdot f_s,\ 2 f_s/L,\ N^2,\ f_s/N\}$ | P3 |
| **FFT butterfly + IFFT-via-FFT** | M10 | Draw 4-pt or 8-pt DIT flow ; bit-reverse input ; recover $x[n]$ from $X[k]$ | P4 |

---

## §1 — MLP Neural Networks (Module 6)

### Topic checklist

- [x] **Neuron model:** weighted sum, bias, activation function
- [x] **Activation functions:** ReLU, sigmoid, tanh, identity (linear output layer)
- [x] **Forward propagation** through hidden + output layers
- [x] **Layer-by-layer evaluation** (don't skip layers)
- [x] **Training basics** (backprop, gradient descent — high-level only; the EC lab goes deeper)
- [x] **Network topology** notation: $[n_{\text{in}}, n_{\text{hidden}}, n_{\text{out}}]$
- [x] **Counting parameters:** weights + biases for an MLP

### Equations to memorise

**Single neuron forward pass** (the master formula — everything else is just plugging in):
$$\text{out} = f\!\left(\sum_{j=1}^{N_{\text{in}}} w_j \cdot x_j + b\right)$$

**Activations:**
$$\text{ReLU}(y) = \max(0, y)$$
$$\sigma(y) = \frac{1}{1 + e^{-y}} \quad\text{(sigmoid; smooth 0–1)}$$
$$\tanh(y) = \frac{e^y - e^{-y}}{e^y + e^{-y}} \quad\text{(smooth −1 to +1)}$$

**Network forward pass (vector form):**
$$\vec{H} = f_{\text{hidden}}(W^{(1)} \vec{X} + \vec{b}^{(1)})$$
$$\vec{Y} = f_{\text{out}}(W^{(2)} \vec{H} + \vec{b}^{(2)})$$

**Parameter count for a 1-hidden-layer MLP** with topology $[N_i, N_h, N_o]$:
$$\#\text{weights} = N_i \cdot N_h + N_h \cdot N_o, \quad \#\text{biases} = N_h + N_o$$

> [!warning] **The trap on every MLP exam problem.** Pre-activation negative + ReLU activation → output is **0**, not the negative number. Triple-check signs before writing the answer.

---

## §2 — DTFT and DFT (Module 7)

### Topic checklist

- [x] **DTFT definition** for an aperiodic discrete signal (continuous in $\omega$, $2\pi$-periodic)
- [x] **DFT definition** as $N$ uniformly-spaced samples of the DTFT around the unit circle
- [x] **Sampling in frequency domain** ↔ periodic extension in time
- [x] **Condition to avoid time-aliasing in DFT**: $N \geq L$
- [x] **DFT of $x[n]$ of length $L$** with various $N$ (zero-padding interpolates the DTFT)
- [x] **DFT properties** (linearity, time shift, frequency shift, Parseval, convolution, conjugate symmetry for real signals)

### Equations to memorise

**DTFT (analysis):**
$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]\,e^{-j\omega n}$$
**DTFT (synthesis):**
$$x[n] = \frac{1}{2\pi}\int_{-\pi}^{\pi} X(e^{j\omega})\,e^{j\omega n}\,d\omega$$

**DFT (analysis):**
$$X[k] = \sum_{n=0}^{N-1} x[n]\,e^{-j 2\pi k n / N},\quad k = 0, 1, \dots, N-1$$
**IDFT (synthesis):**
$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k]\,e^{+j 2\pi k n / N},\quad n = 0, 1, \dots, N-1$$

**Twiddle factor:** $W_N = e^{-j 2\pi/N}$. So $X[k] = \sum_n x[n] W_N^{kn}$.

**Conjugate symmetry (real $x[n]$):** $X[N - k] = X^*[k]$, so $X[0]$ and $X[N/2]$ are real, and only $X[0\,..\,N/2]$ are independent.

**DFT properties (the most-likely-to-appear ones):**

| Property                  | Formula                                                         |      |                        |      |     |
| ------------------------- | --------------------------------------------------------------- | ---- | ---------------------- | ---- | --- |
| Linearity                 | $\alpha x_1 + \beta x_2 \leftrightarrow \alpha X_1 + \beta X_2$ |      |                        |      |     |
| Time shift (circular)     | $x[(n - n_0)_N] \leftrightarrow X[k] e^{-j 2\pi k n_0 / N}$     |      |                        |      |     |
| Frequency shift           | $x[n] e^{j 2\pi k_0 n / N} \leftrightarrow X[(k - k_0)_N]$      |      |                        |      |     |
| Circular convolution      | $x_1 \circledast x_2 \leftrightarrow X_1[k] X_2[k]$             |      |                        |      |     |
| Parseval                  | $\sum_n                                                         | x[n] | ^2 = \frac{1}{N}\sum_k | X[k] | ^2$ |
| Conjugate symmetry (real) | $X[N - k] = X^*[k]$                                             |      |                        |      |     |

> [!warning] **Sampling-in-freq aliasing.** Sampling $X(e^{j\omega})$ at $N$ points (= the DFT) corresponds to **periodic extension** of $x[n]$ with period $N$ in time. If $L > N$, periods overlap = **time aliasing** = bad reconstruction. Always $N \geq L$.

---

## §3 — Z-Transform (Module 7)

### Topic checklist

- [x] **Z-transform definition**, **inverse Z-transform** (concept; not usually computed by integral)
- [x] **Region of convergence (ROC)** — causal: $|z| > r_{\max}$ ; anti-causal: $|z| < r_{\min}$ ; two-sided: annulus
- [x] **Pole-zero plot** — × for poles, ○ for zeros
- [x] **Stability:** ROC includes the unit circle ⟺ DTFT exists
- [x] **Causal stable:** all poles **inside** the unit circle
- [x] **Time-shift property** (the workhorse for converting $H(z)$ to difference equations)
- [x] **Difference equation ↔ $H(z)$ ↔ block diagram** (round trip)

### Equations to memorise

**Z-transform definition:**
$$X(z) = \sum_{n=-\infty}^{\infty} x[n]\,z^{-n}$$

**Time shift (the property you'll use 90% of the time):**
$$x[n - n_0]\ \leftrightarrow\ z^{-n_0} X(z)$$

**Transfer function from difference equation.** Given
$$\sum_{k=0}^{N} a_k\,y[n - k] = \sum_{k=0}^{M} b_k\,x[n - k]$$
(with $a_0 = 1$ by convention), the transfer function is
$$H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_{k=0}^{M} b_k z^{-k}}{1 + \sum_{k=1}^{N} a_k z^{-k}}.$$

**ROC rules table:**

| Sequence type            | ROC                                           |     |                                        |
| ------------------------ | --------------------------------------------- | --- | -------------------------------------- |
| Right-sided / causal     | $\{                                           | z   | > r_{\max}\}$ (outside outermost pole) |
| Left-sided / anti-causal | $\{                                           | z   | < r_{\min}\}$ (inside innermost pole)  |
| Two-sided                | annulus between two pole rings                |     |                                        |
| **DTFT exists**          | ROC includes the unit circle $                | z   | = 1$                                   |
| **Causal AND stable**    | all poles **strictly inside** the unit circle |     |                                        |

> [!tip] **Causal+stable rule of thumb:** every pole at $|z| < 1$ ✓. Even one pole at $|z| \geq 1$ → unstable causal system.

---

## §4 — Difference Equations & Block Diagrams (Modules 7 + 8)

### Topic checklist

- [x] **Calculate impulse response** $h[n]$ given a difference equation (set $x[n] = \delta[n]$ and iterate)
- [x] **Calculate output** $y[n]$ given input and difference equation (iterate, or convolve)
- [x] **FIR vs IIR** classification by inspecting the difference equation / $H(z)$ denominator
- [x] **Direct Form I, Direct Form II, Transposed DF-II, Cascade, Parallel** — sketch each
- [x] **Number of storage (delay) elements** for each form
- [x] **When to use cascade vs parallel** (for numerical stability or fixed-point implementation)

### FIR vs IIR (the easy classifier)

- **FIR:** $H(z)$ has only $z^{-k}$ terms in the **numerator** (denominator is constant). $y[n]$ depends only on **inputs**. Impulse response has finite length.
- **IIR:** $H(z)$ denominator has $z^{-k}$ terms ($k \geq 1$). $y[n]$ depends on **past outputs** (feedback). Impulse response can be infinite.

### Block-diagram comparison (memorise)

| Form | Storage elements | Notes |
|---|---|---|
| **Direct Form I** | $M + N$ | Two delay lines (FF then FB). Simple. |
| **Direct Form II** | $\max(M, N)$ | Shared delay line — IIR (poles) first, then FIR (zeros). |
| **Transposed DF-II** | $\max(M, N)$ | Reverse all DF-II arrows. Often better numerical behavior. |
| **Cascade** | $\sum 2$ per biquad | Series of 2nd-order sections. Good for fixed-point. |
| **Parallel** | $\sum 2$ per biquad | Sum of 2nd-order sections (after partial fractions). |

For a system with $M$ feedforward taps and $N$ feedback taps, $\max(M, N)$ is the **minimum** required storage; DF-II achieves it.

### How to derive the difference equation from $H(z)$ (template)

1. **Cross multiply** $H(z) = Y(z)/X(z)$.
2. **Expand** so all $Y(z)$ terms are on the LHS, all $X(z)$ on the RHS.
3. **Apply $z^{-l} \leftrightarrow x[n-l]$.**
4. **Solve for $y[n]$** (move all $y[n-l]$ for $l \geq 1$ to the RHS — flip sign).

Example (from Exam 2 Practice Problem 2): $H(z) = \dfrac{1 + 3 z^{-1}}{1 + \tfrac{3}{10} z^{-1} - \tfrac{1}{10} z^{-2}}$ →
$$y[n] = x[n] + 3 x[n-1] - \tfrac{3}{10} y[n-1] + \tfrac{1}{10} y[n-2].$$

> [!tip] **Sketching DF-II from a difference equation in 30 seconds.**
> 1. Take the difference equation in standard form (everything on RHS): $y[n] = \sum b_k x[n-k] - \sum a_k y[n-k]$.
> 2. Draw a **single vertical delay chain** of length $\max(M, N)$ on the left (each box = $z^{-1}$).
> 3. Tap each delay node with weight $b_k$ to a **summing junction** on the right → that's $y[n]$.
> 4. Tap each delay node with weight $-a_k$ back to the **input summing junction** at the top of the delay chain.
> 5. Done. You've drawn DF-II.

---

## §5 — FFT (Module 10)

### Topic checklist

- [x] **DFT direct computation:** $N^2$ complex mults
- [x] **FFT (radix-2 DIT):** $\frac{N}{2}\log_2 N$ butterflies, $\sim 2 N \log_2 N$ real mults
- [x] **Decimation-in-time** (DIT) — split by even/odd indices
- [x] **Butterfly structure** — sum + difference with twiddle scaling
- [x] **Bit-reversed input order** for DIT FFT
- [x] **4-point and 8-point flow graphs** (be able to draw from memory)
- [x] **IDFT via FFT** — conjugate-FFT-conjugate-divide trick
- [x] **FFT for real-valued signal** — $N$-point real signal → $\frac{N}{2}$-point complex FFT

### Equations to memorise

**Direct DFT cost:**
$$\text{CMULT} = N^2 \quad ; \quad \text{RMULT} = 4 N^2$$

**Radix-2 FFT cost:**
$$\text{stages} = \log_2 N$$
$$\text{butterflies} = \frac{N}{2}\log_2 N$$
$$\text{RMULT} \approx 2 N \log_2 N$$

**Speedup:** $\dfrac{4 N^2}{2 N \log_2 N} = \dfrac{2N}{\log_2 N}$. At $N = 1024$: **~205× faster**.

**Twiddle factor relations** (the symmetries the FFT exploits):
$$W_N^{k + N/2} = -W_N^k, \quad W_N^{k+N} = W_N^k, \quad W_N^{2k} = W_{N/2}^k$$

**IDFT-via-FFT (memorise this 4-step recipe):**
1. Take complex conjugate: $X^*[k]$.
2. Run forward FFT: $\text{FFT}(X^*[k])$.
3. **Divide by $N$.**
4. Take complex conjugate again.

The result is $x[n]$.

**For real-valued signal $N$-point FFT:**
- Treat samples as alternating real/imag of an $\frac{N}{2}$-point complex sequence.
- Run an $\frac{N}{2}$-point FFT.
- Apply post-processing (one extra butterfly stage) to recover the $N$-point spectrum.
- Total cost: $\frac{N}{2}\log_2 \frac{N}{2}$ complex butterflies + $\frac{N}{2}$ post-processing butterflies.

### Counting cheat-sheet (must-have on the cheat sheet)

| $N$ | $\log_2 N$ | Butterflies | Real mults |
|---|---|---|---|
| 4 | 2 | 4 | 16 |
| 8 | 3 | 12 | 48 |
| 16 | 4 | 32 | 128 |
| 32 | 5 | 80 | 320 |
| 64 | 6 | 192 | 768 |
| 128 | 7 | 448 | 1792 |
| 256 | 8 | 1024 | 4096 |
| 512 | 9 | 2304 | 9216 |
| 1024 | 10 | 5120 | 20480 |

### Bit-reverse permutation table

$$N = 4: \{0, 1, 2, 3\} \rightarrow \{0, 2, 1, 3\}$$
$$N = 8: \{0, 1, 2, 3, 4, 5, 6, 7\} \rightarrow \{0, 4, 2, 6, 1, 5, 3, 7\}$$

(Reverse the binary representation of each index. For $N=8$ that means 3-bit reversal: 001 → 100, 010 → 010, 011 → 110, etc.)

---

## §6 — Time-Frequency Analysis & Windowing (Module 11)

### Topic checklist

- [x] **Why windowing exists** — finite segments cause spectral leakage
- [x] **Spectral leakage** — energy spread into adjacent bins because the implied window has finite duration
- [x] **Window functions** — rectangular, Hamming, Hann, Bartlett (maybe Blackman)
- [x] **Main-lobe width** vs **side-lobe height** trade-off
- [x] **Time-frequency resolution trade-off** (longer $L$ = better freq resolution, but worse time localisation)
- [x] **Frequency resolution** $\Delta f = f_s / N$
- [x] **DFT/FFT implementation considerations** — picking $N, L$, window type
- [x] **Minimum $L$ to resolve close-by frequencies** $|f_1 - f_2| > \text{(window's main-lobe width in Hz)}$

### Window comparison cheat sheet (PUT THIS ON YOUR 8.5×11)

| Window | Main-lobe width (rad/sample) | Main-lobe width (Hz) | Peak side-lobe (dB) | When to use |
|---|---|---|---|---|
| Rectangular | $4\pi/L$ | $2 f_s / L$ | −13 dB | Best resolution, worst leakage |
| Bartlett (triangular) | $8\pi/L$ | $4 f_s / L$ | −25 dB | OK middle ground |
| Hann | $8\pi/L$ | $4 f_s / L$ | −31 dB | General-purpose smooth |
| Hamming | $8\pi/L$ | $4 f_s / L$ | −41 dB | Better side-lobe than Hann |
| Blackman | $12\pi/L$ | $6 f_s / L$ | −58 dB | When side-lobes must be tiny |

**Conversion formula** (rad/sample → Hz): $f = \omega \cdot f_s / (2\pi)$. So $4\pi/L$ rad/sample → $(4\pi/L) \cdot (f_s/2\pi) = 2 f_s / L$ Hz.

### Resolution vs binning vs leakage — three different things

| Concept | Set by | Formula |
|---|---|---|
| **Frequency resolution (windowing)** | $L$ + window choice | rect: $2 f_s/L$ Hz ; Hamming/Hann: $4 f_s/L$ Hz |
| **Bin spacing (binning)** | $N$ | $f_s/N$ Hz |
| **Spectral leakage** | window type | side-lobe height (dB) |

> [!warning] **Don't confuse them.** Zero-padding (increasing $N$ without increasing $L$) **does not** improve resolution — it just gives you a finer-grained look at the same blurry spectrum.

### Implementation flowchart for "design a DFT/FFT to resolve two tones"

1. **Resolution requirement:** need $|f_1 - f_2| >$ (window main-lobe width in Hz).
2. **Solve for minimum $L$** given window type. E.g., to resolve 40 Hz with a Hamming window at $f_s = 800$ Hz: $4 f_s / L < 40 \Rightarrow L > 80$.
3. **Pick FFT size $N$:** smallest power of 2 with $N \geq L$.
4. **Confirm bin resolution** $f_s / N$ is fine enough to distinguish $f_1, f_2$ in different bins.

---

## §7 — Master Equation Sheet (the one you copy onto 8.5×11)

> [!tip] **Suggested layout for your one-page cheat sheet.** Three columns. Left = MLP + Z-transform + DF table. Middle = DFT/IDFT/DTFT + properties + butterfly counts. Right = sampling/resolution + window comparison + the four "always-on" formulas.

### MLP (top of left column)
- $\text{out} = f(\sum w_j x_j + b)$
- $\text{ReLU}(y) = \max(0, y)$
- $\sigma(y) = 1/(1 + e^{-y})$
- $\tanh(y) = (e^y - e^{-y})/(e^y + e^{-y})$
- Param count: $N_i N_h + N_h N_o$ weights, $N_h + N_o$ biases.

### Z-transform (middle of left column)
- $X(z) = \sum x[n] z^{-n}$
- $x[n - n_0] \leftrightarrow z^{-n_0} X(z)$
- $H(z) = \frac{\sum b_k z^{-k}}{1 + \sum a_k z^{-k}}$
- ROC causal: $|z| > r_{\max}$
- DTFT exists ⟺ ROC ⊃ unit circle
- Causal stable ⟺ all poles inside unit circle

### Block diagrams (bottom of left column)
| Form | Storage |
|---|---|
| DF-I | $M + N$ |
| DF-II | $\max(M, N)$ |
| Transposed DF-II | $\max(M, N)$ |
| Cascade / Parallel | $\sum 2$ per biquad |

### DFT / DTFT (top of middle column)
- $X[k] = \sum_{n=0}^{N-1} x[n] e^{-j 2\pi kn/N}$
- $x[n] = \tfrac{1}{N}\sum_k X[k] e^{+j 2\pi kn/N}$
- $W_N = e^{-j 2\pi/N}$
- $X(e^{j\omega}) = \sum_n x[n] e^{-j\omega n}$
- Real $x[n]$: $X[N-k] = X^*[k]$
- Linearity: $\alpha x_1 + \beta x_2 \leftrightarrow \alpha X_1 + \beta X_2$
- Time shift: $x[(n - n_0)_N] \leftrightarrow e^{-j 2\pi k n_0/N} X[k]$
- Circular conv: $x_1 \circledast x_2 \leftrightarrow X_1 X_2$
- Parseval: $\sum |x[n]|^2 = \tfrac{1}{N}\sum |X[k]|^2$

### FFT (middle of middle column)
- Butterflies: $\frac{N}{2}\log_2 N$
- Stages: $\log_2 N$
- Real mults: $2 N \log_2 N$
- Direct DFT: $N^2$ complex = $4 N^2$ real
- $W_N^{k+N/2} = -W_N^k$
- $W_N^{2k} = W_{N/2}^k$

### IDFT-via-FFT (bottom of middle column)
1. Conjugate $X[k] \to X^*[k]$.
2. Run forward FFT.
3. **Divide by $N$.**
4. Conjugate.

### Bit-reverse for $N = 4$ and $N = 8$ (with butterfly diagrams sketched freehand)

### Sampling + resolution (top of right column)
- $L = T \cdot f_s$
- $\Delta f = f_s/N$ (binning)
- Rect window resolution: $2 f_s / L$ Hz
- Hamming/Hann resolution: $4 f_s / L$ Hz
- $N \geq L$ for DFT
- $N$ must be power of 2 for radix-2 FFT

### Window comparison table (bottom of right column)
- See §6 above — copy verbatim.

### The 4 always-on formulas (right margin, prominent)
1. $L = T \cdot f_s$
2. $\Delta f = f_s / N$
3. Direct DFT cost = $4 N^2$ real mults
4. FFT cost = $2 N \log_2 N$ real mults

---

## §8 — Pre-exam study plan (recommended, T−1 days)

> [!example] **Wednesday night** (the night before): re-do all 4 practice problems freehand without looking at the answer key. Time yourself — Dr. Wang's exam is roughly the same size, so 4 problems in ~120 minutes = 30 min per problem.

> [!example] **Thursday morning of**: re-derive the IDFT-via-FFT trick on scratch paper, sketch a 4-pt butterfly with bit-reverse from memory, recite the four "always-on" formulas. That's it.

### Practice problem suggestions outside the practice exam

- **From HW3** (NN): a different topology, maybe a sigmoid output. Re-do it.
- **From HW4** (FFT/DFT properties): the linearity / time-shift / circular conv questions.
- **From HW5** (the one I [[eee-404-hw5-walkthrough|walked through]]): two-tone DTFT, Hamming windowing, FFT compute budget. Re-attempt the 4 problems and check against the walkthrough.

> [!tip] **Common pitfalls flagged from the practice exam answer key.**
> 1. **MLP P1 — output Y₂ is 0 due to ReLU on negative.** Don't write $-0.049$.
> 2. **Z-transform P2 — DTFT exists requires ROC ⊃ unit circle.** That's why ROC is $|z| > 1/2$, not "outside outermost pole" alone.
> 3. **Sampling P3(b) — main-lobe width converted to Hz.** The exam says "rectangular window," not "Hamming," so use $2 f_s / L$, not $4 f_s / L$.
> 4. **Sampling P3(d) — real vs. complex multiplication count.** Direct DFT = $N^2$ complex = $4 N^2$ real. The answer key reports both.
> 5. **FFT P4 — bit-reversed input order $\{x[0], x[2], x[1], x[3]\}$.** Drawing $\{x[0], x[1], x[2], x[3]\}$ in natural order is wrong.
> 6. **IFFT P4(d) — divide by $N$.** Easy to forget after running the FFT on conjugated values.

---

## See also

- [[eee-404-exam-2-walkthrough]] — every practice problem solved with derivations
- [[eee-404]] — course page (master roadmap of FFT module + new modules)
- [[eee-404-hw5-walkthrough]] — already-walked-through HW5 (DTFT, Hamming, FFT compute budget)
- [[mlp]], [[neuron]], [[relu]], [[forward-propagation]] — neural networks (Module 6)
- [[dtft]], [[dft]], [[idft]], [[dft-properties]] — Fourier basics (Module 7)
- [[z-transform]], [[region-of-convergence]], [[direct-form-i]], [[direct-form-ii]], [[fir-vs-iir]] — Z-transform mechanics
- [[fft]], [[butterfly]], [[bit-reversed-order]], [[twiddle-factor]], [[real-valued-fft]] — FFT mechanics
- [[window-function]], [[rectangular-window]], [[hamming-window]], [[hann-window]], [[bartlett-window]], [[spectral-leakage]], [[window-resolution-criterion]], [[frequency-resolution]] — Module 11
