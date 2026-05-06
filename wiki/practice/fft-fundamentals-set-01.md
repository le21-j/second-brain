---
title: FFT Fundamentals — Practice Set 01
type: practice
course:
  - "[[eee-404]]"
tags: [practice, fft]
concept:
  - "[[fft]]"
  - "[[dft]]"
difficulty: mixed
created: 2026-04-21
updated: 2026-05-06
---

# FFT Fundamentals — Practice Set 01

> **How to use this:** Try each problem with pencil + paper before expanding the solution. When you miss one, log what tripped you up in [[fft-gotchas]] — pattern recognition is the whole point. Problems run easy $\to$ hard.

---

### 1. Twiddle factor values [easy]
What are $W_4^0, W_4^1, W_4^2, W_4^3$ as complex numbers?

<details><summary>Solution</summary>

$W_N^k = \cos(2\pi k/N) - j\cdot\sin(2\pi k/N)$. For $N = 4$:
- $W_4^0 = 1$
- $W_4^1 = -j$
- $W_4^2 = -1$
- $W_4^3 = j$

See [[twiddle-factor]].

</details>

---

### 2. Direct DFT cost [easy]
For $N = 64$, how many **real multiplications** are needed to compute the DFT directly (using the definition)?

- (a) 448
- (b) 768
- (c) 4096
- (d) 16384

<details><summary>Solution</summary>

Direct DFT: $N^2$ complex MULTs $= $ **$4N^2$** real MULTs $= 4\cdot 64^2 = $ **$16384$** $\to$ (d).

See [[dft-computation-complexity]].

</details>

---

### 3. Radix-2 FFT cost [easy]
For $N = 64$, how many real multiplications does a complex $N$-point FFT need?

<details><summary>Solution</summary>

$2N\cdot\log_2 N = 2\cdot 64\cdot\log_2 64 = 2\cdot 64\cdot 6 = $ **$768$**.

</details>

---

### 4. Bit-reversed order [easy–medium]
Take the complex conjugate of $X[k] = [1, 2 - j, -3, 2 + j]$ and arrange it in bit-reversed order. What do you get?

- (a) $[1, 2 - j, -3, 2 + j]$
- (b) $[1, 2 + j, -3, 2 - j]$
- (c) $[1, -3, 2 + j, 2 - j]$
- (d) $[1, -3, 2 - j, 2 + j]$

<details><summary>Solution</summary>

Conjugate: $[1, $ **$2 + j$**$, -3, $ **$2 - j$**$]$.
Bit-reverse for $N = 4$ ($00, 01, 10, 11 \to 00, 10, 01, 11$): positions $(0, 1, 2, 3) \to (0, 2, 1, 3)$.
Result: $[1, -3, 2 + j, 2 - j] \to $ **(c)**.

See [[bit-reversed-order]].

</details>

---

### 5. Frequency bin to frequency [medium]
$f_s = 8192$ Hz, $N = 128$, and $X[4]$ and $X[124]$ are the only non-zero bins. What's the signal's frequency?

- (a) 128 Hz
- (b) 256 Hz
- (c) 7872 Hz
- (d) 7936 Hz

<details><summary>Solution</summary>

$\Delta f = f_s/N = 8192/128 = 64$ Hz.
Bin $4$ is at $k\cdot\Delta f = 4\cdot 64 = $ **$256$ Hz**. Bin $124 = N - 4$ is the conjugate-symmetric mirror, also $256$ Hz.
Answer: **(b)**.

See [[dft-bin-interpretation]], [[conjugate-symmetry]].

</details>

---

### 6. Scaling recovery [medium]
You run a 1024-point FFT with scaling of $0.5$ at **every** stage. To recover the correct DFT, you should:

- (a) Multiply the output by 2
- (b) Multiply the output by 10
- (c) Multiply the output by 1024
- (d) Divide the output by 2

<details><summary>Solution</summary>

$\log_2(1024) = 10$ stages, each scaling by $0.5 \to$ total scale $= (1/2)^{10} = $ **$1/1024$**.
To undo: multiply by **$1024$** $\to$ **(c)**.

See [[fft-scaling]].

</details>

---

### 7. Real-input FFT cost [medium]
For $N = 64$, how many real multiplications are needed using the complex 32-point FFT trick for real inputs?

- (a) 448
- (b) 768
- (c) 4096
- (d) 16384

