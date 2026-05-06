---
title: EEE 404 HW5 — DTFT, Windowing, Resolution & FFT Compute Budget (Walkthrough)
type: walkthrough
course:
  - "[[eee-404]]"
tags: [eee-404, homework, walkthrough, dtft, dft, fft, hamming, rectangular, butterfly, stm32]
sources:
  - "[[homework-2026-04-27-eee-404-hw5]]"
created: 2026-04-27
updated: 2026-05-06
---

# EEE 404 HW5 — Walkthrough

> [!note] **What this is.** A per-problem walkthrough of HW5. For every problem I (a) **state it** verbatim, (b) **explain the overarching concept** so you understand what's being tested, (c) give the **headline answer** as a highlighted line, and (d) provide a **collapsible "Show derivation" callout** next to each equation so you can choose to view the full step-by-step algebra without it cluttering the page.
>
> The **highlighted lines** (like this) are the headline answers — what to write down on the submission. Click any callout titled "📐 Show derivation" to expand the in-depth breakdown.

> [!tip] **How the drop-downs work.** Click the **▶** triangle on the left of any `📐 Show derivation` callout to expand it (or **▼** to collapse). Body equations stay visible — only the *derivations* are tucked away by default.

---

## Problem 1 — Two-Tone DTFT, Hamming Windowing, FFT Compute

> **Setup.** A discrete-time real signal sampled at $f_s = 8$ kHz:
> $$x[n] = 2\cos\!\left(\tfrac{\pi}{4}n + \tfrac{\pi}{4}\right) + \cos\!\left(\tfrac{\pi}{3}n\right).$$

The two digital frequencies are $\omega_1 = \pi/4$ rad/sample and $\omega_2 = \pi/3$ rad/sample. Their **separation**
$$\Delta\omega = \omega_2 - \omega_1 = \tfrac{\pi}{3} - \tfrac{\pi}{4} = \tfrac{\pi}{12} \approx 0.262\text{ rad/sample}$$
is the number that controls everything in parts (b) and (c).

---

### Problem 1(a) — Plot $|X(e^{j\omega})|$

> **(a)** Determine and plot the magnitude of the DTFT $|X(e^{j\omega})|$ of the signal $x[n]$.

#### The concept

The DTFT of a single cosine is **two impulses** in the frequency domain — one at $+\omega_0$, one at $-\omega_0$ — each of magnitude $A\pi$ where $A$ is the amplitude. The constant phase $\phi$ rotates the impulses but does **not** change their magnitude. See [[dtft]].

#### Headline answer

**$|X(e^{j\omega})|$ has four impulses inside $|\omega| \leq \pi$:**
- **$\omega = \pm \pi/4$, magnitude $\mathbf{2\pi}$** (from the amplitude-2 cosine)
- **$\omega = \pm \pi/3$, magnitude $\mathbf{\pi}$** (from the amplitude-1 cosine)
- The pattern is **$2\pi$-periodic** in $\omega$.

> [!info]- 📐 Show derivation — DTFT of a cosine, then linearity
>
> **Step 1 — Euler's formula on each cosine.**
>
> $$2\cos\!\left(\tfrac{\pi}{4}n + \tfrac{\pi}{4}\right) = e^{j(\pi/4)\,n + j\pi/4} + e^{-j(\pi/4)\,n - j\pi/4}$$
>
> $$\cos\!\left(\tfrac{\pi}{3}n\right) = \tfrac{1}{2}\,e^{j(\pi/3)\,n} + \tfrac{1}{2}\,e^{-j(\pi/3)\,n}$$
>
> **Step 2 — DTFT of a complex exponential.**
>
> $$\sum_{n=-\infty}^{\infty} e^{j\omega_0 n}\,e^{-j\omega n} = 2\pi\,\delta(\omega - \omega_0)\quad\text{for } |\omega| \leq \pi$$
>
> **Step 3 — Apply linearity.**
>
> $$X(e^{j\omega}) = 2\pi e^{j\pi/4}\delta(\omega - \tfrac{\pi}{4}) + 2\pi e^{-j\pi/4}\delta(\omega + \tfrac{\pi}{4}) + \pi\,\delta(\omega - \tfrac{\pi}{3}) + \pi\,\delta(\omega + \tfrac{\pi}{3})$$
>
> **Step 4 — Take magnitudes** (each $|2\pi e^{j\phi}| = 2\pi$, each $|\pi| = \pi$):
>
> $$|X(e^{j\omega})| = 2\pi\bigl[\delta(\omega - \tfrac{\pi}{4}) + \delta(\omega + \tfrac{\pi}{4})\bigr] + \pi\bigl[\delta(\omega - \tfrac{\pi}{3}) + \delta(\omega + \tfrac{\pi}{3})\bigr]$$
>
> The phase $\pi/4$ in the first cosine **drops out of the magnitude** — that's why the answer above doesn't mention it.

