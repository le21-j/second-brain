---
title: EEE 404 — Lab Exam + ABET Quiz Walkthrough (2026-05-05)
type: walkthrough
course: [[eee-404]]
tags: [eee-404, lab-exam, abet-quiz, study-guide, finals, lab-5, lab-6, project-1, project-2, assembly, dsp, fft, mlp, fixed-point]
sources: [[eee-404]], [[eee-404-exam-2-walkthrough]], [[eee-404-exam-2-study-guide]], [[eee-404-project-2-walkthrough]], [[lab-eee-404-project-2-fft-applications]]
created: 2026-05-04
updated: 2026-05-04
---

# EEE 404 — Lab Exam + ABET Quiz Walkthrough

> [!note] **Tomorrow's exam window: Tuesday 2026-05-05, 9:50–11:40 AM.**
> Two back-to-back assessments in the EEE 404 final-exam slot. Source: [Canvas announcement 2026-04-23](https://canvas.asu.edu/courses/241591/discussion_topics/7051419) by [[chao-wang]].
>
> | # | Assessment | Length | Format | Points | Resources |
> |---|---|---|---|---|---|
> | 1 | **Lab Exam** | 15 min | Canvas, 5 multiple-choice | 50 | **open book + open notes**, laptop required |
> | 2 | **ABET Quiz** | 30 min | Paper, MC + T/F + fill-in + short-essay | 50 | **closed book** except **two 8.5×11 sheets**, calculator OK |
>
> **Combined output decision.** Both assessments are scheduled in the same exam slot and the ABET quiz subsumes every topic on the lab exam. Rather than split into two walkthroughs that would duplicate ~70% of content, this single page covers both — **§A** is the lab-exam study guide (5 topic blocks, one per MC question), **§B** is the ABET quiz cheat-sheet skeleton (whole-semester comprehensive). Jayden, you'll have this file open in Obsidian during the lab exam, and you'll have the **§B Master Cheat Sheet** transcribed onto your two 8.5×11 sheets for the ABET quiz.

> [!tip] **The 90-minute strategy for tomorrow morning.**
> 1. **9:50–9:55 (5 min):** sit down, open this page in Obsidian split-screen with Canvas. Skim §A. Have lab manuals + project-2 walkthrough open in adjacent tabs.
> 2. **9:55–10:10 (15 min):** take the lab exam. **Five questions, 3 minutes each.** Don't camp on one — flag and move.
> 3. **10:10–10:15 (5 min):** put away laptop, pull out the two 8.5×11 sheets you transcribed from §B.
> 4. **10:15–10:45 (30 min):** ABET quiz. Read every question fully before answering — the "short essay" items reward concepts, not derivations.
> 5. **10:45–11:40:** banked time / submit. Walk to SCOB 250 for the EEE 335 final at 12:10.

---

# §A — LAB EXAM (50 pts, 15 min, open book/notes)

> [!example] **Format anchor.** Five multiple-choice questions, one per topic below. **3 minutes per question** average. Open laptop, open notes — but the time pressure means you must **know where things live in your notes before the exam starts**, not search during. Keep this page, [[eee-404-project-2-walkthrough]], the lab manuals, and the slide decks ([Lab 5 overview](../../raw/labs/eee-404/lab-exam-prep/lab5_overview.pdf), [Lab 6 overview](../../raw/labs/eee-404/lab-exam-prep/lab6_overview.pdf), [Project 1 overview](../../raw/labs/eee-404/lab-exam-prep/project1_overview.pdf)) all open in tabs.

## A.1 — Lab 5: Digital Filters

> [!info] **Source:** [Lab 5 overview slides](../../raw/labs/eee-404/lab-exam-prep/lab5_overview.pdf) · [Module 8 difference equation deck](../../raw/slides/eee-404/m8-difference-equation-filter-implementation.pdf) · [[summary-eee-404-m8-difference-equation]]

### Framework — the 4 building blocks

1. **IIR vs FIR classifier** (from $H(z)$ denominator)
2. **Difference equation ↔ block diagram** (DF-I, DF-II, transposed DF-II)
3. **Hardware path:** PDM mic → I²S → DMA → callback → filter → I²S → DAC
4. **Fixed-point implementation tradeoffs:** scaling, truncation error, overflow

### Headline answers to memorize

**Answer (FIR vs IIR):** **FIR** has only feedforward taps ($y[n] = \sum b_k x[n-k]$, denominator of $H(z)$ is constant). **IIR** has feedback ($a_k$ terms with $k \geq 1$). FIR has finite impulse response and is always stable; IIR can have infinite impulse response and can go unstable if poles fall outside the unit circle.

**Answer (echo as IIR):** A simple echo is $y[n] = x[n] + \alpha \cdot y[n - D]$ where $D$ = delay in samples and $\alpha$ = attenuation. **Bigger $D$ = longer echo gap; bigger $\alpha$ = louder/more sustained echo.** $\alpha < 1$ for stability.

**Answer (FIR HP vs LP):** A length-2 averaging FIR $y[n] = \tfrac{1}{2}(x[n] + x[n-1])$ is a **low-pass** (smooths fast variations). The differencing FIR $y[n] = \tfrac{1}{2}(x[n] - x[n-1])$ is **high-pass** (kills DC, passes fast variations).

### Implementation details (the lab-exam ammo)

**Hardware/timing facts** (from Lab 5 slides, [Lab 5 overview p.11](../../raw/labs/eee-404/lab-exam-prep/lab5_overview.pdf)):
- **Sampling rate:** $f_s = 16\,000$ samples/sec.
- **Callback period:** every **1 ms** (16 samples per callback).
- **PDM → PCM conversion** happens inside the callback before filtering.
- **Two BSP APIs:** `BSP_AUDIO_IN_Init()` + `BSP_AUDIO_IN_Record()` start mic; `BSP_AUDIO_OUT_Init()` + `BSP_AUDIO_OUT_Play()` start DAC. Half-buffer + complete-buffer callbacks (`BSP_AUDIO_IN_HalfTransfer_CallBack` / `BSP_AUDIO_IN_TransferComplete_CallBack`) are where the filter runs.
- **DMA** moves samples without CPU intervention — frees the CPU for the actual filtering.
- **I²S:** synchronous serial interface (Philips, MSB/LSB-justified, PCM standards). Two instances: one as receiver (mic), one as transmitter (DAC).
- Within **1 ms**, you must finish PDM→PCM conversion AND filter computation, or you miss real-time deadline.

**Three filter implementation flavors** (per [Lab 5 overview p.2](../../raw/labs/eee-404/lab-exam-prep/lab5_overview.pdf)):
1. **C floating-point** — easy to write, slowest.
2. **C fixed-point** — manual Q-format scaling; faster than float but watch overflow.
3. **Hybrid inline assembly fixed-point** — fastest; uses ARM DSP instructions like `SMULL`, `SMLAL`, saturated `SSAT`. Most compact code path.

> [!warning] **The fixed-point trap.** When you compute $y[n] = b_0 x[n] + b_1 x[n-1] + \dots$ in Q1.15: each multiply produces a Q2.30 (or Q1.30) result, so you must shift right by 15 to get back to Q1.15. **If you skip the shift you get apparent overflow / wraparound.** Truncation error appears when you discard the lower 15 bits.

> [!tip] **What to memorize vs. derive (Lab 5).**
> **Memorize:**
> 1. $f_s = 16$ kHz, 1 ms callback, 16 samples per callback.
> 2. Echo: $y[n] = x[n] + \alpha \cdot y[n-D]$, $\alpha < 1$ for stability.
> 3. FIR LP = sum-and-divide; FIR HP = subtract-and-divide.
>
> **Derive at the moment** (because the question may parameterize differently):
> - Whether a given $H(z)$ is FIR or IIR (look at denominator).
> - Number of delay elements (DF-I = $M+N$; DF-II = $\max(M,N)$).

**Same framework as:** [[eee-404-exam-2-walkthrough]] §P2 (Z-transform → DF-II), [[eee-404-exam-2-study-guide]] §4 (block diagrams), [[summary-eee-404-m8-difference-equation]].

---

## A.2 — Lab 6: Music Note Synthesis

> [!info] **Source:** [Lab 6 overview slides](../../raw/labs/eee-404/lab-exam-prep/lab6_overview.pdf) · Module 9 sinusoidal synthesis deck on Canvas.

### Framework — the 4 building blocks

1. **Sine table look-up** with two reconstruction strategies (round-down vs linear interpolation)
2. **Phase accumulator** — generates the table index from the desired note frequency
3. **ADSR envelope** — Attack, Decay, Sustain, Release amplitude shaping
4. **Fixed-point implementation tradeoffs** (same scaling/truncation issues as Lab 5)

### Headline answers to memorize

**Answer (round-down vs linear interpolation):** **Round-down** picks the nearest table index by truncation — fast, but introduces audible quantization noise on the synthesized tone. **Linear interpolation** between adjacent table entries reduces this noise at the cost of one extra multiply-add. **Linear interpolation produces a cleaner tone**, especially at higher pitches where the phase increment is large relative to the table size.

**Answer (ADSR envelope):** ADSR shapes the *amplitude* of the synthesized sine over time so that a note has a piano-like or guitar-like attack and decay rather than starting and stopping abruptly. The four phases are:
- **A**ttack — amplitude ramps up from 0 to peak (typically 5–50 ms).
- **D**ecay — amplitude falls from peak to a sustain level.
- **S**ustain — amplitude held constant while the note is "on."
- **R**elease — amplitude ramps down to 0 after note-off.

**Answer (timing):** **Sample rate 16 kHz, half-buffer = 512 samples = 32 ms callback period.** Per [Lab 6 overview p.6](../../raw/labs/eee-404/lab-exam-prep/lab6_overview.pdf): "every 512/16000 = 32 ms, one callback fires; you must generate 512 samples in that window."

### The phase accumulator (the math the question may probe)

A sine table with $L$ entries spans **one period** of a unit sine: `table[i] = sin(2π·i/L)`. To synthesize frequency $f_0$ at sample rate $f_s$:

$$\text{phase\_increment} = \frac{f_0 \cdot L}{f_s}$$

Each sample, advance `phase` by `phase_increment` and read `table[floor(phase)]` (round-down) or interpolate between `table[floor(phase)]` and `table[floor(phase)+1]` (linear interpolation). Wrap `phase` modulo $L$.

**Worked example:** $f_0 = 440$ Hz (A4), $f_s = 16\,000$ Hz, $L = 1024$. `phase_increment = 440·1024/16000 = 28.16`. Round-down advances by 28 each sample; linear interpolation advances by 28.16 and interpolates the 0.16 remainder.

### Three implementation flavors (same as Lab 5)

1. **C floating-point** — `sin()` from `math.h` directly; easy but very slow.
2. **C fixed-point** — `int16_t` table, Q1.15 representation, integer indexing, integer ADSR.
3. **Hybrid inline assembly fixed-point** — fastest; uses ARM `SMULL`/`SMLAL` for ADSR scaling.

> [!tip] **What to memorize vs. derive (Lab 6).**
> **Memorize:**
> 1. ADSR = Attack, Decay, Sustain, Release (in that order).
> 2. $f_s = 16$ kHz, half-buffer = 512 samples, 32 ms per callback.
> 3. Phase increment formula: $\Delta\phi = f_0 L / f_s$.
>
> **Derive:**
> - Round-down vs interpolation tradeoff (precision vs cycles).
> - Whether a given operation overflows in Q1.15.

**Same framework as:** [[fixed-point-arithmetic]], the sine table look-up pattern reuses the *table-index → reconstruction* idea from any quantization step.

---

## A.3 — Project 1: Real-Time Image Processing

> [!info] **Source:** [Project 1 overview slides](../../raw/labs/eee-404/lab-exam-prep/project1_overview.pdf) · Module 5 image processing decks (intro, gray-level transforms, histogram equalization).

### Framework — the 4 building blocks

1. **Thresholding** (3 variants: global, band, semi)
2. **Gray-level quantization** (reduce 256 levels → 128/64/32/16)
3. **Gray-level transformations** (linear or piecewise-linear remapping)
4. **Histogram equalization** (CDF-based contrast stretch)

### Headline answers to memorize

**Answer (thresholding variants):**
- **Global thresholding:** if pixel $\geq T$, output 255; else output 0. Pure binary.
- **Band thresholding:** if $T_{\text{lo}} \leq$ pixel $\leq T_{\text{hi}}$, output 255; else 0. Keeps a "band" of intensities.
- **Semi-thresholding:** if pixel $\geq T$, output pixel (unchanged); else output 0. Keeps bright regions, blacks out dark.

**Answer (gray-level quantization):** Reducing from 256 ($2^8$) to $L$ levels means dividing each pixel value by $\lfloor 256/L \rfloor$ (or right-shifting by $8 - \log_2 L$ bits). For $L = 16$: shift right by 4. **Result: visible posterization / banding** in smooth gradients. Lower $L$ = more banding but smaller storage.

**Answer (linear gray-level transformation):** Apply $\text{out} = a \cdot \text{in} + b$ pixelwise, clamp to [0, 255]. Three common variants:
- **Identity:** $a=1$, $b=0$ (no change).
- **Negative / inversion:** $\text{out} = 255 - \text{in}$.
- **Brightness shift:** $a=1$, $b=+50$ (brighter) or $b=-50$ (darker).
- **Contrast stretch:** $a > 1$, then clamp.
**Piecewise linear** = different $(a,b)$ in different intensity bands.

**Answer (histogram equalization):** Compute the **histogram** $h[k]$ = count of pixels with intensity $k$ (for $k = 0, \dots, 255$). Compute the **CDF** $H[k] = \sum_{j=0}^{k} h[j]$. The new pixel value is

$$\text{out}[i,j] = \left\lfloor \frac{H[\text{in}[i,j]] - H_{\min}}{N - H_{\min}} \cdot 255 \right\rfloor$$

where $N$ = total pixels and $H_{\min}$ = the smallest non-zero CDF value. **Effect: stretches contrast so that the histogram becomes ~uniform.**

### Hardware setup for Project 2 (real-time)

Per [Project 1 overview p.5](../../raw/labs/eee-404/lab-exam-prep/project1_overview.pdf):
- **USART2** is the serial path to MATLAB.
- **PA2 = USART2_TX** (board → PC), **PA3 = USART2_RX** (PC → board).
- Two USB ports needed: one for ST-Link programming, one for serial-to-USB converter.
- MATLAB script grabs webcam frame → sends pixels over UART → STM32 processes → STM32 sends back → MATLAB displays.

### Two implementation flavors

1. **C** — straightforward pixel loops.
2. **Hybrid inline assembly** — for hot inner loops (e.g., histogram increment, threshold compare).

> [!tip] **What to memorize vs. derive (Project 1).**
> **Memorize:**
> 1. Three thresholding types: global, band, semi (and what each preserves).
> 2. Histogram equalization = CDF-based stretch.
> 3. PA2/PA3 for USART2 serial communication.
>
> **Derive:**
> - The output of an arbitrary linear gray-level transform on a given pixel.
> - The histogram-equalization output for a given small image (mechanically: build histogram → CDF → apply formula).

**Same framework as:** [[fixed-point-arithmetic]] (the quantization-by-shift idea), the LUT pattern (used again in Lab 6 sine table).

---

## A.4 — Project 2: Applications of Fast Fourier Transform

> [!info] **Source:** [Project 2 lab manual](../../raw/labs/eee-404/project-2-lab-manual.pdf) · [Project 2 overview slides](../../raw/labs/eee-404/project-2-overview-slides.pdf) · **Full walkthrough already filed:** [[eee-404-project-2-walkthrough]] (refer to it during the exam).

### Framework — the 5 building blocks

1. **STFT pipeline:** window → zero-pad → real FFT → magnitude → bin-to-Hz mapping
2. **`arm_rfft_fast_f32` API** + the packed output format (DC and Nyquist co-located, then complex pairs)
3. **Magnitude / power spectrum** computation (square-and-add I and Q)
4. **`max_index` for fundamental-frequency / formant detection** (autocorrelation pitch detection in Project 2)
5. **Window function selection** (rect = best resolution / worst leakage; Hamming = better leakage)

### Headline answers to memorize

**Answer (CMSIS API call):** `arm_rfft_fast_init_f32(&S, FFT_LEN);` once at init, then `arm_rfft_fast_f32(&S, in, out, 0);` per frame. The `0` flag means **forward FFT**; `1` means inverse.

**Answer (packed output format):** For an $N$-point real FFT, output is also length $N$ but **packed**: `out[0]` = real part of DC ($X[0]$), `out[1]` = real part of Nyquist ($X[N/2]$), then complex pairs `out[2], out[3]` = real, imag of $X[1]$; `out[4], out[5]` = real, imag of $X[2]$; … This saves space because a real signal's DFT has conjugate symmetry.

**Answer (bin-to-Hz):** Bin $k$ corresponds to frequency $f_k = k \cdot f_s / N$. So the bin index of a target frequency $f$ is `k_target = round(f * N / fs)`.

**Answer (`max_index` for fundamental):** The fundamental frequency of a vowel is the **bin with the largest magnitude in the autocorrelation** (or equivalently the period that gives the largest peak in `IFFT(|FFT|²)`). For a vowel sampled at $f_s = 16$ kHz with $N = 1024$, vocal-fundamental range 80–400 Hz maps to bin range $\sim 5$–$26$.

**Answer (windowing tradeoff):** **Rectangular** has narrowest main lobe ($2 f_s/L$ Hz) but highest sidelobes (−13 dB). **Hamming** has wider main lobe ($4 f_s/L$ Hz) but much lower sidelobes (−41 dB). Use rectangular when resolution matters, Hamming when leakage matters.

> [!tip] **What to memorize vs. derive (Project 2).**
> **Memorize:**
> 1. `arm_rfft_fast_f32` API call + packed output layout (DC and Nyquist in slots 0,1).
> 2. Bin-to-Hz: $f_k = k f_s / N$.
> 3. Window comparison numbers (rect vs Hamming main-lobe widths and sidelobe heights).
>
> **Derive:**
> - The bin index for a given Hz.
> - Whether a given STFT setup can resolve two specified frequencies (use [[window-resolution-criterion]]).

**Same framework as:** [[eee-404-project-2-walkthrough]], [[eee-404-exam-2-walkthrough]] §P3, §P4, [[eee-404-hw5-walkthrough]], [[summary-eee-404-m11-effect-of-window-and-speech]].

---

## A.5 — Assembly Programming

> [!info] **Source:** [Exam 1 review](../../raw/other/eee-404/exam1_review.pdf) Problem 3 + [Exam 1 key](../../raw/other/eee-404/exam1_key.pdf). The announcement says: "format similar to Quiz 1 and Exam 1 Practice Exam Problem 3." That problem has 4 parts (ORR, LDRH, LDRSB, STRB) with addressing-mode variants.

### Framework — the 4 building blocks

1. **Register-shifted operands** (`ORR Rd, Rn, Rm, LSL #n`) — barrel shifter applied before the operation
2. **Load/store addressing modes** — pre-index, pre-index with update, post-index
3. **Sign-extending vs zero-extending** loads (`LDRSB`/`LDRSH` vs `LDRB`/`LDRH`)
4. **Endianness** — STM32F4 is little-endian (LSB at lowest address)

### Headline answers to memorize

**Answer (register shifts):** `LSL #n` left-shifts by $n$ bits before the ALU op. `LSL #4` is the same as multiplying by 16. `0xF012 5634 << 4 = 0x0125 6340` (the upper nibble `F` is shifted out; the right side gets a new `0` nibble).

**Answer (addressing modes — the table you must memorize):**

| Form | Effective address | Update Rn? | Notation |
|---|---|---|---|
| Immediate offset (no update) | `[Rn, #imm]` → `Rn + imm` | **No** | `LDR R0, [R1, #4]` |
| Pre-index with update (`!`) | `[Rn, #imm]!` → `Rn + imm` | **Yes** (Rn ← Rn+imm before access) | `LDR R0, [R1, #4]!` |
| Post-index | `[Rn], #imm` → `Rn` (then update) | **Yes** (Rn ← Rn+imm **after** access) | `LDR R0, [R1], #4` |

**Answer (sign-extension on `LDRSB`):** `LDRSB Rd, [Rn]` loads ONE byte from memory into the lower 8 bits of `Rd`, then **sign-extends** to all 32 bits. If the byte's MSB is 1 (e.g., `0xF0`), the upper 24 bits of `Rd` become `0xFFFFFF` → final `Rd = 0xFFFFFFF0`. If MSB is 0, upper bits are 0.

**Answer (`STRB` — store byte):** `STRB Rd, [Rn, #imm]` writes the **least significant byte** of `Rd` to memory. Upper 24 bits of `Rd` are ignored. Pre-index without `!` does **not** update `Rn`.

### The Exam-1-Problem-3 walkthrough (reuse this format on tomorrow's question)

For each instruction, ask in this order:

1. **What is the operation?** (load, store, logical, shift)
2. **What is the operand size?** (B = 8-bit byte; H = 16-bit halfword; word = 32-bit; S-prefix = signed/sign-extend)
3. **What is the addressing mode?** (immediate, pre-index, pre-index-with-update `!`, post-index)
4. **What is the effective address?** (Rn ± offset, or Rn alone for post-index)
5. **What changes?** (Rd, Rn-after-update, or memory location — list each)

**Worked example** (from [Exam 1 key](../../raw/other/eee-404/exam1_key.pdf)):

`LDRH R0, [R1, #4]!` with `R1 = 0x2000 8000`, memory `[0x2000 8004] = 0x78`, `[0x2000 8005] = 0x56`.
- Operand: H = 16-bit halfword (zero-extend, since no S).
- Addressing mode: pre-index **with update** (the `!`).
- Effective address: `R1 + 4 = 0x2000 8004`.
- Halfword at `0x2000 8004` (little-endian): low byte `0x78` at addr 4, high byte `0x56` at addr 5 → halfword value `0x5678`.
- **R0 ← 0x0000 5678** (zero-extended into upper 16 bits).
- **R1 ← 0x2000 8004** (updated because of `!`).

> [!tip] **What to memorize vs. derive (Assembly).**
> **Memorize:**
> 1. The addressing-mode table above (pre-index / pre-index-with-update / post-index).
> 2. Little-endian: low byte at low address.
> 3. `S` prefix on loads = sign-extend.
> 4. `LSL #n` = multiply by $2^n$ (if no overflow).
>
> **Derive:**
> - The effective address and updated registers for any instruction (use the 5-step checklist above).
> - The hex value at a memory location after little-endian reassembly.

**Same framework as:** [Exam 1 Problem 3](../../raw/other/eee-404/exam1_review.pdf), Quiz 1, [[summary-eee-404-exam-2-review]] (no overlap — Exam 2 didn't test ARM ISA).

---

# §B — ABET QUIZ (50 pts, 30 min, closed book + 2 sheets)

> [!example] **Format anchor.** **Comprehensive paper quiz covering the entire semester.** Mix of multiple choice, true/false, fill-in-the-blank, and short essay. Closed book except for **two 8.5×11 sheets** (you have already filled one for [[eee-404-exam-2-walkthrough|Exam 2]] — bring it; build the second to cover Modules 1, 2, 4, 5, 9). Calculator allowed.

## B.1 — Master Cheat Sheet (the second 8.5×11 you must build tonight)

> [!warning] **Build this on PAPER tonight before bed.** Do not try to memorize it raw. The act of writing it cements recall. Suggested layout: three columns × two pages (front+back of one sheet, or one sheet each side). Sheet 1 = the existing [[eee-404-exam-2-study-guide|Exam 2 cheat sheet]] (Modules 6, 7, 8, 10, 11). Sheet 2 = the content below (Modules 1, 2, 4, 5, 9 — the Exam 1 + lab/project material).

### B.1.1 — Sampling, LTI, Convolution (Module 1)

**Nyquist rate:** to avoid aliasing, $f_s \geq 2 f_{\max}$. **Minimum** sampling rate = $2 f_{\max}$.

**Continuous → discrete frequency conversion:**
$$\omega = 2\pi f / f_s \quad [\text{rad/sample}], \qquad F = f / f_s \quad [\text{cycles/sample}]$$

For $x(t) = A\cos(\Omega t)$ at sampling rate $f_s$: $x[n] = A\cos(\omega n)$ where $\omega = \Omega / f_s$ (radians) or $F = \Omega / (2\pi f_s)$ (cycles). **Worked example:** $x(t) = 1.6\cos(10\pi t)$ at $f_s = 20$ Hz → $f_{\max} = 5$ Hz, Nyquist rate = 10 Hz. With $f_s = 20$: $\omega = 10\pi/20 = 0.5\pi$ rad/sample → $x[n] = 1.6\cos(0.5\pi n)$ → values $\{1.6, 0, -1.6, 0, \dots\}$.

**Linear convolution** of $x[n]$ (length $L_1$) with $h[n]$ (length $L_2$) has output length $L_1 + L_2 - 1$. **Region of support** = where output is non-zero.

**Circular convolution** ($N$-point) wraps both signals to length $N$ and convolves modulo $N$. **Equality with linear convolution** requires $N \geq L_1 + L_2 - 1$.

**LTI properties:** linearity (homogeneity + additivity), time-invariance. **Impulse response** $h[n]$ characterizes any LTI completely: $y[n] = x[n] * h[n]$.

**FIR vs IIR (from impulse response):** **FIR** has finite-length $h[n]$. **IIR** has infinite-length $h[n]$ (because of recursive feedback).

### B.1.2 — Number Representation (Module 4)

**Qm.n format (2's complement, $m+n+1$ bits including sign):**
- **Range:** $-2^m$ to $2^m - 2^{-n}$.
- **Precision (resolution):** $2^{-n}$.
- **Conversion to binary:** integer-encode $\lfloor x \cdot 2^n \rceil$ in 2's complement.

**4-bit Q-formats** (1 sign bit + 3 magnitude/fractional bits):

| Format | Range | Precision |
|---|---|---|
| Q3.0 | $-8$ to $+7$ | 1 |
| Q2.1 | $-4$ to $+3.5$ | 0.5 |
| Q1.2 | $-2$ to $+1.75$ | 0.25 |
| Q0.3 | $-1$ to $+0.875$ | 0.125 |

**Highest-precision Q-format that represents $|x|_{\max}$:** pick the Q-format whose positive range $\geq |x|_{\max}$ AND whose precision is finest. **Worked example:** $x = 1.6$ → Q3.0 (range 7) and Q2.1 (range 3.5) and Q1.2 (range 1.75) all fit; **Q1.2 has finest precision** (0.25), so Q1.2 it is. (Q0.3's range only 0.875 < 1.6, doesn't fit.)

**Q1.2 representation of 1.6:** $1.6 \cdot 4 = 6.4 \to$ round to 6 = `0110` = `01.10`. Recovers as $6/4 = 1.5$. **Quantization error = $|1.6 - 1.5| = 0.1$.**

**Multiplication of Q1.2 × Q1.2:** product is in **Q2.4** (sums the integer-bits, sums the fractional-bits). To convert back to Q1.2: arithmetic right-shift by 2, take low 4 bits. **Use 8-bit double-precision intermediate to prevent overflow.**

**Single-precision floating point** (IEEE 754):
- Format: $(-1)^S \cdot 1.M \cdot 2^{E - 127}$
- 1 sign bit + 8 exponent bits + 23 mantissa bits.
- **Bias = 127** (subtract from stored E to get true exponent).
- **Mantissa is implicit-1 normalized** ($1.M$).

**Worked examples** (from [Exam 1 key](../../raw/other/eee-404/exam1_key.pdf)):
- $0.3125 = 1.25 \cdot 2^{-2}$ → S=0, E=125 = `0111 1101`, M = 0.25 → `0 01111101 01000000000000000000000`.
- $14 = 1.75 \cdot 2^3$ → S=0, E=130 = `1000 0010`, M = 0.75 → `0 10000010 11000000000000000000000`.

### B.1.3 — ARM Cortex-M4 Instructions (Module 2)

**Cheat-sheet block** (copy these onto your sheet — same content as §A.5 but compressed):

| Instruction | What it does |
|---|---|
| `ORR Rd, Rn, Rm, LSL #n` | `Rd = Rn \| (Rm << n)` |
| `LDR R0, [R1, #4]` | `R0 = *(R1+4)`, R1 unchanged |
| `LDR R0, [R1, #4]!` | R1 ← R1+4, then `R0 = *R1` |
| `LDR R0, [R1], #4` | `R0 = *R1`, then R1 ← R1+4 |
| `LDRB` / `LDRH` | Load byte/halfword, zero-extend |
| `LDRSB` / `LDRSH` | Load byte/halfword, **sign-extend** |
| `STRB Rd, [Rn, #imm]` | Store low byte of Rd to memory |
| Endianness | **Little-endian** (LSB at lowest address) |

**Subroutine call standard (AAPCS):**
- **R0–R3** = argument / return registers (caller-saved).
- **R4–R11** = local variables (callee-saved — push to stack on entry, pop on exit).
- **R13 = SP** (stack pointer), **R14 = LR** (link register), **R15 = PC** (program counter).
- `BL label` = branch with link (saves return address in LR, then PC ← label).
- `BX LR` = branch to address in LR (return).

### B.1.4 — Image Processing (Module 5)

(Already in §A.3 — copy the four bullets to your sheet.)

- **Thresholding:** global / band / semi.
- **Quantization:** divide pixel by $\lfloor 256/L \rfloor$, or right-shift by $8 - \log_2 L$.
- **Linear gray-level transform:** $\text{out} = a \cdot \text{in} + b$ (clamp).
- **Histogram equalization:** $\text{out} = \lfloor (H[\text{in}] - H_{\min}) / (N - H_{\min}) \cdot 255 \rfloor$.

### B.1.5 — Music Synthesis & Audio (Module 9 + Lab 5/6 hardware)

- **Phase increment:** $\Delta\phi = f_0 L / f_s$.
- **ADSR:** Attack → Decay → Sustain → Release.
- **Sample rate:** 16 kHz everywhere. **Lab 5 callback:** every 1 ms (16 samples). **Lab 6 callback:** every 32 ms (512 samples).
- **DMA half/complete callback** model.
- **PDM (mic) → PCM (computation) → I²S (DAC)** is the audio chain.
- **AM modulation (from Module 9 sinusoidal synthesis):** $y(t) = (1 + m \cdot s(t)) \cos(2\pi f_c t)$ where $m$ = modulation index.

### B.1.6 — Memorize-cold list (the always-on facts)

1. $f_s \geq 2 f_{\max}$ (Nyquist).
2. $\omega = 2\pi f / f_s$.
3. Linear conv length = $L_1 + L_2 - 1$.
4. **Direct DFT** = $N^2$ complex mults; **FFT** = $\frac{N}{2}\log_2 N$ butterflies; **speedup** $= 2N/\log_2 N$.
5. Bin-to-Hz: $f_k = k f_s / N$.
6. **DTFT exists** ⟺ ROC contains the unit circle.
7. **Causal stable** ⟺ all poles strictly inside unit circle.
8. **DF-I storage** = $M+N$; **DF-II storage** = $\max(M,N)$.
9. **Real $x[n]$:** $X[N-k] = X^*[k]$.
10. **Window resolution:** rect $= 2 f_s/L$, Hamming $= 4 f_s/L$.
11. **Floating-point bias** = 127.
12. **ARM little-endian.** Pre-index `[R1,#4]` no update; `[R1,#4]!` updates; `[R1],#4` post-index update.
13. **Histogram equalization** uses the CDF as the remapping function.
14. **ADSR** = attack-decay-sustain-release (in that order).
15. **PDM mic + I²S + DMA + 16 kHz + 1 ms callback** is the entire Lab 5/6 hardware story.

## B.2 — Likely short-essay prompts (rehearse one-paragraph answers)

> [!tip] **Strategy for short-essay items.** ABET cares about *conceptual* understanding, not derivations. One-paragraph answers (3–5 sentences) are right-sized. Lead with the headline claim, then 2 supporting reasons, then a 1-sentence application/example. **Bold the headline.**

**Q1: "Explain the difference between FIR and IIR filters and when you'd choose each."**
> **FIR filters use only feedforward taps; IIR filters use feedback.** FIR has a finite-length impulse response ($h[n] = 0$ outside a finite window) and is **always stable**, but typically needs a higher tap count for sharp frequency responses. IIR has infinite-length impulse response from its recursive structure, achieves sharp transitions with far fewer coefficients, but **can go unstable if poles fall outside the unit circle**. **Use FIR** when stability and linear phase matter (e.g., audio crossover); **use IIR** when computation budget is tight and you can verify pole locations (e.g., echo reverb on the STM32).

**Q2: "Explain why we use windowing before computing a DFT."**
> **A finite-length DFT implicitly multiplies the signal by a rectangular window, which causes spectral leakage.** When the signal frequency doesn't align with a DFT bin, the rectangular window's wide sidelobes spread that energy into adjacent bins, masking nearby weaker tones. **Applying a tapered window (Hamming, Hann, Blackman) reduces sidelobe height** at the cost of a wider main lobe. The tradeoff is **resolution vs. dynamic range**: rectangular gives the narrowest main lobe (best two-tone resolution); Hamming gives ~30 dB lower sidelobes (best for revealing weak tones).

**Q3: "Compare fixed-point and floating-point implementations on the STM32F4."**
> **Fixed-point is faster on the Cortex-M4 but requires manual scaling; floating-point is easier to write but spends more cycles per multiply-add.** The Cortex-M4 has hardware single-precision FPU but no double-precision FPU, so fast float math is limited to single-precision. Fixed-point uses Q-format (e.g., Q1.15) — every multiply produces a higher-precision intermediate (Q2.30) that must be shifted and saturated back. **Use fixed-point** for hot inner loops where every cycle matters (real-time filters at 16 kHz); **use floating-point** for prototyping and for code paths where headroom and dynamic range matter more than speed.

**Q4: "Describe the FFT and explain why it is faster than the direct DFT."**
> **The FFT computes the same DFT with $O(N \log N)$ operations instead of $O(N^2)$ by exploiting twiddle-factor periodicity.** A radix-2 decimation-in-time FFT splits the $N$-point DFT into two $N/2$-point DFTs of the even-indexed and odd-indexed samples, recursively. Each stage requires $N/2$ butterfly operations; there are $\log_2 N$ stages, totaling $\frac{N}{2} \log_2 N$ butterflies. **At $N = 1024$, the speedup is roughly $2N/\log_2 N \approx 205\times$** — what would take seconds becomes milliseconds, enabling real-time spectral analysis on a microcontroller.

**Q5: "What is histogram equalization and why does it improve image contrast?"**
> **Histogram equalization remaps pixel intensities through the cumulative distribution function (CDF) so that the output histogram is approximately uniform.** When an image has all its pixels concentrated in a narrow intensity range (low contrast), the CDF is steep in that range and shallow elsewhere; remapping by the CDF stretches the busy range over the full [0, 255] output, which **redistributes contrast**. The technique is a non-parametric, content-adaptive contrast stretch — automatically stronger where the image needs it. It can over-amplify noise in dark regions, so it's often combined with local windowing (CLAHE).

## B.3 — True/False reflexes (rehearse the trap patterns)

> [!warning] **The 6 most common T/F traps from Dr. Wang's question style.** Mark T/F, then in your head say *why* in 5 words.

| # | Statement | T/F | Why |
|---|---|---|---|
| 1 | "FIR filters can be unstable for the wrong coefficient choice." | **F** | FIR has no feedback poles |
| 2 | "Sampling a 5 Hz cosine at 8 Hz aliases it." | **T** | Need ≥ 10 Hz |
| 3 | "Q1.2 has the same range as Q2.1." | **F** | Q1.2 range is half |
| 4 | "Zero-padding improves frequency resolution." | **F** | It interpolates the DTFT, doesn't add information |
| 5 | "An IIR filter's pole at $|z| = 1$ is marginally stable." | **T** | But not BIBO stable |
| 6 | "A real-valued signal's DFT has $X[k] = X^*[N-k]$." | **T** | Conjugate symmetry |
| 7 | "The Cortex-M4 stores multi-byte values big-endian." | **F** | Little-endian |
| 8 | "An $N$-point FFT has $\log_2 N$ stages." | **T** | Standard radix-2 |
| 9 | "Histogram equalization preserves the original mean intensity." | **F** | It pushes the histogram toward uniform |
| 10 | "ReLU on a negative pre-activation outputs the negative number." | **F** | ReLU outputs 0 |

## B.4 — Fill-in-the-blank reflexes

| Stem | Answer |
|---|---|
| The Nyquist rate of a 5 Hz cosine is ___ Hz. | 10 |
| An $N$-point FFT requires ___ butterflies. | $\frac{N}{2}\log_2 N$ |
| For a real signal, $X[N-k] = $ ___. | $X^*[k]$ |
| The bias of single-precision float is ___. | 127 |
| A direct DFT requires ___ complex multiplications. | $N^2$ |
| The frequency resolution of a Hamming-windowed DFT is ___ Hz. | $4 f_s / L$ |
| `LDRSB R0, [R1]` loads a ___-bit value and ___-extends it. | 8, sign |
| ADSR stands for ___, ___, ___, ___. | Attack, Decay, Sustain, Release |
| Histogram equalization remaps pixels using the ___ as the transfer function. | CDF |
| The address-mode notation `[R1, #4]!` means ___. | Pre-index with update |
| The smallest sampling rate to reconstruct $x(t) = \cos(20\pi t)$ is ___ Hz. | 20 (since $f_{\max} = 10$, Nyquist = 20) |
| The phase increment for a 1 kHz tone at 16 kHz with a 1024-entry table is ___. | 64 |

---

# §C — Pre-Exam Routine (tonight + tomorrow morning)

## C.1 — Tonight (2026-05-04 evening)

> [!example] **Tonight's plan.** Capacity allocation for a busy day. You also have the EEE 335 final tomorrow afternoon, so don't burn yourself out on EEE 404.

1. **45 min — Build the second 8.5×11 sheet.** Use §B.1 above. Hand-write it; the act of writing is the rehearsal.
2. **20 min — Re-read [[eee-404-project-2-walkthrough]].** That walkthrough was filed today; it covers the Project 2 multiple-choice question entirely.
3. **15 min — Re-do [Exam 1 Problem 3](../../raw/other/eee-404/exam1_review.pdf)** (4 ARM instructions) freehand without the key. Then check against §A.5 + the [Exam 1 key](../../raw/other/eee-404/exam1_key.pdf).
4. **10 min — Skim §B.3 + §B.4** (T/F + fill-in reflexes). These are the lowest-effort point grabs on the ABET quiz.
5. **STOP.** Sleep. The EEE 335 final is at 12:10 — don't sacrifice sleep.

## C.2 — Tomorrow morning (2026-05-05)

> [!example] **Pre-exam morning.** Don't try to learn anything new. Reinforce, then go.

1. **08:30 — Wake up. Eat breakfast.** Coffee.
2. **09:00–09:30 — Rehearse the 15 always-on facts** (§B.1.6). Recite them out loud once. If any are wobbly, re-read just that line on the cheat sheet.
3. **09:30–09:45 — Walk to exam room.** Bring: laptop (charged + charger), 2× 8.5×11 sheets, calculator, ID, water.
4. **09:50–11:40 — Lab Exam (15 min) → ABET Quiz (30 min) → bank time.**
5. **11:40 — Submit. Walk to SCOB 250 for EEE 335.** Use the bank time to grab lunch before the EEE 335 final.

---

# Related

- [[eee-404]] — course home (master roadmap)
- [[eee-404-exam-2-walkthrough]] — Exam 2 per-problem walkthrough (deeper on Modules 6, 7, 8, 10, 11)
- [[eee-404-exam-2-study-guide]] — the existing 8.5×11 cheat sheet for the Exam 2 sheet (use as Sheet 1)
- [[eee-404-project-2-walkthrough]] — Project 2 walkthrough (open during the lab exam)
- [[eee-404-hw5-walkthrough]] — HW5 walkthrough (window-resolution + FFT-budget intuition)
- [[lab-eee-404-project-2-fft-applications]] — Project 2 source summary
- [[summary-eee-404-m6-neural-networks]] — Module 6 (NN)
- [[summary-eee-404-m7-frequency-domain]] — Module 7 (DTFT/DFT/Z)
- [[summary-eee-404-m8-difference-equation]] — Module 8 (filter implementation, Lab 5 backbone)
- [[summary-eee-404-m10-butterfly]] — Module 10 (FFT)
- [[summary-eee-404-m11-effect-of-window-and-speech]] — Module 11 (windowing + speech)
- [[summary-eee-404-exam-2-review]] — Exam 2 practice exam summary
- [[chao-wang]] — instructor

**Source files** (all on Canvas):
- [Lab 5 overview slides](../../raw/labs/eee-404/lab-exam-prep/lab5_overview.pdf)
- [Lab 6 overview slides](../../raw/labs/eee-404/lab-exam-prep/lab6_overview.pdf)
- [Project 1 overview slides](../../raw/labs/eee-404/lab-exam-prep/project1_overview.pdf)
- [Project 2 lab manual](../../raw/labs/eee-404/project-2-lab-manual.pdf)
- [Exam 1 review](../../raw/other/eee-404/exam1_review.pdf) + [Exam 1 key](../../raw/other/eee-404/exam1_key.pdf)
- [Exam 2 review](../../raw/other/eee-404/exam2_review.pdf)
