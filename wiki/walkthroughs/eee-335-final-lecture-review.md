---
title: EEE 335 Final Exam — Lecture-by-Lecture Review (Analog Portion, Lectures 17–36)
type: walkthrough
course:
  - - eee-335
tags:
  - eee-335
  - finals
  - walkthrough
  - lecture-review
  - analog
  - mosfet-amplifier
  - frequency-response
  - cascode
  - differential-pair
sources:
  - raw/slides/eee-335/lecture-review-units-4-6-final-spring-2026-slides.pdf
  - raw/slides/eee-335/practice-final-exam-spring-25.pdf
  - raw/slides/eee-335/practice-final-exam-spring-25-solutions.pdf
created: 2026-05-03
updated: 2026-05-03
---

# EEE 335 Final — Lecture-by-Lecture Review (Lectures 17–36 + CCA + CCA-HFR)

> [!warning] **Exam logistics — do not skip.**
> - **Date/Time:** Tuesday, May 5, 2026 — **12:10 PM – 2:00 PM** (110 minutes).
> - **Room:** SCOB 250.
> - **Coverage:** **Units 4–6 only** — Lectures 17–36 plus CCA (Cascode Amp) and CCA-HFR. **Sedra/Smith Chapters 7, 8, 9, 10.** Exam 1 material (Units 1–3, MOSFET physics + CMOS digital) is **NOT** on the final.
> - **Format:** ~**75% multi-part problems with partial credit** (must show work) + ~**25% multiple-choice / true-false / short-answer** (no partial credit). **110 points available** (10 pts of bonus).
> - **Allowed:** scientific calculator, **one** 8.5×11" double-sided **OR** two single-sided **handwritten formula sheet(s)**, pens/pencils/erasers.
> - **NOT allowed:** textbook, notes (other than the formula sheet), tablets, phones, classmates.

> [!tip] **What this is.** A per-lecture roadmap for the final, built on McDonald's 115-slide "Units 4–6 Review" deck. For every lecture I list (a) the **textbook section**, (b) **what's tested**, (c) **the headline formulas/results to put on your cheat sheet**, and (d) the **recommended practice problems** McDonald flagged in the review.
>
> The companion piece [[eee-335-final-walkthrough]] has fully-worked Unit-1–6 problems with derivation drop-downs — use this lecture-review for **what to memorize and where it lives**, then use the walkthrough for **how to solve a specific problem type**.

---

## Quick study strategy (read once, then go)

1. **Build the cheat sheet first.** Tables 7.2 (small-signal models), 7.4 (CS / CS-with-Rs / CG / SF characteristics), 10.1 (high-freq MOSFET model), and 1.2 (LP/HP STC networks) are the four anchor tables — copy them verbatim. Add the **Unit 6 formulas** ($A_{v,\text{cascode}}$, diff-pair $g_m$, CMRR for s.e. and diff. output, current-mirror-loaded diff amp). See "Master Cheat Sheet" at the end of this doc.
2. **Re-do Examples 8.3, 10.5, 10.6, 10.8, 10.9, 9.1, 9.11** with the answers covered. These are the EXACT problem types that appear on the exam.
3. **Drill the True/False bank** (Section "T/F + MC quick-fire" near the bottom) — these are easy points if you've internalized the table.
4. **Practice the gain-comparison + bandwidth-trade question** (Cascode vs CS under big/small $R_L$ — Lecture CCA-HFR). Practice Final Problem #2 is exactly this.

---

# Unit 4 — Integrated Circuit (IC) Amplifiers (Lectures 17–22)

> [!example] **Unit 4 in one breath.** Take a transistor, give it a DC bias so it sits in saturation, drop a small AC signal on the gate, and ask: **what's $R_\text{in}$, $A_{vo}$, $R_o$, $A_v$, $G_v$?** Three configurations matter (CS, CG, CD/SF), with two variants (CS with $R_S$, CS with active load). Tables 7.4 and 8 boxed formulas.

## Lecture 17 — Transistor Amplifier Basic Principles (§7.1.2, 7.1.4)

- **What's tested:** Identify why a CS-like circuit gives a voltage gain. Compute the **DC operating (Q) point**:
  $$I_{DQ} = \tfrac{1}{2}\,k_n(V_{GS} - V_t)^2, \qquad V_{DSQ} = V_{DD} - I_{DQ}\,R_D$$
- **Headline:** Q-point must sit in **saturation** (i.e., $V_{DS} \geq V_{OV}$) for amplification. Triode → distortion; cutoff → no signal.
- **What to know:**
  - Voltage amplifier definition $v_o = A_v v_i$.
  - Load line and graphical Q-point — recognize sat/triode boundary on the $i_D$–$v_{DS}$ plot.
  - The input is $v_i = v_{gs}$ (small AC) ridden on $V_{GS}$ (DC).

## Lecture 18 — Small-Signal Model (§7.2.1)

- **What's tested:** Replace the MOSFET with its **small-signal equivalent** (hybrid-π or T model). Compute $g_m$ three ways:
  $$g_m = k_n'(W/L)V_{OV} = \sqrt{2k_n'(W/L)\,I_{DQ}} = \frac{2I_{DQ}}{V_{OV}}$$
- **Small-signal validity:** $v_{gs} \ll 2V_{OV}$. If violated, you can't linearize.
- **Headline models** (see Table 7.2):

| Model | When to use |
|---|---|
| **Hybrid-π** | When the source is grounded (pure CS analysis) or you need explicit $r_o$ |
| **T-model** | When the source has a resistor (CS-with-$R_s$, CG, source follower) — $1/g_m$ at the source is built-in |

- 📝 **Recommend Practice:** any HW5 problem on small-signal parameter extraction.

## Lecture 19 — Three Basic Configurations + Key Intrinsic Features (§7.3.1–7.3.7)

- **What's tested:** Given a configuration (CS, CG, or SF), pull $R_\text{in}$, $A_{vo}$, $R_o$, $A_v$, $G_v$ from memory or derive in 2 minutes.
- **Headline (memorize Table 7.4 — neglect $r_o$):**

