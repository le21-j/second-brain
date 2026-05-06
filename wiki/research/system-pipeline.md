---
title: System Pipeline — AirComp with Regret-Learning Power Control
type: research
course:
  - "[[research]]"
tags: [aircomp, regret-learning, system-design, protocol, ppdu, wifi-inspired]
sources:
  - "[[paper-unregrettable-hpsr]]"
  - "[[paper-aircomp-feel-demo]]"
  - "[[paper-aircomp-survey]]"
  - "[[daily-2026-04-23-pluto-deployment-and-regret-learning]]"
created: 2026-04-21
updated: 2026-05-06
---

# System Pipeline

End-to-end protocol for an AirComp system implementing the game-theoretic distributed power-control scheme of [[paper-unregrettable-hpsr]]. One ES, $N$ EDs, OFDM signaling, WiFi-inspired control plane.

**Design goals:**
1. Each ED learns $|h_n|$ (needed by [[regretful-learning]] utility) — without global CSI exchange.
2. Only participating EDs contribute — straggler-robust.
3. Training rounds allow the ES to compute MSE against a known reference.
4. Per-epoch feedback carries MSE $+$ aggregate scalars so EDs can update their power-selection probabilities locally.
5. All control signaling is protected by sync sequences $+$ FEC $+$ CRC.

## 0. System model and assumptions

| Parameter | Value / Meaning |
|---|---|
| $N$ | Number of EDs. Paper evaluates up to 100. |
| $L$ | Quantization levels per ED's strategy space. Paper uses $L = 100$. |
| $P_n \in \{0, P_{\max}/L, \ldots, P_{\max}\}$ | Discrete transmit power options at ED $n$. |
| $P_{\max}$ | Peak power budget, e.g., $1$ W. |
| $\eta$ | Denoising factor at ES, fixed. Paper uses $\eta = 0.5$. |
| $\alpha$ | Channel-projection exponent in $g(|h_n|) = 1/|\log|h_n||^\alpha$. Paper uses $\alpha = 0.1$. |
| $\mu$ | Inertia parameter for regret matching. Paper uses $\mu = 3000$ (constant) or adaptive. |
| $\sigma^2$ | AWGN variance at ES. Paper uses $\sigma^2 = 10^{-12}$. |
| $f_c$ | Carrier frequency. Paper uses $2.405$ GHz (ISM band, WiFi-friendly). |
| Channel model | 3GPP TR 38.901 UMi Street Canyon (outdoor) or InH Office (indoor). |

**Assumption of TDD reciprocity:** the channel estimated on the DL beacon (Stage 1) is used for the UL AirComp transmission (Stage 4). Valid if the turnaround is faster than the channel coherence time ($T_c \approx 10$–$100$ ms indoors at $2.4$ GHz).

## 1. Pipeline overview

```
┌──────────┐  Beacon #1   ┌──────────┐
│   ES     ├─────────────→│   EDs    │  Stage 1: DL beacon → each ED runs LS
└──────────┘              └──────────┘           to estimate |h_n|.

┌──────────┐   per-ED ACK + CSI reports (TDMA)   ┌──────────┐
│   EDs    ├────────────────────────────────────→│   ES     │  Stage 2: participants ACK,
└──────────┘                                     └──────────┘           upload |ĥ_n|.

┌──────────┐  Beacon #2 (training trigger)  ┌──────────┐
│   ES     ├───────────────────────────────→│   EDs    │  Stage 3: sync waveform, assigns
└──────────┘                                └──────────┘           training amplitudes.

┌──────────┐   simultaneous training transmission   ┌──────────┐
│   EDs    ├───────────────────────────────────────→│   ES     │  Stage 4: AirComp with
└──────────┘                                        └──────────┘           known amplitudes.

┌──────────┐   (local: ES computes MSE against reference)   
└──────────┘                                                         Stage 5: MSE measurement.

┌──────────┐   DL feedback (MSE + aggregates)   ┌──────────┐
│   ES     ├───────────────────────────────────→│   EDs    │  Stage 6: broadcast feedback,
└──────────┘                                    └──────────┘           each ED updates ψ^{t+1}.

┌──────────┐    per-ED ACK of feedback (TDMA)   ┌──────────┐
│   EDs    ├────────────────────────────────────→│   ES     │  Stage 7: confirm receipt;
└──────────┘                                     └──────────┘           non-ACKers reuse prior P_n.
```

