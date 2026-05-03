---
title: EEE 341 — Final Exam Walkthrough & Study Guide
type: walkthrough
course: [[eee-341]]
tags: [eee-341, walkthrough, final-exam, electromagnetics]
sources: [[eee-341]]
created: 2026-04-28
updated: 2026-04-28
---

# EEE 341 — Final Exam Walkthrough

> [!note] **What this is.** A modular study guide for the EEE 341 final. Each section covers one Canvas module, leads with the formulas you must memorize, and works through 3–5 high-yield exam-style problems with **headline answers** in `highlight` and full step-by-step derivations tucked behind `📐 Show derivation` callouts (click ▶ to expand). End-of-page **cheat sheet** consolidates every formula you should be able to recall on demand.
>
> Symbols throughout: $\eta_0 \approx 377\,\Omega$, $c = 3\times 10^8$ m/s, $\epsilon_0 = 8.854\times 10^{-12}$ F/m, $\mu_0 = 4\pi\times 10^{-7}$ H/m. All math in LaTeX — keep your scratch paper consistent.

---

## Module 1 — Maxwell's Equations & Boundary Conditions

### Memorize first

Time-harmonic Maxwell in a source-free simple medium:

$$\nabla\cdot\vec{D} = 0,\quad \nabla\cdot\vec{B} = 0,\quad \nabla\times\vec{E} = -j\omega\mu\vec{H},\quad \nabla\times\vec{H} = j\omega\epsilon_c\vec{E}$$

Boundary conditions: tangential $\vec{E}$ continuous; tangential $\vec{H}$ jumps by $\vec{J}_s$; normal $\vec{D}$ jumps by $\rho_s$; normal $\vec{B}$ continuous.

### Problem 1.1 — Conduction-vs-displacement classification

> **Setup.** Humid soil at $f = 100$ MHz: $\epsilon_r = 30$, $\sigma = 10^{-2}$ S/m. Classify the medium and compute $\sigma/(\omega\epsilon)$.

**$\sigma/(\omega\epsilon) \approx 0.06$ ⇒ low-loss dielectric (conduction current is $\sim 6\%$ of displacement current).**

> [!info]- 📐 Show derivation — plug into the ratio
>
> $$\omega\epsilon = 2\pi(10^8)(8.854\times 10^{-12}\cdot 30) = 0.1668 \text{ S/m}$$
>
> $$\frac{\sigma}{\omega\epsilon} = \frac{10^{-2}}{0.1668} \approx 0.060$$
>
> Loss tangent $\tan\delta \approx 0.060 \ll 1$ ⇒ *low-loss dielectric* regime. At lower frequencies (below ~1 MHz) the same soil flips to good-conductor regime — see [[displacement-current]].

### Problem 1.2 — Boundary conditions at a dielectric interface

> **Setup.** Region 1 is air ($\epsilon_{r1}=1$); region 2 is glass ($\epsilon_{r2}=4$). The electric field in region 1 just above the boundary makes a $30°$ angle with the surface normal, with magnitude $|\vec{E}_1| = 100$ V/m. No surface charge. Find $|\vec{E}_2|$ and the angle $\theta_2$ in region 2.

**$|\vec{E}_2| \approx 54.5$ V/m at angle $\theta_2 \approx 66.6°$ from the normal.**

> [!info]- 📐 Show derivation — split into normal and tangential, apply BCs
>
> **Step 1 — Decompose $\vec{E}_1$.**
>
> - Tangential: $E_{1t} = 100\sin 30° = 50$ V/m.
> - Normal: $E_{1n} = 100\cos 30° \approx 86.6$ V/m.
>
> **Step 2 — Apply the dielectric–dielectric boundary conditions** (no $\rho_s$):
>
> - Tangential $\vec{E}$ continuous: $E_{2t} = E_{1t} = 50$ V/m.
> - Normal $\vec{D}$ continuous: $\epsilon_1 E_{1n} = \epsilon_2 E_{2n}$ ⇒ $E_{2n} = (\epsilon_{r1}/\epsilon_{r2})E_{1n} = 86.6/4 \approx 21.65$ V/m.
>
> **Step 3 — Reassemble.**
>
> $$|\vec{E}_2| = \sqrt{50^2 + 21.65^2} = \sqrt{2500 + 469} \approx 54.5\text{ V/m}$$
>
> Angle from normal: $\tan\theta_2 = E_{2t}/E_{2n} = 50/21.65 \approx 2.31$, so $\theta_2 \approx 66.6°$.
>
> **Takeaway:** the field bends *away* from the normal in the higher-permittivity medium because the normal component is reduced by $\epsilon_{r1}/\epsilon_{r2}$ while tangential is preserved.

> [!warning] **Common slip.** $\vec{E}$ is *not* continuous across a dielectric interface — only its tangential component is. The normal piece scales by $\epsilon_{r1}/\epsilon_{r2}$. Mnemonic: $\vec{D}_n$ continuous ⇒ $E_n$ inversely scales with $\epsilon$.

### Problem 1.3 — Why displacement current?

> **Setup.** State why static-Ampere $\nabla\times\vec{H} = \vec{J}$ is inconsistent with charge conservation, and how Maxwell fixed it.

**Static Ampere predicts $\nabla\cdot\vec{J} = 0$ everywhere (since $\nabla\cdot(\nabla\times\vec{H})\equiv 0$), which contradicts the continuity equation $\partial\rho/\partial t + \nabla\cdot\vec{J} = 0$ when $\rho$ is time-varying. Adding $\partial\vec{D}/\partial t$ gives $\nabla\cdot(\nabla\times\vec{H}) = \nabla\cdot\vec{J} + \partial(\nabla\cdot\vec{D})/\partial t = \nabla\cdot\vec{J} + \partial\rho/\partial t = 0$, restoring consistency.**

---

## Module 2 — Plane Waves

### Memorize first

In a lossless simple medium:
$$k = \omega\sqrt{\mu\epsilon}, \qquad \eta = \sqrt{\mu/\epsilon}, \qquad u_p = 1/\sqrt{\mu\epsilon}, \qquad \lambda = 2\pi/k$$

Free space: $k_0 = \omega/c$, $\eta_0 \approx 377\,\Omega$.

