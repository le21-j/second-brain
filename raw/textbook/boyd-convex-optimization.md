# Convex Optimization — Boyd & Vandenberghe

**Category:** Math (optimization)
**Status:** FREE
**URL:** https://stanford.edu/~boyd/cvxbook/
**Authors:** Stephen Boyd (Stanford EE), Lieven Vandenberghe (UCLA)
**Publisher:** Cambridge University Press, 2004
**Roadmap phase:** reference — Ch 1–5

## Topic coverage
- Ch 1: Introduction — what is convex, why it matters.
- Ch 2: Convex sets.
- Ch 3: Convex functions.
- Ch 4: Convex optimization problems (LP, QP, SOCP, SDP, GP).
- Ch 5: **Duality — the chapter that pays for the whole book** (Lagrangian, KKT conditions, strong duality).
- Ch 6–11: algorithms (interior-point, Newton, gradient).

## Why it's on the roadmap
> "Chapters 1–5."

The first five chapters give you a vocabulary that shows up in **every resource allocation, beamforming, and rate control paper** in wireless. KKT conditions explicitly appear in the water-filling solution for power allocation, in the WMMSE algorithm, and in the derivation of the "learning to optimize" literature ([[sun-learning-to-optimize]]).

## The one takeaway
If you only read one chapter, read Chapter 5 (Duality). Dual decomposition is a technique you will reach for every time a resource-allocation problem has a shared constraint.

## Pair with
- Stanford CVX course (Boyd's own lectures on YouTube, https://www.youtube.com/playlist?list=PL3940DD956CDF0622).
- CVXPY (https://www.cvxpy.org/) for hands-on.

## Related wiki pages
- [[python-ml-wireless]]
- [[stephen-boyd]]
