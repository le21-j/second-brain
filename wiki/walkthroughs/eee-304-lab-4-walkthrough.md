---
title: EEE 304 Lab 4 — AM Modulation/Demodulation Walkthrough
type: example
course: [[eee-304]]
tags: [eee-304, lab, walkthrough, am, modulation, demodulation, simulink, butterworth, communication]
sources: [[lab-eee-304-lab-4-am-modulation]]
created: 2026-04-25
updated: 2026-04-26
revisions:
  - 2026-04-26 — corrected #3 missing-block identification: blocks are CARRIER SOURCE + LPF (not Product + LPF). Added simulation-Nyquist analysis and the $f_c = 5$ kHz derivation. Original walkthrough mis-identified the Product as missing — verified by inspecting `AM_Mod_coherent_tada_inc.slx` XML directly.
---

# EEE 304 Lab 4 — AM Modulation/Demodulation Walkthrough

> [!note] **What this is.** A per-question walkthrough of the lab. For every numbered question I (a) **state it** verbatim, (b) **explain the overarching concept** so you understand what's being tested, then (c) **walk through the concrete steps** to complete it. Use this alongside the lab manual at `raw/labs/EEE 304 Lab4.pdf`.
>
> The **highlighted lines** (like this) are the headline answer for that question.

> [!warning] **Naming nit.** The PDF is titled "EEE 304, Lab 4" but the assignment section inside calls itself "Lab 2 Assignment" — assume **Lab 4** throughout.

---

## #0. Overview

> **#0.** Write an overview of your results.

### The concept

A summary section. Keep it short — what the lab is teaching, what you found, and any anomalies. Save the meat for the per-question answers.

### How to write it

A 4–6 sentence paragraph at the top of your report:

> [!example] **Sample overview**
> *In this lab I built and exercised three Simulink models for AM modulation/demodulation. The first model used **coherent demodulation** with a Butterworth LPF — varying the carrier frequency (down to 1 kHz) and the modulation index (up to $\mu = 2$) confirmed that coherent demod recovers the message regardless of $\mu$ but breaks once $\omega_c < 2B$ because the sidebands overlap. The second model used **envelope detection** — over-modulation ($\mu > 1$) caused visible distortion in the recovered signal, matching the manual's prediction. The third model required filling in the missing Product and Analog-Filter blocks of a coherent demodulator and adjusting the demodulation gain to $2\times$ to compensate for the $\tfrac{1}{2}$ factor introduced by the demod math; once corrected, the `tada.wav` audio sounded identical on both the direct path and the modulated/demodulated path.*

**Headline:** coherent demod is robust to $\mu$; envelope detection only works for $\mu \leq 1$; the recovered message is always $\tfrac{1}{2}m(t)$ until you apply a gain of 2.

---

## #1. Coherent Demodulation in Simulink (`AM_Mod_coherent.slx`)

The setup recap: **baseband (message) signal at $f_m = 2$ kHz**, **carrier amplitude $A = 2$**, **carrier frequency starting at $f_c = 20$ kHz**. There are 3 knobs (baseband amp, carrier freq, scope select).

### #1.1 — **Choose $n$ and $\text{cutoff}$ for the demodulation Butterworth LPF**

> **Q1.1.** In the "Analog Filter Design" block, the parameters of the Butterworth filter have been assigned using variables: $n$ is the order of the filter and $\text{cutoff}$ is the cutoff frequency in **rad/s**. By looking at the frequency of the baseband signal (2000 Hz), decide on a cutoff value and order. Run the simulation. What is the choice of $n$ and $\text{cutoff}$ that gives you perfect demodulation?

#### The concept

After the demodulator multiplies the received AM signal by $\cos(\omega_c t)$ again, the spectrum has copies at **DC** (the message) and at $\pm 2\omega_c = \pm 2\pi(40 \text{ kHz})$ (junk to throw away). See [[coherent-demodulation]].

