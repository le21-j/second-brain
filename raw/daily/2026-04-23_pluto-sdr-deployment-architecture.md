---
date: 2026-04-23
topic: Adalm Pluto SDR — AirComp + Regret Learning deployment architecture
tags: [pluto-sdr, zynq-7010, fpga, aircomp, regret-learning, ofdm, sdr, embedded, systemverilog, libiio]
related: [[implementation-README]], [[build-deployment]], [[system-architecture]]
status: active
source_conversation: Claude Code session, session 1 of this topic
---

# 2026-04-23 — Pluto SDR Deployment Architecture (Session 1)

First deep-dive into [[implementation]] folder. Clarified the gap between **source code** and **deployed firmware** on the Adalm Pluto, and what "running the experiment" actually means end-to-end.

---

## Key Concepts (TL;DR for future me)

### 1. [[Zynq-7010 SoC — two halves]]
The Pluto's Zynq XC7Z010 is one chip with two very different halves that MUST be programmed separately:
- **PS (Processing System)** = dual-core ARM Cortex-A9 @ 667 MHz, runs PetaLinux userspace → takes **C binaries**
- **PL (Programmable Logic)** = FPGA fabric (28K cells, 80 DSP48E1s, 60 BRAM36s) → takes a **bitstream**

The split determines where you put what:
- Anything sample-rate (sync correlation, FFT, CP, channel estimation, CRC) → **FPGA (SystemVerilog)**
- Anything epoch-rate (state machine, regret-learning math, header pack/parse, radio config) → **ARM (C)**

### 2. [[HDL vs C — fundamentally different artifacts]]
- `.sv` (SystemVerilog) is NOT code you run. It describes **digital circuits**. Vivado synthesizes it into a **bitstream** that reprograms the FPGA fabric at boot. There is no "execution" — it's hardware configuration.
- `.c` cross-compiles to an ARM **binary**. That binary runs as a normal Linux process on the Pluto's ARM.

You can never "copy `.sv` files onto the Pluto." The Pluto has no Vivado.

### 3. [[Flashing vs running — two separate phases]]
- **Provisioning (once):** Build `pluto.frm` on dev machine → drag-and-drop onto Pluto's USB mass-storage mount → Pluto auto-reflashes.
- **Experiment (every run):** Power on → SSH in → launch `aircomp_es` / `aircomp_ed` → they drive the FSM and coordinate **over the air**.

The `.frm` is a monolithic image bundling: u-boot + Linux kernel + device tree + FPGA bitstream + rootfs (with your binaries in `/usr/bin/`).

### 4. [[USB is out of the real-time path]]
Key architectural win vs. a laptop-GNURadio-over-USB setup:
- All sample-rate data stays **on-chip**: AD9363 → FPGA → AXI-DMA → DDR → ARM userspace (via mmap).
- USB is only used for (a) one-time flashing, (b) optional SSH observability, (c) post-run log retrieval.
- You can literally unplug USB after launching and the experiment runs fine.

### 5. [[Remaining jitter sources]] (honest caveats)
Dropping USB doesn't mean zero jitter:
- **Linux scheduling jitter** — FSM runs in userspace, not RTOS. Small, mitigatable with `chrt -f 80` or core pinning.
- **Inter-Pluto TCXO drift** — each Pluto has its own 40 MHz TCXO, drifts tens of ppm. Current design uses Golay per-frame resync; fine phase coherence NOT yet achieved. Deferred: [[PTP IEEE 1588]] + [[Octoclock fine-sync]]. Affects raw AirComp SNR but not algorithmic validity of regret-learning results.

### 6. [[Experiment lifecycle — one epoch]]
```
ES: beacon → EDs        (RF)
EDs: CSI ACKs → ES      (RF, TDMA slots)
ES: training trigger    (RF)
EDs: AirComp superposition TX (RF, all 4 simultaneously)
ES: compute MSE, broadcast feedback
EDs: ACK feedback
EDs: update regret tables, pick new power for epoch N+1
```

All 5 Plutos (1 ES + 4 EDs) talk to each other **wirelessly**, not over Ethernet. Host laptop just launches binaries and pulls `/var/log/aircomp.log` after.

