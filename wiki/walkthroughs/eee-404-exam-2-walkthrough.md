---
title: EEE 404 Exam 2 — Practice Exam Walkthrough
type: example
course: [[eee-404]]
tags: [eee-404, exam, walkthrough, mlp, dtft, dft, fft, z-transform, difference-equation, butterfly, windowing]
sources: [[summary-eee-404-exam-2-review]]
created: 2026-04-29
updated: 2026-04-29
---

# EEE 404 Exam 2 — Practice Exam Walkthrough

> [!note] **What this is.** A per-problem walkthrough of the **Exam 2 Practice Exam** that Dr. Wang posted on Canvas (`raw/other/eee-404-exam-2-review.pdf`). For every problem I (a) **state it** verbatim, (b) **explain the overarching concept** so you understand what's being tested, (c) give the **headline answer** in a bold lead line, and (d) provide a **collapsible "📐 Show derivation" callout** so the deep algebra doesn't crowd the page.
>
> **Companion page:** [[eee-404-exam-2-study-guide]] — the formula sheet and topic checklist organised by topic. Use the walkthrough to *learn the methods*, the study guide to *plan your 8.5×11 cheat sheet*.

> [!tip] **How to use this on exam day.** The exam is **closed-book except one 8.5×11 sheet**. Calculator allowed. 150 pts total. Walk through every problem here at least twice — once to follow the logic, once trying to predict each step before reading it. The four practice problems map almost 1:1 onto the four conceptual buckets the exam tests.

> [!warning] **Modules covered.** Module 6 (Multi-Layer Perceptron NN), Module 7 (DTFT, DFT, Z-transform, block diagrams, difference equations), Module 10 (FFT), Module 11 (windowing, time-frequency analysis). HW3, HW4, HW5 are fair game — see [[homework-2026-04-27-eee-404-hw5]] for HW5 already-walked-through.

---

## Problem 1 — Multi-Layer Perceptron Forward Pass

> **Setup.** A 2-input, 1-hidden-layer (2 neurons), 2-output MLP with **ReLU** activation $f(y) = \max(0, y)$ in both hidden and output layers.
>
> **Weights and biases (from the diagram):**
> - Input → Hidden: $w_{I_1 H_1} = 0.1$, $w_{I_1 H_2} = 0.2$, $w_{I_2 H_1} = 0.3$, $w_{I_2 H_2} = 0.4$. Biases $b_{H_1} = 0.15$, $b_{H_2} = 0.25$.
> - Hidden → Output: $w_{H_1 O_1} = 0.5$, $w_{H_1 O_2} = 0.6$, $w_{H_2 O_1} = 0.7$, $w_{H_2 O_2} = 0.8$. Biases $b_{O_1} = 0.3$, $b_{O_2} = -0.4$.
>
> **Inputs:** $X_1 = 0.05,\ X_2 = 0.1$. Find $H_1, H_2, Y_1, Y_2$.

### The concept

**Forward propagation** in an MLP. Every neuron does the same three-step thing:

1. **Weighted sum** of all inputs feeding into it: $z = \sum_j w_j x_j$.
2. **Add the bias**: $z + b$.
3. **Apply the activation**: $\text{out} = f(z + b)$.

The whole network is just this three-step recipe layered. **Layer-by-layer**, never skip ahead — the hidden-layer outputs are the inputs to the output layer. See [[mlp]] and [[neuron]].

> [!tip] **ReLU is your friend on exam day.** $f(y) = \max(0, y)$. If $y \geq 0$ output is $y$; if $y < 0$ output is $0$. No sigmoid algebra, no exponentials. **Catch all negative pre-activations and write 0.**

### Headline answers

**$H_1 = 0.185$, $H_2 = 0.3$, $Y_1 = 0.6025$, $Y_2 = 0$.**

The "trap" answer is $Y_2$ — its pre-activation is **negative** ($-0.049$), so ReLU clamps it to $0$. Forgetting that costs you the easiest gimme on the page.