The LPF must:
- **Pass** the message at $2$ kHz $\Rightarrow$ $\text{cutoff} > 2$ kHz (with margin).
- **Reject** the demodulation images at $40$ kHz $\Rightarrow$ $\text{cutoff} \ll 40$ kHz.
- Use enough **filter order** to attenuate the $40$ kHz junk by at least $\sim 40$ dB.

#### Walkthrough

1. **Open MATLAB**, click in the **command window**, and type:
   ```matlab
   n      = 4;
   cutoff = 2*pi*5000;     % 5000 Hz, expressed as rad/s
   ```
   > [!warning] **Units gotcha.** The Simulink block expects $\text{cutoff}$ in **rad/s**, not Hz. Forgetting the $2\pi$ factor is the #1 mistake on this question.

2. **Open `AM_Mod_coherent.slx`** and confirm the "Analog Filter Design" block parameters reference the variables $n$ and $\text{cutoff}$ (not literal numbers).

3. **Run the simulation** (the green ▶ button at the top of the Simulink toolbar).

4. **Open the "Demodulated Signal Scope".** You should see two traces overlaid:
   - The original baseband signal (the reference).
   - The modulated-then-demodulated signal.

5. **Verify:**
   - Same **frequency** (both at $2$ kHz)? ✅ should match.
   - Same **amplitude**? ✅ after the built-in $\tfrac{1}{2}$ Gain block, the amplitudes should match.
   - **Phase** may differ — that's OK and expected (filter delay).

6. **Take a screenshot** of the Demodulated Signal Scope.

#### Answer

**$n = 4$, $\text{cutoff} = 2\pi \cdot 5000$ rad/s** (i.e., 5 kHz). Any cutoff in roughly **3 kHz to 30 kHz** works; order 4–6 is plenty.

> [!tip] **Why these numbers?** Cutoff sits comfortably between the message ($2$ kHz) and the demodulation image ($40$ kHz). 4th-order rolls off at $80$ dB/decade, attenuating the $40$ kHz junk by $\sim 72$ dB. See [[butterworth-filter]] for the full design procedure.

---

### #1.2 — **Spectrograms at all 5 knob positions**

> **Q1.2.** With your $n$ and $\text{cutoff}$, provide screenshots of the spectrum analyzer for all 5 positions of knob 3: **baseband, carrier, modulated, demodulated unfiltered, demodulated+filtered**. Provide side-by-side screenshots of baseband and demodulated+filtered to show they look the same.

#### The concept

Each knob position routes a different signal into the spectrum analyzer. You're stepping through the AM pipeline in the **frequency domain** — proving that what we did mathematically (shift the message to $\pm\omega_c$, then shift back, then filter) actually happens to the spectrum.

#### What you should see

> [!example] **Expected spectrograms** (carrier at $20$ kHz, message at $2$ kHz)
>
> | Knob position | Expected spectral content |
> |---|---|
> | **Baseband** | One peak at $2$ kHz |
> | **Carrier** | One peak at $20$ kHz |
> | **Modulated** | Peak at $20$ kHz (carrier residue) + sidebands at $18$ kHz (LSB) and $22$ kHz (USB) |
> | **Demodulated unfiltered** | Peak at $2$ kHz (message back) + peaks at $38$/$40$/$42$ kHz (the $2\omega_c$ images) + DC peak (the carrier residue) |
> | **Demodulated + filtered** | Just $2$ kHz — the LPF has removed everything else |

#### Walkthrough

1. With the simulation **running** (let it free-run), turn knob 3 through all 5 positions.
2. For each position, **screenshot** the spectrum analyzer.
3. Place the **baseband** and **demodulated+filtered** screenshots **side-by-side** in your report.

**Verify:** the side-by-side baseband and demodulated+filtered spectrograms should both show a **single peak at $2$ kHz** at the same height, confirming end-to-end recovery.

---

### #1.3 — **Vary carrier frequency: 20 → 10 → 5 → 1 kHz**

