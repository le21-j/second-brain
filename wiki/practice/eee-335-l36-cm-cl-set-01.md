---
title: "EEE 335 L36 — C_M and C_L in the Diff-Amp + Current-Mirror — Practice Set 01"
type: practice
course:
  - "[[eee-335]]"
tags:
  - practice
  - differential-pair
  - current-mirror
  - frequency-response
  - ac-ground
concept:
  - "[[differential-pair]]"
  - "[[current-mirror]]"
  - "[[millers-theorem]]"
  - "[[mosfet-high-frequency-model]]"
difficulty: medium
created: 2026-04-30
---

# EEE 335 L36 — $C_M$ and $C_L$ in the Diff-Amp + Current-Mirror — Practice Set 01

> Attempt each problem before scrolling to the solution. The full Socratic synthesis these problems came out of is logged at [[diff-amp-frequency-response]]. The diff-pair topology is the standard NMOS-input pair $M_1, M_2$ with a PMOS current-mirror load $M_3$ (diode-connected) and $M_4$, single-ended output taken from $M_2$'s drain. Inputs $V_{in+}$ to $M_2$, $V_{in-}$ to $M_1$. Tail bias $I_{SS}$ to ground.

## Problems

### 1. Easy — diode-connected $C_{gd}$
A single MOSFET has three relevant intrinsic capacitances: $C_{gs}$, $C_{gd}$, and $C_{db}$. In a **diode-connected** configuration (gate tied directly to drain), which of these capacitances is "shorted out" and contributes nothing to the small-signal AC behavior? Why?

<details><summary>Solution</summary>

**Answer:** $C_{gd}$ is shorted out.

In a diode-connected MOSFET, the gate node and the drain node are **the same node**. $C_{gd}$ is, by definition, the capacitance from gate to drain — i.e., from one node to itself. Its two plates are at the same potential at all times, so no displacement current can flow through it. It's electrically invisible.

$C_{gs}$ and $C_{db}$ remain valid: they connect gate-or-drain (now one node) to source and to bulk respectively, which are different nodes.

This is exactly why, when enumerating parasitics at the **mirror node** of a current-mirror-loaded diff pair, we include $C_{gs3}$ but **not** $C_{gd3}$.

</details>

### 2. Medium — building $C_M$ and $C_L$ from parasitics
For the diff-amp + current-mirror topology described in the header, draw or list which parasitic capacitances land at:

(a) the **mirror node** (drain of $M_1$ = gate-drain of $M_3$ = gate of $M_4$), and

(b) the **output node** (drain of $M_2$ = drain of $M_4$).

For each cap, identify which terminal lives at the high-Z node and which terminal lives at AC ground. State explicitly which AC-ground assumption justifies treating its far end as ground. Then write the lumped expressions $C_M = \dots$ and $C_L = \dots$ in terms of the elementary $C_{gs}$, $C_{gd}$, $C_{db}$ parasitics of $M_1, M_2, M_3, M_4$ plus an external load $C_{\text{ext}}$ at the output.

<details><summary>Solution</summary>

**(a) Mirror node parasitics** — the mirror node is at impedance $r_{o1} \parallel \tfrac{1}{g_{m3}} \approx \tfrac{1}{g_{m3}}$. Caps with one plate here and the other at AC ground:

| Cap | Far-end node | Why far end is AC ground |
|---|---|---|
| $C_{gs3}$ | $V_{DD}$ (source of PMOS $M_3$) | Supply rail = AC ground by definition |
| $C_{gs4}$ | $V_{DD}$ (source of PMOS $M_4$) | Supply rail = AC ground |
| $C_{db1}$ | bulk (true ground) | Bulk = AC ground |
| $C_{db3}$ | bulk | Bulk = AC ground |
| $C_{gd1}$ | gate of $M_1$ = $V_{in-}$ | Driven by ideal source $R_S \approx 0$, so input node is AC ground |

> [!note] $C_{gd3}$ is **not** in this list — $M_3$ is diode-connected, so $C_{gd3}$ has both plates on the same node and is shorted out (see Problem 1).

$$C_M = C_{gs3} + C_{gs4} + C_{db1} + C_{db3} + C_{gd1}$$

**(b) Output node parasitics** — the output node is high-Z ($r_{o2} \parallel r_{o4}$, tens of k$\Omega$). Caps with one plate here and the other at AC ground:

| Cap | Far-end node | Why far end is AC ground |
|---|---|---|
| $C_{db2}$ | bulk | Bulk = AC ground |
| $C_{db4}$ | bulk | Bulk = AC ground |
| $C_{gd2}$ | gate of $M_2$ = $V_{in+}$ | Ideal source $R_S \approx 0$, input node is AC ground |
| $C_{gd4}$ | gate of $M_4$ = mirror node | Mirror node is AC ground via diode-connected $1/g_{m3}$ |
| $C_{\text{ext}}$ | true ground (load cap to ground) | By assumption |

