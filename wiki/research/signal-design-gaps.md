---
title: Signal-Design Gaps in the Pipeline (Beacon / Sync / Data / Feedback)
type: research
course: [[research]]
tags: [signal-design, beacon, sync, feedback, 6g, gap-analysis]
sources: [[paper-rethinking-edge-ai-spm]], [[paper-experimental-ota-fl]], [[paper-channel-aware-constellation]], [[paper-itu-r-m2516]], [[paper-industrial-6g-ran]], [[paper-signal-peak-power]], [[paper-aircomp-feel-demo]]
created: 2026-04-21
updated: 2026-04-26
---

# Signal-Design Gaps — Beacon, Sync, Data, Feedback

Gap analysis against the 6G-research consensus (ITU-R, IEEE Signal Processing Magazine, 3GPP direction, major industry labs). Per-signal-type assessment of what [[system-pipeline]] gets right, what's under-specified, and what the literature says to do about it.

## 0. Framing — what "gap" means here

The pipeline is sound at the algorithm level ([[regretful-learning]]) but under-specified at the **signaling layer**. Many signal choices are inherited from [[paper-aircomp-feel-demo]] (5 Adalm Plutos, short-range indoor) and may not scale to 6G targets (cellular distances, massive device counts, heavy-tailed interference, NTN). This document identifies each gap and points at the paper that fills it.

---

## 1. Beacon signals (Stage 1 + Stage 3)

### What the pipeline currently says
Stage 1: Golay-32 × 4 sync preamble + Zadoff-Chu-97 CHEST + polar-128 header. Reuses [[paper-aircomp-feel-demo]]'s PPDU.

### Gaps found in 6G literature

**G1.1 — Separation of idle-mode vs connected-mode beacons.** [[paper-industrial-6g-ran]] notes this is a major 6G design principle: 6G separates idle and connected signals so data nodes can sleep. Jayden's current beacon serves both discovery (who's participating) and training trigger (go transmit now) in one signal. Split into:
- **Discovery beacon** (rare, wide-area): low rate, idle-mode devices wake up on it.
- **Training trigger** (per-epoch): short, high-rate, only for devices already associated.

**G1.2 — Beacon periodicity not specified.** [[paper-experimental-ota-fl]] runs beacon $+$ calibration $+$ training in coherence blocks ($\sim 100$ ms indoor). Pipeline should set beacon period $=$ fraction of $T_c \times$ margin. For 2.4 GHz indoor static: period $\sim 50$ ms; for outdoor mobile: $\sim 5$ ms.

**G1.3 — Power control on the beacon itself is missing.** [[paper-aircomp-survey]] Sec IV-B discusses per-beacon power control for ensuring edge EDs can receive. Set beacon TX power to guarantee cell-edge SNR $\geq 10$ dB. Without this, EDs at the cell edge silently drop out.

**G1.4 — 6G vs 5G NR numerology.** [[paper-experimental-ota-fl]] uses numerology 0 ($15$ kHz spacing, $66\ \mu$s symbols). For 6G sub-THz or mmWave, numerologies scale up: subcarrier spacing may be $120$ kHz–$1.92$ MHz. Pipeline should parameterize numerology, not hardcode $15$ kHz.

### Recommended concrete changes
- Introduce **two-tier beacon**: discovery beacon $+$ training trigger.
- Parameterize numerology: $(f_c, \text{SCS}, \text{CP})$ tuple per deployment.
- Specify beacon power and periodicity in the pipeline doc.

---

## 2. Synchronization signals

### What the pipeline currently says
Gold codes (or Golay — see [[robust-signaling]] for the distinction) for frame sync; assumes sync precision from [[paper-aircomp-feel-demo]] of $\sim 1\ \mu$s jitter.

### Gaps found in 6G literature

**G2.1 — Fine vs coarse sync is not made explicit.** This is the single most important gap. Per [[paper-rethinking-edge-ai-spm]] Sec II-B:

| Sync regime | What it means | When required |
|---|---|---|
| **Fine sync** | Symbol-level timing $+$ tight CFO $+$ phase-coherent | CSIT-aware schemes with channel inversion (HPSR-style) |
| **Coarse sync** | Frame-level timing $+$ moderately stable carriers | Blind / weighted / FSK-MV schemes |

Jayden's HPSR-based pipeline **needs fine sync** because the utility function relies on magnitude alignment — which implicitly requires coherent superposition. The pipeline should say so, budget for it explicitly, and describe how fine sync is achieved.

**G2.2 — PTP $+$ Octoclock or equivalent is required.** [[paper-experimental-ota-fl]] proves sub-$\mu$s sync is achievable via a dual-layer scheme:
- **Host-level: PTP (IEEE 1588)** over Ethernet — synchronizes companion computer clocks via NIC hardware timestamps.
- **SDR-level: shared clock/PPS distribution** (e.g., Octoclock-G) — synchronizes radio hardware with equal-length cables.

Without this dual layer, Jayden's aggregation will fail coherent combining — paper demonstrates garbage output in Fig 5a when PTP is off.

