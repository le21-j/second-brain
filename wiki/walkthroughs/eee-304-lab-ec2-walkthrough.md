---
title: EEE 304 Lab EC2 — Feedback Control with an Arduino (Walkthrough)
type: walkthrough
course:
  - "[[eee-304]]"
tags: [eee-304, lab, walkthrough, extra-credit, arduino, simulink, feedback-control, integral-controller, plant-identification, linearization]
sources:
  - "[[lab-eee-304-lab-ec2-feedback-control]]"
created: 2026-05-03
updated: 2026-05-06
---

# EEE 304 Lab EC2 — Feedback Control with an Arduino (Walkthrough)

> [!note] **What this is.** A per-question walkthrough of the **Extra Credit Lab EC2** for EEE 304. For every numbered question I (a) **state it** verbatim, (b) **explain the overarching concept** so you understand what's being tested, then (c) **walk the concrete steps** to complete it. Use this alongside the lab manual: [EEE 304 Lab EC2.pdf](../../raw/labs/EEE_304_Lab_EC2.pdf).

> [!warning] **Prereq.** This lab assumes you've completed **Lab EC1** (or at least gone through Section 2 of EC1 to install the **MATLAB + Simulink Support Package for Arduino Hardware**). It also assumes you can deploy a Simulink model to the **Arduino Due** in **Monitor & Tune** (External) mode.

---

## What you build

A **closed-loop illumination controller**: a white **LED** is the actuator (driven by Arduino PWM pin 12), a **phototransistor** is the sensor (read by ADC pin A0), and a **discrete-time integral controller** running on the Due holds the measured light intensity at a desired set-point even when the LED's nonlinear response or external lighting tries to disturb it.

**Big-picture pipeline:**

```text
[reference setpoint] ─┬──> [error] ──> [C(z) integrator] ──> [PWM 0–255] ──> [LED]
                      │                                                       │
                      │                                                  (light)
                      │                                                       ↓
                      └────[low-pass filter]──[ADC, 12-bit]──[phototransistor]
```

**Two Simulink models, two roles:**

| Model | Role |
|---|---|
| [Calibrate_Sensor.slx](../../raw/labs/Calibrate_Sensor.slx) | Open-loop characterization: sweep PWM 0–255, record ADC reading. Used to fit the plant model. |
| [Closed_loop_I_Ctrl.slx](../../raw/labs/Closed_loop_I_Ctrl.slx) | The full feedback loop with the integral controller. The thing you tune. |

---

## Hardware setup (read once before starting)

**Bill of materials:** Arduino Due + 1 white LED ($> 3000$ mcd) + 1 NTE3034A phototransistor (or PT334-6C) + 100 kΩ resistor + 100–200 Ω optional current-limit resistor + breadboard + jumper wires.

**Circuit:**

| Connection | Purpose |
|---|---|
| Due **PWM pin 12** → LED anode (through optional 100–200 Ω) | Actuator drive |
| LED cathode → GND | Return |
| Phototransistor **collector (C)** → Due **5V** | Sensor power |
| Phototransistor **emitter (E)** → 100 kΩ pull-down → GND | Sensor signal |
| Junction of E and 100 kΩ → Due **A0** | ADC input |

> [!warning] **Distance matters.** Place the LED **less than 1 cm** from the phototransistor and pointing directly at it. Too far apart → the phototransistor saturates only at high PWM, making the calibration curve unusable.

> [!warning] **Don't skip the 100–200 Ω current limit on the LED.** The Due outputs 3.3 V, the LED is rated for 5 V, so plugging it straight into pin 12 won't blow it up *immediately* — but PWM duty cycles approaching 100 % can stress both the LED and the Due's pin driver. Add the resistor.

---

## #0. Overview

> **#0.** Write an overview of your results.

### How to write it

A short paragraph (4–6 sentences). State **what plant model you fit (a, b)**, **what controller gain achieved 1 rad/s bandwidth**, **how a 10× larger gain looked**, and **at what gain the system went unstable**.