---

## Stage 1. Downlink beacon + per-ED channel estimation

**What happens.** ES broadcasts a structured beacon. Every ED that hears it estimates its own scalar $|h_n|$ via least squares against the known pilot.

**Signal structure** (see [[robust-signaling]] for rationale):
- Preamble: **Golay-32 repeated $4\times$**, BPSK, RRC pulse shape. Provides time sync $+$ CFO estimation.
- CHEST field: one OFDM symbol carrying a **Zadoff-Chu-97** sequence on every other active subcarrier. Nulled subcarriers used for noise-variance estimation.
- Header: 1 OFDM symbol, polar-128 rate-$1/2$ $+$ CRC-8. Carries beacon sequence number, network ID, next-stage timing info.

**At each ED.** After frame sync detection and CFO correction, ED runs LS on the CHEST field:

$$\hat{h}_n = (p^H r_n) / L \quad \text{(LS on pilot sequence } p\text{)}$$

$$|\hat{h}_n|^2 = |p^H r_n|^2 / L^2 \quad \text{(magnitude; what [[regretful-learning]] actually consumes)}$$

**Fact-check against papers:**
- [[paper-aircomp-feel-demo]] uses identical sequence choices (Golay-32 sync, ZC CHEST) and validates them on Adalm Pluto SDRs at $15$ MHz bandwidth.
- [[paper-unregrettable-hpsr]] assumes $|h_n|$ is known but does not specify how it is obtained. Jayden's LS-from-beacon approach is the obvious practical realization and consistent with standard TDD assumptions.
- **TDD reciprocity** is an implicit assumption. If the DL and UL channels diverge (FDD, high mobility) then the $|h_n|$ used at the ED for utility computation (Stage 6) will not match the channel on the UL AirComp round (Stage 4). For a static/indoor testbed this is fine.

---

## Stage 2. Per-ED ACK + CSI reporting

**What happens.** After the beacon, each ED gets an allotted slot (TDMA within the contention window) to ACK and report its $|\hat{h}_n|$. EDs that fail to ACK or report within their window are dropped from this epoch.

**Protocol pattern (WiFi-inspired):**
- ES beacon's header includes the list of allocated AIDs (Association IDs — short integer user IDs) and their time offsets. Analogous to a TIM IE in 802.11.
- ED $n$ transmits during its slot $[t_0 + n \cdot T_{\text{slot}}, t_0 + (n+1) \cdot T_{\text{slot}})$.
- Payload:
  - Short preamble ($4$ Golay repetitions) for timing.
  - 1 OFDM symbol carrying $\{\text{AID (25 bits)}, |\hat{h}_n|^2 \text{ quantized to 16 bits}, \text{status flags}\}$, polar-128 $+$ CRC-8.
- **Participation logic:** if ES does not detect a valid, CRC-clean ACK in ED $n$'s window $\to n$ is marked inactive for this epoch.
- **NACK handling:** if ED detects a CRC failure on its own beacon reception, it sends a NACK in its slot; the ES excludes it.

**User ID assignment.** On bootstrap each ED registers once and receives a persistent AID. Subsequent beacons reference AIDs; no association overhead per-round.

**Gold codes (optional robustness layer).** If slot collisions are possible (e.g., multiple EDs miscounting their slot indices), each ED can scramble its ACK payload with a per-AID **Gold code**. The ES descrambles with each code in parallel — low cross-correlation between codes lets it separate simultaneous transmitters. See [[robust-signaling]] for the distinction between Gold and Golay.

**Fact-check against papers:**
- [[paper-aircomp-feel-demo]] uses essentially this pattern in its calibration procedure (Fig 2): each ED responds to a trigger with a ZC sequence in its assigned slot.
- Dropping non-responders matches the "absentee votes" concept in [[paper-fsk-mv]] — EDs not confident in their gradient abstain.
- Reporting $|\hat{h}_n|^2$ uplink costs $16$ bits $\times N$ per epoch. For $N=100$ this is $1600$ bits of overhead per epoch. Alternative: let the ES estimate $|h_n|$ from the UL ACK itself (ZC preamble in the ACK slot gives the ES a per-ED channel measurement for free). Consider switching to this.

