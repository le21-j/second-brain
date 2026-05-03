---
title: EEE 404 Project 2 — Applications of FFT (Walkthrough)
type: walkthrough
course: [[eee-404]]
tags: [eee-404, project, fft, stft, windowing, vowel-analysis, pitch-detection, formant, stm32, cmsis, walkthrough]
sources: [[lab-eee-404-project-2-fft-applications]]
created: 2026-05-02
updated: 2026-05-02
---

# EEE 404 Project 2 — Applications of FFT (Walkthrough)

> [!example] What this project actually is
> Two FFT-based DSP applications running on the STM32F407 board. Task 1 finds the **pitch** (fundamental frequency) of a vowel via autocorrelation and reads its **formants** off the FFT — proving you understand the difference between excitation and vocal-tract envelope. Task 2 streams a **real-time spectrum** of the on-board MEMS mic over UART and compares **windowing** options. Total student-written code: **two C functions** (`max_index`, `apply_window`) and **four FILL_IN_BLANK lines**. Everything else (DMA, audio I/O, MATLAB receiver) is given.

## Sources

- Assignment PDF: [`raw/labs/eee-404/project-2-lab-manual.pdf`](../../raw/labs/eee-404/project-2-lab-manual.pdf)
- Starter code: [`raw/labs/eee-404/project-2-code/`](../../raw/labs/eee-404/project-2-code/)
- Source summary: [[lab-eee-404-project-2-fft-applications]]
- Concepts you'll lean on: [[fft]], [[real-valued-fft]], [[cmsis-dsp-fft]], [[stft]], [[window-function]], [[hamming-window]], [[hann-window]], [[rectangular-window]], [[autocorrelation-pitch-detection]], [[formant]]

---

# Task 1 — Vowel analysis

## **1.1) Record vowel sounds in Audacity**

> [!info] What you're doing
> Producing two `.wav` files of you holding a vowel for ~5 seconds. These get fed into MATLAB (Task 1.2) and converted into the C header arrays `vowel_a.h` / `vowel_i.h` (Task 1.3). Pre-recorded examples are on Canvas if your mic flakes.

**Steps:**

1. Install Audacity from <https://www.audacityteam.org/download/>.
2. Open Audacity. Set **Project Sample Rate** (bottom-left dropdown) to **16000 Hz** — anything you record will get downsampled to 8 kHz in MATLAB anyway, so 16 kHz is plenty and keeps file sizes small.
3. Click record (red dot). Hold **"a" as in *father*** for ~5 seconds. Stop.
4. **File → Export → Export as WAV → save as `a.wav`** in your project folder. Choose `Signed 16-bit PCM` if asked.
5. Repeat for **"i" as in *see***, save as `i.wav`.