> [!example] **Sample overview**
> *In this lab I built an LED + phototransistor feedback loop on an Arduino Due and identified the open-loop plant via calibration: the input-output map was well-fit by an exponential $\text{outp} = a \exp(b\cdot\text{inp})$ with $a \approx 80$ and $b \approx 0.011$, log-linearizing to a unit-gain plant. With the integrator $C(z) = K_I/(z-1)$ and sample time $T_s = 0.01$ s, choosing $K_I = 0.01$ produced a closed-loop time constant of $\sim 1$ s (1 rad/s bandwidth), confirmed by the slow but smooth tracking of a square-wave reference. Increasing to $K_I = 0.1$ produced ~10 rad/s bandwidth and visibly faster step response with mild ringing. Pushing $K_I$ above $\sim 1$ caused sustained oscillations — confirming the textbook prediction that excessive integral gain destabilizes the loop.*

**Headline:** an integral controller with $K_I \approx 0.01$ on an LED + phototransistor system gives clean ~1-second tracking; 10× more is fast but ringy; 100× is unstable.

---

## #1. Plant identification — record `inp`, `outp` and fit $a, b$

> **#1.** Provide a table of the two vectors **"inp"** and **"outp"** you recorded as discussed in Section 2.2 with the values of the PWM and Intensities from the calibration experiment. Provide a plot and the identified values of the plant parameters $(a, b)$.

### The concept — why a model is needed

Feedback control needs a **plant model** $P$ relating actuator input (PWM duty, 0–255) to sensor output (ADC reading, 0–4095). For an LED + phototransistor pair, the relationship is **nonlinear** because:

- **The LED's $I$–$V$ curve is exponential** above its forward voltage.
- **The phototransistor's collector current is roughly proportional to incident photon flux**, but its output voltage across a fixed load saturates as it approaches the supply rail.

The composite map empirically fits very well to an **exponential model**:

$$\text{outp} = a \cdot \exp(b \cdot \text{inp})$$

where $\text{inp} \in [0, 255]$ is the PWM register value and $\text{outp} \in [0, 4095]$ is the 12-bit ADC reading. Once you have $a$ and $b$, you **log-linearize** by passing $\text{outp}$ through $\ln$ — then the plant becomes linear with slope $b$ and intercept $\ln a$, which you handle by setting the Simulink "gain" block to $1/a$ so the **effective plant gain becomes 1** at every operating point.

> [!tip] **Why linearize at all?** Linear feedback theory (transfer functions, Bode, root-locus) only works if the plant is linear. Around an operating point you can replace any smooth nonlinearity with a Taylor-series first-order approximation — the error is small as long as you stay close to that point. Here the log trick gives you **global linearity** because the nonlinearity happens to be exactly exponential.

### Walkthrough