---

## Stage 3. Second beacon — training-round trigger and amplitude assignment

**What happens.** ES broadcasts a second beacon that (a) provides sync for simultaneous UL transmission, (b) tells each participating ED which **known training amplitude** $a_n$ to transmit at.

**Signal structure.**
- Reuses Stage 1 PPDU frame template.
- Header signals $\{\text{epoch ID}, \text{training bit} = 1, \text{feedback channel map}\}$.
- Data field: per-ED amplitude assignment table — $\{\text{AID} \to a_n\}$. Polar-128 $+$ CRC-8.

**Amplitude assignment.** During the training phase, amplitudes $a_n = \sqrt{P_n}$ are pre-allocated (e.g., all EDs assigned $a_n = \sqrt{P_{\max}/2}$) and **known at both ends**. This makes Stage 5 MSE computation possible — the ES knows what it *should* receive and can compare against what it *did* receive.

**Note on renumbering.** The user's original pipeline labeled this "Fourth Step" but skipped "Third." I've renumbered so stages are 1–7 contiguous. Original semantics preserved.

**Fact-check:**
- [[paper-aircomp-feel-demo]] uses a gradient-trigger beacon (`t_grd` $+$ sync) to fire simultaneous UL transmissions. Same pattern.
- [[paper-unregrettable-hpsr]] models $s_n$ as zero-mean unit-variance **data** symbols, not training pilots. Using known training amplitudes is a **deviation** — but necessary if we want the ES to measure MSE during training. In production (post-training) the pipeline would switch back to real data symbols. Consider two modes: **training mode** (known $a_n$, compute MSE) and **operational mode** (random $s_n$, infer MSE from variance).

---

## Stage 4. AirComp uplink transmission

**What happens.** All participating EDs transmit simultaneously using the ES-assigned training amplitudes, pre-compensated for their own channel magnitudes.

**Per-ED transmission.** ED $n$ transmits:

$$x_n(t) = a_n \cdot s_{\text{train}}(t)$$

where $s_{\text{train}}(t)$ is a reference waveform common to all EDs (e.g., an OFDM training symbol with QPSK on active subcarriers).

**At the ES.** Received signal:

$$y(t) = \sum_n h_n \cdot x_n(t) + w(t) = \sum_n h_n \cdot a_n \cdot s_{\text{train}}(t) + w(t)$$

**Phase coherence is critical.** For the superposition to be constructive, all EDs must transmit at the same instant with negligible CFO drift. This is achieved by:
- Common sync from Stage 3 beacon.
- Per-ED time-offset correction baked into the calibration phase ([[paper-aircomp-feel-demo]] Fig 2).
- Optional: closed-loop CFO tracking via pilot subcarriers.

**Fact-check:**
- [[paper-unregrettable-hpsr]] Eq 2 is this exact signal model.
- [[paper-aircomp-feel-demo]] demo achieved $\sim 1\ \mu$s sync error — adequate for non-coherent FSK-MV but probably too loose for coherent magnitude-alignment. Jayden may need tighter sync (sub-sample, via a PLL or GPS-disciplined oscillator).
- **Open question:** does HPSR assume phase-coherent superposition, or just magnitude alignment? Re-reading Eq 2: the sum is coherent (no $|\cdot|$ around the sum). So phases of $h_n \cdot s_n$ must align. This requires either (a) phase-inverting at each ED (requires full complex CSI, contradicting the "only magnitude needed" claim), or (b) same data $s_n$ plus random phase absorbed into $s_n$'s variance, or (c) a non-coherent receiver. Worth clarifying with Jayden before implementation.

---

## Stage 5. MSE measurement at ES

**What happens.** ES compares the received superposed signal $y$ against what it *should* have received given the known training amplitudes and estimated channels (from Stage 2 CSI reports).

**Expected signal.** If the ES knows all $\{a_n\}$ and $\{|\hat{h}_n|\}$ from Stage 2:

$$y_{\text{expected}} = \sum_n |\hat{h}_n| \cdot a_n \cdot s_{\text{train}} \quad \text{(assuming coherent phase alignment)}$$

**Measured MSE per epoch.**

$$\text{MSE} = \frac{1}{K \cdot T_{\text{train}}} \cdot \sum_t |y(t) - y_{\text{expected}}(t)|^2 \quad \text{(averaged over training samples)}$$

where $K$ is the number of samples and $T_{\text{train}}$ the training duration.

**Or equivalently** in the form of [[paper-unregrettable-hpsr]] Eq 4:

$$\text{MSE} = \frac{1}{N^2} \cdot \sum_n \left(\frac{|\hat{h}_n| \cdot a_n}{\sqrt{\eta}} - 1\right)^2 + \frac{\sigma^2}{N^2 \cdot \eta}$$

This form lets the ES break down per-ED contribution and feed back useful diagnostics.

**Fact-check:** directly matches the HPSR MSE formulation.

---

## Stage 6. Feedback broadcast — MSE + aggregate sums for utility update

**What happens.** ES broadcasts a feedback frame containing the MSE and the aggregate scalars each ED needs to compute its [[regretful-learning]] utility.

**What the ES broadcasts:**
- $\text{MSE}^t$ — the current-epoch MSE (optional diagnostic).
- For each ED $n$ (addressed by AID): $S_1(n) = \sum_{n' \neq n} g(|\hat{h}_{n'}|) \cdot \sqrt{P_{n'}}$ and $S_2(n) = \sum_{n' \neq n} g(|\hat{h}_{n'}|)^2 \cdot P_{n'}$.
- Current epoch ID.
- Next-epoch schedule (timing of next beacon).

**Bandwidth.** $2$ scalars per ED $\times 32$ bits each $= 64$ bits/ED. For $N=100$, $6400$ bits per feedback frame. Fits in a few OFDM symbols with polar coding.

**User's original design.** Jayden's Step 6 says "channel gains of the other ED" — i.e., broadcast $\{|\hat{h}_{n'}|\}_{n'}$ to all EDs, who then compute the sums locally. This is **more bandwidth-intensive** ($N \times 16$ bits $= 1600$ bits for $N=100$, times $N$ receivers). But:
- **Simpler** — no per-ED custom sums, just broadcast the full vector once.
- **More flexible** — EDs can compute alternative utility functions or diagnostics without ES re-work.
- **Easier to prototype** — less bookkeeping at ES.

**Recommendation:** start with Jayden's design (broadcast $\{|\hat{h}_{n'}|\}$), profile bandwidth, switch to per-ED aggregates only if needed.

**At each ED.** On receiving the feedback:
1. Compute counterfactual utility $U_n(a_k, P^t_{-n})$ for every alternative power action $a_k$.
2. Update running average regret $D^t_n[j,k]$.
3. Compute positive regret $R^t_n[j,k] = \max(D^t_n[j,k], 0)$.
4. Update probability vector $\psi^{t+1}_n$ via regret matching.

**Fact-check:**
- [[paper-unregrettable-hpsr]] Sec III explicitly states "the overall signal stemming from the rest of the devices… can be easily broadcasted by the edge server without requiring personalized information for each device." The paper recommends aggregate sums; Jayden's "full channel gains" design is a flexibility/bandwidth trade-off.
- [[paper-aircomp-feel-demo]] uses DL feedback (`t_feed`, `t_mv`) for exactly this kind of closed-loop control.

---

## Stage 7. Feedback ACK + fallback

**What happens.** Each participating ED ACKs that it successfully received and decoded the feedback. If an ED fails to ACK, it is flagged; in the **next epoch** that ED reuses its current $P_n$ selection rather than updating.

**Protocol pattern.** Identical to Stage 2 — per-AID TDMA slot, polar-128 $+$ CRC-8 payload carrying $\{\text{AID}, \text{ACK/NACK}, \text{hash of received feedback}\}$.

