# Operations Log

Append-only chronological record of every operation on the wiki. One entry per op. Format:

```
## [YYYY-MM-DD] {op} | {title}
- bullets describing what was touched
```

Greppable: `grep "^## \[" log.md | tail -10`

Ops: `ingest` · `query` · `practice` · `walkthrough` · `lint` · `setup`

---

## [2026-04-30] query | EEE 335 L36 — deriving $C_M$ and $C_L$ via Socratic session

- Resolved confusion: why $C_{gd2} \parallel C_{gd4}$ at the output node — both far ends are AC ground (input node via $R_S \approx 0$, mirror node via diode-connected $1/g_{m3}$).
- Locked in three core ideas: (1) AC ground = LOW Z (not high Z) per $v = iZ$; (2) node Z $\neq$ gate input Z (node Z is parallel combination of everything connected); (3) diode-connected drain Z = $1/g_m$ (gate-to-drain feedback collapses $r_o$).
- Created `wiki/mistakes/diff-amp-frequency-response.md` — known gotchas (gate vs node Z, $v=iZ$ direction, diode-connected drain Z, $C_{gd2} \parallel C_{gd4}$ approximation, diode-connected $C_{gd}$ shorted) + Jayden's personal log entry for the session.
- Created `wiki/practice/eee-335-l36-cm-cl-set-01.md` — three problems graded easy → hard: (1) which cap is shorted in a diode-connected MOSFET; (2) build $C_M$ and $C_L$ from parasitics with AC-ground justifications; (3) what breaks if the input source is high-Z (Miller multiplication, bandwidth collapse). To be attempted later.
- `index.md` updated — added the new mistake page and practice page entries.

## [2026-04-30] setup | Fix agent loading + move teacher to global + add slash commands