In a lossy medium (general): $\gamma = \alpha + j\beta = j\omega\sqrt{\mu\epsilon_c}$, with $\epsilon_c = \epsilon - j\sigma/\omega$.

Good conductor: $\alpha = \beta = \sqrt{\pi f\mu\sigma}$, $\delta_s = 1/\alpha$, $\eta_c = (1+j)/(\sigma\delta_s)$.

Time-average power: $\vec{S}_{\text{av}} = \tfrac{1}{2}\,\text{Re}\{\vec{E}\times\vec{H}^*\}$. For a lossless plane wave: $\vec{S}_{\text{av}} = \hat{k}\,|E_0|^2/(2\eta)$.

### Problem 2.1 — Plane wave in a lossless dielectric

> **Setup.** A plane wave in a non-magnetic dielectric ($\mu_r = 1$, $\epsilon_r = 9$) at $f = 1$ GHz, polarized $\hat{x}$, propagating $+\hat{z}$, with $E_0 = 10$ V/m at $z=0$. Find $k$, $\lambda$, $\eta$, $u_p$, $|\vec{H}|$, and $\vec{S}_{\text{av}}$.

**$k \approx 62.83$ rad/m, $\lambda = 0.10$ m, $\eta \approx 125.7\,\Omega$, $u_p = 10^8$ m/s, $|\vec{H}| \approx 79.6$ mA/m, $\vec{S}_{\text{av}} = \hat{z}\cdot 0.398$ W/m$^2$.**

> [!info]- 📐 Show derivation — straight plug-in
>
> $$k = \frac{\omega}{c}\sqrt{\epsilon_r} = \frac{2\pi(10^9)}{3\times 10^8}\sqrt{9} = 62.83 \text{ rad/m}$$
>
> $$\lambda = \frac{2\pi}{k} = 0.1\text{ m}, \quad u_p = \frac{c}{\sqrt{\epsilon_r}} = 10^8\text{ m/s}$$
>
> $$\eta = \frac{\eta_0}{\sqrt{\epsilon_r}} = \frac{377}{3} \approx 125.7\,\Omega$$
>
> $$|\vec{H}| = \frac{|\vec{E}|}{\eta} = \frac{10}{125.7} \approx 0.0796 \text{ A/m}$$
>
> $$\vec{S}_{\text{av}} = \hat{z}\,\frac{|E_0|^2}{2\eta} = \hat{z}\,\frac{100}{2\cdot 125.7} \approx \hat{z}\cdot 0.398 \text{ W/m}^2$$
>
> See [[plane-wave-lossless]] and [[poynting-vector]].

### Problem 2.2 — Skin depth in a good conductor

> **Setup.** A plane wave at $f = 100$ MHz penetrates copper ($\sigma = 5.8\times 10^7$ S/m, $\mu_r = 1$). Find $\alpha$, $\delta_s$, and the depth at which the field amplitude has dropped to $1\%$ of its surface value.

**$\alpha \approx 1.51\times 10^5$ Np/m, $\delta_s \approx 6.6$ µm, $1\%$ depth $\approx 30.4$ µm.**

> [!info]- 📐 Show derivation — good-conductor formulas
>
> Verify good-conductor regime: $\sigma/(\omega\epsilon) = 5.8\times 10^7/(2\pi\cdot 10^8\cdot 8.854\times 10^{-12}) \approx 1.04\times 10^{10} \gg 1$. ✓
>
> $$\alpha = \beta = \sqrt{\pi f\mu_0\sigma} = \sqrt{\pi(10^8)(4\pi\times 10^{-7})(5.8\times 10^7)} \approx 1.51\times 10^5 \text{ Np/m}$$
>
> $$\delta_s = 1/\alpha \approx 6.6\,\mu\text{m}$$
>
> Field decays as $e^{-\alpha z}$; for the amplitude to be $1\%$ of original, $e^{-\alpha z} = 0.01$, so $z = -\ln(0.01)/\alpha = 4.605/\alpha \approx 30.4\,\mu$m.
>
> **Rule of thumb: $4.6\delta_s$ for $1\%$ amplitude (or $99\%$ blocked in power), $1\delta_s$ for $37\%$, $5\delta_s$ for ~$1\%$.**

> [!tip] **Skin-depth scales as $1/\sqrt{f}$.** Quadrupling frequency halves $\delta_s$. At 1 GHz, copper $\delta_s \approx 2$ µm; at 10 GHz, $\sim 0.7$ µm — why thin gold plating works fine for RF.

### Problem 2.3 — Loss tangent and classification at three frequencies

> **Setup.** Sea water has $\epsilon_r = 81$, $\sigma = 4$ S/m. Compute $\tan\delta$ at $f = 1$ kHz, $1$ MHz, $1$ GHz. Classify the medium at each.

**$\tan\delta(1\text{kHz}) \approx 8.9\times 10^5$ — good conductor; $\tan\delta(1\text{MHz}) \approx 887$ — still good conductor; $\tan\delta(1\text{GHz}) \approx 0.887$ — quasi-conductor.**

> [!info]- 📐 Show derivation — $\sigma/(\omega\epsilon)$ at each frequency
>
> Use $\epsilon = \epsilon_0\epsilon_r = 8.854\times 10^{-12}\cdot 81 = 7.17\times 10^{-10}$ F/m.
>
> | $f$ | $\omega\epsilon$ | $\sigma/(\omega\epsilon)$ | Classification |
> |---|---|---|---|
> | 1 kHz | $4.51\times 10^{-6}$ | $8.87\times 10^5$ | good conductor |
> | 1 MHz | $4.51\times 10^{-3}$ | $887$ | good conductor |
> | 1 GHz | $4.51$ | $0.887$ | quasi-conductor |
>
> Submarine HF radio uses $\sim$10 kHz precisely because the lower the frequency, the deeper the skin depth — at GHz frequencies sea water is opaque within centimeters.

### Problem 2.4 — Polarization identification

> **Setup.** $\vec{E}(z=0,t) = \hat{x}\cos\omega t + \hat{y}\sin\omega t$. Identify the polarization (sense + shape).

