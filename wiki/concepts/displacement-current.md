---
title: Displacement Current
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, electromagnetics, maxwell, amperes-law]
sources: [raw/slides/eee-341/lecture-1-4-displacement-current-9-30.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Displacement Current

## In one line
The term $\partial\vec{D}/\partial t$ that Maxwell added to Ampere's law so a time-varying electric field can produce a magnetic field — even in vacuum, where no charges flow.

## Example first
Charge a parallel-plate capacitor with a sinusoidal current $i(t) = I_0\cos\omega t$. Wrap an Amperian loop around the wire on one side: $\oint\vec{H}\cdot d\vec{l} = i(t)$. Now slide the surface bounded by that loop *between the plates* — there is no conduction current crossing it. Static Ampere would say the loop integral is zero, contradicting the first calculation. The displacement current density

$$\vec{J}_d = \frac{\partial\vec{D}}{\partial t} = \epsilon\frac{\partial\vec{E}}{\partial t}$$

restores agreement: between the plates $\vec{E}$ is changing at exactly the right rate to deliver the missing $i(t)$ through the displacement-current surface integral.

## The idea
A changing electric field "looks like" a current to magnetic-field-generating physics. There is no actual charge motion — the field itself carries the bookkeeping. This term is what enables EM waves to propagate through vacuum.

## Formal definition

$$\vec{J}_d = \frac{\partial\vec{D}}{\partial t} = \epsilon\frac{\partial\vec{E}}{\partial t} \quad \text{[A/m}^2\text{]}$$

The full Ampere–Maxwell law is

$$\nabla\times\vec{H} = \underbrace{\vec{J}}_{\text{conduction}} + \underbrace{\frac{\partial\vec{D}}{\partial t}}_{\text{displacement}}$$

Time-harmonic form: $\vec{J}_d = j\omega\epsilon\vec{E}$.

## Conduction-vs-displacement ratio
$$\frac{|\vec{J}_c|}{|\vec{J}_d|} = \frac{\sigma}{\omega\epsilon}$$

This dimensionless ratio classifies materials at a given frequency:
- $\sigma/(\omega\epsilon) \gg 1$ — **good conductor** (conduction dominates)
- $\sigma/(\omega\epsilon) \ll 1$ — **good insulator / low-loss dielectric** (displacement dominates)
- Order unity — **quasi-conductor** (both matter; humid soil at MHz is the classic example)

In free space $\sigma = 0$ so only displacement current can exist.

## Why it matters / when you use it
Without it, Ampere's law contradicts the [[charge-current-continuity]] equation in the time-varying case, and EM waves cannot propagate. It is also what makes the [[complex-permittivity]] bookkeeping work — collapsing $\sigma$ and $\omega\epsilon$ into one number $\omega\epsilon_c$.

## Common mistakes
- **Calling it "current" without quotes.** No charge moves in displacement current. The name is historical (Maxwell envisioned an aether with elastic displacement); the math is what matters.
- **Treating $\sigma/(\omega\epsilon)$ as a static property.** It is *frequency-dependent*. Soil that's a conductor at 1 kHz is a dielectric at 10 GHz.

## Related
- [[maxwell-equations]] — where the term lives
- [[complex-permittivity]] — how to fold conduction + displacement into one number
- [[helmholtz-equation]] — depends on $\partial\vec{D}/\partial t$ to support wave solutions