> [!info]- 📐 Show derivation — neuron-by-neuron forward pass
>
> **Hidden neuron $H_1$:**
> $$z_{H_1} = w_{I_1 H_1} X_1 + w_{I_2 H_1} X_2 + b_{H_1} = (0.1)(0.05) + (0.3)(0.1) + 0.15$$
> $$= 0.005 + 0.03 + 0.15 = 0.185$$
> $$H_1 = \text{ReLU}(0.185) = 0.185 \quad (\geq 0, \text{ pass through})$$
>
> **Hidden neuron $H_2$:**
> $$z_{H_2} = (0.2)(0.05) + (0.4)(0.1) + 0.25 = 0.01 + 0.04 + 0.25 = 0.30$$
> $$H_2 = \text{ReLU}(0.30) = 0.30$$
>
> **Output neuron $Y_1$:** (note: now the inputs are the hidden-layer outputs $H_1, H_2$)
> $$z_{Y_1} = w_{H_1 O_1} H_1 + w_{H_2 O_1} H_2 + b_{O_1} = (0.5)(0.185) + (0.7)(0.30) + 0.3$$
> $$= 0.0925 + 0.21 + 0.3 = 0.6025$$
> $$Y_1 = \text{ReLU}(0.6025) = 0.6025$$
>
> **Output neuron $Y_2$:**
> $$z_{Y_2} = (0.6)(0.185) + (0.8)(0.30) + (-0.4) = 0.111 + 0.24 - 0.4 = -0.049$$
> $$Y_2 = \text{ReLU}(-0.049) = \mathbf{0}$$
>
> **The bias $-0.4$ pulled $z_{Y_2}$ negative**, so ReLU zeroes it. This is the test of whether you actually understand ReLU vs. just regurgitating $\max$.

> [!warning] **Where students lose points.** (1) **Wrong weight indexing** — re-read which weight goes from which neuron *to* which neuron; the convention in the diagram is "weight on the wire feeding into the right-side neuron." (2) **Forgetting bias.** Each neuron has its own bias. (3) **Forgetting to apply activation** — the assignment frequently asks for $H_1, H_2$ as the *post-activation* values. (4) **Negative pre-activation** silently passing through as a real number — always check the sign before writing the answer.

### Why it matters / what to study

This is **forward propagation only** (no training, no backprop). The exam may give you:
- A different number of inputs / hidden neurons / outputs (e.g., 3-9-6 like the EC lab).
- Different activations: **ReLU**, **sigmoid** $\sigma(y) = 1/(1+e^{-y})$, or **tanh**. Practice each.
- A "vector form" presentation $\vec{H} = f(W\vec{X} + \vec{b})$ rather than scalar wire-by-wire — it's the same math.

**Cheat-sheet items:** ReLU formula, sigmoid formula, tanh formula, the per-neuron forward equation $\text{out} = f(\sum w_j x_j + b)$.

---

## Problem 2 — Z-Transform → ROC, Difference Equation, FIR/IIR, Direct Form II

> **Setup.** LTI system with transfer function
> $$H(z) = \frac{1 + 3z^{-1}}{1 + \tfrac{3}{10} z^{-1} - \tfrac{1}{10} z^{-2}}.$$
>
> **(a)** If the Fourier transform of $h[n]$ exists, sketch the pole-zero plot and shade the ROC.
> **(b)** Express the input–output relationship as a difference equation.
> **(c)** FIR or IIR? Why?
> **(d)** Sketch the **Direct Form II** signal-flow diagram and report the number of storage elements.

### The concept

Four mini-skills in one problem:

1. **Factor the transfer function** to find poles and zeros.
2. **The DTFT exists iff the unit circle $|z|=1$ lies inside the ROC.** For a causal LTI system, ROC is $|z| > \text{(largest pole magnitude)}$.
3. **Cross-multiply** $H(z) = Y(z)/X(z)$ and use the **time-shift property** $z^{-l} \leftrightarrow x[n-l]$ to recover the difference equation.
4. **Direct Form II** shares the delay line between feedforward and feedback paths — needs **only $\max(M, N)$** delays where $M$ and $N$ are the orders of numerator and denominator. See [[direct-form-ii]] and [[z-transform]].

### Headline answers

**(a) Zeros at $z = 0$ and $z = -3$. Poles at $z = 1/5$ and $z = -1/2$. ROC: $|z| > 1/2$** (largest |pole|, and includes the unit circle so DTFT exists).

**(b) Difference equation:** $\mathbf{y[n] = x[n] + 3x[n-1] - \tfrac{3}{10} y[n-1] + \tfrac{1}{10} y[n-2]}$.

**(c) IIR.** The denominator has $z^{-1}, z^{-2}$ terms → there are **feedback** terms ($y[n-1], y[n-2]$) → impulse response is infinite.

**(d) Direct Form II needs 2 storage elements** (because $\max(M=1, N=2) = 2$).