**Why reuse the previous power on failure.** If an ED updated without valid feedback, its $\psi^{t+1}$ would be based on stale regret — worse than the known-okay $P^t$. "Inertia" is the default behavior in regret matching ($\psi^{t+1}(a_j)$ is the residual probability of keeping the current action); non-update extends this naturally.

**Fact-check:**
- Matches WiFi block-ACK patterns (aggregate ACKs into one frame if possible).
- [[paper-unregrettable-hpsr]] does not model feedback loss. This is a real-world robustness addition beyond the paper.

---

## 2. Robustness layer summary

See [[robust-signaling]] for the full catalog. The pipeline uses:

| Layer | Mechanism |
|---|---|
| Frame sync | Golay-32 $\times$ 4 repetitions (BPSK, RRC) |
| Channel estimation | Zadoff-Chu-97 in CHEST field |
| Control FEC | Polar-128, rate $1/2$, BPSK, CRC-8 |
| Data FEC | Polar-128, rate $1/2$, BPSK, CRC-8 (reused) |
| User ID | 25-bit AID (from association) $+$ optional Gold-code scrambling per AID |
| Timing sync | Beacon TSF-style broadcast; per-ED offset corrected via calibration feedback |
| CFO correction | Pilot-subcarrier phase tracking (QPSK Golay-64) |

---

## 3. Implementation status

**What exists.**
- Schema (this file), summaries of 8 anchor papers, concept pages for [[aircomp-basics]], [[regretful-learning]], [[channel-estimation]], [[robust-signaling]].
- Code scaffolding at `aircomp-regret-pluto/` (top-level folder; previously `implementation/`): C firmware, SystemVerilog HDL, Python reference, Vivado build scripts.

**What does not yet exist in this vault.**
- No ED or ES Python scripts are currently in `raw/`. Jayden mentioned "can you please update both the ED and ES script" — those scripts must live elsewhere (external repo? local dev folder?). **Before any implementation work, drop the current ED/ES scripts into `raw/` or tell me where they are.**

**Build toolchain.** The three-artifact pipeline (FPGA bitstream via Vivado, ARM binary via cross-compiler, merged by `plutosdr-fw`) is documented at [[pluto-build-toolchain]]. Windows-host setup via WSL2 is [[wsl2-embedded-workflow]]. The specific cross-compiler is [[gcc-arm-linux-gnueabihf]]; the general concept is [[cross-compilation]]. In-progress walkthrough: [[daily-2026-04-23-sdr-toolchain-questions]] (paused at Vivado install).

**Runtime model.** Once flashed, the 5 Plutos coordinate **wirelessly**; USB is out of the real-time path entirely. See [[pluto-experiment-lifecycle]] for the flash-once / launch-each-epoch split and the honest caveats on remaining jitter (Linux scheduling + TCXO drift).

**PS/PL split.** Sample-rate DSP (Golay correlator, 128-pt FFT, CP add/remove, LS channel estimator, CRC) lives in the FPGA fabric; epoch-rate logic (FSM, regret matching, PPDU framing, libiio config) runs in C on the ARM. See [[zynq-ps-pl-split]] for the rationale and what each half is doing during an epoch.

**Pre-flash verification.** Code changes ride the [[pre-flash-test-pyramid]] — Python algorithmic tests (Layer 1) and C host compile + run (Layer 3) catch most bugs before the reflash bill.

**Benchtop config.** For 4-Pluto bench bring-up: $L = 4$ power levels, $P_{\max} = 1$ mW (action set $\{0.25,\,0.50,\,0.75,\,1.00\}$ mW). Convergence in $\sim 3$ rounds vs $\sim 50$ at paper scale. See [[regretful-learning]] § "Implementation notes" and [[aircomp-utility-s1-s2]] for how the two-scalar feedback decomposes the utility.

**Staged implementation plan (suggested):**
1. **Phase A — Core algorithm in Python (no RF):** simulate the regret-learning algorithm on random channel draws. Verify convergence matches the HPSR paper's Fig 1 ($10$ EDs, MSE $\sim 8 \times 10^{-8}$, regret $\to 0$ in $\sim 30$ iterations).
2. **Phase B — Add protocol stubs:** ED/ES classes with the 7 stages as methods. Replace actual RF with AWGN simulation.
3. **Phase C — PPDU $+$ FEC:** build the Golay/ZC/polar pipeline in software. Test in simulation.
4. **Phase D — SDR port:** target Adalm Pluto or USRP. Follow [[paper-aircomp-feel-demo]]'s IP core approach.

