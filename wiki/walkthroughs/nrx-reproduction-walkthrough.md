---
title: NRX (Neural Receiver) M7 Reproduction Walkthrough
type: walkthrough
course:
  - "[[python-ml-wireless]]"
tags:
  - walkthrough
  - phase-3
  - m7
  - neural-receiver
  - nrx
  - sionna
  - reproduction
  - capstone
sources:
  - "[[paper-nrx-cammerer-2023]]"
  - "[[paper-nrx-wiesmayr-2024]]"
  - "[[paper-sionna-2022]]"
  - "[[paper-sionna-research-kit-2025]]"
created: 2026-05-01
updated: 2026-05-01
---

# NRX (Neural Receiver) M7 Reproduction Walkthrough

> [!tip] What this walkthrough is
> A **step-by-step reproduction guide** for the NVIDIA Neural Receiver line — the **single highest-leverage Phase-3-M7 deliverable for the NVIDIA-intern application**. By the end you'll have:
> 1. A working Sionna environment.
> 2. A reproduced NRX BLER curve matching either Cammerer 2023 or Wiesmayr 2024.
> 3. A blog-post writeup ready to drop into a cold email or a GitHub README.
> 4. A clear extension target for **paper-nrx-wiesmayr-2024 → site-specific NRX** (the M10 follow-on).

> [!warning] Reproduce-first discipline
> **Do not skip Stage 0–4.** A claimed "I extended the NRX" without first matching the published baseline is a red flag in any NVIDIA technical review.

---

## Stage 0 — Read both papers (1–2 days)

**Goal:** know what you're reproducing **before** you touch code.

**What to read in order:**

| Step | Source | Time |
|---|---|---|
| 1 | [[paper-sionna-2022]] — the simulator | 90 min |
| 2 | [[paper-nrx-cammerer-2023]] — the original NRX architecture | 3 h |
| 3 | [[paper-nrx-wiesmayr-2024]] — the standard-compliant real-time variant | 3 h |
| 4 | [[neural-receiver]] concept page — the wiki summary | 20 min |
| 5 | [[paper-sionna-research-kit-2025]] — see how NRX deploys on Jetson | 60 min |

> [!note] Proposition extraction
> While reading, list **5–10 propositions per paper** in your own words: "the receiver does X because Y." This is the **proposition-extraction reading workflow** Jayden's `[[teacher]]` agent will quiz you on. File propositions to `wiki/practice/nrx-propositions.md` (TODO).

**Headline numbers to remember (target reproduction targets):**

- **Cammerer 2023:** ~1 dB BLER gain over LMMSE at $10^{-2}$ on 3GPP CDL channels.
- **Wiesmayr 2024:** standard-compliant at 5G NR slot timing (~1 ms); within 0.3 dB of Cammerer 2023's offline NRX.
- **Sionna Research Kit:** reaches the published numbers on a Jetson AGX Orin — proving the NRX is deployable, not just simulator-only.

---

## Stage 1 — Environment setup (~30 min)

**Goal:** working Sionna + PyTorch / TensorFlow installation; GPU verified.

> [!tip] Use uv for Python; conda when CUDA bundling is needed
> Sionna 1.x targets TensorFlow ≥ 2.15 and Python 3.10–3.11. Stick to the version pinned by the NRX repo.