| Amp | $R_\text{in}$ | $A_{vo}$ | $R_o$ | $A_v$ | $G_v$ |
|---|---|---|---|---|---|
| **CS** | $\infty$ | $-g_m R_D$ | $R_D$ | $-g_m(R_D \| R_L)$ | $-g_m(R_D \| R_L)$ |
| **CS-w/$R_s$** | $\infty$ | $\dfrac{-g_m R_D}{1+g_m R_s}$ | $R_D$ | $\dfrac{-g_m(R_D \| R_L)}{1 + g_m R_s}$ | same as $A_v$ |
| **CG** | $1/g_m$ | $g_m R_D$ | $R_D$ | $g_m(R_D \| R_L)$ | $\dfrac{R_D \| R_L}{R_\text{sig} + 1/g_m}$ |
| **SF** | $\infty$ | $1$ | $1/g_m$ | $\dfrac{R_L}{R_L + 1/g_m}$ | same as $A_v$ |

> [!tip] **Pattern recognition.**
> - **CS:** voltage amplifier (high gain, infinite $R_\text{in}$, but moderate $R_o$). Inverts (-).
> - **CG:** **current buffer** ($R_\text{in} = 1/g_m$ small, output current ≈ input current). Non-inverting.
> - **SF:** **voltage buffer** ($A_v \to 1$, low $R_o = 1/g_m$). Non-inverting. Useful as last stage to drive a heavy load.

- **Voltage gain bookkeeping** (also memorize):
  $$A_v = A_{vo}\frac{R_L}{R_L + R_o}, \qquad G_v = \frac{R_\text{in}}{R_\text{in} + R_\text{sig}}\,A_{vo}\,\frac{R_L}{R_L+R_o}$$
- **For a good voltage amp:** want **$R_\text{in}$ BIG** + **$R_o$ small** + **$R_L$ big**. CS+SF cascade does this nicely.

## Lecture 20 — IC Biasing: Current Mirror (§8.2.1, 8.2.3)

- **What's tested:** Generate a stable DC bias current using a **current mirror** (Q1 diode-connected, Q2 mirrors). Account for **channel-length modulation** as a finite output resistance.
- **Headline formulas:**
  $$I_O = I_\text{REF}\,\frac{(W/L)_2}{(W/L)_1}\quad\text{(ideal)}$$
  $$I_O = I_\text{REF}\,\frac{(W/L)_2}{(W/L)_1}\!\left(1 + \frac{V_O - V_{GS}}{V_A}\right)\quad\text{(with channel-length modulation)}$$
  $$I_\text{REF} = \frac{V_{DD} - V_{GS}}{R}$$
- **Saturation requirement on Q2:** $V_O \geq V_{GS} - V_{tn} = V_{OV}$ — sets the lower limit of output swing.
- **Current steering:** chain mirrors to bias multiple stages (Q1→Q2, Q3, ...). All transistors must stay in saturation.
- 📝 **Recommend Practice:** **HW5 problems 8.2, 8.3, 8.6** + In-class Exercise 8.2.

## Lecture 21 — The Basic Gain Cell (§8.3.1, 8.3.2)

- **What's tested:** A CS amplifier loaded by an **ideal current source** (no $R_D$ — instead the load is $r_o$ of the current source itself). This is the canonical IC-style amplifier.
- **Intrinsic gain:** when load is **ideal** ($R_O = \infty$):
  $$\boxed{A_{vo} = -g_m r_o = -V_A\sqrt{\frac{2k_n'(W/L)}{I}} = -\frac{2V_A}{V_{OV}}}$$
- **With PMOS current source as load** ($R_o = r_{o2}$, finite):
  $$A_{v0} = -g_{m1}(r_{o1} \| r_{o2}) = -\frac{g_m r_o}{2}\quad(\text{if } V_{A1} = |V_{A2}|)$$
- **Why it matters:** Intrinsic gain is the upper bound on what one transistor can do alone. Want bigger gain? **Cascode** (Lecture CCA).
- 📝 **Recommend Practice:** **Example 8.3** (worked in the review slides — DC + small-signal gain + output swing range), **Exercise 8.8**, **HW 8.46**.

> [!example] **Example 8.3 problem signature** (commonly mirrored on the final)
> Given $V_{DD}, V_{tn}, V_{tp}, k_n', k_p', V_A, I_\text{REF}, |V_{OV}|$:
> a) Find DC component of $v_I$ and the $W/L$ ratios so all transistors operate at the given $|V_{OV}|$.
> b) Determine the small-signal voltage gain.
> c) Determine the allowable range of output signal swing.
> d) (Variant) Replace the current source with $R_D$; find $I_D, V_{DD}'$ to keep gain and swing unchanged.

## Lecture 22 — Buffers: CG and SF (§8.4.1)

- **What's tested:** **Common Gate as a current buffer** ($A_{io} = 1$ A/A — the input current rides through to the output). Compute its **input and output resistances**, especially when **$r_o$ is included**:
  $$R_\text{in,CG} = \frac{r_o + R_L}{1 + g_m r_o} \approx \frac{1}{g_m} + \frac{R_L}{g_m r_o}$$
  $$R_\text{out,CG} = r_o + R_S + g_m r_o R_S \approx (g_m r_o)R_S \quad (\text{when } R_S \neq 0)$$
- **Why this matters:** $R_\text{out}$ becomes **$g_m r_o$ times** $R_S$ — a huge boost. This is why **cascoding** dramatically increases output resistance.
- 📝 **Recommend Practice:** **Exercises 8.10, 8.11**.

---

# Unit 5 — Frequency Response of Single-Stage Amplifiers (Lectures 23–30 + CCA-HFR)

> [!example] **Unit 5 in one breath.** Add capacitors. The MOSFET has internal $C_{gs}, C_{gd}, C_{db}$ (Table 10.1). External capacitors $C_{C1}, C_{C2}, C_S$ couple AC and bypass DC at low frequencies. **EEE 335 focuses on midband + high-frequency band** — at midband, all C's are open or short and gain is flat; at HF, internal MOSFET caps roll off the gain. Estimate the rolloff frequency $f_H$ four ways, increasing in sophistication.

## Lecture 23 — Amplifier Frequency Response, STC Networks (§1.6)

- **What's tested:** Recognize when an amp has a single-time-constant transfer function. Plot 20-log-magnitude (dB) Bode plots.
- **Headline formulas (memorize Table 1.2):**

| Network    | $T(s)$                    | $T(j\omega)$                    | $          | T   | $                                | Phase                         | $\omega_0$      |
| ---------- | ------------------------- | ------------------------------- | ---------- | --- | -------------------------------- | ----------------------------- | --------------- |
| **LP-STC** | $\dfrac{K}{1+s/\omega_0}$ | $\dfrac{K}{1+j\omega/\omega_0}$ | $\dfrafic{ | K   | }{\sqrt{1+(\omega/\omega_0)^2}}$ | $-\tan^{-1}(\omega/\omega_0)$ | $1/\tau = 1/RC$ |
| **HP-STC** | $\dfrac{Ks}{s+\omega_0}$  | $\dfrac{K}{1-j\omega_0/\omega}$ | $\dfrac{   | K   | }{\sqrt{1+(\omega_0/\omega)^2}}$ | $\tan^{-1}(\omega_0/\omega)$  | $1/\tau$        |

