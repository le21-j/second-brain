# Operations Log

Append-only chronological record of every operation on the wiki. One entry per op. Format:

```
## [YYYY-MM-DD] {op} | {title}
- bullets describing what was touched
```

Greppable: `grep "^## \[" log.md | tail -10`

Ops: `ingest` · `query` · `practice` · `walkthrough` · `lint` · `setup` · `tutor`

---

## [2026-05-04] walkthrough | EEE 404 Lab Exam + ABET Quiz (Tue 5/5 9:50–11:40 AM)
- Pulled scope from Canvas API (course 241591): announcement 7051419 from [[chao-wang]] dated 2026-04-23 spelled out exact format — Lab Exam = 5 MC (Lab 5 / Lab 6 / Project 1 / Project 2 / Assembly), 15 min, 50 pts, open book; ABET Quiz = comprehensive paper, 30 min, 50 pts, closed book + 2× 8.5×11 sheets
- Auto-downloaded: `lab5_overview.pdf`, `lab6_overview.pdf`, `project1_overview.pdf` (into `raw/labs/eee-404/lab-exam-prep/`); `exam1_review.pdf`, `exam1_key.pdf`, `exam2_review.pdf` (into `raw/other/eee-404/`)
- Wrote `wiki/walkthroughs/eee-404-final-quiz-walkthrough.md` — combined walkthrough (back-to-back same morning, content overlaps): §A Lab Exam study guide (5 topic blocks with framework + headline answers + memorize-vs-derive callouts) + §B ABET Quiz cheat-sheet skeleton (sampling/LTI/conv, Q-format/floating point, ARM ISA, image processing, music synthesis, memorize-cold list, short-essay rehearsal prompts, T/F + fill-in reflexes) + §C pre-exam routine
- Updated `index.md` — promoted new walkthrough to top of EEE 404 walkthroughs

## [2026-05-04] practice | EEE 335 Final Practice Set 01 (Tue 5/5 12:10–2:00 PM)
- Pulled scope from Canvas API (course 245462): announcements confirmed Tue May 5 12:10–2:00 PM, SCOB 250, Units 4–6 (Lectures 17–36 + CCA + CCA-HFR); UGTA Diego's 4/30 correction noted ("diff pair is non-inverting" with the input convention used)
- Wrote `wiki/practice/eee-335-final-set-01.md` — 11 problems mixed difficulty (~134 pts simulated, vs 110 real exam) covering all 10 problem types from [[eee-335-final-lecture-review]]: Q-point + small-signal extraction (P1), configuration choice + $G_v$ (P2), current-mirror biasing (P3), basic gain cell + swing (P4 ≈ Sedra Ex 8.3), CS HF first analysis (P5 ≈ Spring 2025 P1), OCTC on the same CS (P6), Cascode HF advantage (P7 ≈ Spring 2025 P2), CM-loaded diff amp full pipeline ($A_d, A_{cm}$, CMRR, L36 pole/zero — P8 ≈ Spring 2025 P4), T/F drill (P9), MC + short answer (P10), 2-stage cascode + diff amp bonus (P11)
- Each solution invokes the 5 framework patterns from [[eee-335-final-lecture-review]]; What-to-memorize-vs-derive callouts on every problem; collapsible solution dropdowns; cross-links to existing concept pages and to [[eee-335-l36-cm-cl-set-01]] for difficulty calibration; master cheat-sheet anchor at end
- Updated `index.md` — added new practice set to Practice section under existing EEE 335 set

## [2026-05-04] walkthrough | EEE 304 Final Exam — full numerical solutions (8 problems, 350 pts)
- Ingested two new files into `raw/slides/eee-304/`: `304final-1.pdf` (1 pp, the actual final exam with specific numbers + Tsakalis transform sheet) and `fourier.pdf` (12 pp, Oppenheim-Willsky transform tables — open-book reference)
- Wrote `wiki/summaries/slides-2026-05-04-eee-304-final-exam.md` — TL;DR + per-problem topic+numbers table + open-book reference panel inventory
- Wrote `wiki/walkthroughs/eee-304-final-exam-walkthrough.md` — full per-problem **numerical** solutions for all 8 problems with: stability checks first (caught 2 of 4 unstable systems in P1 → DNE answers), boxed final answers, derivation drop-downs (P7 design-point verification), Nyquist sanity-check (P8), DC-component evaluation gotcha (P8 zero at $z=1$ kills constant), Master cheat sheet, and quick-reference numerical-answers table
- **Verified answers:** P1.1 = $-1$, P1.2 = DNE, P1.3 = $-1/4$, P1.4 = DNE, P2: $\tau = 1/(14\pi)$, P3: $a = \pi/10$, P4: ROC $|z| > 0.5$, P5: $H = 1/(4z^2)$, P6: $N = 13$, P7: $K \approx 13.35$, $\tau_z \approx 0.181$, P8: $y(t) \approx 0.0333\cos(t + 88.4°)$
- Updated `wiki/courses/eee-304.md` — promoted exam walkthrough to top of Walkthroughs (⭐⭐), added both new sources to Sources filed
- Updated `index.md` — promoted exam walkthrough at top of EEE 304 Walkthroughs section (⭐⭐), added exam summary at top of EEE 304 Summaries

## [2026-05-04] walkthrough | EEE 304 Final Exam (8 problems, 350 pts, 150 min — May 4–6 window)
- Ingested `raw/slides/eee-304/Final_slides.pdf` (8 pp, "Final Exam Preview" deck dated 4/23/2026)
- Wrote `wiki/summaries/slides-2026-05-04-eee-304-final-exam-preview.md` — TL;DR + per-problem source map (Modules 1/2/4 + HW1/4/7 + Lab 3)
- Wrote `wiki/walkthroughs/eee-304-final-walkthrough.md` — full per-problem walkthrough of all 8 problems (steady-state response, CT/DT filtering, ROC, Euler/Tustin discretization, PAM TDM/FDM bandwidth, closed-loop control, sampled-data CT equivalents) with: example-first concept explanations, full LaTeX derivations, collapsible drop-downs for the messier algebra (Tustin substitution, Term A/B magnitude+phase decomposition), master cheat sheet, time budget table
- Updated `wiki/courses/eee-304.md` — added "Final Exam arc" section to roadmap, promoted final walkthrough to top of Walkthroughs, added Final Exam Preview slides to Sources
- Updated `index.md` — promoted `eee-304-final-walkthrough` to top of EEE 304 walkthroughs (bolded), added slides summary under EEE 304 Summaries

## [2026-05-03] walkthrough | EEE 335 Final Lecture-by-Lecture Review (Lectures 17–36, Units 4–6)
- Pulled the EEE 335 Final Exam Canvas page (course id 245462; final on Tue May 5, 12:10–2:00 PM, SCOB 250; covers Units 4–6 = Lectures 17–36 + CCA + CCA-HFR; Sedra/Smith Ch 7, 8, 9, 10)
- Downloaded `lecture-review-units-4-6-final-spring-2026-slides.pdf` (115 pp, McDonald Spring 2026 review deck), `practice-final-exam-spring-25.pdf` (8 pp), `practice-final-exam-spring-25-solutions.pdf` (9 pp) into `raw/slides/eee-335/`
- Wrote `wiki/walkthroughs/eee-335-final-lecture-review.md` — per-lecture review for Lectures 17–36 + CCA + CCA-HFR with: textbook section, what's tested, headline formulas, recommended practice problems (from McDonald's "Recommend Practice" callouts in the review deck), master cheat sheet, T/F drill bank, Practice Final 2025 problem-type map, time budget (1 min/pt + 5 min reading)
- Updated `wiki/courses/eee-335.md` — promoted new walkthrough to top of Walkthroughs section
- Updated `index.md` — bolded the new walkthrough under EEE 335 with exam date

