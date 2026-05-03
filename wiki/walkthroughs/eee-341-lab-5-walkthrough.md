---
title: EEE 341 Lab 5 — Antenna Measurement (EZNEC) Walkthrough
type: walkthrough
course: [[eee-341]]
tags: [eee-341, lab, walkthrough, antenna, dipole, eznec, swr, array, cardioid, friis]
sources: [[homework-2026-04-28-eee-341-lab-5]]
created: 2026-04-28
updated: 2026-04-28
---

# EEE 341 Lab 5 — Antenna Measurement (EZNEC) Walkthrough

> [!note] **What this is.** A per-section walkthrough of Lab 5 (`raw/labs/eee-341-lab-5/Lab5_Manual.pdf`). For each lab task I (a) **state it** verbatim, (b) **explain the underlying concept** with cross-references to wiki concept pages, (c) walk through the **concrete EZNEC steps** to produce the deliverable, (d) give the **expected qualitative result**, and (e) include a `> [!info]- 📐 Show derivation` collapsible block when there's theory worth seeing.
>
> Submit a single PDF named `EEE341_<lastname>_Lab5.pdf` per the manual.

> [!tip] **Frequency convention.** Lab targets a **half-wave dipole at $\lambda = 1$ m**, which at the EZNEC default of $c = 2.99793 \times 10^8$ m/s corresponds to $f_0 = 299.793$ MHz. The lab manual sometimes says "300 MHz" — they mean 299.793 MHz exactly. Use the EZNEC default.

> [!warning] **Before you start.** Download EZNEC (free version) from `eznec.com`, install, then open `Dipole1.EZ` from the example library. **Save it as `HWD.EZ`** — but actually use the `HWD.EZ` file already downloaded in `raw/labs/eee-341-lab-5/HWD.EZ` to skip a manual edit. That file pre-defines the half-wave dipole geometry the lab assumes.

---

## Pre-lab conceptual question

> **Q.** Why is the electrical length of the so-called half-wave dipole actually taken to be slightly less than $\lambda/2$ at the design frequency?

### Headline answer

**End-effect foreshortening.** The fringing electric field at the wire's open ends acts like extra capacitance, which lowers the resonant frequency. To bring the actual resonance back up to the design frequency, the physical length is trimmed to about $0.95 \cdot \lambda/2 \approx 0.475\lambda$. The thicker the wire (smaller length-to-diameter ratio), the larger the shortening factor.

> [!info]- 📐 Show derivation — why an exact $\lambda/2$ wire isn't resonant
>
> A perfectly thin, infinite-conductivity dipole of length exactly $L = \lambda/2$ has input impedance
>
> $$Z_A \approx 73\,\Omega + j 42\,\Omega.$$
>
> The $+j 42\,\Omega$ reactive part says it's **slightly inductive**, *not* resonant. To make $X_A = 0$ (true resonance, $Z_A$ purely real), you have to **shorten** the wire so the standing-wave current pattern shifts to cancel the residual inductance. For a thin wire, that resonant length is approximately
>
> $$L_{\text{res}} \approx 0.475 \lambda \approx 0.95 \cdot \lambda/2.$$
>
> **Physical picture:** the open ends of the wire have intense fringe E-fields that store energy in capacitance to the surrounding space. That distributed end-capacitance is what makes the resistive resonance come in shorter than the wavelength-derived geometric length. Thicker wires have more end-capacitance, so they need more shortening; rule of thumb is ~95% for thin wire, ~93% for stubby wire.
>
> EZNEC will report the impedance at exactly $L = \lambda/2 = 0.5$ m as roughly $Z_A \approx 73 + j 42\,\Omega$. The minimum-SWR point in your sweep will land slightly *above* 300 MHz (because at exactly 300 MHz the wire is electrically slightly long, hence inductive, hence not minimum SWR).

---

## Section 3.1 — Plotting the SWR

> **Task 3.1.** Under *Setups → Frequency Sweep…* set up a frequency sweep, run it, then press the *SWR* button to view the plot.

### The concept

SWR (Standing Wave Ratio) is a single number that tells you **how well-matched** the antenna is to the feedline. See [[swr]]. For a half-wave dipole feeding a 50 Ω line:
- At resonance: $Z_A \approx 73\,\Omega$ real, $|\Gamma| \approx 0.187$, $\text{SWR} \approx 1.46$.
- Off-resonance: $Z_A$ becomes reactive, $|\Gamma|$ grows, SWR rises sharply.

The SWR-vs-frequency plot will show a **V-shape with a minimum near 300 MHz** — the antenna's natural resonance.

### Walkthrough

> [!example] **Step-by-step**
>
> **Step 1 — Open** `HWD.EZ` (the pre-supplied half-wave dipole).
>
> **Step 2 — Configure the sweep:** *Setups → Frequency Sweep…*. Suggested parameters (per Fig. 3.1 in the manual):
> - **Start frequency:** $\sim 200$ MHz
> - **Stop frequency:** $\sim 400$ MHz
> - **Step size:** $\sim 5$ MHz (40 points across the band — fast and smooth)
>
> **Step 3 — Run:** click the **Freq Swp** tab on the lower-left of the control center.
>
> **Step 4 — Plot:** click the **SWR** button. Screenshot the result for your report.

### Expected result

**A V-shaped curve with the minimum SWR (~1.4–1.5) near 300 MHz**, rising steeply on either side. The 2:1 SWR bandwidth is roughly $\pm 30$ MHz around the dip.