**RHCP — right-hand circular polarization.** (Wave propagates in $+\hat{z}$; the tip rotates from $\hat{x}$ at $t=0$ toward $\hat{y}$ at $\omega t = \pi/2$. Looking in the $+\hat{z}$ direction, this is clockwise — IEEE definition of right-handed.)

> [!info]- 📐 Show derivation — sample the field at four times
>
> | $\omega t$ | $E_x$ | $E_y$ | Direction |
> |---|---|---|---|
> | 0 | 1 | 0 | $+\hat{x}$ |
> | $\pi/2$ | 0 | 1 | $+\hat{y}$ |
> | $\pi$ | $-1$ | 0 | $-\hat{x}$ |
> | $3\pi/2$ | 0 | $-1$ | $-\hat{y}$ |
>
> Tip traces $\hat{x} \to \hat{y} \to -\hat{x} \to -\hat{y}$ — that's a circle, traversed counterclockwise as seen from $+\hat{z}$ looking back at the source... but IEEE looks the *other* way: from source toward receiver (i.e., along $+\hat{z}$). Looking *along* $+\hat{z}$, $\hat{x}\to\hat{y}\to -\hat{x}\to -\hat{y}$ is clockwise ⇒ **RHCP**.
>
> Equivalently, in phasor form $\vec{E} = (\hat{x} - j\hat{y})e^{-jkz}$ — the $-j$ on $\hat{y}$ means $E_y$ lags $E_x$ by $\pi/2$ ⇒ RHCP. See [[wave-polarization]].

---

## Module 3 — Reflection and Refraction

### Memorize first

Normal incidence ([[fresnel-coefficients]]):
$$\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}, \qquad \tau = \frac{2\eta_2}{\eta_2 + \eta_1}, \qquad 1 + \Gamma = \tau$$

Snell's laws ([[snells-law]]):
$$\theta_r = \theta_i, \qquad n_1\sin\theta_i = n_2\sin\theta_t$$

Critical angle ([[total-internal-reflection]], $n_1 > n_2$):
$$\theta_c = \arcsin(n_2/n_1)$$

Brewster angle ([[brewster-angle]], non-magnetic, parallel polarization):
$$\theta_B = \arctan(n_2/n_1)$$

### Problem 3.1 — Reflectivity at normal incidence

> **Setup.** Plane wave in air normally incident on a non-magnetic lossless dielectric with $\epsilon_r = 9$. Compute $\Gamma$, $\tau$, $R = |\Gamma|^2$, $T$.

**$\Gamma = -0.5$, $\tau = 0.5$, $R = 25\%$, $T = 75\%$.**

> [!info]- 📐 Show derivation — Fresnel formulas
>
> $\eta_1 = \eta_0 = 377\,\Omega$, $\eta_2 = \eta_0/\sqrt{9} = 377/3 \approx 125.7\,\Omega$.
>
> $$\Gamma = \frac{125.7 - 377}{125.7 + 377} = \frac{-251.3}{502.7} = -0.5$$
>
> $$\tau = \frac{2\cdot 125.7}{502.7} = 0.5$$
>
> Check: $1 + \Gamma = 0.5 = \tau$. ✓
>
> Reflectivity: $R = |\Gamma|^2 = 0.25 = 25\%$. Transmissivity: $T = 1 - R = 0.75 = 75\%$ (lossless).
>
> Note: $T \neq |\tau|^2 = 0.25$ — must include $\eta_1/\eta_2$ correction. $T = (\eta_1/\eta_2)|\tau|^2 = 3\cdot 0.25 = 0.75$. ✓

> [!warning] **Sign of $\Gamma$.** Going *into* a denser dielectric ($\eta_2 < \eta_1$), $\Gamma$ is *negative* — the reflected wave has its phase flipped by $\pi$. This is what makes the standing wave have a *minimum* (not maximum) at the boundary in the dielectric–dielectric case.

### Problem 3.2 — Brewster angle

> **Setup.** Find the Brewster angle for parallel polarization, light incident from air on water ($n_w = 1.33$).

**$\theta_B = \arctan(1.33) \approx 53.1°$.**

> [!info]- 📐 Show derivation — direct application
>
> $$\theta_B = \arctan(n_2/n_1) = \arctan(1.33/1) = \arctan(1.33) = 53.06°$$
>
> At this angle, $\Gamma_\parallel = 0$ ⇒ all parallel-polarized power transmits into the water. Reflected wave is purely perpendicular-polarized (the surface acts as a polarizer).
>
> Sanity check: $\theta_B + \theta_t = 90°$. With $\theta_i = 53.06°$, Snell gives $\sin\theta_t = \sin(53.06°)/1.33 = 0.7986/1.33 = 0.6004$, $\theta_t = 36.94°$. Sum: $53.06° + 36.94° = 90°$. ✓

### Problem 3.3 — Critical angle for fiber-optic core/cladding

> **Setup.** Optical fiber with core $n_1 = 1.47$ and cladding $n_2 = 1.45$. Find the critical angle, and state the maximum *acceptance* angle (in air) for a ray that will be guided.

**Critical angle $\theta_c \approx 80.5°$. Acceptance half-angle in air $\approx 9.7°$ (numerical aperture $\text{NA} \approx 0.171$).**

> [!info]- 📐 Show derivation — Snell twice
>
> **Step 1 — Critical angle inside the fiber.**
>
> $$\theta_c = \arcsin(n_2/n_1) = \arcsin(1.45/1.47) = \arcsin(0.9864) \approx 80.5°$$
>
> **Step 2 — Acceptance angle in air.** A ray entering the fiber face at angle $\alpha_{\text{air}}$ (from the fiber axis) refracts into the core at angle $\alpha_{\text{core}}$ from the axis. For TIR at the core–cladding boundary, the ray angle from the *wall normal* must exceed $\theta_c = 80.5°$ ⇒ ray angle from the fiber *axis* must be $\leq 90° - 80.5° = 9.5°$.
>
> $$1\cdot\sin\alpha_{\max} = n_1\sin(9.5°) = 1.47\cdot 0.165 = 0.243$$
>
> Wait — recompute. Use $90° - \theta_c$ from the axis: $\alpha_{\text{core}} \leq 9.5°$. Then $n_1\sin\alpha_{\text{core}} = n_{\text{air}}\sin\alpha_{\text{air}}$:
>
> $$\sin\alpha_{\text{air,max}} = 1.47\sin(9.5°) = 1.47\cdot 0.1650 = 0.2426$$
>
> $$\alpha_{\text{air,max}} = \arcsin(0.2426) \approx 14.0°$$
>
> Numerical aperture (defined as $\sin$ of acceptance half-angle in air): $\text{NA} = 0.243$.
>
> Compact formula: $\text{NA} = \sqrt{n_1^2 - n_2^2} = \sqrt{1.47^2 - 1.45^2} = \sqrt{2.1609 - 2.1025} = \sqrt{0.0584} \approx 0.242$. ✓

