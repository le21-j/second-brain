---
title: Diff Amp Frequency Response — Mistakes
type: mistake
course:
  - "[[eee-335]]"
tags:
  - mistakes
  - differential-pair
  - current-mirror
  - frequency-response
  - miller
  - ac-ground
concept:
  - "[[differential-pair]]"
  - "[[current-mirror]]"
  - "[[millers-theorem]]"
created: 2026-04-30
updated: 2026-04-30
---

# Diff Amp Frequency Response — Common Mistakes

Mistakes that surface when deriving the lumped node capacitances $C_M$ (mirror node) and $C_L$ (output node) for a differential pair with a current-mirror load. The whole derivation hinges on which nodes are AC ground and *why*.

## Known gotchas (general)

- **Gate input Z vs node Z** — A MOSFET gate has $\infty$ DC input impedance, but the *node* the gate is connected to is NOT high-Z by virtue of the gate alone. The node's impedance is the **parallel combination of EVERYTHING connected to it**, dominated by the smallest term. The gate's $\infty$ becomes irrelevant once a low-Z source ($R_S$) or low-Z element (diode-connected drain $1/g_m$) is in parallel with it. Always enumerate every connection at a node before declaring its impedance.

- **$v = i \cdot Z$ direction** — For a node to behave like AC ground, $Z$ must be **SMALL** (so an injected current produces a tiny voltage). Common error: assuming high-Z = AC ground. It's the **opposite** — high-Z nodes are where signal *develops* (output node, mirror node before approximation); low-Z nodes are where signal is *killed* (AC ground via $R_S$ or diode-connected $1/g_m$). The math is $v = iZ$: small $Z$ means small $v$ for any reasonable $i$.

- **Diode-connected drain $Z = 1/g_m$** — When a MOSFET has its gate tied to its drain, the gate-to-drain feedback collapses the small-signal output impedance from $r_o$ (tens of k$\Omega$) down to $\sim 1/g_m$ (a few hundred $\Omega$). This is the mechanism that AC-grounds the mirror node in a current-mirror-loaded diff pair: $M_3$ is diode-connected, so the mirror node sees $r_{o1} \parallel \tfrac{1}{g_{m3}} \approx \tfrac{1}{g_{m3}}$. Without this collapse, the mirror node would be high-Z and would not lump cleanly into a single node-cap $C_M$.

- **$C_{gd2} \parallel C_{gd4}$ at the output** — They are **NOT literally in parallel by raw KVL**: their far-end plates are at different nodes ($C_{gd2}$'s far plate is at the input node, $C_{gd4}$'s far plate is at the mirror node). They lump as parallel **only after both far-end nodes are approximated as AC ground** — input via $R_S \approx 0$, mirror via $1/g_{m3}$. State the approximation explicitly when writing $C_L$; the textbook formula bakes it in silently.

- **Diode-connected $C_{gd}$ is shorted out** — For a diode-connected MOSFET (gate = drain, e.g., $M_3$ in a current mirror), $C_{gd}$ has both plates on the **same node**. A capacitor whose two plates are at the same potential cannot store charge — it's electrically invisible. Do **not** include the diode-connected transistor's $C_{gd}$ when summing parasitics at the mirror node. ($C_{gs}$ still counts: gate-to-source = mirror-node-to-$V_{DD}$ = mirror-node-to-AC-ground.)

## Jayden's personal log

- `2026-04-30` — *Built up from raw confusion to full synthesis on $C_M$ / $C_L$ for the diff-amp + current-mirror.* Flipped $v = iZ$ direction twice before locking in **low-Z = AC ground** (kept defaulting to "high-Z = where the signal is, must be ground"). Conflated **gate input Z** ($\infty$) with **node Z** (parallel combination of everything connected). Missed the diode-connected $1/g_{m3}$ when first enumerating the mirror node's connections — needed the explicit prompt "what is the impedance looking into a diode-connected MOSFET drain?" to surface it. Resolved by walking the parallel-combination logic at both the input node and the mirror node and confirming both reduce to AC ground in the small-Rs / $g_{m3} r_{o1} \gg 1$ regime. Pattern to remember: **the lumped $C_M$ / $C_L$ formula is just "sum every parasitic that has one plate at the high-Z node and one plate at AC ground" — once the AC-ground status of every neighboring node is established, the formula falls out without further thought.**

## Related

- [[differential-pair]] — gain expressions and DC operating point
- [[current-mirror]] — load topology that creates the mirror node
- [[millers-theorem]] — same family of "what is across the cap" questions
- [[mosfet-high-frequency-model]] — source of the $C_{gs}$, $C_{gd}$, $C_{db}$ parasitics
- [[octc-method]] — how lumped node-caps feed into bandwidth estimation
- [[eee-335-final-walkthrough]] — Unit 6 final-prep coverage of the diff pair