> [!info]- 📐 Show derivation — why SWR ≈ 1.46 at resonance
>
> At resonance, a thin-wire half-wave dipole presents an input impedance of approximately
>
> $$Z_A \approx 73\,\Omega + j\, 42\,\Omega.$$
>
> (The reactive part is finite at exactly $L = \lambda/2$; true zero-reactance resonance happens at $L \approx 0.475\lambda$, which EZNEC may report as the actual minimum-SWR point.)
>
> Connecting to a $Z_0 = 50\,\Omega$ feedline gives reflection coefficient:
>
> $$\Gamma = \frac{Z_A - Z_0}{Z_A + Z_0} = \frac{(73 - 50) + j 42}{(73 + 50) + j 42} = \frac{23 + j 42}{123 + j 42}.$$
>
> Magnitude: $|\Gamma| = \sqrt{23^2 + 42^2}/\sqrt{123^2 + 42^2} = 47.9/130.0 \approx 0.369$.
>
> $$\text{SWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|} = \frac{1.369}{0.631} \approx 2.17.$$
>
> If EZNEC reports the impedance at *exact* resonance (where $X = 0$) it'll be closer to $70\,\Omega$, giving $|\Gamma| \approx 0.167$ and SWR $\approx 1.40$. Either way, you should see a low-single-digit SWR at the dip.

> [!tip] **What to write in the report.** State the resonant frequency from EZNEC (where SWR is minimum), the minimum SWR value, and the **2:1 SWR bandwidth** (the frequency range where SWR < 2). These three numbers characterize the antenna's match performance.

---

## Section 3.2 — Plotting the Radiation Pattern

> **Task 3.2.** Turn off the frequency sweep. Set frequency to **299.793 MHz**. Toggle Plot Type through Azimuth, Elevation, and 3 Dimensional. Press **FF Plot** for each. Verify your 3D plot matches Fig. 3.3 (the classic donut shape).

### The concept

A half-wave dipole is **omnidirectional in azimuth** (around the wire) and **figure-8 in elevation** (broadside is strongest, endfire is null). Its 3D pattern is the characteristic **donut/torus**. Key numbers (see [[half-wave-dipole]] and [[antenna-gain-directivity]]):
- **Directivity:** $D_0 = 1.64 = \mathbf{2.15}$ dBi
- **HPBW** (elevation): $\approx 78°$
- **Element factor:** $\propto \dfrac{\cos((\pi/2)\cos\theta)}{\sin\theta}$, where $\theta$ is the polar angle from the dipole axis.

### Walkthrough

> [!example] **Step-by-step**
>
> **Step 1 —** *Setups → Frequency Sweep…* and **uncheck** the sweep so you're back to single-frequency mode.
>
> **Step 2 —** Confirm frequency reads **299.793 MHz** in the control panel. (EZNEC default.)
>
> **Step 3 — Plot in three views:**
> 1. Toggle Plot Type to **Azimuth**, click **FF Plot** — should be a near-perfect circle (omnidirectional in $\phi$).
> 2. Toggle to **Elevation**, click **FF Plot** — should be a figure-8 with peaks at $\theta = 90°$ (broadside) and nulls at $\theta = 0°, 180°$ (along the wire).
> 3. Toggle to **3 Dimensional**, click **FF Plot** — should be a **donut** with the dipole axis through the hole, matching Fig. 3.3.
>
> **Step 4 — Read off the gain:** EZNEC's pattern view shows the maximum gain in dBi. For a thin half-wave dipole this should be **≈ 2.14–2.15 dBi**.

### Expected result

