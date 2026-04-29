---
title: Pre-Flash Test Pyramid — De-risking Before a Pluto Reflash
type: concept
course: [[research]]
tags: [research, pluto, testing, dev-loop, pytest, vivado, wsl, cross-compile]
sources: [[daily-2026-04-23-pluto-deployment-and-regret-learning]]
created: 2026-04-24
updated: 2026-04-26
---

# Pre-Flash Test Pyramid

## In one line
A 6-layer testing hierarchy that catches bugs at increasing levels of realism, so you spend your reflash budget ($5$ Plutos $\times \sim 2$ min reflash + reconfigure per cycle) only on bugs that truly need the hardware in the loop.

## Example first — the cost of each layer, in seconds

Suppose you just changed one line in `firmware/ed/regret_learning.c`. How long to know whether it's broken?

| Layer | What it runs | Round trip |
|---|---|---|
| 1. Python algorithmic | `pytest python_reference/tests/` | ~5 s |
| 2. HDL simulation | `vivado -mode batch -source hdl/tb/run_all.tcl` | ~2–10 min |
| 3. C host compile + run | `wsl` → `gcc -o test_regret_standalone ... && ./test_regret_standalone` | ~3 s |
| 4. ARM cross-compile | `make CROSS_COMPILE=arm-linux-gnueabihf-` | ~10 s |
| 5. C + HDL co-simulation | Vivado XSim with DPI to the C model | ~5–15 min |
| 6. Hardware-in-loop on one Pluto | Flash → SSH → run | ~5–10 min per cycle, × 5 devices |

Running Layer 1+3 on every save catches $\sim 90\%$ of logic bugs at $\sim 10$ s per try. Running Layer 6 for a change that would have been caught in Layer 1 is $\sim 60\times$ slower — which, compounded across many edit-test cycles, is the difference between shipping a research demo in a week vs a month.

## The idea

Each layer **trades off realism for speed**. Bugs caught at a lower layer cost less; bugs that escape to hardware cost most. The pyramid is pedantic about writing tests at the lowest layer that can catch a given class of bug.

```
         ▲ more realistic, slower feedback
         │
     ┌───┴──────────────────────────────┐
  6  │  HIL on one Pluto (final sanity) │
  5  │  C + HDL co-simulation           │
  4  │  ARM cross-compile (linker OK?)  │
  3  │  C host compile + run (WSL gcc)  │
  2  │  HDL simulation (Vivado testbench)│
  1  │  Python algorithmic (pytest)     │
     └──────────────────────────────────┘
         │
         ▼ more abstract, faster feedback
```

## Per-layer purpose

### Layer 1 — Python algorithmic (`python_reference/tests/`)
Proves the algorithm is right in isolation from hardware. The canonical implementation lives in `python_reference/asset_spec/regret_matching.py`; tests run against that. Fast, deterministic, no toolchain dependencies beyond `numpy + pytest`. **Status in this project: ✓ green**, 17/17 tests pass.

### Layer 2 — HDL simulation (Vivado XSim + SV testbenches)
Proves the HDL modules implement their spec, with stimulus driven from golden vectors. Catches timing-closure-agnostic bugs — off-by-ones, state-machine stalls, wrong-endian AXI-Lite fields. **Status: ⧗ deferred** (ASU lab PC has no Vivado + no admin; home PC is the next milestone).

### Layer 3 — C host compile + run
Same C source, same algorithm, but compiled with host gcc and run natively on the dev machine. Proves the C port matches Python (ignoring PRNG differences: numpy Mersenne vs xorshift32 in the C). **Status: ✓ green** via WSL gcc 13.3.0 — `test_regret_standalone` converges on the same oracle action as the Python inspection script.

### Layer 4 — ARM cross-compile
`make CROSS_COMPILE=arm-linux-gnueabihf-` — same C, same headers, but with the ARM toolchain. Catches build-system bugs (missing soft-float flag, 32-bit / 64-bit type confusion, libc API differences) without yet needing a target. **Status: optional** until closer to flash — the source already compiles, and binary reaches target only in Layer 6.

### Layer 5 — C + HDL co-simulation
The C FSM driving the HDL testbench over a DPI / XSim bridge. Catches integration bugs (AXI-Lite register ordering, DMA descriptor layout, mmap offset mismatches) without committing a bitstream. Slow enough to not run on every save. **Status: optional**, mostly a pre-flight before a long HIL campaign.

### Layer 6 — Hardware-in-loop on one Pluto
Flash one device, run it against a benchtop signal generator or another Pluto, verify the RF waveform on a spectrum analyzer + CRC-clean packets arriving. The final truth — but the slowest, most brittle, and the one where asymmetric bugs (RF, clocks, thermal) finally appear. **Status: ⧗ final step**, gated on Layer 2 green.

## Why it matters / when you use it

Every edit-test cycle should bottom out at the **lowest layer that can catch the class of bug you suspect**:

- Just changed an equation in regret matching? Layer 1.
- Just changed an AXI-Lite register offset? Layer 5 (or 6 if you're brave).
- Just added a new `fprintf` for a log message? Layer 3.
- Touched the `config.h` for `N_POWER_LEVELS`? Layer 1 + Layer 3 (regenerate golden vectors, re-run C standalone).

The rule of thumb: **if a bug can be caught at layer N, do not reflash.** Reflash is layer 6; use it sparingly.

## Common mistakes

- **Skipping layer 1 and going straight to Layer 6.** You'll chase an RF ghost for two days when a 5-second pytest would have showed the bug. Don't.
- **Treating Python as "not real."** The `python_reference/asset_spec/` code is the **canonical spec**; C and HDL are ports of it. When they disagree, Python wins by definition — until someone re-ratifies the asset_spec.
- **No golden-vector cross-check between layers.** The layers must agree on the same inputs/outputs. `test_asset_golden.py` writes a JSON; `firmware/ed/tests/test_regret_vs_asset.c` reads it (TODO: finish the JSON parser stub). Bit-exact cross-check closes the loop.
- **Running all 6 layers on every save.** That defeats the point. Run the cheap ones on save; run the expensive ones on milestone commits.

## Related
- [[pluto-experiment-lifecycle]] — why reflash is expensive (what you're saving against)
- [[pluto-build-toolchain]] — the Vivado + gcc build machinery behind each layer
- [[wsl2-embedded-workflow]] — host setup for Layers 1, 3, 4 on a Windows dev machine
- [[regretful-learning]] — the algorithm the test suite validates
- [[hmc-psi-rebuild]] — the specific semantics the C and Python must agree on

## Sources / further reading
- `aircomp-regret-pluto/python_reference/tests/` — Layer 1 in the flesh
- `aircomp-regret-pluto/firmware/ed/tests/` — Layer 3 harness + Layer 3↔1 cross-check (in progress)
- `aircomp-regret-pluto/hdl/tb/` — Layer 2 testbenches
