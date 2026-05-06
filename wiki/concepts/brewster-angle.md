---
title: Brewster Angle
type: concept
course:
  - "[[eee-341]]"
tags: [eee-341, electromagnetics, oblique-incidence, polarization]
sources: [raw/slides/eee-341/lecture-3-8-critical-angle-total-internal-reflection-and-brewster-angle-12-08.pdf]
created: 2026-04-28
updated: 2026-05-06
---

# Brewster Angle

## In one line
The angle of incidence at which **parallel-polarized** light is *fully transmitted* (zero reflection) — given by $\theta_B = \arctan(n_2/n_1)$ for non-magnetic media.

## Example first
Sunlight reflecting off a wet road from air ($n_1 = 1$) to water ($n_2 = 1.33$):

$$\theta_B = \arctan(1.33/1) = 53.1°$$

At this angle the *horizontally* polarized component (parallel to the road) reflects with $\Gamma_\parallel = 0$ — only the *vertical* component reflects. That's why polarized sunglasses (rejecting horizontal polarization) cut road glare.

## The idea
For parallel polarization, $\Gamma_\parallel = (\eta_2\cos\theta_t - \eta_1\cos\theta_i)/(\eta_2\cos\theta_t + \eta_1\cos\theta_i)$ has a numerator that can vanish for the right choice of $\theta_i$. Combined with Snell's law, this picks out a unique angle.

## Formal definition
For non-magnetic media ($\mu_1=\mu_2=\mu_0$):

$$\boxed{\theta_B = \arctan\sqrt{\frac{\epsilon_2}{\epsilon_1}} = \arctan\frac{n_2}{n_1}}$$

Equivalent geometric statement: at the Brewster angle, the reflected and transmitted rays are *perpendicular* to each other ($\theta_B + \theta_t = 90°$).

For perpendicular polarization there is **no Brewster angle** in non-magnetic media — $\Gamma_\perp$ is never zero.

## Behavior near the Brewster angle
At $\theta_i = \theta_B$, $\Gamma_\parallel = 0$ and all parallel-polarized power transmits. For mixed polarization, the *reflected* wave is purely perpendicular-polarized — the reflection acts as a polarizer.

## Why it matters / when you use it
- **Anti-glare coatings, polarized sunglasses, photography polarizing filters.**
- **Brewster windows** in laser cavities to enforce a single linear polarization with zero loss per pass.
- A polarization-purity sanity check at radar bench: tilt to Brewster angle, watch one polarization disappear.

## Common mistakes
- **Wrong polarization.** Brewster works for *parallel* (TM, $\vec{E}$ in the plane of incidence). Perpendicular (TE) reflection is never zero (in non-magnetic media).
- **Using $\sin$ instead of $\tan$.** The formula is $\arctan$, not $\arcsin$.
- **Ignoring direction.** $\theta_B$ from medium 1 to 2 satisfies $\arctan(n_2/n_1)$; from 2 to 1 it's $\arctan(n_1/n_2)$ — they sum to $90°$.

## Related
- [[snells-law]] — $\Gamma_\parallel$ formulas
- [[fresnel-coefficients]] — normal-incidence baseline
- [[total-internal-reflection]] — opposite extreme ($|\Gamma| = 1$)
- [[wave-polarization]] — what "parallel" vs "perpendicular" means