> **Q1.3.** Without changing the Butterworth filter from #1.1, vary the carrier frequency to 10 kHz, 5 kHz, and 1 kHz. Provide screenshots of the spectrograms (baseband + demodulated+filtered) in each case. Discuss your observations.

#### The concept

The unbreakable rule of AM is $\omega_c > 2B$ — the carrier must be at least **twice the message bandwidth** above baseband. Otherwise the **upper and lower sidebands overlap each other** and the message is destroyed at the transmitter, before the receiver even gets to do anything.

For our message at $2$ kHz, the **bandwidth** is $\sim 2$ kHz, so the rule says we need $f_c > 4$ kHz.

> [!warning] **Why "without changing the filter"?** Because the filter was designed assuming $2f_c = 40$ kHz is far above the cutoff. As we move $f_c$ down, eventually $2f_c$ lands inside the passband — that's a separate failure on top of the sideband-overlap one.

#### What you should see

> [!example] **Expected outcomes**
>
> | $f_c$ | Status | What the demodulated+filtered spectrogram shows |
> |---|---|---|
> | $20$ kHz | ✅ healthy ($f_c \gg B$) | clean $2$ kHz tone |
> | $10$ kHz | ✅ still works | clean $2$ kHz tone ($2f_c = 20$ kHz still well past cutoff) |
> | $5$ kHz | ⚠️ marginal ($f_c \approx 2B$) | $2$ kHz tone present but the $2f_c = 10$ kHz image now lands close to the LPF cutoff — may leak through depending on filter order |
> | $1$ kHz | ❌ broken ($f_c < B$) | the sidebands at $-1 \pm 2 = \pm 1, \pm 3$ kHz overlap the carrier and each other; demodulated spectrum is **garbage** with extra spectral lines and the original $2$ kHz tone barely visible |

#### Walkthrough

1. Stop the simulation (■).
2. **Inside the "Carrier Signal" block**, change the frequency parameter to $10000$ Hz. (Knob 2 also works.)
3. Run again. Screenshot baseband + demod+filtered.
4. Repeat for $5000$ Hz and $1000$ Hz.

**Headline observation:** as $f_c$ drops below $2B = 4$ kHz, the AM sidebands overlap and demodulation fails irreversibly. This is the spectral analog of aliasing.

---

### #1.4 — **Vary baseband amplitude: 1 → 2 → 4 (modulation index)**

> **Q1.4.** Keep $f_c = 20$ kHz. Change the baseband amplitude from 1 to 2 and then 4. Provide spectrograms (baseband vs demodulated+filtered) and discuss. Do they match Section 3?

#### The concept

This is testing what [[modulation-index]] tells us. With $A = 2$:

| Baseband amplitude $m_{\text{peak}}$ | $\mu = m_{\text{peak}}/A$ | Regime |
|---|---|---|
| $1$ | $0.5$ | under-modulation |
| $2$ | $1.0$ | perfect modulation |
| $4$ | $2.0$ | **over-modulation** |

**Section 3 says: "In the case of coherent demodulation, any value of $\mu$ provides reconstruction."** So all three should work — and that's exactly what we expect to observe.

> [!tip] **Why coherent demod doesn't care about $\mu$.** The mathematical recovery is
>
> $$r(t)\cos(\omega_c t) = \tfrac{1}{2}(A + m(t)) + \text{(high-freq junk at } 2\omega_c\text{).}$$
>
> The LPF rejects the junk and you get $\tfrac{1}{2}(A + m(t))$ regardless of how big $m(t)$ is. There's no rectification step that breaks when the envelope dips negative. Compare with [[envelope-detection]], where **rectification** of the over-modulated signal does break things.

#### Walkthrough

1. **Inside the "Baseband Signal" block**, set amplitude to $1$. Run, screenshot.
2. Change to $2$. Run, screenshot.
3. Change to $4$. Run, screenshot.
4. For each, capture **baseband** and **demodulated+filtered** spectrograms.
5. **Discussion to write:** All three cases recover a clean $2$ kHz tone in the demod+filtered spectrum — only the **amplitude** changes. This matches Section 3's claim that coherent demod handles any $\mu$.