**G2.3 — CFO correction not specified.** CFO accumulates phase error over the packet. [[paper-aircomp-feel-demo]] tracks CFO via $4\times$ Golay repetition. [[paper-experimental-ota-fl]] relies on Octoclock for frequency; if that's unavailable, pipeline must add pilot-subcarrier phase tracking mid-packet (typically a pair of QPSK Golay-64 tracking symbols every $N$ data symbols).

**G2.4 — $\alpha$-stable interference not modeled.** [[paper-rethinking-edge-ai-spm]] Sec V-B $+$ [[paper-signal-peak-power]] cite [Clavier 2021] showing real IoT interference is **heavy-tailed ($\alpha$-stable), not Gaussian**. Jayden's AWGN assumption is optimistic. Sync detection thresholds need adjustment (standard matched-filter thresholds underperform under impulsive noise).

### Recommended concrete changes
- Explicitly declare **fine sync regime** in the pipeline preamble.
- Add PTP (or GPS-PPS if outdoor) $+$ clock distribution to the hardware requirements.
- Add CFO tracking symbols mid-packet.
- Replace Gaussian noise assumption with $\alpha$-stable in simulation analyses.

---

## 3. Data signals (Stage 4 AirComp transmission)

### What the pipeline currently says
Stage 4: all EDs transmit simultaneously on same OFDM subcarriers using known training amplitudes. Each ED transmits $x_n = \sqrt{P_n} \cdot s_n$.

### Gaps found in 6G literature

**G3.1 — Training vs operational mode not distinguished.** [[paper-rethinking-edge-ai-spm]] Sec II-A clearly separates pilot training signals from data signals. Jayden's "known training amplitudes" is equivalent to a pilot — works for MSE measurement but can't be maintained during real aggregation. Need both:
- **Training mode**: known amplitudes $\to$ MSE measurement, regret update.
- **Operational mode**: random $s_n$ data symbols $\to$ live aggregation, no ground-truth MSE. Variance-based quality estimation instead.

**G3.2 — Peak Power (PAPR) constraint ignored.** [[paper-signal-peak-power]] shows OTA-FL gradients have high PAPR by distribution (unlike uniform symbols). For $N > 100$, receiver ADC saturation is a real risk. Jayden's pipeline should either:
- Apply per-ED randomization (QPSK-phase scramble like [[paper-fsk-mv]]).
- Use tone reservation (reserve a few OFDM tones for PAPR cancellation).
- Budget $\text{OBO}_{\min}$ $\to$ reduces effective cell radius (trade-off per [[paper-aircomp-survey]] Eq 44).

**G3.3 — Channel-aware constellation alternative unconsidered.** [[paper-channel-aware-constellation]] shows a **completely different data-signal design philosophy**: instead of pre-equalizing to cancel the channel, use the channel randomness as the demodulation constellation. Key finding: **small cells $\to$ pre-equalize (Type I), large cells $\to$ blind (Type II)**. Jayden's pipeline is Type I implicitly — good for small-range indoor, bad for cellular.

**G3.4 — Instantaneous peak-power vs average-power constraint confusion.** HPSR uses average power constraint $\mathbb{E}[P_n] \leq P_{\max}/L$ but real regulators (FCC/ETSI) enforce peak EIRP. Pipeline needs to distinguish. Per [[paper-rethinking-edge-ai-spm]] Eq 1, most AirComp schemes assume average; truly cellular-compliant deployment needs instantaneous constraint.

### Recommended concrete changes
- Split Stage 4 into **training sub-mode** (known amps, measure MSE) and **operational sub-mode** (random $s_n$, aggregate, infer MSE from variance).
- Add per-ED QPSK randomization to reduce PAPR.
- Document the Type I/II transmit-coefficient choice (pre-equalize vs blind) and when to use each.
- Specify peak vs average power constraint explicitly.

---

## 4. Feedback signals (Stage 6)

### What the pipeline currently says
ES broadcasts MSE + per-ED aggregate sums (or full channel vector) over OFDM with polar coding.

### Gaps found in 6G literature

**G4.1 — CSI compression direction.** Industry/3GPP consensus (per [[paper-industrial-6g-ran]] and the Keysight/Samsung 2025 research) is that **AI-based CSI compression** (autoencoder two-sided models, JSCM) is standard for 6G. For $N=100$ EDs, 16-bit CSI $\times N = 1600$ bits per feedback. Autoencoder compression typically reduces this $5$–$10\times$. Pipeline could use a small autoencoder at the ES (compressor) $+$ matching decoder at each ED.

**G4.2 — Feedback channel coding.** [[paper-aircomp-feel-demo]] uses polar-128 rate-$1/2$ $+$ CRC-8 (5G NR control-channel style). This is a sound choice but should be parameterized:
- Short feedback ($<\,200$ bits): polar-128 $+$ CRC-8 (current).
- Medium feedback ($200$–$1000$ bits): polar-512 or LDPC, CRC-16.
- Long feedback ($>\,1000$ bits, with CSI): LDPC rate-$1/3$ $+$ CRC-24.