```bash
# 1. Make a fresh project dir
mkdir nrx-reproduction && cd nrx-reproduction

# 2. Install uv if not present
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Create venv with the right Python
uv venv --python 3.11
source .venv/bin/activate

# 4. Install Sionna + PyTorch + Jupyter
uv pip install sionna jupyterlab tensorflow pytorch lightning hydra-core wandb numpy matplotlib

# 5. Verify GPU
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

**Sanity checks before proceeding:**

- [ ] `import sionna` works without warnings.
- [ ] GPU is detected (or note explicitly if you're on CPU and adjust expected runtime).
- [ ] `nvidia-smi` shows free memory ≥ 8 GB (NRX training peaks ~6 GB).

> [!warning] Common setup failures
> - **TensorFlow + CUDA mismatch.** TF 2.15 wants CUDA 12.2; check `tf.test.is_built_with_cuda()`.
> - **Sionna version drift.** Sionna 0.18 → 1.0 broke the `RadioMaterial` API ([[sionna-rt]] page calls this out). Pin to the version the NRX repo's `requirements.txt` specifies.

---

## Stage 2 — Clone the NRX repo + run the published demo (~1 h)

**Goal:** verify the published code runs end-to-end before any modification.

```bash
git clone https://github.com/NVlabs/neural_rx
cd neural_rx
uv pip install -e .
```

Run the **first official notebook** (typically `examples/notebooks/01_train_nrx.ipynb` or similar — check the repo's README for the canonical demo).

> [!example] What success looks like at end of Stage 2
> A loss curve that goes down. A trained NRX checkpoint. **You have not yet matched the published BLER curve** — that's Stage 4.

---

## Stage 3 — Read the training pipeline (~1 day)

**Goal:** understand every component of the NRX before claiming you can extend it.

Walk the codebase with this map:

| Component | Where it lives (typical Sionna structure) | What it does |
|---|---|---|
| **Channel model** | `sionna/channel/` (CDL, TDL, ray-traced) | Generates synthetic channels |
| **OFDM resource grid** | `sionna/ofdm/resource_grid.py` | Pilots + data subcarrier mapping; see [[ofdm-phy-basics]] |
| **NRX model** | `models/nrx_*.py` in the repo | The neural network — typically CNN over (time, frequency, antennas) |
| **Loss function** | `binary_cross_entropy` per bit on output LLRs | Note: BCE per bit, not per symbol |
| **Training loop** | TF/Keras-style `model.fit` or custom loop | Standard Adam, cosine LR |
| **Decoder** | LDPC ([[ldpc-codes]]) post-NRX | NRX outputs LLRs; LDPC decodes |

> [!info]- 📐 Show the BCE-on-LLRs derivation
> NRX outputs $L_b = \log\frac{P(b=1\mid y)}{P(b=0\mid y)}$ for each bit. BCE on bit $b$ with target $b^*$ is:
>
> $$\mathcal{L}_b = -b^*\log\sigma(L_b) - (1-b^*)\log\sigma(-L_b)$$
>
> Sum over all coded bits → minibatch loss. Critically, this is **before** LDPC decoding, so the NRX is trained on the LLR-quality signal that the decoder consumes.

**Active reading checklist:**

- [ ] Where is the channel-noise variance set? (sweep this — it controls Eb/N0).
- [ ] What's the pilot pattern? (3GPP-compliant grid? Or simplified?)
- [ ] Is the LDPC decoder differentiable? (For end-to-end training: yes; for inference: doesn't matter.)
- [ ] What's the batch size + training duration that the paper claims is sufficient?

---

## Stage 4 — Reproduce the headline BLER curve (~2 days for training; longer if no GPU)

**Goal:** train NRX from scratch and match the published BLER vs Eb/N0 curve.

**Procedure:**

1. **Pick the operating point** — match the paper's choice (CDL-C-300ns, 64 subcarriers, 4 TX × 4 RX antennas typically).
2. **Train for the published epoch count** — Cammerer 2023 reports ~100K steps; Wiesmayr 2024 trains shorter for the standard-compliant variant.
3. **Evaluate at 5+ SNR points** — sweep Eb/N0 from -5 dB to +15 dB; minimum 10⁵ frames per point for stable BLER.
4. **Plot vs. classical baselines** — LMMSE, K-best detector, and the LDPC-decoded version. **All three must be on the same plot or the result is uninteresting.**

> [!example] What success looks like
> Your NRX BLER curve sits **within ~0.2 dB** of the published Cammerer 2023 curve at $10^{-2}$ BLER, on the same channel + antenna config. If it's >1 dB off, debug:
>
> - Pilot pattern wrong?
> - LDPC parity-check matrix wrong?
> - Training too short?
> - SNR definition different (Eb/N0 vs Es/N0)?

> [!warning] BLER vs BER plotting trap
> The NRX papers report **BLER** (block error rate) — pre-LDPC BLER is the symbol-decision quality; post-LDPC BLER is the published headline. Make sure you're plotting the right one. See [[ber-bler]].

**Deliverable at end of Stage 4:**

- A reproduced figure that mirrors the paper's main BLER plot.
- A table: NRX vs LMMSE vs K-best at $10^{-2}$ BLER.
- All hyperparameters logged to W&B (or equivalent).

---

## Stage 5 — Write up the reproduction (~1 day)

**Goal:** produce the **artifact** an NVIDIA reviewer would see.

Write a `README.md` for your fork of the NRX repo with:

```markdown
# NRX Reproduction — [Cammerer 2023 / Wiesmayr 2024]