> [!info]- 📐 Show derivation — (a) Factor $H(z)$ and find ROC
>
> **Step 1 — Multiply num and den by $z^2$** to get a polynomial in $z$:
> $$H(z) = \frac{z^2 + 3z}{z^2 + \tfrac{3}{10} z - \tfrac{1}{10}} = \frac{z(z+3)}{z^2 + \tfrac{3}{10} z - \tfrac{1}{10}}$$
>
> **Step 2 — Factor the denominator.** Use the quadratic formula on $z^2 + 0.3 z - 0.1 = 0$:
> $$z = \frac{-0.3 \pm \sqrt{0.09 + 0.4}}{2} = \frac{-0.3 \pm 0.7}{2} = \{0.2,\ -0.5\} = \{1/5,\ -1/2\}$$
>
> So $H(z) = \dfrac{z(z+3)}{(z - 1/5)(z + 1/2)}$.
>
> **Step 3 — Identify poles and zeros.**
> - **Zeros** (numerator = 0): $z = 0$ and $z = -3$.
> - **Poles** (denominator = 0): $z = 1/5$ and $z = -1/2$.
>
> **Step 4 — ROC for DTFT existence.** A right-sided (causal) sequence has $\text{ROC} = \{|z| > r_{\max}\}$ where $r_{\max}$ is the largest pole magnitude. Here $r_{\max} = \max(1/5,\ 1/2) = 1/2$. The DTFT requires the unit circle inside the ROC, i.e. $1 > 1/2$ ✓.
>
> **Sketch:** mark zeros (×... wait, zeros are ○, poles are ×) — **zeros as O at $z=0$ and $z=-3$**, **poles as × at $z = 1/5$ and $z = -1/2$**, dashed unit circle, shade everything outside the circle of radius $1/2$.

> [!info]- 📐 Show derivation — (b) Difference equation from $H(z)$
>
> **Cross-multiply** $H(z) = Y(z)/X(z)$:
> $$\bigl(1 + \tfrac{3}{10} z^{-1} - \tfrac{1}{10} z^{-2}\bigr) Y(z) = \bigl(1 + 3 z^{-1}\bigr) X(z)$$
>
> **Apply the time-shift property** $z^{-l} X(z) \leftrightarrow x[n-l]$:
> $$y[n] + \tfrac{3}{10} y[n-1] - \tfrac{1}{10} y[n-2] = x[n] + 3 x[n-1]$$
>
> **Solve for $y[n]$** (move feedback to RHS with sign flip):
> $$\boxed{y[n] = x[n] + 3 x[n-1] - \tfrac{3}{10} y[n-1] + \tfrac{1}{10} y[n-2]}$$

> [!info]- 📐 Show derivation — (d) Direct Form II diagram and storage-element count
>
> **Why DF-II shares delays.** Direct Form I implements the feedforward (zero) section first then the feedback (pole) section, using two separate delay lines of lengths $M$ and $N$. Direct Form II reverses the order — it does the **all-pole IIR section first**, producing an intermediate signal $w[n]$, then applies the feedforward FIR section. **Both sections see the same intermediate signal**, so they share the delay line. Total delays = $\max(M, N)$.
>
> **Here:** $M = 1$ (one $x[n-1]$ tap), $N = 2$ (two $y[n-l]$ taps). $\max(1, 2) = \mathbf{2}$ storage elements.
>
> **Diagram (top-to-bottom flow, ASCII):**
>
> ```
>  x[n] ──────►(+)──────────►(+)─────► y[n]
>               ▲              ▲
>               │              │
>          (–3/10)·         3·    
>               │              │
>             [w₁ = w[n−1]] ──┘
>               ▲              ▲
>               │              │
>               │           (no extra delay for x — DF-II only stores w)
>          (+1/10)·         
>               │              
>             [w₂ = w[n−2]]
> ```
>
> Read it as: incoming $x[n]$ adds the two feedback contributions $-\tfrac{3}{10} w[n-1] + \tfrac{1}{10} w[n-2]$ to form $w[n]$. Then $y[n] = w[n] + 3 w[n-1]$. The single delay chain $w[n], w[n-1], w[n-2]$ is shared between feedback and feedforward — that's the magic of DF-II.

### Why it matters / what to study

The exam will rotate the **same skill matrix** through different transfer functions:
- 1st-order vs 2nd-order denominators.
- Real vs complex-conjugate poles.
- Pole-zero cancellation at $z = 0$ (causes "delay" interpretation).
- Maybe a transposed Direct Form II or a cascade form.