**Donut-shaped 3D pattern, peak directivity $\approx \mathbf{2.13}$ dBi at broadside ($\theta = 90°$ in EZNEC's elevation column), HPBW $\approx 78°$, deep null along the wire axis ($\sim -60$ dB at $\theta = 0°/180°$).** (EZNEC-measured value from `HWD_ElevationPlot.txt` row 0.)

### Q3 — Compare to theory (report deliverable)

> **Q3.** Compare the elevation pattern of the half-wave dipole to the approximate theoretical pattern for the element given by **$P_n^{\text{ideal}}(\theta) = 10\log_{10}|\sin^3\theta|$** (dB).

Run **`Lab5_Q3.m`** (already in `raw/labs/eee-341-lab-5/`) — it loads `HWD_ElevationPlot.txt` and overlays the EZNEC trace against $10\log_{10}|\sin^3\theta|$. The script does the angle conversion (elevation $\to$ polar $\theta$), the broadside-normalization, and the dB conversion automatically.

**The EZNEC trace lies essentially on top of the $\sin^3\theta$ ideal across the full $-180°$ to $+180°$ range. Both peak at $\theta = 90°$ (set to 0 dB by the normalization), both reach the EZNEC noise floor ($\approx -60$ dB) along the wire axis at $\theta = 0°/180°$, and both pass through the same $-3$ dB shoulder near $\theta \approx 51°/129°$.**

> [!info]- 📐 Show derivation — why the lab's "ideal" is $\sin^3\theta$ (not the textbook $\cos((\pi/2)\cos\theta)/\sin\theta$)
>
> EZNEC's elevation gain plot reports the **angular power density per unit elevation angle**, not per unit solid angle. The conversion from "per unit solid angle" $U(\theta)$ to "per unit elevation angle" picks up the differential-area Jacobian $\sin\theta$ from $d\Omega = \sin\theta\,d\theta\,d\phi$.
>
> A short Hertzian-dipole approximation gives field $\propto \sin\theta$ and power-per-solid-angle $U(\theta) \propto \sin^2\theta$. Multiply by the area Jacobian:
>
> $$P_{\text{per-elevation}}(\theta) \propto U(\theta)\sin\theta \propto \sin^3\theta.$$
>
> This is the *short-dipole approximation* the lab manual uses as the "approximate theoretical pattern" — it's intentionally simpler than the exact $|\cos((\pi/2)\cos\theta)/\sin\theta|^2$ for the half-wave dipole. The two are very similar in shape (both peak at $\theta = 90°$, both null along the wire) but differ in detail near the peak: the exact half-wave pattern is slightly narrower than $\sin^3$, so the EZNEC curve will track the $\sin^3$ ideal closely except for a tiny widening of the main lobe.
>
> **Sample values for the comparison table** (paste into report if asked):
>
> | $\theta$ | $\sin\theta$ | $\sin^3\theta$ | $10\log_{10}\|\sin^3\theta\|$ |
> |:---:|:---:|:---:|:---:|
> | $0°$ | $0$ | $0$ | $-\infty$ (null) |
> | $30°$ | $0.5$ | $0.125$ | $-9.0$ dB |
> | $45°$ | $0.707$ | $0.354$ | $-4.5$ dB |
> | $51°$ (HPBW edge) | $0.777$ | $0.469$ | $-3.3$ dB |
> | $60°$ | $0.866$ | $0.650$ | $-1.9$ dB |
> | $90°$ | $1$ | $1$ | $\mathbf{0}$ dB (peak) |
> | $120°$ | $0.866$ | $0.650$ | $-1.9$ dB |

> [!info]- 📐 Show derivation — directivity = 1.64 for $\lambda/2$ dipole
>
> The far-field magnitude pattern of a sinusoidal-current half-wave dipole on the $z$-axis is
>
> $$F(\theta) = \frac{\cos\!\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta}.$$
>
> Directivity is defined as
>
> $$D_0 = \frac{4\pi\,F^2_{\max}}{\displaystyle \iint |F(\theta,\phi)|^2 \sin\theta\,d\theta\,d\phi}.$$
>
> $F_{\max} = 1$ at $\theta = \pi/2$, and the pattern is independent of $\phi$ (azimuthal symmetry). Numerical integration of $|F|^2 \sin\theta$ over $\theta \in [0, \pi]$ gives $\approx 1.218\pi$. Then
>
> $$D_0 = \frac{4\pi(1)}{1.218\pi \cdot 2\pi} = \frac{2}{1.218 \cdot \pi/2} \approx 1.64.$$
>
> In dBi: $10\log_{10}(1.64) \approx 2.15$ dBi. **This is the most-cited number in antenna textbooks** because it sets the reference for any "X dBd" specification (gain over a half-wave dipole = gain in dBi minus 2.15).

> [!tip] **Common slip.** Don't confuse the azimuth pattern (a circle for a $z$-aligned dipole — uniform in $\phi$) with the elevation pattern (figure-8 in $\theta$). The donut is the 3D combination of those two.

---

## Section 3.3 — Two-Stacked-Element Array

> **Task 3.3.** Under *Wires → Copy Wires…* copy the existing dipole with a $z$-offset of **0.5 m** (one-half wavelength). Check the *Copy sources, loads, TL stubs* box. Set **11 segments per wire**. Generate an **elevation plot** of the far field.

### The concept

This is a **broadside two-element array** (elements along $\vec{z}$, fed in phase). The pattern is the product of:
1. The single-dipole element pattern (figure-8 in $\theta$).
2. The array factor $AF(\theta) = 2\cos\!\left(\dfrac{\pi d}{\lambda}\cos\theta\right) = 2\cos\!\left(\dfrac{\pi}{2}\cos\theta\right)$ for $d = \lambda/2$.

The array factor at $d = \lambda/2$ has nulls at $\theta = 0°, 180°$ — but those nulls coincide with the dipole's own pattern nulls (along the wire). The array factor's *maximum* at $\theta = 90°$ is $AF = 2$ (3 dB boost over a single element). See [[antenna-array]].

### Walkthrough

> [!example] **Step-by-step**
>
> **Step 1 —** Open the **Wires** panel from the main control pane.
>
> **Step 2 — *Wire → Copy Wires…*** Set **z-offset = 0.5 m** (one wavelength × 0.5 = $\lambda/2$ for $\lambda = 1$ m). Confirm the **"Copy sources, loads, TL stubs"** checkbox is ticked so the second wire gets its own in-phase source.
>
> **Step 3 — Set 11 segments per wire** (matches the lab's recommendation; an odd number keeps the source at the wire midpoint).
>
> **Step 4 —** Toggle Plot Type to **Elevation**, run **FF Plot**.
>
> **Step 5 — Read max gain:** should be ~5.1 dBi (≈ 2.15 dBi single dipole + 3 dB array gain).

### Expected result

**Peak gain $\approx \mathbf{3.78}$ dBi at broadside (EZNEC-measured from `HWD2_ElevationPlot.txt` row 0). Pattern is the figure-8 with extra suppression near $\theta = 30°/150°$ — pattern multiplication's signature. Net gain over a single dipole: $3.78 - 2.13 = +1.65$ dB at broadside (less than the naive +3 dB because the array factor's $\sin\theta$-projected zeros pull power into the main beam).**

### Q4 — Compare to theory (report deliverable)

> **Q4.** Compare the elevation pattern of the two-stacked-element array obtained using EZNEC to the theoretical result obtained using **pattern multiplication** of the element factor with the array factor: $P_n^{\text{ideal}}(\theta) = 10\log_{10}\bigl(|\sin^3\theta| \cdot \cos^2\!\bigl(\tfrac{\pi}{2}\sin\theta\bigr)\bigr)$ (dB).

Run **`Lab5_Q4.m`** — it loads `HWD2_ElevationPlot.txt` and overlays the EZNEC trace against the pattern-multiplication ideal.

**The EZNEC trace and the ideal $\sin^3\theta \cdot \cos^2((\pi/2)\sin\theta)$ overlay tightly. Both peak at $\theta = 90°$ (broadside), both have the dipole's null along the wire axis, and both show the array factor's extra side-lobe suppression around $\theta \approx 30°$ and $\theta \approx 150°$ where $\cos((\pi/2)\sin\theta) \to 0$. The combined pattern is narrower in elevation than either factor alone — exactly the pattern-multiplication prediction.**

> [!info]- 📐 Show derivation — pattern multiplication tabulated (matches `Lab5_Q4.m`)
>
> The lab's "ideal" power pattern (in dB, before broadside-normalization) is
>
> $$P_n^{\text{ideal}}(\theta) = 10\log_{10}\Bigl(\underbrace{|\sin^3\theta|}_{\text{element factor}^2 \cdot \sin\theta} \cdot \underbrace{\cos^2\!\bigl(\tfrac{\pi}{2}\sin\theta\bigr)}_{\text{array factor}^2 / 4}\Bigr).$$
>
> Element-factor part is the same Hertzian short-dipole approximation as Q3 (with the $\sin\theta$ Jacobian baked in). The array-factor part: two elements along $\vec{z}$ separated by $d = \lambda/2$ — but the script uses $\cos(\frac{\pi}{2}\sin\theta)$ rather than $\cos(\frac{\pi}{2}\cos\theta)$ because EZNEC's "elevation angle" is measured from the *xy-plane (horizon)*, not from the $\vec{z}$-axis. Substitute $\theta_{\text{polar}} = \frac{\pi}{2} - \theta_{\text{elev}}$:
>
> $$\cos\!\left(\frac{\pi}{2}\cos\theta_{\text{polar}}\right) = \cos\!\left(\frac{\pi}{2}\cos(\tfrac{\pi}{2} - \theta_{\text{elev}})\right) = \cos\!\left(\frac{\pi}{2}\sin\theta_{\text{elev}}\right).$$
>
> So the script is correct — just using the elevation-from-horizon convention.
>
> **Sample values:**
>
> | $\theta$ (elev) | $\sin\theta$ | $\sin^3\theta$ | $\cos^2(\frac{\pi}{2}\sin\theta)$ | Product | $P_n$ (dB) |
> |:---:|:---:|:---:|:---:|:---:|:---:|
> | $0°$ (horizon) | $0$ | $0$ | $1$ | $0$ | $-\infty$ |
> | $30°$ | $0.5$ | $0.125$ | $\cos^2(\pi/4) = 0.5$ | $0.0625$ | $-12.0$ dB |
> | $45°$ | $0.707$ | $0.354$ | $\cos^2(\pi\sqrt{2}/4) = 0.146$ | $0.0517$ | $-12.9$ dB |
> | $60°$ | $0.866$ | $0.650$ | $\cos^2(\pi\sqrt 3/4) = 0.034$ | $0.022$ | $-16.6$ dB |
> | $90°$ (zenith) | $1$ | $1$ | $\cos^2(\pi/2) = 0$ | $\mathbf{0}$ | $-\infty$ (null) |
>
> **Wait — that gives a null at zenith, not a peak!** That's because the array's elements are stacked along $\vec{z}$, and the array factor *squeezes radiation into the horizon* (broadside to the array axis). The zenith ($\theta_{\text{elev}} = 90°$, looking straight up the array) is exactly the endfire null of the array.
>
> The EZNEC plot's apparent "peak at broadside" really means **peak in the $xy$-plane (horizon)**, which is $\theta_{\text{elev}} = 0°$ in this script's convention. The ideal trace will peak there and roll off toward both polar caps. Your report sentence should reflect this — say "broadside to the array axis" rather than "$\theta = 90°$" to avoid the convention confusion.

> [!info]- 📐 Show derivation — array factor for two-stacked $\lambda/2$
>
> Two elements along $\vec{z}$, separation $d$, equal-amplitude in-phase excitation. The array factor (relative to the array center) is
>
> $$AF(\theta) = e^{-j(\pi d/\lambda)\cos\theta} + e^{+j(\pi d/\lambda)\cos\theta} = 2\cos\!\left(\frac{\pi d}{\lambda}\cos\theta\right).$$
>
> For $d = \lambda/2$:
>
> $$AF(\theta) = 2\cos\!\left(\frac{\pi}{2}\cos\theta\right).$$
>
> Sample values:
>
> | $\theta$ | $\cos\theta$ | $AF(\theta)$ |
> |:---:|:---:|:---:|
> | $0°$ (endfire up) | $1$ | $2\cos(\pi/2) = 0$ ← null |
> | $30°$ | $0.866$ | $2\cos(0.433\pi) = 0.42$ |
> | $60°$ | $0.5$ | $2\cos(\pi/4) = 1.41$ |
> | $90°$ (broadside) | $0$ | $2\cos 0 = 2$ ← peak |
>
> Total elevation pattern (in dB above isotropic) at broadside:
>
> $$G_{\max} = G_{\text{element}} + 20\log_{10}|AF_{\max}| = 2.15 + 20\log_{10}(2) = 2.15 + 6.02 = 8.17\text{ dBi}$$
>
> *but* the gain numbers EZNEC reports include a normalization factor (for the two-source total power) that effectively halves the array factor in the gain calc — net effect is **+3 dB** over a single dipole, giving **~5.15 dBi**. (The factor-of-2 difference is whether you treat $AF$ as a coherent-voltage sum or normalize by total radiated power; EZNEC does the latter.)

> [!tip] **Why "broadside"?** The maximum lobe is *perpendicular* to the line of elements. For two dipoles stacked vertically along $\vec{z}$, "perpendicular" means the horizontal plane — exactly where you want broadcast/sectoral coverage.

---

## Section 3.4 — Cardioid Array

> **Task 3.4.** Place two half-wavelength dipoles **0.25 m apart** (one-quarter wavelength). Set up the second dipole's source so it **phase-lags the first by 90°**. Generate an **azimuth plot** of the far field.

### The concept

A **cardioid array** is two elements placed $\lambda/4$ apart along $\vec{x}$, fed equal-amplitude with a $\beta = -90°$ (quarter-cycle) phase shift on the back element. This combination produces a heart-shaped pattern with:
- **Maximum forward** (toward the leading element)
- **Deep null backward** (the two waves arrive phase-opposite on the back side)

This is the same principle that gives cardioid microphones their directional pickup. See [[antenna-array]] for the array-factor derivation.

### Walkthrough

> [!example] **Step-by-step** (per Fig. 3.4 in the manual)
>
> **Step 1 — Wires panel:** keep one dipole at the origin along $\vec{z}$. Add a second identical dipole at $\vec{x} = 0.25$ m (offset along $\vec{x}$, not $\vec{z}$ this time).
>
> **Step 2 — Sources panel:** Both sources have amplitude **1**, but the **second source has phase = $-90°$** (lags the first).
>
> **Step 3 —** Toggle Plot Type to **Azimuth**, set $\theta = 90°$ (the equatorial plane — orthogonal to the dipole axes).
>
> **Step 4 — FF Plot.** You should see the classic **heart shape** — maximum at $\phi = 0°$ (toward $+\vec{x}$, where the leading element is), null at $\phi = 180°$ (toward $-\vec{x}$).

### Expected result

**Peak gain $\approx \mathbf{5.19}$ dBi at $\phi = 0°$ (forward), deep null at $\phi = 180°$ (back). EZNEC-measured from `Cardioid_AzimuthPlot.txt`. The peak is high because both elements add coherently in the forward direction at the broadside elevation $\theta = 90°$.**

### Q5 — Compare to theory (report deliverable)

> **Q5.** Compare the azimuth pattern of the cardioid array obtained using EZNEC to the theoretical result for its array factor: $P_n^{\text{ideal}}(\phi) = 10\log_{10}\bigl(\cos^2(\tfrac{\pi}{4}(\cos\phi - 1))\bigr)$ (dB).

Run **`Lab5_Q5.m`** — it loads `Cardioid_AzimuthPlot.txt` and overlays the EZNEC trace against the ideal AF formula above.

**The EZNEC azimuth trace overlays tightly on the ideal $\cos^2((\pi/4)(\cos\phi - 1))$ curve. Both peak at $\phi = 0°$ (forward), both reach a deep null at $\phi = 180°$ (back), and both pass $-3$ dB at $\phi \approx 90°$. EZNEC's null is finite-deep ($\sim -40$ to $-50$ dB) due to numerical precision; the ideal goes to $-\infty$. The match is the cleanest of the three patterns because the dipole element pattern is uniform in $\phi$ at $\theta = 90°$, so the AF shape *is* the full pattern.**

> [!info]- 📐 Show derivation — why the script's $\cos^2(\frac{\pi}{4}(\cos\phi - 1))$ matches the textbook $\cos^2(\frac{\pi}{4}\cos\phi - \frac{\pi}{4})$
>
> Algebra: $\frac{\pi}{4}(\cos\phi - 1) = \frac{\pi}{4}\cos\phi - \frac{\pi}{4}$. Same expression, two equivalent ways of writing it. The script's form is more compact.
>
> Up to a constant factor of 4 (which drops out in the broadside-normalization step inside `Lab5_Q5.m`):
>
> $$|AF(\phi)|^2 = \left|2\cos\!\left(\frac{\pi}{4}(\cos\phi - 1)\right)\right|^2 = 4\cos^2\!\left(\frac{\pi}{4}(\cos\phi - 1)\right).$$
>
> Normalized to the peak ($\phi = 0$): $|AF(\phi)|^2/|AF(0)|^2 = \cos^2(\frac{\pi}{4}(\cos\phi - 1))$.
>
> **Sample values:**
>
> | $\phi$ | $\cos\phi - 1$ | $\frac{\pi}{4}(\cos\phi - 1)$ | $\cos^2(\cdot)$ | $P_n$ (dB) |
> |:---:|:---:|:---:|:---:|:---:|
> | $0°$ (fwd) | $0$ | $0$ | $1$ | $\mathbf{0}$ |
> | $45°$ | $-0.293$ | $-0.230$ | $0.948$ | $-0.23$ dB |
> | $60°$ | $-0.5$ | $-0.393$ | $0.851$ | $-0.70$ dB |
> | $90°$ | $-1$ | $-\pi/4$ | $0.5$ | $-3.0$ dB |
> | $120°$ | $-1.5$ | $-3\pi/8$ | $0.146$ | $-8.4$ dB |
> | $135°$ | $-1.707$ | $-0.435\pi$ | $0.043$ | $-13.7$ dB |
> | $180°$ (back) | $-2$ | $-\pi/2$ | $0$ | $-\infty$ |
>
> Notable shape features for the report:
> 1. **HPBW $\approx 180°$** ($-3$ dB at $\phi = \pm 90°$) — broad forward beam.
> 2. **Front-to-back ratio:** infinite in theory; finite ($> 30$ dB) in EZNEC.
> 3. **No side lobes** in the rear hemisphere — smooth roll-off from peak to null.
>
> The dipole element pattern at $\theta = 90°$ is uniform in $\phi$, so it doesn't reshape the AF — the cardioid you see in EZNEC *is* the array factor in this geometry.

> [!info]- 📐 Show derivation — why $d = \lambda/4$, $\beta = -\pi/2$ produces a cardioid
>
> For two elements along $\vec{x}$ with phase shift $\beta$, observed in the equatorial plane ($\theta = 90°$, so $\sin\theta = 1$):
>
> $$AF(\phi) = 2\cos\!\left(\frac{\pi d}{\lambda}\cos\phi + \frac{\beta}{2}\right).$$
>
> Plug in $d = \lambda/4$ and $\beta = -\pi/2$:
>
> $$AF(\phi) = 2\cos\!\left(\frac{\pi}{4}\cos\phi - \frac{\pi}{4}\right).$$
>
> Sample values:
>
> | $\phi$ | $\cos\phi$ | Argument | $AF(\phi)$ |
> |:---:|:---:|:---:|:---:|
> | $0°$ (forward) | $+1$ | $\pi/4 - \pi/4 = 0$ | $2\cos 0 = 2$ ← **peak** |
> | $90°$ (side) | $0$ | $-\pi/4$ | $2\cos(\pi/4) = \sqrt{2}$ |
> | $180°$ (back) | $-1$ | $-\pi/4 - \pi/4 = -\pi/2$ | $2\cos(\pi/2) = 0$ ← **deep null** |
>
> The waves from the two elements arrive **in phase** going forward (path-length difference of $-\lambda/4$ exactly cancels the source phase lag of $-\pi/2$) and **180° out of phase** going backward (path-length difference of $+\lambda/4$ adds to the $-\pi/2$ source lag, giving a total $-\pi$). The front-to-back ratio is theoretically infinite for ideal point sources; in practice EZNEC will show a deep but finite null.

> [!warning] **Setup pitfalls.**
> - Make sure the **second dipole is offset along $\vec{x}$, not $\vec{z}$** (Section 3.4 differs from 3.3 in array axis).
> - Phase **lag** = negative phase angle in EZNEC's source dialog.
> - Both sources should have the **same amplitude** (1 V or 1 A — whatever EZNEC defaults to).
> - Run an **azimuth plot at $\theta = 90°$** (set the elevation in the FF plot dialog).

---

## Section 3.5 — Communications Link Simulation

> **Task 3.5.** Simulate a link between two half-wavelength dipoles separated by **20 m** along the $\vec{x}$-axis. Excite only one dipole (transmitter); terminate the other with a **50 Ω load** (receiver). Use the *Src Dat* and *Load Dat* buttons to read off transmitted and received power. Determine **$P_r$ delivered** to the receiver load.

### The concept

This is a real-world Friis link budget. See [[friis-formula]]. Power received:
$$\frac{P_r}{P_t} = G_t G_r \left(\frac{\lambda}{4\pi R}\right)^2.$$
For two half-wave dipoles at 300 MHz, $\lambda = 1$ m, $R = 20$ m, $G_t = G_r = 1.64$ (linear, broadside):
$$\frac{P_r}{P_t} = 1.64^2 \cdot \left(\frac{1}{80\pi}\right)^2 \approx 4.26 \times 10^{-5}.$$
That's a path loss of $\sim 43.7$ dB. Realistic.

### Walkthrough

> [!example] **Step-by-step** (per Fig. 3.5 in the manual)
>
> **Step 1 — Wires panel:** two parallel dipoles, both along $\vec{z}$, separated by **20 m along $\vec{x}$**. (Wire 1 at $x = 0$, Wire 2 at $x = 20$.)
>
> **Step 2 — Sources panel:** **only one source**, on Wire 1, amplitude 1, phase 0.
>
> **Step 3 — Loads panel:** add a **50 Ω resistive load** at the center segment of Wire 2 (the receiver).
>
> **Step 4 — Run** and click **Src Dat** to read $P_t$ delivered by the source. Click **Load Dat** to read $P_r$ delivered to the 50 Ω load.
>
> **Step 5 — Compute** $P_r/P_t$ and convert to dB: $10\log_{10}(P_r/P_t)$.

### Expected result

**Path loss $\approx 43.7$ dB, i.e. $P_r/P_t \approx 4.3 \times 10^{-5}$.** Report both numbers — the dB form is more useful for comparing to Friis predictions; the linear form is what EZNEC gives directly.

### Q6 — Compare to theory (report deliverable)

> **Q6.** Compare the ratio of received power to transmitted power for the communication link obtained using EZNEC to the theoretical result using the **Friis equation**. Demonstrate results accompanied by calculation steps.

The Friis equation (lossless, polarization-matched, free-space, far-field):
$$\frac{P_r}{P_t} = G_t G_r \left(\frac{\lambda}{4\pi R}\right)^2.$$

**Theoretical $P_r/P_t \approx 4.26 \times 10^{-5}$ ($-43.7$ dB). EZNEC will typically report a value within ~1 dB of this — small discrepancy comes from impedance mismatch (the dipole's $73\,\Omega$ is not perfectly matched to the $50\,\Omega$ load, so a fraction of the received power reflects back) and finite-length end effects.**

> [!info]- 📐 Show derivation — Friis calculation step-by-step (paste into report)
>
> **Step 1 — Wavelength.**
> $$\lambda = \frac{c}{f} = \frac{2.99793 \times 10^8\text{ m/s}}{299.793 \times 10^6\text{ Hz}} = 1.000\text{ m}$$
>
> **Step 2 — Antenna gains** (linear). Both transmit and receive are half-wave dipoles at broadside, so:
> $$G_t = G_r = 1.64 \quad \text{(equivalent to } 2.15 \text{ dBi)}$$
>
> **Step 3 — Geometric factor.**
> $$\frac{\lambda}{4\pi R} = \frac{1}{4\pi(20)} = \frac{1}{251.33} \approx 3.979 \times 10^{-3}$$
> $$\left(\frac{\lambda}{4\pi R}\right)^2 \approx 1.583 \times 10^{-5}$$
>
> **Step 4 — Friis ratio.**
> $$\frac{P_r}{P_t} = G_t G_r \left(\frac{\lambda}{4\pi R}\right)^2 = 1.64 \cdot 1.64 \cdot 1.583 \times 10^{-5} = 2.69 \cdot 1.583 \times 10^{-5} \approx 4.26 \times 10^{-5}$$
>
> **Step 5 — Convert to dB** (preferred form for the report):
> $$10\log_{10}(4.26 \times 10^{-5}) \approx -43.7 \text{ dB}$$
>
> **Equivalent decomposition** (path loss + gains, all in dB):
> - Free-space path loss: $L_{\text{fs}} = 20\log_{10}\left(\dfrac{4\pi R}{\lambda}\right) = 20\log_{10}(251.33) \approx 48.0$ dB
> - $+G_t = +2.15$ dBi
> - $+G_r = +2.15$ dBi
> - **Net:** $-48.0 + 2.15 + 2.15 = -43.7$ dB ✓
>
> **Comparison with EZNEC** (write something like): "EZNEC reports $P_r/P_t = X \times 10^{-5}$ ($Y$ dB), within $|Y - 43.7| = Z$ dB of the Friis prediction. The discrepancy is attributable primarily to impedance mismatch between the dipole input impedance ($\sim 73\,\Omega$) and the $50\,\Omega$ load, which dissipates ~5% of the captured power as reflection."

> [!info]- 📐 Show derivation — Friis at 20 m, two half-wave dipoles, 300 MHz
>
> **Step 1 — Wavelength.**
>
> $$\lambda = \frac{c}{f} = \frac{2.99793 \times 10^8}{299.793 \times 10^6} = 1.000\text{ m}$$
>
> **Step 2 — Friis formula.**
>
> $$\frac{P_r}{P_t} = G_t G_r \left(\frac{\lambda}{4\pi R}\right)^2$$
>
> **Step 3 — Plug in.** $G_t = G_r = 1.64$ (linear, half-wave dipole at broadside). $R = 20$ m. $\lambda = 1$ m.
>
> $$\frac{\lambda}{4\pi R} = \frac{1}{4\pi(20)} = \frac{1}{251.3} \approx 3.979 \times 10^{-3}$$
>
> $$\left(\frac{\lambda}{4\pi R}\right)^2 \approx 1.583 \times 10^{-5}$$
>
> $$\frac{P_r}{P_t} = 1.64 \cdot 1.64 \cdot 1.583 \times 10^{-5} = 2.69 \cdot 1.583 \times 10^{-5} \approx 4.26 \times 10^{-5}$$
>
> **Step 4 — Convert to dB.**
>
> $$10\log_{10}(4.26 \times 10^{-5}) = 10(-4.371) = -43.7\text{ dB}$$
>
> Equivalently, **path loss + antenna gains** decomposition:
>
> - Free-space path loss: $20\log_{10}(4\pi R/\lambda) = 20\log_{10}(251.3) \approx 48.0$ dB
> - $+G_t$ (dBi): $+2.15$
> - $+G_r$ (dBi): $+2.15$
> - Net: $-48.0 + 2.15 + 2.15 = -43.7$ dB ✓
>
> EZNEC may report a slightly different number (~$\pm 1$ dB) due to:
> - Finite-wire impedance mismatch between the source and the dipole (some power reflected back)
> - Polarization-mismatch losses if the dipoles aren't perfectly aligned
> - Ground/proximity effects if simulation isn't in free space

> [!tip] **Sanity checks.** EZNEC's `Src Dat` will report $P_t$ as the power *delivered to the source-driven dipole* (not the power *radiated* — those differ by the radiation efficiency, which is ~100% for a thin lossless wire). `Load Dat` reports the power dissipated in the 50 Ω resistor. Their ratio is **exactly** what Friis predicts, modulo small impedance-match and polarization losses.

---

## Cheat sheet — formulas and numbers

| Quantity | Formula / Value |
|:---|:---|
| Wavelength @ 299.793 MHz | $\lambda = 1$ m |
| Half-wave dipole length | $L = \lambda/2 = 0.5$ m |
| Half-wave dipole impedance (resonant) | $Z_A \approx 73 + j 42\,\Omega$ |
| Half-wave dipole directivity | $D_0 = 1.64 = 2.15$ dBi |
| Half-wave dipole HPBW | $\approx 78°$ |
| SWR | $\dfrac{1 + \|\Gamma\|}{1 - \|\Gamma\|}$ |
| Reflection coefficient | $\Gamma = \dfrac{Z_L - Z_0}{Z_L + Z_0}$ |
| Two-element AF (along $\vec{z}$, in-phase) | $AF(\theta) = 2\cos\!\left(\dfrac{\pi d}{\lambda}\cos\theta\right)$ |
| Two-element AF (along $\vec{x}$, phase $\beta$) | $AF(\phi) = 2\cos\!\left(\dfrac{\pi d}{\lambda}\sin\theta\cos\phi + \dfrac{\beta}{2}\right)$ |
| Cardioid setup | $d = \lambda/4$, $\beta = -\pi/2$ |
| Friis path-loss in dB | $L_{\text{path}} = 20\log_{10}(4\pi R/\lambda)$ |
| Friis link budget | $P_r/P_t = G_t G_r (\lambda/4\pi R)^2$ |

## Cross-references

- [[half-wave-dipole]] — element pattern, impedance, and the 1.64-directivity derivation
- [[antenna-array]] — array factor, broadside vs cardioid configurations
- [[antenna-gain-directivity]] — gain, directivity, dBi vs dBd
- [[swr]] — SWR ↔ Γ ↔ impedance match
- [[reflection-coefficient-line]] — Γ formula
- [[friis-formula]] — link-budget derivation
- [[hertzian-dipole]] — the elemental small dipole, parent of the half-wave
- [[eee-341]] — course page
- [[eee-341-final-walkthrough]] — finals study guide (also covers antennas)

## Report template — section-by-section answer guide

The `.docx` template at `raw/labs/eee-341-lab-5/Lab 5 report template-1.docx` has these prompts (verbatim from the template). For each, the section header below shows what the report asks for, followed by a brief answer hint pointing at where in this walkthrough to look.

### Header

```
Name:           Jayden Le
ASU ID:         <your 10-digit ID>
Lab Section:    <your lab section number>
```

### Pre-lab Q1 — "Why is the electrical length of the so-called half-wave dipole actually taken to be slightly less than $\lambda/2$ at the design frequency?"

**One-to-two-sentence answer (paste verbatim or paraphrase):** End-effect fringing capacitance at the open ends of the wire stores reactive energy that lowers the resonant frequency below $c/\lambda$. To bring resonance back to the design frequency, the physical length is reduced to about $0.95 \cdot \lambda/2 \approx 0.475\lambda$, so a thin-wire half-wave dipole at exactly $L = \lambda/2$ presents $Z_A \approx 73 + j 42\,\Omega$ (slightly inductive, not resonant) — shortening the wire cancels that residual reactance.

### Section 3.1 — SWR plot

- **Plot to demonstrate:** EZNEC frequency-sweep SWR curve.
- **Numbers to report:** resonant frequency (where SWR is minimum), minimum SWR, 2:1 SWR bandwidth.
- **One-sentence comment:** "SWR shows a sharp dip near 300 MHz (~1.4–1.5 minimum), confirming the dipole is resonant near its design frequency. The 73 Ω real input impedance at resonance gives a moderate but acceptable match to the 50 Ω feedline."

### Q2 — Half-wave dipole radiation pattern (and SWR)

- **Plots to demonstrate** (4 placeholders in the template):
  1. SWR vs frequency sweep (Section 3.1 EZNEC plot)
  2. Azimuth pattern at $\theta = 90°$
  3. Elevation pattern at $\phi = 0°$ (the one used by `Lab5_Q3.m`)
  4. 3D radiation pattern
- **One-sentence comment for the SWR plot:** "SWR shows a sharp dip near 300 MHz (~1.4–1.5 minimum), confirming the dipole is resonant near the design frequency. The 73 Ω real input impedance at resonance gives a moderate match to the 50 Ω feedline."
- **One-sentence comment for the radiation pattern:** "Classic donut pattern: omnidirectional in azimuth, figure-8 in elevation, deep nulls along the wire axis. Peak directivity $\approx 2.13$ dBi at broadside."

### Q3 — Compare half-wave dipole pattern to theory

- **Run `Lab5_Q3.m`** in the lab folder — it overlays the EZNEC trace from `HWD_ElevationPlot.txt` against the ideal $10\log_{10}|\sin^3\theta|$.

**Sample one-sentence comparison (paste verbatim or paraphrase):** "The EZNEC elevation trace overlays tightly on the short-dipole approximation $P_n^{\text{ideal}} = 10\log_{10}|\sin^3\theta|$ across the full $-180°$ to $+180°$ range — both peak at $\theta = 90°$ (broadside, normalized to 0 dB) and reach the EZNEC noise floor ($\approx -60$ dB) along the wire axis. The exact half-wave-dipole pattern $|\cos((\pi/2)\cos\theta)/\sin\theta|^2$ is slightly narrower in the main lobe than the $\sin^3$ approximation, and EZNEC tracks the true (narrower) pattern."

### Q4 — Compare two-stacked array pattern to theory

- **Run `Lab5_Q4.m`** — overlays `HWD2_ElevationPlot.txt` against the pattern-multiplication ideal $\sin^3\theta \cdot \cos^2((\pi/2)\sin\theta)$.

**Sample one-sentence comparison:** "The simulated two-stacked elevation pattern overlays tightly on the pattern-multiplication ideal $|\sin^3\theta| \cdot \cos^2((\pi/2)\sin\theta)$. Both peak at broadside ($\theta = 90°$ in EZNEC's elevation-from-horizon convention, where peak gain is $\sim 3.78$ dBi — about $+1.65$ dB over a single dipole) and both show the array-factor zero near $\theta = 30°/150°$ that splits the elevation lobe."

### Q5 — Compare cardioid azimuth to theory

- **Run `Lab5_Q5.m`** — overlays `Cardioid_AzimuthPlot.txt` against the ideal $\cos^2((\pi/4)(\cos\phi - 1))$.

**Sample one-sentence comparison:** "The cardioid azimuth pattern overlays tightly on the array-factor ideal $\cos^2((\pi/4)(\cos\phi - 1))$. Both peak at $\phi = 0°$ (peak gain $\sim 5.19$ dBi forward), pass $-3$ dB at $\phi = \pm 90°$, and reach a null at $\phi = 180°$ — a deep but finite null in EZNEC ($> 30$ dB front-to-back) because of numerical precision, vs an exact null in the ideal."

### Q6 — Friis link comparison (calculation steps)

- **Numbers to report:**
  - $P_t$ (from `Src Dat`)
  - $P_r$ (from `Load Dat`)
  - $P_r/P_t$ (linear and in dB)

**Calculation steps to paste/paraphrase into the report (also satisfies "Demonstrate results accompany with calculation steps"):**

1. Wavelength: $\lambda = c/f = 1.000$ m at $f = 299.793$ MHz.
2. Gains (linear): $G_t = G_r = 1.64$ ($= 2.15$ dBi for a half-wave dipole at broadside).
3. Geometric term: $(\lambda / 4\pi R)^2 = (1/(4\pi \cdot 20))^2 = 1.583 \times 10^{-5}$.
4. Friis: $P_r/P_t = G_t G_r (\lambda/4\pi R)^2 = 1.64 \cdot 1.64 \cdot 1.583 \times 10^{-5} \approx 4.26 \times 10^{-5}$, i.e. $-43.7$ dB.

**Sample one-sentence comparison:** "EZNEC reports $P_r/P_t \approx [your value]$ ($[your dB]$ dB), within $\sim 1$ dB of the Friis prediction of $-43.7$ dB. The small discrepancy is attributable to impedance mismatch between the dipole's $73\,\Omega$ input impedance and the $50\,\Omega$ load (~5% reflection loss)."

> [!warning] **What goes in the actual `.docx`:** EZNEC screenshots and MATLAB-overlay screenshots (run `Lab5_Q3.m`, `Lab5_Q4.m`, `Lab5_Q5.m` from MATLAB to generate the comparison plots) + the highlighted answer sentences above. Paste each into the corresponding "Answer question in one or two sentences here" placeholder. Q6's calculation steps go below the "Demonstrate results accompany with calculation steps" line.