### 7. [[Dev loop — faster feedback before reflashing]]
Before paying "rebuild bitstream + reflash 4 Plutos":
1. [[Python reference]] — pure simulation, `pytest python_reference/tests/`
2. [[HDL testbenches]] — `vivado -mode batch -source hdl/tb/run_all.tcl`
3. **C self-test** — `aircomp_ed --self-test` on x86 laptop, exercises regret learner + PPDU codec

---

## Concept Map (Obsidian stubs to create later)

- [[Adalm Pluto SDR]] — target platform, Zynq XC7Z010 + AD9363
- [[AirComp]] — over-the-air computation, coherent waveform superposition
- [[Regret Learning]] — Hart-Mas-Colell update, power-level selection
- [[OFDM Pipeline]] — Golay sync, 128-pt FFT, CP add/remove, LS channel est, CRC-8
- [[AXI-Lite register map]] — see [[implementation/docs/registers.md]]
- [[libiio]] — AD9361 control (LO, gain, sample rate)
- [[UIO driver]] — `/dev/uio0` mmap path to custom FPGA IP
- [[plutosdr-fw]] — Analog Devices' stock firmware build system we merge into
- [[TDMA]] — time-division multiple access, used for ACK slots
- [[Zadoff-Chu pilot]] — known reference sequence for channel estimation
- [[Xilinx FFT IP]] — `xfft_128.xci`, pipelined streaming, 128-point
- [[PetaLinux]] — Xilinx BSP, used for kernel/DT changes only

---

## Full Conversation Log

### Q1 — "Can you explain what is going on in this folder and how I can implement these C and HDL scripts onto my adalm pluto sdrs?"

**Concepts introduced:** two-halves of the Zynq (ARM + FPGA), role split (ES vs ED), three artifacts per Pluto (bitstream, ARM binary, device tree), `pluto.frm` merged image, flashing workflow, `aircomp_es`/`aircomp_ed` launch commands, three sanity-check paths.

**Summary of answer:**
- Explained that the folder is a production impl of the Python prototype, split into `firmware/` (C on ARM) and `hdl/` (SystemVerilog on FPGA).
- Walked through the 6-step deployment: install Vivado + cross-compiler + `plutosdr-fw`, build bitstream, build firmware, merge into `pluto.frm`, drag-drop flash, launch ES first then EDs.
- Flagged 4 gotchas: missing `xfft_128.xci`, required `plutosdr-fw ≥ v0.34`, ES-first launch order, unique hostnames needed for 4 Plutos.

### Q2 — "I am essentially importing these scripts into the pluto directly correct?"

**Misconception corrected.** The Pluto is not like a Raspberry Pi where you SSH in and drop source files.

**Key points:**
- `.sv` files are NOT runnable — they describe circuits, must be synthesized by Vivado into a bitstream.
- `.c` files *could* compile on the Pluto (it runs Linux), but Pluto ships with no gcc, so cross-compile on dev machine.
- Only **binaries** + **bitstream** + **device tree patch** get bundled into `pluto.frm` and flashed.
- Mental model: **"the Pluto is an appliance you re-flash, not a workstation you develop on."**
- Edit-compile-test loop lives on the PC; each cycle ends with reflashing targets. No hot-reload for FPGA; no live-patching C binary.

### Q3 — "Wait so we are just flashing the image onto the pluto? How are these plutos going to run the test/experiment?"

**Clarified flashing vs. running as two separate phases.**

**Key points:**
- Flashing = provisioning (install Linux + FPGA logic + binary), done once per Pluto.
- Running = SSH into each Pluto → launch binary → binaries coordinate wirelessly.
- 5 SSH sessions (1 ES + 4 EDs), ES must start first (blocks until ≥1 ACK arrives).
- Inside a Pluto: FPGA does all real-time DSP at sample rate; ARM C code is the "conductor" reacting to DMA interrupts, making learning decisions, pushing TX payloads.
- Results: `/var/log/aircomp.log` on ES, `scp` off after the run.
- Faster dev loop options: Python sim, HDL testbenches, C self-test — all before reflashing.

### Q4 — "So essentially there is still no usb jitter correct because the code is being run directly on the SDR's and the data is only gathered after the experiment is done run?"

**Confirmed: yes, USB jitter is out of the loop.**