## Headline figure
![BLER curve](figures/bler-comparison.png)

## What I reproduced
- 3GPP CDL-C 300ns delay spread, 4×4 MIMO, 64 subcarriers
- NRX matches published BLER at 10⁻² within 0.2 dB
- Compared against LMMSE + K-best baselines

## Hyperparameters
[exact W&B run link or YAML]

## How to reproduce
[command-line steps]
```

> [!tip] The headline figure is what an NVIDIA reviewer remembers
> Spend an extra hour on it: clear axis labels, perceptually-uniform colormap, big fonts, no whitespace waste. See [[textbook-scientific-visualization-matplotlib]] for the patterns.

---

## Stage 6 — Extension ideas (Phase 4 M10 — only after Stage 5 lands)

**Goal:** turn the reproduction into a **publishable extension**.

Three concrete extension targets, ranked by leverage:

| Extension | Effort | Cold-email leverage |
|---|---|---|
| **Site-specific NRX in [[sionna-rt]]** ([[paper-diff-rt-calibration-2024]] companion) — calibrate scene + train NRX on calibrated channels; compare to generic-channel NRX | 2–3 weeks | **HIGHEST** — direct match to M10 + Hoydis-team's current research |
| **Transformer-block swap** — replace the CNN backbone with a small Transformer; ablate | 1–2 weeks | Medium — clean writeup material |
| **Quantize NRX → INT8 via [[onnx]]+[[tensorrt]]** — measure latency + accuracy trade | 1 week | High — directly applies to [[paper-sionna-research-kit-2025]] Jetson deployment |

> [!tip] Cold-email talking-point template
> "I reproduced your [Cammerer 2023 / Wiesmayr 2024] NRX result on 3GPP CDL channels (within 0.2 dB at 10⁻² BLER) and extended to **[site-specific scene calibrated via diff-rt-calibration / Transformer-block ablation / TensorRT-INT8 deployment]**. Repo at [URL]; happy to walk through the design choices."

---

## Common gotchas (collected from the audit + the papers)

| Gotcha | Symptom | Fix |
|---|---|---|
| Pilot pattern mismatch | NRX BLER 3 dB worse than LMMSE | Re-check 3GPP TS 38.211 pilot positions |
| Eb/N0 vs Es/N0 confusion | Curves look 3 dB off | Convert: $E_s/N_0 = E_b/N_0 + 10 \log_{10}(R_c \cdot \log_2 M)$ |
| LDPC mismatch | Post-LDPC BLER worse than pre-LDPC | Verify base graph + lifting size match 3GPP NR |
| Insufficient frames per SNR point | BLER curve has visible noise | $\geq 10^5$ frames per point at $10^{-2}$; $\geq 10^6$ at $10^{-3}$ |
| Sionna version pinning skipped | API breakage mid-reproduction | Pin to repo's `requirements.txt` exact version |
| Wrong LR schedule | Loss plateaus early | Cosine LR with warm-up — check repo defaults |
| Mixed-precision training silently broken | NaN losses | See [[mixed-precision-training]] for the FP16/FP32 hygiene checklist |

---

## Appendix — companion concept pages

- [[neural-receiver]] — the umbrella concept (CNN over time-frequency)
- [[neural-decoder]] — the post-NRX decoding subblock
- [[belief-propagation]] — what the LDPC decoder is doing
- [[ofdm-phy-basics]] — subcarriers, CP, pilots
- [[ldpc-codes]] — 5G NR data-channel code
- [[ber-bler]] — performance metric definitions
- [[mixed-precision-training]] — FP16 hygiene
- [[onnx]] + [[tensorrt]] — for the deployment extension
- [[paper-sionna-2022]] — the simulator stack
- [[paper-nrx-cammerer-2023]], [[paper-nrx-wiesmayr-2024]] — the source papers
- [[paper-sionna-research-kit-2025]] — Jetson deployment target
- [[hoydis]], [[cammerer]], [[aitaoudia]], [[wiesmayr]] — authors / NVIDIA-intern targets

---

## Appendix — Jayden's attempts log

> Date format: `YYYY-MM-DD`. Log each attempt with what worked / didn't / what to fix next time.

- **TBD** — first reproduction attempt (target: Phase 3 M7, Nov 2026).

---

> [!success] Definition of done
> Stage 5 completed = ready to send the cold email; Stage 6 completed = ready to draft the Asilomar 2027 workshop submission.