> [!example] **Sketch.** Four vertical arrows along the $\omega$-axis: tall arrows ($2\pi$) at $\omega = \pm\pi/4$, shorter arrows ($\pi$) at $\omega = \pm\pi/3$. Plot from $-\pi$ to $+\pi$; the pattern repeats outside that range.

---

### Problem 1(b) — Can $L = 64$ Hamming Resolve the Two Tones?

> **(b)** Let $s[n]$ be a segment of $x[n]$ obtained by windowing with a Hamming window $w[n]$ of length $L$. Indicate whether the frequency components of $x[n]$ can be detected from $S(e^{j\omega})$ if $L = 64$. Why?

#### The concept

Windowing in time = **convolving** the spectrum with the window's DTFT $W(e^{j\omega})$. Each ideal impulse becomes a "lump" of width equal to the window's main-lobe width. Two tones can be **resolved** iff their separation exceeds that main-lobe width. See [[window-resolution-criterion]].

For Hamming: main-lobe width $= 8\pi/L$.

#### Headline answer

**No, $L = 64$ is too short.** The Hamming main-lobe width $8\pi/64 = \pi/8 \approx 0.393$ rad/sample exceeds the tone separation $\pi/12 \approx 0.262$ rad/sample, so the two main lobes overlap and merge into a single blob in $S(e^{j\omega})$.

> [!info]- 📐 Show derivation — apply the resolution criterion
>
> **Step 1 — Compute the main-lobe width at $L = 64$.**
>
> $$\Delta\omega_{\text{main}} = \frac{8\pi}{L} = \frac{8\pi}{64} = \frac{\pi}{8} \approx 0.3927\text{ rad/sample}$$
>
> **Step 2 — Compute the tone separation.**
>
> $$\Delta\omega_{\text{tones}} = \omega_2 - \omega_1 = \frac{\pi}{3} - \frac{\pi}{4} = \frac{4\pi - 3\pi}{12} = \frac{\pi}{12} \approx 0.2618\text{ rad/sample}$$
>
> **Step 3 — Compare.**
>
> $$\Delta\omega_{\text{main}} = \frac{\pi}{8} \;>\; \frac{\pi}{12} = \Delta\omega_{\text{tones}}$$
>
> Main lobe is **wider** than the gap between the tones. The two main lobes therefore overlap, smearing the two impulses into one blob centered between $\pi/4$ and $\pi/3$. **Cannot resolve.**
>
> **Numerical check:** ratio is $(8\pi/L) / (\pi/12) = 96/L$. For $L = 64$ the ratio is $1.5$ — i.e. the main lobe is $1.5\times$ wider than the gap. Need ratio $\leq 1$, i.e. $L \geq 96$.

> [!warning] **Common slip.** Don't confuse this with bin spacing $\Delta f = f_s/N$. Even if you took a 64-point DFT and the bins were nominally fine enough, the **window** still smears each impulse over $8\pi/L$ rad/sample — bin spacing can't undo that smear.

---

### Problem 1(c) — Smallest Hamming $L^*$ That Resolves

> **(c)** Determine the length $L^*$ of the Hamming window that would provide the best time-resolution while allowing the frequency components of $x[n]$ to be resolved. Justify.

#### The concept

"Best time resolution" $=$ **smallest $L$**. (A long window blurs over a long time interval, so for transient signals you want $L$ as small as you can get away with.) The smallest $L$ that still resolves the tones is the one for which main-lobe width *equals* the tone separation.

#### Headline answer

**$L^* = 96$.**