**Key points:**
- Real-time path is 100% on-chip: AD9363 → FPGA → AXI-DMA → DDR → ARM (mmap).
- USB used only for: flashing (one-time), optional SSH observability, post-run log retrieval. None timing-critical.
- Litmus test: can unplug USB after launching binaries, experiment completes fine.
- **Honest caveats on remaining jitter:**
  - Linux scheduling jitter (small, mitigable via `chrt -f 80` + core pinning)
  - **Inter-Pluto clock drift** — 4 independent 40 MHz TCXOs drift tens of ppm. Current design relies on Golay per-frame resync, not fine phase coherence. Deferred fix: PTP or Octoclock. Affects raw AirComp SNR but not regret-learning algorithmic validity.

### Q5 — "Can you save this entire conversation in a .md file..." (this file)

Meta — set up the second-brain log file you're reading now.

---

# Session 2 — 2026-04-23 (same day, afternoon)

Continued session. Verified regret-learning algorithm against asset_spec, re-routed all canonical references, rewrote divergent python_reference files as thin wrappers, set up GitHub + weekly scheduled pytest, ran pre-flash tests on the C firmware via WSL, and did a deep walk through the regret-matching algorithm (ψ, μ, D, S1/S2, counterfactual utilities, one-round delay).

## Session 2 — Key Concepts

### 1. [[Canonical spec is asset_spec/ only]]
`python_reference/asset_spec/regret_matching.py` is the algorithmic ground truth (per its own README). Everything else in `python_reference/` — `common/`, `ed/`, `es/` — is sketch code that may or may not match. All doc references, C headers, and HDL package comments re-routed to name ONLY asset_spec as canonical. `ed/regret_learning.py` and `ed/utility.py` were rewritten as **thin wrappers** over asset_spec semantics so they stop being landmines. Test files updated to match.

### 2. [[HMC ψ rebuilt each round — not additive]]
Hart-Mas-Colell regret matching does NOT maintain ψ as a running-average-with-regret-added-each-round. Each epoch, ψ is rebuilt from scratch as `ψ[k] = max(0, D[j][k]) / μ` for `k ≠ j`, and `ψ[j] = 1 − Σ ψ[others]`. The cumulative memory of past epochs lives in **D** (running-average regret matrix, decayed by `(t-1)/t` each round), not in ψ. Common confusion with Hedge (exponential weights), which IS additive — different algorithm family.

### 3. [[One-round μ delay]]
Adaptive μ update (`μ = 0.01 / sum_regret`) fires AFTER ψ is rebuilt inside `regret_update()`. So the freshly-adapted μ only affects ψ on the NEXT round. Matches asset_spec lines 135 vs 172 exactly. Consequence: round 0 shows ψ ≈ [~0, 1, ~0, ~0] even when regret is large, because rebuild_psi used the OLD μ=3000. The "shift" lands on round 1. Intentional — prevents ψ oscillation.

### 4. [[Exploration floor of 1e-6]]
`PSI_EXPLORATION_FLOOR = 1e-6` in regret_learning.h. Without it, `ψ[k]=0` would permanently lock out action k — can't sample → can't observe regret → stuck forever. The floor guarantees every action has ≥ 1-in-a-million sampling probability, which preserves the HMC convergence proofs under environmental change.

### 5. [[Utility decomposition: S1 (gain) vs S2 (penalty)]]
Each ED receives two scalars from the ES per epoch:
- `S1_n = Σ_{n'≠n} g(|h_{n'}|) · √(P_{n'}/η)` — linear sum of others' contributions
- `S2_n = Σ_{n'≠n} g(|h_{n'}|)² · P_{n'}/η` — quadratic sum

Utility `u_n = g(|h_n|)·√(P_n/η)·S1 − g(|h_n|)²·(P_n/η)·S2`:
- Term 1 **gains** from coherent contribution, scales linearly with √P
- Term 2 **penalizes** excess power, scales quadratically with P

The asymmetry creates a sweet-spot optimum that regret matching finds. Bandwidth wise, 2 scalars per ED per epoch regardless of N — constant-size feedback. Also a privacy win: EDs don't learn each other's channels.