<details><summary>Solution</summary>

$\log_2(N/2)\cdot N + 2N = \log_2 32\cdot 64 + 128 = 5\cdot 64 + 128 = 320 + 128 = $ **$448$** $\to$ **(a)**.

Compare: native 64-pt FFT $= 768$. Real-input trick saves $\approx 42\%$.

See [[real-valued-fft]], [[dft-computation-complexity]].

</details>

---

### 8. Window main lobe [easy]
Which window has the smallest main-lobe width in frequency?

- (a) Rectangular
- (b) Hamming
- (c) Hann
- (d) Triangular

<details><summary>Solution</summary>

Rectangular: $4\pi/L$. All others: $8\pi/L$ (Bartlett: $8\pi/(L+1)$). Smallest $= $ **(a) Rectangular**.

Pay attention to the follow-up: *narrow main lobe* doesn't mean *best window overall* — rect also has the worst side lobes. See [[window-function]].

</details>

---

### 9. DFT by hand [medium]
Compute the 4-point DFT of $x[n] = [1, 0, 1, 0]$.

<details><summary>Solution</summary>

$X[k] = \sum x[n]\cdot W_4^{kn}$. With $x[0] = x[2] = 1$, $x[1] = x[3] = 0$:
- $X[0] = 1\cdot 1 + 0\cdot 1 + 1\cdot 1 + 0\cdot 1 = $ **$2$**
- $X[1] = 1\cdot 1 + 0\cdot(-j) + 1\cdot(-1) + 0\cdot(j) = $ **$0$**
- $X[2] = 1\cdot 1 + 0 + 1\cdot 1 + 0 = $ **$2$**
- $X[3] = 1 + 0 + (-1) + 0 = $ **$0$**

Result: **$X[k] = [2, 0, 2, 0]$**. Two spikes at $k = 0$ and $k = 2$ (DC + Nyquist). Makes sense: $[1, 0, 1, 0]$ is a 2-sample-period pulse train, which is exactly the Nyquist tone (sampled cosine at $f_s/2$), plus a DC level of $0.5$ — sum of DC component and alternating component.

</details>

---

### 10. IDFT by hand [medium–hard]
Given $X[k] = [4, 0, 0, 0]$, find $x[n]$.

<details><summary>Solution</summary>

IDFT: $x[n] = (1/N) \sum X[k]\cdot e^{+j2\pi kn/N}$. Only $X[0] = 4$ contributes.
$x[n] = (1/4) \cdot 4 \cdot 1 = $ **$1$** for all $n$. So $x[n] = [1, 1, 1, 1]$.

Intuition: all energy at DC $\to$ constant signal.

Via the FFT recipe:
1. $X^* = [4, 0, 0, 0]$.
2. Bit-reverse $\to [4, 0, 0, 0]$ (unchanged; $0$s are symmetric).
3. Forward FFT: all four stages see a $4$ and three $0$s $\to$ output is $[4, 4, 4, 4]$.
4. $\div 4 \to [1, 1, 1, 1]$. Conjugate (real) $\to$ **$[1, 1, 1, 1]$** $\checkmark$.

See [[idft]].

</details>

---

### 11. Overflow detection [hard]
Explain **why** the lab code wraps FFT outputs with `* 0.5` when `scale_or_not == 1`, and why it must multiply by `SIZE_FFT` at the end. Then explain what specifically goes wrong with a 128-pt real-valued sinusoid in fixed-point **without** scaling.

<details><summary>Solution</summary>

- Each butterfly computes `X[i] + U·X[k]`. In the worst case this sum can be twice the magnitude of the inputs. Multiply by $0.5 \to$ the stage output magnitude never exceeds the input range. After $\log_2 N$ stages, total shrinkage is $1/N$, so recover by multiplying output by $N$.
- Without scaling on 128-pt: $7$ stages of potential doubling $\to$ values up to $2^7 = 128\times$ the Q15 range. In 32-bit fixed-point those sums overflow, wrap around (two's complement), and produce garbage. Scaling prevents this by keeping intermediate magnitudes within Q15's $(-1, 1)$ bound.

See [[fft-scaling]], [[fixed-point-arithmetic]].

</details>

---

## Your attempts

_(Log attempts here: date, problem numbers, what you missed, what pattern to remember. I'll also echo anything you tell me into [[fft-gotchas]].)_
