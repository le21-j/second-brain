---
title: Daily — Pluto Deployment Architecture + Regret-Learning Deep Dive (2026-04-23)
type: summary
source_type: daily
source_path: raw/daily/2026-04-23_pluto-sdr-deployment-architecture.md
source_date: 2026-04-23
course: [[research]]
tags: [research, pluto-sdr, zynq, fpga, aircomp, regret-learning, hart-mas-colell, deployment, ofdm, wsl2, pytest, sessions]
created: 2026-04-24
updated: 2026-04-26
---

# Daily — Pluto Deployment Architecture + Regret-Learning Deep Dive (2026-04-23)

> **Provenance.** Two-session Q&A log from 2026-04-23, captured inside the implementation tree at `aircomp-regret-pluto/second_brain/` and copied to `raw/daily/` for the vault. 25 numbered questions total — Session 1 (Q1–Q5) covers deployment architecture, Session 2 (Q6–Q25) is a regret-learning algorithmic deep dive with sidecar ops notes (GitHub auth, weekly pytest, WSL workaround).

## TL;DR

- **Deployment model clarified.** The Pluto's Zynq is a two-halves-of-one-chip appliance: FPGA bitstream + ARM ELF are built on a dev machine, merged into `pluto.frm`, flashed once. Experiments run over the air — USB is out of the real-time path. Jitter budget is Linux scheduling + TCXO drift (mitigable with SCHED_FIFO + Golay-per-frame resync for coarse sync, PTP/Octoclock deferred for fine sync).
- **Regret matching semantics nailed down.** Canonical source is `asset_spec/regret_matching.py`; `ed/regret_learning.py` and `ed/utility.py` were rewritten as thin wrappers over asset_spec. HMC rebuilds $\psi$ from zero each round (not additive like Hedge). Adaptive $\mu$ has a one-round delay. Exploration floor $10^{-6}$ keeps actions reachable. Utility decomposes via $(S_1, S_2)$ aggregates — constant-size, privacy-preserving feedback.
- **Bench config shrunk.** $L = 4$ power levels at $\{0.25,\,0.50,\,0.75,\,1.00\}$ mW for $N = 4$ Plutos. Convergence in $\sim 3$ rounds vs $\sim 50$ at paper's $L = 100$. `config.h` / `config.py` / `aircomp_pkg.sv` all mirror the new values via shared macros.
- **Pre-flash test pyramid operationalized.** Layer 1 (pytest, 17/17 ✓) and Layer 3 (WSL gcc + `test_regret_standalone` ✓) green. Layer 2 (Vivado HDL sim) deferred to home PC — ASU lab PC AV blocks unsigned compilers like MSYS2 `cc1.exe`; WSL escape hatch works.
- **Ops plumbing.** Weekly pytest routine scheduled on Anthropic infra (Tuesday 1pm Phoenix), currently blocked on Claude GitHub App OAuth install.

## Key takeaways

