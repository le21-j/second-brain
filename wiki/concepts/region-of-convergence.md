---
title: Region of Convergence (ROC)
type: concept
course:
  - "[[eee-404]]"
tags: [z-transform, roc, stability, causality, dsp, eee-404]
sources:
  - "[[summary-eee-404-m7-frequency-domain]]"
created: 2026-04-29
updated: 2026-05-06
---

# Region of Convergence (ROC)

## In one line
The **ROC** of a Z-transform $X(z)$ is the set of complex $z$ for which the defining sum converges — without it, $X(z)$ doesn't uniquely identify $x[n]$.

## Example first

Take $H(z) = \dfrac{z(z+3)}{(z - 1/5)(z + 1/2)}$ (Exam 2 Problem 2). Poles at $z = 1/5$ and $z = -1/2$. **Three possible ROCs:**

1. **$|z| > 1/2$** (outside outermost pole) → **causal** sequence. Includes the unit circle ($1 > 1/2$) → DTFT exists ✓ → **causal AND stable**.
2. **$1/5 < |z| < 1/2$** → **two-sided** sequence (one pole on each side). Does NOT include unit circle (it's outside the annulus) → DTFT does **not** exist.
3. **$|z| < 1/5$** (inside innermost pole) → **anti-causal** sequence. Does NOT include unit circle → DTFT does not exist.

The "the Fourier transform of $h[n]$ exists" hint in the exam locks you into ROC option 1.

## The idea

Two different signals can share the same $X(z)$ formula but differ in which $z$ values make the sum converge. **The ROC is the disambiguator.** It also encodes:
- **Causality** — right-sided (causal) sequences have ROC = exterior of a circle.
- **Stability** — sequence is BIBO stable iff ROC includes the unit circle.

## Formal definition

For $X(z) = \sum_n x[n] z^{-n}$:
$$\text{ROC}(X) = \{z \in \mathbb C : \text{the sum converges}\}$$

ROCs are always **open annular regions** centered at the origin (rings, possibly degenerating to disks or punctured planes). Boundaries can be circles of radii equal to pole magnitudes.

## ROC rules table (memorise for Exam 2)

| Sequence type | ROC |
|---|---|
| Right-sided / causal $x[n] = 0$ for $n < n_0$ | $\{|z| > r_{\max}\}$ — outside outermost pole |
| Left-sided / anti-causal $x[n] = 0$ for $n > n_0$ | $\{|z| < r_{\min}\}$ — inside innermost pole |
| Two-sided / both | annulus between two pole rings |
| Finite-length | entire $z$-plane (possibly excluding $z = 0$ or $z = \infty$) |

**Stability test:** $h[n]$ absolutely summable ($\sum |h[n]| < \infty$) ⟺ ROC includes the unit circle ⟺ DTFT exists.

**Causal+stable test:** sequence is right-sided AND BIBO-stable ⟺ ROC includes everything outside the unit circle ⟺ all poles strictly inside the unit circle.

## Why it matters / when you use it

- **Exam 2 Problem 2(a):** "If the DTFT of $h[n]$ exists, sketch ROC" — requires knowing the rules above.
- **Filter design:** confirm a designed filter is stable and causal.
- **Inverse Z-transform:** the ROC determines whether you take the right-sided or left-sided expansion.

## Common mistakes

- **Confusing "DTFT exists" with "causal stable".** DTFT exists requires only that ROC ⊃ unit circle. Causal stable additionally requires the ROC be of the form $|z| > r_{\max}$.
- **Forgetting that ROC is part of the answer.** Saying "$X(z) = 1/(1 - 0.5 z^{-1})$" without an ROC is ambiguous.
- **Drawing ROC as a closed region.** ROCs are open (poles aren't in the ROC).

## Related

- [[z-transform]] — the parent concept
- [[dtft]] — exists when ROC ⊃ unit circle
- [[direct-form-ii]] — block-diagram realisation
- [[eee-404-exam-2-walkthrough]] — Problem 2(a) for a 2nd-order IIR

## Practice
- Exam 2 Practice Problem 2(a)
