---
title: "EEE 335 — Final Exam Practice Set 01"
type: practice
course: "[[eee-335]]"
tags:
  - practice
  - finals
  - mosfet-amplifier
  - frequency-response
  - differential-pair
  - cascode
  - current-mirror
  - octc
  - miller
  - cmrr
  - small-signal
  - q-point
concept:
  - "[[mosfet-small-signal-model]]"
  - "[[common-source-amplifier]]"
  - "[[common-gate-amplifier]]"
  - "[[source-follower]]"
  - "[[current-mirror]]"
  - "[[cascode-amplifier]]"
  - "[[differential-pair]]"
  - "[[cmrr]]"
  - "[[millers-theorem]]"
  - "[[octc-method]]"
  - "[[mosfet-high-frequency-model]]"
  - "[[cs-amplifier-frequency-response]]"
difficulty: mixed
created: 2026-05-04
---

# EEE 335 — Final Exam Practice Set 01

> [!warning] **Final exam: Tuesday 2026-05-05, 12:10–2:00 PM, SCOB 250, 110 minutes, ~110 pts.** Allowed: scientific calculator + **one 8.5×11" double-sided** (or two single-sided) handwritten formula sheet. NOT allowed: textbook, notes beyond the formula sheet, tablets, phones, classmates.
>
> **Coverage:** Units 4–6 only — Lectures 17–36 + CCA + CCA-HFR. Sedra/Smith Ch. 7, 8, 9, 10.

> [!example] **How to use this set.**
> Attempt every problem **freehand on paper without scrolling**. Time yourself: total budget = 110 minutes (about 1 minute per point). Each problem labels its difficulty and the **3–5 building blocks** it tests so you can pattern-match the solution before deriving. After each attempt, expand the solution and check. Log mistakes in **Jayden's attempts** at the bottom.
>
> Style anchored on:
> - [Spring 2025 practice final](../../raw/slides/eee-335/practice-final-exam-spring-25.pdf) + [solutions](../../raw/slides/eee-335/practice-final-exam-spring-25-solutions.pdf) — the canonical problem-type bank McDonald draws from.
> - [Units 4–6 review deck](../../raw/slides/eee-335/lecture-review-units-4-6-final-spring-2026-slides.pdf) — McDonald's 115-slide pre-final review.
> - [[eee-335-final-lecture-review]] — the lecture-by-lecture map and master cheat sheet (the 5 framework patterns).
> - [[eee-335-l36-cm-cl-set-01]] — companion practice set for the L36 CM-loaded diff amp HF response (same difficulty calibration as Problem 8 below).

> [!tip] **The 5 framework patterns** (from [[eee-335-final-lecture-review]] — repeated here so you don't need to flip).
> 1. **Half-circuit analysis** — diff input → tail virtual ground → CS half-circuit. CM input → tail moves → CS-with-$R_s$ half-circuit using $R_s = 2 R_{SS}$.
> 2. **Three building-block gains** — CS ($-g_m R_\text{out}$), CS-with-$R_s$ ($-R_\text{out}/(1/g_m + R_s)$), diode-connected ($1/g_m$ looking in).
> 3. **$R_\text{out}$ at any node** — drain alone: $r_o$. Drain with source resistor: $r_o(1 + g_m R_s)$. Source (gate grounded): $1/g_m$. Cascode total: $g_m r_o^2$.
> 4. **Four definitions** — $A_d = v_o/v_{id}$, $A_{cm} = v_o/v_{icm}$, $\text{CMRR} = |A_d/A_{cm}|$, $A_d^\text{s.e.} = \tfrac{1}{2} A_d^\text{diff}$ (matched).
> 5. **"What changes if…" reflex** — ideal tail ⇒ $A_{cm}\to 0$. Cascode load ⇒ $R_o \to g_m r_o^2$, gain $\to (g_m r_o)^2$. Diff out ⇒ $A_d$ doubles, $A_{cm}\to 0$ (matched).

---

## Problems

### 1. **Q-point + small-signal extraction** (Easy, 8 pts) — Lectures 17, 18

A common-source amplifier uses an NMOS with $k_n' = 0.4 \text{ mA/V}^2$, $W/L = 25$, $V_{tn} = 0.5$ V, $V_A = 20$ V. The DC bias gives $I_D = 0.5$ mA. The drain resistor is $R_D = 20$ k$\Omega$ tied to $V_{DD} = 1.8$ V. The signal source has $R_\text{sig} = 0$ (ideal voltage source); the load is $R_L = \infty$ (open).

> [!example] **Concept this problem tests.** Pattern 2 (CS gain) + the basic small-signal parameter extraction.
>
> **Building blocks:** $g_m = \sqrt{2 k_n' (W/L) I_D}$ ; $r_o = V_A / I_D$ ; CS open-circuit gain $A_{vo} = -g_m R_\text{out}$.

(a) Find $V_{OV}$ at the Q-point.
(b) Find $g_m$ and $r_o$.
(c) Confirm the transistor is in saturation if $V_{DS} = 0.8$ V.
(d) Find the open-circuit voltage gain $A_{vo}$ when $r_o$ is **neglected**.
(e) Find $A_{vo}$ with $r_o$ included.

<details><summary>Solution</summary>

**(a) $V_{OV}$:** From $I_D = \tfrac{1}{2} k_n' (W/L) V_{OV}^2$ → $V_{OV} = \sqrt{2 I_D / [k_n' (W/L)]} = \sqrt{2 \cdot 0.5 / (0.4 \cdot 25)} = \sqrt{0.1} = \mathbf{0.316\text{ V}}$.