## [2026-05-03] walkthrough | EEE 304 Lab EC1 + Lab EC2 (Arduino extra-credit labs)
- Pulled the two extra-credit labs from Canvas API (EEE 304, course id 246317, assignment ids 6968953 + 6968954)
- Downloaded `EEE_304_Lab_EC1.pdf`, `EEE_304_Lab_EC2.pdf`, and the 5 Simulink models (`Arduino_test.slx`, `Tones_1.slx`, `Tones_2.slx`, `Calibrate_Sensor.slx`, `Closed_loop_I_Ctrl.slx`) into `raw/labs/`
- Wrote `wiki/walkthroughs/eee-304-lab-ec1-walkthrough.md` — 5 questions (Arduino_test plot; tone-mixture identification; pin 7/8 grounding table; hardware photo; `butter` filter design at $f_s = 5$ kHz, order 4, three filters)
- Wrote `wiki/walkthroughs/eee-304-lab-ec2-walkthrough.md` — 4 questions (calibration + exponential plant fit $a, b$; integral controller $K_I = 0.01$ for 1 rad/s and $K_I = 0.1$ for 10 rad/s; instability demo; hardware photo)
- Updated `wiki/courses/eee-304.md` — added EC1/EC2 to Walkthroughs and Sources sections
- Updated `index.md` — promoted both walkthroughs under EEE 304 (bold, due 2026-05-06)

