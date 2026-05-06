# Wiki Index

Catalog of every page in the wiki. Organized by section. The LLM updates this on every ingest and every new page creation. See [[CLAUDE]] for the schema.

> **Getting around:** Open any `[[link]]` in Obsidian to jump there. Use the graph view (Ctrl+G) to see how pages connect.

---

## Courses

- [[eee-404]] — EEE 404/591 Real Time DSP (Dr. Chao Wang)
- [[eee-350]] — EEE 350 Random Signal Analysis (Dr. Cihan Tepedelenlioglu)
- [[eee-304]] — EEE 304 Signals and Systems II / Communication Systems
- [[eee-341]] — EEE 341 Engineering Electromagnetics (Cemil Geyik) — 49 lecture PDFs ingested, finals walkthrough filed
- [[eee-335]] — EEE 335 Analog and Digital Circuits (MOSFET physics → CMOS logic → IC amplifiers → frequency response → differential pair)
- [[python-ml-wireless]] — **14-month Physical-Layer ML Roadmap** targeting NVIDIA + Wi-Lab (May 2026 → Jun 2027)

## Implementation

Code living at [`aircomp-regret-pluto/`](../aircomp-regret-pluto/) — 4× Adalm Pluto AirComp pipeline (folder previously named `implementation/`; zipped backup at `implementation.zip`). See [`aircomp-regret-pluto/README.md`](../aircomp-regret-pluto/README.md) for usage. Design persona rules in `CLAUDE.md` → "Implementation agent — 6G researcher persona".

### Toolchain concepts (for the Pluto build pipeline)
- [[cross-compilation]] — the general concept
- [[gcc-arm-linux-gnueabihf]] — the specific ARM cross-compiler
- [[pluto-build-toolchain]] — the three-artifact build pipeline (Vivado + GCC + `plutosdr-fw`)
- [[wsl2-embedded-workflow]] — Windows host setup via WSL2

### Architecture + runtime concepts
- [[zynq-ps-pl-split]] — PS (ARM) vs PL (FPGA); where each file in `aircomp-regret-pluto/` runs
- [[pluto-experiment-lifecycle]] — flash-once / run-each-epoch; USB out of real-time path; jitter sources
- [[pre-flash-test-pyramid]] — 6-layer dev loop for catching bugs before reflashing

### Algorithm internals
- [[hmc-psi-rebuild]] — HMC rebuilds ψ each round from D (not additive like Hedge); μ delay; exploration floor
- [[aircomp-utility-s1-s2]] — `(S1, S2)` aggregate feedback; utility decomposition; bandwidth + privacy

## Research

- [[system-pipeline]] — **Main design doc.** End-to-end AirComp + regret-learning pipeline (7 stages, fact-checked against papers)
- [[signal-design-gaps]] — **Gap analysis.** Beacon / sync / data / feedback signal design gaps vs 2024–2026 6G research
- [[aircomp-basics]] — System model, MSE, denoising
- [[regretful-learning]] — Hart & Mas-Colell regret matching for distributed power control
- [[channel-estimation]] — LS estimation of `|h_n|` from beacon
- [[robust-signaling]] — Gold/Golay/polar/CRC choices for the control plane

## People

- [[chao-wang]] — EEE 404 instructor

### Physical-Layer ML Roadmap — researchers & teachers

**Target labs**
- [[alkhateeb]] — Wi-Lab director (ASU), primary PhD target
- [[hoydis]] — NVIDIA Sionna lead, primary NVIDIA research contact
- [[aitaoudia]] — NVIDIA Sionna co-lead (NEW 2026-05-01) — Hoydis's closest collaborator
- [[cammerer]] — NVIDIA Sionna NRX lead (NEW 2026-05-01) — Stuttgart pedigree, owns the NRX repo
- [[wiesmayr]] — ETH PhD with NVIDIA-internship-then-coauthorship trajectory (NEW 2026-05-01) — first author of NRX-2024 + SALAD-2025; the example of the role Jayden is targeting
- [[alikhani]] — Wi-Lab PhD student (NEW 2026-05-01) — first author of LWM/LWM-Spectro/LWM-Temporal
- [[morais]] — Wi-Lab alum at NVIDIA, strategic preparatory contact
- [[oshea]] — DeepSig, co-author of seminal PHY-ML paper
- [[heath]] — UT Austin / NCSU, Alkhateeb's PhD advisor
- [[bjornson]] — KTH, Wireless Future channel
- [[lichtman]] — UMD, author of PySDR

**Teachers / textbook authors**
- [[karpathy]] — Zero-to-Hero, nanoGPT
- [[raschka]] — Lightning AI, PyTorch bridge teacher
- [[rougier]] — NumPy + matplotlib pedagogy
- [[prince]] — *Understanding Deep Learning*
- [[bishop]] — PRML
- [[murphy]] — *Probabilistic Machine Learning*
- [[goodfellow]] — GANs + DL textbook
- [[sutton]] — RL canon (with Barto)
- [[mackay]] — *Information Theory, Inference, and Learning Algorithms*
- [[ng]] — Coursera ML/DL specializations
- [[chollet]] — Keras, *Deep Learning with Python*

## Concepts — Physical-Layer ML Roadmap