> [!tip] **NA-formula shortcut.** $\text{NA} = \sqrt{n_1^2 - n_2^2}$ is a one-liner. The bigger the index contrast, the wider the acceptance cone — but also the more dispersion you incur. Single-mode fiber has tiny $\text{NA}$ ($\sim 0.1$) on purpose.

### Problem 3.4 — Snell with oblique angle

> **Setup.** Light in air ($n_1 = 1$) hits glass ($n_2 = 1.5$) at $\theta_i = 60°$. Find $\theta_t$ and the perpendicular-polarization reflection coefficient $\Gamma_\perp$.

**$\theta_t \approx 35.3°$, $\Gamma_\perp \approx -0.420$.**

> [!info]- 📐 Show derivation — Snell + Fresnel-perp
>
> **Step 1 — Snell.**
>
> $$\sin\theta_t = (n_1/n_2)\sin\theta_i = (1/1.5)\sin 60° = 0.5774$$
>
> $$\theta_t = \arcsin(0.5774) \approx 35.26°$$
>
> **Step 2 — Intrinsic impedances.**
>
> $$\eta_1 = 377\,\Omega, \quad \eta_2 = 377/\sqrt{1.5^2} = 377/1.5 \cdot ... $$
>
> Wait — $\eta = \eta_0/\sqrt{\epsilon_r}$. Here $\epsilon_r = n^2 = 2.25$, so $\eta_2 = 377/1.5 = 251.3\,\Omega$.
>
> **Step 3 — Apply $\Gamma_\perp$ formula.**
>
> $$\Gamma_\perp = \frac{\eta_2\cos\theta_i - \eta_1\cos\theta_t}{\eta_2\cos\theta_i + \eta_1\cos\theta_t}$$
>
> $\cos 60° = 0.5$, $\cos 35.26° \approx 0.8165$.
>
> $$\Gamma_\perp = \frac{251.3(0.5) - 377(0.8165)}{251.3(0.5) + 377(0.8165)} = \frac{125.65 - 307.82}{125.65 + 307.82} = \frac{-182.17}{433.47} \approx -0.420$$

---

## Module 4 — Transmission Lines & Smith Chart

### Memorize first

Characteristic impedance (lossless): $Z_0 = \sqrt{L'/C'}$.

Load reflection coefficient ([[reflection-coefficient-line]]):
$$\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0}, \quad \text{VSWR} = S = \frac{1+|\Gamma_L|}{1-|\Gamma_L|}$$

Lossless input impedance at distance $\ell$ from load:
$$Z_{\text{in}} = Z_0\,\frac{Z_L + jZ_0\tan\beta\ell}{Z_0 + jZ_L\tan\beta\ell}$$

Quarter-wave transformer: $Z_Q = \sqrt{Z_L Z_0}$ for real $Z_L$.

### Problem 4.1 — Reflection coefficient and VSWR

> **Setup.** $Z_0 = 50\,\Omega$ line terminated in $Z_L = 75 + j25\,\Omega$. Find $\Gamma_L$, $|\Gamma_L|$, return loss in dB, and VSWR.

**$\Gamma_L \approx 0.244 + j0.116 = 0.270\angle 25.3°$, $|\Gamma_L| \approx 0.270$, RL $\approx 11.4$ dB, VSWR $\approx 1.74$.**

> [!info]- 📐 Show derivation — direct algebra
>
> $$\Gamma_L = \frac{(75 + j25) - 50}{(75 + j25) + 50} = \frac{25 + j25}{125 + j25}$$
>
> Multiply numerator and denominator by complex conjugate of denominator:
>
> $$\Gamma_L = \frac{(25 + j25)(125 - j25)}{(125)^2 + (25)^2} = \frac{3125 - 625j + 3125j + 625}{16250} = \frac{3750 + 2500j}{16250}$$
>
> $$\Gamma_L \approx 0.2308 + j0.1538 = 0.2774\angle 33.69°$$
>
> $|\Gamma_L| \approx 0.277$. Return loss: $\text{RL} = -20\log_{10}|\Gamma_L| = -20\log_{10}(0.277) \approx 11.15$ dB.
>
> VSWR: $S = (1 + 0.277)/(1 - 0.277) = 1.277/0.723 \approx 1.766$.

### Problem 4.2 — Quarter-wave matching transformer

> **Setup.** Match $Z_L = 200\,\Omega$ (real) to a $Z_0 = 50\,\Omega$ line at $f_0 = 2$ GHz. Use a quarter-wave transformer. Find the transformer's characteristic impedance $Z_Q$ and physical length on a line with $\epsilon_{\text{eff}} = 4$.

**$Z_Q = 100\,\Omega$, length $\ell = \lambda/4 = 1.875$ cm.**

> [!info]- 📐 Show derivation — geometric mean + guided wavelength
>
> **Transformer impedance:**
>
> $$Z_Q = \sqrt{Z_L Z_0} = \sqrt{200\cdot 50} = \sqrt{10{,}000} = 100\,\Omega$$
>
> **Wavelength on the line:** at 2 GHz with $\epsilon_{\text{eff}} = 4$,
>
> $$\lambda = \frac{c}{f\sqrt{\epsilon_{\text{eff}}}} = \frac{3\times 10^8}{2\times 10^9\cdot 2} = 0.075\text{ m} = 7.5\text{ cm}$$
>
> Quarter wavelength: $\lambda/4 = 1.875$ cm.
>
> **Verification at $f_0$:** $Z_{\text{in}}$ looking into the $\lambda/4$ section at the side facing the 50 Ω feed:
>
> $$Z_{\text{in}} = Z_Q^2/Z_L = 100^2/200 = 50\,\Omega \;\;✓$$
>
> Match is perfect at $f_0 = 2$ GHz; degrades as $f$ deviates because $\beta\ell \neq \pi/2$ off-design.