- **Bandwidth definition:** $T(\omega_1)_\text{dB} = T(\omega_2)_\text{dB} = T_\text{max,dB} - 3\text{ dB}$. We typically neglect $\omega_1$ (the low-frequency cut) in EEE 335 — focus on $\omega_2 \equiv \omega_H$.
- 📝 **Recommend Practice:** STC derivations from Lecture 23 + **HW6 1.70**.

## Lecture 24 — High-Frequency MOSFET Model (§10.1.1)

- **What's tested:** Know the **5-cap MOSFET hybrid-π model**: $C_{gs}, C_{gd}, C_{db}, C_{sb}$ (and remember $C_{sb}$, $C_{db}$ are usually ≪ $C_{gs}, C_{gd}$, so we drop them).
- **Capacitance formulas:**
  $$C_{ov} = W L_{ov} C_{ox}, \qquad C_{gd} = C_{ov}, \qquad C_{gs} = \tfrac{2}{3}WLC_{ox} + C_{ov}$$
  $$C_{sb} = \frac{C_{sb0}}{\sqrt{1 + V_{SB}/V_0}}, \qquad C_{db} = \frac{C_{db0}}{\sqrt{1 + V_{DB}/V_0}}$$
- **MOSFET unity-gain frequency** (intrinsic speed):
  $$\boxed{f_T = \frac{g_m}{2\pi(C_{gs} + C_{gd})}}$$
- 📝 **Recommend Practice:** **Exercises 10.1, 10.2**, **HW6 10.1, 10.3**.

## Lecture 25 — High-Frequency Response of CS Amplifier — 1st Analysis (§10.2.2)

- **What's tested:** The simplest HF analysis of a CS amp: collapse $C_{gd}$ into an equivalent input capacitance via Miller, then it's a single-pole LP-STC at the gate.
- **Mid-band gain** ($C_{gd}, C_{gs}$ open):
  $$A_M = G_{V\max} = -\frac{R_G}{R_G + R_\text{sig}}\,g_m R_L', \qquad R_L' = r_o \| R_D \| R_L$$
