---
title: Boundary Conditions for Electromagnetic Fields
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, electromagnetics, boundary-conditions, interfaces]
sources: [raw/slides/eee-341/lecture-1-5-boundary-conditions-for-electromagnetics-11-37.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Boundary Conditions for EM Fields

## In one line
At an interface between two media, the *tangential* components of $\vec{E}$ and $\vec{H}$ and the *normal* components of $\vec{D}$ and $\vec{B}$ obey four matching rules; deviations require a surface charge or surface current.

## Example first
A plane wave hits glass ($\epsilon_{r2}=4$) at normal incidence from air ($\epsilon_{r1}=1$). At the surface:

- $\vec{E}$ is tangential to the boundary, so $E_{1t} = E_{2t}$ — the electric field is continuous through the glass.
- $\vec{H}$ is also tangential, no surface current at the dielectric–dielectric interface, so $H_{1t} = H_{2t}$.
- These two continuity rules are exactly what give the [[fresnel-coefficients]].

If medium 2 were a perfect conductor instead, $\vec{E}_{2}=0$ inside, so $E_{1t}=0$ at the surface — the wave cannot have a tangential $\vec{E}$ on a PEC. That is why the [[reflection-coefficient-line]] for a PEC short is $-1$.

## The idea
Each boundary condition comes from applying an integral form of Maxwell's equations to an infinitesimally thin pillbox or Amperian loop straddling the interface, then taking the thickness $\to 0$.

## Formal definition

| Quantity | Boundary condition | Source |
|---|---|---|
| Normal $\vec{D}$ | $\hat{n}\cdot(\vec{D}_1 - \vec{D}_2) = \rho_s$ | Gauss / pillbox |
| Normal $\vec{B}$ | $\hat{n}\cdot(\vec{B}_1 - \vec{B}_2) = 0$ | $\nabla\cdot\vec{B}=0$ |
| Tangential $\vec{E}$ | $\hat{n}\times(\vec{E}_1 - \vec{E}_2) = 0$ | Faraday / Amperian loop |
| Tangential $\vec{H}$ | $\hat{n}\times(\vec{H}_1 - \vec{H}_2) = \vec{J}_s$ | Ampere–Maxwell / loop |

Here $\hat{n}$ points from medium 2 into medium 1; $\rho_s$ is surface charge density (C/m$^2$), $\vec{J}_s$ surface current density (A/m).

### Special cases
- **Two perfect dielectrics:** $\rho_s = 0$, $\vec{J}_s = 0$ ⇒ all four components continuous.
- **Dielectric–perfect conductor:** all fields vanish inside the conductor. Tangential $\vec{E} = 0$ at the surface; $\vec{H}$ at the surface is tangential and equals $\vec{J}_s\times\hat{n}$; surface charge $\rho_s = D_n$.

## Why it matters / when you use it
- Derive [[fresnel-coefficients]] (normal incidence reflection/transmission).
- Derive [[snells-law]] from phase-matching the tangential propagation factor across the boundary.
- Set up the eigenvalue problem for [[waveguide-modes]] (PEC walls force $E_t=0$).

## Common mistakes
- **Forgetting which component is which.** Mnemonic: $\vec{E}$ and $\vec{H}$ care about *tangent*; $\vec{D}$ and $\vec{B}$ care about *normal*.
- **Assuming $\rho_s = 0$ when there's a conductor.** A surface charge always builds up at a metal–dielectric interface; only the dielectric–dielectric case has no $\rho_s$ by default.

## Related
- [[maxwell-equations]] — the integral forms these come from
- [[fresnel-coefficients]] — direct application
- [[snells-law]] — phase matching
- [[waveguide-modes]] — PEC walls drive the eigenvalue problem