**(b) $g_m$ and $r_o$:**
$$g_m = \sqrt{2 k_n' (W/L) I_D} = \sqrt{2 \cdot 0.4 \cdot 25 \cdot 0.5} = \sqrt{10} = \mathbf{3.16\text{ mA/V}}$$
$$r_o = V_A / I_D = 20 / 0.5 = \mathbf{40\text{ k}\Omega}$$

Sanity check via the second formula: $g_m = 2 I_D / V_{OV} = 2(0.5) / 0.316 = 3.16$ mA/V. ✓

**(c) Saturation check:** Need $V_{DS} \geq V_{OV}$. $0.8 \geq 0.316$ ✓ — **in saturation.**

**(d) $A_{vo}$ neglecting $r_o$:** From Table 7.4, $A_{vo} = -g_m R_D = -3.16 \cdot 20 = \mathbf{-63.2\text{ V/V}}$.

**(e) $A_{vo}$ with $r_o$:** $R_\text{out} = R_D \| r_o = 20 \| 40 = (20 \cdot 40)/(20+40) = 800/60 = 13.33$ k$\Omega$. So $A_{vo} = -g_m (R_D \| r_o) = -3.16 \cdot 13.33 = \mathbf{-42.1\text{ V/V}}$.

**Answer:** Including $r_o$ drops the gain by ~33%. **Always check whether the problem says "neglect $r_o$" or not** — the gap is 20 V/V here.

> [!tip] **What to memorize vs. derive.**
> **Memorize:** $g_m = \sqrt{2 k_n' (W/L) I_D} = 2 I_D / V_{OV}$ ; $r_o = V_A / I_D$ ; $A_{vo,\text{CS}} = -g_m R_\text{out}$.
> **Derive at the moment:** $V_{OV}$ from $I_D$ ; $R_\text{out} = R_D \| r_o$ vs. $R_D$ alone (depends on whether $r_o$ matters).

</details>

**Same framework as:** Spring 2025 practice final P1(a) ; [[eee-335-final-walkthrough]] §Unit 4 ; [[mosfet-small-signal-model]] ; [[common-source-amplifier]].

---

### 2. **Configuration choice + $G_v$ end-to-end** (Easy–Medium, 10 pts) — Lecture 19

You need to drive a $R_L = 1$ k$\Omega$ load from a source with $R_\text{sig} = 100$ k$\Omega$, using a single NMOS biased so that $g_m = 5$ mA/V and $r_o = 50$ k$\Omega$. Available: a DC supply and any biasing resistors needed; one transistor; configurations CS, CG, or SF.

> [!example] **Concept this problem tests.** Pattern 2 + Pattern 5 ("what changes if…"). Match the configuration's $R_\text{in}, R_o$ profile to the source/load.
>
> **Building blocks:** Table 7.4 (CS, CG, SF input/output resistances and gains).

(a) For each of CS, CG, SF, compute $G_v = v_o / v_\text{sig}$ (use $r_o$).
(b) Which configuration is best for this driver scenario? Justify in one sentence.

<details><summary>Solution</summary>

**Set up.** $G_v = \dfrac{R_\text{in}}{R_\text{in} + R_\text{sig}} \cdot A_{vo} \cdot \dfrac{R_L}{R_L + R_o}$.

**(a) Compute each:**

**CS:** $R_\text{in} = \infty$ → input divider = 1. $A_{vo} = -g_m(R_D \| r_o)$. With no $R_D$ given, assume $R_D \to \infty$ so $R_o = r_o = 50$ k$\Omega$ and $A_{vo} = -g_m r_o = -5 \cdot 50 = -250$ V/V. Output divider: $R_L / (R_L + R_o) = 1/(1+50) = 0.0196$. **$G_v = 1 \cdot (-250) \cdot 0.0196 = \mathbf{-4.9\text{ V/V}}$.**

**CG:** $R_\text{in} = 1/g_m = 0.2$ k$\Omega$ → input divider = $0.2/(0.2 + 100) = 0.002$. $A_{vo} = +g_m r_o = +250$ V/V. Output divider: $1/(1+50) = 0.0196$. **$G_v = 0.002 \cdot 250 \cdot 0.0196 = \mathbf{+0.0098\text{ V/V}}$ (negligible).**

**SF:** $R_\text{in} = \infty$ → input divider = 1. $A_{vo} \approx 1$. $R_o = 1/g_m = 0.2$ k$\Omega$. Output divider: $1/(1+0.2) = 0.833$. **$G_v = 1 \cdot 1 \cdot 0.833 = \mathbf{+0.833\text{ V/V}}$.**

**(b) Best choice: CS.** It has the highest $|G_v|$ (≈5 V/V) — the only one that provides voltage gain in this scenario. Both CS and SF benefit from infinite $R_\text{in}$ to absorb the 100 k$\Omega$ source; only CS provides voltage amplification. SF would be the right answer if the goal were *unity-gain buffering* (e.g., feeding a smaller load impedance after a gain stage), but here the load is small (1 k$\Omega$) and the CS amp's high $R_o$ kills the output divider — so CS still wins on $|G_v|$ but the output transfer is poor. **A two-stage CS+SF cascade would beat single-CS** by giving full $|A_{vo}| = 250$ on the first stage, then SF buffering the 1 k$\Omega$ load.

> [!tip] **What to memorize vs. derive.**
> **Memorize:** the matchups — **CS for voltage gain**, **CG for current buffering** ($R_\text{in}$ low, $R_o$ high), **SF for low-impedance load driving** ($R_o = 1/g_m$).
> **Derive:** the $G_v$ end-to-end with both dividers — easy to forget the input divider when $R_\text{in}$ is finite (CG case).

</details>

**Same framework as:** Lecture 19 problems ; [[common-source-amplifier]] ; [[common-gate-amplifier]] ; [[source-follower]].

---

### 3. **Current-mirror biasing + saturation check** (Easy, 8 pts) — Lecture 20

A simple NMOS current mirror has $Q_1$ diode-connected with $(W/L)_1 = 10$, and $Q_2$ outputs to a load with $(W/L)_2 = 30$. Both transistors have $k_n' = 0.4$ mA/V², $V_{tn} = 0.5$ V, $V_A = 25$ V. The reference current is set by $R = 100$ k$\Omega$ from $V_{DD} = 1.8$ V to the gate-drain of $Q_1$.

> [!example] **Concept this problem tests.** Pattern 2 (mirror as biasing block) + Pattern 3 (saturation requirement).
>
> **Building blocks:** $I_\text{REF} = (V_{DD} - V_{GS}) / R$ ; $I_O = I_\text{REF} \cdot (W/L)_2 / (W/L)_1$ ; $V_{O,\min} = V_{OV}$ ; $R_o = r_o$.

(a) Find $I_\text{REF}$.
(b) Find $I_O$ (ignore channel-length modulation for this part).
(c) What is the **minimum allowed $V_O$** at the drain of $Q_2$ to keep it in saturation?
(d) Find the output resistance $R_o$ of $Q_2$ at the operating point.

<details><summary>Solution</summary>

**(a) $I_\text{REF}$:** Self-consistent — need $V_{GS}$ at $Q_1$ first. From $I_\text{REF} = \tfrac{1}{2} k_n' (W/L)_1 V_{OV}^2$ and $V_{GS} = V_{OV} + V_{tn}$:

Try $V_{OV} = 0.5$ V → $I_\text{REF} = \tfrac{1}{2}(0.4)(10)(0.25) = 0.5$ mA → $V_{GS} = 1$ V → $I_\text{REF} = (1.8 - 1)/100 = 0.008$ mA. Inconsistent.

Iterate. Set $I_\text{REF} = (1.8 - V_{GS})/R = (1.8 - V_{tn} - V_{OV})/R$ and $I_\text{REF} = \tfrac{1}{2} k_n'(W/L)_1 V_{OV}^2$:
$$\tfrac{1}{2}(0.4)(10)V_{OV}^2 = (1.3 - V_{OV})/100$$
$$2 V_{OV}^2 = (1.3 - V_{OV})/100 \to 200 V_{OV}^2 + V_{OV} - 1.3 = 0$$

Quadratic: $V_{OV} = [-1 + \sqrt{1 + 4(200)(1.3)}] / (2 \cdot 200) = [-1 + \sqrt{1041}] / 400 = (-1 + 32.26)/400 = \mathbf{0.0782\text{ V}}$.

Then $I_\text{REF} = \tfrac{1}{2}(0.4)(10)(0.0782)^2 = 2 \cdot 0.00611 = \mathbf{0.0122\text{ mA} \approx 12.2\,\mu\text{A}}$.

(Sanity: $V_{GS} = 0.5 + 0.0782 = 0.578$ V → $I_\text{REF} = (1.8 - 0.578)/100 = 0.01222$ mA ✓.)

**(b) $I_O$:** $I_O = I_\text{REF} \cdot (W/L)_2 / (W/L)_1 = 12.2 \cdot (30/10) = \mathbf{36.6\,\mu\text{A}}$.

**(c) Minimum $V_O$:** $Q_2$ stays in saturation as long as $V_{DS2} \geq V_{OV2}$. Since $Q_2$ has the same $V_{OV}$ as $Q_1$ (both have $V_{GS} = 0.578$ V because gates are connected and sources are both at ground), $V_{O,\min} = V_{OV} = \mathbf{0.078\text{ V}}$.

**(d) $R_o$ at $Q_2$:** $r_{o2} = V_A / I_O = 25 / 0.0366 = \mathbf{683\text{ k}\Omega}$.

> [!warning] **The trap.** Naive students plug $V_{OV} = 0.5$ V or some other guess into the formula without realizing the mirror's $V_{GS}$ is set by $V_{DD}, R$, and $(W/L)_1$ self-consistently. **Either iterate or solve the quadratic.** McDonald's 2025 exam used $V_{DD} = 1.8$ V and $V_{tn} = 0.5$ V — the $V_{OV}$ ends up small (~50–100 mV) because $R$ is big.

> [!tip] **What to memorize vs. derive.**
> **Memorize:** $I_O = I_\text{REF} \cdot (W/L)_2/(W/L)_1$, mirror saturation requires $V_O \geq V_{OV}$, $r_o = V_A/I_D$.
> **Derive:** $V_{OV}$ self-consistently (iterate or quadratic).

</details>

**Same framework as:** Lecture 20 problems ; HW5 problem 8.2/8.3/8.6 ; [[current-mirror]].

---

### 4. **Basic gain cell + output swing** (Medium, 12 pts) — Lecture 21 (Example 8.3 signature)

An NMOS basic gain cell has $V_{DD} = 1.8$ V, $V_{tn} = 0.4$ V, $|V_{tp}| = 0.4$ V, $k_n' = 0.4$ mA/V², $|k_p'| = 0.1$ mA/V², $V_{An} = 12.5$ V, $|V_{Ap}| = 9$ V. The bias is set by a PMOS current source so that $I_D = 100\,\mu$A and $|V_{OV}| = 0.2$ V for **both** the NMOS and PMOS. (The reference current $I_\text{REF}$ is generated elsewhere.)

> [!example] **Concept this problem tests.** Pattern 2 (intrinsic gain) + Pattern 3 ($R_\text{out}$ from two transistors in parallel) + the saturation-determined output-swing range.
>
> **Building blocks:** $A_{v0} = -g_m (r_{o1} \| r_{o2})$ ; $V_{O,\max} = V_{DD} - |V_{OV,p}|$ ; $V_{O,\min} = V_{OV,n}$ ; $W/L$ from $I_D = \tfrac{1}{2} k' (W/L) V_{OV}^2$.

(a) Find $V_{GS,n}$ and the DC component of $v_I$ that biases the cell.
(b) Find $(W/L)_n$ and $(W/L)_p$.
(c) Find $g_{m,n}$, $r_{o,n}$, $r_{o,p}$.
(d) Find the small-signal voltage gain $A_v$.
(e) Find the allowable range of $v_O$ at the output (the swing limits set by saturation).

<details><summary>Solution</summary>

**(a) $V_{GS,n}$ and $V_I$:** $V_{GS,n} = V_{tn} + V_{OV,n} = 0.4 + 0.2 = \mathbf{0.6\text{ V}}$. The DC input voltage at the gate is $V_I = V_{GS,n} = \mathbf{0.6\text{ V}}$ (assuming the source is at ground).

**(b) Aspect ratios:** From $I_D = \tfrac{1}{2} k' (W/L) V_{OV}^2$:
$$(W/L)_n = \frac{2 I_D}{k_n' V_{OV,n}^2} = \frac{2(0.1)}{0.4 \cdot 0.04} = \frac{0.2}{0.016} = \mathbf{12.5}$$
$$(W/L)_p = \frac{2 I_D}{|k_p'| V_{OV,p}^2} = \frac{2(0.1)}{0.1 \cdot 0.04} = \frac{0.2}{0.004} = \mathbf{50}$$

(PMOS needs $4\times$ wider because $|k_p'|$ is $4\times$ smaller than $k_n'$.)

**(c) Small-signal parameters:**
$$g_{m,n} = 2 I_D / V_{OV,n} = 2(0.1) / 0.2 = \mathbf{1\text{ mA/V}}$$
$$r_{o,n} = V_{An} / I_D = 12.5 / 0.1 = \mathbf{125\text{ k}\Omega}$$
$$r_{o,p} = |V_{Ap}| / I_D = 9 / 0.1 = \mathbf{90\text{ k}\Omega}$$

**(d) Voltage gain:**
$$R_\text{out} = r_{o,n} \| r_{o,p} = (125 \cdot 90)/(125 + 90) = 11250 / 215 = 52.3\text{ k}\Omega$$
$$\boxed{A_v = -g_{m,n} \cdot (r_{o,n} \| r_{o,p}) = -1 \cdot 52.3 = \mathbf{-52.3\text{ V/V}}}$$

**(e) Output swing range:**

**Upper limit** (PMOS stays in saturation): $V_O \leq V_{DD} - |V_{OV,p}| = 1.8 - 0.2 = \mathbf{1.6\text{ V}}$.

**Lower limit** (NMOS stays in saturation, $V_{DS,n} \geq V_{OV,n}$): $V_O \geq V_{OV,n} = \mathbf{0.2\text{ V}}$.

**Answer: $0.2 \leq v_O \leq 1.6$ V** → swing range = **1.4 V peak-to-peak**, centered at 0.9 V.

> [!tip] **What to memorize vs. derive.**
> **Memorize:** intrinsic-gain skeleton $A_{v0} = -g_m r_o$ ; with active load $A_v = -g_m (r_{on} \| r_{op})$. **Memorize the swing-range bounds** $V_{O,\max} = V_{DD} - |V_{OV,p}|$ and $V_{O,\min} = V_{OV,n}$ — they're trivial to derive but trivial to forget on exam day.
> **Derive:** $W/L$ from $I_D$ and $V_{OV}$ ; the parallel combination of $r_o$'s.

</details>

**Same framework as:** Sedra Example 8.3 (worked in [the review deck](../../raw/slides/eee-335/lecture-review-units-4-6-final-spring-2026-slides.pdf)) ; HW 8.46 ; [[cascode-amplifier]] (next-step extension of this problem).

---

### 5. **CS HF response: Miller approximation + first analysis** (Medium, 14 pts) — Lectures 25, 26

A common-source amplifier has $g_m = 2$ mA/V, $r_o = 100$ k$\Omega$, $R_D = 50$ k$\Omega$, $R_\text{sig} = 5$ k$\Omega$, $R_L = 50$ k$\Omega$, $C_{gs} = 100$ fF, $C_{gd} = 30$ fF, $C_L = 50$ fF. Assume $R_G \to \infty$ (gate-bias resistor doesn't matter; ideal voltage source through $R_\text{sig}$).

> [!example] **Concept this problem tests.** Pattern 2 (CS gain) + Miller's theorem (Lecture 26) + the simple "first-analysis" $f_H$ from Lecture 25.
>
> **Building blocks:** mid-band gain $A_M = -g_m R_L'$ ; Miller multiplier $C_\text{eq} = C_{gd}(1 + g_m R_L')$ ; $f_H = 1/[2\pi R_\text{sig}'(C_{gs} + C_\text{eq})]$.

(a) Find the mid-band gain $A_M$.
(b) Apply Miller's theorem: find the Miller-multiplied input capacitance $C_\text{eq}$.
(c) Find the upper 3-dB frequency $f_H$ using the first (single-pole) analysis. Treat $C_L$ as part of $R_L'$ — i.e., for this part neglect $C_L$.
(d) State why this single-pole approximation works here.

<details><summary>Solution</summary>

**(a) Mid-band gain:**
$$R_L' = r_o \| R_D \| R_L = 100 \| 50 \| 50$$

$50 \| 50 = 25$ k$\Omega$ ; $100 \| 25 = 2500/125 = 20$ k$\Omega$. So $R_L' = 20$ k$\Omega$.

$$\boxed{A_M = -g_m R_L' = -2 \cdot 20 = \mathbf{-40\text{ V/V}}}$$

**(b) Miller-multiplied input capacitance:**
$$C_\text{eq} = C_{gd}(1 + g_m R_L') = 30 \text{ fF} \cdot (1 + 2 \cdot 20) = 30 \cdot 41 = \mathbf{1230\text{ fF}}$$
$$C_\text{in} = C_{gs} + C_\text{eq} = 100 + 1230 = \mathbf{1330\text{ fF}}$$

**(c) $f_H$ (single-pole approximation):** With $R_G \to \infty$, $R_\text{sig}' = R_\text{sig} = 5$ k$\Omega$.
$$\boxed{f_H = \frac{1}{2\pi R_\text{sig}' C_\text{in}} = \frac{1}{2\pi \cdot 5\times 10^3 \cdot 1330 \times 10^{-15}} = \frac{1}{2\pi \cdot 6.65 \times 10^{-9}} = \mathbf{23.9\text{ MHz}}}$$

**(d) Why the approximation works:** The Miller-multiplied $C_\text{eq}$ at the gate side is **41× larger** than $C_{gd}$ alone, dominating $C_{gs}$ (1230 fF vs. 100 fF). The pole at the gate side has $\tau = R_\text{sig}' \cdot 1330$ fF $\approx 6.65$ ns. The pole at the output side is set by $R_L' \cdot C_L = 20\text{ k} \cdot 50\text{ fF} = 1$ ns — about **6.6× faster**. So the gate pole **dominates** and a single-pole estimate is accurate.

> [!warning] **Common mistake.** Forgetting the "+1" in $C_{gd}(1 + g_m R_L')$. Miller multiplies by $(1 - K)$ where $K$ is the **inverting** gain, so $1 - (-g_m R_L') = 1 + g_m R_L'$. **Including the +1 is small here** ($1/41 \approx 2.4\%$) but it's what makes the formula dimensionally consistent.

> [!tip] **What to memorize vs. derive.**
> **Memorize:** Miller's theorem $Z_1 = Z/(1-K)$, $Z_2 = Z/(1 - 1/K)$. The Miller-multiplied input cap formula $C_\text{eq} = C_{gd}(1 + g_m R_L')$ is the most-used result in Unit 5.
> **Derive:** $R_L'$ as the parallel of three resistors. The dominance argument (compare RC at gate vs. output).

</details>

**Same framework as:** Sedra Example 10.1 ; Spring 2025 practice final P1 ; [[millers-theorem]] ; [[cs-amplifier-frequency-response]].

---

### 6. **OCTC method on the same CS amp** (Medium, 12 pts) — Lecture 29

Reuse the parameters from Problem 5. Now compute $f_H$ using the **method of open-circuit time constants** including $C_L$ at the output node.

> [!example] **Concept this problem tests.** OCTC mechanically: enumerate every cap, compute the resistance seen by each (with all *other* caps open), sum $\tau_k = C_k R_k$, take $\omega_H = 1/\sum \tau_k$.
>
> **Building blocks:** $R_{gs} = R_\text{sig}'$ ; $R_{gd} = R_\text{sig}'(1 + g_m R_L') + R_L'$ ; $R_{C_L} = R_L'$.

(a) Compute the three resistances $R_{gs}, R_{gd}, R_{C_L}$.
(b) Compute the three time constants $\tau_{gs}, \tau_{gd}, \tau_{C_L}$.
(c) Compute $f_H$ from the OCTC sum.
(d) Compare with the first-analysis answer from Problem 5(c) and explain the difference.

<details><summary>Solution</summary>

**(a) Resistances seen by each cap.** From Lecture 29 (CS three-cap formulas):
- $R_{gs} = R_\text{sig}' = 5\text{ k}\Omega$.
- $R_{gd} = R_\text{sig}'(1 + g_m R_L') + R_L' = 5(1 + 40) + 20 = 5 \cdot 41 + 20 = 205 + 20 = 225\text{ k}\Omega$.
- $R_{C_L} = R_L' = 20\text{ k}\Omega$.

**(b) Time constants:**
- $\tau_{gs} = C_{gs} R_{gs} = 100 \text{ fF} \cdot 5 \text{ k}\Omega = 500 \text{ ps}$.
- $\tau_{gd} = C_{gd} R_{gd} = 30 \text{ fF} \cdot 225 \text{ k}\Omega = 6750 \text{ ps}$.
- $\tau_{C_L} = C_L R_{C_L} = 50 \text{ fF} \cdot 20 \text{ k}\Omega = 1000 \text{ ps}$.
- **Total $\tau_H = 500 + 6750 + 1000 = 8250 \text{ ps} = 8.25 \text{ ns}$.**

**(c) $f_H$ from OCTC:**
$$\boxed{f_H = \frac{1}{2\pi \tau_H} = \frac{1}{2\pi \cdot 8.25 \times 10^{-9}} = \mathbf{19.3\text{ MHz}}}$$

**(d) Comparison with first analysis.** First analysis gave $f_H = 23.9$ MHz; OCTC gives $f_H = 19.3$ MHz. **OCTC is lower by about 19%** because it includes:
- The **$R_L'$ added to $R_{gd}$** (was missing in the first analysis — only $R_\text{sig}'(1 + g_m R_L')$).
- **$C_L$ at the output node** (entirely missed by the first analysis, which assumed $R_L'$ was capacitor-free).

OCTC is the **conservative / pessimistic** estimate; it correctly accounts for the second pole that the first-analysis approximation hand-waves away.

> [!tip] **What to memorize vs. derive.**
> **Memorize:** the three OCTC resistances for CS — $R_{gs} = R_\text{sig}'$, $R_{gd} = R_\text{sig}'(1 + g_m R_L') + R_L'$, $R_{C_L} = R_L'$. These appear on the formula sheet next to $f_H = 1/(2\pi \sum C_k R_k)$.
> **Derive:** the time constants ; the comparison with first analysis (ratio depends on which cap dominates).

</details>

**Same framework as:** Sedra Example 10.5 ; Spring 2025 practice final P1 ; [[octc-method]].

---

### 7. **Cascode HF advantage** (Hard, 18 pts) — Lectures CCA, CCA-HFR

A cascode amplifier is built from two NMOS transistors. $Q_1$ (CS at the bottom) has the same parameters as Problem 5 ($g_m = 2$ mA/V, $r_o = 100$ k$\Omega$, $C_{gs1} = 100$ fF, $C_{gd1} = 30$ fF, $C_{db1} = 20$ fF). $Q_2$ (CG at the top) is matched: $g_{m2} = 2$ mA/V, $r_{o2} = 100$ k$\Omega$, $C_{gs2} = 100$ fF, $C_{gd2} = 30$ fF. The drain of $Q_2$ is loaded by an ideal current source ($R_L = \infty$) **plus** an external load $R_L = 50$ k$\Omega$ through a load cap $C_L = 50$ fF. The signal source has $R_\text{sig} = 5$ k$\Omega$.

> [!example] **Concept this problem tests.** Pattern 3 (cascode total $R_o$ = $g_m r_o^2$) + Pattern 5 ("what changes if we cascode") + the absence of Miller multiplication on $C_{gd1}$ because the CG above presents a low impedance to $Q_1$'s drain. **The big signature problem from Spring 2025 P2.**
>
> **Building blocks:** $R_{d1} = R_{\text{in},2} \approx 1/g_{m2}$ ; cascode mid-band gain $A_M = -g_{m1}(R_o \| R_L)$ where $R_o = (g_{m2} r_{o2}) r_{o1}$ ; three time constants $\tau_1, \tau_2, \tau_3$.

(a) Find the resistance the CG ($Q_2$) presents at $Q_1$'s drain ($R_{d1}$).
(b) Find the cascode output resistance $R_o$ and the mid-band gain $A_M$ when loaded by $R_L = 50$ k$\Omega$.
(c) Compute the three OCTC time constants $\tau_1, \tau_2, \tau_3$.
(d) Compute $f_H$ for the cascode.
(e) **Compare** with the CS amplifier from Problem 5/6: report the gain ratio and bandwidth ratio.

<details><summary>Solution</summary>

**(a) $R_{d1}$.** $Q_2$ is a common-gate stage with its source seeing $r_{o1}$ as a "tail" and its drain seeing $R_L$ above. Looking into $Q_2$'s source (which IS $Q_1$'s drain):
$$R_{\text{in},2} = \frac{r_{o2} + R_L}{1 + g_{m2} r_{o2}}$$

With $r_{o2} = 100$ k$\Omega$ and $R_L = 50$ k$\Omega$: $R_{\text{in},2} = (100 + 50)/(1 + 200) = 150/201 = \mathbf{0.746\text{ k}\Omega}$.

So $R_{d1} \approx 1/g_{m2} = 0.5$ k$\Omega$ to a rough approximation, or **0.746 k$\Omega$** with the load-up correction.

**(b) Cascode $R_o$ and $A_M$.**
$$R_o \approx (g_{m2} r_{o2}) r_{o1} = (2 \cdot 100) \cdot 100 = 20{,}000\text{ k}\Omega = 20\text{ M}\Omega$$
$$R_o \| R_L = 20{,}000 \| 50 \approx \mathbf{49.9\text{ k}\Omega}$$
$$A_M = -g_{m1}(R_o \| R_L) = -2 \cdot 49.9 = \mathbf{-99.8\text{ V/V}}$$

(Note: when $R_L = 50$ k$\Omega$ is **finite**, $R_o \| R_L \approx R_L$ because $R_o \gg R_L$. The cascode's huge $R_o$ is wasted unless the load is also huge (e.g., a cascoded current source above). **Compare to CS Problem 5: $A_M = -40$ V/V; cascode here is $-99.8$ V/V — ~2.5× better gain.**)

**(c) Three time constants** (Lecture CCA-HFR):

$$\tau_1 = R_\text{sig}\bigl[C_{gs1} + C_{gd1}(1 + g_{m1} R_{d1})\bigr]$$

The Miller multiplier on $C_{gd1}$ is now $(1 + g_{m1} R_{d1}) = (1 + 2 \cdot 0.746) = 2.49$ — **MUCH smaller than the CS case (was 41)**. Plug:
$$\tau_1 = 5 \text{ k}\Omega \cdot [100 + 30 \cdot 2.49] = 5 \cdot [100 + 74.7] = 5 \cdot 174.7 = 873.5 \text{ ps}$$

$$\tau_2 = R_{d1}(C_{db1} + C_{gs2} + C_{gd1})$$
$$\tau_2 = 0.746 \text{ k}\Omega \cdot (20 + 100 + 30) \text{ fF} = 0.746 \cdot 150 = 112 \text{ ps}$$

$$\tau_3 = (R_o \| R_L)(C_{gd2} + C_L) = 49.9 \cdot (30 + 50) = 49.9 \cdot 80 = 3992 \text{ ps}$$

**Total $\tau_H = 873.5 + 112 + 3992 = 4977.5 \text{ ps} \approx 5.0 \text{ ns}$.**

**(d) $f_H$ for cascode:**
$$\boxed{f_H = \frac{1}{2\pi \cdot 5.0 \times 10^{-9}} = \mathbf{31.8\text{ MHz}}}$$

**(e) Comparison with CS:**

| | CS (Problem 5/6) | Cascode (this problem) | Ratio |
|---|---|---|---|
| $\|A_M\|$ | 40 V/V | 99.8 V/V | **2.5×** more gain |
| $f_H$ | 19.3 MHz (OCTC) | 31.8 MHz | **1.65×** more bandwidth |
| $\|A_M\| \cdot f_H$ (gain-bandwidth) | 772 MHz | 3174 MHz | **4.1×** more GBW |

**Cascode wins on both axes** — gain (because $R_o \gg R_D$, even though limited by $R_L$ here) AND bandwidth (because Miller multiplication on $C_{gd1}$ is killed: factor of 2.49 instead of 41). **The bandwidth advantage is dramatic when $R_\text{sig}$ is large.**

> [!warning] **The exam will test the qualitative reasoning.** Why does cascode have a bandwidth advantage? **Because the CG above presents low impedance ($\approx 1/g_{m2}$) at $Q_1$'s drain, killing the Miller multiplication on $C_{gd1}$.** That's the full story in one sentence. Students who memorize formulas without this story can't answer "explain why" questions.

> [!tip] **What to memorize vs. derive.**
> **Memorize:** cascode $R_o = g_m r_o^2$ ; $R_{\text{in,CG}} = (r_o + R_L)/(1 + g_m r_o) \approx 1/g_m$ when $r_o, R_L$ similar magnitude.
> **Derive:** the three OCTC time constants ; the comparison ratios. The bandwidth-advantage mechanism (no Miller multiplication on $C_{gd1}$).

</details>

**Same framework as:** Spring 2025 practice final P2 ; [[cascode-amplifier]] ; Lecture CCA-HFR slides.

---

### 8. **CM-loaded diff amp: $A_d$, $A_{cm}$, CMRR, HF response** (Hard, 22 pts) — Lectures 32–36

A CM-loaded MOS diff amp uses NMOS input pair $Q_1, Q_2$ and PMOS current-mirror load $Q_3$ (diode-connected) and $Q_4$. Tail current source: $I = 200\,\mu$A with output resistance $R_{SS} = 500$ k$\Omega$. All input pair: $V_{tn} = 0.5$ V, $k_n' = 0.4$ mA/V², $V_{An} = 10$ V, $V_{OV} = 0.2$ V. All mirror: $|V_{tp}| = 0.5$ V, $|k_p'| = 0.1$ mA/V², $|V_{Ap}| = 7.5$ V, $|V_{OV}| = 0.2$ V. Each input pair transistor carries $I_D = I/2 = 100\,\mu$A. Mirror node capacitance $C_M = 80$ fF. Output load capacitance $C_L = 60$ fF.

> [!example] **Concept this problem tests.** Pattern 1 (half-circuit virtual ground + CS-with-$R_s$ for CM) + Pattern 4 (the four definitions) + the L36 pole/zero formulas. **Spring 2025 practice final P4 verbatim — the 28-pt headliner.**
>
> **Building blocks:** $g_{m1} = I/V_{OV}$ ; $r_{o1} = V_{An} / (I/2)$ ; $r_{o4} = |V_{Ap}|/(I/2)$ ; $A_d = g_{m1}(r_{o2} \| r_{o4})$ ; $A_{cm} \approx -1/(2 g_{m3} R_{SS})$ ; $\omega_{p1} = 1/(R_o C_L)$ ; $\omega_{p2} = g_{m3}/C_M$ ; $\omega_z = 2 g_{m3}/C_M$.

(a) Find $g_{m1}$ and $g_{m3}$. (Use $g_m = I/V_{OV}$ for the diff pair where $I$ is the **tail** current; $g_{m3} = 2 I_{D3}/|V_{OV,p}|$ for the mirror.)
(b) Find $r_{o1}$ and $r_{o4}$.
(c) Find the differential mid-band gain $A_d$ (single-ended output at $Q_2$'s drain).
(d) Find $A_{cm}$ (single-ended output, matched mirror).
(e) Find CMRR in linear and in dB.
(f) **By what factor must $R_{SS}$ change to increase CMRR by 6 dB?** What's the equivalent change in $L$ (channel length of the tail bias transistor)?
(g) Find the load pole $\omega_{p1}$, the mirror pole $\omega_{p2}$, and the mirror zero $\omega_z$. Express in Hz.

<details><summary>Solution</summary>

**(a) $g_m$ values:**
$$g_{m1} = I/V_{OV,n} = 200\,\mu\text{A} / 0.2\text{ V} = \mathbf{1\text{ mA/V}}$$
$$g_{m3} = 2 I_{D3} / |V_{OV,p}| = 2 \cdot 100\,\mu\text{A} / 0.2\text{ V} = \mathbf{1\text{ mA/V}}$$

**(b) $r_o$ values:**
$$r_{o1} = r_{o2} = V_{An} / (I/2) = 10 / 0.1 = \mathbf{100\text{ k}\Omega}$$
$$r_{o4} = |V_{Ap}| / (I/2) = 7.5 / 0.1 = \mathbf{75\text{ k}\Omega}$$

**(c) Differential gain (single-ended output):**
$$R_o = r_{o2} \| r_{o4} = 100 \| 75 = (100 \cdot 75)/(175) = 7500/175 = 42.86\text{ k}\Omega$$
$$\boxed{A_d = g_{m1} \cdot R_o = 1 \cdot 42.86 = \mathbf{42.86\text{ V/V}}}$$

(Sign convention: with $V_\text{in+}$ at $Q_2$ — UGTA Diego's correction from Apr 30 — the gain is **non-inverting**, i.e., positive.)

**(d) Common-mode gain:**
$$\boxed{A_{cm} \approx -\frac{1}{2 g_{m3} R_{SS}} = -\frac{1}{2 \cdot 1 \times 10^{-3} \cdot 500 \times 10^3} = -\frac{1}{1000} = \mathbf{-10^{-3}\text{ V/V}}}$$

**(e) CMRR:**
$$\text{CMRR} = |A_d / A_{cm}| = 42.86 / 10^{-3} = \mathbf{42{,}860}$$
$$\text{CMRR (dB)} = 20 \log_{10}(42{,}860) = 20 \cdot 4.632 = \mathbf{92.6\text{ dB}}$$

**(f) +6 dB CMRR:** 6 dB = factor of 2 in linear (since $20\log 2 = 6.02$). CMRR ∝ $R_{SS}$ for the s.e.-output formula, so **$R_{SS}$ must double**. Since $R_{SS}$ comes from $r_o$ of the bias transistor, and $r_o = V_A L / (I \cdot \text{scaling})$ at fixed $W/L$ (because $V_A \propto L$ in a fixed-process technology), **doubling $R_{SS}$ requires doubling $L$**.

**(g) Pole and zero locations:**
$$\omega_{p1} = \frac{1}{R_o C_L} = \frac{1}{42.86 \times 10^3 \cdot 60 \times 10^{-15}} = \frac{1}{2.57 \times 10^{-9}} = 3.89 \times 10^8\text{ rad/s}$$
$$\boxed{f_{p1} = \omega_{p1} / (2\pi) = \mathbf{61.9\text{ MHz}}}$$

$$\omega_{p2} = \frac{g_{m3}}{C_M} = \frac{1 \times 10^{-3}}{80 \times 10^{-15}} = 1.25 \times 10^{10}\text{ rad/s}$$
$$\boxed{f_{p2} = \omega_{p2}/(2\pi) = \mathbf{1.99\text{ GHz}}}$$

$$\omega_z = \frac{2 g_{m3}}{C_M} = 2 \omega_{p2}$$
$$\boxed{f_z = \mathbf{3.98\text{ GHz}}}$$

**Pole-zero ordering:** $f_{p1} (62\text{ MHz}) \ll f_{p2} (1.99\text{ GHz}) < f_z (3.98\text{ GHz})$. The **load pole dominates** by ~30×, so $f_H \approx f_{p1} = 62$ MHz. The mirror pole/zero pair is a 6-dB/oct dip but at frequencies far above the dominant pole, so it has minimal effect on the in-band response.

> [!warning] **The four traps on Problem 4-style questions.**
> 1. **$g_m$ for diff pair: $g_m = I/V_{OV}$** (tail current, NOT $I/2$). Half the students use the wrong formula.
> 2. **Single-ended $A_{cm}$ has a "1/2" factor in the denominator** because of how the CM signal splits across the pair. With matched mirror it doesn't go to zero.
> 3. **CMRR units:** if you compute the ratio $|A_d/A_{cm}|$ and convert to dB, double-check whether you used $20 \log$ (voltage ratio) — not $10 \log$ (power).
> 4. **Channel-length scaling:** $V_A \propto L$ at fixed $W/L$ → $r_o \propto L$ → $R_{SS} \propto L$ → CMRR(s.e.) $\propto L$. Doubling $L$ adds 6 dB.

> [!tip] **What to memorize vs. derive.**
> **Memorize (high-priority):**
> 1. $A_d = g_m(r_{o2} \| r_{o4})$.
> 2. $g_m = I/V_{OV}$ for the diff pair (where $I$ = tail current).
> 3. CMRR(s.e.) = $g_m R_{SS}$ for matched mirror.
> 4. The three frequencies: $\omega_{p1} = 1/(R_o C_L)$, $\omega_{p2} = g_{m3}/C_M$, $\omega_z = 2 g_{m3}/C_M$.
>
> **Derive:** $r_{o1}, r_{o2}, r_{o4}$ from $V_A$ and $I_D$ ; the parallel combination ; the CMRR-vs-$L$ scaling.

</details>

**Same framework as:** Spring 2025 practice final P4 (verbatim) ; in-class Example 9.11 ; HW 9.85, 9.88, 10.70, 10.76 ; [[differential-pair]] ; [[cmrr]] ; [[eee-335-l36-cm-cl-set-01]].

---

### 9. **True/False drill** (Easy, 7 × 2 pts = 14 pts) — All units

> [!example] **Format anchor.** Mirrors UGTA Diego's drill style. Mark T/F **and write a 5-word reason** (mental check — don't write on the actual exam).

(a) An FIR filter can be unstable for the wrong coefficient choice.
(b) The output resistance of the cascode amp is approximately $g_m r_o^2$, which is much larger than a single CS amp.
(c) Sampling a 5 Hz cosine at 8 Hz aliases it. **(EEE 404 trap — included as cross-domain check; ignore on the actual EEE 335 exam.)**
(d) Common-mode gain of a diff amp **decreases** when the tail source's output resistance increases.
(e) Cascoding a CS amp **always** improves bandwidth, regardless of the load.
(f) The Miller effect causes $C_{gd}$ to appear larger at the input of an inverting amplifier.
(g) In a CM-loaded diff amp, the mirror zero is exactly twice the mirror pole.

<details><summary>Solution</summary>

| (a) | F | FIR has no feedback — always stable. |
| (b) | T | $R_o = g_{m2} r_{o2} \cdot r_{o1}$ ≈ $g_m r_o^2$. |
| (c) | T | (EEE 404 cross-check — Nyquist needs ≥ 10 Hz.) |
| (d) | T | $A_{cm} \approx -1/(2 g_{m3} R_{SS})$ — bigger $R_{SS}$, smaller $\|A_{cm}\|$. |
| (e) | F | When $R_L$ is small, cascode and CS have similar bandwidth. Cascode wins on BW only when $R_L$ is large enough that the Miller effect dominates the CS amp. |
| (f) | T | Miller multiplies $C_{gd}$ by $(1 + g_m R_L')$ at the input. |
| (g) | T | $\omega_z = 2 g_{m3}/C_M = 2 \omega_{p2}$ exactly. |

</details>

**Same framework as:** [[eee-335-final-lecture-review]] §"T/F + MC quick-fire"; UGTA Diego's drill bank.

---

### 10. **Multiple choice + short answer** (Easy–Medium, 11 pts) — All units

(a) **(3 pts) MC.** How many poles and zeros does the CM-loaded diff amp have?
- (i) 1 pole, 0 zeros — (ii) 2 poles, 0 zeros — (iii) 2 poles, 1 zero — (iv) 3 poles, 1 zero

(b) **(3 pts) MC.** When $R_\text{sig} \approx 0$, the 3-dB pole of a CS amp is set by:
- (i) $C_{gs}$ at the gate — (ii) $C_{gd}$ Miller-multiplied at the gate — (iii) $C_{gd}$ at the output and $C_L$ at the output — (iv) the body-source cap $C_{sb}$.

(c) **(2 pts) Short.** Common-source-with-degeneration ($R_s$): write the open-circuit voltage gain $A_{vo}$ in terms of $g_m, R_D, R_s$.

(d) **(3 pts) Short.** Source follower with body effect: state the mid-band gain in terms of $g_m, g_{mb}, R_L, r_o$.

<details><summary>Solution</summary>

**(a) (iii) 2 poles, 1 zero.** Load pole + mirror pole + mirror zero (Lecture 36).

**(b) (iii) $C_{gd}$ at the output and $C_L$ at the output.** When $R_\text{sig} \to 0$, the gate-side pole vanishes and the output-side pole dominates: $f_H = 1/[2\pi(C_L + C_{gd}) R_L']$. (Lecture 27.)

**(c) $A_{vo} = -\dfrac{g_m R_D}{1 + g_m R_s}$** (Table 7.4).

**(d) $G_{V\max} = \dfrac{g_m R_L'}{1 + g_m R_L'}$** where $R_L' = R_L \| r_o \| (1/g_{mb})$. The $1/g_{mb}$ in parallel is the body-effect contribution: it lowers $R_L'$ and pulls the gain below unity. (Lecture 31.)

</details>

**Same framework as:** Spring 2025 practice final P5 ; Lecture 27, 31, 36.

---

### 11. **Bonus — 2-stage cascode + diff amp** (Hard, 5 pts) — Cross-unit synthesis

A CMOS op-amp first stage is a CM-loaded diff amp identical to Problem 8 (single-ended output, $A_d = 42.86$ V/V). The second stage is a single-transistor common-source with $g_{m,5} = 0.8$ mA/V, $r_{o,5} = 90$ k$\Omega$, loaded by an ideal current source. What is the **mid-band differential gain end-to-end** (single-ended input → single-ended output)?

<details><summary>Solution</summary>

**Stage 1:** $A_{d,1} = +42.86$ V/V (single-ended output, non-inverting per UGTA correction).

**Stage 2** (CS with ideal current-source load): $A_{v,2} = -g_{m,5} r_{o,5} = -0.8 \cdot 90 = -72$ V/V.

**Total:** $A_d = A_{d,1} \cdot A_{v,2} = 42.86 \cdot (-72) = \mathbf{-3{,}086\text{ V/V}} \approx -70\text{ dB}$.

**Sign:** negative because Stage 2 is inverting; Stage 1 is non-inverting.

> [!tip] **Why this matters.** Real op-amps cascade a CM-loaded diff amp (high gain, modest BW) with a CS amp (more gain, modest BW) to build up to the ~$10^5$ open-loop gain you see in spec sheets. Frequency compensation (Miller cap across Stage 2) usually sets the dominant pole — but that's a Sedra Ch. 12 topic, not on this final.

</details>

**Same framework as:** Op-amp two-stage architecture (Sedra Ch. 12) ; [[differential-pair]] + [[common-source-amplifier]] cascade.

---

## Time-budget summary for the actual exam (110 min total)

| # | Type | Points | Suggested time |
|---|---|---|---|
| 1 | Q-point + small-signal extraction | 8 | 6 min |
| 2 | Configuration choice + $G_v$ | 10 | 8 min |
| 3 | Current mirror biasing | 8 | 8 min |
| 4 | Basic gain cell + swing | 12 | 12 min |
| 5 | CS HF first analysis (Miller) | 14 | 12 min |
| 6 | OCTC on the same CS | 12 | 8 min (re-uses Problem 5) |
| 7 | Cascode HF advantage | 18 | 18 min |
| 8 | CM-loaded diff amp full pipeline | 22 | 22 min |
| 9 | T/F drill | 14 | 5 min |
| 10 | MC + short answer | 11 | 5 min |
| 11 | Bonus | 5 | 4 min (if time) |
| | **Total** | **134** | **108 min** |

(Practice set has more points than the real exam — overpracticing on the hard problems is the whole point.)

> [!warning] **Don't camp on Problem 8 sub-parts.** If sub-part (f) or (g) is taking >5 min each, **skip and come back**. The DC bias + small-signal pipeline (parts a–e) is worth most of the points; the pole/zero locations are 4 pts of bonus territory.

---

## Master cheat-sheet anchor (build your formula sheet from this)

> [!example] **Print this section, hand-copy onto your 8.5×11" double-sided sheet, then practice once before exam morning.** This is a compressed version of [[eee-335-final-lecture-review]] §"Master Cheat Sheet" — go there for the full version.

### Most-used formulas by frequency-of-appearance

1. **$g_m = I/V_{OV} = \sqrt{2 k_n'(W/L) I_D}$** (used in every problem)
2. **$r_o = V_A / I_D$**
3. **CS gain:** $A_{vo} = -g_m R_\text{out}$ ; with $r_o$: $-g_m(R_D \| r_o)$
4. **CG:** $R_\text{in} = 1/g_m$, $R_o = r_o + R_S(1 + g_m r_o)$, $A_{vo} = +g_m R_o$
5. **SF:** $R_\text{in} = \infty$, $R_o = 1/g_m$, $A_v \approx 1$
6. **Cascode:** $R_o = (g_{m2} r_{o2}) r_{o1}$ ; $A_{v0} = -(g_m r_o)^2$ (ideal load) ; $-\tfrac{1}{2}(g_m r_o)^2$ (cascode load)
7. **Mirror:** $I_O = I_\text{REF} (W/L)_2 / (W/L)_1$ ; saturation $V_O \geq V_{OV}$
8. **Miller:** $Z_1 = Z/(1 - K)$ ; for $K = -g_m R_L'$, $C_{gd}$ becomes $C_{gd}(1 + g_m R_L')$
9. **CS first analysis $f_H$:** $f_H = 1/[2\pi R_\text{sig}'(C_{gs} + C_{gd}(1 + g_m R_L'))]$
10. **OCTC for CS:** $\tau_H = C_{gs} R_\text{sig}' + C_{gd}[R_\text{sig}'(1 + g_m R_L') + R_L'] + C_L R_L'$ ; $f_H = 1/(2\pi \tau_H)$
11. **Diff pair $g_m$:** $g_m = I/V_{OV}$ (tail current)
12. **Diff out $A_d = g_m R_D$** (or $g_m(r_o \| R_D)$) ; **s.e. $A_{d,\text{s.e.}} = g_m R_D / 2$** (with resistive load)
13. **CM-loaded $A_d = g_m(r_{o2} \| r_{o4})$**
14. **CMRR(s.e.) = $g_m R_{SS}$** ; **CMRR(diff,mismatched) = $2 g_m R_{SS}/(\Delta R_D / R_D)$**
15. **CMRR(dB) = $20 \log_{10}(\text{CMRR})$** ; +6 dB = ×2 in linear
16. **L36 trio:** $\omega_{p1} = 1/(R_o C_L)$, $\omega_{p2} = g_{m3}/C_M$, $\omega_z = 2 g_{m3}/C_M$ (mirror zero exactly 2× mirror pole)

### Always-on facts (the 5 to memorize cold)

1. $A_d = g_m (r_{o2} \| r_{o4})$ for the active-load diff pair.
2. $g_m = I_\text{tail} / V_{OV}$ for the diff pair (not $I_D/V_{OV}$ — that's the half-circuit form, which gives the same number anyway).
3. $\text{CMRR}_\text{s.e.} = g_m R_{SS}$.
4. $\omega_p = 1/(R_o C_L)$ — load pole everywhere.
5. **CMRR ∝ $R_{SS}$ ∝ $L$** (channel length of the tail bias transistor) → **+6 dB CMRR = ×2 $L$**.

### Saturation requirements (always check)

- **NMOS:** $V_{DS} \geq V_{OV} = V_{GS} - V_t$.
- **PMOS:** $V_{SD} \geq |V_{OV}| = V_{SG} - |V_{tp}|$.
- **Diff amp CM range:** $V_{CM,\max} = V_{DD} - I R_D / 2 + V_{tn}$ ; $V_{CM,\min} = -V_{SS} + V_{CS} + V_{OV} + V_{tn}$.

---

## Jayden's attempts

_Log attempts here: date, which problems, what was wrong, what clicked. After exam day, mark which problem types on the **actual** final you got right vs. wrong._

- _(empty — fill in tonight after first attempt or tomorrow after exam)_

---

## Related

- [[eee-335]] — course page (master roadmap)
- [[eee-335-final-walkthrough]] — earlier Units 1–6 walkthrough with worked problems and collapsible derivations
- [[eee-335-final-lecture-review]] — the lecture-by-lecture map + master cheat sheet (the 5 framework patterns, full formula list)
- [[eee-335-l36-cm-cl-set-01]] — companion practice set for Lecture 36 (CM-loaded diff amp + $C_M, C_L$ identification)

### Concept pages

- [[mosfet-small-signal-model]], [[common-source-amplifier]], [[common-gate-amplifier]], [[source-follower]] — Unit 4 single-stage building blocks
- [[current-mirror]] — Unit 4 IC biasing
- [[cascode-amplifier]] — Unit 5 + CCA
- [[mosfet-high-frequency-model]], [[millers-theorem]], [[octc-method]], [[cs-amplifier-frequency-response]] — Unit 5 frequency response
- [[differential-pair]], [[cmrr]] — Unit 6

### Source files

- [Spring 2025 practice final](../../raw/slides/eee-335/practice-final-exam-spring-25.pdf) + [solutions](../../raw/slides/eee-335/practice-final-exam-spring-25-solutions.pdf)
- [Units 4–6 review deck (115 pp)](../../raw/slides/eee-335/lecture-review-units-4-6-final-spring-2026-slides.pdf)
- All Lecture 17–36, CCA, CCA-HFR slide PDFs are linked in [[eee-335-final-lecture-review]] §Related.