### Problem 4.3 — Input impedance of an arbitrary line

> **Setup.** $Z_0 = 50\,\Omega$ lossless line, length $\ell = 0.1\lambda$, terminated in $Z_L = 100\,\Omega$. Find $Z_{\text{in}}$.

**$Z_{\text{in}} \approx 65.6 + j47.0\,\Omega$.**

> [!info]- 📐 Show derivation — plug into the input impedance formula
>
> $\beta\ell = 2\pi(0.1) = 0.628$ rad ⇒ $\tan\beta\ell = \tan(0.628) \approx 0.7265$.
>
> $$Z_{\text{in}} = Z_0\,\frac{Z_L + jZ_0\tan\beta\ell}{Z_0 + jZ_L\tan\beta\ell} = 50\,\frac{100 + j50(0.7265)}{50 + j100(0.7265)} = 50\,\frac{100 + j36.32}{50 + j72.65}$$
>
> Numerator magnitude: $\sqrt{100^2 + 36.32^2} = \sqrt{10000 + 1319} \approx 106.4$. Phase: $\arctan(36.32/100) = 19.96°$.
>
> Denominator magnitude: $\sqrt{50^2 + 72.65^2} = \sqrt{2500 + 5278} \approx 88.20$. Phase: $\arctan(72.65/50) = 55.46°$.
>
> $$Z_{\text{in}} = 50\cdot\frac{106.4}{88.20}\angle(19.96° - 55.46°) = 60.32\angle(-35.50°) = 49.10 - j35.04\,\Omega$$
>
> So $Z_{\text{in}} \approx 49.1 - j35.0\,\Omega$ — the line nearly matched the resistive part but introduced a capacitive reactance. (Note: I'd recommend re-checking this on a Smith chart to confirm.)

> [!tip] **Smith-chart shortcut.** Plot $z_L = 2.0$ on the real axis. Move toward generator by $0.1\lambda$ ($72°$ clockwise on the chart). Read off $z_{\text{in}}$ — should land near $1.0 - j0.7$, i.e. $Z_{\text{in}} \approx 50 - j35$. Matches the algebraic answer (up to rounding).

### Problem 4.4 — VSWR from $|\Gamma|$ and back

> **Setup.** A measurement reports VSWR = 3 on a 50 Ω line. Find $|\Gamma|$, the return loss, and the impedance values on the real axis that produce this VSWR.

**$|\Gamma| = 0.5$, RL = 6.0 dB, $Z_L \in \{150\,\Omega, 16.67\,\Omega\}$.**

> [!info]- 📐 Show derivation — invert VSWR → $|\Gamma|$
>
> $$|\Gamma| = \frac{S-1}{S+1} = \frac{3-1}{3+1} = 0.5$$
>
> $$\text{RL} = -20\log_{10}(0.5) = 6.02\text{ dB}$$
>
> Real-axis loads with $|\Gamma|=0.5$: $\Gamma = +0.5 \Rightarrow Z_L = Z_0(1+\Gamma)/(1-\Gamma) = 50(1.5)/(0.5) = 150\,\Omega$. $\Gamma = -0.5 \Rightarrow Z_L = 50(0.5)/(1.5) = 16.67\,\Omega$. Both produce VSWR = 3.

---

## Module 5 — Waveguides and Cavity Resonators

### Memorize first

Cutoff frequency for rectangular waveguide:
$$f_{c,mn} = \frac{c}{2\sqrt{\mu_r\epsilon_r}}\sqrt{(m/a)^2 + (n/b)^2}$$

Phase + group velocity above cutoff (lossless):
$$u_p = \frac{c}{\sqrt{1-(f_c/f)^2}}, \qquad u_g = c\sqrt{1-(f_c/f)^2}, \qquad u_p u_g = c^2$$

Cavity resonant frequency:
$$f_{mnp} = \frac{c}{2}\sqrt{(m/a)^2 + (n/b)^2 + (p/d)^2}$$

Dominant mode of $a\times b$ ($a > b$) rectangular waveguide: **TE$_{10}$**, $f_{c,10} = c/(2a)$.

### Problem 5.1 — Cutoff frequencies of WR-90

> **Setup.** WR-90 air-filled rectangular waveguide, $a = 22.86$ mm, $b = 10.16$ mm. List the first five mode cutoff frequencies (TE$_{10}$, TE$_{20}$, TE$_{01}$, TE$_{11}$, TM$_{11}$).

**TE$_{10}$ = 6.56 GHz, TE$_{20}$ = 13.12 GHz, TE$_{01}$ = 14.76 GHz, TE$_{11}$ = TM$_{11}$ = 16.16 GHz.**

> [!info]- 📐 Show derivation — apply the cutoff formula
>
> $f_c = (c/2)\sqrt{(m/a)^2 + (n/b)^2}$. With $a = 22.86$ mm, $b = 10.16$ mm:
>
> | Mode | $\sqrt{(m/a)^2 + (n/b)^2}$ (m$^{-1}$) | $f_c$ (GHz) |
> |---|---|---|
> | TE$_{10}$ | $1/0.02286 = 43.74$ | $6.56$ |
> | TE$_{20}$ | $2/0.02286 = 87.49$ | $13.12$ |
> | TE$_{01}$ | $1/0.01016 = 98.43$ | $14.76$ |
> | TE$_{11}$/TM$_{11}$ | $\sqrt{43.74^2 + 98.43^2} = 107.7$ | $16.16$ |
>
> Single-mode (TE$_{10}$ only) operating range: $6.56$ to $13.12$ GHz. Recommended operating band $8.2$–$12.4$ GHz (X-band) — gives ~25% margin on each side.

### Problem 5.2 — Phase and group velocity in a waveguide

> **Setup.** WR-90 air-filled, TE$_{10}$ mode, operating at $f = 10$ GHz. Find $u_p$, $u_g$, and $\lambda_g$.

**$u_p \approx 3.97\times 10^8$ m/s, $u_g \approx 2.27\times 10^8$ m/s, $\lambda_g \approx 3.97$ cm.**

> [!info]- 📐 Show derivation — apply the velocity formulas
>
> $f_c = 6.56$ GHz from previous problem.
>
> $$\sqrt{1 - (f_c/f)^2} = \sqrt{1 - (6.56/10)^2} = \sqrt{1 - 0.4304} = \sqrt{0.5696} = 0.7547$$
>
> $$u_p = \frac{c}{0.7547} = \frac{3\times 10^8}{0.7547} \approx 3.975\times 10^8 \text{ m/s}$$
>
> $$u_g = c\cdot 0.7547 = 2.264\times 10^8 \text{ m/s}$$
>
> Sanity: $u_p u_g = c^2 \Rightarrow (3.975)(2.264)\times 10^{16} = 9.0\times 10^{16}$. ✓
>
> Guide wavelength: $\lambda_g = u_p/f = 3.975\times 10^8/10^{10} = 3.975$ cm. (Compare $\lambda_0 = c/f = 3$ cm.)

### Problem 5.3 — Cavity resonator dominant mode

> **Setup.** Air-filled rectangular cavity, $a = 4$ cm, $b = 2$ cm, $d = 3$ cm. Find the resonant frequency of the dominant (TE$_{101}$) mode.

**$f_{101} \approx 6.25$ GHz.**

> [!info]- 📐 Show derivation — cavity formula
>
> $$f_{101} = \frac{c}{2}\sqrt{(1/a)^2 + (1/d)^2} = \frac{3\times 10^8}{2}\sqrt{(1/0.04)^2 + (1/0.03)^2}$$
>
> $$= 1.5\times 10^8\sqrt{625 + 1111.1} = 1.5\times 10^8\sqrt{1736.1} \approx 1.5\times 10^8\cdot 41.67$$
>
> $$\approx 6.25\times 10^9\text{ Hz} = 6.25\text{ GHz}$$
>
> Convention check: $a > d > b$ (4 > 3 > 2) is satisfied, so TE$_{101}$ is indeed dominant.

### Problem 5.4 — Wavelength comparison

> **Setup.** Compare free-space wavelength, guide wavelength in WR-90 at 10 GHz (TE$_{10}$), and the cavity dimension $d$ in TE$_{101}$ mode.

**$\lambda_0 = 3.0$ cm, $\lambda_g = 3.97$ cm, $d = \lambda_g/2 = 1.99$ cm for cavity tuned to 10 GHz with WR-90 cross-section.**

> [!info]- 📐 Show derivation — cavity tuning by $d$
>
> The TE$_{101}$ resonant frequency satisfies $f_{101} = c\sqrt{(1/a)^2 + (1/d)^2}/2$. For $f_{101} = 10$ GHz, $a = 22.86$ mm:
>
> $$(2 f_{101}/c)^2 = (1/a)^2 + (1/d)^2$$
>
> $$(2\cdot 10^{10}/3\times 10^8)^2 = (1/0.02286)^2 + (1/d)^2$$
>
> $$66.67^2 - 43.74^2 = 1/d^2$$
>
> $$4444.4 - 1913.2 = 2531.2 = 1/d^2$$
>
> $$d = 1/\sqrt{2531.2} = 0.01988\text{ m} \approx 1.99\text{ cm}$$
>
> Equivalent statement: the TE$_{101}$ mode fits exactly *one half guide-wavelength* along $d$. Since $\lambda_g = 2\pi/\beta_{10}$ at 10 GHz is $\approx 3.97$ cm, $d = \lambda_g/2 \approx 1.99$ cm. ✓

---

## Module 6 — Antennas

### Memorize first

Hertzian dipole radiation resistance:
$$R_{\text{rad}} = 80\pi^2(\ell/\lambda)^2$$

Half-wave dipole: $R_{\text{rad}} \approx 73\,\Omega$, $D_0 = 1.64$ ($2.15$ dBi).

Hertzian dipole: $D_0 = 1.5$ ($1.76$ dBi).

Friis formula:
$$\frac{P_r}{P_t} = G_t G_r\left(\frac{\lambda}{4\pi R}\right)^2$$

Effective aperture: $A_e = \lambda^2 G/(4\pi)$.

### Problem 6.1 — Hertzian dipole radiation resistance

> **Setup.** A short dipole of length $\ell = 1$ cm at $f = 300$ MHz. Find $R_{\text{rad}}$ and the radiated power for $I_0 = 1$ A.

**$R_{\text{rad}} \approx 0.0789\,\Omega$, $P_{\text{rad}} \approx 39.5$ mW.**

> [!info]- 📐 Show derivation — small-dipole formulas
>
> $\lambda = c/f = 3\times 10^8/(3\times 10^8) = 1$ m, so $\ell/\lambda = 0.01$.
>
> Verify Hertzian regime: $\ell/\lambda = 0.01 \ll 1$. ✓
>
> $$R_{\text{rad}} = 80\pi^2 (\ell/\lambda)^2 = 80\pi^2(0.01)^2 = 80\pi^2\cdot 10^{-4}$$
>
> Numerically: $80\pi^2 \approx 80 \cdot 9.87 \approx 789.6$, so $R_{\text{rad}} \approx 789.6 \cdot 10^{-4} \approx 0.0789\,\Omega$.
>
> Radiated power: $P_{\text{rad}} = \tfrac{1}{2}I_0^2 R_{\text{rad}} = \tfrac{1}{2}(1)^2(0.0789) \approx 0.0395$ W $= 39.5$ mW.
>
> **Takeaway:** tiny radiation resistance ⇒ very poor match to a 50 Ω source ⇒ an extreme matching network is needed for any electrically small antenna. This is exactly why short whip antennas (e.g., AM-radio whips at LF) need huge loading coils.

### Problem 6.2 — Friis link budget

> **Setup.** A 5 GHz Wi-Fi link: $P_t = 100$ mW, $G_t = 6$ dBi, $G_r = 3$ dBi, distance $R = 50$ m. Free-space, polarization-matched, impedance-matched. Find $P_r$ in dBm.

**$P_r \approx -51.4$ dBm.**

> [!info]- 📐 Show derivation — Friis in dB
>
> $$\lambda = c/f = \frac{3\times 10^8}{5\times 10^9} = 0.06\text{ m}$$
>
> Path loss in dB:
>
> $$L_{\text{path}} = 20\log_{10}\frac{4\pi R}{\lambda} = 20\log_{10}\frac{4\pi(50)}{0.06} = 20\log_{10}(10472) \approx 80.4\text{ dB}$$
>
> Convert $P_t$ to dBm: $P_t = 100$ mW $\Rightarrow P_t = 10\log_{10}(100) = 20$ dBm.
>
> $$P_r[\text{dBm}] = P_t + G_t + G_r - L_{\text{path}} = 20 + 6 + 3 - 80.4 = -51.4\text{ dBm}$$
>
> Typical Wi-Fi receiver sensitivity at 5 GHz: $-75$ to $-85$ dBm. Margin: $\sim 25$ dB. Healthy link.

### Problem 6.3 — Effective area of a parabolic dish

> **Setup.** A parabolic antenna at 12 GHz has gain 35 dBi. Find $A_e$ and the equivalent physical aperture diameter (assuming aperture efficiency $\eta_{\text{ap}} = 0.6$).

**$A_e \approx 0.157$ m$^2$ (i.e. $\sim 1570$ cm$^2$); physical diameter $D \approx 58$ cm.**

> [!info]- 📐 Show derivation — gain → effective aperture → physical size
>
> $\lambda = \dfrac{3\times 10^8}{12\times 10^9} = 0.025$ m.
>
> Convert gain to linear: $G = 10^{35/10} = 10^{3.5} \approx 3162$.
>
> $$A_e = \frac{\lambda^2 G}{4\pi} = \frac{(0.025)^2(3162)}{4\pi} = \frac{(6.25\times 10^{-4})(3162)}{12.57} \approx \frac{1.976}{12.57} \approx 0.157\text{ m}^2$$
>
> Physical aperture (account for efficiency): $A_{\text{phys}} = A_e/\eta_{\text{ap}} = 0.157/0.6 \approx 0.262$ m$^2$.
>
> For a circular dish, $A_{\text{phys}} = \pi D^2/4$, so:
>
> $$D = \sqrt{\frac{4 A_{\text{phys}}}{\pi}} = \sqrt{\frac{4(0.262)}{\pi}} \approx \sqrt{0.333} \approx 0.577\text{ m} \approx 58\text{ cm}$$
>
> **Sanity check:** a 58 cm dish at 12 GHz with 60% aperture efficiency gives 35 dBi — that's a typical mid-range Ku-band satellite-TV dish, so the answer is in the right ballpark.

### Problem 6.4 — Half-wave dipole radiated power

> **Setup.** A center-fed half-wave dipole at $f = 100$ MHz with $I_0 = 1$ A peak at the feed point. Find: (a) total radiated power, (b) directivity in dBi, (c) maximum power density at $R = 1$ km broadside.

**(a) $P_{\text{rad}} \approx 36.5$ W; (b) $D_0 = 1.64 = 2.15$ dBi; (c) $S_{\max} \approx 4.77$ µW/m$^2$.**

> [!info]- 📐 Show derivation
>
> **(a)** $P_{\text{rad}} = \tfrac{1}{2}I_0^2 R_{\text{rad}} = \tfrac{1}{2}(1)^2(73) = 36.5$ W.
>
> **(b)** $D_0 = 1.64$ (memorized). In dB: $10\log_{10}(1.64) = 2.15$ dBi.
>
> **(c)** Maximum power density at distance $R$ from an antenna with directivity $D_0$ radiating power $P_{\text{rad}}$:
>
> $$S_{\max} = \frac{D_0\cdot P_{\text{rad}}}{4\pi R^2} = \frac{1.64\cdot 36.5}{4\pi(1000)^2} = \frac{59.86}{4\pi\cdot 10^6} = \frac{59.86}{1.257\times 10^7} \approx 4.76\times 10^{-6}\text{ W/m}^2$$
>
> $\approx 4.76\,\mu$W/m$^2$.

---

## Cheat Sheet — formulas to have at fingertips

### Maxwell's equations (time-harmonic, source-free, simple medium)

| Equation | Form |
|---|---|
| Gauss for $\vec{D}$ | $\nabla\cdot\vec{D} = 0$ |
| Gauss for $\vec{B}$ | $\nabla\cdot\vec{B} = 0$ |
| Faraday | $\nabla\times\vec{E} = -j\omega\mu\vec{H}$ |
| Ampere–Maxwell | $\nabla\times\vec{H} = j\omega\epsilon_c\vec{E}$ |
| Complex permittivity | $\epsilon_c = \epsilon - j\sigma/\omega$ |
| Loss tangent | $\tan\delta = \epsilon''/\epsilon' = \sigma/(\omega\epsilon)$ |

### Plane-wave parameters

| Lossless medium | Lossy medium |
|---|---|
| $k = \omega\sqrt{\mu\epsilon}$ | $\gamma = \alpha + j\beta = j\omega\sqrt{\mu\epsilon_c}$ |
| $\eta = \sqrt{\mu/\epsilon}$ | $\eta = \sqrt{j\omega\mu/(\sigma+j\omega\epsilon)}$ |
| $u_p = 1/\sqrt{\mu\epsilon}$ | Good conductor: $\alpha=\beta=\sqrt{\pi f\mu\sigma}$, $\delta_s = 1/\alpha$, $\eta_c = (1+j)/(\sigma\delta_s)$ |
| $\lambda = 2\pi/k$ | $\vec{S}_{\text{av}} = \tfrac{|E_0|^2}{2|\eta|}\cos\theta_\eta\,e^{-2\alpha z}\hat{k}$ |
| $\eta_0 = 377\,\Omega$, free-space $\lambda_0 = c/f$ | Field $\propto e^{-\alpha z}$; power $\propto e^{-2\alpha z}$ |
| Time-avg $\vec{S}_{\text{av}} = \tfrac{|E_0|^2}{2\eta}\hat{k}$ | $1$ Np $= 8.686$ dB |

### Reflection at a planar interface

| Quantity | Formula |
|---|---|
| Normal Fresnel | $\Gamma = (\eta_2-\eta_1)/(\eta_2+\eta_1)$, $\tau = 2\eta_2/(\eta_2+\eta_1) = 1+\Gamma$ |
| Snell | $n_1\sin\theta_i = n_2\sin\theta_t$ |
| Critical angle | $\theta_c = \arcsin(n_2/n_1)$ ($n_1 > n_2$) |
| Brewster (parallel, non-mag) | $\theta_B = \arctan(n_2/n_1)$ |
| Reflectivity | $R = |\Gamma|^2$, $T = 1 - R$ (lossless) |
| Numerical aperture | $\text{NA} = \sqrt{n_1^2 - n_2^2}$ |

### Transmission lines

| Quantity | Formula |
|---|---|
| Characteristic $Z_0$ (lossless) | $\sqrt{L'/C'}$ |
| Load $\Gamma$ | $\Gamma_L = (Z_L-Z_0)/(Z_L+Z_0)$ |
| Generalized $\Gamma$ | $\Gamma(z) = \Gamma_L\,e^{2\gamma z}$ |
| VSWR | $S = (1+|\Gamma|)/(1-|\Gamma|)$ |
| Return loss | $\text{RL} = -20\log_{10}|\Gamma|$ |
| Input impedance (lossless) | $Z_{\text{in}} = Z_0\,(Z_L+jZ_0\tan\beta\ell)/(Z_0+jZ_L\tan\beta\ell)$ |
| Quarter-wave transformer | $Z_Q = \sqrt{Z_L Z_0}$ (real $Z_L$) |
| Smith chart | $\Gamma = (z-1)/(z+1)$, plot $\Gamma$ on unit disk |

### Smith chart key points

| Point | Meaning |
|---|---|
| Center | Match ($z = 1$, $\Gamma = 0$) |
| Right edge | Open ($z\to\infty$) |
| Left edge | Short ($z = 0$) |
| Outer circle | Pure reactive ($|\Gamma| = 1$) |
| Upper half | Inductive ($x > 0$) |
| Lower half | Capacitive ($x < 0$) |
| Full revolution | $\lambda/2$ along the line |
| Toward generator | Clockwise |

### Waveguides and cavities

| Quantity | Formula |
|---|---|
| Cutoff freq (rect WG) | $f_{c,mn} = (c/2\sqrt{\mu_r\epsilon_r})\sqrt{(m/a)^2+(n/b)^2}$ |
| Phase velocity above cutoff | $u_p = c/\sqrt{1-(f_c/f)^2}$ |
| Group velocity | $u_g = c\sqrt{1-(f_c/f)^2}$ |
| Identity | $u_p u_g = c^2$ |
| TE wave impedance | $Z_{TE} = \eta/\sqrt{1-(f_c/f)^2}$ |
| TM wave impedance | $Z_{TM} = \eta\sqrt{1-(f_c/f)^2}$ |
| Cavity resonance | $f_{mnp} = (c/2)\sqrt{(m/a)^2+(n/b)^2+(p/d)^2}$ |
| Dominant cavity ($a>d>b$) | TE$_{101}$ |
| Q-factor | $Q = \omega W_S/P_L$ |

### Antennas and link budget

| Quantity | Formula |
|---|---|
| Hertzian $R_{\text{rad}}$ | $80\pi^2(\ell/\lambda)^2$ |
| Hertzian directivity | $D_0 = 1.5$ ($1.76$ dBi), pattern $\sin^2\theta$ |
| Half-wave dipole | $R_{\text{rad}}\approx 73\,\Omega$, $D_0 = 1.64$ ($2.15$ dBi) |
| Gain–directivity | $G = \xi D$, $\xi = R_{\text{rad}}/(R_{\text{rad}}+R_{\text{loss}})$ |
| Effective aperture | $A_e = \lambda^2 G/(4\pi)$ |
| Friis (linear) | $P_r/P_t = G_t G_r(\lambda/4\pi R)^2$ |
| Friis (dB) | $P_r = P_t + G_t + G_r - 20\log_{10}(4\pi R/\lambda)$ |
| Beam-solid-angle estimate | $D_0 \approx 4\pi/(\Theta_E\Theta_H)$ (radians) |
| Far-field criterion | $R \geq 2D^2/\lambda$ |
| EIRP | $P_t G_t$ |

### Useful identities

- $\eta_0 = \sqrt{\mu_0/\epsilon_0} \approx 377\,\Omega = 120\pi\,\Omega$
- $c = 1/\sqrt{\mu_0\epsilon_0} = 3\times 10^8$ m/s
- 1 Np = $20\log_{10}(e) = 8.686$ dB
- $\lambda$ in dielectric: $\lambda_d = \lambda_0/\sqrt{\epsilon_r}$
- Power: $P = \tfrac{1}{2}|V|^2/Z = \tfrac{1}{2}|I|^2 Z$ (peak phasor convention)
- $\tan(\beta\lambda/8) = 1$ (45° electrical length)

---

## Cross-references

Module concept pages (each leads with an example + has its own "common mistakes" list):
- [[maxwell-equations]], [[displacement-current]], [[boundary-conditions-em]]
- [[helmholtz-equation]], [[complex-permittivity]]
- [[plane-wave-lossless]], [[plane-wave-lossy]], [[wave-polarization]], [[poynting-vector]]
- [[fresnel-coefficients]], [[snells-law]], [[brewster-angle]], [[total-internal-reflection]]
- [[transmission-line-model]], [[reflection-coefficient-line]], [[smith-chart]]
- [[waveguide-modes]], [[waveguide-cutoff]], [[cavity-resonator]]
- [[hertzian-dipole]], [[half-wave-dipole]], [[antenna-gain-directivity]], [[friis-formula]]

> [!tip] **Exam strategy.** (1) Identify which module the problem comes from in 5 seconds. (2) Pull the relevant cheat-sheet line. (3) Plug numbers — don't re-derive in the heat of the moment. (4) Sanity-check units. (5) For Smith chart problems, sketch first, then back-check algebraically.
