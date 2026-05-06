---
title: EEE 304 Lab EC1 — Filtering with an Arduino (Walkthrough)
type: walkthrough
course:
  - "[[eee-304]]"
tags: [eee-304, lab, walkthrough, extra-credit, arduino, simulink, butterworth, filter, embedded, pwm, dac]
sources:
  - "[[lab-eee-304-lab-ec1-arduino-filter]]"
created: 2026-05-03
updated: 2026-05-06
---

# EEE 304 Lab EC1 — Filtering with an Arduino (Walkthrough)

> [!note] **What this is.** A per-question walkthrough of the **Extra Credit Lab EC1** for EEE 304. For every numbered question I (a) **state it** verbatim, (b) **explain the overarching concept** so you understand what's being tested, then (c) **walk the concrete steps** to complete it. Use this alongside the lab manual: [EEE 304 Lab EC1.pdf](../../raw/labs/EEE_304_Lab_EC1.pdf).

> [!warning] **Prereq.** This lab assumes you've installed the **MATLAB + Simulink Support Package for Arduino Hardware** and can deploy a Simulink model to the **Arduino Due** (3.3V logic, 12-bit DAC, 84 MHz). Lab manual Section 2 walks you through that setup if you haven't.

---

## What you build

A **digital audio filter** running in real time on an Arduino Due. The Due's DAC1 pin drives a headphone (20–40 Ω). A Simulink model generates **four sine tones (80, 200, 500, 800 Hz)**, sums them, optionally filters them through one of four "If Action Subsystems," and pushes the result out the DAC. Two ground-able digital pins (7 and 8) select which subsystem runs — letting you A/B compare unfiltered vs. band-stop vs. band-pass-low vs. band-pass-high by ear.

**Three Simulink models, three roles:**

| Model | Role |
|---|---|
| [Arduino_test.slx](../../raw/labs/Arduino_test.slx) | Sanity check — drives the on-board L-LED with a sinusoidal PWM brightness; logs `data` to MATLAB workspace. |
| [Tones_1.slx](../../raw/labs/Tones_1.slx) | Generates the four-tone sum and pushes it straight to DAC1. **Always-pass-through.** |
| [Tones_2.slx](../../raw/labs/Tones_2.slx) | Same generator, but routes through one of four **If Action Subsystems** selected by digital pins 7 + 8. |

**Hardware safety.**

> [!warning] **Do NOT use a speaker with impedance below 20 Ω.** It will burn out the DAC channel on the Due. Headphones in the 20–40 Ω range are safe. Measure with a multimeter before plugging in if unsure.

---

## #0. Overview

> **#0.** Write an overview of your results.

### How to write it

A short paragraph (4–6 sentences) at the top of the report. State **what models you ran**, **what you observed**, and **whether your filter designs in #5 matched the manual's spec**.

> [!example] **Sample overview**
> *In this extra-credit lab I deployed three Simulink models to an Arduino Due: a test sinusoid driving the on-board LED, a four-tone generator (80/200/500/800 Hz) feeding the DAC1 headphone, and a filtered version with four selectable If-Action paths. The unfiltered output is clearly a **mixture of tones**, not a single pitch. Grounding pins 7 and 8 in different combinations switched between pass-through, a band-stop (silence), a band-pass passing only the low pair (80, 200 Hz), and a band-pass passing only the high pair (500, 800 Hz). Finally, I designed all three filters in MATLAB using `butter` at order 4 and `fs = 5` kHz; the Bode plots confirm the expected pass / stop bands.*

**Headline:** the Arduino Due, with Simulink-generated DSP code, can do real-time audio filtering you can hear by ear.

---

## #1. Plot the test-model `data` variable

> **#1.** Provide the plot of the "data" variable that you obtained after running the test in Section 3.2.

### The concept

Section 3.2 has you run **`Arduino_test.slx`** in **External Mode** with **Monitor & Tune**. The model contains:
- A **Sine Wave** block generating a sinusoid (offset and scaled to the range $[0, 255]$ so it fits the 8-bit PWM register).
- A **PWM** output block driving Arduino pin 13 (the on-board L LED).
- A **scope** with logging on, exporting samples to a MATLAB variable named `data`.

`data` ends up as an $N \times 2$ array — column 1 is timestamps, column 2 is the sinusoid samples. You're asked to plot column 2 against column 1.

#### Walkthrough

1. **Open `Arduino_test.slx`** and set the workspace variable `TSI` (the sample time index) — type in the MATLAB command window:

   ```matlab
   TSI = 0.001;     % 1 ms sample time → 1 kHz PWM update rate
   ```

   > [!tip] **Why `TSI` and not a literal number?** The sine-wave block, the PWM block, and the model's "Fixed-step size" all reference the **same variable** so you only change it in one place.