---

## 3a. Signal-design gaps (6G research cross-check)

A dedicated gap analysis against 2024–2026 6G research lives in **[[signal-design-gaps]]**. High-priority findings:

- **Sync regime is implicit — declare it.** Pipeline requires **fine sync** (symbol-level $+$ tight CFO/phase) because of HPSR's coherent magnitude alignment. See [[paper-rethinking-edge-ai-spm]] Sec II-B for the taxonomy.
- **PTP (IEEE 1588) $+$ Octoclock is the validated way to get sub-$\mu$s sync on commodity SDRs.** See [[paper-experimental-ota-fl]].
- **Split Stage 4 into training-mode (known amplitudes) and operational-mode (random data).** Current pipeline only covers training. PAPR becomes a real issue in operational mode — see [[paper-signal-peak-power]].
- **Split Stage 1 beacon into discovery $+$ training-trigger**, per 6G industry consensus. See [[paper-industrial-6g-ran]].
- **Consider blind or weighted alternatives** to the currently-CSIT-aware design. [[paper-rethinking-edge-ai-spm]] shows weighted (WAFeL) beats CSIT-aware by $\sim 15\%$ accuracy with less CSI overhead.
- **Add CFO-tracking pilot subcarriers** mid-packet. Not in the current PPDU template.
- **Compress feedback via autoencoder** (6G CSI-compression direction). $\sim 70\%$ bandwidth saving on Stage 6.

## 4. Open questions / decisions needed

1. **Phase coherence.** Does HPSR's Eq 2 require phase coherence (if so, how is it achieved without full complex CSI), or is there an implicit non-coherent path? See Stage 4 fact-check above. Jayden should clarify or pick one.
2. **Training-mode vs operational-mode.** Pipeline's Stage 4–5 uses known training amplitudes to compute MSE. Does the system ever run in "operational mode" with random data symbols? If so, how is MSE inferred post-training?
3. **Feedback content — scalar aggregates vs full channel vector.** See Stage 6 recommendation. Current default: broadcast $\{|\hat{h}_{n'}|\}$, $\sim 1600$ bits for $N=100$. Optimizable to $6400$ bits of per-ED aggregates (actually larger! — re-check whether aggregate-per-ED is really cheaper for this $N$).
4. **Reciprocity.** TDD assumed. Does the target deployment satisfy this?
5. **Stage 3 naming.** User's original pipeline skipped "Third Step." Renumbered here to 1–7. Confirm this is correct.
6. **ED/ES scripts location.** See Implementation status above.

---

## Related
- [[federated-learning]] — **the umbrella ML paradigm this pipeline implements** (specifically OTA-FL, the analog-aggregation flavor); cold-email-relevant cross-pollination with the broader [[python-ml-wireless]] roadmap.
- [[paper-unregrettable-hpsr]] — the algorithmic anchor
- [[paper-aircomp-feel-demo]] — the practical protocol template
- [[paper-aircomp-survey]] — theoretical background
- [[regretful-learning]] — the algorithm
- [[hmc-psi-rebuild]] — HMC ψ update semantics (the nuance behind Stage 6's regret update)
- [[aircomp-utility-s1-s2]] — the `(S1, S2)` aggregate feedback format
- [[aircomp-basics]] — the channel/MSE model
- [[channel-estimation]] — Stage 1 detail
- [[robust-signaling]] — sync/FEC details
- [[zynq-ps-pl-split]] — how each pipeline stage maps to PS or PL on the Pluto
- [[pluto-experiment-lifecycle]] — how the pipeline actually runs across 5 devices post-flash
- [[pluto-build-toolchain]] — the build pipeline that produces the runtime artifacts
- [[pre-flash-test-pyramid]] — the 6-layer verification hierarchy
- [[cross-compilation]], [[gcc-arm-linux-gnueabihf]], [[wsl2-embedded-workflow]] — toolchain concepts