**Cheat-sheet items:** Quadratic formula, ROC rules (causal: outside; anti-causal: inside; two-sided: annulus), DF-I vs DF-II vs Transposed-DF-II vs Cascade vs Parallel storage counts, the $z^{-l} \leftrightarrow x[n-l]$ shift property.

> [!warning] **FIR vs IIR: the easy mistake.** FIR = finite impulse response = no feedback = $y[n]$ depends only on present and past **inputs** $x[n], x[n-1], \dots$ IIR has feedback (depends on past **outputs** too). Look at the **denominator of $H(z)$** — if it's just $1$ (or a constant), the system is FIR. If it has $z^{-1}$ or higher terms, it's IIR. Don't be fooled by a fancy numerator.

### Block-diagram cheatsheet you should know cold

| Form | Storage elements | Notes |
|---|---|---|
| **Direct Form I** | $M + N$ | Most intuitive; separate feedforward and feedback delay lines |
| **Direct Form II** | $\max(M, N)$ | Shared delay line between feedback (first) and feedforward (second) |
| **Transposed DF-II** | $\max(M, N)$ | Reverse all arrow directions in DF-II; swap nodes ↔ junctions |
| **Cascade** | $\sum 2 \cdot N_{\text{biquad}}$ | Series of 2nd-order sections (biquads) |
| **Parallel** | $\sum 2 \cdot N_{\text{biquad}}$ | Sum of 2nd-order sections (after partial fractions) |

---

## Problem 3 — Sampling, DTFT/DFT/FFT Sizes, Multiplications, Resolution

> **Setup.** A real signal sampled at $f_s = 800$ Hz:
> $$x(t) = \sin(2\pi f_1 t) + \sin(2\pi f_2 t).$$
> $s[n]$ is the **L-point** segment corresponding to **50 ms** of $x(t)$.
>
> **(a)** What is $L$?
> **(b)** What condition on $f_1, f_2$ for them to be detected from $S(e^{j\omega})$ (the DTFT)?
> **(c)** Given $L$, find minimum DFT size $N_1$ and minimum FFT size $N_2$.
> **(d)** Number of (real) multiplications if DFT of size $N_1$ is computed directly.
> **(e)** For an $N_2$-point DFT/FFT, frequency resolution in Hz?

### The concept

Five mini-questions, each on a different formula you must know cold:

1. **L from time × sample rate**: $L = T \cdot f_s$.
2. **Resolution from main-lobe width**: rectangular window's main-lobe width is $4\pi/L$ rad/sample → $2 f_s/L$ Hz. Tones must be separated by **more than** this to resolve.
3. **DFT vs FFT minimum sizes**: DFT just needs $N \geq L$; FFT needs $N$ to be a **power of 2** and $N \geq L$.
4. **Direct DFT cost**: $N^2$ complex multiplications = $4 N^2$ real multiplications.
5. **Frequency resolution**: $\Delta f = f_s/N$ Hz.

See [[frequency-resolution]], [[window-resolution-criterion]], [[dft-computation-complexity]].

### Headline answers

**(a) $L = 40$.**
**(b) $f_1$ and $f_2$ must be separated by more than $\mathbf{40}$ Hz** (rectangular-window main-lobe width converted to Hz).
**(c) Min DFT size $N_1 = 40$. Min FFT size $N_2 = 64$** (next power of 2 ≥ 40).
**(d) $N_1$-point direct DFT: $\mathbf{1600}$ complex multiplications $= \mathbf{6400}$ real multiplications.**
**(e) Frequency resolution at $N_2 = 64$: $\mathbf{12.5}$ Hz.**

> [!info]- 📐 Show derivation — (a) Length of the segment
>
> Each sample is spaced $T_s = 1/f_s = 1/800 = 1.25$ ms apart. In 50 ms you fit
> $$L = \frac{0.050\text{ s}}{1.25\text{ ms}} = 0.050 \cdot 800 = 40\text{ samples}.$$
> Rule of thumb: $L = T \cdot f_s$ where $T$ is segment duration in seconds.