2. **Set the model to External Mode.** In the Simulink toolbar, the **MODE** dropdown should say **External**. (On Simulink 2023+ the path is `HARDWARE → Run on Board → External`.)

3. **Connect the Due** via USB. Verify in your OS that a serial port appeared (e.g., `COM3` on Windows, `/dev/cu.usbmodem...` on macOS).

4. **Click "Monitor & Tune"** (the play-with-graph icon in the HARDWARE tab). Simulink will:
   - Compile the model.
   - Flash the Arduino.
   - Open a scope showing the sinusoid in real time.
   - Continuously log samples to the workspace as `data`.

5. **Stop after a few seconds**, then plot:

   ```matlab
   plot(data(:,1), data(:,2));
   xlabel('Time (s)');
   ylabel('PWM value (0–255)');
   title('Arduino_test.slx — sinusoid logged via External Mode');
   grid on;
   ```

> [!example] **Expected shape**
> A clean sinusoid oscillating between roughly **0 and 255**, with the period set by the Sine Wave block parameters. **No DC offset clipping** at top or bottom — if you see flattening, your amplitude or offset is wrong.

> [!tip] **Visual sanity check.** While the model runs, the on-board **L LED** (next to the USB programming port — there are 4 LEDs labeled `RX`, `TX`, `L`, `ON`) should fade smoothly from off to bright in a sinusoidal rhythm. If it just blinks on/off, your PWM signal is square-wave-shaped, not sinusoidal — re-check the sine block parameters.

**Answer:** screenshot of `plot(data(:,1), data(:,2))` showing one full sinusoidal cycle, $y$-axis from 0 to 255.

---

## #2. Single tone, or a mixture?

> **#2.** Does the audio heard on the headphone in the experiment of Section 3.3 sound like it is a single tone or a mixture of frequencies?

### The concept

Section 3.3 has you load **`Tones_1.slx`**, which generates **four sine waves at 80, 200, 500, and 800 Hz** (each amplitude 0.5, all summed, then shifted up by 2, then scaled by 400 so the result lands in $[0, 1600]$ for the 12-bit DAC). The sum is fed to **DAC1** without any filtering.

Mathematically the signal you hear is:

$$y(t) = K \cdot \bigl[\sin(2\pi \cdot 80\,t) + \sin(2\pi \cdot 200\,t) + \sin(2\pi \cdot 500\,t) + \sin(2\pi \cdot 800\,t)\bigr] + \text{offset}$$

A signal with **four distinct frequency components** does **not** sound like a single pure tone. The 80 Hz component is a low rumble; 200 Hz is a deep musical pitch (roughly $G_3$); 500 Hz is bright (around $B_4$); 800 Hz is brighter still ($G_5$). When summed, the four blend into a complex chord-like timbre.

**Answer:** **It is a mixture of frequencies, not a single tone.** You can hear the low rumble of the 80/200 Hz pair simultaneously with the brighter 500/800 Hz pair. A single pure tone has no harmonic richness; this signal is clearly a chord.

> [!tip] **Sanity check by ear.** Briefly cup your hand over one ear — you should still hear at least two distinct pitches, not one. If it sounds like a single buzzy tone, your headphone may be misconnected or your output amplitude is way too low.

---

## #3. Pin 7 / Pin 8 grounding table

> **#3.** As part of your report, connect wires to pin 7 and 8 as per the following table and report on what type of frequencies you can hear. Choose between **high**, **low**, **all**, and **none**.

### The concept — Table 2 from the manual

`Tones_2.slx` routes the four-tone sum through one of **four "If Action Subsystem" blocks**, selected by digital pins 7 and 8. The Arduino Due's digital inputs **default to HIGH (1)** when nothing is connected; **grounding** an input pulls it LOW (0). The four cases:

| Pin 7 | Pin 8 | Subsystem activated | Filter type |
|---|---|---|---|
| Not Grounded | Not Grounded | Subsystem 1 | **Pass-through** (no filter) |
| Grounded | Not Grounded | Subsystem 2 | One of: band-stop, BP-low, BP-high |
| Not Grounded | Grounded | Subsystem 3 | One of: band-stop, BP-low, BP-high |
| Grounded | Grounded | Subsystem 4 | One of: band-stop, BP-low, BP-high |

The manual states **"in no particular order"** — you must **identify by ear** which subsystem is which. The three filters available among subsystems 2, 3, 4 are:

- **Band-stop:** kills all signals → you hear **none** (silence).
- **Band-pass for low frequencies** (80, 200 Hz) → you hear **low** (the rumble).
- **Band-pass for high frequencies** (500, 800 Hz) → you hear **high** (the bright pair).

### The procedure

1. **Open `Tones_2.slx`.** Confirm it has the four "If Action Subsystem" blocks and a multiplexer selecting between them based on pins 7 and 8.
2. **Deploy to hardware** (HARDWARE → Deploy to Hardware) — this flashes the model permanently to the Due, so you can test without USB power.
3. **For each row of the table, configure pins 7 and 8** using jumper wires:
   - **Not grounded** = leave the pin floating (no wire).
   - **Grounded** = connect the pin to GND with a jumper.
4. **Listen** to the headphone and decide: **high** / **low** / **all** / **none**.
5. **Fill in the table:**

| Pin 7 | Pin 8 | Frequencies heard |
|---|---|---|
| Not Grounded | Not Grounded | **all** (pass-through — guaranteed by the manual) |
| Grounded | Not Grounded | *(record what you hear)* |
| Not Grounded | Grounded | *(record what you hear)* |
| Grounded | Grounded | *(record what you hear)* |

> [!warning] **The exact mapping depends on how Subsystems 2/3/4 are wired in your `Tones_2.slx` file.** The manual deliberately doesn't tell you — it's a listening exercise. The three answers among the bottom three rows must be exactly **{low, high, none}** in some permutation.

> [!tip] **How to tell low vs high vs none by ear:**
> - **none** = silence (or near-silence, possibly with a faint hiss). Easy to spot.
> - **low** = a deep, dull rumble (the 80/200 Hz pair). No brightness.
> - **high** = bright and treble-heavy (the 500/800 Hz pair). No rumble.
> - **all** = the rich chord you heard in #2.

> [!example] **Common student mapping** *(varies by `Tones_2.slx` file — verify yours)*
> | Pin 7 | Pin 8 | Heard |
> |---|---|---|
> | Not Grounded | Not Grounded | all |
> | Grounded | Not Grounded | none |
> | Not Grounded | Grounded | low |
> | Grounded | Grounded | high |

**Answer:** four entries — **all** for the first row (guaranteed), and your measured **{low, high, none}** assignments for the other three rows.

---

## #4. Photo of the hardware setup

> **#4.** Take a photo of your last hardware set up (Arduino DUE, the headphone and wiring) and attach it to the lab report.

### The shot list

A single clear photo showing:

- The **Arduino Due** with the USB cable plugged into the **programming port** (the one closest to the power jack).
- The **headphone wire** clipped to **GND** and **DAC1** on the Due (via crocodile clips or jumper wires).
- The **jumper wires** to pins 7 and 8 — show the configuration for at least one of the rows from #3 (e.g., both grounded).
- (Optional but appreciated:) the breadboard with any extra wiring used to make connections cleaner.

> [!tip] **Photo composition.** Take it from above, in good light, framed so all wire endpoints are visible. Phone camera is fine. Annotate with arrows in your favorite editor pointing to **DAC1**, **GND**, **pin 7**, **pin 8** if the wires are hard to trace.

**Answer:** one labeled JPG/PNG embedded in the report.

---

## #5. Design three Butterworth filters in MATLAB

> **#5.** As part of your report, design the following digital filters using the **`butter`** command in MATLAB. Provide MATLAB code and Bode plots of these filters. Choose **order 4** and sampling rate **5 kHz**.
> - A band-stop filter to kill all signals so nothing is heard.
> - A band-pass filter to allow only low frequencies (80, 200 Hz).
> - A band-pass filter to allow only high frequencies (500, 800 Hz).

### The concept

The three filters need to act on the four tones at **80, 200, 500, 800 Hz** sampled at **$f_s = 5$ kHz** (Nyquist $f_N = 2.5$ kHz). MATLAB's `butter` function takes **normalized cutoff frequencies** $W_n = f / f_N$ in the range $(0, 1)$.

For each filter you choose **passband edges** that comfortably bracket the tones you want to keep (or stop), with margin so the rolloff doesn't bite into the desired tones:

| Filter | Pass / stop band (Hz) | $W_n = f/f_N$ |
|---|---|---|
| **Band-pass low** | pass 50–250 Hz (covers 80, 200) | $[0.020, \,0.100]$ |
| **Band-pass high** | pass 400–1000 Hz (covers 500, 800) | $[0.160, \,0.400]$ |
| **Band-stop** | stop 50–1000 Hz (kills all four tones) | $[0.020, \,0.400]$ |

