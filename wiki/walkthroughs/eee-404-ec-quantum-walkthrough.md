---
title: EEE 404 Extra-Credit Lab — QFT vs DFT Speech Compression — Walkthrough + Report Skeleton
type: walkthrough
course:
  - "[[eee-404]]"
tags: [eee-404, lab, extra-credit, walkthrough, quantum-computing, qft, dft, speech, compression, peak-picking, j-dsp]
sources:
  - "[[summary-eee-404-ec-quantum-lab]]"
created: 2026-04-29
updated: 2026-05-06
---

# EEE 404 Extra-Credit Lab: QFT vs DFT Speech Compression — Walkthrough

> [!note] **What this is.** A per-section walkthrough of the **Extra Credit Lab on Quantum Computing** (`raw/labs/eee-404/ec-quantum-qft_dft_exercise.pdf`). It (a) explains the concepts of QFT, peak-picking, and quantum noise; (b) walks through the J-DSP simulation steps; (c) explains how to fill the SNR table; and (d) ends with a **fill-in-the-blanks report skeleton** in the standard Lab/Project Report Template format.
>
> **Lab is worth 20 extra credit points.** Due 2026-05-02 06:59 UTC (Friday morning).
> **No hardware required** — runs entirely in a web browser at https://jdspwebsite.netlify.app/.
> **Provided files:** lab PDF + table template (`ec-quantum-qft_dft_jdsp_simulation_table.docx`).

> [!tip] **The headline workflow.** Build a J-DSP block diagram (SigGen → FFT → PeakPicking → IFFT → SNR), record SNR for each (window-noise-type, qubit-count, peak-method) combination, repeat for QFT instead of FFT. Fill out the 14-row table and discuss the trends. **No coding** — it's all drag-and-drop in J-DSP.

---

## Section I — Concepts you should understand before starting

### 1.1 DFT-based speech compression via peak-picking (review)

For each speech frame $x[n]$ of length $N$:

1. Compute $X[k] = \text{DFT}(x[n])$.
2. **Peak-pick** $L$ of the $N$ frequency bins (set the rest to 0). Two strategies:
   - **First $L$**: keep $X[0..L-1]$, zero out the rest.
   - **Largest $L$**: keep the $L$ bins with largest $|X[k]|$, zero out the rest.
3. Compute $\hat{x}[n] = \text{IDFT}(X_{\text{peak-picked}}[k])$.
4. **SNR** = $10 \log_{10}\!\left(\dfrac{\sum_n |x[n]|^2}{\sum_n |x[n] - \hat{x}[n]|^2}\right)$ in dB.

**Parseval guarantees** that "largest $L$" maximises SNR for a fixed $L$ (you keep the most energy). See [[parseval-theorem]].

### 1.2 Quantum Fourier Transform (QFT)

The QFT is the quantum-circuit analog of the DFT, acting on the amplitudes of an $N = 2^n$-qubit superposition state:
$$\text{QFT}|k\rangle = \frac{1}{\sqrt{N}}\sum_{j=0}^{N-1} e^{+j 2\pi j k / N}|j\rangle$$

> [!warning] **Sign-of-exponent quirk.** QFT uses $e^{+j 2\pi jk/N}$ (positive sign). DFT uses $e^{-j 2\pi jk/N}$ (negative sign). Apart from the sign, and a swap of bins 2 and 4 in the 4-point case (handled by an extra SWAP gate in the QFT circuit), the magnitudes match. So in the **noiseless** limit, QFT-based and DFT-based compression should give nearly identical SNR.