> [!info]- 📐 Show derivation — (b) Resolution condition
>
> When you take a finite-length segment, you've implicitly multiplied by a **rectangular window** of length $L$. Convolving in frequency, each ideal delta becomes the window's DTFT $W(e^{j\omega})$, which for a rectangular window is a Dirichlet kernel with **main-lobe width $4\pi/L$ rad/sample** (zero-crossing to zero-crossing).
>
> Two tones are **resolvable** iff their separation exceeds the main-lobe width:
> $$|\omega_1 - \omega_2| > \frac{4\pi}{L} \text{ rad/sample}.$$
>
> Convert to Hz using $\omega = 2\pi f/f_s$:
> $$|f_1 - f_2| > \frac{4\pi/L}{2\pi/f_s} = \frac{2 f_s}{L} = \frac{2 \cdot 800}{40} = \mathbf{40 \text{ Hz}}.$$
>
> **For Hamming/Hann the width doubles to $8\pi/L$ → $4 f_s/L$ Hz** ($= 80$ Hz here). Recta is sharpest in resolution, worst in side-lobes.

> [!info]- 📐 Show derivation — (c) Minimum DFT and FFT sizes
>
> **DFT size:** to avoid time-domain overlap (aliasing in the periodic extension that the DFT implicitly computes), need $N_1 \geq L$. So $N_1 = L = 40$.
>
> **FFT size:** the radix-2 FFT requires $N$ to be a power of 2. Smallest power of 2 with $N_2 \geq L = 40$ is $N_2 = 64$ (since $2^5 = 32 < 40 < 64 = 2^6$). So $N_2 = 64$.
>
> **Always pad with zeros** if $L < N$ — this just interpolates the DFT, doesn't add new info.

> [!info]- 📐 Show derivation — (d) Direct DFT multiplication count
>
> Direct DFT formula:
> $$X[k] = \sum_{n=0}^{N-1} x[n]\,e^{-j 2\pi k n / N}, \quad k = 0, 1, \dots, N-1.$$
>
> Each $X[k]$ requires $N$ complex multiplications and $N-1$ complex additions. Doing this for all $N$ values of $k$ gives **$N^2$ complex multiplications**.
>
> Each complex multiplication = $(a + jb)(c + jd) = (ac - bd) + j(ad + bc)$ → **4 real multiplications** + 2 real additions.
>
> Therefore $N^2$ complex mults = $\mathbf{4 N^2}$ real mults.
>
> Plug in $N_1 = 40$: $40^2 = 1600$ complex = $4 \cdot 1600 = 6400$ real.

> [!info]- 📐 Show derivation — (e) Frequency resolution
>
> The DFT samples the DTFT at $N$ uniformly spaced points around the unit circle. The spacing in digital frequency is $2\pi/N$ rad/sample. Convert to Hz with $f = \omega \cdot f_s / (2\pi)$:
> $$\Delta f = \frac{2\pi/N}{2\pi/f_s} = \frac{f_s}{N} = \frac{800}{64} = \mathbf{12.5 \text{ Hz}}.$$
>
> This is the **DFT-bin resolution** (the spacing between bins). It's distinct from **windowing resolution** in part (b), which depends on $L$ and window type. Increasing $N$ via zero-padding **does NOT** improve windowing resolution — only changing $L$ or the window does.

### Why it matters / what to study

This is the **bread-and-butter calculation** of the FFT module. Expect a similar problem with different numbers (and possibly Hamming or Hann window — then the main-lobe width is $8\pi/L$ rad/sample = $4 f_s/L$ Hz).

> [!tip] **Memorise these four formulas — they'll reappear in 3 of the 4 exam problems:**
> 1. **Sample count from time:** $L = T \cdot f_s$
> 2. **Window main-lobe width to Hz:** rect: $2 f_s / L$; Hamming/Hann: $4 f_s / L$
> 3. **DFT cost:** $N^2$ complex = $4 N^2$ real multiplications
> 4. **Bin resolution:** $\Delta f = f_s / N$

> [!warning] **Resolution vs binning — don't confuse them.**
> - **Resolution** (window main-lobe width) is set by $L$ and window type. It tells you "can I tell two tones apart?"
> - **Binning** ($f_s/N$) is set by FFT size $N$. It tells you "what frequencies do I report?"
> - You can have $\Delta f = 1$ Hz binning (huge $N$) but still be unable to resolve tones $30$ Hz apart if $L$ is too short.

---

## Problem 4 — 4-Point DFT by Definition + FFT Butterfly + IFFT