- **Miller multiplier** for $C_{gd}$:
  $$C_\text{eq} = C_{gd}(1 + g_m R_L'), \qquad C_\text{in} = C_{gs} + C_\text{eq}$$
- **Upper 3-dB frequency (1st analysis — single-pole approx):**
  $$\boxed{\omega_H = \frac{1}{R_\text{sig}'\,C_\text{in}}, \qquad f_H = \frac{1}{2\pi R_\text{sig}'[C_{gs} + C_{gd}(1 + g_m R_L')]}}$$
- 📝 **Recommend Practice:** **Example 10.1**, **Exercise 10.6**, **HW6 10.19, 10.22**.

## Lecture 26 — Miller's Theorem (§10.2.5)

- **What's tested:** Replace an impedance $Z$ that bridges input and output of an amp with gain $K$ by **two impedances to ground**:
  $$\boxed{Z_1 = \frac{Z}{1-K} \text{ (input side)}, \qquad Z_2 = \frac{Z}{1 - 1/K} \text{ (output side)}}$$
- **For inverting amp** ($K = -g_m R_L'$, large negative): $Z_1 = Z/(1-K) = Z/(1 + g_m R_L')$ — this is what makes $C_{gd}$ "appear bigger" at the input by the Miller factor.
- 📝 **Recommend Practice:** **Example 10.4**, **HW6 10.17**.

## Lecture 27 — Frequency Response of CS with Low $R_\text{sig}$ (§10.2.3)

- **What's tested:** When $R_\text{sig} \approx 0$, the input pole vanishes and the response is **dominated by the output node** ($C_L + C_{gd}$ in parallel with $R_L'$). One pole **and** one zero.
- **Transfer function:**
  $$\frac{V_o}{V_\text{sig}} = -g_m R_L' \cdot \frac{1 - s(C_{gd}/g_m)}{1 + s(C_L + C_{gd})R_L'}$$
- **Pole and zero:**
  $$f_H = \frac{1}{2\pi(C_L + C_{gd})R_L'}, \qquad f_Z = \frac{g_m}{2\pi C_{gd}}$$
- **Unity-gain (gain-bandwidth product):**
  $$\boxed{f_t = |A_M| \cdot f_H = g_m R_L' \cdot f_H}$$
- 📝 **Recommend Practice:** **Example 10.2**, **HW6 10.23, 10.25**.

## Lecture 28 — Tools for HF Analysis: Square-Root Method (§10.3.2)

- **What's tested:** When the gain function has multiple poles and zeros, estimate $\omega_H$ as:
  $$\boxed{\omega_H \approx \frac{1}{\sqrt{\bigl(\sum 1/\omega_{pi}^2\bigr) - 2\bigl(\sum 1/\omega_{zi}^2\bigr)}}}$$
- **Dominant-pole approximation:** if $\omega_{p1} \ll$ all others, $\omega_H \approx \omega_{p1}$.
- This is the more accurate generalization of the simple "1/RC" estimate. Use it when no single pole dominates.

## Lecture 29 — Method of Open-Circuit Time Constants (OCTC) (§10.4.3)

- **What's tested:** Estimate $\omega_H$ when there are multiple capacitors but you don't want to grind through the algebra.
- **The recipe:**
  1. Set ALL voltage sources to **short**, current sources to **open**.
  2. For **each capacitor $C_k$**, compute the **resistance $R_k$ seen by it** with **all other capacitors set to OPEN**.
  3. Each capacitor contributes a time constant $\tau_k = C_k R_k$.
  4. **Estimate the 3-dB frequency:**
     $$\boxed{\omega_H \approx \frac{1}{\sum_k \tau_k} = \frac{1}{\sum_k C_k R_k}}$$
- **For a CS amplifier (3 caps: $C_{gs}, C_{gd}, C_L$):**
  $$\omega_H \approx \frac{1}{C_{gs}R_\text{sig}' + C_{gd}[R_\text{sig}'(1 + g_m R_L') + R_L'] + C_L R_L'}$$
  Notice the **Miller factor** $(1 + g_m R_L')$ baked into $R_{gd}$.
- **Resistance-seen-by formulas (CS):**
  $$R_{gs} = R_\text{sig}', \qquad R_{C_L} = R_L', \qquad R_{gd} = R_L' + g_m R_\text{sig}' R_L' + R_\text{sig}'$$
- 📝 **Recommend Practice:** **Example 10.5** (worked in review slides — $g_m = 2$ mA/V, $C_{gs} = 20$ fF, $C_{gd} = 5$ fF, $C_L = 25$ fF, $R_\text{sig} = 20$ kΩ, $R_L' = 10$ kΩ → $G_{V\max} = -20$ V/V (26 dB), $\tau_H = 2800$ ps, $f_H = 56.8$ MHz). **HW7 10.40, 10.46, 10.47**.

## Lecture 30 — HF Response of Common-Gate Amplifier (§10.5.1)

- **What's tested:** CG amp has **2 time constants** (one at the source via $C_{gs}$, one at the drain via $C_{gd} + C_L$). The drain pole usually dominates.
- **Time constants:**
  $$\tau_1 = C_{gs}\!\left[R_\text{sig} \,\Big\|\, \frac{r_o + R_L}{1 + g_m r_o}\right], \qquad \tau_2 = (C_{gd} + C_L)\!\left[R_L \| (r_o + R_\text{sig} + g_m r_o R_\text{sig})\right]$$
- **3-dB pole:** $\omega_H \approx 1/(\tau_1 + \tau_2)$, typically $\tau_2 \gg \tau_1$ so $\omega_H \approx 1/\tau_2$.
- **CG advantage at HF:** **no Miller multiplication** because the gate is grounded — much higher bandwidth than a CS amp at the same gain when $R_\text{sig}$ is large.
- 📝 **Recommend Practice:** **Example 10.6** (worked in review slides — same numbers as Example 10.5 but in CG: $G_{V\max} = 0.95$ V/V, $f_H = 263$ MHz — note **lower gain but ~5× more bandwidth** vs CS).

## Lecture 31 — HF Response of Source Follower (CD Amplifier) (§10.6.1)

- **What's tested:** The Source Follower has **1 zero + 2 poles**. The poles can be **real** (need to compare them) or **complex** (use $Q$ factor).
- **Mid-band gain (with body effect $\chi$ included via $g_{mb} = \chi g_m$):**
  $$R_L' = R_L \,\Big\|\, r_o \,\Big\|\, \frac{1}{g_{mb}}, \qquad G_{V\max} = \frac{g_m R_L'}{1 + g_m R_L'}$$
- **Transfer function:**
  $$\frac{V_o}{V_\text{sig}} = G_{V\max}\,\frac{1 + s/\omega_z}{1 + b_1 s + b_2 s^2}, \qquad f_z = \frac{g_m}{2\pi C_{gs}}$$
- **Two real poles, well-separated** (one ≥ 4× the other):
  $$\omega_H \approx \frac{1}{b_1}\quad(\text{OCTC value})$$
- **Two real poles, close together** (less than 4× apart):
  $$\omega_H \approx \frac{1}{\sqrt{1/\omega_{p1}^2 + 1/\omega_{p2}^2 - 2/\omega_z^2}}\quad(\text{square-root method})$$
- **Two complex-conjugate poles** ($Q > 0.5$):
  $$1 + b_1 s + b_2 s^2 = 1 + s/(Q\omega_0) + s^2/\omega_0^2$$
  - $Q = 0.707$ → maximally flat (Butterworth).
  - $Q > 0.707$ → **peaking** in magnitude response (problem!).
- 📝 **Recommend Practice:** **Example 10.8** (worked in review slides — answers: $G_{V\max} = 0.8$ V/V, $f_z = 15.9$ GHz, $Q = 0.42$ (real poles), $f_{p1} = 1.99$ GHz, $f_{p2} = 6.7$ GHz, $f_H = 1.9$ GHz, MOSFET $f_T = 12.7$ GHz). **HW Exercise 10.19**.

## Lecture CCA — The Cascode Amplifier (§8.5.1, 8.5.2)

- **What's tested:** Stack a CG (Q2) on top of a CS (Q1). Q2 acts as a current buffer, multiplying $r_{o1}$ by $g_{m2} r_{o2}$.
- **Output resistance:**
  $$\boxed{R_o \approx (g_{m2} r_{o2}) r_{o1}}$$
- **Intrinsic gain (ideal current source load):**
  $$A_{v0} = -g_{m1} R_o \approx -(g_{m1} r_{o1})(g_{m2} r_{o2}) \approx -(g_m r_o)^2$$
- **With PMOS cascode current source as load** (need both R_on and R_op big!):
  $$\boxed{A_v \approx -\tfrac{1}{2}(g_m r_o)^2 \quad\text{(all matched)}}$$
- **The trap:** loading a cascode with a single PMOS (not cascoded) gives $R_L = r_{o3}$, which is much smaller than $R_o = g_m r_o^2$. Then $A_v \approx -g_{m1} r_{o3}$ — **no better than a regular CS amp!** You must cascode the load too.
- 📝 **Recommend Practice:** Practice Final Problem #3 — design a **PMOS cascode current source** for given $I, R_o, |V_{OV}|$.

## Lecture CCA-HFR — HF Response of Cascode Amplifier (§10.4.2)

- **What's tested:** Cascode has **3 time constants**:
  $$\tau_1 = R_\text{sig}\bigl[C_{gs1} + C_{gd1}(1 + g_{m1} R_{d1})\bigr]$$
  $$\tau_2 = R_{d1}(C_{db1} + C_{gs2} + C_{gd1})$$
  $$\tau_3 = (R_o \| R_L)(C_{gd2} + C_L)$$
- **Where:** $A_{v1} = -g_{m1}(r_{o1} \| R_{\text{in}2})$ and $R_{\text{in}2} = (r_{o2} + R_L)/(1 + g_{m2} r_{o2})$ is the CG input resistance.
- **3-dB pole:** $\omega_H = 1/(\tau_1 + \tau_2 + \tau_3)$.

> [!warning] **Cascode vs CS — the BIG signature problem (Practice Final #2 verbatim).**
> | Scenario | CS gain | Cascode gain | CS BW | Cascode BW | Verdict |
> |---|---|---|---|---|---|
> | $R_\text{sig}$ big, $R_L$ big (∼$g_m r_o^2$) | $-g_m r_o$ | $-(g_m r_o)^2/2$ | similar | similar | **Cascode wins on gain** |
> | $R_\text{sig}$ big, $R_L \ll r_o$ | $-g_m R_L$ | $-g_m R_L$ | smaller (Miller) | **larger (no Miller)** | **Cascode wins on BW** |
>
> **Why the bandwidth differs:** in CS, $R_L' = R_L$ so $C_{gd}(1 + g_m R_L)$ is the Miller-multiplied capacitance. In Cascode, $R_{d1} \approx 1/g_m$ (because the CG above has $R_\text{in2} \approx 1/g_m$), so the Miller factor on $C_{gd1}$ becomes $(1 + g_m \cdot 1/g_m) = 2$ — **no big multiplication**. Hence cascode kills the Miller effect on $C_{gd1}$.

---

# Unit 6 — Multi-Transistor & Differential Amplifiers (Lectures 32–36)

> [!example] **Unit 6 in one breath.** Two matched transistors with their sources tied together to a tail current source $I$. Apply $v_{G1}, v_{G2}$, define $v_{id} = v_{G1} - v_{G2}$ (differential) and $V_{CM} = (v_{G1}+v_{G2})/2$ (common-mode). The differential gain is large, the common-mode gain is small (rejected by the tail source), and **CMRR = $|A_d|/|A_{cm}|$** is the figure of merit. The current-mirror-loaded variant is the canonical IC differential amp (Lectures 35–36).

## Lecture 32 — The MOS Differential Pair, Input Common-Mode Range (§9.1, 9.1.1)

- **What's tested:** Find the **range of $V_{CM}$** that keeps Q1 and Q2 in saturation.
- **Headline formulas:**
  $$\boxed{V_{CM,\max} = V_{DD} - \tfrac{I}{2}R_D + V_t}$$
  $$\boxed{V_{CM,\min} = -V_{SS} + V_{CS} + V_{OV} + V_t}$$
  where $V_{CS}$ is the minimum voltage required across the tail current source (typically the $V_{OV}$ of the bias transistor or the saturation requirement of the cascode mirror).
- **Saturation requirement:** $V_{DS} \geq V_{GS} - V_t$, i.e., $V_D \geq V_{CM} - V_t$.
- 📝 **Recommend Practice:** **Example 9.1**, **HW 9.1, 9.10, 9.16**.

## Lecture 33 — Diff Pair Drain Current & Small-Signal (§9.1.3, 9.1.4)

- **What's tested:** Large-signal current law:
  $$i_{D1} = \tfrac{I}{2} + \tfrac{I}{V_{OV}}\,\tfrac{v_{id}}{2}\sqrt{1 - \!\left(\tfrac{v_{id}/2}{V_{OV}}\right)^2}, \qquad i_{D2} = \tfrac{I}{2} - (\dots)$$
- **Linear range:** valid for $|v_{id}| \leq \sqrt{2}\,V_{OV}$. Outside this, one transistor cuts off and all $I$ flows through the other.
- **Small-signal approximation** ($v_{id} \ll 2V_{OV}$):
  $$i_{d1} = \frac{I}{V_{OV}}\,\frac{v_{id}}{2} = g_m\,\frac{v_{id}}{2}, \qquad g_m = \frac{I}{V_{OV}}$$
  - Note: $g_m$ here is computed at $I_{DQ} = I/2$, so $g_m = 2(I/2)/V_{OV} = I/V_{OV}$. Same value as before.
- **Three equivalent forms of $g_m$** (Diff Pair):
  $$g_m = \frac{I}{V_{OV}} = k_n'\frac{W}{L}V_{OV} = \sqrt{k_n'\frac{W}{L} I}$$
  (where $I$ here is the **tail current**, NOT the per-transistor current).

## Lecture 33 cont. — Differential Gain (§9.1.4)

- **What's tested:** When fed differential inputs $v_{G1} = +v_{id}/2, v_{G2} = -v_{id}/2$, the **source node is a virtual ground** (because $g_{m1} = g_{m2}$).
- **Differential output (taken between drains):**
  $$\boxed{A_d = \frac{v_{o2} - v_{o1}}{v_{id}} = g_m R_D \quad\text{(or } g_m(R_D \| r_o) \text{ if } r_o \text{ matters)}}$$
- **Single-ended output (taken at $v_{o2}$ alone):**
  $$\boxed{A_{d,\text{s.e.}} = \frac{v_{o2}}{v_{id}} = \frac{g_m R_D}{2}\quad\text{(half the differential gain)}}$$
- **With current-source loads instead of $R_D$** (PMOS independent sources):
  $$A_d = g_m(r_{o1} \| r_{o3})\quad(r_{o3} \gg R_D \text{ → much higher gain})$$
- 📝 **Recommend Practice:** **HW 9.10, 9.16, 9.55, 9.56**.

## Lecture 34 — Common-Mode Rejection Ratio (§9.3.1)

- **What's tested:** When $v_{G1} = v_{G2} = V_{icm}$ (common input), how much does the output respond? Should be small.
- **Differential output (matched):** $A_{cm} = 0$, so $\text{CMRR} = \infty$.
- **Differential output, with $R_D$ mismatch** $\Delta R_D$:
  $$A_{cm} \approx -\frac{\Delta R_D}{2 R_{SS}}$$
  $$\boxed{\text{CMRR}_\text{diff} = \frac{|A_d|}{|A_{cm}|} \approx \frac{2g_m R_{SS}}{\Delta R_D / R_D}}$$
  where $R_{SS}$ is the **output resistance of the tail current source** (bigger = better CMRR).
- **Single-ended output (always non-zero $A_{cm}$ even matched):**
  $$|A_{cm,\text{s.e.}}| \approx \frac{R_D}{2 R_{SS}}, \qquad \boxed{\text{CMRR}_{\text{s.e.}} = g_m R_{SS}}$$
- **In dB:** $\text{CMRR}(\text{dB}) = 20\log(|A_d|/|A_{cm}|)$.
- **Headline:** **differential output is far better** for CM noise rejection. To boost CMRR, **increase $R_{SS}$** (e.g., cascode the tail source).
- 📝 **Recommend Practice:** **In-class Example 9.11**, **HW 9.55, 9.56**.

> [!tip] **Practice Final #4(f) signature: "If it is required to increase the CMRR by 6 dB, by what factor should the channel length of $Q_5$ be changed?"** Since CMRR ∝ $R_{SS}$ ∝ $L$ (at fixed $W$, since $r_o = V_A L / I$ and $V_A \propto L$ in 0.18-µm processes), and **6 dB = factor of 2**, the answer is **double the channel length**.

## Lecture 35 — Diff Amp with Current-Mirror Load (§9.5.3, 9.5.5)

- **What's tested:** Replace the two PMOS independent loads with a **current mirror** (Q3 diode-connected, Q4 mirrors). This **doubles** the effective transconductance to single-ended output (current is added in phase, not subtracted).
- **Mid-band gain:**
  $$G_m = g_{m1} \quad(\text{matched})$$
  $$R_o = r_{o2} \| r_{o4}$$
  $$\boxed{A_d = G_m R_o = g_{m1}(r_{o2} \| r_{o4}) \approx \tfrac{1}{2}\,g_m r_o\quad(\text{all matched})}$$
- **Common-mode gain:**
  $$\boxed{A_{cm} \approx -\frac{1}{2 g_{m3} R_{SS}}}$$
- **CMRR:**
  $$\boxed{\text{CMRR} = \frac{|A_d|}{|A_{cm}|} \approx g_{m1}(r_{o2} \| r_{o4})\cdot 2 g_{m3} R_{SS} \approx g_m^2 r_o R_{SS}\quad(\text{matched})}$$
- 📝 **Recommend Practice:** **In-class Exercise 9.17**, **HW 9.85, 9.88**.

## Lecture 36 — HF Response of CM-Loaded Diff Amp (§10.6.2)

- **What's tested:** **2 poles + 1 zero**.
- **Frequency-dependent transconductance:**
  $$G_m(s) = g_m\,\frac{1 + s\dfrac{C_m}{2 g_{m3}}}{1 + s\dfrac{C_m}{g_{m3}}}$$
- **Total transfer function:**
  $$A_d(s) = G_m(s) \cdot Z_o(s) = g_m R_o \cdot \frac{1 + s C_m / (2g_{m3})}{1 + s C_m / g_{m3}} \cdot \frac{1}{1 + s R_o C_L}$$
- **Three frequencies (memorize):**
  $$\boxed{\omega_{p1} = \frac{1}{R_o C_L}\quad\text{(load pole)},\qquad \omega_{p2} = \frac{g_{m3}}{C_m}\quad\text{(mirror pole)},\qquad \omega_z = \frac{2 g_{m3}}{C_m}\quad\text{(mirror zero)}}$$
- **Pole-zero ordering:** $\omega_{p2} < \omega_z = 2\omega_{p2}$ (mirror zero is exactly **2×** the mirror pole).
- 📝 **Recommend Practice:** **In-class Example 10.9**, **HW 10.70, 10.76**.

> [!tip] **Bonus signature on Practice Final #4(g):** "Find the load pole, the mirror pole and the mirror zero with $C_\text{Load} = 47$ fF on the output node and $C_\text{mirror} = 57$ fF at the Q1 drain node." **Plug into the three boxed formulas above. That's the entire problem.**

---

# Master Cheat Sheet (build your formula sheet from this)

> [!example] **Recommend printing this section, hand-copying onto your formula sheet, then practicing once before exam day.**

### MOSFET basics

$$I_D^\text{sat} = \tfrac{1}{2} k_n'(W/L) V_{OV}^2 (1 + \lambda V_{DS}), \quad V_{OV} = V_{GS}-V_t, \quad r_o = V_A/I_D$$

$$g_m = k_n'(W/L) V_{OV} = \sqrt{2k_n'(W/L) I_D} = 2 I_D / V_{OV}$$

### Single-stage amplifier table (Table 7.4 — neglecting $r_o$)

| | $R_\text{in}$ | $A_{vo}$ | $R_o$ |
|---|---|---|---|
| **CS** | $\infty$ | $-g_m R_D$ | $R_D$ |
| **CS-w/$R_s$** | $\infty$ | $-g_m R_D / (1+g_m R_s)$ | $R_D$ |
| **CG** | $1/g_m$ | $g_m R_D$ | $R_D$ |
| **SF** | $\infty$ | $1$ | $1/g_m$ |

Bookkeeping: $A_v = A_{vo}\,R_L/(R_L+R_o)$, $G_v = R_\text{in}/(R_\text{in}+R_\text{sig}) \cdot A_v$.

### Current mirror & basic gain cell

$$I_O = I_\text{REF}\,(W/L)_2/(W/L)_1, \qquad I_\text{REF} = (V_{DD} - V_{GS})/R$$

$$A_{vo,\text{intrinsic}} = -g_m r_o = -2 V_A / V_{OV}$$

### Cascode amplifier

$$R_o \approx (g_{m2} r_{o2}) r_{o1}, \qquad A_{v0} \approx -(g_m r_o)^2 \;\text{(ideal load)}, \qquad A_v \approx -\tfrac{1}{2}(g_m r_o)^2 \;\text{(cascode load)}$$

### Diff pair

$$g_m = I/V_{OV}, \qquad |v_{id}|_\max = \sqrt{2} V_{OV}$$

$$A_d = g_m R_D \;\text{(diff out)}, \qquad A_{d,\text{s.e.}} = g_m R_D / 2 \;\text{(s.e.)}$$

### CM-loaded diff amp

$$A_d = g_m(r_{o2} \| r_{o4}) \approx \tfrac{1}{2} g_m r_o, \qquad A_{cm} \approx -1/(2 g_{m3} R_{SS}), \qquad \text{CMRR} \approx g_m^2 r_o R_{SS}$$

### Common-mode range

$$V_{CM,\max} = V_{DD} - \tfrac{I}{2}R_D + V_t, \qquad V_{CM,\min} = -V_{SS} + V_{CS} + V_{OV} + V_t$$

### CMRR

$$\text{CMRR}_\text{diff,mismatch} = 2 g_m R_{SS} / (\Delta R_D / R_D), \qquad \text{CMRR}_\text{s.e.} = g_m R_{SS}$$

$$\text{CMRR (dB)} = 20\log(\text{CMRR})$$

### High-frequency MOSFET model (Table 10.1)

$$C_{gs} = \tfrac{2}{3}WLC_{ox} + WL_{ov}C_{ox}, \qquad C_{gd} = WL_{ov}C_{ox}, \qquad f_T = g_m / [2\pi(C_{gs}+C_{gd})]$$

### CS HF response (1st analysis with Miller)

$$A_M = -g_m R_L', \qquad C_\text{in} = C_{gs} + C_{gd}(1 + g_m R_L')$$

$$\omega_H = \frac{1}{R_\text{sig}'\,C_\text{in}}, \qquad f_H = \frac{1}{2\pi R_\text{sig}' [C_{gs} + C_{gd}(1 + g_m R_L')]}$$

### CS HF response (low $R_\text{sig}$, output-pole limited)

$$f_H = \frac{1}{2\pi (C_L + C_{gd}) R_L'}, \qquad f_Z = \frac{g_m}{2\pi C_{gd}}, \qquad f_t = |A_M| f_H$$

### OCTC method (CS — 3 caps)

$$R_{gs} = R_\text{sig}', \qquad R_{gd} = R_\text{sig}'(1 + g_m R_L') + R_L', \qquad R_{C_L} = R_L'$$

$$\omega_H \approx \frac{1}{C_{gs}R_{gs} + C_{gd}R_{gd} + C_L R_{C_L}}$$

### Square-root method (multi-pole/zero)

$$\omega_H \approx 1/\sqrt{\sum 1/\omega_{pi}^2 - 2\sum 1/\omega_{zi}^2}$$

### Source follower (1 zero + 2 poles)

$$f_z = g_m/(2\pi C_{gs}); \quad \text{2 real well-separated poles: } \omega_H \approx 1/b_1; \quad \text{else SQRT method or complex with } Q$$

### Miller's theorem

$$Z_1 = Z/(1-K), \qquad Z_2 = Z/(1 - 1/K)$$

### CM-loaded diff amp HF (2 poles + 1 zero)

$$\omega_{p1} = 1/(R_o C_L), \qquad \omega_{p2} = g_{m3}/C_m, \qquad \omega_z = 2 g_{m3}/C_m$$

### STC networks (Table 1.2)

| | $T(s)$ | $\omega_0$ |
|---|---|---|
| **LP-STC** | $K/(1+s/\omega_0)$ | $1/RC$ |
| **HP-STC** | $Ks/(s+\omega_0)$ | $1/RC$ |

---

# T/F + MC quick-fire (drill these — easy points)

**Truth table** (from the Practice Final and from the lecture material):

| Statement | T/F | Why |
|---|---|---|
| In a differential amp, **CMRR is desired to be high** | **T** | High CMRR = good rejection of common noise. |
| A cascode amplifier has **high gain as long as $R_L$ is low** | **F** | Need $R_L \sim g_m r_o^2$ (i.e., **high** $R_L$, often a cascode current source). Low $R_L$ kills the gain advantage. |
| A common-gate amp **makes a good current buffer** | **T** | $A_{io} = 1$ A/A; high $R_o$, low $R_\text{in}$ — the textbook current buffer. |
| The Miller Effect **causes $C_{gd}$ to be reduced** when reflected to the input | **F** | Miller **increases** $C_{gd}$ at the input by factor $(1 + g_m R_L')$ — that's the whole problem. |
| Common-mode gain of a diff amp **increases with an ideal current source** | **F** | An ideal tail current source has $R_{SS} = \infty$, making $A_{cm} = 0$. CM gain **decreases** (improves). |
| **$R_\text{in}$ of CS is less than $R_\text{in}$ of CG** | **F** | $R_\text{in,CS} = \infty$, $R_\text{in,CG} = 1/g_m$. CS is **bigger**. |
| In analog amplifiers, MOSFETs **should operate in saturation** | **T** | Saturation gives constant $g_m$; triode adds nonlinearity / signal-dependent gain. |

**Multiple choice:**

| Question | Answer | Explanation |
|---|---|---|
| How many poles and zeros does a CM-loaded diff amp have? | **(c) 2 poles, 1 zero** | Lecture 36: load pole + mirror pole + mirror zero. |
| If $R_\text{sig}$ is small, the 3-dB pole of CS comes from… | **(c) $C_{gd}$ reflected to output** + **(d) $C_L$ on the output** | Lecture 27: output pole limited by $(C_L + C_{gd}) R_L'$ once $R_\text{sig} \approx 0$. |

**Short answer:**

| Question | Answer |
|---|---|
| Common drain (SF) can have what type of poles? | **Complex-conjugate poles** (with peaking if $Q > 0.707$) — the only one of CS/CG/SF that does this. |
| Name 3 methods for estimating $f_H$ of a CS amp | (1) **First analysis** with Miller-multiplied $C_\text{in}$ as a simple LP-STC, (2) **OCTC method** summing $\tau_k = C_k R_k$, (3) **Square-root method** $\omega_H \approx 1/\sqrt{\sum 1/\omega_p^2 - 2 \sum 1/\omega_z^2}$. (Could also count: dominant-pole approx; full transfer-function analysis.) |

---

# Practice Final problem-type breakdown (Spring 2025)

| Problem | Pts | What it tests | Lecture(s) |
|---|---|---|---|
| **#1** | 15 | CS amp HF analysis using OCTC: find $G_v$, $f_H$, $f_t$ given $g_m, r_o, R_\text{sig}, R_L, C_{gs}, C_{gd}, C_{db}, C_L$. | 25, 27, 29 |
| **#2** | 18 | Cascode the same amp from #1; recompute $G_v$, $f_H$, $f_t$; report **factor by which $f_t$ improves**. | CCA, CCA-HFR |
| **#3** | 15 | Design a **PMOS cascode current source** for given $I, R_o, |V_{OV}|$: find $V_{G1}, V_{G2}$, max output, $W/L$. | 20, CCA |
| **#4** | 28 | Full **CM-loaded MOS diff amp** analysis: DC bias, $V_{OV}$, $V_S$ at sources of Q1/Q2, $V_G$ at gates of Q3/Q4, $g_m$, $r_o$, **$A_d$**, **$R_{SS}$**, **$A_{cm}$**, **CMRR (dB)**, channel-length factor for +6 dB CMRR. **Bonus: poles + zero** with given $C_L, C_m$. | 32, 33, 34, 35, 36 |
| **#5** | 24 | T/F (7 × 2 pts) + MC (3-5 pts each) + short answer (3 pts each). | All units |
| **Bonus** | 5 | 2-stage amp mid-band differential gain (s.e. output). | 35 + cascade |

**Time budget (110 min, 110 pts):** 1 minute per point + 5 minutes reading the exam = 105 min budgeted, 5 min slack. **Don't get stuck on a single subpart of #4** (worth 3 pts — bail and come back).

---

# Topics that historically appear EVERY EXAM (do these last if short on time)

1. ⭐ **Compute $g_m, r_o$ from DC bias** (every problem starts with this).
2. ⭐ **CS amp HF response with OCTC** (Practice #1).
3. ⭐ **Cascode HF advantage explanation** (Practice #2 + T/F #2).
4. ⭐ **CM-loaded diff amp full pipeline:** $A_d$ → $A_{cm}$ → CMRR → CMRR(dB) (Practice #4).
5. ⭐ **CMRR vs $R_{SS}$ scaling** (Practice #4(f) — channel length factor).
6. **Diff amp DC bias** (Practice #4(a)(b) — current divides equally, $V_S = V_{CM} - V_{GS}$).
7. **Cascode current source design** (Practice #3 — 3 unknowns: $V_{G1}, V_{G2}, W/L$).
8. **Source follower 2-pole/1-zero analysis** (less common but lurking).
9. **Source follower with body effect ($g_{mb} = \chi g_m$).**
10. **Miller's theorem** quick reflection.

---

# Related

- [[eee-335]] — course page (full Unit 4–6 roadmap with concept-page links)
- [[eee-335-final-walkthrough]] — earlier Units 1–6 walkthrough with worked problems and collapsible derivation drop-downs
- **Review slides (115 pp, McDonald Spring 2026)** — [Units 4-6 Review S26 slides](../../raw/slides/eee-335/lecture-review-units-4-6-final-spring-2026-slides.pdf)
- **Practice final** — [Practice Final Exam Spring 25](../../raw/slides/eee-335/practice-final-exam-spring-25.pdf) · [Solutions](../../raw/slides/eee-335/practice-final-exam-spring-25-solutions.pdf)

### Lecture slides (Units 4–6)

- Lecture 17 — [Transistor Amplifier Basic Principles](../../raw/slides/eee-335/lecture-17-transistor-amplifier-basic-principles-slides.pdf)
- Lecture 18 — [Small-Signal Model](../../raw/slides/eee-335/lecture-18-small-signal-model-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-18-small-signal-model-problems.pdf) · [Solutions](../../raw/slides/eee-335/lecture-18-small-signal-model-solutions.pdf)
- Lecture 19 — [Basic Configurations](../../raw/slides/eee-335/lecture-19-basic-configurations-slides.pdf)
- Lecture 20 — [IC Biasing](../../raw/slides/eee-335/lecture-20-ic-biasing-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-20-ic-biasing-problems.pdf)
- Lecture 21 — [The Basic Gain Cell](../../raw/slides/eee-335/lecture-21-the-basic-gain-cell-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-21-the-basic-gain-cell-problems.pdf)
- Lecture 22 — [Buffers: CG and Source Follower](../../raw/slides/eee-335/lecture-22-buffers-common-gate-and-source-follower-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-22-buffers-common-gate-and-source-follower-problems.pdf)
- Lecture 23 — [Frequency Response of Amplifiers](../../raw/slides/eee-335/lecture-23-frequency-response-of-amplifiers-slides.pdf)
- Lecture 24 — [High-Frequency MOSFET Model](../../raw/slides/eee-335/lecture-24-high-frequency-mosfet-model-slides.pdf) · [Solutions](../../raw/slides/eee-335/lecture-24-high-frequency-mosfet-model-solutions.pdf)
- Lecture 25 — [HF Response of CS Amplifier](../../raw/slides/eee-335/lecture-25-high-frequency-response-of-cs-amplifier-slides.pdf)
- Lecture 26 — [Miller's Theorem](../../raw/slides/eee-335/lecture-26-miller-s-theorem-slides.pdf) · [Solutions](../../raw/slides/eee-335/lecture-26-miller-s-theorem-solutions.pdf)
- Lecture 27 — [Frequency Response of CS with Low Rsig](../../raw/slides/eee-335/lecture-27-frequency-response-of-cs-with-low-rsig-slides.pdf)
- Lecture 28 — [Tools for HF Response Analysis](../../raw/slides/eee-335/lecture-28-tools-for-high-frequency-response-analysis-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-28-tools-for-high-frequency-response-analysis-problems.pdf)
- Lecture 29 — [Method of Open-Circuit Time Constants (OCTC)](../../raw/slides/eee-335/lecture-29-method-of-open-circuit-time-constants-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-29-method-of-open-circuit-time-constants-problems.pdf)
- Lecture 30 — [HF Response of CG Amplifier](../../raw/slides/eee-335/lecture-30-high-frequency-response-of-cg-amplifier-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-30-high-frequency-response-of-cg-amplifier-problems.pdf)
- Lecture 31 — [HF Response of Source Follower (CD)](../../raw/slides/eee-335/lecture-31-high-frequency-response-of-source-follower-cd-amplifier-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-31-high-frequency-response-of-source-follower-cd-amplifier-problems.pdf)
- Lecture 32 — [The MOS Differential Pair (1)](../../raw/slides/eee-335/lecture-32-the-mos-differential-pair-1-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-32-the-mos-differential-pair-1-problems.pdf) · [Solutions](../../raw/slides/eee-335/lecture-32-the-mos-differential-pair-1-solutions.pdf)
- Lecture 33 — [The MOS Differential Pair (2)](../../raw/slides/eee-335/lecture-33-the-mos-differential-pair-2-slides.pdf)
- Lecture 34 — [Common-Mode Rejection in Diff Amp](../../raw/slides/eee-335/lecture-34-common-mode-rejection-in-differential-amplifier-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-34-common-mode-rejection-in-differential-amplifier-problems.pdf)
- Lecture 35 — [Diff Amp with Current-Mirror Load](../../raw/slides/eee-335/lecture-35-differential-amplifier-with-current-mirror-load-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-35-differential-amplifier-with-current-mirror-load-problems.pdf)
- Lecture 36 — [Frequency Response of CM-Loaded Diff Amp](../../raw/slides/eee-335/lecture-36-frequency-response-of-differential-amplifier-with-current-mirror-load-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-36-frequency-response-of-differential-amplifier-with-current-mirror-load-problems.pdf)
- Lecture CCA — [Cascode Amplifier](../../raw/slides/eee-335/lecture-cca-cascode-amplifier-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-cca-cascode-amplifier-problems.pdf)
- Lecture CCA-HFR — [HF Response of Cascode Amplifier](../../raw/slides/eee-335/lecture-cca-hf-hf-response-cascode-amplifier-slides.pdf) · [Problems](../../raw/slides/eee-335/lecture-cca-hf-hf-response-cascode-amplifier-problems.pdf)

### Concept pages

[[mosfet-small-signal-model]] · [[common-source-amplifier]] · [[common-gate-amplifier]] · [[source-follower]] · [[current-mirror]] · [[mosfet-high-frequency-model]] · [[millers-theorem]] · [[octc-method]] · [[cs-amplifier-frequency-response]] · [[cascode-amplifier]] · [[differential-pair]] · [[cmrr]]