### Wireless + ML core
- [[physical-layer-ml]] — umbrella concept
- [[sionna]] — NVIDIA's differentiable link-level simulator (umbrella)
- [[sionna-rt]] — **NEW 2026-05-01** — Sionna's differentiable ray-tracing module (vs the umbrella)
- [[nvidia-aodt]] — **NEW 2026-05-01** — NVIDIA Aerial Omniverse Digital Twin (productized cousin of Sionna)
- [[deepmimo]] — Wi-Lab ray-traced channel dataset
- [[deepsense-6g]] — multi-modal real-world sensing-comm dataset
- [[large-wireless-model]] — Wi-Lab foundation model (LWM)
- [[neural-receiver]] — NVIDIA's 5G NR neural receiver
- [[neural-decoder]] — **NEW 2026-05-01** — distinct from neural-receiver; the BP-replacement subblock (Cammerer's PhD line)
- [[autoencoder-phy]] — O'Shea/Hoydis 2017 E2E autoencoder
- [[csi-feedback]] — CsiNet and descendants
- [[differentiable-ray-tracing]] — Sionna RT + calibration
- [[wireless-digital-twin]] — Alkhateeb vision + NVIDIA AODT
- [[beam-prediction]] — DeepSense task, multi-modal fusion
- [[channel-charting]] — self-supervised CSI-based positioning
- [[modulation-classification]] — RadioML + AMC
- [[ofdm]] — the waveform connecting DSP ↔ PHY-ML

### Python / ML foundations
- [[pytorch]] — the framework
- [[numpy-vectorization]] — the prerequisite
- [[transformer]]
- [[attention-mechanism]]
- [[convolutional-neural-network]]
- [[variational-autoencoder]]
- [[generative-adversarial-network]]
- [[diffusion-model]]
- [[graph-neural-network]]
- [[reinforcement-learning]]
- [[backpropagation]]
- [[autograd]]

### Optimization, loss functions, regularization (NEW 2026-05-01 — Phase 1 foundations sprint)
- [[gradient-descent]] — walk downhill; the algorithm behind every DL training step
- [[stochastic-gradient-descent]] — minibatch GD; the actual default
- [[adam-optimizer]] — adaptive per-parameter learning rate; the modern default
- [[cross-entropy-loss]] — the classification loss; pairs with [[softmax]]
- [[mse-loss]] — the regression loss; NMSE is its wireless variant
- [[softmax]] — logits → probability distribution
- [[regularization]] — L1/L2 penalties; weight decay; the umbrella for fighting [[overfitting-bias-variance]]
- [[dropout]] — stochastic activation zeroing; implicit Bayesian ensemble
- [[batch-normalization]] — normalize per minibatch; enables 10× larger LR
- [[overfitting-bias-variance]] — generalization error decomposition; double descent

### Wireless basics (NEW 2026-05-01 — Phase 1–2 foundations sprint)
- [[qam-modulation]] — $\log_2 M$ bits per symbol; 5G data-channel modulation
- [[ldpc-codes]] — sparse parity-check + belief propagation; 5G data-channel code
- [[ber-bler]] — performance metrics; $10^{-2}$ BLER point is the 5G design target
- [[mimo-basics]] — spatial multiplexing / diversity / beamforming; channel matrix $\mathbf{H}$
- [[mmwave-mimo]] — sparse + hybrid + blockage-prone variant; the SHARED Wi-Lab/Sionna problem
- [[fading-channels]] — Rayleigh / Rician / 3GPP UMi/UMa; multipath delay + Doppler
- [[matched-filter]] — optimal SNR linear filter for known waveforms
- [[equalization]] — undo ISI; ZF / LMMSE / DFE / neural
- [[belief-propagation]] — DSP↔ML identity bridge; sum-product on factor graph = neural BP / GNN message-passing

### Reinforcement learning atoms (NEW 2026-05-01 — Phase 3 M7–M8 sprint)
> **Reading priority for NVIDIA-intern goal:** [[ppo]] + [[sac]] + [[gae]] + [[policy-gradient]] are load-bearing for any Phase 3 wireless-RL deliverable. [[q-learning]] + [[dqn]] are pedagogical foundations. [[sarsa]] + [[bandit-regret]] are background reference (read once, don't dwell).
- [[policy-gradient]] — directly parameterize $\pi_\theta$; gradient ascent on expected return
- [[reinforce]] — Monte-Carlo policy gradient (the simplest member)
- [[actor-critic]] — adds value-function critic for variance reduction
- [[gae]] — Generalized Advantage Estimation; the variance-reduction trick powering PPO/A2C
- [[ppo]] — modern on-policy default with clipped trust region
- [[sac]] — **Soft Actor-Critic; off-policy continuous-action default for wireless RL**
- [[q-learning]] — off-policy TD; learns $Q^*$ directly
- [[dqn]] — Q-learning + neural network + replay buffer + target network *(discrete-action baseline; see [[sac]] for wireless)*
- [[sarsa]] — on-policy cousin *(read for Sutton-Barto Ch 6 completeness; not portfolio-priority)*
- [[bandit-regret]] — Sutton-Barto Ch 2 stateless RL *(background reference — direct ancestor of [[regretful-learning]] AirComp work)*

### Industrial / deployment / wireless-protocol concepts (load-bearing for NVIDIA-intern goal)
> **Reading priority:** the first three are first-technical-screen-probe-level. The rest are supporting.
- [[5g-nr-pusch-structure]] — **NEW 2026-05-01 (Lyra audit)** — DM-RS / TBS / HARQ timing / 3GPP TR refs; **the first technical-screen probe**.
- [[sionna-api-cheatsheet]] — **NEW 2026-05-01 (Lyra audit)** — Sionna 2.x API surface; the operational prep artifact for the M7 NRX reproduction.
- [[onnx]] — PyTorch → TensorRT bridge format (deployment-chain).
- [[tensorrt]] — NVIDIA's GPU inference compiler (FP16/INT8) — extended with **INT8 calibration workflow** (Lyra audit fix).
- [[quantization-aware-training]] — **NEW 2026-05-01 (Lyra audit)** — PTQ vs QAT; recovers Wiesmayr-2024 NRX 0.5 dB on Jetson.
- [[mixed-precision-training]] — FP16 / BF16 / FP8; M3 ResNet-18-with-AMP backbone.
- [[link-adaptation]] — MCS selection per slot; OLLA classical, [[paper-wiesmayr-salad-2025|SALAD]] modern.
- [[harq]] — Hybrid ARQ; provides ACK/NACK feedback that drives link adaptation.
- [[scaling-laws]] — Kaplan / Chinchilla; load-bearing for M11 LWM extension.
- [[ofdm-phy-basics]] — subcarriers / CP / pilot grid; M2 OFDM-from-scratch foundation.
- [[ris]] — Reconfigurable Intelligent Surface *(Wi-Lab MILCOM demo; secondary for NVIDIA goal)*.
- [[o-ran]] — Open RAN architecture; xApps / E2 interface.
- [[umap]] — non-linear dim reduction *(only used by [[paper-morais-similarity-2026]]; background)*.

### Channel coding + FL + DT-calibration (NEW 2026-05-01)
- [[polar-codes]] — **5G NR control-channel code; Cammerer's PhD line origin** (mandatory pre-cold-email read).
- [[digital-twin-calibration]] — **closed-loop concept wrapping [[paper-diff-rt-calibration-2024]]; M10 capstone technical core.**
- [[federated-learning]] — FedAvg + OTA-FL umbrella *(load-bearing for AirComp track / [[system-pipeline]]; secondary for NVIDIA-Sionna-team goal)*.
- [[reed-muller-codes]] — polar's algebraic ancestor *(background reference — read after polar-codes, not portfolio-priority)*.

## Concepts — EEE 304 (Communication Systems)

### AM modulation/demodulation
- [[amplitude-modulation]] — `Φ_AM(t) = (A + m(t))·cos(w_c·t)`, USB/LSB, why we shift to a high carrier
- [[modulation-index]] — μ = m_peak / A; under / perfect / over-modulation
- [[coherent-demodulation]] — multiply by carrier again + LPF; works for any μ
- [[envelope-detection]] — `|signal|` + bandpass; cheap but only works for μ ≤ 1
- [[butterworth-filter]] — maximally flat LPF/BPF design; the workhorse in this lab

### Pulse modulation + multiplexing + amplification
- [[pulse-amplitude-modulation]] — sample at Nyquist, send pulses with sample-valued amplitudes
- [[time-division-multiplexing]] — interleave N PAM streams into a frame with a sync slot
- [[chopper-amplifier]] — square-wave modulate up + bandpass amplify + chop down → `G = 2A·sin²(πD)/π²`

## Concepts — EEE 404 (FFT / DSP)

### FFT & Fourier transforms
- [[dtft]], [[dft]], [[fft]] — Discrete-Time Fourier Transform / Discrete / Fast Fourier Transform
- [[twiddle-factor]], [[butterfly]], [[decimation-in-time]], [[bit-reversed-order]] — FFT mechanics
- [[fft-scaling]] — overflow prevention
- [[dft-bin-interpretation]], [[frequency-resolution]], [[nyquist-frequency]], [[conjugate-symmetry]] — interpretation
- [[idft]], [[real-valued-fft]] — inverse + real-signal optimization
- [[fixed-point-arithmetic]] — Q15 embedded arithmetic
- [[complex-multiplication]], [[dft-computation-complexity]]
- [[dft-properties]], [[parseval-theorem]] — algebra of the DFT (NEW 2026-04-29)
- [[stft]], [[window-function]], [[spectral-leakage]], [[window-resolution-criterion]] — time-frequency
- [[rectangular-window]], [[hamming-window]], [[hann-window]], [[bartlett-window]]
- [[autocorrelation-pitch-detection]] — pitch via $\mathrm{IFFT}(|\mathrm{FFT}|^2)$ (NEW 2026-05-02 from Project 2)
- [[formant]] — vocal-tract resonances; spectral envelope peaks (NEW 2026-05-02 from Project 2)
- [[cmsis-dsp-fft]] — `arm_rfft_fast_f32` API + packed output (NEW 2026-05-02 from Project 2)

### Z-transform + filter implementation (NEW 2026-04-29 from Modules 7+8)
- [[z-transform]], [[region-of-convergence]] — Z-domain + ROC rules
- [[difference-equation]], [[fir-vs-iir]] — time-domain LTI form + classifier
- [[direct-form-i]], [[direct-form-ii]] — block-diagram realisations

### Neural networks (NEW 2026-04-29 from Module 6)
- [[neuron]] — atomic forward-pass building block
- [[mlp]] — multi-layer perceptron architecture
- [[relu]] — default activation (with the negative-pre-activation trap)
- [[forward-propagation]] — layer-by-layer inference
- [[backpropagation]] — training (already existed; reinforced)

## Concepts — EEE 335 (Analog & Digital Circuits)

### Unit 1 — MOSFET physics
- [[mosfet-iv-characteristics]] — triode/saturation regions, $I_D$ equations
- [[mosfet-body-effect]] — $V_t = V_{t0} + \gamma(\sqrt{V_{SB}+2\phi_F}-\sqrt{2\phi_F})$

### Unit 2 — CMOS logic
- [[cmos-inverter-vtc]] — VTC, noise margins $\tfrac{1}{8}(3V_{DD}+2V_t)$
- [[cmos-transistor-sizing]] — $W_p/W_n$, series/parallel rules
- [[cmos-power-dissipation]] — static = 0; $P_{\text{dyn}} = \alpha CV_{DD}^2 f$

### Unit 3 — Memory & switches
- [[pass-transistor-logic]] — NMOS poor-1, transmission gate
- [[sram-cell]] — 6T topology, read/write sizing constraints

### Unit 4 — Small-signal amplifiers
- [[mosfet-small-signal-model]] — $g_m$, $r_o$, $g_{mb}$
- [[common-source-amplifier]] — $A_v = -g_m R_L'$
- [[common-gate-amplifier]] — current buffer, $R_{\text{in}} \approx 1/g_m$
- [[source-follower]] — voltage buffer, $A_v \approx 1$
- [[current-mirror]] — $I_O = I_{\text{REF}}(W/L)_2/(W/L)_1$

### Unit 5 — High frequency
- [[mosfet-high-frequency-model]] — $C_{gs}$, $C_{gd}$, $f_T$
- [[millers-theorem]] — input cap multiplied by $(1+|A_v|)$
- [[octc-method]] — $\omega_H \approx 1/\sum C_k R_k$
- [[cs-amplifier-frequency-response]] — Miller-dominated bandwidth

### Unit 6 — Multi-transistor + differential
- [[cascode-amplifier]] — $A_v = -(g_m r_o)^2$
- [[differential-pair]] — $A_d = g_m R_D$ (diff), $\tfrac{1}{2}g_m R_D$ (s.e.)
- [[cmrr]] — $\text{CMRR}_\text{s.e.} = g_m R_{SS}$

## Concepts — EEE 341 (Electromagnetics)

### Module 1 — Foundations
- [[maxwell-equations]] — point/integral/time-harmonic forms; the four pillar equations
- [[displacement-current]] — $\partial\vec{D}/\partial t$, what makes Ampere consistent
- [[boundary-conditions-em]] — tangential/normal continuity at material interfaces

### Module 2 — Plane waves
- [[helmholtz-equation]] — time-harmonic wave equation $\nabla^2\vec{E} - \gamma^2\vec{E} = 0$
- [[complex-permittivity]] — $\epsilon_c = \epsilon - j\sigma/\omega$, loss tangent
- [[plane-wave-lossless]] — $k$, $\eta$, TEM propagation
- [[plane-wave-lossy]] — $\alpha$, $\beta$, skin depth, surface impedance
- [[wave-polarization]] — linear, circular (RHCP/LHCP), elliptical, axial ratio
- [[poynting-vector]] — power density, time-average $\tfrac{1}{2}\text{Re}\{\vec{E}\times\vec{H}^*\}$

### Module 3 — Reflection & refraction
- [[fresnel-coefficients]] — $\Gamma, \tau$ at normal incidence
- [[snells-law]] — reflection + refraction at oblique incidence (TE/TM)
- [[brewster-angle]] — $\theta_B = \arctan(n_2/n_1)$, zero parallel reflection
- [[total-internal-reflection]] — critical angle, evanescent waves, fiber optics

### Module 4 — Transmission lines & Smith chart
- [[transmission-line-model]] — distributed R, L, G, C; characteristic impedance $Z_0$
- [[reflection-coefficient-line]] — $\Gamma_L$, VSWR, return loss
- [[smith-chart]] — purpose, key features, single-stub & quarter-wave matching

### Module 5 — Waveguides & cavity resonators
- [[waveguide-modes]] — TEM, TE, TM mode classification
- [[waveguide-cutoff]] — cutoff frequency, propagation/evanescent regimes
- [[cavity-resonator]] — TE$_{mnp}$, TM$_{mnp}$, dominant TE$_{101}$, Q-factor

### Module 6 — Antennas
- [[hertzian-dipole]] — elemental dipole; $R_{\text{rad}} = 80\pi^2(\ell/\lambda)^2$
- [[half-wave-dipole]] — practical $R_{\text{rad}} \approx 73\,\Omega$ wire antenna
- [[antenna-gain-directivity]] — $G = \xi D$, beamwidth, effective area
- [[friis-formula]] — link budget $P_r/P_t = G_tG_r(\lambda/4\pi R)^2$

## Concepts — EEE 350 (Probability & Statistics)

### Moments & dependence
- [[covariance]], [[correlation-coefficient]], [[variance-of-a-sum]]
- [[independent-vs-uncorrelated]] — the classic gotcha
- [[bivariate-gaussian]], [[multivariate-gaussian]]
- [[random-vector]], [[iid-samples]], [[max-of-iid]]

### Conditional expectation
- [[conditional-expectation]] — E[X|Y] is a RV
- [[iterated-expectations]] — E[E[X|Y]] = E[X]
- [[conditional-variance]], [[law-of-total-variance]]
- [[sum-of-random-number-of-rvs]] — compound / random sums

### Asymptotic theorems
- [[markov-inequality]], [[chebyshev-inequality]]
- [[convergence-in-probability]]
- [[weak-law-of-large-numbers]]
- [[gamblers-fallacy]] — the classic LLN misuse
- [[central-limit-theorem]]
- [[standardization]] — the (X − μ)/σ rescaling (distinct from CLT)
- [[variance-scaling-rule]] — Var(cX) = c²·Var(X)
- [[continuity-correction]], [[binomial-via-clt]]
- [[standard-normal-table]]

### Bayesian inference
- [[bayesian-inference]]
- [[prior-distribution]], [[posterior-distribution]]
- [[detection-vs-estimation]]
- [[map-detection]], [[map-estimation]]
- [[lms-estimation]] — MMSE = E[θ|X] (Wiley/MIT naming: "LMS")
- [[linear-mmse-estimation]] — aX + b, the linear-restricted estimator (HW7 naming: "LMSE")
- [[antipodal-signaling]]

### Classical estimation
- [[maximum-likelihood-estimation]]
- [[unbiased-estimator]], [[consistent-estimator]], [[efficient-estimator]]
- [[confidence-interval]]

### Hypothesis testing
- [[significance-test]] — reject/fail-to-reject under fixed α
- [[neyman-pearson-test]]
- [[type-i-error]], [[type-ii-error]]
- [[likelihood-ratio-test]]
- [[chi-squared-test]]

### Regression
- [[linear-regression]], [[least-squares]], [[power-law-regression]]

### Descriptive statistics
- [[sample-mean]], [[sample-variance]], [[sample-covariance]]
- [[sample-median]], [[sample-mode]], [[order-statistics]]
- [[histogram]], [[skewness-kurtosis]]

### Stochastic processes (intro)
- [[stochastic-process]], [[stationary-process]]
- [[white-gaussian-process]], [[colored-noise]]
- [[poisson-process]], [[markov-chain]]

## Concepts — Learning meta (study skills + AI tutoring)

- [[retrieval-practice]] — testing yourself beats re-reading; the test *is* the learning, not just the assessment
- [[blooms-taxonomy]] — 6-level cognitive hierarchy; AI handles bottom 3 (memorize / understand / apply), humans must own top 3 (analyze / evaluate / create)
- [[ai-learning-risk-complexity]] — Sung's framework: as topic complexity rises, LLM accuracy falls and 10% errors compound — make the gating decision upfront

## Formulas

- [[dft-formula]] — forward + expanded
- [[idft-formula]] — and FFT-based recipe
- [[fft-butterfly]] — X[k] and X[k+N/2]
- [[twiddle-factor-formula]] — periodicity, half-circle, squaring
- [[covariance-formula]] — Cov, ρ, Var-of-sum, samples
- [[conditional-expectation-formulas]] — tower rule, total variance, Gaussian conditional, random sums
- [[asymptotic-formulas]] — Markov, Chebyshev, WLLN, CLT
- [[inference-formulas]] — Bayes, MAP, LMS, MLE, CI, LRT, LS

## Walkthroughs

Per-question lab/HW walkthroughs (concept-first, then steps). Filed under `wiki/walkthroughs/`. The headline teaching artifacts when ingesting an assignment.

### EEE 404
- **[[eee-404-final-quiz-walkthrough]]** — **Lab Exam + ABET Quiz combined walkthrough** (Tue 5/5 9:50–11:40 AM). §A = 5 lab-exam topic blocks (Lab 5 digital filters, Lab 6 music synthesis, Project 1 image processing, Project 2 FFT, Assembly programming). §B = ABET quiz cheat-sheet skeleton + likely short-essay/T-F/fill-in items. Pre-exam routine + time strategy. ⭐
- **[[eee-404-project-2-walkthrough]]** — Project 2 walkthrough: vowel analysis (`max_index`, autocorrelation pitch detection, formant reading) + real-time spectrum analyzer (4 FILL_IN_BLANKs + `apply_window`, window comparison). Due Mon 5/4.
- **[[eee-404-exam-2-walkthrough]]** — full per-problem walkthrough of all 4 Exam 2 practice problems (MLP forward pass; Z-transform/ROC/DF-II; sampling/DFT/FFT sizing; 4-pt DFT direct + FFT butterfly + IFFT). Thursday 4/30 exam.
- **[[eee-404-exam-2-study-guide]]** — companion topic checklist + master equation sheet for the 8.5×11 cheat sheet
- **[[eee-404-ec-ml-walkthrough]]** — EC ML lab walkthrough + report skeleton (XOR-XOR on STM32; due Fri 5/2; 10 EC pts)
- **[[eee-404-ec-quantum-walkthrough]]** — EC Quantum lab walkthrough + report skeleton (QFT vs DFT in J-DSP; due Fri 5/2; 20 EC pts)
- [[eee-404-hw5-walkthrough]] — full per-problem HW5 walkthrough (DTFT, Hamming/rectangular resolution, FFT butterflies, STM32 real-time budget) with collapsible derivation drop-downs
- [[eee-404-lab-7-fill-in-walkthrough]] — every FILL_IN_BLANK explained

### EEE 304
- **[[eee-304-final-exam-walkthrough]] — Full numerical solutions to the actual final exam (8 problems, 350 pts) — verified end-to-end** ⭐⭐
- **[[eee-304-final-walkthrough]] — Final Exam concept walkthrough (8 problem types, 350 pts, 150 min, open May 4 10 AM → May 6 11:59 PM)** ⭐
- **[[eee-304-lab-ec1-walkthrough]]** — extra-credit Lab EC1 (Arduino Due digital filtering, `butter` filter design at $f_s = 5$ kHz, headphone DAC output). Due 2026-05-06.
- **[[eee-304-lab-ec2-walkthrough]]** — extra-credit Lab EC2 (LED + phototransistor feedback control with discrete-time integral controller; plant ID via exponential fit; closed-loop bandwidth $1$ rad/s and 10×). Due 2026-05-06.
- [[eee-304-lab-4-walkthrough]] — full per-question Lab 4 walkthrough (AM modulation/demodulation in Simulink)
- [[eee-304-hw7-walkthrough]] — full per-problem HW7 walkthrough (cascaded AM, TDM-PAM, chopper amplifier)

### EEE 350
- **[[eee-350-final-walkthrough]] — Module-by-Module Final Review (cumulative).** Per-module breakdown of slides 1–49: building blocks, headline formulas, representative practice problems lifted from each lecture's "Worked examples" + the 3 practice sets + HW7. Master Cheat Sheet (6 tables) + pre-exam routine. ⭐
- [[eee-350-hw7-walkthrough]] — full per-problem HW7 walkthrough (significance testing + MMSE/LMSE estimation)

### EEE 341
- [[eee-341-lab-5-walkthrough]] — Lab 5 (EZNEC antenna sims: SWR, radiation pattern, two-stacked array, cardioid, Friis link). Due Thu 4/30.
- [[eee-341-final-walkthrough]] — finals study guide

### EEE 335
- **[[eee-335-final-lecture-review]]** — **lecture-by-lecture final review (Lectures 17–36 + CCA + CCA-HFR; analog only).** Final is **Tue May 5, 12:10–2:00 PM, SCOB 250.** Master cheat sheet + T/F drill bank + Practice Final problem-type map.
- [[eee-335-final-walkthrough]] — full per-unit final exam study guide with collapsible derivations + cheat-sheet formula table (Units 1–6: MOSFET physics, CMOS logic, memory, IC amplifiers, frequency response, diff pair/cascode/CMRR)

### EEE 341
- [[eee-341-final-walkthrough]] — full per-module final exam study guide with collapsible derivations + cheat-sheet formula table (Modules 1–6: Maxwell + BCs, plane waves, reflection/refraction, transmission lines + Smith chart, waveguides + cavity resonators, antennas + Friis)

### Physical-Layer ML Roadmap (NEW 2026-05-01 — Tier-6)
- [[nrx-reproduction-walkthrough]] — **the M7 capstone: step-by-step NRX reproduction guide** for [[paper-nrx-cammerer-2023]] / [[paper-nrx-wiesmayr-2024]]. 6-stage process from "read the papers" to "ready to send the cold email." The headline teaching artifact for the entire roadmap.

## Examples

Standalone worked examples (one-off teaching examples, not full assignments). Filed under `wiki/examples/`.

### EEE 404
- [[dft-computation-burden]] — 5 min of 8 kHz speech: 38 hours direct
- [[idft-4pt-via-fft]] — IDFT via the conjugate trick
- [[real-valued-fft-4pt]] — N-pt real via N/2-pt complex
- [[frequency-bin-256hz]] — 256 Hz @ fs=8192, N=64

### EEE 350
- [[covariance-of-x-and-x-plus-z]] — Cov(X, X+Z) bilinearity
- [[stick-breaking-iterated-expectations]] — two-stage random experiment
- [[polling-sample-size]] — how many voters? (Chebyshev vs CLT)
- [[map-detection-antipodal]] — unequal-prior MAP threshold
- [[mle-for-exponential-rate]] — λ̂ = 1/x̄
- [[fair-coin-significance-test]] — HW7 11.1.6: two-sided α = 0.05 via CLT
- [[lmse-discrete-pmf]] — HW7 12.2.3: Ŷ_L(X) = (5/8)X − 1/16
- [[lmse-continuous-pdf]] — HW7 12.2.4: X̂_L(Y) = (5/9)Y on triangular support
- [[mmse-vs-lmse-erlang]] — HW7 12.2.6: MMSE = LMSE in both directions

## Practice

- [[fft-fundamentals-set-01]] — EEE 404 DFT/FFT fundamentals
- [[prob-fundamentals-set-01]] — EEE 350 moments / multivariate / conditional
- [[asymptotics-set-01]] — EEE 350 Chebyshev / LLN / CLT
- [[inference-set-01]] — EEE 350 Bayesian / MLE / hypothesis testing
- [[eee-335-l36-cm-cl-set-01]] — EEE 335 L36: $C_M$ / $C_L$ at mirror + output nodes (diode-connected cap, parasitic enumeration, high-Z source Miller breakdown)
- **[[eee-335-final-set-01]]** — **EEE 335 Final Practice Set 01** (Tue 5/5 12:10–2:00 PM). 11 problems mixed difficulty covering all 10 problem types from [[eee-335-final-lecture-review]]: Q-point/small-signal, configuration choice, current-mirror biasing, basic gain cell + swing, CS HF (Miller + OCTC), cascode HF advantage, CM-loaded diff amp full pipeline ($A_d$, $A_{cm}$, CMRR, L36 pole/zero), T/F drill, MC + short answer, 2-stage cascade bonus. Master cheat-sheet anchor at end. ⭐
- [[generalization-set-01]] — **NEW 2026-05-01** — Zhang 2017 random-labels prediction (structured vs random data, train-test gap as diagnostic, mutual information $I(X;Y)$)

## Mistakes

- [[fft-gotchas]] — FFT / DSP common mistakes
- [[prob-gotchas]] — probability / statistics common mistakes
- [[diff-amp-frequency-response]] — EEE 335 diff-amp + current-mirror frequency-response gotchas (AC-ground reasoning, gate vs node Z, $C_{gd2} \parallel C_{gd4}$ approximation)
- [[mistakes/generalization]] — **NEW 2026-05-01** — generalization gotchas (training accuracy ≠ understanding; random-label test accuracy is chance-level $1/K$, not $0\%$)

## Summaries

### Learning meta (study skills + AI tutoring)
- [[article-2026-04-29-giles-oxford-ai-learning]] — *Giles.* Use AI as a Socratic tutor: retrieval practice, multi-level explanations, Bloom's-calibrated practice, no-embarrassment iterative re-explanation, proposition-extraction reading workflow
- [[article-2026-04-29-sung-ai-learning-faster]] — *Justin Sung.* Risk-vs-complexity gating + Bloom's top-3 belongs to humans (deeper diagnostic; survey-driven; the AI-feels-helpful illusion dismantled)

### Physical-Layer ML Roadmap
- [[article-2026-04-23-physical-layer-ml-roadmap]] — the 14-month roadmap (NVIDIA + Wi-Lab)

### Physical-Layer ML Roadmap — textbooks (NEW 2026-05-01)
**Full summaries (PDFs ingested):**
- [[textbook-prince-understanding-deep-learning]] — Prince UDL v5.0.3, the **primary DL textbook** (Phase 1–2)
- [[textbook-sutton-barto-rl]] — Sutton-Barto 2nd ed, the **RL canon** (Phase 3)
- [[textbook-mackay-itila]] — MacKay Information Theory, **LDPC chapters 47–50** (Phase 3)
- [[textbook-parr-matrix-calculus]] — Parr-Howard *Matrix Calculus*, one-sitting backprop math (Phase 1)

**Reference-card stubs (no PDF mirrored — Tier-1 lint-fix sweep, NEW 2026-05-01):**
- [[textbook-pysdr-lichtman]] — PySDR (Lichtman), the single most wireless-relevant free resource. Phase 1 M2 OFDM-from-scratch backbone.
- [[textbook-bishop-prml]] — Bishop PRML, the DSP↔ML identity bridge (Ch 13 HMM/Kalman + Ch 8 graphical models)
- [[textbook-goodfellow-deep-learning]] — Goodfellow/Bengio/Courville, theoretical reference (Ch 5–10 + 14–15)
- [[textbook-deep-learning-with-pytorch]] — Stevens et al., PyTorch internals (Ch 1–8)
- [[textbook-from-python-to-numpy]] — Rougier, NumPy vectorization (Phase 1 M2)
- [[textbook-deep-learning-with-python-chollet]] — Chollet, TensorFlow/Keras (Phase 2 M6 — Sionna prep)
- [[textbook-d2l-dive-into-deep-learning]] — Zhang et al., code-first companion to Prince
- [[textbook-murphy-pml-intro]] — Murphy, modern probabilistic ML encyclopedia
- [[textbook-ml-with-pytorch-scikit-learn]] — Raschka, sklearn → PyTorch bridge
- [[textbook-scientific-visualization-matplotlib]] — Rougier, publication-figure portfolio rule

### Physical-Layer ML Roadmap — papers
**Phase 1–3 ingested (2026-05-01):**
- **Foundational PHY-ML:** [[paper-oshea-hoydis-2017-autoencoder]], [[paper-aitaoudia-hoydis-2020-ofdm]], [[paper-dorner-2018-otaair]] — autoencoder-PHY thread.
- **NVIDIA Sionna:** [[paper-sionna-2022]], [[paper-sionna-rt-2023]] — the simulator + differentiable RT.
- **NVIDIA neural receivers:** [[paper-nrx-cammerer-2023]], [[paper-nrx-wiesmayr-2024]] — NRX line; Wiesmayr is the standard-compliant real-time version.
- **Wi-Lab DeepMIMO/DeepSense/LWM:** [[paper-deepmimo-2019]], [[paper-deepsense-6g-2023]], [[paper-lwm-2024]], [[paper-digital-twin-vision-2023]] — Alkhateeb's full stack.
- **Subdomain canon:** [[paper-csinet-wen-2018]] (CSI feedback), [[paper-radioml-oshea-2018]] (modulation classification + RadioML 2018.01A), [[paper-channel-charting-studer-2018]] (self-supervised positioning).

**Phase 4 ingested (NEW 2026-05-01 — Tier-1 sweep):**
- **Sionna RT calibration (M10):** [[paper-diff-rt-calibration-2024]] — Hoydis et al. 2024 IEEE TMLCN; gradient-based RT calibration on real DICHASUS measurements. **The method paper for the Phase 4 M10 NVIDIA-portfolio capstone.**
- **Wi-Lab 2026 LWM sequels (M12 reading):** [[paper-lwm-spectro-2026]] (Kim/Alikhani/Alkhateeb — MoE foundation model for I/Q spectrograms) + [[paper-lwm-temporal-2026]] (Alikhani/Malhotra/Hamidi-Rad/Alkhateeb — sparse spatio-temporal attention for channel trajectories).

**Phase 4 ingested (NEW 2026-05-01 — Tier-2 sweep, 6 papers):**
- **NVIDIA Aerial 2025 flagship line:** [[paper-sionna-research-kit-2025]] (Cammerer et al. — Jetson + Sionna + TensorRT 5G testbed) + [[paper-wiesmayr-salad-2025]] (Wiesmayr et al. — ACK/NACK-only link adaptation, beats OLLA by 15%).
- **Wi-Lab sim-to-real / digital-twin operationalization:** [[paper-morais-similarity-2026]] (Morais/Alikhani/Alkhateeb — task-aware dataset distance metric, Pearson > 0.85 with transfer performance) + [[paper-luo-dt-csi-feedback-2025]] (Luo/Khosravirad/Alkhateeb — site-specific digital twins for CSI compression with fidelity decomposition).
- **Wi-Lab V2V + RIS hardware:** [[paper-deepsense-v2v-2024]] (Morais/Charan/Alkhateeb — 120 km mmWave V2V dataset) + [[paper-osman-ris-oran-2025]] (Osman/Shekhawat/Alkhateeb — 1024-element 28-GHz RIS in 5G O-RAN, MILCOM 2025 Best Demo).

**Tier-3 ingested (NEW 2026-05-01 — foundational papers + RL coverage):**
- **Cammerer-cold-email prereq:** [[paper-gruber-2017-channel-decoding]] — Gruber/Cammerer/Hoydis/ten Brink 2017 (CISS); the foundational neural-decoder paper that started Cammerer's PhD line.
- **Phase 2 M6 generative trio:** [[paper-kingma-2013-vae]] (VAE) + [[paper-goodfellow-2014-gan]] (GAN) + [[paper-ho-2020-ddpm]] (DDPM diffusion) — the three foundational generative-modeling papers M6 reproduction needs.

### EEE 404
- [[slides-fft-core-equations]], [[slides-fft-idft]], [[slides-fft-implementation]], [[slides-fft-interpretation]], [[slides-fft-real-valued-signal]], [[slides-window-functions]], [[lab-7-fft]]
- [[homework-2026-04-27-eee-404-hw5]] — HW5: DTFT of cosines, window resolution, butterfly count, STM32 real-time budget
- **NEW 2026-04-29:** [[summary-eee-404-m6-neural-networks]], [[summary-eee-404-m7-frequency-domain]], [[summary-eee-404-m8-difference-equation]], [[summary-eee-404-m10-butterfly]], [[summary-eee-404-m11-effect-of-window-and-speech]] — Module 6/7/8/10/11 lecture-deck summaries
- **NEW 2026-04-29:** [[summary-eee-404-exam-2-review]] — Exam 2 practice exam handout summary
- **NEW 2026-04-29:** [[summary-eee-404-ec-ml-lab]] — EC ML lab source summary
- **NEW 2026-04-29:** [[summary-eee-404-ec-quantum-lab]] — EC Quantum lab source summary
- **NEW 2026-05-02:** [[lab-eee-404-project-2-fft-applications]] — Project 2 source summary: vowel analysis + real-time spectrum analyzer

### EEE 304
- [[slides-2026-05-04-eee-304-final-exam]] — **The actual final exam** (1 pp, 8 problems with specific numbers, 350 pts) + open-book reference panel
- [[slides-2026-05-04-eee-304-final-exam-preview]] — Final Exam Preview deck (8 pp, one slide/problem, May 4–6 exam window)
- [[lab-eee-304-lab-4-am-modulation]] — Lab 4: AM modulation + coherent vs envelope demodulation (Simulink + tada.wav fill-in-the-blanks)
- [[homework-2026-04-26-eee-304-hw7]] — HW7: cascaded modulation, TDM-PAM bandwidth, chopper-amplifier gain derivation

### Research — AirComp & Regret Learning (core)
- [[paper-unregrettable-hpsr]] — **HPSR 2026** Sabyrbek/Purisai/Tsiropoulou — regret-learning distributed power control (the algorithmic anchor)
- [[paper-aircomp-survey]] — Şahin & Yang 2023 — comprehensive AirComp survey
- [[paper-aircomp-feel-demo]] — Şahin 2022 — SDR demo of OAC for FEEL (the practical protocol template)
- [[paper-fsk-mv]] — Şahin et al. 2021 — non-coherent FSK majority vote
- [[paper-bpsk-complement]] — Wang et al. 2025 — two's-complement digital AirComp
- [[paper-md-aircomp-plus]] — Qiao et al. 2026 — blind massive digital AirComp
- [[paper-ncota-dgd]] — Michelusi 2024 — non-coherent over-the-air decentralized GD
- [[paper-uav-aircomp]] — Fu et al. 2021 — UAV-assisted AirComp (context only)

### Research — 6G Signal Design (for pipeline gap-analysis)
- [[paper-rethinking-edge-ai-spm]] — Azimi-Abarghouyi/Fischione/Huang 2025 (IEEE SPM) — CSIT-aware / blind / weighted taxonomy + fine-vs-coarse sync
- [[paper-experimental-ota-fl]] — Pradhan et al. 2025 — first 5G-NR-compliant OTA-FL testbed (PTP + Octoclock + Gold-sequence sync)
- [[paper-channel-aware-constellation]] — Li/Chen/Fischione 2025 — digital OTA with channel-randomness-as-constellation
- [[paper-itu-r-m2516]] — ITU-R 2022 — IMT-2030 (6G) framework
- [[paper-industrial-6g-ran]] — 2025 industry consensus on 6G RAN (SSB, feedback, AI-native)
- [[paper-signal-peak-power]] — 2025 — PAPR constraint in OTA-FL
- [[paper-6g-aircomp-foundations]] — Wang et al. 2022 — MIMO-focused 6G AirComp survey

### EEE 350
- [[slides-38-covariance]] — covariance, variance of sum, correlation, bivariate Gaussian
- [[slides-39-multivariate-vectors]] — random vectors, i.i.d., max of n, multivariate Gaussian
- [[slides-40-conditional-expectation]] — E[X|Y] as RV, iterated expectations, random sums
- [[slides-41-lln-clt-intro]] — Chebyshev, convergence
- [[slides-42-wlln]] — Weak LLN + polling
- [[slides-43-clt-apps]] — CLT, binomial approximation
- [[slides-43.5-bayesian-inference]] — MAP, LMS
- [[slides-44-mle-ci]] — MLE, confidence intervals
- [[slides-45-neyman-pearson]] — hypothesis testing, LRT
- [[slides-46-regression]] — linear + power-law
- [[slides-46.5-descriptive-stats]] — sample statistics, histogram
- [[slides-47-stochastic-processes]] — RP intro, white/colored noise, Poisson, Markov
- [[homework-2026-04-23-eee-350-hw7]] — **HW7** significance testing + MMSE/LMSE
- **NEW 2026-04-29:** [[summary-eee-350-m8-bernoulli-poisson-gaussian-rp]] — Module 8 (Week 15): Gaussian RPs + Bernoulli + Poisson processes (slides 47.5, 48, 49)
- **NEW 2026-04-29:** [[summary-eee-350-backfill-modules-1-5]] — catalog of slides 1–37.5 (Modules 1–5) backfilled from Canvas; raw `.pptx` files all on disk in `raw/slides/eee-350/`

### Daily research Q&A
- [[daily-2026-04-23-sdr-toolchain-questions]] — ⏸️ in-progress: WSL2 / Pluto toolchain walkthrough (paused at Vivado install)
- [[daily-2026-04-23-pluto-deployment-and-regret-learning]] — Pluto deployment architecture (Q1–Q5) + regret-learning deep dive (Q6–Q25)

### Workload planning
- [[daily-2026-04-28-workload]] — **Week of 4/28 → 5/12.** 24 items, 2 finals (EEE 404 Thu + EEE 304 Wed 5/6), Friday cliff with 11 items same day
- [[daily-2026-04-28-finals-prep]] — **Master finals prep.** Per-course study plan, wiki coverage audit, gaps to fill in EEE 341 + EEE 335