$$C_L = C_{db2} + C_{db4} + C_{gd2} + C_{gd4} + C_{\text{ext}}$$

**The whole point:** $C_{gd2}$ and $C_{gd4}$ both appear in $C_L$ even though their *far-end* nodes are different (input node vs mirror node). They lump as parallel only because **both** of those far-end nodes are AC-grounded — input via $R_S \approx 0$ and mirror via $1/g_{m3}$. If either approximation breaks (see Problem 3), the parallel-combination formula breaks too.

</details>

### 3. Hard — what if the input source is high-Z?
Suppose $V_{in+}$ is **not** an ideal voltage source but is driven by a sensor with $R_S = 1\,\text{M}\Omega$ in series. (The differential-pair gate at $M_2$ still has $\infty$ DC input impedance, but the *node* impedance at the gate of $M_2$ is now set by $R_S$ in parallel with the gate-side parasitics.)

(a) What changes about the AC-ground status of the input node at $M_2$'s gate?

(b) How does this break the simple "$C_L$ is the sum of parasitics at the output node" formula derived in Problem 2?

(c) What new effect appears at the output that wasn't there before, and how does it scale?

<details><summary>Solution</summary>

**(a)** The input node is no longer AC ground. With $R_S = 1\,\text{M}\Omega$, the input node sees $R_S \parallel R_{\text{gate}} = R_S \parallel \infty = R_S = 1\,\text{M}\Omega$ — which is **higher** than the output node's $r_{o2} \parallel r_{o4}$ (~tens of k$\Omega$). Far from being AC ground, the input node is now the *highest*-Z node in the circuit. Signal develops there, not gets killed there.

**(b)** $C_{gd2}$'s far plate (the gate of $M_2$) is no longer at AC ground. The clean "lump every parasitic at the output node into a single $C_L$ to ground" picture breaks because $C_{gd2}$ now connects two high-Z nodes (input node ↔ output node) — it's a **bridging** capacitance, not a node capacitance. You can't just add it to $C_L$ as a cap-to-ground; it now mediates feedback between input and output.

**(c) Miller multiplication.** With a bridging cap between two nodes that have a voltage gain $A_v$ between them ($M_2$ is a common-source-like stage from input gate to output drain), apply [[millers-theorem]]:

$$C_{\text{Miller, in}} = C_{gd2} \cdot (1 + |A_v|), \qquad C_{\text{Miller, out}} = C_{gd2} \cdot \left(1 + \tfrac{1}{|A_v|}\right) \approx C_{gd2}$$

So at the **input node** you now see $C_{gs2} + C_{gd2}(1 + |A_v|)$ — and since $|A_v|$ for a diff pair with current-mirror load is $g_m \cdot (r_{o2} \parallel r_{o4})$ (tens to hundreds), $C_{gd2}$ gets multiplied by ~50–500×. Combined with the $1\,\text{M}\Omega$ source resistance, this creates a **dominant low-frequency pole at the input** (Miller pole):

$$f_{p,\text{in}} \approx \frac{1}{2\pi R_S \cdot C_{gd2}(1 + |A_v|)}$$

For $R_S = 1\,\text{M}\Omega$, $C_{gd2} = 5\,\text{fF}$, $|A_v| = 100$:

$$f_{p,\text{in}} \approx \frac{1}{2\pi \cdot 10^6 \cdot 5 \times 10^{-15} \cdot 101} \approx 315\,\text{kHz}$$

— a sensor-frontend instead of an open-loop op-amp, and the bandwidth has collapsed by 2–3 orders of magnitude versus the ideal-source case.

> [!tip] **The general lesson:** the lumped $C_M$ / $C_L$ formulas assume every "far-end" node of every gate-drain cap is AC-grounded. When that breaks (high-Z source, capacitive coupling, transistor cascading), Miller multiplication appears and the bandwidth analysis must move from OCTC node-cap to actual two-node feedback.

</details>

## Jayden's attempts

- `2026-04-30` — **Not yet attempted.** This set was generated immediately after a Socratic session in which Jayden derived $C_M$ and $C_L$ from first principles by walking the AC-ground logic at every node. The session is logged at [[diff-amp-frequency-response]] (Jayden's personal log). The hardest problem (Problem 3) is the most interesting — it breaks the cleanest assumption in the whole derivation and is exactly the kind of follow-up that shows up on EEE 335 problem sets and analog interview questions.

## Related

- [[diff-amp-frequency-response]] — mistake log capturing the Socratic derivation that led to this set
- [[differential-pair]] — gain expressions
- [[current-mirror]] — load topology
- [[millers-theorem]] — needed for Problem 3
- [[mosfet-high-frequency-model]] — where the $C_{gs}, C_{gd}, C_{db}$ parasitics come from
- [[octc-method]] — using lumped node caps to estimate bandwidth
- [[eee-335-final-walkthrough]] — Unit 6 final-prep coverage