### 6. [[Counterfactual utility every epoch]]
`regret_update()` evaluates `ed_utility(h, P[k], s1, s2)` for EVERY candidate action k each round, not just the chosen one. The `u_cf − u_played` difference is the "what if I'd played k?" regret that drives D → ψ. The counterfactual uses FIXED s1, s2 (others' behavior held constant within a round) — a deliberate simplification over true game-theoretic "others would respond" reasoning, but asymptotically correct per the HMC theorem.

### 7. [[Config shrunk: L=4, P_max=1mW]]
Bench-friendly config. Action set `linspace(P_max/L, P_max, L)` = **{0.25, 0.50, 0.75, 1.00} mW** for the 4 Plutos. Coarser than paper (L=100) but sufficient for benchtop bring-up. Convergence in ~3 rounds vs ~50 at higher L. Config.h / config.py / aircomp_pkg.sv all mirror these values; C and HDL pick them up automatically via macros. If L changes later, regret state scales as L×L (currently 16 cells × 8 bytes = ~150 bytes per ED).

### 8. [[AV blocks unsigned compilers on ASU lab PC]]
MSYS2's `gcc.exe` launches fine, but when it spawns `cc1.exe` (the actual C compiler backend), endpoint security silently kills the subprocess. No error message, no quarantine alert — just `cc1` exits immediately. Root cause: ASU AV/EDR blocks unsigned binaries from executing. **Escape hatch:** WSL. Linux kernel isolation means Windows AV can't inspect WSL subprocess execution. Ubuntu 24.04 + gcc 13.3.0 already present on the lab PC, Windows drives mount at `/mnt/c/`. Works cleanly.

### 9. [[Three-way algorithmic agreement achieved]]
Asset-spec Python ↔ `ed/regret_learning.py` wrapper ↔ `firmware/ed/regret_learning.c`:
- 17/17 pytest tests pass (Python wrapper matches asset spec)
- `test_regret_standalone` (WSL gcc) converges on the same oracle action as the Python inspection script
- D / ψ trajectories agree modulo PRNG differences (numpy Mersenne vs xorshift32)

Bit-exact comparison is stubbed: `firmware/ed/tests/test_regret_vs_asset.c` has the JSON-parser TODO; finishing it closes the bit-level loop.

### 10. [[Pre-flash pyramid status]]
- **Layer 1 — Python algorithmic:** ✓ green (17/17 pytest)
- **Layer 2 — HDL simulation:** ⧗ deferred (needs Vivado; ASU lab PC has no Vivado / no admin)
- **Layer 3 — C host compile + run:** ✓ green (WSL gcc, test_regret_standalone converges)
- **Layer 4 — ARM cross-compile:** ⧗ optional until closer to flash
- **Layer 5 — C+HDL co-sim:** ⧗ optional
- **Layer 6 — Hardware-in-loop on one Pluto:** ⧗ final step

Home-PC Vivado is the next milestone.

### 11. [[Weekly pytest routine scheduled]]
Remote scheduled routine `trig_017891Je8naWc4hmoQmNGdn2`. Cron `0 20 * * 2` (UTC) = **Tuesday 1:00 PM America/Phoenix** weekly. Clones `https://github.com/le21-j/aircomp-regret-pluto` (private), runs `pip install pytest numpy`, then `pytest python_reference/tests/`. Reports to routines UI; attempts `gh issue create` on failure if `gh` CLI is available in sandbox. **Currently blocked on GitHub App OAuth install** (https://github.com/apps/claude) — separate authorization from the MCP connector. Manual run attempted, got `github_repo_access_denied` until OAuth is completed.

---

## Session 2 — Full Conversation Log

### Q6 — "double check in the implementation folder that the regret learning matches the python references"
Confirmed: C regret_learning.c is a faithful port of **asset_spec/regret_matching.py** (not `ed/regret_learning.py`, which itself diverges from asset_spec). One intentional divergence: non-adaptive-μ sum>1 path rescales gracefully instead of `sys.exit()`. Discovered `python_reference/ed/regret_learning.py` used a different D update pattern and μ formula; `ed/utility.py`'s `power_level_to_watts` included a zero-power action that asset_spec explicitly excludes.

### Q7 — "route all references to asset_spec... rewrap them as thin wrappers"
Rewrote `ed/regret_learning.py` + `ed/utility.py` as thin Python ports matching asset_spec algorithm (same formulas as the C). Added prominent WARNING blocks to `python_reference/README.md`. Re-routed all doc pointers (README, build.md, architecture.md) and source-comment pointers (config.h, aircomp_pkg.sv) to name asset_spec as canonical. Removed "Hart-Mas-Colell" branding per user request; now reference the paper (`[[paper-unregrettable-hpsr]]`) and `regret_matching.py`. Created `test_asset_golden.py` — runs canonical asset, asserts invariants every round, writes golden-vector JSON for C cross-check. Stubbed `firmware/ed/tests/test_regret_vs_asset.c` — harness + Makefile target; JSON parser is a TODO (needs cJSON or similar).

### Q8 — "how would I test my C functions now that python is checked"
Laid out the 6-layer pre-flash pyramid. Focused on Layers 1–3 for today. Layer 1 (Python) ✓. Layer 2 (HDL) deferred to home PC. For Layer 3 (C), tried MSYS2 install — blocked by AV. Pivoted to WSL successfully.

### Q9 — "pytest is not recognized"
Three fixes, all committed:
- Windows Python path: Microsoft Store stub shadowed real `Python313`. Installed pytest+numpy via full-path pip; recommended disabling Store aliases.
- `conftest.py` shim in `python_reference/` aliases `implementation.*` → `python_reference.*` for legacy test imports.
- `matplotlib` stubbed via `unittest.mock.MagicMock` in test_asset_golden.py (asset_spec top-level imports it unnecessarily).
- asset_spec Python-3 compat fix: line 202 had `np.all(conv_diff < epsilon)` with `conv_diff` as a list — raises TypeError. Wrapped in `np.array()`. Documented in asset_spec/README.md.
- `common/pluto.py`: broadened `except ImportError` to `except Exception` — pyadi-iio's libiio dlopen raises TypeError on Windows when libiio isn't installed, slipped past the narrow guard. Matches the "falls back to sim mode" README promise.

17/17 tests pass on both Python 3.13 (fresh) and Anaconda Python 3.12 (with pyadi-iio installed).

### Q10 — "can you explain what is going on this python test"
Walked through all 5 test files (test_asset_golden, test_dsp, test_feedback, test_loopback, test_regret). Emphasized that all 17 tests prove algorithmic correctness at L=4 before any hardware work — Layer 1 of the pre-flash pyramid.

### Q11 — "how to see the test vectors and output from each algorithm"
Four techniques: the golden-vectors JSON (already on disk), reading test source, `pytest -s` + `print()`/`breakpoint()`, and a dedicated **`inspect_test_vectors.py`** script written during the session. The script has stages: `ofdm`, `sync`, `channel-est`, `crc`, `frame`, `regret`, `all`. Prints inputs, intermediate state, outputs per stage. Had to fix two API mismatches in my first draft (`fec.crc8` → `fec._crc8`, `ppdu.build_frame` → `ppdu.encode_frame` with `Header` dataclass).

### Q12 — "change regret learning config... 1 mW / N"
Updated N_POWER_LEVELS 20→4 and P_MAX_W 0.010→0.001 in config.h + config.py. Fixed architecture.md dimensional note (was "N×L=80 doubles", now "L×L=16"). Re-parameterized a hardcoded test index. Regenerated golden vectors (filename now `regret_N=4_L=4_seed=42.json`, 220KB from 3.3MB). All tests still pass. HDL had no power-level logic so no HDL changes needed.

### Q13 — "how would I do gh auth login"
Walked through `winget install --id GitHub.cli --scope user` + interactive web auth flow. Separately mentioned `gh auth setup-git` for credential-helper config.

### Q14 — "what is /schedule weekly pytest and how are you implementing it"
Explained remote scheduled routines: Claude agents running on Anthropic infrastructure on a cron schedule, cloning the repo from GitHub. Created routine `trig_017891Je8naWc4hmoQmNGdn2` for weekly Tuesday 1pm Phoenix pytest. Manual-run attempt failed with `github_repo_access_denied` — user needs to install Claude GitHub App (OAuth, separate from the MCP connector).

### Q15 — ".yml file" misconception
Clarified that `.yml` in `.github/workflows/` is GitHub Actions (CI/CD), different system. What's needed for scheduled routines is a GitHub App OAuth install at https://github.com/apps/claude — click-through, no file.

### Q16 — "i have wsl installed"
Verified: Ubuntu 24.04, gcc 13.3.0, Windows drives at `/mnt/c/`. Built and ran `test_regret_standalone` in WSL. Converged on correct action. Layer 3 green.

### Q17 — "could i not use vs code as a c compiler"
Clarified VSCode isn't a compiler — uses external toolchain, same AV problem. Suggested Codespaces (free 60h/mo), WSL (working), Remote-SSH (more setup).

### Q18 — "update the c regret-learning test to show channel gain + utility calculations + psi updates"
Enhanced `test_regret_standalone.c` to print per-round: full config echo, action set, utility landscape (oracle view), counterfactual utility table for all actions, instantaneous regret, D matrix row before/after update, ψ before/after, adaptive μ explanation, oracle-vs-learner comparison at end.

### Q19 — "why psi has values of 0"
Not actually zero — displayed 0.0000 due to `%.4f` format. Real values are 1e-6 (PSI_EXPLORATION_FLOOR). Essential mechanism: prevents permanent action lockout, preserves HMC convergence proof under environmental change.

### Q20 — "psi is the probability of each action?"
Confirmed. ψ[k] = probability the learner picks action k next round. Sum to 1, non-negative. Each round: D stores history of regrets, ψ is the forward-looking policy derived from D/μ.

### Q21 — "is it accounting for other EDs' channel gains"
Yes, but indirectly through aggregate statistics S1, S2 broadcast by the ES. Each ED sees two scalars that encode (g(|h|), P) sums over OTHERS. No ED sees individual neighbor channels. Constant-size feedback regardless of N. Privacy preserved.

### Q22 — "what is s1 and s2"
Formal definitions + intuition:
- S1_n = Σ_{n'≠n} g(|h_{n'}|)·√(P_{n'}/η) — linear "chorus amplitude"
- S2_n = Σ_{n'≠n} g(|h_{n'}|)²·(P_{n'}/η) — quadratic "chorus energy"

Utility trades off term1 (gain × S1, rises as √P) vs term2 (penalty × S2, rises as P). Sweet spot where regret matching lives. Ran a hand calculation showing S1_0 ≈ 0.134, S2_0 ≈ 0.006 for ED 0 at round 0 of the golden scenario.

### Q23 — "shouldnt action 2 and 3 have higher probability after round 0"
One-round delay explanation. `rebuild_psi()` runs BEFORE adaptive μ update inside `regret_update()`. So round 0's ψ uses μ=3000 (initial), making switch probabilities ≈ regret/3000 ≈ 1e-5. Adaptive μ then sets μ=0.2390 for NEXT round. Round 1 rebuilds ψ with μ=0.2390 → switch probs 0.11 for action 3, 0.06 for action 2. The shift you expected lands one round later. Matches asset_spec ordering exactly.

### Q24 — "double check asset_spec... does psi stay at 25% and regret adds on that baseline"
Confirmed against asset_spec/regret_matching.py lines 117-165: ψ is **rebuilt from zeros** each round (line 117), non-chosen actions get `ψ[k] = regret/μ` (assignment, not addition, line 135), chosen action gets `ψ[j] = 1 − Σ others` (line 159). User's "additive on 25% baseline" intuition describes **Hedge / exponential weights** — a different no-regret algorithm family. HMC is "rebuild from regret/μ, carry memory in D." Both are valid no-regret learners; HMC is what the HPSR paper uses and what the C implements.

### Q25 — "update the second brain files so i can push them"
This entry.

---

## Open Questions / Follow-ups

**Carried over from Session 1:**
- [ ] Generate `xfft_128.xci` in Vivado IP Catalog before first bitstream build (blocker for FPGA build).
- [ ] Rename 4 Plutos to unique hostnames (`pluto1..pluto4`) via `fw_setenv hostname plutoN` + reboot.
- [ ] Decide on clock-coherence strategy: accept TCXO-drift-limited SNR for first experiments, or invest in Octoclock/PTP before running.
- [ ] Decide whether to SCHED_FIFO + pin the C binary to core 1 on first bring-up (belt-and-suspenders).
- [ ] Confirm `plutosdr-fw` version ≥ v0.34 for device-tree-overlay support.

**New from Session 2:**
- [ ] **Install Claude GitHub App** at https://github.com/apps/claude (scheduled routine is blocked until this OAuth is done — `github_repo_access_denied` on manual-run attempt).
- [ ] **Monitor first weekly pytest fire**: Tuesday 2026-04-28 at 1:00 PM America/Phoenix (20:00 UTC). Routine ID `trig_017891Je8naWc4hmoQmNGdn2`, managed at https://claude.ai/code/routines/trig_017891Je8naWc4hmoQmNGdn2.
- [ ] **Home PC: install Vivado** and run `hdl/tb/run_all.tcl` to close Layer 2 of the pre-flash pyramid. WebPACK is free for XC7Z010.
- [ ] **Home PC: verify reproducibility** — pull repo, run WSL gcc + pytest + test_regret_standalone. Confirm identical results to lab PC.
- [ ] **Fill in JSON-parser stub** in `firmware/ed/tests/test_regret_vs_asset.c` (cJSON or jansson) to close the bit-exact C↔Python numerical cross-check.
- [ ] **Connect GitHub MCP connector** at https://claude.ai/customize/connectors if routine failure-reports should auto-create GitHub issues via API (currently relies on `gh` CLI in sandbox; probably unavailable).
- [ ] **Decide when to scale L back up** — current L=4 is bench-friendly; paper uses L=100. Revisit when studying algorithmic limits vs. hardware limits.
- [ ] **Dev-loop reminder:** edit on lab PC → push → `wsl` to run gcc + pytest → if both green, worth the bitstream build.

## Candidate Wiki Pages to Spawn Next

**Carried over from Session 1:**
- `[[Zynq-7010 PS-PL split]]`
- `[[pluto.frm build pipeline]]`
- `[[AXI interconnect variants]]` (Lite vs Stream vs MM)
- `[[Golay complementary sequences]]` (why ±1 coefficients, no multipliers)
- `[[LS channel estimation with ZC pilot]]`
- `[[Hart-Mas-Colell regret matching]]` (link to Papers/ folder)
- `[[Coherent AirComp clock requirements]]` (PTP/Octoclock tradeoffs)

**New from Session 2:**
- `[[Hedge vs HMC regret matching]]` — two no-regret learning families, when each applies; clarifies the "additive vs rebuild" intuition gap.
- `[[Adaptive μ one-round delay]]` — why ψ responds in round t+1 not t; asset_spec line pointer.
- `[[Exploration floor rationale]]` — 1e-6 / convergence proof / environment-change resilience.
- `[[HPSR utility landscape]]` — when term2 (penalty) dominates, oracle action shifts; plot-worthy.
- `[[S1 and S2 aggregates]]` — definitions, physical interpretation, bandwidth + privacy arguments.
- `[[Pre-flash test pyramid]]` — Python → HDL → C host → ARM cross → co-sim → HIL (6 layers).
- `[[ASU lab PC constraints]]` — AV blocks unsigned compilers, no admin, WSL escape hatch.
- `[[Weekly pytest routine operational notes]]` — auth flow, failure modes, GitHub App install, schedule ID.
- `[[asset_spec deviations log]]` — surgical edits tracked in asset_spec/README.md to keep "verbatim" honest.
- `[[Pluto action set {0.25, 0.50, 0.75, 1.00} mW]]` — specific bench config + scaling plan.

---

## How to update this log (for future Claude sessions)

**Maintenance rules:**
1. Append new dated H2 sections (`## 2026-MM-DD — Topic`) rather than rewriting history.
2. Each new Q&A session gets its own file in `implementation/second_brain/` dated with the new date.
3. Cross-link heavily with `[[wikilinks]]` — Obsidian builds the graph from these.
4. Promote recurring concepts from "mentioned inline" → standalone `[[Concept Page]].md` once they appear in 2+ sessions.
5. Keep the "Key Concepts (TL;DR)" section at the top scannable — 1-3 sentences per concept.
6. Full Q&A verbatim preserved at the bottom for replay value.

**Style targets (Karpathy-inspired):**
- Write as if re-reading in 6 months with zero context.
- Prefer concrete code paths, filenames, commands over abstract descriptions.
- Call out misconceptions you had, not just what you learned — the delta is where the insight lives.
- Every technical claim should name a specific file, register, signal, or command.