## [2026-05-01] practice | generalization-set-01 — Zhang 2017 random-labels prediction
- Created wiki/practice/generalization-set-01.md (Problem 1 = Zhang random-labels prediction; logged Jayden's attempt)
- Created wiki/mistakes/generalization.md (2 gotchas + 1 personal entry)
- Updated index.md
- Socratic 6-turn session built up: train/test acc as measurements not mechanisms; the gap as diagnostic; networks memorize random labels (Zhang 2017); chance level ≠ 0%; structured vs random data via mutual information $I(X;Y)$

## [2026-05-01] ingest | Physical-Layer ML Roadmap Phase 1–4 sources — bulk ingest

**Trigger.** Jayden asked whether the wiki had enough material for the teacher agent to teach the [[python-ml-wireless]] roadmap. Audit found: strong concept-page coverage for Phase 3–4 specialization (Sionna, NRX, DeepMIMO, transformers — already 22+ pages), but thin on Phase 1–2 ML/wireless foundations and zero downloaded textbook/paper PDFs. This ingest fills both gaps.

**PDFs downloaded (free, mirrored locally; ~146 MB total):**
- **Textbooks** (`raw/textbook/pdfs/`): Prince UDL v5.0.3 (21 MB, Feb 2026), Sutton-Barto RL 2ed (42 MB), MacKay ITILA (5.4 MB), Parr Matrix Calculus (743 KB).
- **Papers** (`raw/articles/ml-phy/pdfs/`): O'Shea-Hoydis 2017, Sionna 2022, Sionna RT 2023, NRX Cammerer 2023, NRX Wiesmayr 2024, DeepMIMO 2019, DeepSense 6G 2023, LWM 2024, CsiNet 2018, RadioML 2018, Channel Charting 2018, Digital Twin Vision 2023, Aït Aoudia OFDM 2020, Dörner OTAir 2018, Simeone 2018, ResNet 2015, Attention is All You Need 2017.

**Source summaries written** (`wiki/summaries/`):
- 4 textbook summaries: `textbook-prince-understanding-deep-learning`, `textbook-sutton-barto-rl`, `textbook-mackay-itila`, `textbook-parr-matrix-calculus`. Each anchors confirmed TOC against roadmap month-by-month plan.
- 14 paper summaries (12 priority + 2 supplementary): `paper-oshea-hoydis-2017-autoencoder`, `paper-sionna-2022`, `paper-sionna-rt-2023`, `paper-nrx-cammerer-2023`, `paper-nrx-wiesmayr-2024`, `paper-deepmimo-2019`, `paper-deepsense-6g-2023`, `paper-lwm-2024`, `paper-csinet-wen-2018`, `paper-radioml-oshea-2018`, `paper-channel-charting-studer-2018`, `paper-digital-twin-vision-2023`, `paper-aitaoudia-hoydis-2020-ofdm`, `paper-dorner-2018-otaair`. Simeone, ResNet, Attention left as PDFs only — well-known, no summary needed.

**Foundational concept pages created** (`wiki/concepts/`, 17 pages, all example-first per Jayden's learning style):
- ML foundations: `gradient-descent`, `stochastic-gradient-descent`, `adam-optimizer`, `cross-entropy-loss`, `mse-loss`, `softmax`, `regularization`, `dropout`, `batch-normalization`, `overfitting-bias-variance`.
- Wireless foundations: `qam-modulation`, `ldpc-codes`, `ber-bler`, `mimo-basics`, `fading-channels`, `matched-filter`, `equalization`.

**Why this matters.** Before this ingest, the teacher agent could anchor Phase 3–4 dialogues but would have to improvise (or refuse) for Phase 1–2 questions like "teach me gradient descent" or "teach me QAM." With these 17 foundational pages, the agent can run its full Socratic-retrieval-Bloom-3 playbook across the whole 14-month roadmap.

**Skipped (out of session scope; not yet downloaded):**
- Bishop PRML, Goodfellow DL, Boyd Convex Optimization, Murphy PML — defer.
- Online courses (CS50P, Karpathy Zero-to-Hero, CS231n, etc.) — videos, not text-ingestable; reference cards already exist.
- ~45 secondary papers in `raw/articles/ml-phy/README.md` — defer until Jayden actually reads them.

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

## [2026-05-01] lint | python-ml-wireless wiki audit (post 5/1 ingest)
- Inventoried **423 unique wiki-link targets** vs **352 existing pages**; found **73 broken-link targets** of which ~40 are real gaps (rest are template placeholders / agent names / folder names).
- **Small fixes applied directly (4 edits across 4 files):** `[[ldpc]]` → `[[ldpc-codes]]` in [[textbook-mackay-itila]]; `[[lab-7-fill-in-walkthrough]]` → `[[eee-404-lab-7-fill-in-walkthrough]]` in [[daily-2026-04-28-workload]]; `[[ian-goodfellow]]` → `[[goodfellow]]` in [[generative-adversarial-network]]; `[[paper-noncoherent-dgd]]` → `[[paper-ncota-dgd]]` in [[paper-fsk-mv]].
- **Top finding — textbook-name aliasing.** Across 27 files (incl. [[python-ml-wireless]], all 11 people pages, 14 concept pages), references like `[[deep-learning-with-pytorch]]`, `[[pysdr-lichtman]]`, `[[bishop-prml]]` resolve to nothing. Two redundancy types: (a) 4 books whose summaries already exist under `textbook-` prefix (parr, mackay, prince, sutton) — references to bare names are just misaliased; (b) 9 books referenced but with no summary page (pysdr, goodfellow-DL, deep-learning-with-pytorch, deep-learning-with-python-chollet, from-python-to-numpy, bishop-prml, murphy-pml-intro, ml-with-pytorch-scikit-learn, d2l, scientific-visualization-matplotlib).
- **Inbound-link health on 31 new pages** (2026-05-01 ingest): Phase-1 foundation concept pages all ≥1 inbound link (gradient-descent has 8, cross-entropy 7, regularization 7); paper summaries well-cross-referenced (oshea-hoydis 7, nrx-cammerer 7, sionna 6); textbook-prince-understanding-deep-learning is the most-referenced page in the new batch (14 inbound links). No orphans in the new ingest.
- **Concept-page gaps** (referenced by ≥2 pages, no page exists): `belief-propagation` (3), `mmwave-mimo` (3), `massive-mimo` (2), `chain-rule` (1+), `sigmoid` (1+), `tanh` (1+), `layer-normalization` (1+).
- **Phase-4 paper gaps** (referenced as `[[paper-…]]` but no summary): `paper-diff-rt-calibration-2024`, `paper-lwm-spectro-2026`, `paper-lwm-temporal-2026`. These are the highest-value next ingest candidates.
- Full lint report + proposed ingest plan delivered in chat (not filed as a wiki page; ephemeral). No `index.md` change.

## [2026-05-01] ingest | python-ml-wireless Tier-1 sweep — Phase 4 papers + concept stubs + textbook stubs + alias sweep
- **Trigger.** Jayden approved Tier-1 of the post-lint ingest plan. Ran a single batch with 2 background phy-ml-coach audits in parallel against the NVIDIA-intern roadmap goal (Sionna intern S2027 + Wi-Lab PhD F2028).
- **3 Phase 4 papers downloaded** to `raw/articles/ml-phy/pdfs/` (~21 MB total): `diff-rt-calibration-2024.pdf` (Hoydis et al. IEEE TMLCN, arxiv:2311.18558, the M10 capstone method paper) + `lwm-spectro-2026.pdf` (arxiv:2601.08780, M12 reading) + `lwm-temporal-2026.pdf` (arxiv:2603.10024, M12 reading).
- **3 paper summaries written** in `wiki/summaries/`: [[paper-diff-rt-calibration-2024]], [[paper-lwm-spectro-2026]], [[paper-lwm-temporal-2026]]. Each has reproduce-first / extend-second portfolio move, named baselines, named datasets (DICHASUS / RadioML 2018.01A / DeepMIMO Boston5G_28), interviewer talking-point callouts.
- **2 stub concept pages written** in `wiki/concepts/` to fill the highest-priority lint gaps: [[belief-propagation]] (the canonical DSP↔ML identity bridge — sum-product on factor graph = neural BP / GNN message-passing; Nachmani 2018 / Buchberger 2020 referenced) + [[mmwave-mimo]] (the SHARED Wi-Lab/Sionna load-bearing topic — sparse + hybrid + blockage-prone variant of MIMO).
- **3 people pages written** (audit-driven, NVIDIA cold-email prerequisites): [[aitaoudia]] (NVIDIA Sionna #2 — Hoydis's closest collaborator), [[cammerer]] (NVIDIA Sionna NRX lead — Stuttgart pedigree, owns the NRX repo), [[alikhani]] (Wi-Lab PhD student — first author of LWM/LWM-Spectro/LWM-Temporal).
- **10 textbook reference-card stubs written** in `wiki/summaries/` with `textbook-` prefix: [[textbook-pysdr-lichtman]], [[textbook-bishop-prml]], [[textbook-goodfellow-deep-learning]], [[textbook-deep-learning-with-pytorch]], [[textbook-from-python-to-numpy]], [[textbook-deep-learning-with-python-chollet]], [[textbook-d2l-dive-into-deep-learning]], [[textbook-murphy-pml-intro]], [[textbook-ml-with-pytorch-scikit-learn]], [[textbook-scientific-visualization-matplotlib]]. Each has phase-anchored "where it's used in the roadmap" — Bishop and Murphy promoted from "reference, never required" to specific milestone anchors per audit feedback.
- **Textbook alias sweep across `wiki/`** (sed-driven): rewrote 14 distinct broken bare-name wiki-links to canonical `textbook-` prefix across all `.md` files (e.g. `[[deep-learning-with-pytorch]]` → `[[textbook-deep-learning-with-pytorch]]`, `[[prince-understanding-deep-learning]]` → `[[textbook-prince-understanding-deep-learning]]`, `[[mackay-information-theory]]` → `[[textbook-mackay-itila]]`, etc.). `raw/textbook/*.md` reference cards left untouched (immutable).
- **Audit-driven fixes applied (8 edits):** added DICHASUS dataset name + classical-baselines section + "interviewer talking point" callout to diff-rt-calibration; reordered diff-rt portfolio move so reproduce comes first and PR/workshop is explicit stretch; added Step 0 reproduce step + named baselines (CNN/ResNet/ViT-from-scratch) to lwm-spectro; softened over-stated "InterDigital ships codecs" → "R&D + standards-essential patents" in lwm-temporal; added baselines + csi-feedback cross-link to lwm-temporal; reframed Bishop "no phase devotes time" → table of M4/M6/M7/M11 chapter anchors; reframed Murphy similarly; strengthened Phase 2 M4 "headline figure = first thing NVIDIA reviewer sees" in scientific-visualization-matplotlib; added [[graph-neural-network]] cross-link + corrected M9 → M7/M10–M12 in belief-propagation; added [[antenna-array]] to mmwave-mimo Related.
- **Navigation updated.** [[python-ml-wireless]] course page promoted belief-propagation + mmwave-mimo from "stub TBD" to live wiki-links, added 3 people-page wiki-links, added Phase-4 papers + 10 textbook stubs to Sources sections; `index.md` got new subsections under Summaries (Phase 4 papers + textbook reference-card stubs) and 3 new people entries under Target labs.
- **Broken-link inventory after sweep:** 73 → 45 (net −28). Remaining 45 split between EEE-341 EM concepts (10 — not roadmap-relevant), AirComp/research stubs (~7), template placeholders (`link`, `wiki-link`, `formulas`, `research`, `teacher` — 5), and a tail of legitimate concept gaps for next-tier ingest (`chain-rule`, `sigmoid`, `tanh`, `layer-normalization`, `massive-mimo`, `mixed-precision-training`, `quantization-aware-training`, `sim-to-real`, `foundation-model`).
- **Audit feedback flagged for Tier 2:** `sionna-rt` deep-dive concept page; `nvidia-aodt` (Aerial Omniverse Digital Twin) concept page; `neural-decoder` concept page distinct from `neural-receiver`. All three are explicit NVIDIA-intern cold-email vocabulary.
- Total: **3 PDFs, 16 new wiki pages (3 papers + 2 concepts + 3 people + 10 textbooks), 2 background audit agents, 8 audit-driven edits, 14-alias sed sweep across `wiki/`.**

## [2026-05-01] ingest | python-ml-wireless Tier-2 sweep — Phase 4 NVIDIA-Aerial 2025 line + Wi-Lab 2024-2026 papers + 3 cold-email concept pages
- **Trigger.** Jayden approved Tier-2 immediately after Tier-1 — same session. Continued the same NVIDIA-Sionna-intern lens with a third background phy-ml-coach audit.
- **6 Phase 4 papers downloaded** to `raw/articles/ml-phy/pdfs/` (~67 MB total): `morais-similarity-2026.pdf` (arxiv:2601.01023), `osman-ris-oran-2025.pdf` (arxiv:2510.20088), `deepsense-v2v-2024.pdf` (arxiv:2406.17908), `sionna-research-kit-2025.pdf` (arxiv:2505.15848), `wiesmayr-salad-2025.pdf` (arxiv:2510.05784), `luo-dt-csi-feedback-2025.pdf` (arxiv:2509.25793).
- **6 paper summaries written:** [[paper-sionna-research-kit-2025]] (the literal NVIDIA Aerial-team product an intern would deploy), [[paper-wiesmayr-salad-2025]] (15% throughput beat over OLLA via ACK/NACK-only link adaptation), [[paper-morais-similarity-2026]] (task-aware dataset distance, Pearson > 0.85 with transferability), [[paper-deepsense-v2v-2024]] (120 km mmWave V2V dataset), [[paper-osman-ris-oran-2025]] (1024-elem 28-GHz RIS hardware, MILCOM 2025 Best Demo), [[paper-luo-dt-csi-feedback-2025]] (digital-twin fidelity decomposition for CSI compression). All have reproduce-first portfolio moves with named baselines + interviewer talking-points.
- **3 NVIDIA-cold-email concept pages written:** [[sionna-rt]] (the differentiable RT module, distinct from the [[sionna]] umbrella — load-bearing for the M10 capstone reproduction), [[nvidia-aodt]] (Aerial Omniverse Digital Twin product — what the BS-level intern would actually work on; with explicit factual-caveats callout per audit), [[neural-decoder]] (BP-replacement subblock distinct from [[neural-receiver]]; Cammerer's PhD line).
- **1 person page added:** [[wiesmayr]] — ETH PhD student with **NVIDIA-internship-then-coauthorship trajectory** = the literal example of the role Jayden is targeting. First author of NRX-2024 + SALAD-2025.
- **Audit-driven fixes applied (7 edits):** factual API correction in [[sionna-rt]] (`scene.get` → `scene.radio_materials["itu_concrete"]` for Sionna 1.x); softened "the stack" framing in [[nvidia-aodt]] to "a commercial GPU stack used in operator trials"; added integration-caveat callout warning that AODT 25.x integrates with Aerial as separate components, not a fused pipeline; replaced broken `[[hypothesis-test]]` with `[[neyman-pearson-test]]` in SALAD; wiki-linked `[[ris]]` and `[[o-ran]]` (Tier-3 stubs) in Osman so links fail loud; back-linked SRK + Luo papers from sionna-rt; added paper cross-links to nvidia-aodt.
- **Navigation updated.** [[python-ml-wireless]] course page added Phase 4 Tier-2 paper group block (NVIDIA Aerial 2025 flagship line + Wi-Lab sim-to-real + Wi-Lab V2V/RIS hardware), promoted sionna-rt + nvidia-aodt + neural-decoder concept pages, added wiesmayr to people list. `index.md` got Tier-2 paper subsection + 3 new concept entries + wiesmayr in target-labs section.
- **Audit-flagged Tier 3 candidates:** (a) **Gruber/Cammerer/Hoydis/ten Brink 2017** "On Deep Learning–based Channel Decoding" (CISS) — the load-bearing prereq for any Cammerer cold email; (b) Phase 2 M6 **generative foundations**: Kingma 2013 VAE (arxiv:1312.6114), Goodfellow 2014 GAN (arxiv:1406.2661), Ho 2020 DDPM (arxiv:2006.11239) — currently the M6 generative line has zero PDF backing; (c) **Tse-Viswanath Ch 7–8** for Phase 2 mmWave/MIMO grounding before LWM; (d) stub concept pages for `[[ris]]`, `[[o-ran]]`, `[[link-adaptation]]`, `[[umap]]`, `[[tensorrt]]` so Tier-2 summaries stop introducing dead links.
- Total: **6 PDFs, 10 new wiki pages (6 papers + 3 concepts + 1 person), 1 background audit agent, 7 audit-driven edits.**

## [2026-05-01] setup | Teacher web-app for Socratic-tutor UX with proper Markdown + LaTeX rendering
- **Trigger.** Jayden noted that `/teacher` in Claude Code's terminal renders LaTeX as raw `$\mu$` text and Markdown as raw `##` / `> [!note]` syntax — making Socratic dialogue hard to digest. Asked for a local web app that lives in this repo and syncs across devices.
- **Built `apps/teacher/`** — minimal local web app: FastAPI backend (`server.py`, ~120 lines) wraps the Anthropic SDK with prompt caching on the system prompt; loads the same `~/.claude/agents/teacher.md` persona used by `/teacher`; serves a single static HTML chat UI (`static/index.html`) with marked.js (Markdown), KaTeX (LaTeX with auto-render), highlight.js (code), and localStorage conversation persistence.
- **Files:** `apps/teacher/{README.md, pyproject.toml, .env.example, .gitignore, server.py, static/index.html}`. uv-managed Python deps (anthropic, fastapi, uvicorn, dotenv, pydantic).
- **Sync model.** `apps/teacher/` is committed; `.env` (API key) is gitignored. New device: `git pull && cd apps/teacher && cp .env.example .env && [add key] && uv sync && uv run server.py` → http://localhost:8765.
- **Features.** Model selector (Sonnet 4.6 / Opus 4.7 / Haiku 4.5); New-chat reset; Copy / Save→wiki buttons (clipboard-copies a Markdown attempt block ready to paste into `wiki/practice/`); usage stats showing cached tokens so prompt-caching savings are visible.

## [2026-05-01] ingest | python-ml-wireless Tier-3 sweep — Phase 2 generative foundations + Phase 3 RL atoms + dead-link stubs
- **Trigger.** Jayden approved Tier-3 in the same session. Final tier of post-lint ingest plan.
- **4 foundational papers downloaded** to `raw/articles/ml-phy/pdfs/` (~14.9 MB total): `gruber-2017-channel-decoding.pdf` (arxiv:1701.07738, the **mandatory pre-Cammerer-cold-email read** — neural-decoder origin), `kingma-2013-vae.pdf` (arxiv:1312.6114), `goodfellow-2014-gan.pdf` (arxiv:1406.2661), `ho-2020-ddpm.pdf` (arxiv:2006.11239).
- **4 paper summaries:** [[paper-gruber-2017-channel-decoding]] (Cammerer's PhD line origin), [[paper-kingma-2013-vae]], [[paper-goodfellow-2014-gan]], [[paper-ho-2020-ddpm]] — closes Phase 2 M6 generative reproduction line + the load-bearing Cammerer cold-email prereq.
- **7 RL atomic concept pages** in `wiki/concepts/`: [[q-learning]], [[sarsa]], [[policy-gradient]], [[reinforce]], [[actor-critic]], [[ppo]], [[dqn]]. Closes the gap where Sutton-Barto was filed as textbook but no atomic pages existed for the teacher agent.
- **5 stub concept pages** to close loud-fail dead links from Tier-2 audit: [[ris]], [[o-ran]], [[link-adaptation]], [[umap]], [[tensorrt]]. (`antenna-array` already existed from EEE 341.)
- **Navigation updated.** Course page got Tier-3 paper subsection + RL atoms group + Industrial/deployment group; `index.md` got 5 new concept-section subgroups.
- **Final broken-link inventory after Tier-3:** 438 link targets vs 398 pages = 59 broken (most are still EEE-341 EM concepts not roadmap-relevant + research-track stubs + template placeholders). All audit-flagged Tier-2 dead links closed.
- **Roadmap state after Tier-3:** Phase 1 ✅✅, Phase 2 ✅ (generative trio now backed by PDFs), Phase 3 ✅✅ (RL fully covered, atomic pages exist), Phase 4 ✅✅ (12 papers ingested across NVIDIA + Wi-Lab clusters), Phase 5 process-only.
- Total: **4 PDFs, 16 new wiki pages (4 papers + 7 RL + 5 stubs), 1 background audit agent.**

**Cumulative across the 2026-05-01 session: 13 PDFs downloaded + 42 new wiki pages (13 papers + 12 concepts + 4 people + 13 textbook stubs/full) + 4 audit-agent passes + 1 web app + 19 audit-driven edits.**

## [2026-05-01] lint | Tier-3 audit fixes (cross-link + factual + reproduce-discipline)
- **Trigger.** Third phy-ml-coach audit pass (Tier-3 batch) returned a 14-item punch list. Applied all 14 fixes inline.
- **Cross-link gaps closed (5 — these were teach-blockers):** [[reinforcement-learning]] umbrella now wiki-links the 7 atomic RL pages ([[q-learning]], [[sarsa]], [[policy-gradient]], [[reinforce]], [[actor-critic]], [[ppo]], [[dqn]]) instead of plain text; [[variational-autoencoder]] now sources [[paper-kingma-2013-vae]]; [[generative-adversarial-network]] now sources [[paper-goodfellow-2014-gan]] + reading order points at the wiki-link; [[diffusion-model]] now sources [[paper-ho-2020-ddpm]]; [[neural-decoder]] now sources [[paper-gruber-2017-channel-decoding]] + reading order leads with it as "mandatory pre-Cammerer-cold-email read."
- **Factual fixes (3):** [[paper-ho-2020-ddpm]] sampling pseudocode rewritten to match Algorithm 2 paren grouping; [[paper-gruber-2017-channel-decoding]] arch claim softened to "1–3 hidden layers, up to ~128 units" (paper sweeps); "training on ~10% of codebook" softened to "small fraction (varies by N)"; [[q-learning]] FrozenLake "5000 episodes" softened to "few thousand episodes."
- **Reproduce-discipline fixes (3):** [[paper-ho-2020-ddpm]] Extend now gated on FID parity with GAN baseline first; [[paper-goodfellow-2014-gan]] Extend now gated on matching DCGAN-MNIST FID first; [[q-learning]] + [[ppo]] Practice TODOs now require CleanRL reference reproduction before any wireless port.
- **Minor cross-link adds (3):** [[link-adaptation]] → [[reinforcement-learning]] (SALAD is Bayesian-RL); [[umap]] → [[channel-charting]] (sibling manifold technique); [[reinforcement-learning]] wireless-applications now wiki-links [[link-adaptation]] + [[paper-wiesmayr-salad-2025]].
- **Audit-flagged Tier 4 candidates (deferred — explicitly unblock M7-M8-M10 deliverables):** (1) `[[sac]]` — continuous-control RL, the actual default for wireless deliverables; (2) `[[gae]]` — Generalized Advantage Estimation, currently buried inside [[actor-critic]]; (3) full pages for the existing stubs [[belief-propagation]] + [[mmwave-mimo]] (mark as "stubs — promote"); (4) `[[gnn]]` standalone (BP-as-GNN is the key NRX framing); (5) `[[onnx]]` (PyTorch → TensorRT bridge); (6) `[[bandit-regret]]` (Sutton-Barto Ch 2 + Jayden's existing AirComp [[regretful-learning]] connection); (7) `[[harq]]` (load-bearing for SALAD/OLLA).
- **Wiki coverage estimate after Tier-3 + this fix pass:** ~82% complete for the teacher agent to teach the [[python-ml-wireless]] roadmap end-to-end. Remaining 18% = the 7 Tier-4 candidates above + secondary papers in `raw/articles/ml-phy/README.md`.

## [2026-05-01] ingest | python-ml-wireless Tier-4 sweep — close M7-M8-M10 deliverable-unblocking gaps
- **Trigger.** Jayden approved Tier-4 in same session — final tier of post-lint planning.
- **5 atomic concept pages written** (the Tier-3 audit's M7-M8-M10 unblocking list, minus 2 candidates resolved in place: `gnn` already exists as [[graph-neural-network]]; `belief-propagation` + `mmwave-mimo` are already full pages from Tier-1):
  - [[sac]] — Soft Actor-Critic; **the off-policy continuous-action default for wireless RL** (most wireless papers since 2019). Comparison table SAC vs PPO vs DDPG vs DQN.
  - [[gae]] — Generalized Advantage Estimation; the variance-reduction trick that powers PPO/A2C/A3C; previously buried inside [[actor-critic]]'s Variants table — now a full atomic page.
  - [[onnx]] — Open Neural Network Exchange; the PyTorch → [[tensorrt]] bridge format; closes the deployment-chain pedagogical gap.
  - [[bandit-regret]] — Multi-armed bandits + regret theory; **the direct ancestor of [[regretful-learning]] AirComp** (single-agent special case). Cold-email lineage paragraph: Robbins 1952 → Lai-Robbins → UCB → Hart-Mas-Colell → AirComp 2026.
  - [[harq]] — Hybrid ARQ retransmission; load-bearing for [[link-adaptation]]; per-attempt BLER vs post-HARQ residual ($\tau^4$ upper bound) distinction explained.
- **Cross-link backfills (7 edits):** [[reinforcement-learning]] now wiki-links [[bandit-regret]], [[gae]], [[sac]] in the algorithm list (no more "TBD" notes); [[actor-critic]] Variants entry promoted GAE → wiki-link; [[ppo]] table + Related now wiki-link [[gae]] + [[sac]]; [[tensorrt]] Related now wiki-links [[onnx]]; [[regretful-learning]] (the AirComp anchor) now wiki-links [[bandit-regret]] as its single-agent special case; [[link-adaptation]] now wiki-links [[harq]] + [[bandit-regret]]; [[paper-wiesmayr-salad-2025]] Related now wiki-links [[harq]] + [[link-adaptation]].
- **Audit-driven fixes (3):** softened SAC vs TD3 mistake bullet to clarify both algorithms can layer features independently; qualified HARQ $\tau^4$ residual claim as "independent-attempts upper bound" (real chase-combining / IR makes it lower); dropped "(Tier-4 atomic page TBD)" from [[reinforcement-learning]].
- **Audit-flagged Tier 5 candidates (deferred — none block M7-M8 immediately, (a)+(b) load-bearing by M11, (c)–(e) by M13 cold-email window):** (a) **polar codes / Reed-Muller** depth beyond LDPC (5G NR control-channel reading); (b) **federated learning** (FedAvg / FedProx) for Phase 4 wireless-FL deliverables + Wi-Lab Morais V2V connection; (c) **diffusion model details** beyond the existing umbrella concept page; (d) **AODT internals** beyond the existing [[nvidia-aodt]] product page; (e) **digital-twin calibration loop specifics** (wraps [[paper-diff-rt-calibration-2024]] more deeply).
- **Wiki coverage estimate after Tier-4:** ~85–90% complete for the teacher agent to teach the [[python-ml-wireless]] roadmap end-to-end. Tier 1-4 covers RL (bandits → SAC), supervised DL, wireless-PHY, deployment chain (Sionna RT → ONNX → TensorRT → AODT), AirComp/regret track, all 12+ Phase-4 papers across NVIDIA + Wi-Lab clusters.
- Total Tier 4: **5 new wiki pages, 1 background audit agent, 7 cross-link backfills, 3 audit-driven content fixes.**

**Final cumulative across the 2026-05-01 session: 13 PDFs downloaded + 47 new wiki pages (13 papers + 17 concepts + 4 people + 13 textbooks) + 5 audit-agent passes + 1 web app (apps/teacher) + ~36 audit-driven edits across all tiers. Final broken-link count: ~55 (down from 73 at session start despite adding 47 pages).**

## [2026-05-01] ingest | python-ml-wireless Tier-5 sweep — channel coding + federated learning + DT calibration concept loop
- **Trigger.** Jayden approved Tier-5 in same session — closes the audit-flagged "load-bearing by M11" + "load-bearing by M13 cold-email window" concept gaps from Tier-4 audit.
- **4 atomic concept pages written:**
  - [[polar-codes]] — 5G NR control-channel code (PBCH/PDCCH/PUCCH); the **load-bearing partner of [[ldpc-codes]]**: data = LDPC, control = polar. SC / SCL / CRC-SCL decoder hierarchy. **Cammerer's PhD line ([[paper-gruber-2017-channel-decoding]]) starts here, not LDPC** — fluency mandatory before cold-email.
  - [[reed-muller-codes]] — polar's algebraic ancestor; Plotkin (u, u+v) construction; still alive in 5G NR PUCCH Format 0/1 for short ACK/NACK.
  - [[federated-learning]] — **the umbrella ML paradigm that [[system-pipeline]] (Jayden's AirComp project) literally implements as OTA-FL**. FedAvg / FedProx / OTA-FL family table, sync mechanism, channel inversion connection to [[truncated-channel-inversion]] / [[regretful-learning]]. The connective tissue between Jayden's existing research and the broader roadmap.
  - [[digital-twin-calibration]] — closed-loop concept wrapping [[paper-diff-rt-calibration-2024]] as a methodology (not just a paper summary). 4-axis trainable parameter taxonomy from [[paper-luo-dt-csi-feedback-2025]] (geometry / materials / RT params / hardware modeling). M10 capstone technical core; mandatory cold-email talking-point material.
- **Audit-driven content fixes (4):** corrected polar-codes "first family proven to achieve Shannon capacity" → "symmetric capacity of any B-DMC" (technically precise per Arıkan); replaced factually-wrong polar ASCII butterfly with Arıkan recursion equation $G_N = F^{\otimes n}$; added Cammerer 2017 *Scaling DL-based Decoding by Partitioning* reference to polar-codes; added McMahan 2017 FedAvg arxiv:1602.05629 reference to federated-learning.
- **Cross-link backfills (10 edits):** [[ldpc-codes]] now wiki-links [[polar-codes]] + [[reed-muller-codes]] (the data/control split partners); [[belief-propagation]] now references [[polar-codes]] (BP-on-polar variant); [[neural-decoder]] now references [[polar-codes]] (the actual code family Gruber 2017 uses); [[robust-signaling]] now references [[polar-codes]] as a control-plane FEC candidate; [[system-pipeline]] now references [[federated-learning]] as its umbrella ML paradigm; [[regretful-learning]] now references [[federated-learning]] (broader paradigm); [[paper-aircomp-survey]] now references [[federated-learning]]; [[wireless-digital-twin]] now references [[digital-twin-calibration]] + [[sionna-rt]] + [[nvidia-aodt]]; [[nvidia-aodt]] now references [[digital-twin-calibration]]; [[differentiable-ray-tracing]] now references [[digital-twin-calibration]] + [[paper-diff-rt-calibration-2024]] + [[cammerer]] + [[aitaoudia]]; [[paper-diff-rt-calibration-2024]] + [[paper-luo-dt-csi-feedback-2025]] now reference [[digital-twin-calibration]].
- **Audit-flagged Tier 6 candidates (deferred — auditor explicitly recommended Tier-6 should be practice sets + walkthroughs, not concept pages):** (1) **scaling-laws / neural-scaling** atomic page (M11 LWM context); (2) **OFDM-PHY basics** atomic page (subcarrier / CP / pilot grid — currently scattered across [[neural-receiver]] and paper summaries); (3) **gradient-clipping + mixed-precision training** PyTorch hygiene page; (4) **M7 neural-receiver reproduction walkthrough** — auditor flagged this as the **highest-value single artifact left to write**.
- **Wiki coverage estimate after Tier-5:** **~95% conceptually closed for M0 → M13** end-to-end teach-ability. Every milestone from Python setup (M0) through LWM extension (M11) has at least one concept page that defines its load-bearing terms, links to the canonical paper, and states the portfolio artifact. The wiki has **transitioned from "build the map" to "execute the plan"** — Tier 6+ should pivot from concept-page coverage to practice sets + walkthroughs.
- Total Tier 5: **4 new wiki pages, 1 background audit agent, 4 audit-driven content fixes, 10 cross-link backfills.**

**Final final cumulative across the 2026-05-01 session: 13 PDFs + 51 new wiki pages (13 papers + 21 concepts + 4 people + 13 textbooks) + 6 audit-agent passes + 1 web app + ~50 audit-driven edits.**

## [2026-05-01] walkthrough | python-ml-wireless Tier-6 — NRX M7 capstone walkthrough + 3 atomic pages + first practice set
- **Trigger.** Tier-5 audit explicitly recommended pivoting from concept-page coverage to practice + walkthroughs; named the M7 NRX reproduction walkthrough as **the highest-value single artifact left to write**.
- **1 walkthrough written:** [[nrx-reproduction-walkthrough]] — 6-stage NVIDIA-NRX-reproduction guide (read papers → env setup → clone repo + run demo → read training pipeline → reproduce headline BLER curve → write up → ranked extension targets). Includes hyperparameter targets, common-gotcha table, BCE-on-LLRs derivation in collapsible callout, "definition of done" rubric. **The single highest-leverage executable artifact for the NVIDIA cold email.**
- **3 atomic concept pages** (Tier-5 audit's small-but-load-bearing list):
  - [[scaling-laws]] — Kaplan + Chinchilla; predicts loss vs $(N, D, C)$ as power laws; M11 LWM extension cannot be done compute-optimally without it.
  - [[ofdm-phy-basics]] — subcarriers / CP / pilot grid / resource grid; the M2 OFDM-from-scratch deliverable foundation, also load-bearing for any NRX work.
  - [[mixed-precision-training]] — FP16 / BF16 / FP8; PyTorch AMP recipe; the M3 ResNet-18-with-AMP deliverable backbone.
- **1 practice set written:** [[belief-propagation-set-01]] — 5 mixed-difficulty problems (tiny LDPC by hand → BP-on-trees vs loopy → neural BP as GNN → NRX connections → weighted-BP PyTorch implementation challenge). Worked solutions in collapsible blocks; doubles as practice-set template.
- **Navigation updated.** [[python-ml-wireless]] course page got Tier-6 atomics + walkthroughs + practice subsections. `index.md` got Tier-6 atomics under concept lists + "Physical-Layer ML Roadmap" subsection under Walkthroughs (NRX walkthrough as first entry) + new subsection under Practice.
- **Tier-6 transition: from "build the map" to "execute the plan."** Per the audit, the wiki has shifted from concept-coverage mode to executable-artifact mode. Next-tier candidates: more practice sets (q-learning-set-01, polar-codes-set-01), Phase-2-M4 autoencoder-PHY reproduction walkthrough mirroring the NRX one.
- **Final broken-link count: 58.** Down from 73 at session start despite adding 56 new wiki pages — net 15 gaps closed, against an additional 41 net-new-page count.
- Total Tier 6: **5 new wiki pages (1 walkthrough + 3 concepts + 1 practice set), 0 background audits.**

**Final final final cumulative across the 2026-05-01 session: 13 PDFs + 56 new wiki pages (13 papers + 24 concepts + 1 walkthrough + 1 practice + 4 people + 13 textbooks) + 6 audit-agent passes + 1 web app (apps/teacher) + ~50 audit-driven edits. Final broken-link count: 58 (73 → 58). The wiki has transitioned from "build the map" to "execute the plan."**

## [2026-05-01] lint | Lyra-driven full-wiki audit + redundancy/goal-alignment fixes
- **Trigger.** Jayden invoked `@lyra` to audit the entire wiki for (a) redundancy and (b) goal-alignment vs the NVIDIA-Sionna-intern goal. Lyra returned a 10-action ranked plan; all 10 applied.
- **3 new concept pages written** (Lyra GAP-1 / GAP-2 / GAP-3+5):
  - [[5g-nr-pusch-structure]] — DM-RS Type 1/2 + Mapping A/B; TBS table + 38.214 spec anchor; HARQ timing ($K_1$/$K_2$/RV/NDI/HARQ-process-ID); 3GPP TR 38.211/212/214 split. **First-technical-screen probe coverage.**
  - [[quantization-aware-training]] — PTQ vs QAT; straight-through estimator; calibration-set composition; PyTorch QAT pattern + TensorRT INT8 export. Closes the "[[paper-nrx-wiesmayr-2024]] 0.5 dB recovery via QAT" gap.
  - [[sionna-api-cheatsheet]] — Sionna 2.x API surface in 12-line PUSCH end-to-end; 6 core objects table; 3 typical training-run shapes (NRX / autoencoder / Sionna RT); Keras Layer subclassing pattern; Sionna 0.x → 2.x breaking-change table. **The operational prep artifact for the M7 NRX reproduction.**
- **2 pages extended** (Lyra GAP-3 + GAP-8):
  - [[tensorrt]] gained a full INT8 calibration workflow section — `IInt8EntropyCalibrator2` Python pattern, calibrator-choice table, per-tensor vs per-channel granularity, `trtexec` verification step, fallback-to-QAT criterion.
  - [[nvidia-aodt]] gained an "Aerial SDK vs Sionna research stack" section distinguishing Sionna (research, TF/Keras) from Aerial SDK / cuBB (production, C++/CUDA, real-time) from AODT (digital-twin runtime); plus a "what an Aerial intern actually does" callout.
- **3 redundancy collapses** (Lyra R1 + R2 + R4):
  - [[neural-receiver]] portfolio-move section + [[paper-nrx-cammerer-2023]] portfolio block both collapsed to one-line pointers to [[nrx-reproduction-walkthrough]]. Eliminated ~30 lines of duplicate workflow descriptions.
  - [[policy-gradient]] Cartpole derivation stripped; replaced with pointer to [[reinforce]]; umbrella now only carries the theorem + variants table.
  - Stale "to be created" TODO lists in [[textbook-prince-understanding-deep-learning]] + [[textbook-sutton-barto-rl]] struck; pages now correctly listed as "Created in the 2026-05-01 sprint" with wiki-links.
- **Tangential-content de-emphasis** applied to `index.md`: priority callout in RL-atoms block ("PPO + SAC + GAE + policy-gradient are load-bearing; SARSA + bandit-regret are background"); annotated [[reed-muller-codes]] / [[umap]] / [[federated-learning]] / [[sarsa]] / [[bandit-regret]] / [[dqn]] with "(background reference)" or "(secondary for NVIDIA goal)" so attention isn't pulled during Phase 3 M7 crunch.
- **Course page restructure:** [[python-ml-wireless]] Industrial/deployment subsection now leads with the 3 new Lyra-driven pages followed by existing deployment chain. Index.md mirrors load-bearing-first ordering.
- Total Lyra fix pass: **3 new wiki pages + 2 page extensions + 3 redundancy collapses + 1 nav-restructure + 1 attention-budget annotation pass = 10 actions completed.**

**FINAL FINAL FINAL FINAL cumulative across the 2026-05-01 session: 13 PDFs + 59 new wiki pages (13 papers + 27 concepts + 1 walkthrough + 1 practice + 4 people + 13 textbooks) + 7 audit-agent passes (6 phy-ml-coach + 1 lyra) + 1 web app + ~60 audit-driven edits. Final broken-link count: 57 (73 → 57). The wiki is now ~95–98% conceptually closed for the NVIDIA-intern goal — every first-technical-screen probe area has a concept page; every reproduce-before-innovate workflow is documented; redundancy is collapsed; tangential content is de-emphasized rather than deleted.**

## [2026-05-01] lint | EC walkthroughs Canvas verification + frontmatter fix
- **Trigger.** Jayden asked me to "go through Canvas and create walkthroughs for the two EC labs due today." Pulled EEE 404 assignments via Canvas API; both EC labs are due **2026-05-02 06:59 UTC** (tomorrow morning), not today. Both walkthroughs already exist from the 2026-04-29 ingest: [[eee-404-ec-ml-walkthrough]] (XOR-XOR neural-network mod, ~10 EC pts, 429 lines) + [[eee-404-ec-quantum-walkthrough]] (QFT vs DFT in J-DSP, ~20 EC pts, 272 lines). Companion source summaries [[summary-eee-404-ec-ml-lab]] + [[summary-eee-404-ec-quantum-lab]] also already filed.
- **Frontmatter sweep applied.** Pre-2026-04-27 walkthroughs were filed under `wiki/examples/` and tagged `type: example`. After the 2026-04-27 reorganization moved them to `wiki/walkthroughs/`, the frontmatter was never updated. Sed-fixed `type: example` → `type: walkthrough` across 12 files: `eee-304-hw7-walkthrough`, `eee-304-lab-4-walkthrough`, `eee-335-final-walkthrough`, `eee-341-final-walkthrough`, `eee-341-lab-5-walkthrough`, `eee-350-hw7-walkthrough`, `eee-404-ec-ml-walkthrough`, `eee-404-ec-quantum-walkthrough`, `eee-404-exam-2-study-guide`, `eee-404-exam-2-walkthrough`, `eee-404-hw5-walkthrough`, `eee-404-lab-7-fill-in-walkthrough`. All 13 walkthroughs (12 fixed + the new [[nrx-reproduction-walkthrough]]) now correctly tagged `type: walkthrough` for Dataview queries.
- **No content changes** to either EC walkthrough — they were already comprehensive and ready to use.

## [2026-05-02] walkthrough | EEE 404 Project 2 — Applications of Fast Fourier Transform
- **Trigger.** Jayden asked me to ingest Project 2 from Canvas and write a walkthrough. Pulled via the Canvas API (course `241591`, assignment `6831782`, due **2026-05-04 06:59 UTC** — Monday morning). Worth 40 pts.
- **Files filed in `raw/labs/eee-404/`:** `project-2-lab-manual.pdf` (the spec), `project-2-overview-slides.pdf`, `project-2-code.zip` + unzipped tree (`audio_spectrum_analyzer/`, `vowel_analysis/`, `uart_receive_fft_plot_spectrum.m`, CMSIS), and `project-2-pages/` (six Canvas wiki pages — turned out to be MediaPlus video iframes only, no text content).
- **Source summary written:** [[lab-eee-404-project-2-fft-applications]] — TL;DR + concepts + worked-example callouts + open questions.
- **3 new concept pages:** [[autocorrelation-pitch-detection]] (Wiener–Khinchin pitch via $\mathrm{IFFT}(|\mathrm{FFT}|^2)$), [[formant]] (vocal-tract resonances vs glottal pitch), [[cmsis-dsp-fft]] (the `arm_rfft_fast_f32` API + the **packed output format** that's the most common bug source).
- **Walkthrough page:** [[eee-404-project-2-walkthrough]] — per-task structure, leading bold `**Answer:**` lines, callouts for setup/gotchas, collapsible derivations (windowing math, Hamming sidelobe cancellation, in-place buffer reasoning). Covers all 4 FILL_IN_BLANK lines, both function bodies (`max_index`, `apply_window`), the MATLAB workflow, and the deliverables checklist.
- **Course page updated:** [[eee-404]] — added Project 2 to "Sources filed", "Walkthroughs", and the FFT-module roadmap (entries 20-22). `updated:` bumped to 2026-05-02.
- **Index touched:** added EEE 404 concept entries and the Project 2 summary + walkthrough cross-references.

## [2026-05-04] setup | Schema update — "framework over formulas" pedagogical principle

- **CLAUDE.md:** added top-level "Framework over formulas" principle right after the learning-style note. Every concept page / walkthrough / source summary must now teach the small set of underlying patterns that generate all variant formulas, not 20 memorized cases.
- **Concept page template:** added a new `## Patterns / framework` section with a 3-part contract — list the 3–5 building blocks, sketch the derivation skeleton in 2–4 lines, and explicitly call out memorize-vs.-derive.
- **Walkthrough Op #4:** every numbered question must now name the framework (the 3–5 building blocks the question reduces to), include a `> [!tip] What to internalize vs. memorize` callout, and cross-link to other walkthrough questions / concept pages that share the same blocks.
- **[[eee-335-final-lecture-review]]:** added a top-level "Framework over formulas — read this before you start memorizing" section listing the 5 patterns that generate every formula in Units 4–6 (half-circuit analysis, three gain primitives, $R_\text{out}$ rules, the four definitions, "what changes if…" reflex), plus a unit→pattern table. Added a Unit-6-specific framework callout for the diff-amp variant explosion. `updated:` bumped to 2026-05-04, tag `framework-over-formulas` added.

## [2026-05-04] setup | Teacher agent — added Phase A "framework outline" before Socratic questioning

- **`.claude/agents/teacher.md`** — inserted new Section 2 "Framework outline before deep questioning" between retrieval-first (Section 1) and complexity gating (now Section 3). Locks in a two-phase teaching shape: (Phase A) outline the 3–5 generalized building blocks of the concept, names only, no formulas; (Phase B) Socratic drill with each question explicitly applying or combining one of the named blocks, with the block name in brackets at end of question. Includes a generalized-vs.-specific table, exit conditions for skipping Phase A (explicit override / Bloom 1–2 / no recurring pattern structure), and an instruction to reuse names from any wiki concept page's `## Patterns / framework` section.
- Renumbered subsequent sections (3 → 4 etc.) so numbering stays sequential.
- **Output format** rewritten to reflect the two-phase flow across Turn 1 (retrieval), Turn 2 (assessment + Phase A outline + first L1 question), Turn 3+ (Phase B drill loop), end-of-session.
- Frontends affected: `/teacher` slash command, `@agent-teacher` mentions, agent-dropdown selection in `wt`. No code changes — teacher persona only.

## [2026-05-04] setup | Teacher agent — added Phase C "closing recap" subsection

- **`.claude/agents/teacher.md`** — added Phase C subsection inside Section 2 (between Phase B and the "When to skip Phase A" exit rule). On session-close signals ("I'm good" / "got it" / successful L4 answer), the teacher now produces a structured artifact in this fixed order: `## ✅ Session recap` → `### Frameworks we used` (same 3-5 named blocks from Phase A) → `### Thinking process — how the blocks combined` (3-6 line story, not algebra) → `### Final equation` (single `$$...$$` display-math line so it renders + gets the copy/pin buttons in wt) → `### What to internalize vs. memorize`. Hard rules: reuse Phase A vocabulary, no new derivations, recap before productive-metrics check.
- **Output format** — promoted Phase C to step 11; productive metrics moved to 12; spaced-revisit + file updates to 13.
- No code changes; agent persona only. Takes effect on next chat (LLMSession re-reads system prompt on connect).

## [2026-05-05] setup | wiki/tutor-sessions/ folder + workflow added

- **New folder:** `wiki/tutor-sessions/` with the first daily file [[tutor-2026-05-05]] — one file per calendar day; every Q from Jayden (quick lookup or full teaching session) appends as a numbered Q-entry; Phase C closing recap from `.claude/agents/teacher.md` appends at the end of teaching sessions. Concept pages, [[mistakes/...]] logs, and [[practice/...]] sets are still updated as separate artifacts — the daily file links to them, does not duplicate them.
- **CLAUDE.md schema updates:**
  - Added `wiki/tutor-sessions/` to the directory tree.
  - Added a naming-convention bullet (`tutor-YYYY-MM-DD.md`) describing closing-recap behavior.
  - Added `tutor-session` to the frontmatter `type:` enum.
  - Added a "Tutor session daily file" page template covering Q-entries, the four required Phase C sections (Frameworks used / Thinking process / Final equation in display math / What to internalize vs. memorize), Mistakes flagged, Open questions, and Spaced revisit plan.
  - Modified Op #2 (Query) step 6 — every Q now logs to today's tutor-session file.
  - Added Op #6 (Tutor session) — explicit bookkeeping around the teacher persona's Phase A → B → C protocol; defers Socratic mechanics to `.claude/agents/teacher.md`.
  - Updated "five operations" → "six operations" and added `tutor` to the ops vocabulary.
- **`index.md`:** added "Tutor sessions" subsection (between Daily research Q&A and Workload planning).
- **`log.md`:** added `tutor` to the header ops list.
