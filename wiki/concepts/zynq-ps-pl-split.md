---
title: Zynq-7010 PS/PL Split
type: concept
course:
  - "[[research]]"
tags: [research, pluto, zynq, fpga, arm, systemverilog, embedded, architecture]
sources:
  - "[[daily-2026-04-23-pluto-deployment-and-regret-learning]]"
created: 2026-04-24
updated: 2026-05-06
---

# Zynq-7010 PS/PL Split

## In one line
The Adalm Pluto's Xilinx Zynq XC7Z010 is one chip with two independently programmed halves — a dual-core ARM CPU (the **PS**, "Processing System") and an FPGA fabric (the **PL**, "Programmable Logic") — and you must think of them as two different machines that happen to share a die.

## Example first — where does each file in `aircomp-regret-pluto/` run?

Consider the two most important source files in the implementation tree:

```
aircomp-regret-pluto/
├── firmware/ed/regret_learning.c   ← runs on the PS (ARM)
└── hdl/rtl/ofdm_rx.sv               ← becomes hardware on the PL (FPGA)
```

- `regret_learning.c` cross-compiles to an **ARM ELF binary** via `arm-linux-gnueabihf-gcc`. That binary runs as a normal Linux process on the PS's dual-core Cortex-A9, under PetaLinux.
- `ofdm_rx.sv` is **synthesized** by Vivado into a **bitstream** (`*.bit`). That bitstream is loaded into the PL at boot and reprograms the fabric into a physical OFDM receiver circuit. **The `.sv` file itself is not executed** — there is no interpreter. It describes digital logic that becomes copper and silicon.

If you SSH into a Pluto and try to `run ofdm_rx.sv`, nothing happens — the Pluto has no Vivado, and an HDL file is not a program.

## The idea

A Zynq is a **System-on-Chip** that fuses a CPU and an FPGA with a high-bandwidth AXI interconnect. Each half has its own programming model:

| Half | Hardware | Programming model | Language | Artifact |
|---|---|---|---|---|
| **PS** — Processing System | dual-core ARM Cortex-A9 @ 667 MHz | sequential instruction execution, runs Linux | C (or anything gcc-targeted) | ARM ELF binary |
| **PL** — Programmable Logic | 28K logic cells, 80 DSP48E1, 60 BRAM36 | parallel hardware description | SystemVerilog / VHDL | `*.bit` bitstream |

**Why the split matters for our pipeline.** The design rule for [[system-pipeline]] is:

- **Sample-rate work $\to$ PL.** $1.92$ Msamples/s is way too fast to service from userspace Linux. Anything that runs once per ADC sample lives in hardware: Golay correlator for frame sync, 128-pt FFT/IFFT, CP add/remove, LS channel estimator, CRC-8 LFSR.
- **Epoch-rate work $\to$ PS.** Once per AirComp round (tens of ms) is well within ARM reach. The state machine, regret-matching math, PPDU pack/parse, radio config via libiio — all C on the ARM.

Cross these wires (e.g. a Python loop on the PS sampling every ADC word) and the design cannot meet timing. Cross them the other way (e.g. Hart-Mas-Colell regret matching in HDL) and you burn LUTs on float math that the A9 does for free.

## Formal definition

The Zynq-7000 family Technical Reference Manual (UG585) calls the ARM subsystem the **Processing System (PS)** and the FPGA fabric the **Programmable Logic (PL)**. They communicate over **AXI4** interfaces:

- **AXI-Lite** — low-bandwidth register access. PS writes/reads PL control registers here.
- **AXI-Stream** — high-bandwidth, flow-controlled data. Sample streams between AD9361 ↔ PL ↔ AXI-DMA flow here.
- **AXI4 (full, memory-mapped)** — used by AXI-DMA to DMA PL samples into DDR so the PS can mmap them.

Our custom IP slots onto these standard interfaces — see `aircomp-regret-pluto/docs/registers.md` for the exact AXI-Lite register map.

## Why it matters / when you use it

Every "how do I put this code on the Pluto?" question boils down to: **is this PS work or PL work?** Get that wrong and you spend a day debugging something that's a category error:

- "Why is my FFT missing samples?" — you put it on the PS; move it to the PL.
- "Why does my regret table get corrupted?" — you put it on the PL; move it to the PS.
- "Why can't I `gcc` this .sv file?" — you can't; SystemVerilog is synthesized, not compiled.

## Common mistakes

- **Treating the Pluto like a Raspberry Pi.** The Pi is CPU-only — SSH in, edit files, run them. The Pluto is an appliance: you cross-build **two** artifacts on a dev machine, merge them into `pluto.frm`, and re-flash. See [[pluto-experiment-lifecycle]] for the flashing-vs-running distinction.
- **"Copying the .sv files onto the Pluto."** There is no Vivado on the Pluto. Synthesis happens on your dev machine; only the bitstream reaches the device.
- **Putting sample-rate DSP on the ARM.** Linux scheduling alone will blow your latency budget. Even real-time priority can't beat a dedicated hardware datapath for 1.92 Msamples/s.
- **Putting epoch-rate control logic on the FPGA.** HMC regret matching needs float math, dynamic memory, and runs once per round — no reason to burn DSP48s on it.

## Related
- [[pluto-experiment-lifecycle]] — how the two halves run an experiment together
- [[pluto-build-toolchain]] — the three-artifact build pipeline (Vivado → bitstream, gcc → ARM binary, `plutosdr-fw` → `pluto.frm`)
- [[cross-compilation]] — why we build on a dev machine, not the target
- [[system-pipeline]] — the AirComp pipeline stages and which half each runs on
- [[wsl2-embedded-workflow]] — Windows host setup for the dev machine

## Sources / further reading
- Xilinx UG585 — Zynq-7000 SoC Technical Reference Manual
- ADI Pluto wiki — https://wiki.analog.com/university/tools/pluto