- **HDL $\neq$ code, it's hardware description.** `.sv` files are synthesized into a bitstream by Vivado on a dev machine; the Pluto has no Vivado. `.c` files cross-compile to ARM ELF. You can't copy `.sv` files onto the Pluto and you can't natively compile C on the Pluto (no gcc on the stock image). See [[zynq-ps-pl-split]].
- **The Pluto is an appliance you re-flash, not a workstation you develop on.** Edit-compile-test lives on the PC; each deploy ends with reflashing targets. No hot-reload for FPGA, no live-patch for the C binary. See [[pluto-experiment-lifecycle]].
- **USB out of the real-time path is a genuine architectural win.** The AD9363 $\to$ FPGA $\to$ AXI-DMA $\to$ DDR $\to$ ARM mmap datapath stays on-chip. USB is only for flashing + SSH + post-run log retrieval — none of which is timing-critical.
- **HMC $\psi$ rebuild vs Hedge additive is the load-bearing distinction.** Jayden's intuition that $\psi$ accumulates regret on top of a $25\%$ uniform baseline describes **Hedge**, not HMC. HMC carries memory in $D$ (running-average regret matrix), $\psi$ is rebuilt each round from $D$. This is the single most-asked question in Session 2 (Q20, Q23, Q24). See [[hmc-psi-rebuild]].
- **Adaptive $\mu$ fires after $\psi$ is rebuilt.** One-round delay is intentional, prevents oscillation. Round-0 $\psi$ uses the initial $\mu = 3000$ and looks nearly flat; round-1 is the first $\psi$ with the adapted $\mu$. Matches asset_spec lines 135 vs 172 exactly.
- **Counterfactual utility uses $(S_1, S_2)$, not individual neighbor states.** The ES computes $S_1^{(n)} = \sum_{n' \neq n} g(|h_{n'}|)\sqrt{P_{n'}/\eta}$ (linear "chorus amplitude") and $S_2^{(n)} = \sum_{n' \neq n} g(|h_{n'}|)^2 (P_{n'}/\eta)$ (quadratic "chorus energy") and broadcasts them per ED. See [[aircomp-utility-s1-s2]].
- **Three-way algorithmic agreement achieved.** Python asset_spec $\leftrightarrow$ `ed/regret_learning.py` wrapper $\leftrightarrow$ `firmware/ed/regret_learning.c` all converge on the same oracle action on the golden scenario; bit-exact C $\leftrightarrow$ Python cross-check stubbed pending JSON parser.
- **AV endpoint security is a real engineering hazard.** MSYS2 looks fine, fails silently on `cc1.exe` spawn. WSL bypasses it because Linux kernel isolation puts subprocess execution outside Windows AV's reach.

## Concepts introduced (new pages)

- [[zynq-ps-pl-split]] — PS (ARM) vs PL (FPGA) halves of the Zynq-7010; where each file in `aircomp-regret-pluto/` runs
- [[pluto-experiment-lifecycle]] — flash-once / launch-per-epoch split; USB out of real-time path; Linux + TCXO jitter caveats
- [[pre-flash-test-pyramid]] — 6-layer dev loop (Python $\to$ HDL sim $\to$ C host $\to$ ARM cross $\to$ co-sim $\to$ HIL) with per-layer purpose
- [[hmc-psi-rebuild]] — HMC $\psi$-rebuild semantics vs Hedge additive; one-round $\mu$ delay; exploration floor $10^{-6}$
- [[aircomp-utility-s1-s2]] — $(S_1, S_2)$ aggregate feedback, utility decomposition, bandwidth + privacy arguments, hand calculation

## Reinforced / cross-linked

- [[regretful-learning]] — extended with "Implementation notes" section: asset_spec as canonical source, $L = 4$ bench config, $\psi$ rebuild, exploration floor, counterfactual $(S_1, S_2)$, test pyramid pointer.
- [[system-pipeline]] — extended with runtime model + PS/PL split + benchtop config callouts; related-links expanded to include the 4 new concept pages.
- [[pluto-build-toolchain]] — added "flashing vs running" callout and a pre-flash-pyramid gate inside the iteration loop.
- [[wsl2-embedded-workflow]] — added "escape hatch — when Windows AV blocks unsigned compilers" section documenting the ASU lab PC incident and WSL workaround.
- [[paper-unregrettable-hpsr]] — still the algorithmic anchor; this session operationalizes the paper's Algorithm 1 + Eqs 5–6.
- [[daily-2026-04-23-sdr-toolchain-questions]] — companion daily from the same day (Vivado / WSL install walkthrough, paused at Step 5).

## Worked content kept in `raw/`, not duplicated in wiki

- **Full Q1–Q25 transcript.** `raw/daily/2026-04-23_pluto-sdr-deployment-architecture.md` has the verbatim Q&A for replay value. When debugging a specific subtlety (e.g., "why did round 0's $\psi$ look flat?") it's faster to grep the raw log than to read abstracted concept pages.
- **Hand calculations for $(S_1, S_2)$.** The raw log carries round-0 numbers at seed $= 42$ for ED $0$; the concept page [[aircomp-utility-s1-s2]] cites a cleaned-up version but the raw has the full arithmetic.
- **Operational routine details.** Weekly pytest routine ID `trig_017891Je8naWc4hmoQmNGdn2`, cron `0 20 * * 2` (UTC) = Tuesday 1:00 PM Phoenix, blocked on https://github.com/apps/claude OAuth install. These are ephemeral ops state — they live in the raw file and in open-questions below, not in a concept page.

## Open questions / follow-ups

**Hardware / bring-up (carried over from Session 1):**
- [ ] Generate `xfft_128.xci` in Vivado IP Catalog before first bitstream build.
- [ ] Rename 4 Plutos to unique hostnames (`pluto1..pluto4`) via `fw_setenv hostname plutoN` + reboot.
- [ ] Decide on clock-coherence strategy: accept TCXO-drift-limited SNR for first experiments, or invest in Octoclock/PTP before running.
- [ ] Confirm `plutosdr-fw` version $\geq$ v0.34 for device-tree-overlay support.
- [ ] Whether to SCHED_FIFO + core-pin the C binary to core 1 on first bring-up.

**Software / ops (new from Session 2):**
- [ ] Install Claude GitHub App at https://github.com/apps/claude to unblock the scheduled weekly pytest.
- [ ] Monitor first scheduled fire: Tue 2026-04-28 1:00 PM Phoenix (20:00 UTC).
- [ ] Home PC: install Vivado (WebPACK is free for XC7Z010) and run `hdl/tb/run_all.tcl` to close Layer 2 of the pre-flash pyramid.
- [ ] Home PC: reproduce the WSL gcc + pytest + `test_regret_standalone` flow from the lab PC to confirm identical results.
- [ ] Finish JSON-parser stub in `firmware/ed/tests/test_regret_vs_asset.c` (cJSON or jansson) to close bit-exact C $\leftrightarrow$ Python cross-check.
- [ ] Decide when to scale $L$ back to $100$ — once hardware is stable and we're studying algorithmic limits.

## Related

- [[regretful-learning]] — the algorithm
- [[system-pipeline]] — the 7-stage protocol these devices execute
- [[paper-unregrettable-hpsr]] — source paper for the game-theoretic update
- [[paper-experimental-ota-fl]] — validated PTP + Octoclock sync recipe (the deferred fine-sync upgrade)
- CLAUDE.md → "Implementation agent — 6G researcher persona" — persona rules for working inside `aircomp-regret-pluto/`

## Sources

- `raw/daily/2026-04-23_pluto-sdr-deployment-architecture.md` — full 25-question Q&A log
- `aircomp-regret-pluto/python_reference/asset_spec/regret_matching.py` — the canonical spec referenced throughout Session 2
- `aircomp-regret-pluto/docs/{build.md,architecture.md,registers.md}` — impl docs cited throughout Session 1