> **Setup.** $x[n] = \{1, 2, -3, -4\}$ for $n = 0, 1, 2, 3$.
>
> **(a)** Compute the 4-point DFT using the definition equation.
> **(b)** Sketch the 4-point FFT flow graph (DIT). Label inputs and outputs at every stage.
> **(c)** Number of butterflies and number of (real) multiplications.
> **(d)** Use the FFT butterfly graph to compute IFFT and recover $x[n]$.

### The concept

The keystone problem of the FFT module. Four sub-skills:

1. **Direct DFT** by plugging into $X[k] = \sum x[n] e^{-j 2\pi kn/N}$ — for $N = 4$ the twiddles are $\{1, -j, -1, +j\}$.
2. **DIT FFT flow graph** — even-indexed samples $\{x[0], x[2]\}$ on top, odd-indexed $\{x[1], x[3]\}$ on bottom (this is the **bit-reversed input order** for $N=4$).
3. **Counting**: number of butterflies = $\frac{N}{2} \log_2 N$; number of real multiplications = $2 N \log_2 N$ (rule of thumb for radix-2).
4. **IFFT-via-FFT trick**: $x[n] = \frac{1}{N}\bigl(\text{FFT}(X^*[k])\bigr)^*$ — same hardware, two conjugations and one division.

See [[fft]], [[butterfly]], [[bit-reversed-order]], [[idft]], [[twiddle-factor]].

### Headline answers

**(a) $X[k] = \{-4,\ 4 - 6j,\ 0,\ 4 + 6j\}$.**
**(b) See butterfly flow graph below — $\mathbf{4}$ butterflies in $\mathbf{2}$ stages.**
**(c) $\mathbf{4}$ butterflies, $\mathbf{16}$ real multiplications** ($2 N \log_2 N = 2 \cdot 4 \cdot 2$).
**(d) IFFT recovers $x[n] = \{1,\ 2,\ -3,\ -4\}$ ✓.**

> [!info]- 📐 Show derivation — (a) Direct 4-point DFT
>
> $$X[k] = \sum_{n=0}^{3} x[n] e^{-j 2\pi k n / 4} = \sum_{n=0}^{3} x[n] (W_4)^{kn}, \quad W_4 = e^{-j 2\pi/4} = -j.$$
>
> The four powers of $W_4$:
> $$W_4^0 = 1,\quad W_4^1 = -j,\quad W_4^2 = -1,\quad W_4^3 = +j.$$
>
> **$X[0]$** (DC, sum of all samples):
> $$X[0] = 1 + 2 + (-3) + (-4) = -4.$$
>
> **$X[1]$:**
> $$X[1] = 1\cdot 1 + 2\cdot(-j) + (-3)\cdot(-1) + (-4)\cdot j = 1 - 2j + 3 - 4j = 4 - 6j.$$
>
> **$X[2]$:**
> $$X[2] = 1 + 2\cdot(-1) + (-3)\cdot 1 + (-4)\cdot(-1) = 1 - 2 - 3 + 4 = 0.$$
>
> **$X[3]$:**
> $$X[3] = 1 + 2\cdot j + (-3)\cdot(-1) + (-4)\cdot(-j) = 1 + 2j + 3 + 4j = 4 + 6j.$$
>
> **Sanity check:** since $x[n]$ is real, $X[k]$ has conjugate symmetry: $X[3] = X[1]^* = (4 - 6j)^* = 4 + 6j$ ✓. $X[0]$ and $X[2]$ are real (because $0$ and $N/2$ are self-conjugate bins) ✓.