**Headline answer:** coherent demod recovers the $2$ kHz message at all three amplitudes ($\mu = 0.5, 1.0, 2.0$). Only the recovered amplitude scales — the shape is preserved. This matches Section 3.

---

## #2. Envelope (Non-Coherent) Demodulation (`AM_Mod_incoherent.slx`)

> [!note] **What's different.** This model uses **envelope detection** ([[envelope-detection]]): take $|\,r(t)\,|$ then **bandpass** filter. The "Analog Filter Design" block here is a **10th-order bandpass** with band edges $W_{\text{lo}}$ and $W_{\text{hi}}$. The baseband is shifted up by the carrier amplitude (the **Constant1** block adds 2) so the envelope is non-negative.

### #2.1 — **Set $W_{\text{lo}} = 30 \cdot 2\pi$, $W_{\text{hi}} = 5000 \cdot 2\pi$ and explain each scope**

> **Q2.1.** Set $W_{\text{lo}} = 30 \cdot 2\pi$, $W_{\text{hi}} = 5000 \cdot 2\pi$ in the Analog Filter Design parameters. Take screenshots from all scopes (Baseband, Carrier Signal, Modulated, Demodulated unfiltered, LPF Scope, Demodulated Signal Scope). Explain in your own words what is happening to the baseband signal at each scope position.

#### The concept

You're walking the message through the envelope detector. The two band edges are doing two distinct jobs:
- $W_{\text{lo}} = 30 \cdot 2\pi$ rad/s ($\approx 30$ Hz): removes the **DC offset** that came from the $+A$ shift at the transmitter.
- $W_{\text{hi}} = 5000 \cdot 2\pi$ rad/s ($\approx 5$ kHz): removes the $2\omega_c$ rectification harmonics at $40$ kHz / $80$ kHz / etc.

The pass region is $30$ Hz to $5$ kHz — wide enough for the $2$ kHz message, narrow enough to suppress everything else.

#### Walkthrough — what each scope shows

> [!example] **Per-scope explanation** (write this in your report)
>
> | Scope | What you see | What's happening |
> |---|---|---|
> | **Baseband** | clean $2$ kHz sine | the message $m(t)$ before anything happens |
> | **Carrier Signal** | clean $20$ kHz sine | the carrier $\cos(\omega_c t)$ |
> | **Modulated Signal Scope** | a $20$ kHz oscillation whose envelope traces a $2$ kHz sine, all positive | $(A + m(t))\cos(\omega_c t)$ — note the envelope is **non-negative** thanks to the $+A$ shift |
> | **Demodulated unfiltered** | a fully rectified, positive-only waveform with both fast spikes and a slow envelope | $\bigl|(A + m(t))\cos(\omega_c t)\bigr|$ — the $|\cdot|$ block has folded all negatives back up, creating both DC content and $2\omega_c$ harmonics |
> | **LPF Scope** | a clean $2$ kHz sine, possibly with a slight DC offset removed | the bandpass has stripped the DC and the $2\omega_c$ junk, leaving only the message frequency |
> | **Demodulated Signal Scope** | the recovered message, looking like the baseband (perhaps scaled) | final output — should match the baseband in shape and frequency |

**Headline:** the bandpass filter does two cleanups in one block — $W_{\text{lo}}$ kills the DC from the $+A$ shift, $W_{\text{hi}}$ kills the rectification harmonics. Both are required for envelope detection to work.

---

### #2.2 — **Drop $W_{\text{lo}}$ to $1 \cdot 2\pi$ — what changes?**

> **Q2.2.** Change $W_{\text{lo}}$ to $1 \cdot 2\pi$. What happens to the spectrogram of the demodulated+filtered signal? What frequencies do you think are present and why?

#### The concept