> [!info]- 📐 Show derivation — solve $8\pi/L = \pi/12$
>
> **Resolution requirement (Hamming):**
>
> $$\frac{8\pi}{L} \leq \Delta\omega_{\text{tones}} = \frac{\pi}{12}$$
>
> **Solve for $L$:**
>
> $$L \geq \frac{8\pi}{\pi/12} = 8 \cdot 12 = 96$$
>
> **Smallest $L$ satisfying the inequality** $\Rightarrow L^* = 96$.
>
> **Why "best time-resolution" means smallest $L$:** the window is a sliding-aperture low-pass filter in time. A length-$L$ window blurs over $L$ samples of time. For a non-stationary signal (one whose spectrum changes), shorter windows track changes better. The job here is to find the *smallest* window that still passes the frequency-resolution test.

> [!tip] **Time-frequency uncertainty.** This is the [[stft]] trade-off in microcosm: $L$ controls both time blur ($L \cdot T_s$ seconds) and frequency blur ($\Delta\omega_{\text{main}} = 8\pi/L$ rad/sample). The product is fixed by the window shape — you can move the trade-off but you can't beat it.

---

### Problem 1(d) — Frequency Resolution of the $L^*$-Point DFT

> **(d)** Let $s_2[n]$ be a segment of $x[n]$ obtained by windowing with the $L^*$-point Hamming from (c). Let $S_2[k]$ be the $L^*$-point DFT of $s_2[n]$. Determine the frequency resolution of $S_2[k]$.

#### The concept

The DFT samples the DTFT at $N$ equally-spaced points, with **bin spacing**:
$$\Delta f = \frac{f_s}{N}$$
This is **a property of the DFT length $N$**, not the window shape. See [[frequency-resolution]].

#### Headline answer

**$\Delta f = f_s / L^* = 8000 / 96 \approx \mathbf{83.33}$ Hz.**

> [!info]- 📐 Show derivation — bin-spacing formula plug-in
>
> **Bin spacing formula:**
>
> $$\Delta f = \frac{f_s}{N}$$
>
> **Plug in $f_s = 8000$ Hz, $N = L^* = 96$:**
>
> $$\Delta f = \frac{8000}{96} = \frac{1000}{12} = 83.\overline{3}\text{ Hz}$$
>
> **Equivalent forms:**
> - Digital: $\Delta\omega = 2\pi/N = 2\pi/96 = \pi/48$ rad/sample.
> - Analog angular: $\Delta\Omega = 2\pi f_s/N \approx 523.6$ rad/s.
>
> **Sanity check:** the two tones in $x[n]$ are at digital frequencies $\pi/4$ and $\pi/3$, which correspond to analog frequencies
>
> $$f_1 = \tfrac{\pi/4}{2\pi}\cdot f_s = 1000\text{ Hz}, \qquad f_2 = \tfrac{\pi/3}{2\pi}\cdot f_s \approx 1333.3\text{ Hz}.$$
>
> Their separation $333.3$ Hz is $\approx 4 \cdot \Delta f$ — comfortably resolvable in bins.

> [!warning] **Bin spacing $\neq$ resolution.** Bin spacing is a sampling artifact of the DFT (controlled by $N$), but the *resolution* of what you can actually distinguish is set by the **window's main-lobe width** (controlled by $L$ and the window shape). Often $N = L$, but in zero-padding scenarios $N > L$ — bins get finer but resolution does not improve.

---

### Problem 1(e) — Butterflies for the 64-Point Rectangular-Windowed FFT

> **(e)** Let $s_3[n]$ be a segment of $x[n]$ obtained by windowing with a 64-point rectangular window. Let $S_3[k]$ be the 64-point DFT of $s_3[n]$. Determine the minimum number of FFT butterflies needed to compute $S_3[k]$. Justify.

#### The concept

A radix-2 FFT of length $N = 2^p$ runs $\log_2(N)$ **stages**. Each stage performs $N/2$ butterflies. So total butterflies $= \frac{N}{2}\log_2(N)$. See [[butterfly]] and [[fft]].

#### Headline answer

**Minimum butterflies $= 192$.**