- **Diagnosed:** new agent files (pluto-engineer, phy-ml-coach, teacher) were silently rejected by Claude Code's YAML parser because their `description:` field contained unquoted `[[wiki-links]]` and embedded double-quoted strings. Lyra didn't have these, which is why only it loaded.
- **Fix:** rewrote each `description:` field as a double-quoted YAML scalar with no `[[...]]` brackets and no embedded `"..."` titles. Detail moved to body content, where it was already.
- **Moved teacher to user/global scope:** `~/.claude/agents/teacher.md`. Removed the project copy. Pluto-engineer and phy-ml-coach stay at project scope (they reference `aircomp-regret-pluto/` and the wiki — not portable).
- **Created slash commands** so `/teacher`, `/pluto-engineer`, `/phy-ml-coach` work as direct invocations:
  - `~/.claude/commands/teacher.md` (global, matches teacher's scope)
  - `.claude/commands/pluto-engineer.md` (project)
  - `.claude/commands/phy-ml-coach.md` (project)
  - Each uses `$ARGUMENTS` to forward the user's invocation text into the agent prompt.
- **Updated CLAUDE.md "Custom agents" section** to document the new scopes, three invocation patterns (slash command / `@`-mention / `/agents` UI), the reload-on-edit gotcha, and the YAML frontmatter validation gotcha (so future-me doesn't repeat this).
- **For the user:** running `/agents` once will now rescan and load the three repaired agents.

## [2026-04-29] ingest | Two YouTube videos on using AI as a learning tool (Giles + Sung)

- **Raw sources saved:**
  - `raw/articles/2026-04-29-giles-oxford-ai-learning.md` — Giles' "Oxford Researchers Discovered How to Use AI To Learn Like A Genius" (250 lines including frontmatter)
  - `raw/articles/2026-04-29-sung-ai-learning-faster.md` — Justin Sung's "How to Learn FASTER using AI (without damaging your brain)" (1,149 lines including frontmatter)
  - Both deduped from yt-dlp auto-captions via `awk '!seen[$0]++'`
- **Summary pages:**
  - [[article-2026-04-29-giles-oxford-ai-learning]] — TL;DR + 10 takeaways + 3 worked-example prompts (Socratic momentum drill, proposition extraction, 20-key-terms-in-5-categories)
  - [[article-2026-04-29-sung-ai-learning-faster]] — TL;DR + 11 takeaways + 3 worked examples (research-summary trap, survey-question that changed the answer, calculator analogy)
- **New concept pages** (load-bearing for `.claude/agents/teacher.md`):
  - [[retrieval-practice]] — example-first (chain rule re-read vs retrieve), Karpicke & Roediger 2008, fluency illusion, "how to apply this week" tied to Exam 2 prep
  - [[blooms-taxonomy]] — example-first (chain rule at every level), AI/human boundary at the top-3 / bottom-3 split, the Sung gating rule made explicit
  - [[ai-learning-risk-complexity]] — example-first (variance formula vs neural-receiver SOTA — same shape, different risk), the two-graph framework, the 80/90 rule, week-relevant gating tables
- **Index updated:**
  - New section "Concepts — Learning meta (study skills + AI tutoring)" inserted between EEE 350 concepts and Formulas
  - New subsection "Learning meta" added to Summaries
- **Why this matters for the wiki:** every operating rule in `.claude/agents/teacher.md` now has a citable wiki anchor. The teacher agent can `[[wiki-link]]` to its rationale instead of re-explaining itself.
- **Pages touched:** `raw/articles/{2}.md` (new), `wiki/summaries/{2}.md` (new), `wiki/concepts/{3}.md` (new), `index.md` (2 edits).

## [2026-04-29] setup | Wiki-style global formatting + 3 new sub-agents (pluto-engineer, phy-ml-coach, teacher)

- **Created `~/.claude/CLAUDE.md`** (user scope, applies to all projects) — defaults substantive answers to wiki-page structure (one-line answer → example first → idea → formal → why → gotchas → related), mandates LaTeX for all math, formatting rules for tables/code/callouts/wiki-links/collapsibles. Terminal renders most of it; LaTeX shows raw but stays forward-compatible with Obsidian / docs / wiki.
- **Created `.claude/agents/pluto-engineer.md`** — 6G signal-processing researcher persona for `aircomp-regret-pluto/`. Lifted from the existing CLAUDE.md "Implementation agent" section, reframed in second person + self-contained. Hardware budget table, FPGA/ARM split, code-style rules, committed engineering decisions.
- **Created `.claude/agents/phy-ml-coach.md`** — Physical-Layer ML Roadmap coach for [[python-ml-wireless]]. Lifted from CLAUDE.md "Physical-Layer ML Roadmap persona" section. Targets NVIDIA Sionna intern + Wi-Lab PhD; portfolio-first; reproduce-before-innovate; canonical toolchain table.
- **Created `.claude/agents/teacher.md`** — AI tutor synthesized from (a) Giles' Oxford-AI method video (retrieval practice, Socratic questioning, multi-level explanations, Bloom's taxonomy ladder, proposition-extraction reading workflow) + (b) Justin Sung's risk-vs-complexity / Bloom's-top-3 framework + (c) Jayden's example-first learning style + (d) the wiki schema's existing teaching artifacts (`wiki/practice/`, `wiki/mistakes/`). Refuses to just answer — forces retrieval, escalates Bloom's level, auto-files attempts and misconceptions back to the wiki.
- **Updated CLAUDE.md "Custom agents" section** — registered all three new agents alongside `lyra`. Added pointers at the top of each existing persona section noting the agent-file equivalent. Note about user-scope vs project-scope formatting rules.
- **Tools used**: installed `yt-dlp` via Homebrew (was missing); pulled auto-captions for both videos to `/tmp/yt-transcripts/` (TPLPpz6dD3A: 1,712 words; 4gQIAXjraLo: 7,456 words after dedupe).
- Pages touched: `~/.claude/CLAUDE.md` (new), `.claude/agents/{pluto-engineer,phy-ml-coach,teacher}.md` (new), `CLAUDE.md` (3 edits).

## [2026-04-29] query | What is impulse response in difference equations? Is it H(z) = Y(z)/X(z)?

- Disambiguated $h[n]$ (time-domain sequence) vs $H(z)$ (Z-domain transfer function) — same information, two domains, related by Z-transform pair.
- Worked the same 1st-order IIR ($y[n] = x[n] - \tfrac{1}{2} y[n-1]$) two ways: time-domain iteration with $\delta[n]$ vs Z-transform with table lookup. Both yielded $h[n] = (-\tfrac{1}{2})^n u[n]$.
- Surfaced practical guidance: time-domain iteration faster for FIR / short responses; Z-transform faster for IIR with rational $H(z)$.
- Offered to file [[impulse-response]] as a new concept page since it threads through Modules 7, 8, 10 and is exam-relevant tomorrow.

## [2026-04-29] query | What is feed-forward propagation in MLPs?

- Answered from existing wiki pages — [[forward-propagation]], [[mlp]], [[neuron]] (all filed earlier today from EEE 404 Module 6).
- Disambiguated "feed-forward" (architecture, no recurrence) vs "forward propagation" (the layer-by-layer computation).
- Walked the 2-2-2 example from Exam 2 Practice P1 (inputs $X_1=0.05, X_2=0.10$, ReLU): $H_1=0.185$, $H_2=0.30$, $Y_1=0.6025$, $Y_2=0$.
- Surfaced exam relevance — Exam 2 P1 is exactly forward propagation; offered to generate a fresh practice set with new weights.
- No new pages created; existing concept pages already covered the topic in full.

## [2026-04-29] ingest + walkthrough | EEE 404 Exam 2 + EC labs + missing slides for eee-404 / eee-350

Big batch session. Three deliverables for the user, plus the wiki ingest.

**Canvas pulls (raw):**
- `raw/other/eee-404-exam-2-review.pdf` — practice exam (4 problems, full answer key)
- `raw/labs/eee-404/ec-ml-*` — EC ML lab PDF + code (main.c, embeddedML.c, embeddedML.h)
- `raw/labs/eee-404/ec-quantum-*` — EC Quantum lab PDF + table template (.docx)
- `raw/labs/eee-404/report-template-*` — generic Lab/Project Report Template (PDF + DOCX)
- `raw/slides/eee-404/` — 15 new PDFs covering Modules 6 (NN ×6), 7 (Freq Domain ×5), 8 (Diff Eq ×1), 10 (butterfly fill-in ×1), 11 (Effect of Window + Speech ×2)
- `raw/slides/eee-350/` — 43 new .pptx files covering Modules 1–5 (slides 1–37.5) and Module 8 (slides 47.5, 48, 49)

**Walkthroughs created (the headline teaching artifacts):**
- [[eee-404-exam-2-walkthrough]] — per-problem deep-dive on all 4 practice exam questions (MLP forward; Z-transform/ROC/DF-II; sampling/DFT/FFT sizing; 4-pt DFT direct + butterfly + IFFT). Bold headline answers, collapsible derivations.
- [[eee-404-exam-2-study-guide]] — companion topic checklist + master equation sheet (8 sections; cheat-sheet skeleton with suggested 3-column layout for the 8.5×11 sheet).
- [[eee-404-ec-ml-walkthrough]] — XOR-XOR lab walkthrough; truth table comparison; full code diff (only `y[1]` and `ground_truth[1]` lines change); IDE/SWV setup steps; complete fillable report skeleton.
- [[eee-404-ec-quantum-walkthrough]] — QFT vs DFT speech compression; 14-row simulation table to fill; 5 predicted trends to use as sanity checks; complete fillable report skeleton.

**Concept pages created (12, all NEW):**
- Module 6: [[neuron]], [[mlp]], [[relu]], [[forward-propagation]]
- Modules 7+8: [[z-transform]], [[region-of-convergence]], [[difference-equation]], [[fir-vs-iir]], [[direct-form-i]], [[direct-form-ii]]
- DFT properties: [[dft-properties]], [[parseval-theorem]]

**Source summaries created (8):**
- [[summary-eee-404-exam-2-review]]
- [[summary-eee-404-ec-ml-lab]], [[summary-eee-404-ec-quantum-lab]]
- [[summary-eee-404-m6-neural-networks]] (covers all 6 NN slide decks)
- [[summary-eee-404-m7-frequency-domain]] (covers all 5 Module 7 decks)
- [[summary-eee-404-m8-difference-equation]]
- [[summary-eee-404-m10-butterfly]] (fill-in for the missing Module 10 deck)
- [[summary-eee-404-m11-effect-of-window-and-speech]]
- [[summary-eee-350-m8-bernoulli-poisson-gaussian-rp]]
- [[summary-eee-350-backfill-modules-1-5]] (catalog of all backfilled slides 1–37.5)

**Course pages updated:**
- [[eee-404]] — added Module 6/7/8 concept roadmap, exam 2 + EC lab callouts, expanded Sources Filed and Walkthroughs sections
- [[eee-350]] — added Module 8 (Bernoulli/Poisson/Gaussian) arc and the backfill catalog reference; updated Sources Filed to group by Module

**Index.md updated:**
- New EEE 404 concept block (Z-transform / filter-implementation / NN)
- New walkthrough entries (4 EEE 404 deliverables)
- New summaries entries (8 new summaries across EEE 404 + EEE 350)

**Critical user-facing reminders:**
- Exam 2 is **Thursday 2026-04-30**, closed-book except 8.5×11 sheet, calculator OK, 150 pts. Coverage: Modules 6/7/10/11 + HW3/4/5.
- Both EC labs due **2026-05-02 06:59 UTC** (Friday 5/1 23:59 PT).

## [2026-04-21] setup | Vault initialized as LLM Wiki
- Created folder structure: `raw/{slides,articles,homework,textbook,other,assets}` and `wiki/{courses,concepts,people,formulas,examples,practice,mistakes,summaries}`.
- Wrote `CLAUDE.md` — schema, page templates, operations, and conventions.
- Scaffolded `index.md` (empty, ready to fill as sources get ingested).
- Scaffolded `log.md` (this file).
- Ready for first source ingest.

## [2026-04-21] ingest | EEE 404 — 6 FFT slide decks + Lab 7
- Sources: `raw/slides/{fft_core_equations,fft_idft,fft_implementation,FFT_interpretation,fft_real_valued_signal,window_functions}.pdf` and `raw/labs/lab7.pdf` + `raw/labs/lab7_code/{main.c,sine_table.h,gen_sin_f.m}`.
- Course page: [[eee-404]] + instructor [[chao-wang]].
- Summaries written: 7 (one per source).
- Concept pages written: [[dft]], [[fft]], [[twiddle-factor]], [[butterfly]], [[decimation-in-time]], [[bit-reversed-order]], [[fft-scaling]], [[dft-bin-interpretation]], [[frequency-resolution]], [[nyquist-frequency]], [[conjugate-symmetry]], [[idft]], [[real-valued-fft]], [[fixed-point-arithmetic]], [[complex-multiplication]], [[dft-computation-complexity]], [[stft]], [[window-function]], [[rectangular-window]], [[hamming-window]], [[hann-window]], [[bartlett-window]], [[spectral-leakage]] (23 total).
- Formula pages: 4 ([[dft-formula]], [[idft-formula]], [[fft-butterfly]], [[twiddle-factor-formula]]).
- Examples: [[dft-computation-burden]], [[idft-4pt-via-fft]], [[real-valued-fft-4pt]], [[frequency-bin-256hz]], [[eee-404-lab-7-fill-in-walkthrough]] (5).
- Practice: [[fft-fundamentals-set-01]] — 11 problems, mixed difficulty, drawn directly from lecture Q slides.
- Mistakes: [[fft-gotchas]] — seeded with general gotchas; personal log section open.
- `index.md` rebuilt to reflect all pages. Pre-extracted PDF text saved to `.ingest_tmp/` for re-reads.

## [2026-04-21] setup | Slides reorganized by course
- Moved `raw/slides/*.pdf` → `raw/slides/eee-404/` and `raw/slides/*.pptx` → `raw/slides/eee-350/`.
- Updated source_path frontmatter in the 6 existing EEE 404 summary pages.
- Added basename-uniqueness rule to [[CLAUDE]] so future pages avoid wiki-link collisions.

## [2026-04-21] ingest | EEE 350 — 12 slide decks (decks 38–47)
- Sources: `raw/slides/eee-350/{38..47}*.pptx` — late-semester probability/statistics arc at ASU.
- Caveat: slides are image-heavy (Wiley textbook + MIT 6.041 slide images). Text extraction via `unzip` + `<a:t>` regex gave titles + bullet labels; mathematical content reconstructed from slide structure and standard probability theory.
- Course page: [[eee-350]].
- Summaries: 12 (one per deck — [[slides-38-covariance]] through [[slides-47-stochastic-processes]]).
- Concept pages: 58 new across five arcs:
  - **Moments/dependence** (9): [[covariance]], [[correlation-coefficient]], [[variance-of-a-sum]], [[independent-vs-uncorrelated]], [[bivariate-gaussian]], [[multivariate-gaussian]], [[random-vector]], [[iid-samples]], [[max-of-iid]]
  - **Conditional expectation** (5): [[conditional-expectation]], [[iterated-expectations]], [[conditional-variance]], [[law-of-total-variance]], [[sum-of-random-number-of-rvs]]
  - **Asymptotics** (9): [[markov-inequality]], [[chebyshev-inequality]], [[convergence-in-probability]], [[weak-law-of-large-numbers]], [[gamblers-fallacy]], [[central-limit-theorem]], [[continuity-correction]], [[binomial-via-clt]], [[standard-normal-table]]
  - **Bayesian inference** (8): [[bayesian-inference]], [[prior-distribution]], [[posterior-distribution]], [[detection-vs-estimation]], [[map-detection]], [[map-estimation]], [[lms-estimation]], [[antipodal-signaling]]
  - **Classical + testing** (10): [[maximum-likelihood-estimation]], [[unbiased-estimator]], [[consistent-estimator]], [[efficient-estimator]], [[confidence-interval]], [[neyman-pearson-test]], [[type-i-error]], [[type-ii-error]], [[likelihood-ratio-test]], [[chi-squared-test]]
  - **Regression + descriptive** (11): [[linear-regression]], [[least-squares]], [[power-law-regression]], [[sample-mean]], [[sample-variance]], [[sample-covariance]], [[sample-median]], [[sample-mode]], [[order-statistics]], [[histogram]], [[skewness-kurtosis]]
  - **Stochastic processes** (6): [[stochastic-process]], [[stationary-process]], [[white-gaussian-process]], [[colored-noise]], [[poisson-process]], [[markov-chain]]
- Formula pages: 4 ([[covariance-formula]], [[conditional-expectation-formulas]], [[asymptotic-formulas]], [[inference-formulas]]).
- Examples: 5 ([[covariance-of-x-and-x-plus-z]], [[stick-breaking-iterated-expectations]], [[polling-sample-size]], [[map-detection-antipodal]], [[mle-for-exponential-rate]]).
- Practice sets: 3 ([[prob-fundamentals-set-01]], [[asymptotics-set-01]], [[inference-set-01]]).
- Mistake log: [[prob-gotchas]].
- `index.md` rebuilt to include EEE 350 sections.

## [2026-04-21] ingest | Research — 8 AirComp papers + pipeline design doc
- Sources: 8 PDFs in `raw/articles/` — HPSR 2026 (regret-learning anchor), Şahin & Yang 2023 AirComp survey, Şahin 2022 FEEL SDR demo, FSK-MV, BPSK two's-complement, MD-AirComp+, Non-Coherent DGD, UAV-assisted AirComp.
- New folder: `wiki/research/` — for the research project's concept and design pages (summaries kept in `wiki/summaries/` per schema).
- Paper summaries (8): [[paper-unregrettable-hpsr]], [[paper-aircomp-survey]], [[paper-aircomp-feel-demo]], [[paper-fsk-mv]], [[paper-bpsk-complement]], [[paper-md-aircomp-plus]], [[paper-ncota-dgd]], [[paper-uav-aircomp]].
- Research concept pages (4): [[aircomp-basics]], [[regretful-learning]], [[channel-estimation]], [[robust-signaling]].
- **Main deliverable:** [[system-pipeline]] — professionally rewritten 7-stage pipeline (user skipped "third step"; renumbered 1–7), with fact-checks, open questions, and implementation-phase plan. Serves as the token-efficient reference for future questions about the design.
- Open questions flagged: phase coherence assumption in HPSR Eq 2, TDD reciprocity, training-mode vs operational-mode, feedback bandwidth optimization, location of ED/ES scripts (not in `raw/` — Jayden needs to point at them).
- `index.md` updated with Research section + research summaries list.

## [2026-04-21] ingest | Research — 7 x 6G signal-design papers + signal-design-gaps doc
- Sources: 7 PDFs downloaded via curl into `raw/articles/6g-research/` — ITU-R M.2516 (IMT-2030 framework), Azimi-Abarghouyi et al. IEEE SPM 2025 (CSIT-aware/blind/weighted taxonomy), Pradhan et al. 2025 (first 5G-NR OTA-FL testbed with PTP+Octoclock+Gold), Li/Chen/Fischione 2025 (channel-aware constellation), Wang et al. 2022 (6G AirComp foundations — MIMO-focused complement to Şahin survey), 2025 PAPR/peak-power paper, 2025 industry 6G RAN viewpoints.
- Paper summaries (7): [[paper-rethinking-edge-ai-spm]], [[paper-experimental-ota-fl]], [[paper-channel-aware-constellation]], [[paper-itu-r-m2516]], [[paper-6g-aircomp-foundations]], [[paper-signal-peak-power]], [[paper-industrial-6g-ran]].
- **Main deliverable:** [[signal-design-gaps]] — gap analysis of Jayden's pipeline against 6G research consensus, organized by signal type (beacon / sync / data / feedback). 15 discrete gaps found, each mapped to a paper and to a pipeline section needing revision.
- [[system-pipeline]] patched with a "Signal-design gaps" subsection pointing at the new doc — highest-priority findings surfaced inline.
- `index.md` reorganized: research summaries split into "core" (HPSR and relatives) + "6G signal design" (new papers for the gap analysis).
- Key findings: pipeline's sync regime is implicit (must declare fine-sync); PTP+Octoclock is the validated sub-μs implementation; Stage 4 needs training-mode + operational-mode split; 6G trend is to split discovery beacon from training-trigger beacon; feedback can be CSI-compressed via autoencoder for ~70% bandwidth saving.

## [2026-04-21] implementation | Align regret learner to asset spec
- Imported `raw/assets/{regret_matching,channel_gain,pure_plots}.py` into `implementation/python_reference/asset_spec/` as the canonical algorithmic ground truth, with a README calling out the three semantic differences from HPSR Eq.5-11: (a) action set is `linspace(P_max/L, P_max, L)` — no zero action, (b) `psi` has a 1e-6 exploration floor on alternative actions, (c) adaptive μ uses `μ = 0.01 / sum_regret` (smaller μ → faster switching when regret is large).
- Rewrote `firmware/ed/regret_learning.[hc]` to match: full D-matrix decay by (t-1)/t, exploration floor, μ-doubling loop if sum-of-others > 1, correct adaptive-μ formula with 3000 fallback when sum_regret = 0. Added `regret_row_sum()` for diagnostics / convergence checks.
- Updated `firmware/ed/utility.c` → action set now starts at P_max/L (level 0) instead of 0.
- Extended `firmware/ed/main.c` CLI with `--mu <initial>` (default 500.0) and `--adaptive-mu` flags; `regret_init()` gained `mu_init` + `adaptive` parameters.
- Kept `python_reference/ed/regret_learning.py` and `utility.py` in lock-step with the C — same step numbering, same constants, same formulas. The RegretLearner constructor is backward-compatible (all new params default).
- Added `tests/test_regret.py::test_cross_check_utility_against_asset` that imports `asset_spec/regret_matching.py` and asserts `device_utility()` matches our `utility.utility()` to 1e-9 for a 4-device scenario.
- Added `tests/test_regret.py::test_exploration_floor` and `::test_adaptive_mu_decreases_with_large_regret` for the two non-HPSR behaviours called out in the asset README.

## [2026-04-21] implementation | C + HDL production skeleton
- Pluto-targeted production path: C on ARM (Cortex-A9) + SystemVerilog on FPGA (Zynq-7010 PL). Python moved to `implementation/python_reference/` as algorithmic spec only.
- CLAUDE.md persona updated to match: languages are C11 + SystemVerilog-2012 (with Xilinx FFT IP core allowed for the 128-pt FFT); Python confined to `python_reference/`.
- Docs: `implementation/docs/{architecture,registers,build}.md` — block diagram, AXI-Lite register map (match `fpga_dsp.c`), Vivado + Vitis + PetaLinux build flow.
- Firmware (C): `firmware/common/{config.h, fec.{h,c}, ppdu.{h,c}, fpga_dsp.{h,c}, pluto_io.{h,c}}`; ED: `utility.{h,c}`, `regret_learning.{h,c}`, `state_machine.{h,c}`, `main.c`; ES: `aggregate.{h,c}`, `mse.{h,c}`, `state_machine.{h,c}`, `main.c`; `Makefile` with cross-compile defaults.
- HDL (SystemVerilog): `rtl/{aircomp_pkg, sync_detector, cp_remove, cp_add, fft_128_wrapper, channel_est, crc8, axi_lite_regs, aircomp_core}.sv`; `tb/{tb_crc8, tb_sync}.sv` + `run_all.tcl`; `constraints/{pluto.xdc, device_tree_fragment.dts}`; `scripts/build_project.tcl`.
- FPGA DSP split: sync correlator uses ±1 coefficients (adder tree, no multipliers); 128-pt FFT via Xilinx IP; channel est via precomputed 1/pilot ROM (complex multiply, no divider); CRC-8 LFSR. Estimated XC7Z010 utilisation: ~34% LUT, ~30% DSP48, ~10% BRAM.
- ARM ↔ FPGA interface: AXI-Lite register file (64 words, documented in registers.md); AXI-Stream for sample DMA; one IRQ line to PS GIC.

## [2026-04-21] implementation | Pluto-targeted reference implementation scaffolded
- New folder: `implementation/` with `common/`, `ed/`, `es/`, `tests/`.
- CLAUDE.md extended with "Implementation agent — 6G researcher persona": persona, hardware constraints, FPGA/ARM split strategy, code-style rules (no nested ifs beyond 2 levels, minimal comments, preallocate, vectorize), and committed engineering defaults (numerology, frame layout, regret-learning params, sync regime).
- Modules: `common/{config, ofdm, sync, pilots, ppdu, fec, pluto}`, `ed/{utility, regret_learning, state_machine, main}`, `es/{mse, aggregate, state_machine, main}`.
- `common/pluto.Radio` wraps pyadi-iio with a transparent in-process simulator fallback — same code runs on hardware or laptop.
- State machines implement the 7 pipeline stages (see `implementation/README.md` → "Mapping to the 7 pipeline stages").
- Tests: `test_dsp.py` (OFDM + sync + pilots + CRC + PPDU), `test_regret.py` (learner invariants), `test_feedback.py` (aggregate roundtrip), `test_loopback.py` (full 5-radio smoke test in one process).
- Deliberately deferred per `[[signal-design-gaps]]`: polar-128 (placeholder 3× repetition), PTP fine sync (coarse Golay for now), CSI compression, α-stable noise, mobility.
- index.md updated with an Implementation section pointing at the new folder.

## [2026-04-24] ingest | EEE 350 HW7 — Significance testing + MMSE/LMSE
- Source: `raw/homework/EEE350_HW7.md` — four problems covering fair-coin significance test (11.1.6), LMSE from discrete joint PMF (12.2.3), LMSE from continuous joint PDF (12.2.4), and MMSE-vs-LMSE with an Erlang/Uniform setup (12.2.6); plus five in-chat gotchas on CLT, standardization, Gaussian/Normal naming, and variance scaling.
- **New concept pages (4):** [[significance-test]], [[linear-mmse-estimation]] (LMSE/LLS), [[standardization]] (z-score), [[variance-scaling-rule]] (Var(cX) = c²Var(X)).
- **New worked-example pages (4):** [[fair-coin-significance-test]], [[lmse-discrete-pmf]], [[lmse-continuous-pdf]], [[mmse-vs-lmse-erlang]].
- **Summary:** [[homework-2026-04-23-eee-350-hw7]].
- **Updated [[lms-estimation]]** — added a naming-conflict table reconciling Wiley/MIT "LMS/LLS" with HW7 "MMSE/LMSE" (same math, different abbreviations), plus cross-links to the new pages.
- **Updated [[prob-gotchas]]** — added 8 new gotchas: "trials" vs experiment repetitions, LMSE≠LMS naming, 5-number LMSE shortcut, CLT≠standardization, three CLT scalings, Gaussian=Normal, Var(cX)=c²Var(X), and engineered σ² in the standardization denominator.
- **Updated [[eee-350]]** course page — added HW7 summary to Sources Filed, surfaced [[significance-test]] / [[linear-mmse-estimation]] / [[standardization]] / [[variance-scaling-rule]] on the roadmap, listed the four HW examples.
- **Updated index.md** — added the new concepts under "Asymptotic theorems", "Bayesian inference", "Hypothesis testing"; added the four examples under "EEE 350 examples"; added the HW7 summary under "Summaries → EEE 350".

## [2026-04-24] ingest | Daily research Qs (2026-04-23) — SDR toolchain
- Source: `raw/daily/2026-04-23_Research_Questions.md` — Jayden's running Q&A from yesterday covering `gcc-arm-linux-gnueabihf` (Q1), Windows-host options for SDR work (Q2), WSL2 Ubuntu shell access (Q3), Pluto firmware prerequisites (Q4), and a tailored WSL2+custom-HDL walkthrough (Q5). Status: **in-progress, paused at Q5 Step 5 (Vivado 2022.2 install)**.
- New source type: `daily` (schema extension — `raw/daily/` folder is Jayden-created, not in the original CLAUDE.md layout). Used `source_type: daily` in summary frontmatter; may want to formalize in CLAUDE.md later.
- **New concept pages (4):** [[cross-compilation]], [[gcc-arm-linux-gnueabihf]], [[pluto-build-toolchain]], [[wsl2-embedded-workflow]]. Each distills the *why* and *what to remember* — the raw file remains the runbook for actual procedure.
- **Summary:** [[daily-2026-04-23-sdr-toolchain-questions]] — prominently features a ⏸️ "Resume here" block mirroring the raw file's marker (Step 5, Vivado install).
- **Updated [[system-pipeline]]** — added a "Build toolchain" paragraph under § 3 Implementation status, cross-linking the 4 new concept pages and the daily summary. Appended the toolchain pages to § Related.
- **Updated index.md** — added a new "Toolchain concepts (for the Pluto build pipeline)" subsection under Implementation; added the daily summary under Summaries → "Daily research Q&A" (new subsection); updated the Implementation intro to reflect the `implementation/` → `aircomp-regret-pluto/` rename and note `implementation.zip` as backup.
- **Project note:** the top-level `implementation/` folder has been renamed to `aircomp-regret-pluto/` at the repo root. Old path referenced in index.md (now updated), `CLAUDE.md` (multiple places — **not updated, flagged for Jayden**), and possibly `aircomp-regret-pluto/docs/build.md` (content unchanged, internal paths still say `implementation/...` — also **flagged, not fixed**).

## [2026-04-23] ingest | Physical-Layer ML Roadmap (NVIDIA + Wi-Lab 14-month plan)
- Source: `raw/other/python learning roadmap.md` — Jayden's personal roadmap, May 2026 → Jun 2027. Targets NVIDIA's Sionna team (Hoydis et al.) and Ahmed Alkhateeb's Wi-Lab at ASU.
- **Course page:** [[python-ml-wireless]] — full phase-by-phase curriculum, canonical toolchain, application timeline (NVIDIA intern postings Aug–Oct 2026; Wi-Lab cold-email May–Sep 2027).
- **Source summary:** [[article-2026-04-23-physical-layer-ml-roadmap]].
- **Raw organization:**
  - `raw/textbook/README.md` — catalog of every book on the roadmap.
  - `raw/textbook/*.md` — 23 individual book reference cards (Python / scientific Python / wireless/DSP / PyTorch / TensorFlow / ML / DL / RL / math). Added Bourke "Learn PyTorch for Deep Learning" post-ingest on user prompt — initial sweep missed it.
  - `raw/articles/ml-phy/README.md` — ~60 paper arXiv references grouped by subtopic.
  - `raw/other/online-courses.md` — course catalog (CS50P, Andrew Ng, CS231n, CS224W, Karpathy Zero-to-Hero, HF courses, NVIDIA DLI, etc.).
  - `raw/other/datasets.md` — DeepMIMO v4, DeepSense 6G, DeepVerse 6G, RadioML 2016/2018, COST2100.
- **Wireless + ML core concept pages (14):** [[physical-layer-ml]], [[sionna]], [[deepmimo]], [[deepsense-6g]], [[large-wireless-model]], [[neural-receiver]], [[autoencoder-phy]], [[csi-feedback]], [[differentiable-ray-tracing]], [[wireless-digital-twin]], [[beam-prediction]], [[channel-charting]], [[modulation-classification]], [[ofdm]].
- **Python / ML foundational concept pages (12):** [[pytorch]], [[numpy-vectorization]], [[transformer]], [[attention-mechanism]], [[convolutional-neural-network]], [[variational-autoencoder]], [[generative-adversarial-network]], [[diffusion-model]], [[graph-neural-network]], [[reinforcement-learning]], [[backpropagation]], [[autograd]].
- **People pages (18):** target labs ([[alkhateeb]], [[hoydis]], [[morais]], [[oshea]], [[heath]], [[bjornson]], [[lichtman]]) and teachers / textbook authors ([[karpathy]], [[raschka]], [[rougier]], [[prince]], [[bishop]], [[murphy]], [[goodfellow]], [[sutton]], [[mackay]], [[ng]], [[chollet]]).
- **CLAUDE.md:** added "Python / ML / wireless-comm context — the Physical-Layer ML Roadmap persona" block (mirrors the existing "Implementation agent" block). Frames future questions about Python, ML, wireless comm in terms of the NVIDIA + Wi-Lab trajectory.
- **index.md** reorganized with new Course entry, Physical-Layer ML Roadmap researchers section under People, and two new concept subsections (Wireless + ML core; Python / ML foundations).
- Cross-linked into existing vault: [[system-pipeline]] / [[regretful-learning]] / [[channel-estimation]] stay as the parallel AirComp research track — many Phase 1–2 roadmap deliverables reinforce that work (OFDM from scratch, channel estimation, autoencoder PHY).
- Open questions flagged in the summary: NVIDIA team targeting specifics (decide Sept 2026); letter writers shortlist; whether AirComp work becomes a Phase-4 arXiv preprint.

## [2026-04-24] ingest | Pluto deployment architecture + regret-learning deep dive (2026-04-23 second-brain session)
- Source: `aircomp-regret-pluto/second_brain/2026-04-23_pluto-sdr-deployment-architecture.md` → copied to `raw/daily/2026-04-23_pluto-sdr-deployment-architecture.md`. 25 numbered questions across two sessions (Q1–Q5 deployment architecture, Q6–Q25 regret-learning algorithmic deep dive + ops plumbing).
- Summary: [[daily-2026-04-23-pluto-deployment-and-regret-learning]].
- New concept pages (5): [[zynq-ps-pl-split]], [[pluto-experiment-lifecycle]], [[pre-flash-test-pyramid]], [[hmc-psi-rebuild]], [[aircomp-utility-s1-s2]].
- Extended: [[regretful-learning]] (new "Implementation notes" section — asset_spec canonical, L=4 bench config, ψ rebuild, exploration floor, counterfactual `(S1, S2)`, pyramid pointer), [[system-pipeline]] (runtime model + PS/PL split + benchtop config callouts, related-links expanded), [[pluto-build-toolchain]] (flashing-vs-running callout + pre-flash gate in iteration loop), [[wsl2-embedded-workflow]] (AV-unsigned-compilers escape-hatch section).
- `index.md` updated — new Implementation subsections "Architecture + runtime concepts" and "Algorithm internals"; new daily entry.

## [2026-04-25] ingest | EEE 304 Lab 4 — AM Modulation/Demodulation in Simulink
- Sources: `raw/labs/EEE 304 Lab4.pdf`, `raw/labs/AM_Mod_coherent.slx`, `raw/labs/AM_Mod_incoherent.slx`, `raw/labs/AM_Mod_coherent_tada_inc.slx`, `raw/labs/tada.wav`.
- Course page created: [[eee-304]] — EEE 304 Signals and Systems / Communication Systems.
- Summary: [[lab-eee-304-lab-4-am-modulation]].
- Walkthrough (the headline output, per the user's new "lab walkthrough" skill request): [[eee-304-lab-4-walkthrough]] — per-question concept + steps + expected outcomes for #1.1–#3, formatted with bold + Obsidian `==highlights==` + callout blocks.
- New concept pages (5): [[amplitude-modulation]], [[modulation-index]], [[coherent-demodulation]], [[envelope-detection]], [[butterworth-filter]].
- Memory saved: `feedback_lab_walkthroughs.md` indexed in `MEMORY.md` — applies to any future "ingest a lab" or "help with this lab" request.
- `index.md` updated — new course entry, new "Concepts — EEE 304 (Communication Systems)" section, new EEE 304 walkthrough/summary entries under Examples and Summaries.

## [2026-04-26] walkthrough | EEE 304 HW7 — cascaded AM, TDM-PAM, chopper amplifier
- Sources: `raw/homework/HW7.pdf` (the assignment, no solutions) + `raw/homework/304_hw7_sample25.pdf` (previous-year sample with fully-worked solutions used as a verification reference).
- Summary: [[homework-2026-04-26-eee-304-hw7]].
- Walkthrough: [[eee-304-hw7-walkthrough]] — per-problem concept + step-by-step derivation + cross-check against the sample for each of the 3 problems. Same bold + `==highlights==` + callout-block format as the lab walkthrough.
- New concept pages (3): [[pulse-amplitude-modulation]], [[time-division-multiplexing]], [[chopper-amplifier]].
- Course page extended: [[eee-304]] — added "Pulse modulation + multiplexing arc" section, HW7 to Sources filed, new walkthrough link.
- **Schema change:** the lab-walkthrough memory was broadened and renamed to **`feedback_assignment_walkthroughs.md`** (covers labs **and** homeworks). Added a new operation **#4 Walkthrough** to `CLAUDE.md` so the walkthrough artifact type is now part of the project schema (operations expanded from four to five).
- `index.md` updated — concept section split into "AM modulation/demodulation" and "Pulse modulation + multiplexing + amplification" subsections; new HW7 entries added to Examples and Summaries.

## [2026-04-26] lint | LaTeX-math sweep across the wiki
- Trigger: CLAUDE.md was strengthened earlier today with a non-negotiable "Math notation — always use LaTeX" rule (inline `$ … $`, display `$$ … $$`, ASCII/Unicode math characters banned in prose, tables, summaries, walkthroughs, query answers).
- Pass 1 (earlier in the session, ~150 files): mass conversion of ASCII/Unicode math to LaTeX across `wiki/concepts/`, `wiki/summaries/`, `wiki/research/`, `wiki/practice/`, `wiki/mistakes/`, and most `wiki/formulas/` and `wiki/examples/`. Last file touched: [[wsl2-embedded-workflow]] before the session ended.
- Pass 2 (this resume, 13+ files): finished the long tail.
  - Five untouched examples fully converted: [[stick-breaking-iterated-expectations]], [[polling-sample-size]], [[mle-for-exponential-rate]], [[map-detection-antipodal]], [[covariance-of-x-and-x-plus-z]].
  - Six partially-converted examples cleaned up: [[fair-coin-significance-test]], [[lmse-discrete-pmf]], [[lmse-continuous-pdf]], [[mmse-vs-lmse-erlang]], [[eee-304-hw7-walkthrough]] (only the inline-prose `μs` instances; the report-template code block at the bottom is intentional ASCII per the file's own note).
  - Course pages: [[eee-350]], [[eee-304]], [[eee-404]], [[python-ml-wireless]] roadmap entries.
  - Concept pages: [[butterfly]], [[significance-test]], [[standardization]], [[map-detection]], [[regretful-learning]] — single-line tail-of-file references to Greek symbols.
  - Mistake log: [[prob-gotchas]] — `Correlation ≠ causation` line.
- **Deliberately left as ASCII** (intentional per CLAUDE.md's "fenced code blocks NOT LaTeX" carve-out): pipeline diagrams in [[system-pipeline]], [[chopper-amplifier]], [[pluto-experiment-lifecycle]], [[robust-signaling]]; report-template code blocks at the bottom of [[eee-304-hw7-walkthrough]] and [[eee-304-lab-4-walkthrough]] (explicit "this is plain ASCII for handwritten submissions" note); Python comments in [[numpy-vectorization]]; flow arrows (`→`) in prose lists describing trajectories or workflows (e.g., [[alkhateeb]] PhD → industry placements, [[python-ml-wireless]] reading-order arrows, [[modulation-index]] case-by-case bullets); frontmatter `title:` fields (Obsidian metadata, not rendered as math).
- No structural changes — only character-level conversions and `updated:` date bumps. No new concept pages introduced.

## [2026-04-26] walkthrough | EEE 304 Lab 4 — corrected Part 3 missing-block analysis
- Trigger: Jayden flagged that one of the missing blocks in `AM_Mod_coherent_tada_inc.slx` was the **carrier signal**, not the Demodulator multiplier as the original walkthrough claimed.
- Verified directly against the .slx XML (unzipped `simulink/blockdiagram.xml` + `configSet0.xml`):
  - Modulator and Demodulator (`Product`) blocks are **already present**.
  - The two missing blocks are the **carrier source** (Signal Generator / Sine Wave, feeding both multipliers) and the **LPF** (`Analog Filter Design`).
  - Solver: `ode3` fixed-step with `FixedStep = 1/22050` → simulation Nyquist $= 11025$ Hz. **Critical:** the 20 kHz carrier from Part 1 (where `FixedStep = 1e-6`) cannot be reused here — it would alias.
- Updated [[eee-304-lab-4-walkthrough]] § #3:
  - Replaced "Block 1 = Product multiplier" with "Block 1 = Signal Generator, sine, $f_c = 5000$ Hz, amplitude $2$, branched to both multipliers."
  - Derived $f_c = 5$ kHz as the unique window satisfying (a) $f_c < f_s/2$, (b) $f_c > 2B$ for $B \approx 2$ kHz tada bandwidth, (c) $2f_c < f_s/2$ so the demod image stays below sim Nyquist.
  - Updated LPF cutoff from $2\pi \cdot 10000$ to $2\pi \cdot 5000$ rad/s, order $4 \to 6$, since the image is now at $10$ kHz instead of $40$ kHz and rejection has less octave-margin.
  - Added unit-gotcha callout: Signal Generator uses Hz, Sine Wave (Time-based) uses rad/s — picking the wrong block silently aliases the carrier.
  - Added a `revisions:` frontmatter line documenting the correction so future readers know the original was wrong.
  - Updated report-template skeleton at the bottom of the walkthrough with the corrected block list and justification.
- No new concept pages. No changes to [[eee-304]] or [[lab-eee-304-lab-4-am-modulation]] (the summary's general claims about coherent demod / $\mu$ / Butterworth design remain correct).

## [2026-04-26] walkthrough | EEE 350 HW7 — Significance testing + MMSE/LMSE estimation
- Trigger: the EEE 350 HW7 ingest from 2026-04-24 produced four standalone worked-example pages but **no unified walkthrough**, so it failed to match the convention set by the later EEE 304 HW7 (`eee-304-hw7-walkthrough.md`). Filling that gap.
- New page: [[eee-350-hw7-walkthrough]] — per-problem walkthrough of all four HW7 problems (11.1.6 fair-coin significance test; 12.2.3 LMSE from discrete PMF; 12.2.4 LMSE from continuous PDF; 12.2.6 MMSE-vs-LMSE with Erlang prior). Same bold + Obsidian `==highlights==` + callout-block format as [[eee-304-hw7-walkthrough]] and [[eee-304-lab-4-walkthrough]]. Cross-links each section to the existing standalone example page for full algebraic detail.
- Updated [[eee-350]] course page — added a new "Walkthroughs" subsection (matching the structure of [[eee-304]]) linking the new page.
- Updated [[homework-2026-04-23-eee-350-hw7]] — added a "Walkthrough" section above "Worked examples" pointing at the new page (mirrors [[homework-2026-04-26-eee-304-hw7]]).
- Updated `index.md` — added the walkthrough as the first entry under "EEE 350 examples" so it appears at the top alongside the unified EEE 304 walkthroughs.
- No new concept pages, no source changes, no edits to the four existing example pages — the walkthrough is a new aggregation layer on top of work already done.

## [2026-04-27] walkthrough | EEE 404 HW5 — DTFT, windowing, FFT compute, STM32 budget
- Source: `raw/homework/hw5.pdf` (no worked-solution sample). Two problems: Problem 1 is a five-part DTFT/Hamming/butterfly drill on a two-tone signal at $f_s = 8$ kHz; Problem 2 is a four-part rectangular-vs-Hamming window-resolution drill plus a real-time STM32F407 (168 MHz, 1 inst/cycle, 400-instruction budget) sizing question on signals at $f_s = 1.68$ MHz.
- New summary: [[homework-2026-04-27-eee-404-hw5]].
- New walkthrough: [[eee-404-hw5-walkthrough]] — full per-problem treatment with **collapsible derivation drop-downs** (`<details><summary>📐 Show derivation</summary>...</details>`) next to each headline equation. Headline answer is shown in `==highlight==`; the in-depth algebra/justification is hidden behind the toggle so the page stays scannable but the full derivation is one click away. New format request from Jayden — also saved to `feedback_assignment_walkthroughs.md` for future walkthroughs.
- New concept pages (2): [[dtft]] (the continuous-frequency parent of the DFT — DTFT-of-cosine pair, $2\pi$-periodicity, DTFT-vs-DFT comparison) and [[window-resolution-criterion]] (formal "two tones resolvable iff separation $\geq$ main-lobe width" rule, with the four canonical main-lobe widths in a table).
- Headline answers across all 9 sub-problems:
  - 1(a) impulses at $\pm\pi/4$ (height $2\pi$) and $\pm\pi/3$ (height $\pi$)
  - 1(b) $L = 64$ Hamming **cannot** resolve (main-lobe $\pi/8 >$ separation $\pi/12$)
  - 1(c) $L^* = 96$ (smallest Hamming that resolves)
  - 1(d) $\Delta f = 8000/96 \approx 83.33$ Hz
  - 1(e) $192$ butterflies for the 64-point FFT
  - 2(a) impulses at $\pm\pi/3, \pm\pi/2$ (for $X$) and $\pm\pi/6, \pm\pi/3$ (for $Y$), all height $\pi$
  - 2(b) $L_{\min} = 24$ (rectangular)
  - 2(c) $L'_{\min} = 48$ (Hamming)
  - 2(d) $L^* = 4$ samples — far below the resolution requirement, illustrating the real-time-vs-resolution trade-off
- Updated [[eee-404]] course page — added HW5 to "Sources filed", added new "Walkthroughs" section with the HW5 walkthrough link, added the two new concept pages to the roadmap.
- Updated `index.md` — added the walkthrough at the top of "EEE 404 examples", added the source under "EEE 404 summaries", added the two new concept pages to the EEE 404 concepts list.

## [2026-04-27] walkthrough | EEE 404 HW5 — fix collapsible drop-down syntax
- Issue Jayden flagged: the original `<details><summary>...</summary>...</details>` HTML approach for the "Show derivation" drop-downs was rendering broken in Obsidian — the LaTeX `$...$` and `$$...$$` inside showed as raw code instead of typeset math, and the callout title rendered as code-styled text. Obsidian's markdown parser doesn't process markdown/LaTeX inside raw HTML blocks reliably.
- Fix: replaced all 9 `<details>` blocks in [[eee-404-hw5-walkthrough]] with **Obsidian-native foldable callouts** using `> [!info]- 📐 Show derivation — <label>` syntax (the trailing `-` after `[!info]` makes the callout collapsed by default; `[!info]+` would make it expanded). Every body line is now prefixed with `> ` and display-math blocks have blank `>` lines around them for proper rendering.
- Updated `feedback_assignment_walkthroughs.md` memory — replaced the `<details>` instructions with the corrected `> [!info]-` syntax block, including the rule that **display math inside callouts needs blank `>` lines around it** to render.
- No other content changed in the walkthrough — same problems, same headline answers, same step-by-step derivations. Only the wrapper syntax for the drop-downs was rewritten.

## [2026-04-27] setup | New `wiki/walkthroughs/` folder + reorganization
- Created `wiki/walkthroughs/` as a new top-level folder of the wiki, separate from `wiki/examples/`. Walkthroughs are the headline teaching artifact for full lab/HW assignments; standalone worked examples (one-off problems) stay in `wiki/examples/`. Cleaner organization than mixing both kinds in one folder.
- Moved 5 files from `wiki/examples/` → `wiki/walkthroughs/`: [[eee-304-hw7-walkthrough]], [[eee-304-lab-4-walkthrough]], [[eee-350-hw7-walkthrough]], [[eee-404-hw5-walkthrough]], and the renamed [[eee-404-lab-7-fill-in-walkthrough]] (which Jayden also normalized from the older `lab-7-fill-in-walkthrough.md` to follow the `<course>-<assignment>-walkthrough.md` convention).
- All wiki-links resolve unchanged because Obsidian links by basename, not path. The 13 standalone examples (e.g. [[fair-coin-significance-test]], [[lmse-discrete-pmf]], [[dft-computation-burden]], …) remain in `wiki/examples/` since they are one-off teaching examples, not full assignment walkthroughs.
- Schema updates in `CLAUDE.md`:
  - Directory layout diagram now lists `walkthroughs/` between `examples/` and `practice/`.
  - "Walkthroughs in `wiki/examples/` …" line in the naming-convention section was updated to `wiki/walkthroughs/`, with a back-pointer noting the 2026-04-27 move so future readers know the path changed.
  - Operation #4 (Walkthrough) updated to write into `wiki/walkthroughs/` instead of `wiki/examples/`.
- `feedback_assignment_walkthroughs.md` memory updated — workflow now writes to `wiki/walkthroughs/` for new walkthroughs.
- `index.md` reorganized: added a new top-level `## Walkthroughs` section (above `## Examples`) listing all 5 walkthroughs grouped by course; the `## Examples` section now contains only standalone worked examples.

## [2026-04-28] ingest | Canvas API workload pull — week of 4/28 → 5/12
- First Canvas integration. Jayden shared a personal API token + ASU domain (`canvas.asu.edu`); used it to enumerate active 2026 Spring C courses (EEE 341, 304, 350, 202 Lab, 335, 404) and pull each course's upcoming assignments via the REST API. Cached responses at `/tmp/canvas_*.json` for re-reads within the session; not committed to `raw/`.
- Found **24 items in the next 14 days totaling ~1,366 pts**, including two finals: EEE 404 Exam 2 (Thu 4/30, 150 pts) and EEE 304 Final Exam (Wed 5/6, 350 pts). Friday 5/1 has 11 items due simultaneously — mostly EEE 341 ABET exams + EEE 404 extra credit + EEE 202 final design project.
- Wrote [[daily-2026-04-28-workload]] in `wiki/summaries/` (using the existing `daily-` source-type prefix). Includes triage table sorted by due date, day-by-day plan with recommended sequencing, conflict callouts (Thursday is worst), wiki-first prep map per item, and an offered-walkthrough list (EEE 335 Lab 5, EEE 335 HW8, EEE 341 Lab 5, EEE 202 Final Project, EEE 404 Project 2, EEE 304 EC Labs 1&2 — all candidates if Jayden drops the PDFs into `raw/`).
- `index.md` extended with a new "Workload planning" subsection under Summaries, containing the new page.
- Token security note: shared token can be revoked at Canvas → Account → Settings → Approved Integrations when done; the value is in the session transcript and tmp files only.

## [2026-04-28] setup | Canvas dashboard + Lyra agent + finals prep across all 5 active courses
- **Canvas config persisted.** Token + domain saved to `.canvas-config` at the project root so the dashboard can re-fetch without re-prompting. **Treat that file like a credential** — don't commit to a shared repo. To rotate: regenerate at Canvas → Account → Settings → "+ New Access Token" and update the file.
- **Dashboard script** at `scripts/dashboard.py` (Python stdlib only). Reads `.canvas-config`, fetches assignments for the 5 active courses Jayden is taking (excludes EEE 202 lab where he's the TA), scans the wiki for recently-touched pages, and prints a colored terminal dashboard with: today/soon priorities (auto-linked to relevant wiki pages), assignments-due table sorted by date, recently-touched wiki files, and per-course breakdown. Run with `python scripts/dashboard.py` (default 14-day horizon), `--week` for 7 days, `--refresh` to re-fetch.
- **Lyra prompt-optimizer agent** at `.claude/agents/lyra.md`. Adapted from a user-supplied template, augmented with wiki-awareness: before optimizing a prompt, Lyra scans `wiki/` for relevant pages and bakes `[[wiki-link]]` cross-references into the output prompt so downstream agents reach for class-taught framings before generic ones. Honors the wiki-first sourcing rule. Invoke with the `Agent` tool, `subagent_type: "lyra"`.
- **Workflow update in `CLAUDE.md`**: added a new "Canvas integration" section documenting the Workflow 1 weekly-check loop (which now **auto-downloads every attached file** for due assignments) and Workflow 2 (the terminal dashboard). Added a "Custom agents" section listing Lyra.
- **Finals prep across all 5 active courses** ([[daily-2026-04-28-finals-prep]] is the master document):
  - Pulled syllabus + modules for all 5 courses via Canvas API. Files endpoint is permission-denied for students (93-byte response), so module/page metadata is the source.
  - **EEE 341 (Electromagnetics)** — created stub [[eee-341]] course page with the 6-module roadmap (Foundations → Plane Waves → Reflection/Transmission → Transmission Lines → Waveguides → Antennas) reconstructed from Canvas modules. No concept pages yet — final exam prep needs raw-source ingest of textbook chapters and sample exams.
  - **EEE 335 (Analog/Digital Circuits)** — created stub [[eee-335]] course page with the 6-unit roadmap (MOSFET → CMOS Logic → Memory → IC Amplifiers → Frequency Response → Multi-Transistor/Differential). Sedra/Smith 8e is the canonical reference. No concept pages yet — same need for raw-source ingest.
  - Confidence audit: 🟢 EEE 404 (FFT module fully covered), 🟢 EEE 350 (60+ concept pages from 2026-04-21 ingest), 🟡 EEE 304 (only Module 7 / AM arc covered; Modules 1–6 are gaps), 🔴 EEE 341, 🔴 EEE 335.
  - Per-course study plan included, with explicit "wiki gaps for this exam" callouts and recommended pre-requisite ingest steps before walkthroughs are useful.
- **EEE 304 gap flagged** — wiki only covers Module 7 (AM/PAM/TDM) but the final spans Modules 1–7. Strongly recommended pre-final ingest: HW1–6 solutions are filed in Canvas (`304_hwN_sol.pdf` per module), can be ingested to fill the gap.
- `index.md` updated — Courses section now lists all 5 active courses (with stub markers on 341/335); Summaries → Workload planning subsection adds the finals-prep page.

## [2026-04-28] ingest | EEE 335 — full slide ingest (35 lectures across 6 units) + finals walkthrough
- Source: 79 PDFs in `raw/slides/eee-335/` (slides + per-lecture problem and solution decks). Pre-extracted text at `/tmp/eee335_text/` (75 files).
- **15 concept pages** written (basenames verified unique against existing concepts/ folder):
  - **Unit 1:** [[mosfet-iv-characteristics]], [[mosfet-body-effect]]
  - **Unit 2:** [[cmos-inverter-vtc]], [[cmos-transistor-sizing]], [[cmos-power-dissipation]]
  - **Unit 3:** [[pass-transistor-logic]], [[sram-cell]]
  - **Unit 4:** [[mosfet-small-signal-model]], [[common-source-amplifier]], [[common-gate-amplifier]], [[source-follower]], [[current-mirror]]
  - **Unit 5:** [[mosfet-high-frequency-model]], [[millers-theorem]], [[octc-method]], [[cs-amplifier-frequency-response]]
  - **Unit 6:** [[cascode-amplifier]], [[differential-pair]], [[cmrr]]
- **Walkthrough page:** [[eee-335-final-walkthrough]] — per-unit (Units 1–6) finals study guide, ~22 worked problems with collapsible derivations, plus comprehensive cheat-sheet table at the bottom (DC formulas, small-signal, CMOS logic, three amplifier configurations, current mirror, diff pair/CMRR, high-frequency).
- **Course page:** [[eee-335]] replaced stub with full populated version — roadmap promoted from plain text to wiki-links, sources-filed section lists all 35 lectures grouped by unit.
- **`index.md`:** added `### EEE 335 (Analog & Digital Circuits)` subsection under Concepts (15 entries grouped by unit) and `### EEE 335` under Walkthroughs.
- All math in LaTeX per CLAUDE.md rule; no per-slide summary files (concepts cite source PDFs directly in frontmatter).

## [2026-04-28] ingest | EEE 341 — 49 lecture slides + finals walkthrough
- Source: 49 PDFs in `raw/slides/eee-341/` (Prof. James T. Aberle's lecture decks across 6 modules). Pre-extracted text at `/tmp/eee341_text/` (49 .txt files).
- **20 concept pages** written (basenames verified unique against existing concepts/ folder):
  - **Module 1 — Foundations:** [[maxwell-equations]], [[displacement-current]], [[boundary-conditions-em]]
  - **Module 2 — Plane waves:** [[helmholtz-equation]], [[complex-permittivity]], [[plane-wave-lossless]], [[plane-wave-lossy]], [[wave-polarization]], [[poynting-vector]]
  - **Module 3 — Reflection/refraction:** [[fresnel-coefficients]], [[snells-law]], [[brewster-angle]], [[total-internal-reflection]]
  - **Module 4 — Transmission lines:** [[transmission-line-model]], [[reflection-coefficient-line]], [[smith-chart]]
  - **Module 5 — Waveguides/cavities:** [[waveguide-modes]], [[waveguide-cutoff]], [[cavity-resonator]]
  - **Module 6 — Antennas:** [[hertzian-dipole]], [[half-wave-dipole]], [[antenna-gain-directivity]], [[friis-formula]]
- **Walkthrough page:** [[eee-341-final-walkthrough]] — per-module (Modules 1–6) finals study guide, ~22 worked problems with collapsible `📐 Show derivation` callouts, leading "memorize first" formulas at the top of each module, comprehensive cheat-sheet table at the bottom (Maxwell, plane-wave parameters, Fresnel/Snell/Brewster/TIR, transmission lines, Smith chart, waveguides + cavities, antennas + Friis).
- **Course page:** [[eee-341]] replaced stub with full populated version — roadmap promoted from plain text to wiki-links, sources-filed section lists all 49 lectures grouped by module.
- **`index.md`:** added `### EEE 341` line under Walkthroughs and `## Concepts — EEE 341 (Electromagnetics)` subsection under Concepts (20 entries grouped by module).
- All math in LaTeX per CLAUDE.md rule; no per-slide summary files (concepts cite source PDFs directly in frontmatter).

## [2026-04-30] setup | Deferred routine config — Wi-Lab cold email to Alkhateeb
- Saved deferred RemoteTrigger config (Opus 4.7, Gmail connector, second-brain repo, full self-contained prompt) to [[daily-2026-04-30-alkhateeb-email-routine-config]] for one-shot firing in ~Apr 2027 once Phase 3 portfolio (LWM/DeepMIMO/Sionna repo) is live.
- `run_once_at` left blank by user request — re-fire when ready by pasting body into `RemoteTrigger create`.