**Complexity:** QFT is $O(n^2) = O((\log_2 N)^2)$. The classical FFT is $O(N \log N) = O(n \cdot 2^n)$. So **QFT is exponentially faster** — but only if you have a noise-free quantum computer (we don't yet).

### 1.3 Quantum noise types

Real quantum computers have noise that perturbs the computation:

- **Amplitude damping** (probability $\gamma = \sin^2 \theta$ of losing a photon → $|1\rangle$ → $|0\rangle$ decay).
- **Phase damping** (probability $\lambda = 1 - \cos^2 \phi$ of phase coherence loss; equivalent to phase-flip channel).
- **Depolarising, bit-flip, measurement error** — also exist; less prominent in this lab.

Each noise channel is modeled as a Kraus operator applied to each qubit. **Result:** QFT-based reconstruction degrades vs. classical FFT-based reconstruction when noise > 0%.

### 1.4 Why both "first L" and "largest L"?

- **First $L$:** simulates a low-pass-only compressor (kills all high-frequency energy regardless of magnitude).
- **Largest $L$:** simulates an ideal magnitude-based compressor (keeps energy peaks, kills everything else).

Comparing them tests **whether the most-significant components of speech happen to be the lowest-frequency bins** (often yes for voiced speech).

---

## Section II — The J-DSP simulation walkthrough

> **Block diagram to build** (Figure 6 of the lab PDF):
> ```
>  SigGen(L) → QFT → Normalize → PeakPicking → IQFT → Normalize ──┐
>             ↑                                                    ↓
>             └─────────── Quantum Noise ─── ... ────────────────► SNR
> ```
> For the **classical FFT comparison** — replace `QFT` with `FFT`, `IQFT` with `IFFT`, drop the Quantum Noise block.

### Step 1 — Open J-DSP

Go to https://jdspwebsite.netlify.app/. Watch the intro video the lab links to (it shows the drag-and-drop block-placement workflow).

### Step 2 — Place blocks for the classical FFT pipeline first

1. Drag **SigGen(L)** from the source palette → set $L$ (frame size) per the table row (e.g. $N = 64$ → $L = 64$).
2. Connect → **FFT** block (set FFT size $N = $ table value).
3. Connect → **PeakPicking** block (set $L$ — the *number of bins to keep*, not the frame size; here we mean the inner column "L components" from the table).
   - Toggle between **"first L"** and **"largest L"** modes (PeakPicking has a setting).
4. Connect → **IFFT** block.
5. Branch the original SigGen output to **SNR** block input A; the IFFT output to **SNR** block input B.

**Run the simulation.** Read the SNR value displayed.

### Step 3 — Repeat for QFT pipeline

1. Same SigGen (use the same speech file so SNR is comparable).
2. Replace FFT → **QFT** block. Set the **number of qubits** $n$ such that $N = 2^n$ (e.g. 6 qubits → $N = 64$).
3. Replace IFFT → **IQFT** block (matching qubit count).
4. **Insert QuantumNoise block** between QFT and IQFT (or per the lab's diagram). Set noise type and magnitude (per table row).
5. **Run.** Read the SNR.

### Step 4 — Fill the table

Per the table in the lab PDF (and the docx template):

| Quantum Noise & % | Qubits | $N$ point | $L$ components | SNR_classical (first $L$) | SNR_classical (largest $L$) | SNR_quantum (first $L$) | SNR_quantum (largest $L$) |
|---|---|---|---|---|---|---|---|
| Amplitude-10 | 6 | 64 | 8 | _____ | _____ | _____ | _____ |
| Amplitude-10 | 6 | 64 | 16 | _____ | _____ | _____ | _____ |
| Amplitude-10 | 7 | 128 | 16 | _____ | _____ | _____ | _____ |
| Amplitude-10 | 7 | 128 | 32 | _____ | _____ | _____ | _____ |
| Amplitude-10 | 8 | 256 | 32 | _____ | _____ | _____ | _____ |
| Amplitude-10 | 8 | 256 | 64 | _____ | _____ | _____ | _____ |
| Phase-20 | 6 | 64 | 8 | _____ | _____ | _____ | _____ |
| Phase-20 | 6 | 64 | 16 | _____ | _____ | _____ | _____ |
| Phase-20 | 7 | 128 | 16 | _____ | _____ | _____ | _____ |
| Phase-20 | 7 | 128 | 32 | _____ | _____ | _____ | _____ |
| Phase-20 | 8 | 256 | 32 | _____ | _____ | _____ | _____ |
| Phase-20 | 8 | 256 | 64 | _____ | _____ | _____ | _____ |
| No Noise | 7 | 128 | 32 | _____ | _____ | _____ | _____ |
| No Noise | 8 | 256 | 64 | _____ | _____ | _____ | _____ |

**14 rows × 4 SNR columns = 56 simulation runs.** Plan ~2 hours for the J-DSP work.

> [!tip] **Order of running to minimise reconfiguration.** Group by FFT size — do all 6 rows at $N=64$ first (changing only $L$ and noise), then all 6 at $N=128$, then 4 at $N=256$. Keeps the block-diagram size-related parameters sticky.

---

## Section III — Predicted trends (use these to sanity-check your data)

Before running, **predict** what each trend should look like. If your data violates these by a lot, you've made a setup mistake.

### 3.1 SNR vs $L$ at fixed $N$

> **As $L$ increases, SNR increases.** More retained components → less reconstruction error. At $L = N$ → perfect reconstruction → SNR → $\infty$ (or capped by numerical precision).

### 3.2 Largest $L$ vs first $L$

> **Largest $L$ ≥ first $L$ (always)**, by Parseval. They become equal when speech energy is concentrated at low frequencies (so "largest" picks the lowest bins anyway).

### 3.3 Quantum noise degrades QFT reconstruction

> **SNR_quantum < SNR_classical at any noise > 0%.** Phase damping is generally *less* destructive than amplitude damping for amplitude-magnitude-based methods like peak-picking, because phase doesn't affect the magnitude (which is what peak-picking selects). So:
> - **Amplitude-damping rows** should show **bigger SNR drop** vs. classical.
> - **Phase-damping rows** should show **smaller SNR drop** vs. classical.

### 3.4 No-noise rows

> **SNR_quantum ≈ SNR_classical** in noise-free limit (modulo numerical precision and the 2↔4 bin swap, both small effects).

### 3.5 Larger qubit count $n$ helps both

> Larger $n$ → larger $N$ → more bins to choose from → more flexibility for peak-picking → higher SNR at the same compression ratio $L/N$.

---

## Section IV — Discussion topics for the report (the 5 "Remarks" in the lab)

1. **Tabulate SNR values.** (Done in §III table above.)
2. **Observe SNR values as $L$ increases with $N$ constant.** Comment on the rate of increase. Often roughly logarithmic (each doubling of $L$ adds a fixed dB).
3. **Observe and compare SNR for classical FFT and quantum FFT.** Comment on the gap: it should be (a) zero in no-noise rows, (b) growing as noise % grows, (c) larger for amplitude than for phase noise.
4. **Compare first $L$ vs. largest $L$** (performance vs. compression potential). Largest $L$ wins on SNR; first $L$ wins on simplicity (no sort needed). Discuss the trade-off.
5. **Observe SNR after introducing quantum noise (per noise type).** Connect the observation to the underlying quantum-noise mechanism (amplitude vs. phase).

---

# 📄 Report Skeleton (fill in the blanks Friday)

Copy everything below into a new Word doc / Google Doc, fill in the bracketed blanks, take screenshots where indicated, and export as PDF.

---

> **EEE 404/591 Real Time DSP**
> **Extra Credit Lab: Comparative Study of QFT and DFT in Speech Compression**
> **Name:** Jayden Le
> **Date:** _[YYYY-MM-DD]_

## 1. Objective

Compare classical DFT/FFT-based and quantum QFT/IQFT-based speech compression using peak-picking, with and without quantum noise (amplitude damping, phase damping). Implementation done in **J-DSP** (Java-DSP web platform, https://jdspwebsite.netlify.app/).

## 2. Background

### 2.1 DFT-based peak-picking compression

For an $N$-sample frame $x[n]$, compute $X[k] = \text{DFT}(x[n])$. Keep $L$ of the $N$ bins (set the rest to 0), then $\hat{x}[n] = \text{IDFT}(X_{\text{peak-picked}}[k])$. **Two peak-selection strategies**: (i) first $L$ bins, (ii) largest-magnitude $L$ bins. By **Parseval's theorem**, strategy (ii) maximises retained energy (and thus reconstruction SNR).

### 2.2 QFT and IQFT

The quantum Fourier transform on $n = \log_2 N$ qubits implements the same DFT operation (modulo a sign flip in the phase exponent and a SWAP of certain bins) but with quantum-circuit complexity $O(n^2)$ instead of $O(N \log N)$.

### 2.3 Quantum noise

Real quantum hardware experiences noise that perturbs the QFT result. We test two channels:

- **Amplitude damping** ($\gamma = \sin^2\theta$): qubit decay $|1\rangle \to |0\rangle$ — directly hits the magnitude.
- **Phase damping** ($\lambda = 1 - \cos^2\phi$): phase coherence loss — equivalent to phase-flip channel.

### 2.4 SNR definition

$$\text{SNR}_\text{dB} = 10 \log_{10}\!\left( \frac{\sum_n |x[n]|^2}{\sum_n |x[n] - \hat{x}[n]|^2} \right)$$

## 3. J-DSP Simulation Setup

### 3.1 Block diagram

_[INSERT SCREENSHOT of your J-DSP block diagram showing SigGen → QFT → Normalize → PeakPicking → IQFT → Normalize → SNR, with QuantumNoise tap.]_

### 3.2 Speech file used

_[Name of the speech file you selected from SigGen(L), e.g. "speech1.wav".]_

### 3.3 Simulation parameters

_[List the swept parameters: qubit counts (6, 7, 8), N values (64, 128, 256), L values, and the noise types (Amplitude-10%, Phase-20%, No-Noise).]_

## 4. Results

### 4.1 SNR table

| Quantum Noise & % | Qubits $n$ | $N$ | $L$ | SNR classical (first $L$) | SNR classical (largest $L$) | SNR quantum (first $L$) | SNR quantum (largest $L$) |
|---|---|---|---|---|---|---|---|
| Amplitude-10% | 6 | 64 | 8 | _____ | _____ | _____ | _____ |
| Amplitude-10% | 6 | 64 | 16 | _____ | _____ | _____ | _____ |
| Amplitude-10% | 7 | 128 | 16 | _____ | _____ | _____ | _____ |
| Amplitude-10% | 7 | 128 | 32 | _____ | _____ | _____ | _____ |
| Amplitude-10% | 8 | 256 | 32 | _____ | _____ | _____ | _____ |
| Amplitude-10% | 8 | 256 | 64 | _____ | _____ | _____ | _____ |
| Phase-20% | 6 | 64 | 8 | _____ | _____ | _____ | _____ |
| Phase-20% | 6 | 64 | 16 | _____ | _____ | _____ | _____ |
| Phase-20% | 7 | 128 | 16 | _____ | _____ | _____ | _____ |
| Phase-20% | 7 | 128 | 32 | _____ | _____ | _____ | _____ |
| Phase-20% | 8 | 256 | 32 | _____ | _____ | _____ | _____ |
| Phase-20% | 8 | 256 | 64 | _____ | _____ | _____ | _____ |
| No Noise | 7 | 128 | 32 | _____ | _____ | _____ | _____ |
| No Noise | 8 | 256 | 64 | _____ | _____ | _____ | _____ |

## 5. Discussion

### 5.1 SNR vs L at fixed N

_[Comment: as L increases at fixed N, SNR increases (more retained spectral energy → less reconstruction error). Quantify the trend: roughly how many dB per doubling of L? E.g., "doubling L from 8 → 16 at N=64 raised SNR by ~X dB."]_

### 5.2 Classical FFT vs quantum FFT

_[Comment on the gap. In no-noise rows it should be ≈ 0 dB. In noisy rows, quantum lags classical by ___ dB (amplitude) and ___ dB (phase). Note that phase damping is gentler because peak-picking is magnitude-based.]_

### 5.3 First-L vs largest-L peak-picking

_[Comment: largest-L always wins by Parseval. The gap is larger when speech energy is spread (consonants, fricatives) and smaller when it's concentrated at low frequencies (voiced vowels). Quantify: "largest-L beats first-L by ~Y dB on average."]_

### 5.4 Effect of quantum noise type

_[Compare amplitude damping vs. phase damping. Amplitude damping should produce a bigger SNR drop because peak-picking selects on magnitude. Phase damping mostly preserves magnitudes.]_

### 5.5 Effect of qubit count $n$

_[Comment: more qubits → more bins → more flexibility → SNR improves at the same compression ratio L/N. Quantify across the rows where L/N is held constant (e.g. L/N = 1/4: row 2 vs row 4 vs row 6; row 8 vs row 10 vs row 12).]_

## 6. Conclusion

_[2-3 sentences summarizing what you observed. Suggested theme: "Classical FFT-based peak-picking is robust; QFT-based reaches similar SNR in noise-free limits but degrades sharply with amplitude noise. Largest-L peak-picking dominates first-L by Parseval; quantum hardware is not yet competitive for this task."]_

---

> [!tip] **Time budget for this lab.** ~1 hr reading the PDF + concepts, ~2 hrs running J-DSP simulations (56 runs), ~1 hr writing the report. **Total: ~4 hours** for 20 EC.

> [!tip] **Why this exercise matters beyond the EC points.** This is your first encounter with the **physics-meets-DSP** thread that runs through the [[python-ml-wireless]] roadmap. QFT, while still impractical at scale, is one of the few quantum algorithms with a *direct* DSP interpretation. Pair this with the [[paper-rethinking-edge-ai-spm]] on edge-DSP for a research-essay narrative.

## See also

- [[eee-404]] — course page
- [[dft]], [[fft]], [[idft]], [[parseval-theorem]] — classical DSP basics
- [[eee-404-exam-2-walkthrough]] — Exam 2 Problem 4 is the same DFT-via-FFT machinery
- [[lab-7-fft]] — companion lab on FFT in real time