1. **Open `Calibrate_Sensor.slx`** in Simulink. The model has:
   - A **constant block** (PWM value) controlled by a slider, range 0–255, fed to PWM pin 12.
   - An **ADC read** block reading pin A0, output range 0–4095.
   - A **scope** displaying both signals.
   - **Sample time fixed at $T_s = 0.01$ s** (don't change it).

2. **Set MODE to External** and click **Monitor & Tune**.

3. **Sweep the PWM slider in steps** of ~20 from 0 → 255. At each step, **wait ~1 second** for the readout to settle, then **record the steady ADC value** in your notebook or directly into MATLAB:

   ```matlab
   inp  = [0   20  40  60  80  100 120 140 160 180 200 220 240 255];
   outp = [...];   % fill in with your measurements
   ```

   > [!warning] **Don't rush the slider.** The phototransistor + 100 kΩ load has an RC time constant of a few ms but the human-eye-aligned low-pass filter slows it further. If you slam the slider, the recorded values will be transients, not steady-state.

   > [!tip] **How many points?** 12–15 evenly-spaced steps is more than enough for a good fit. You don't need 256.

4. **Plot to check the shape:**

   ```matlab
   plot(inp, outp, 'o-');
   xlabel('PWM input (0–255)');
   ylabel('ADC output (0–4095)');
   title('Calibration: light intensity vs. PWM duty');
   grid on;
   ```

   > [!example] **Expected shape.** The first ~30–40 PWM values give very low ADC (LED below forward-voltage threshold, basically off). From there the ADC climbs **exponentially**. Above some PWM value ($\geq 200$) it may saturate the phototransistor — drop those tail points before fitting.

5. **Fit the exponential model.** Three options, pick whichever is convenient:

   **Option A — Curve Fitting App (what the manual shows):**
   ```matlab
   cftool         % opens GUI
   ```
   In the GUI: X data = `inp`, Y data = `outp`, fit type = **Exponential**, equation = `a*exp(b*x)`. Click **Fit**, copy the printed $a$ and $b$.

   **Option B — Linear regression on $\ln(\text{outp})$ (analytical, no GUI):**
   ```matlab
   p    = polyfit(inp, log(outp), 1);   % p(1) = b,  p(2) = log(a)
   b_hat = p(1);
   a_hat = exp(p(2));
   fprintf('a = %.4g,  b = %.4g\n', a_hat, b_hat);
   ```
   This is what the manual hints at when it says "*Its parameters can be estimated by linear regression of inp vs ln(outp).*"

   **Option C — Nonlinear lsq:**
   ```matlab
   model    = @(p, x) p(1) * exp(p(2) * x);
   p0       = [50, 0.01];
   p_hat    = lsqcurvefit(model, p0, inp, outp);
   a_hat    = p_hat(1);
   b_hat    = p_hat(2);
   ```

6. **Verify the fit** by overlaying:

   ```matlab
   inp_fine = linspace(min(inp), max(inp), 200);
   plot(inp, outp, 'o', inp_fine, a_hat*exp(b_hat*inp_fine), '-');
   legend('measured','fit');
   ```

> [!example] **Sample fit numbers** *(yours will differ depending on LED, phototransistor, distance, ambient light)*
> $a \approx 80$, $b \approx 0.011$ — meaning $\text{outp}(\text{inp}=200) \approx 80 \cdot e^{0.011 \cdot 200} \approx 80 \cdot e^{2.2} \approx 720$.

7. **Plug $1/a$ into the gain block.** Open `Closed_loop_I_Ctrl.slx`, find the gain block in the feedback path (between the ADC read and the natural log), and **set its value to `1/a_hat`** (the value you fit). Save the model.

> [!tip] **What the gain block does.** The closed-loop model takes $\ln(\text{outp})$, but the controller is meant to compare against a reference in the same scale. Multiplying the raw ADC by $1/a$ before $\ln$ gives $\ln(\text{outp}/a) = \ln a + b\cdot\text{inp} - \ln a = b\cdot\text{inp}$ — i.e., the **plant becomes a pure gain $b$**, removing the offset.

**Answer:** the table of `inp`/`outp` measurements, the plot with the fit overlaid, and your numerical $a$ and $b$.

---

## #2. Design controller gain $K_I$ for 1 rad/s, then 10×

> **#2.** Design a controller gain and implement it in the integrator. Demonstrate how the output response is affected when this gain is changed. First, use a gain that will result in a Bandwidth of 1 rad/sec (Time Constant 1 sec or 100 samples for the hard-coded Sample Time of 0.01 sec.) Then you can increase the gain by a factor of 10. A convenient way to demonstrate the results is to add a "small" square wave at the reference input (say 50–100 units) and take screen shots of the scope under the Monitor & Tune option.

### The concept — discrete integrator and its bandwidth

The controller is a **discrete-time integrator**:

$$C(z) = \frac{K_I}{z-1}$$

After log-linearization the plant is unity-gain (you set the Simulink gain block to $1/a$), so the open-loop transfer function is:

$$L(z) = C(z) \cdot P(z) = \frac{K_I}{z-1}$$

The closed-loop transfer function is:

$$\frac{Y(z)}{R(z)} = \frac{L(z)}{1 + L(z)} = \frac{K_I}{z - 1 + K_I} = \frac{K_I}{z - (1 - K_I)}$$

Closed-loop pole at $z = 1 - K_I$. The continuous-time equivalent decay rate (using $z = e^{-\sigma T_s} \approx 1 - \sigma T_s$) is:

$$\boxed{\sigma \approx \frac{K_I}{T_s}}$$

The closed-loop **bandwidth** is approximately $\omega_{BW} \approx \sigma$, and the **time constant** is $\tau = 1/\sigma$. With $T_s = 0.01$ s:

| Target bandwidth | Target $\tau$ | Required $K_I$ | Settling samples ($\sim 5\tau$) |
|---|---|---|---|
| **1 rad/s** | 1 s | **0.01** | 500 samples (5 s) |
| **10 rad/s** | 0.1 s | **0.1** | 50 samples (0.5 s) |
| 100 rad/s | 0.01 s | 1.0 | (loop-delay-limited; expect instability) |

> [!info]- 📐 Show derivation — closed-loop pole → time constant
>
> Take the difference equation form of the integrator: $u[k+1] = u[k] + K_I \cdot e[k]$. With unity-gain plant $y[k] = u[k]$ and error $e[k] = r[k] - y[k]$:
>
> $$y[k+1] = y[k] + K_I (r[k] - y[k]) = (1-K_I)\,y[k] + K_I\,r[k]$$
>
> For a step reference $r[k] = R$ for $k\geq 0$, the response is geometric with ratio $1 - K_I$. In continuous time, $y(t) = R(1 - e^{-\sigma t})$ where $e^{-\sigma T_s} = 1 - K_I$, so $\sigma = -\ln(1 - K_I)/T_s \approx K_I/T_s$ for small $K_I$.

### Walkthrough

1. **Open `Closed_loop_I_Ctrl.slx`.** Find the **integrator block** (labeled $K_I/(z-1)$ or similar) and the **reference input** (a constant or signal generator).

2. **Add a small square-wave reference** — manual recommends ±50–100 units around an operating point near the middle of your linear range (e.g., 50% PWM):

   - Replace the constant reference block with a **Pulse Generator** block.
   - Set: **Amplitude** = 100, **Period** = 4 s, **Pulse Width** = 50 %, **Phase delay** = 0.
   - Add a constant offset of, say, **400** so the operating point is in the middle of the ADC range.

3. **First run — $K_I = 0.01$ (target bandwidth 1 rad/s):**
   - Open the integrator block dialog and **set $K_I = 0.01$**.
   - **Monitor & Tune.** Open the scope.

   > [!example] **Expected step response shape — 1 rad/s.** The output **smoothly tracks** the square wave with **first-order exponential** rises. **No overshoot.** Each level transition takes roughly **1 second** (the time constant) to reach 63% of the new value, and ~5 seconds to fully settle.

4. **Take a screenshot** with the reference (square wave) and output (smoothed exponential) both visible. Label as "$K_I = 0.01$, bandwidth $\approx 1$ rad/s."

5. **Second run — $K_I = 0.1$ (10× faster):**
   - Stop the simulation, change the integrator gain to **$K_I = 0.1$**, run again.

   > [!example] **Expected step response shape — 10 rad/s.** The output now reaches the new level in about **0.1 seconds** — visibly snappy. You may see **mild overshoot or ringing** because at $\omega_{BW} = 10$ rad/s the loop is starting to feel the effect of the **PWM update rate (~500 Hz)** and the **sensor low-pass filter**. Still stable, just no longer textbook-clean first-order.

6. **Take a second screenshot.** Label as "$K_I = 0.1$, bandwidth $\approx 10$ rad/s."

> [!tip] **Why the response is not perfectly first-order.** The "unity-gain plant" assumption is an idealization — there's still a finite-bandwidth low-pass filter on the sensor (to reject the ~500 Hz PWM ripple), and the ADC has 10 ms quantization in time. As you push $K_I$ higher, these neglected dynamics add **phase lag** that the simple bandwidth formula doesn't capture, and the closed-loop response gains overshoot.

**Answer:** two annotated scope screenshots — one for $K_I = 0.01$ (slow, smooth), one for $K_I = 0.1$ (fast, mild overshoot) — with axes labeled and showing the square-wave reference overlaid with the system output.

---

## #3. Demonstrate instability with too-large $K_I$

> **#3.** Demonstrate that if the controller gain is too large, the closed-loop system becomes unstable.

### The concept — discrete-time stability boundary

For the **idealized model** $L(z) = K_I/(z-1)$, the closed-loop pole at $z = 1 - K_I$ stays inside the unit circle (stable) for $0 < K_I < 2$. **But** the real system has additional unmodeled lags (the sensor LPF, PWM holding, ADC sample delay), each of which adds **phase lag** the ideal pole formula doesn't see. As you increase $K_I$, the **gain crossover frequency** moves up; once it crosses a frequency where the cumulative phase lag equals $-180°$, the closed-loop system has a pole on or outside the unit circle and goes unstable.

In practice, this happens **well before $K_I = 2$** — typically around $K_I \in [0.5, 1.5]$ depending on your filter time constants and the LED's switching rate.

### Walkthrough

1. **Stop the simulation.** Set $K_I$ to a much larger value — start with **$K_I = 1$**.

2. **Run Monitor & Tune.** Watch the scope.

   > [!example] **What unstable looks like.** The output:
   > - **Oscillates continuously** with growing or sustained amplitude.
   > - The oscillation frequency is much higher than your reference square-wave frequency.
   > - The output may **rail to 0 or 4095** (ADC saturation) when the swing exceeds the linear range.
   > - Audibly: if you have headphones near the rig, you may hear a buzz from the LED switching.

3. **Increase further** until oscillation is unmistakable. Try $K_I = 2$, then $K_I = 5$. By $K_I \geq 2$ you're guaranteed unstable in the ideal model alone.

4. **Take a screenshot** of the oscillating output. Label with the exact $K_I$ used.

5. **Optionally, find your boundary.** Sweep $K_I$ from your last stable value (say 0.1) upward in steps (0.2, 0.4, 0.7, 1.0, 1.5, 2.0). The boundary is the smallest $K_I$ at which the output starts ringing forever instead of damping.

> [!warning] **Be ready to stop fast.** When the loop oscillates, the LED can flicker rapidly and the phototransistor can saturate — fine for a few seconds but don't leave it running unattended. Click **Stop Simulation** as soon as you have your screenshot.

> [!tip] **Why this matters in real design.** The simple integrator $C(z) = K_I/(z-1)$ has **only one tuning knob**, and as you saw, pushing it for speed eventually destabilizes you. Real industrial controllers add a **derivative term** (PID) or shape the loop with **lead/lag compensators** to push the stability boundary higher — that's the subject of [[eee-480]] and [[eee-481]].

**Answer:** annotated scope screenshot showing sustained or growing oscillation, with the value of $K_I$ that produced it (e.g., $K_I = 1.5$ — went unstable at this gain).

---

## #4. Photo of the hardware setup

> **#4.** Take a photo of your last hardware set up and attach it to the lab report.

### The shot list

A single clear photo showing:

- The **Arduino Due** with USB programming cable connected.
- The **breadboard** with:
  - The **LED** plugged in (note the orientation — long lead = anode = drives PWM pin 12 side).
  - The **phototransistor** facing the LED at $\leq 1$ cm.
  - The **100 kΩ pull-down** resistor on the phototransistor emitter.
  - (Optional) the 100–200 Ω current-limit resistor on the LED.
- **Jumper wires** to GND, 5V, A0 (sensor read), and pin 12 (PWM out).

> [!tip] **Annotate your photo** with arrows labeling **PWM 12 → LED**, **A0 ← phototransistor**, **5V → C**, **E → 100k → GND**. Makes grading and your future-self debugging easier.

**Answer:** one labeled JPG/PNG embedded at the end of the report.

---

## Submission checklist

| # | Deliverable | Where it lives in the report |
|---|---|---|
| 0 | Overview paragraph | Top |
| 1 | Calibration table + plot + fit $(a, b)$ | Section 1 |
| 2 | Two scope screenshots ($K_I = 0.01$ and $K_I = 0.1$) | Section 2 |
| 3 | Scope screenshot showing instability + the $K_I$ that caused it | Section 3 |
| 4 | Photo of breadboard + Due + LED + phototransistor wiring | Section 4 |

---

## Related

- [[eee-304-lab-ec1-walkthrough]] — sibling extra-credit lab (Arduino-based digital filtering with the same Due)
- [[eee-304-lab-4-walkthrough]] — Lab 4 (AM modulation/demodulation), introduces Simulink + the `butter` filter design workflow
- Lab manual — [EEE 304 Lab EC2.pdf](../../raw/labs/EEE_304_Lab_EC2.pdf)
- Simulink models — [Calibrate_Sensor.slx](../../raw/labs/Calibrate_Sensor.slx), [Closed_loop_I_Ctrl.slx](../../raw/labs/Closed_loop_I_Ctrl.slx)