$W_{\text{lo}}$ was the **high-pass edge** that was killing the DC offset from the transmitter's $+A$ shift. Lowering it from $30$ Hz to $1$ Hz means **DC is now passed through** instead of blocked.

#### What you should see

> [!example] **Expected spectrogram change**
>
> | Before ($W_{\text{lo}} \approx 30$ Hz) | After ($W_{\text{lo}} \approx 1$ Hz) |
> |---|---|
> | Single peak at $2$ kHz | Peak at $2$ kHz **PLUS** a peak at DC ($0$ Hz) |

**Frequencies present at $W_{\text{lo}} = 1 \cdot 2\pi$: a strong DC component (from the $+A$ shift) PLUS the $2$ kHz message.** The DC bleeds through because the new $W_{\text{lo}} = 1 \cdot 2\pi$ rad/s $\approx 1$ Hz band edge is too low to suppress it.

> [!tip] **Why this matters in practice.** AM broadcasters rely on the receiver to AC-couple the demodulated audio (or use a high-pass with $W_{\text{lo}} > 0$). Forgetting that step leaves a constant offset on the audio that doesn't sound bad per se but eats headroom and causes pop noise on amplifier startup.

---

### #2.3 — **What's the modulation index right now? (baseband amp = 1)**

> **Q2.3.** Switch $W_{\text{lo}}$ back to $30 \cdot 2\pi$. Carrier amplitude is $2$, baseband amplitude is $1$. What is the modulation index?

#### The concept

Pure recall from [[modulation-index]]: $\mu = m_{\text{peak}}/A$.

#### Answer

**$\mu = 1/2 = 0.5$.** Under-modulated — comfortable safe zone for envelope detection.

---

### #2.4 — **Set $\mu = 1$ (baseband amp = 2). Any difference?**

> **Q2.4.** Change the baseband amplitude so $\mu = 1$. Is there any difference in the demodulated+filtered signal? Show both spectrogram and signal-vs-time plots.

#### The concept

$\mu = 1$ means $m_{\text{peak}} = A = 2$, so set **baseband amplitude $= 2$**. The envelope $A + m(t)$ just barely touches zero at the troughs of $m(t)$ — no rectification flip yet, but **zero margin**.

#### What you should see

> [!example] **Expected**
>
> - **Spectrogram:** still a clean $2$ kHz peak. Spectrum looks the same as $\mu = 0.5$, just possibly louder.
> - **Time domain:** the recovered signal is **larger in amplitude** than the $\mu = 0.5$ case (by a factor of $2$). Shape unchanged.
> - **Envelope detector:** still works. We're at the boundary, not over it.

**Answer:** at $\mu = 1$, envelope detection still recovers the message cleanly — the recovered amplitude scales linearly with the baseband amplitude, but the shape is preserved.

---

### #2.5 — **Set $\mu = 2$ (baseband amp = 4) — what happens?**

> **Q2.5.** Change the baseband amplitude so $\mu = 2$. Provide spectrogram and any pertinent scope outputs. Describe what's happening.

#### The concept

$\mu = 2$ means $m_{\text{peak}} = 2A = 4$, so set **baseband amplitude $= 4$**. Now the envelope $A + m(t) = 2 + m(t)$ **dips below zero** when $m(t) < -2$. The $|\cdot|$ block in the envelope detector flips those negative excursions back up, producing a **half-rectified, harmonic-distorted** version of the original — *not* the original message.

**This is the failure mode the lab is testing.**

#### What you should see

> [!example] **Expected (the failure)**
>
> - **Time domain (Demodulated unfiltered scope):** the slow envelope is no longer a clean $2$ kHz sine — it has **kinks at the troughs** where the rectification flipped negative excursions back up.
> - **Spectrogram (demod+filtered):** the original $2$ kHz peak is still there but accompanied by **harmonics at $4$ kHz, $6$ kHz, ...** — the rectification has injected harmonic distortion.
> - **Audibly (if it were audio):** the recovered signal would sound distorted, especially on loud passages.