> [!warning] **Order doubling for bandpass / bandstop.** When you call `butter(n, [w_lo w_hi], 'bandpass')` with a **2-element** `Wn`, MATLAB returns a filter of order **2n**, not n. The manual says "Choose order 4" — interpret as `n = 4` (i.e., the resulting BP/BS filter is actually 8th order). This is the standard convention for `butter`.

### The MATLAB code

```matlab
%% EEE 304 Lab EC1 — Question #5
% Design 3 digital Butterworth filters at fs = 5 kHz, order 4.

fs = 5000;        % Sampling rate (Hz)
fn = fs/2;        % Nyquist frequency (Hz)
n  = 4;           % Filter order

% --- Filter 1: Band-pass for low tones (80, 200 Hz) ---
% Pass 50–250 Hz (margin around 80 and 200 Hz)
[b_lp, a_lp] = butter(n, [50  250 ]/fn, 'bandpass');

% --- Filter 2: Band-pass for high tones (500, 800 Hz) ---
% Pass 400–1000 Hz (margin around 500 and 800 Hz)
[b_hp, a_hp] = butter(n, [400 1000]/fn, 'bandpass');

% --- Filter 3: Band-stop covering all four tones ---
% Stop 50–1000 Hz (kills 80, 200, 500, 800 Hz)
[b_bs, a_bs] = butter(n, [50  1000]/fn, 'stop');

%% Bode plots
figure('Name','BP-low: pass 80,200 Hz');
freqz(b_lp, a_lp, 1024, fs);
title('Band-pass for low tones (80, 200 Hz)');

figure('Name','BP-high: pass 500,800 Hz');
freqz(b_hp, a_hp, 1024, fs);
title('Band-pass for high tones (500, 800 Hz)');

figure('Name','BS: kill 80, 200, 500, 800 Hz');
freqz(b_bs, a_bs, 1024, fs);
title('Band-stop (kills all four tones)');
```

### What each Bode plot should show

> [!example] **Expected magnitude responses (visual sanity check):**
> - **BP-low:** flat 0 dB peak around 100–200 Hz, sharp rolloff above ~250 Hz. The 500 and 800 Hz tones land in the **stopband** at $\leq -40$ dB.
> - **BP-high:** flat 0 dB peak around 500–800 Hz, sharp rolloff below ~400 Hz. The 80 and 200 Hz tones land in the **stopband** at $\leq -40$ dB.
> - **BS:** deep notch from ~50 Hz to ~1 kHz; **all four tones** sit in the notch at $\leq -40$ dB.

> [!tip] **Verification by hand.** Print the four tone attenuations at the end of your script:
> ```matlab
> tones = [80 200 500 800];
> for i = 1:numel(tones)
>     [h, ~] = freqz([b_lp;b_hp;b_bs].',[a_lp;a_hp;a_bs].', tones(i)*2*pi/fs);
>     fprintf('%4d Hz: BP-low %.1f dB | BP-high %.1f dB | BS %.1f dB\n', ...
>         tones(i), 20*log10(abs(h(1))), 20*log10(abs(h(2))), 20*log10(abs(h(3))));
> end
> ```
> The output should make it instantly clear which tones each filter passes vs. stops.

**Answer:** the MATLAB script above, plus three Bode plots (one per filter) showing magnitude (dB) and phase (deg) vs. frequency (Hz). Include the verification table.

---

## Submission checklist

| # | Deliverable | Where it lives in the report |
|---|---|---|
| 0 | Overview paragraph | Top |
| 1 | Plot of `data(:,1)` vs `data(:,2)` from `Arduino_test.slx` | Section 1 |
| 2 | Single sentence: "mixture of frequencies" with brief justification | Section 2 |
| 3 | Filled-in pin 7/8 table (4 rows: all + your measured 3) | Section 3 |
| 4 | Photo of Arduino Due + headphone + jumper wiring | Section 4 |
| 5 | MATLAB script + 3 Bode plots + verification table | Section 5 |

---

## Related

- [[eee-304-lab-4-walkthrough]] — Lab 4 (AM modulation/demodulation in Simulink, also uses the `butter` command and Bode plots)
- [[butterworth-filter]] — order vs. cutoff trade-off, why higher order = sharper rolloff
- [[eee-304-lab-ec2-walkthrough]] — sibling extra-credit lab (feedback control with phototransistor + LED on the same Arduino)
- Lab manual — [EEE 304 Lab EC1.pdf](../../raw/labs/EEE_304_Lab_EC1.pdf)
- Simulink models — [Arduino_test.slx](../../raw/labs/Arduino_test.slx), [Tones_1.slx](../../raw/labs/Tones_1.slx), [Tones_2.slx](../../raw/labs/Tones_2.slx)