> [!tip] Mic discipline
> Keep the mic 6 inches from your mouth, hold the vowel **steady** (don't slide pitch or vary loudness), and stay in a quiet room. The middle 0.5 s of the recording is what MATLAB will analyze, so the *middle* is what has to be clean.

---

## **1.2) Analyze vowel sounds in MATLAB and fill the table**

**Answer (preview): you will read $F_1$ and $F_2$ off the FFT plot, read pitch off the autocorrelation plot, and verify pitch from the printed `pitch` line in the command window.**

### What the script does (top-down)

The provided `vowel_analysis.m` does five things on each vowel `.wav`:

1. Resamples to $f_s = 8000$ Hz, averages the stereo channels.
2. Plots a **spectrogram** of the whole recording (top-left subplot) — sanity check that the vowel is steady.
3. Extracts the middle 512 samples and writes them into a **C header file** (`vowel_a.h` or `vowel_i.h`). This is what Task 1.3 will compile into the MCU project.
4. Plots the **time-domain samples** (top-right) and the **double-sided FFT magnitude squared** (bottom-left).
5. Computes the **autocorrelation** as $\mathrm{IFFT}(|\mathrm{FFT}(x)|^2)$, plots it (bottom-right), finds the first non-trivial peak, and prints `pitch = ... Hz`.

### Run it

```matlab
% in MATLAB, in the folder containing vowel_analysis.m and a.wav
edit vowel_analysis.m   % change file_name to 'a.wav' (already done) -- run
% then change line 26 to file_name = 'i.wav'
% AND change lines 47-48 to write vowel_i.h with variable vowel_i
% (the comment on line 46 reminds you of this)
% re-run for 'i'
```

> [!warning] You must edit the script twice
> The script writes `vowel_a.h` with `float vowel_a[512] = {...}` by default. For the "i" vowel you have to flip three things on lines 26, 47, 48: file name to `i.wav`, header to `vowel_i.h`, array name to `vowel_i`. Otherwise the second run overwrites the "a" header, and the MCU project won't build (it includes both `vowel_a.h` and `vowel_i.h`).

### Reading the FFT plot — formants

Click anywhere on the bottom-left subplot ("FFT") in MATLAB's plot window, then use the **Data Cursor** tool (the icon that looks like a "+" in a tooltip) and click on each major **envelope peak** in the positive-frequency half. The first two visible peaks are $F_1$ and $F_2$.

> [!tip] Don't pick a harmonic — pick the envelope peak
> The FFT of a steady vowel looks like a *comb* (the harmonics of $f_0$, spaced at every $\sim 100$ Hz) modulated by a smooth *envelope* (the formants). Click on the **broad bumps**, not the individual comb teeth. If two adjacent comb teeth are about the same height, the formant is between them.

### Reading the autocorrelation plot / command line — pitch

The bottom-right subplot is the autocorrelation $r[k]$. The *first* prominent peak after lag 0 is at index $k_0$. The pitch is

$$f_0 = \frac{f_s}{k_0} = \frac{8000}{k_0}\ \text{Hz}.$$

The script computes this for you and prints e.g.:

```
Estimated pitch is at index 73 (starting from 0) with frequency at 109.589041 Hz.
```

That printed Hz value is the **Calculated** column in the deliverable table.

### Fill the deliverable table

Reasonable ranges to sanity-check against (your numbers will vary by gender, accent, mic):

| Vowel | $F_1$ (Hz) | $F_2$ (Hz) | Pitch $f_0$ (typical) |
|---|---|---|---|
| "a" (*father*)  | $700$–$850$    | $1000$–$1200$   | adult male $\sim 110$, female $\sim 220$ |
| "i" (*see*)     | $250$–$320$    | $2200$–$2700$   | (same — pitch doesn't change with vowel) |

Reference chart: <https://linguistics.ucla.edu/people/hayes/103/Charts/VChart/>

> [!note] Why $F_1$ and $F_2$ change but pitch doesn't
> Pitch is set by your **vocal-cord vibration rate** — that's "you," not "the vowel." Formants are set by your **mouth/tongue shape** — different vowels = different shapes = different formants. See [[formant]] and [[autocorrelation-pitch-detection]] for the full theory.

**Deliverable:** fill all four numeric columns of the table for both vowels, and paste the four-pane MATLAB plot (subplots 2×2: spectrogram / time / FFT / autocorrelation) into the report.

---

## **1.3) Implement `max_index` on the microcontroller**

**Answer: a five-line linear scan over the array, tracking the max value seen and the index where it was seen.** The function lives at the bottom of `vowel_analysis/main.c` (line 393), and `main()` calls it at line 184 to find the index of the largest **non-self-correlation** peak — which is the pitch period in samples.

### Where it's called

```c
// vowel_analysis/main.c  (line 184)
pitch_peaks_index = max_index(&(peaks[index_offset]), num_peaks - index_offset);
```

`peaks[]` is a deduplicated list of every local maximum of the autocorrelation. `index_offset` is 0 or 1 — set to 1 only if the very first peak happens to sit at lag 0 (the trivial self-correlation peak), in which case we slide the start by 1 to ignore it. So `max_index` only ever sees peaks that *might* be the real pitch peak.

### The implementation

> [!info]- 📐 Show derivation — why a plain linear scan is enough
>
> Finding the maximum of a length-$L$ array takes $O(L)$ time. There is no faster algorithm in the comparison model — every element has to be looked at at least once or you can't rule it out as the max. CMSIS does ship `arm_max_f32` which uses SIMD for the same task, but the assignment explicitly asks you to **write `max_index` yourself**, so use plain C. Cortex-M4 is fast enough that the difference is invisible at $L \leq 256$.

Drop this in at line 393 (replacing the empty body):

```c
// find the index of the maximum element of an array
uint32_t max_index(float32_t* x, uint32_t length)
{
    uint32_t   idx     = 0;
    float32_t  max_val = x[0];
    for (uint32_t i = 1; i < length; i++) {
        if (x[i] > max_val) {
            max_val = x[i];
            idx     = i;
        }
    }
    return idx;
}
```

> [!warning] Initialize from `x[0]`, not `0.0f` or `-INFINITY`
> Autocorrelation values can be very small but they are still non-negative for a periodic signal. Initializing `max_val = 0.0f` would still work here (because `r[k] >= 0` after the IFFT in this script) but **it's a brittle pattern** — if you ever reuse `max_index` on a signed array, it'll silently return index 0 for an all-negative input. Initializing from `x[0]` is the correct invariant.

### Verify on hardware

1. Build the `vowel_analysis` project in STM32CubeIDE (be sure both `vowel_a.h` and `vowel_i.h` from MATLAB are in `Core/Inc/` of the project — the script wrote them to the MATLAB working directory; **copy them** into the IDE project).
2. The starter code on line 118 reads `X[i] = vowel_i[i];` — that hard-codes the **"i" vowel**. To test "a", change line 118 to `X[i] = vowel_a[i];`. Recompile.
3. Set a breakpoint on `pitch_freq = 1/(pitch_index/fs);` (line 188) or after it. Run in **Debug** mode.
4. Right-click `pitch_index` and `pitch_freq` in the Variables view → **Add Watch**. Step over line 188; the values should populate.
5. Compare against MATLAB: `pitch_index` should match MATLAB's `max_index` printed value, and `pitch_freq` should match MATLAB's `pitch` (in Hz).

> [!tip] Sanity check: integer division gotcha on line 188
> `pitch_index/fs` divides a `uint32_t` by a `float`. C's usual arithmetic conversions promote `pitch_index` to `float` before the divide, so you get the right answer. **But if you ever rewrite this** as e.g. `pitch_index/(int)fs`, you get integer truncation and a junk frequency. Trust the original line as-is.

**Deliverable:** screenshots of (a) the IDE window with `pitch_index` and `pitch_freq` visible in the Watch panel, one each for "a" and "i", and (b) MATLAB command-line output showing the matching values. Plus the source of `max_index` pasted into the report's code section.

---

# Task 2 — Real-time spectrum analyzer

## **2.1) Fill the four `FILL_IN_BLANK` lines**

**Answer: one line in `main.c` (initialize the FFT) and three lines in `waverecorder.c` (window, FFT, |·|² in the packed format).** Each one corresponds to a stage of the [[stft]] pipeline.

### Pipeline this implements

```
mic PDM ──► PCM ──► copy to FFTInBuffer ──► [WINDOW] ──► [FFT] ──► [|Y|² packed] ──► dB ──► UART
                                              ↑              ↑           ↑
                                          BLANK #2       BLANK #3    BLANK #4
                                                            ↑
                                                        BLANK #1 (init in main)
```

### Blank 1 — `audio_spectrum_analyzer/Core/Src/main.c:109`

```c
// FILL_IN_BLANK: initialize the FFT structure
arm_rfft_fast_init_f32(&fft_handler, FFT_SIZE);
```

> [!note] Why this line exists
> The CMSIS forward/inverse calls below will reach into `fft_handler` for twiddle-factor tables and bit-reversal tables. Those tables are size-dependent, so they're set up by the init call once at startup. `FFT_SIZE` is `#define`'d as `1024` in `main.h`. See [[cmsis-dsp-fft]] for the full API.

### Blank 2 — `Core/Src/waverecorder.c:147` (apply window)

```c
// FILL_IN_BLANK: apply window, comment out this line is equivalent to rectangular window
apply_window(FFTInBuffer, hamming, FFT_SIZE);
```

(Or `hanning` instead of `hamming` — both header arrays are 1024 floats. Swap to test the other window. Comment out for rectangular.)

> [!info]- 📐 Show derivation — why we window before the FFT
>
> The DFT assumes the input is **periodic with period $N$**. Real audio frames usually aren't — the last sample doesn't equal the first. The discontinuity at the wrap-around point smears energy across many bins (**spectral leakage**). A window function $w[n]$ that tapers to zero at the edges removes the discontinuity, at the cost of a wider mainlobe.
>
> Concretely: if $x[n] = \cos(\omega_0 n)$ at frequency $\omega_0$, then a length-$N$ rectangular window gives a spectrum that's a sinc shifted to $\pm \omega_0$ — sidelobes only $-13$ dB down. Multiplying by Hamming shifts the sidelobe floor to about $-43$ dB and broadens the mainlobe by $\sim 2\times$. See [[hamming-window]] vs [[rectangular-window]].

### Blank 3 — `waverecorder.c:150` (forward FFT)

```c
// FILL_IN_BLANK: FFT forward transform
arm_rfft_fast_f32(&fft_handler, FFTInBuffer, FFTOutBuffer, 0);
```

The last argument `0` means **forward**. (Inverse would be `1`.) The output `FFTOutBuffer` is in the CMSIS packed format described in [[cmsis-dsp-fft]] — bin 0 is in slot 0, bin $N/2$ is in slot 1, then bins $1, 2, \dots, N/2-1$ are in `(re, im)` pairs starting at slot 2.

### Blank 4 — `waverecorder.c:168` (compute |·|²)

```c
// FILL_IN_BLANK: compute spectrum (amplitude squared) = real^2 + imaginary^2
spectrum = FFTOutBuffer[i] * FFTOutBuffer[i] + FFTOutBuffer[i+1] * FFTOutBuffer[i+1];
```

Inside the loop, `i` steps by 2, so `FFTOutBuffer[i]` is the real part and `FFTOutBuffer[i+1]` is the imaginary part of bin `i/2`. The next line in the source already converts to dB and subtracts a 60 dB noise-floor offset.

> [!warning] What about bin 0 and bin $N/2$?
> Bin 0 is handled **outside** this loop on line 179 (`SerialOutBuffer[1] = ... FFTOutBuffer[0]*FFTOutBuffer[0] ...`). Bin $N/2$ (Nyquist) is *not* sent over UART because the MATLAB receiver only plots `SIZE = 512` bins (= `FFT_SIZE/2 = 1024/2`), running from DC up to but not including Nyquist. Don't add an extra correction line — the starter code already handles bin 0 correctly.

---

## **2.2) Implement `apply_window`**

**Answer: an element-wise in-place multiply of the signal segment by the window samples.**

`apply_window` lives at the bottom of `waverecorder.c` (line 203). Replace the empty body with:

```c
// apply window to the data segment
void apply_window(float* signal_segment, float* window_function, uint16_t length)
{
    for (uint16_t i = 0; i < length; i++) {
        signal_segment[i] = signal_segment[i] * window_function[i];
    }
}
```

That's it. Three lines.

> [!info]- 📐 Show derivation — why "in-place" is correct here
>
> The caller passes `FFTInBuffer` for `signal_segment`. After this function returns, `FFTInBuffer[i]` holds $w[i] \cdot x[i]$. The very next line (`arm_rfft_fast_f32(...)`) reads `FFTInBuffer` as input and writes `FFTOutBuffer` as output, so the original samples don't need to be preserved. In-place is fine and saves 1024 × 4 = 4 KB of RAM.
>
> If you ever wrote this loop and *also* needed the original samples afterwards, you'd allocate a separate `WindowedBuffer[]` and write `WindowedBuffer[i] = signal_segment[i] * window_function[i];` — but that's a different design, not what this project wants.

---

## **2.3) Run it with the online tone generator**

> [!example] Setup
> 1. Connect the **PA2 (USART2_TX) → RXD** and **GND → GND** between the STM32 board and your USB-to-serial adapter (per the lab manual photo). PE14 ↔ PB10 jumper for the mic clock should already be in place from prior labs.
> 2. Plug the USB adapter into your computer; check Device Manager → Ports for its assigned `COM` number.
> 3. Edit `uart_receive_fft_plot_spectrum.m` line 23 — change `'COM31'` to your actual COM port number.
> 4. **Order matters**: in STM32CubeIDE, set the project to **Debug** mode (not Run). Build → Debug. The IDE will pause at `main()`. **Now** start the MATLAB script (`run uart_receive_fft_plot_spectrum`). MATLAB will block on `serialport()` waiting for the board. **Then** hit Resume in the IDE.
> 5. Open <https://www.szynalski.com/tone-generator/>. Click play on a 1 kHz tone. The MATLAB bar plot should show a tall bar near 1 kHz on the x-axis.

> [!tip] Why the order matters
> If you start the IDE running before MATLAB has the COM port open, the first 100 ms of UART data lands in nowhere and the receiver sees a frame mid-packet — the script will print `'Data alignment error!'` repeatedly. Easiest fix is the IDE-pauses-at-main approach in step 4.

Sweep the tone generator from 100 Hz up to 7 kHz. The peak in the MATLAB plot should track. **Yes, the FFT result reflects the generated tone frequency** — that's the answer to the manual's prompt.

> [!warning] You'll only see up to $f_s / 2$
> The board samples audio at 16 kHz (`fs = 16000` in the MATLAB script), so the maximum frequency the spectrum can represent is 8 kHz (Nyquist). The MATLAB receiver only plots `SIZE = 512` bins covering DC → 8 kHz at $\Delta f = 8000/512 \approx 15.6$ Hz/bin. A tone at 9 kHz aliases down to 7 kHz; don't be confused by it.

---

## **2.4) Compare windows — fill the deliverable table**

**Answer: rectangular has the sharpest peak but huge sidelobes; Hamming and Hanning trade some peak width for much cleaner spectral floors.** Pick a single tone (1 kHz works well) and screenshot all three side-by-side.

### Procedure

1. Edit `waverecorder.c:147` to call `apply_window(FFTInBuffer, hamming, FFT_SIZE)`. Build → Debug → Resume.
2. Tone generator at 1 kHz. Screenshot the MATLAB plot + tone-generator window side-by-side.
3. Edit line 147 to use `hanning` instead. Rebuild, re-run, screenshot.
4. Comment out line 147 entirely (rectangular = no windowing). Rebuild, re-run, screenshot.

### What you should see

| Window | Mainlobe (peak width) | Sidelobe floor | Visual signature on a 1 kHz tone |
|---|---|---|---|
| **Rectangular** ([[rectangular-window]])       | Narrow ($\sim 2$ bins wide) | Worst ($\sim -13$ dB)  | Sharp 1-bar peak, but **lots of grass** at $\sim 70$ dB across the whole spectrum |
| **Hamming** ([[hamming-window]])    | Medium ($\sim 4$ bins)      | Best ($\sim -43$ dB)   | Slightly wider peak, **clean floor** between peaks |
| **Hanning** ([[hann-window]])    | Medium ($\sim 4$ bins)      | Good ($\sim -31$ dB)   | Similar to Hamming, slightly more leakage right next to the peak |

> [!info]- 📐 Show derivation — why these numbers
>
> The DFT of a length-$N$ pure tone windowed by $w[n]$ is a frequency-shifted copy of $W(e^{j\omega})$. The numbers above come from the closed-form spectra of each window:
>
> $$W_{\text{rect}}(e^{j\omega}) = \frac{\sin(\omega N / 2)}{\sin(\omega / 2)}\quad\text{(Dirichlet kernel)}$$
>
> $$W_{\text{Hamming}}(e^{j\omega}) = 0.54\,W_{\text{rect}}(e^{j\omega}) - 0.23\bigl[W_{\text{rect}}(e^{j(\omega-2\pi/N)}) + W_{\text{rect}}(e^{j(\omega+2\pi/N)})\bigr]$$
>
> Hamming's coefficients ($0.54, 0.23, 0.23$) were specifically chosen to **cancel the largest sidelobe of the rectangular kernel**, dropping the floor to $-43$ dB. Hanning uses $(0.5, 0.25, 0.25)$ — easier coefficients, slightly worse cancellation.
>
> See [[window-resolution-criterion]] for the broader resolution-vs-leakage trade-off.

### Filling the table in your report

For each row, your **Observation** column should mention (a) peak sharpness, (b) sidelobe / floor level, (c) which is "better" for resolving close-together tones (rectangular) vs detecting a weak tone next to a strong one (Hamming).

---

# Deliverables checklist

Per Section VII of the lab manual, paste these into a single PDF, in this order:

- [ ] Title page: lab title + your name.
- [ ] **Task 1.2 vowel table** — both rows ("a", "i") fully filled, with the four-pane MATLAB plot pasted into the right column.
- [ ] **Task 2.4 window table** — three rows (Rectangular, Hamming, Hanning), each with a 1 kHz tone-generator + MATLAB plot screenshot.
- [ ] **Screenshots:** for each vowel, the IDE Watch panel showing `pitch_index` and `pitch_freq`, plus the MATLAB command line output of the same. Highlight (with a colored box) the two values in each screenshot.
- [ ] **Code section** — paste, with file-name labels:
  - `vowel_analysis/main.c`: your `max_index` (the function from Task 1.3).
  - `audio_spectrum_analyzer/Core/Src/waverecorder.c`: your `apply_window` (from Task 2.2).
  - All **four FILL_IN_BLANK lines** (1 in `main.c`, 3 in `waverecorder.c`) labeled with their file and line number.

> [!warning] Don't paste the whole file
> The rubric asks for *only* the new code. Paste the function bodies and the four lines; do **not** paste the surrounding boilerplate (the system clock, GPIO init, etc.). That makes the report shorter and easier to grade.

---

## Common pitfalls (gotcha log for next time)

- **CMSIS packed format** — the most common project-2 bug is computing `|Y[k]|^2` as `Y[k]*Y[k]` instead of `Y[2k]*Y[2k] + Y[2k+1]*Y[2k+1]`. The starter loop already steps by 2 to make this less likely, but it's still the trap. See [[cmsis-dsp-fft]].
- **MATLAB `vowel_a.h` vs `vowel_i.h` confusion** — running the script twice without editing the output filename overwrites the first header. The MCU project will silently use whichever vowel was last saved.
- **COM port not closed** — if MATLAB throws `Cannot connect to COM31` on a re-run, you didn't `clear s1` from the previous session (or another program is holding the port). The script's last line clears it; if it crashed before that, type `delete(serialportfind);` in the command window.
- **Forgetting to start the IDE in Debug mode** — running (not debugging) gives the board no chance to pause for MATLAB to attach, and you get `Data alignment error!` until the buffers re-align by accident. Always start in Debug.
- **Window header arrays not in `Core/Inc/`** — `hamming.h` and `hanning.h` are already in the starter zip. If your project tree is different (e.g., you moved files), `apply_window(..., hamming, ...)` will fail to link with "undefined reference to 'hamming'". Fix the include path, don't redeclare.

---

## Filed links

- Source summary: [[lab-eee-404-project-2-fft-applications]]
- New concept pages: [[autocorrelation-pitch-detection]], [[formant]], [[cmsis-dsp-fft]]
- Reused: [[fft]], [[real-valued-fft]], [[stft]], [[window-function]], [[hamming-window]], [[hann-window]], [[rectangular-window]], [[fft-scaling]]
- Course page: [[eee-404]]