#### Walkthrough — what to put in your report

1. Screenshot the **demod+filtered spectrogram** showing the harmonics.
2. Screenshot the **demod-unfiltered scope** showing the kinked envelope.
3. **Discussion:** Match the observation to Section 3's prediction — over-modulation breaks envelope detection irreversibly. Compare to #1.4 where coherent demod handled $\mu = 2$ just fine; that's the **key contrast between coherent and non-coherent demodulation**.

**Headline answer:** $\mu = 2$ over-modulates $\to$ envelope dips negative $\to$ $|\cdot|$ rectification injects harmonic distortion $\to$ recovered spectrum has spurious peaks at $4$ kHz, $6$ kHz, etc. Envelope detection has failed; coherent demod (with the same $\mu$) would not have.

---

## #3. Fill-in-the-Blanks: `tada.wav` Through Coherent Demod (`AM_Mod_coherent_tada_inc.slx`)

> **Q3.** Two blocks are missing and the `Dem Gain` block is configured for the wrong gain. Fill in the missing blocks and run with correct parameters. The "tada" sound should be heard on both the direct path and the modulated/demodulated path. Provide your block choices and the corrected gain. Justify each choice. Screenshot the Demodulated Signal Scope showing both paths.

### The concept

This is a **coherent demodulator** (per the file name `_coherent_`) running on a real audio source (`tada.wav`). The architecture must look like:

```
audio source ─►[×]─►[modulated]──►[×]─►[LPF]─►[Dem Gain]─► output
                ▲                  ▲
                │                  │
                └──── [carrier] ───┘     (one Sine source, branched to BOTH multipliers — coherent)
```

The Modulator and Demodulator multipliers (`Product` blocks) and the Dem Gain are **already placed**. The two empty slots are:
- The **carrier source** — a `Sine Wave` or `Signal Generator` block whose output wires into **both** multipliers.
- The **LPF** (`Analog Filter Design` block) that removes the $2\omega_c$ images after the demod multiplier.

The "Dem Gain" sits at the output and must compensate for the $\tfrac{1}{2}$ factor that coherent demod introduces.

> [!warning] **The simulation runs at the audio rate — that constrains the carrier.** Open *Model Configuration Parameters* and you'll see `Solver = ode3 (fixed-step)`, `FixedStep = 1/22050`. So the simulation Nyquist is **$f_s/2 = 11025$ Hz**. Anything at or above that aliases. The 20 kHz carrier you used in Part 1 will NOT work here — Part 1's `FixedStep` was $10^{-6}$ s.

### What `tada.wav` looks like, signal-wise

A short Microsoft Windows system sound, sample rate $22050$ Hz, dominant musical content (chord fundamentals + harmonics) below $\sim 2$ kHz with energy trailing off above $4$ kHz. Effective bandwidth $B \approx 2$ kHz for filter-design purposes.

### Walkthrough — fill in the missing blocks

#### Missing block #1 — **Carrier source (`Signal Generator` or `Sine Wave`)**

- **Library:** Simulink → Sources → Signal Generator (or Sine Wave).
- **Wave form:** sine.
- **Amplitude:** $2$ (matches the carrier amplitude convention used throughout this lab).
- **Frequency:** **$f_c = 5000$ Hz**.
- **Wiring:** branch the output to **both** the Modulator's second input AND the Demodulator's second input. **Do not** add two separate sources — that would model an incoherent receiver and demod will fail.

**Why $5$ kHz?** Three constraints have to hold simultaneously:

| Constraint | Inequality | Plug in for this model |
|---|---|---|
| Sim Nyquist (no aliasing of carrier itself) | $f_c < f_s/2$ | $f_c < 11025$ Hz |
| AM sideband rule (no overlap of USB/LSB) | $f_c > 2B$ | $f_c > 4$ kHz |
| $2f_c$ demod image stays below sim Nyquist (so the LPF can kill it without alias trickery) | $2f_c < f_s/2$ | $f_c < 5512$ Hz |