> [!info]- 📐 Show derivation — (b) DIT FFT butterfly flow graph for $N = 4$
>
> **Step 0 — Bit-reversed input order.** For $N = 4$, the bit-reverse permutation maps $\{0, 1, 2, 3\} \to \{0, 2, 1, 3\}$ (binary: $00 \to 00$, $01 \to 10$, $10 \to 01$, $11 \to 11$). So the inputs to stage 1, top to bottom, are $x[0], x[2], x[1], x[3]$.
>
> **Stage 1 — two 2-point DFTs (one butterfly each, twiddle $W_2^0 = 1$):**
> Top butterfly on $\{x[0]=1, x[2]=-3\}$:
> $$X_e[0] = x[0] + W_2^0 \cdot x[2] = 1 + (-3) = -2$$
> $$X_e[1] = x[0] - W_2^0 \cdot x[2] = 1 - (-3) = 4$$
> Bottom butterfly on $\{x[1]=2, x[3]=-4\}$:
> $$X_o[0] = x[1] + W_2^0 \cdot x[3] = 2 + (-4) = -2$$
> $$X_o[1] = x[1] - W_2^0 \cdot x[3] = 2 - (-4) = 6$$
>
> **Stage 2 — combine into the 4-point DFT (two butterflies, twiddles $W_4^0 = 1$ and $W_4^1 = -j$):**
> Top butterfly $\{X_e[0]=-2,\ W_4^0 \cdot X_o[0]=1 \cdot -2 = -2\}$:
> $$X[0] = X_e[0] + W_4^0 X_o[0] = -2 + (-2) = -4 \checkmark$$
> $$X[2] = X_e[0] - W_4^0 X_o[0] = -2 - (-2) = 0 \checkmark$$
> Bottom butterfly $\{X_e[1]=4,\ W_4^1 \cdot X_o[1] = -j \cdot 6 = -6j\}$:
> $$X[1] = X_e[1] + W_4^1 X_o[1] = 4 + (-6j) = 4 - 6j \checkmark$$
> $$X[3] = X_e[1] - W_4^1 X_o[1] = 4 - (-6j) = 4 + 6j \checkmark$$
>
> **All four DFT values match part (a).** This is the validation that the butterfly graph is correctly drawn.

> [!example] **ASCII flow graph (read left-to-right):**
> ```
>  STAGE 1 (W₂⁰=1)            STAGE 2 (W₄⁰=1, W₄¹=-j)
>
>  x[0]=1 ────────────●──────────────────●───── X[0]=-4
>                      \                /
>  x[2]=-3 ──[W₂⁰]──×──●──[Xe[0]=-2]──×─●───── X[2]=0
>                                       (×−1 down-leg)
>                                  
>  x[1]=2 ────────────●──────────────[W₄⁰=1]── X[1]=4−6j
>                      \             ╲       
>  x[3]=-4 ──[W₂⁰]──×──●──[Xo[0]=-2]──[W₄¹=-j]──● X[3]=4+6j
>                                       (×−1 down-leg)
> ```
> The exam version Dr. Wang draws is cleaner — see page 6 of `eee-404-exam-2-review.pdf` for the canonical layout. Practice **drawing** it freehand a few times before exam day.

> [!info]- 📐 Show derivation — (c) Counting butterflies and multiplications
>
> **Number of butterflies for radix-2 DIT FFT:**
> $$\#\text{butterflies} = \frac{N}{2} \cdot \log_2 N = \frac{4}{2} \cdot 2 = 4.$$
> Each stage has $N/2$ butterflies; there are $\log_2 N$ stages.
>
> **Number of real multiplications** (radix-2 rule of thumb, treating each twiddle as 4 real mults / each butterfly does 1 complex mult = 4 real mults):
> $$\#\text{real mults} \approx 2 N \log_2 N = 2 \cdot 4 \cdot 2 = 16.$$
>
> Compared to direct-DFT $4 N^2 = 64$ real mults, the FFT saves $64 - 16 = 48$ multiplications even at $N = 4$. The savings explode for larger $N$ — at $N = 1024$, FFT uses $\sim 20{,}000$ vs. direct $\sim 4{,}000{,}000$ ($\sim 200\times$ speedup).

> [!info]- 📐 Show derivation — (d) IFFT via FFT (the conjugate trick)
>
> **The trick.** Define $y[n] = \text{FFT}(X^*[k])$. Then $x[n] = y^*[n]/N$.
>
> **Why it works:** the IDFT formula is
> $$x[n] = \frac{1}{N} \sum_k X[k] e^{+j 2\pi k n / N}.$$
> Taking the conjugate of the sum:
> $$x^*[n] = \frac{1}{N} \sum_k X^*[k] e^{-j 2\pi k n / N} = \frac{1}{N} \cdot \text{FFT}(X^*[k])[n].$$
> So $x[n] = (\text{FFT}(X^*[k])/N)^*$.
>
> **Step-by-step for our values:**
>
> 1. **Conjugate the FFT result:** $X^*[k] = \{-4,\ 4 + 6j,\ 0,\ 4 - 6j\}$.
> 2. **Run the same 4-point FFT butterfly on $X^*[k]$.** Bit-reverse order at the input: $\{X^*[0]=-4, X^*[2]=0, X^*[1]=4+6j, X^*[3]=4-6j\}$.
>
>    **Stage 1:**
>    Top butterfly $\{-4, 0\}$: $X_e = \{-4 + 0, -4 - 0\} = \{-4, -4\}$.
>    Bottom butterfly $\{4+6j, 4-6j\}$: $X_o = \{(4+6j)+(4-6j), (4+6j)-(4-6j)\} = \{8, 12j\}$.
>
>    **Stage 2:** twiddles $W_4^0 = 1$ and $W_4^1 = -j$.
>    Top: $\{X_e[0] + W_4^0 X_o[0], X_e[0] - W_4^0 X_o[0]\} = \{-4 + 8, -4 - 8\} = \{4, -12\}$.
>    Bottom: $\{X_e[1] + W_4^1 X_o[1], X_e[1] - W_4^1 X_o[1]\} = \{-4 + (-j)(12j), -4 - (-j)(12j)\} = \{-4 + 12, -4 - 12\} = \{8, -16\}$.
>
>    **Output of FFT on $X^*$:** $\{4, 8, -12, -16\}$.
>
> 3. **Divide by $N = 4$:** $\{1, 2, -3, -4\}$.
> 4. **Conjugate** (no-op since these are real): $\{1, 2, -3, -4\}$.
>
> **Recovered $x[n] = \{1, 2, -3, -4\}$ ✓** — matches the original.