> [!info]- 📐 Show derivation — count stages and butterflies per stage
>
> **Step 1 — Number of stages.**
>
> $$\#\text{stages} = \log_2(N) = \log_2(64) = 6$$
>
> **Step 2 — Butterflies per stage.** Each stage of a length-$N$ FFT pairs samples and applies one butterfly per pair, so
>
> $$\#\text{butterflies per stage} = \frac{N}{2} = \frac{64}{2} = 32$$
>
> **Step 3 — Total.**
>
> $$\#\text{butterflies total} = \log_2(N) \cdot \frac{N}{2} = 6 \cdot 32 = 192$$
>
> **General formula:**
>
> $$\boxed{\#\text{butterflies} = \frac{N}{2}\log_2(N)}$$
>
> For comparison: a direct DFT computation costs $N^2 = 4096$ complex multiplies — the FFT saves a factor of $N^2 / (N\log_2 N / 2) = 2N/\log_2 N \approx 21$ at $N = 64$. See [[dft-computation-complexity]].

> [!note] **Why the window shape doesn't change the answer.** Multiplying by a rectangular window before the FFT is just an element-wise multiply by ones (or zeros for $n \geq L$) — it doesn't add or remove butterflies. The butterfly count depends only on the FFT length $N$.

---

## Problem 2 — Two-Signal Resolution & Real-Time STM32 Budget

> **Setup.** Two discrete-time signals at $f_s = 1.68$ MHz:
> $$x[n] = \cos\!\left(\tfrac{\pi}{3}n\right) + \cos\!\left(\tfrac{\pi}{2}n\right), \qquad y[n] = \cos\!\left(\tfrac{\pi}{6}n\right) + \cos\!\left(\tfrac{\pi}{3}n\right).$$

Frequency components present:
- $x[n]$: $\omega \in \{\pi/3, \pi/2\}$ (and their negatives).
- $y[n]$: $\omega \in \{\pi/6, \pi/3\}$ (and their negatives).

Smallest separation in $x$: $\pi/2 - \pi/3 = \pi/6$. Smallest separation in $y$: $\pi/3 - \pi/6 = \pi/6$. **Both signals share the same critical separation $\Delta\omega_{\text{crit}} = \pi/6$.**

---

### Problem 2(a) — Plot $|X(e^{j\omega})|$ and $|Y(e^{j\omega})|$

> **(a)** Determine and plot the magnitude of the DTFTs $|X(e^{j\omega})|$ and $|Y(e^{j\omega})|$ of the signals $x[n]$ and $y[n]$.

#### Headline answer

**$|X(e^{j\omega})|$**: four impulses at $\omega = \pm\pi/3, \pm\pi/2$, each of magnitude $\pi$.

**$|Y(e^{j\omega})|$**: four impulses at $\omega = \pm\pi/6, \pm\pi/3$, each of magnitude $\pi$.

> [!info]- 📐 Show derivation — same DTFT-of-cosine machinery as 1(a)
>
> For each cosine $\cos(\omega_0 n)$ the DTFT is $\pi[\delta(\omega - \omega_0) + \delta(\omega + \omega_0)]$ (within $|\omega| \leq \pi$, repeated $2\pi$-periodically) — see [[dtft]].
>
> By linearity, summing two cosines sums their DTFTs. Both cosines here have unit amplitude, so each impulse has magnitude $\pi$.
>
> **$x[n]$:** impulses at $\pm\pi/3$ (from $\cos(\pi n/3)$) and at $\pm\pi/2$ (from $\cos(\pi n/2)$), all magnitude $\pi$.
>
> **$y[n]$:** impulses at $\pm\pi/6$ (from $\cos(\pi n/6)$) and at $\pm\pi/3$ (from $\cos(\pi n/3)$), all magnitude $\pi$.
>
> Note: $y[n]$ shares the $\pi/3$ component with $x[n]$ — that's *not* coincidence, the next two parts use this shared structure.

> [!example] **Sketch.** For each spectrum: four equal-height impulses on the $\omega$-axis. $x$'s impulses are bunched closer to $\pi/2$; $y$'s are bunched closer to baseband.

---

### Problem 2(b) — Min Rectangular Window $L$ to Resolve Both Signals

> **(b)** Let $w[n]$ be a causal rectangular window of length $L$, used to extract $L$-point segments from $x[n]$ and $y[n]$. Determine the minimum window length $L$ that can resolve the frequency components of both $x[n]$ and $y[n]$.

#### The concept

The rectangular window has main-lobe width $4\pi/L$. For both signals to resolve, $L$ must satisfy the resolution criterion against the *smallest* separation across both.

#### Headline answer

**$L_{\min} = 24$.**

> [!info]- 📐 Show derivation — find the binding constraint, solve for $L$
>
> **Step 1 — Find the smallest separation across both signals.**
>
> | Signal | Components | Smallest separation |
> |:---|:---:|:---:|
> | $x[n]$ | $\pi/3, \pi/2$ | $\pi/2 - \pi/3 = \pi/6$ |
> | $y[n]$ | $\pi/6, \pi/3$ | $\pi/3 - \pi/6 = \pi/6$ |
>
> Both signals share the **same critical separation** $\Delta\omega_{\text{crit}} = \pi/6$.
>
> **Step 2 — Apply the rectangular resolution criterion** (main-lobe width $= 4\pi/L$):
>
> $$\frac{4\pi}{L} \leq \frac{\pi}{6} \;\;\Longrightarrow\;\; L \geq \frac{4\pi}{\pi/6} = 24$$
>
> **Smallest $L$ satisfying both signals' constraints:** $L_{\min} = 24$.

---

### Problem 2(c) — Min Hamming Window $L'$ to Resolve Both Signals

> **(c)** Let $w[n]$ be a causal Hamming window of length $L'$, used to extract $L'$-point segments. Determine the minimum window length $L'$ that can resolve the frequency components of both $x[n]$ and $y[n]$.

#### Headline answer

**$L'_{\min} = 48$.**

> [!info]- 📐 Show derivation — same constraint, Hamming main-lobe
>
> **Same critical separation** as (b): $\Delta\omega_{\text{crit}} = \pi/6$.
>
> **Hamming resolution criterion** (main-lobe width $= 8\pi/L'$):
>
> $$\frac{8\pi}{L'} \leq \frac{\pi}{6} \;\;\Longrightarrow\;\; L' \geq \frac{8\pi}{\pi/6} = 48$$
>
> **Smallest $L'$:** $L'_{\min} = 48$.
>
> **Why 2× the rectangular requirement:** Hamming's main lobe is exactly $2\times$ wider than rectangular's, so resolving the same gap needs $2\times$ the window length. The trade-off you bought: $\sim 30$ dB better side-lobe rejection (rectangular's side-lobes are at $-13$ dB; Hamming's at $-43$ dB).

> [!tip] **Why pay $2\times$ samples for the Hamming?** Side-lobe rejection. With a rectangular window, leakage from a strong tone can hide a weak nearby tone in its side lobes ($-13$ dB only). Hamming pushes side lobes down to $-43$ dB at the cost of a wider main lobe. Pick rectangular when both tones are comparable in amplitude; pick Hamming when one is much weaker than the other.

---

### Problem 2(d) — Real-Time STM32 Compute Budget

> **(d)** If the real-time constraint of the application requires that the segment be processed using 400 instructions and the STM32F407 has a 168 MHz clock rate with 1 instruction per cycle, determine the length $L^*$ of the signal segment.

#### The concept

For real-time DSP, **processing time of one segment $\leq$ acquisition time of one segment**. If processing exceeds acquisition, the next segment arrives before the previous is done and the buffer overruns.
- **Processing time** = (instructions per segment) / (clock rate)
- **Acquisition time** = (samples per segment) / (sample rate) $= L^* \cdot T_s$

Set them equal to find the maximum segment length the budget allows.

#### Headline answer

**$L^* = 4$ samples.**

> [!info]- 📐 Show derivation — equate processing time to acquisition time
>
> **Step 1 — Processing time per segment.**
>
> $$T_{\text{proc}} = \frac{\#\text{instructions}}{\text{clock rate}} = \frac{400}{168 \times 10^6\text{ Hz}} = \frac{400}{168}\,\mu\text{s} \approx 2.381\,\mu\text{s}$$
>
> **Step 2 — Sample period.**
>
> $$T_s = \frac{1}{f_s} = \frac{1}{1.68 \times 10^6\text{ Hz}} \approx 0.5952\,\mu\text{s}$$
>
> **Step 3 — Real-time constraint** (segment processing time $\leq$ time to acquire one segment of $L^*$ samples):
>
> $$T_{\text{proc}} \leq L^* \cdot T_s \;\;\Longrightarrow\;\; L^* \geq \frac{T_{\text{proc}}}{T_s} = \frac{400/168}{1/1.68}$$
>
> **Step 4 — Simplify.** Note that $f_{\text{clk}} / f_s = 168\text{ MHz} / 1.68\text{ MHz} = 100$ clock cycles per sample. So the real-time budget is
>
> $$L^* \geq \frac{\#\text{instructions}}{f_{\text{clk}}/f_s} = \frac{400}{100} = 4$$
>
> **Minimum segment length the budget allows:** $L^* = 4$ samples.
>
> **Equivalent intuition:** in 1 sample period the processor runs $f_{\text{clk}} \cdot T_s = 168 \times 10^6 \cdot 0.5952 \times 10^{-6} = 100$ instructions. To spend a budget of $400$ instructions on one segment, the segment must contain $400 / 100 = 4$ samples.

> [!warning] **The tension with (b) and (c).** Parts (b)/(c) said you need $L \geq 24$ (rect) or $L' \geq 48$ (Hamming) to resolve the tones. Part (d) says $L^* = 4$ to fit the real-time budget. The two requirements are incompatible — you cannot both resolve the tones *and* meet the 400-instruction-per-segment budget on this STM32. Real-time DSP is a tower of trade-offs; this homework drops you into one.

> [!tip] **Resolutions for the trade-off in practice.**
> - **Increase the instruction budget per segment** (use a faster MCU, or hardware accelerator).
> - **Decrease $f_s$** (sample slower — but only if Nyquist still holds for your highest tone).
> - **Use overlap-add or block-asynchronous processing** (process longer segments but at lower per-second cost).
> - **Drop the resolution requirement** (if you don't actually need to separate $\pi/3$ and $\pi/2$).

---

## Cross-references

- [[dtft]] — DTFT of cosines, used in 1(a) and 2(a)
- [[window-resolution-criterion]] — the resolution test used in 1(b,c) and 2(b,c)
- [[hamming-window]], [[rectangular-window]] — main-lobe widths
- [[frequency-resolution]] — bin spacing $\Delta f = f_s/N$, used in 1(d)
- [[butterfly]], [[fft]], [[dft-computation-complexity]] — used in 1(e)
- [[stft]] — the time-vs-frequency trade-off behind 1(c)
- [[homework-2026-04-27-eee-404-hw5]] — source summary
- [[eee-404]] — course page
- [[lab-7-fft]] — same STM32F407 / 168 MHz setup as 2(d)

## Report template (copy-paste skeleton)

```
EEE 404/591 HW5
Name: Jayden Le      Date: <due date>

Problem 1.  fs = 8 kHz, x[n] = 2 cos(pi/4 n + pi/4) + cos(pi/3 n)
   Tone separation: pi/3 - pi/4 = pi/12 rad/sample.

   1(a) DTFT: 4 impulses inside |w| <= pi.
        |X(e^jw)| = 2pi at w = +/- pi/4
        |X(e^jw)| = pi   at w = +/- pi/3
        Spectrum is 2pi-periodic.

   1(b) L = 64 Hamming -> main-lobe width = 8pi/64 = pi/8 ~ 0.393.
        Tone separation pi/12 ~ 0.262 < 0.393.
        Main lobes overlap -> CANNOT RESOLVE.

   1(c) Need 8pi/L <= pi/12 -> L >= 96.
        ANSWER: L* = 96 (smallest L for best time-resolution).

   1(d) Bin spacing = fs/N = 8000/96 ~ 83.33 Hz.
        ANSWER: delta_f ~ 83.33 Hz.

   1(e) 64-pt FFT: log2(64) = 6 stages, 64/2 = 32 butterflies/stage.
        ANSWER: 6 * 32 = 192 butterflies.

Problem 2.  fs = 1.68 MHz
            x[n] = cos(pi/3 n) + cos(pi/2 n)
            y[n] = cos(pi/6 n) + cos(pi/3 n)
   Critical separation (both signals): pi/6 rad/sample.

   2(a) |X|: 4 impulses at w = +/- pi/3, +/- pi/2, magnitude pi each.
        |Y|: 4 impulses at w = +/- pi/6, +/- pi/3, magnitude pi each.

   2(b) Rectangular: 4pi/L <= pi/6 -> L >= 24.
        ANSWER: L_min = 24.

   2(c) Hamming: 8pi/L' <= pi/6 -> L' >= 48.
        ANSWER: L'_min = 48.

   2(d) T_proc = 400/168MHz = 2.381 us.
        T_s = 1/1.68MHz = 0.595 us.
        L* = T_proc / T_s = 400 / (168/1.68) = 400/100 = 4.
        ANSWER: L* = 4 samples.
        (Note: this is far below the L>=24/48 needed for resolution
         in (b)/(c) — the real-time constraint is the binding one.)
```

> [!note] **About the report template above.** Intentionally written in plain ASCII (Greek letters as words, no `$...$`) — it's a skeleton for a Word doc / handwritten submission, not a wiki page. The wiki body above renders the same equations in proper LaTeX.