The intersection is roughly $f_c \in (4, 5.5)$ kHz. **$f_c = 5$ kHz** sits squarely in that window with margin on both sides.

> [!tip] **Units gotcha — Signal Generator vs Sine Wave.**
> - **`Signal Generator`** block (the type Part 1 uses): the **Frequency** field is in **Hertz**. Type `5000`.
> - **`Sine Wave`** block in *Time-based* mode: the **Frequency** field is in **rad/s**. Type `2*pi*5000`.
> Picking the wrong units gives you a carrier at $5000/(2\pi) \approx 796$ Hz or at $2\pi \cdot 5000 \approx 31.4$ kHz (which then aliases). Either way the demod fails silently — the model still runs, the audio just sounds like noise.

**Block 1 = Signal Generator (sine), Amplitude $= 2$, Frequency $= 5000$ Hz.** Branch the output into both Modulator and Demodulator multipliers.

#### Missing block #2 — **LPF (`Analog Filter Design` block)**

- **Library:** DSP System Toolbox → Filtering → Filter Implementations → Analog Filter Design.
- **Type:** Lowpass.
- **Design:** Butterworth.
- **Order $n$:** $6$ (or $4$ if you don't mind a touch of $2f_c$ leakage — $6$ gives clean rejection).
- **Cutoff:** $2\pi \cdot 5000$ rad/s ($5$ kHz). Justification:
  - Must pass the audio up to $\sim 4$ kHz $\Rightarrow$ $\text{cutoff} \geq 4$ kHz.
  - Must reject the $2f_c = 10$ kHz image $\Rightarrow$ $\text{cutoff} \ll 10$ kHz.
  - $5$ kHz sits between the two with one octave of separation to the image; 6th-order Butterworth at $f/f_c = 2$ gives $\sim 36$ dB rejection — more than enough.

**Block 2 = Analog Filter Design, Lowpass Butterworth, $n = 6$, $\text{cutoff} = 2\pi \cdot 5000$ rad/s.**

> [!warning] **Don't reuse the LPF cutoff from #1.1 ($f_c = 20$ kHz example).** That setup had $2f_c = 40$ kHz way above the audio, so the LPF cutoff could be lazy. Here $2f_c$ is much closer ($10$ kHz vs a $4$ kHz audio band) — the cutoff has to be tighter and the order higher.

#### Corrected `Dem Gain`

The math: coherent demod outputs $\tfrac{1}{2}m(t) + \tfrac{1}{2}A + \text{(}2\omega_c\text{ images)}$. After the LPF passes only baseband, you have $\tfrac{1}{2}m(t) + \tfrac{1}{2}A$. AC-coupling (or the audio-out hardware) kills the $\tfrac{1}{2}A$ DC term. The $\tfrac{1}{2}$ on $m(t)$ must be undone for the recovered audio to match the direct-path audio in amplitude.

**`Dem Gain` $= 2$.** Justification: cancels the $\tfrac{1}{2}$ factor from $r(t)\cos(\omega_c t) = \tfrac{1}{2}(A + m(t)) + \ldots$ The block ships configured as `Gain = 0`, which would mute the demod path entirely — that's the misconfiguration the prompt hints at.

> [!warning] **If you hear the demod path much quieter than the direct path,** you forgot the $\times 2$ gain (or left it at $0$). If it's much louder, you set the gain too high (or possibly to $4$ by mistake). It should be **$2$** for parity with the direct path.

### Walkthrough — verify both paths sound the same

1. **Run the simulation.**
2. With the **Manual Switch** in the **direct path** position, listen to the audio output. You should hear the `tada.wav` sound.
3. **Flip the Manual Switch** to the modulated/demodulated path. The audio should sound **the same** — same volume, same timbre.
4. Open the **Demodulated Signal Scope**. You should see two traces (direct and demod) overlapping closely, with at most a small delay between them.
5. **Screenshot** the Demodulated Signal Scope showing both traces.

> [!example] **Sanity-check checklist**
> - [ ] Carrier source is **branched** (one block, two outgoing wires) — not duplicated
> - [ ] No clipping in the modulated path scope (means modulation index stayed $\leq 1$)
> - [ ] No high-frequency hiss after the LPF (means cutoff is rejecting the $10$ kHz image)
> - [ ] Both paths overlap on the scope within a small delay (means the gain is correct)
> - [ ] Audibly identical (means everything is right)

### Final answer summary

**Block 1: Signal Generator (sine), Amplitude $= 2$, Frequency $= 5000$ Hz, output branched to both multipliers. Block 2: Analog Filter Design (Lowpass Butterworth, $n = 6$, $\text{cutoff} = 2\pi \cdot 5000$ rad/s). Dem Gain $= 2$.** Justifications: $f_c = 5$ kHz is the unique window satisfying the simulation-Nyquist bound ($f_c < 11025$ Hz), AM sideband rule ($f_c > 2B$), and clean-image bound ($2f_c < f_s/2$); LPF cutoff at $5$ kHz with order $6$ passes the audio while rejecting the $10$ kHz image by $\sim 36$ dB; gain of $2$ undoes the $\tfrac{1}{2}$ from coherent demod.

---

## Cross-references

- [[amplitude-modulation]] — the math behind everything in #1, #2, #3
- [[modulation-index]] — $\mu$ definitions used in #1.4, #2.3, #2.4, #2.5
- [[coherent-demodulation]] — the receiver model in #1 and #3
- [[envelope-detection]] — the receiver model in #2
- [[butterworth-filter]] — the LPF and BPF used throughout
- [[lab-eee-304-lab-4-am-modulation]] — source summary
- [[eee-304]] — course page

## Report template (copy-paste skeleton)

```
EEE 304 Lab 4 — AM Modulation
Name: Jayden Le      Date: 2026-MM-DD

#0. Overview
    [4–6 sentences as in the example above]

#1. Coherent Demodulation
   1.1 n = 4, cutoff = 2*pi*5000 rad/s
       [screenshot of Demodulated Signal Scope showing matched freq + amplitude]
   1.2 [5 spectrograms + side-by-side baseband vs demod+filtered]
   1.3 [3 spectrograms at f_c = 10k/5k/1k + 1-paragraph discussion of sideband overlap]
   1.4 [3 spectrograms at amp = 1/2/4 + paragraph confirming Section 3]

#2. Envelope Detection
   2.1 [6 scope screenshots + per-scope explanation table]
   2.2 [demod+filtered spectrogram at Wlo = 1·2π + DC explanation]
   2.3 μ = 0.5
   2.4 [spectrogram + time-domain at μ = 1 + observation]
   2.5 [spectrogram + scope at μ = 2 + harmonic distortion observation]

#3. tada.wav fill-in
    Block 1 (carrier source): Signal Generator, sine, amplitude=2, freq=5000 Hz
                              (output branched into BOTH Modulator and Demodulator)
    Block 2 (LPF): Analog Filter Design, Butterworth lowpass, n=6, cutoff=2*pi*5000 rad/s
    Dem Gain: 2
    Justification: f_c constrained by sim Nyquist (FixedStep=1/22050 → fs/2=11025 Hz)
                   AND by AM rule (fc > 2B, B≈2 kHz for tada) AND by 2fc < fs/2;
                   intersection is fc ≈ 5 kHz. LPF cutoff at 5 kHz passes audio,
                   rejects the 10 kHz image. Gain of 2 undoes the 1/2 in coherent demod.
    [screenshot of Demodulated Signal Scope showing both paths overlap]
```

> [!note] **About the report template above.** It's intentionally written in plain ASCII (Greek letters as Unicode, no `$...$`) — it's a skeleton for you to copy into a Word doc / handwritten submission, not a wiki page. The wiki body above renders the same equations in proper LaTeX.