### Why it matters / what to study

This is **THE problem-type** for the FFT chapter. Expect a 4-point or 8-point variant on the exam. **Practice drawing the flow graph from memory** — examiners love to see clean labels at every internal node.

> [!tip] **Memorize the radix-2 counts:**
> | $N$ | Stages = $\log_2 N$ | Butterflies = $\frac{N}{2}\log_2 N$ | Real mults $= 2N\log_2 N$ |
> |---|---|---|---|
> | 4 | 2 | 4 | 16 |
> | 8 | 3 | 12 | 48 |
> | 16 | 4 | 32 | 128 |
> | 64 | 6 | 192 | 768 |
> | 128 | 7 | 448 | 1792 |
> | 256 | 8 | 1024 | 4096 |

> [!warning] **The IFFT exam trap.** Students often forget the **division by $N$** at the end. The "FFT on conjugate" gives you $N \cdot x^*[n]$, NOT $x^*[n]$. Always end with `/N` then conjugate (or conjugate then `/N` — order doesn't matter).

---

## Cross-problem patterns to internalise

> [!tip] **What every exam problem is really testing.**
> - **P1 (MLP):** can you crank the forward equation neuron-by-neuron without losing track of indexing or signs?
> - **P2 (Z-transform):** can you go fluently between $H(z) \leftrightarrow$ difference equation $\leftrightarrow$ block diagram, and reason about ROC + DTFT existence?
> - **P3 (Sampling/DFT/FFT sizing):** can you pick the right formula from $\{T\cdot f_s,\ 2 f_s/L,\ N^2,\ f_s/N\}$ for each sub-question?
> - **P4 (FFT butterfly):** can you draw a 4-pt or 8-pt DIT graph, label every node, count operations, and run the IFFT trick backwards?

> [!warning] **The 5 mistakes that will lose you the most points.**
> 1. **Negative pre-activation passing through ReLU as itself** instead of $0$.
> 2. **Confusing "resolution" (windowing) with "binning" (FFT size)** — different formulas, different scaling.
> 3. **FIR-vs-IIR by looking at numerator instead of denominator** of $H(z)$.
> 4. **Forgetting to divide by $N$ in IFFT-via-FFT.**
> 5. **Bit-reversed input order for DIT FFT** — drawing the butterfly with $\{x[0], x[1], x[2], x[3]\}$ in natural order. For $N=4$ the correct order is $\{x[0], x[2], x[1], x[3]\}$.

## See also

- [[eee-404-exam-2-study-guide]] — the formula sheet
- [[eee-404-hw5-walkthrough]] — DTFT, Hamming windowing, FFT real-time budget (already walked through)
- [[eee-404]] — course page (FFT module, Z-transform, NN, etc.)
- [[fft]], [[butterfly]], [[bit-reversed-order]], [[twiddle-factor]] — FFT mechanics
- [[dft]], [[dtft]], [[idft]], [[frequency-resolution]] — Fourier basics
- [[mlp]], [[neuron]], [[relu]], [[forward-propagation]] — neural networks
- [[z-transform]], [[region-of-convergence]], [[direct-form-ii]], [[fir-vs-iir]] — Z-transform mechanics
- [[window-resolution-criterion]], [[spectral-leakage]], [[hamming-window]] — windowing