**G4.3 — Feedback channel design direction.** [[paper-industrial-6g-ran]] notes 6G will likely move feedback from PUCCH/UCI-on-PUSCH (5G NR) to **MAC Control Elements (MAC-CEs)** — lower overhead, more flexible. Jayden's pipeline currently has feedback as a dedicated physical-layer OFDM field, which is architecturally fine but doesn't map cleanly to any 5G NR channel. **For standards alignment**: treat the feedback as a MAC-CE payload encoded at PHY using polar coding.

**G4.4 — MSE-only feedback is too narrow.** Jayden's feedback carries MSE $+$ aggregate sums. [[paper-experimental-ota-fl]] observes that **gradient magnitude information** is sometimes more valuable than scalar MSE for learning quality. Consider extending feedback to include:
- Per-ED reliability flags ($|\hat{h}_n|^2$ quality indicator).
- Byzantine detection hints (per [[paper-aircomp-survey]] Sec IV-E).
- Adaptive inertia $\mu$ broadcast (HPSR paper's Sec IV-D adaptive scheme).

**G4.5 — No forward error correction on the aggregate scalars themselves.** The aggregate sum $\sum g(|h_{n'}|) \cdot \sqrt{P_{n'}}$ is broadcast as a floating-point number ($32$ bits per scalar). A single bit error makes utility computation wrong. CRC protects the frame but numerical error-correcting codes (e.g., Reed-Solomon over finite precision integers) add another layer for safety.

### Recommended concrete changes
- Compress CSI with a small autoencoder ($\sum g \cdot \sqrt{P}$ $+$ $\sum g^2 \cdot P$ per-ED aggregates, not full channel vector) — $\sim 70\%$ bandwidth reduction.
- Parameterize FEC strength by payload length (polar-128 / polar-512 / LDPC).
- Extend feedback with adaptive-$\mu$ $+$ reliability flags.
- Add finite-precision RS code on aggregate scalars.

---

## 5. Summary — pipeline sections to revise

| Pipeline section | Gap-analysis finding | Recommendation |
|---|---|---|
| Stage 1 beacon | Single-beacon for discovery $+$ training (G1.1) | Split into two beacons |
| Stage 1 numerology | Hardcoded $15$ kHz (G1.4) | Parameterize $(f_c, \text{SCS}, \text{CP})$ |
| Stage 1 beacon power | Unspecified (G1.3) | Set to guarantee edge-ED SNR $\geq 10$ dB |
| Stage 1 beacon period | Unspecified (G1.2) | Tie to $T_c \times$ margin |
| Sync regime | Implicit fine-sync (G2.1) | Declare fine-sync explicitly, justify |
| Sync implementation | Unspecified (G2.2) | PTP $+$ Octoclock (or GPS-PPS outdoor) |
| CFO correction | Missing (G2.3) | Pilot-subcarrier phase tracking mid-packet |
| Noise model | Gaussian AWGN (G2.4) | Use $\alpha$-stable in analyses |
| Stage 4 modes | Only training-mode (G3.1) | Add operational-mode with random $s_n$ |
| Stage 4 PAPR | Ignored (G3.2) | Per-ED QPSK randomization or tone reservation |
| Stage 4 constellation | Type I hardcoded (G3.3) | Document Type I/II choice by cell size |
| Stage 4 power constraint | Average only (G3.4) | Specify peak $+$ average |
| Stage 6 CSI format | Full vector (G4.1) | Compress via autoencoder |
| Stage 6 FEC | Polar-128 only (G4.2) | Parameterize by payload length |
| Stage 6 content | MSE $+$ aggregates (G4.4) | Add adaptive-$\mu$, reliability flags |
| Stage 6 numerical safety | CRC only (G4.5) | Add RS on aggregate scalars |

---

## 6. Open questions for Jayden

1. **Target regime** — indoor testbed (like [[paper-aircomp-feel-demo]], $5$ m range), outdoor cellular (like [[paper-experimental-ota-fl]], $20$ m), or large-cell 6G ($100$ m$+$)? Each picks a different point in the gap matrix.
2. **Scheme family** — stay CSIT-aware (HPSR as specified), or evaluate blind / weighted alternatives from [[paper-rethinking-edge-ai-spm]]?
3. **Hardware** — Adalm Pluto (small, $20$ PPM oscillator jitter), USRP X310 (better, Octoclock capable), or full gNB-like equipment?
4. **Protocol-layer fit** — strict 5G NR numerology, or custom?
5. **Feedback compression** — worth the ML overhead (autoencoder needs training), or skip and use raw-scalar broadcast?

---

## Related
- [[system-pipeline]] — the pipeline being analyzed
- [[robust-signaling]] — the sync/FEC catalog
- [[regretful-learning]] — the algorithm anchor
- [[paper-rethinking-edge-ai-spm]] — fine vs coarse sync taxonomy
- [[paper-experimental-ota-fl]] — concrete PTP-based implementation
- [[paper-channel-aware-constellation]] — alternative data-signal design
- [[paper-signal-peak-power]] — PAPR analysis
- [[paper-industrial-6g-ran]] — industry direction on signals
- [[paper-itu-r-m2516]] — ITU-R framework
