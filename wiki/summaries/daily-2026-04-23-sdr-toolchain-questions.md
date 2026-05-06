---
title: Daily Research Questions — SDR Toolchain (2026-04-23)
type: summary
source_type: daily
source_path: raw/daily/2026-04-23_Research_Questions.md
source_date: 2026-04-23
course:
  - "[[research]]"
tags: [research, embedded, sdr, toolchain, arm, cross-compilation, wsl2, vivado, in-progress]
created: 2026-04-24
updated: 2026-05-06
status: in-progress
resume_at: "Q5 Step 5 — Install full Vivado 2022.2"
---

# Daily Research Questions — SDR Toolchain (2026-04-23)

> [!todo] ⏸️ **RESUME HERE next session**
> **Target:** custom HDL build for Pluto on WSL2 Ubuntu — [[pluto-build-toolchain]]
>
> **Completed (from raw log):**
> - [x] Step 1 — WSL2 GUI prep (Windows 11 → WSLg confirmed)
> - [x] Step 2 — `.wslconfig` memory/CPU bump
> - [x] Step 3 — Base packages installed
> - [x] Step 4 — `gcc-arm-linux-gnueabihf` installed (see [[gcc-arm-linux-gnueabihf]])
>
> **Next up:**
> - [ ] **Step 5 — Install full Vivado 2022.2** ← you are here
> - [ ] Step 6 — WebPACK license
> - [ ] Step 7 — Clone `plutosdr-fw` + submodules
> - [ ] Step 8 — First HDL build
>
> **Note on Vivado install:** 2–3 hour wall-clock event; ~30 GB download via web installer. Plan to start before a long break. Fetch `Xilinx_Unified_2022.2_*_Lin64.bin` from `account.amd.com → Downloads archive`.

## TL;DR
Yesterday's Q&A covered the full Pluto build toolchain: what `gcc-arm-linux-gnueabihf` is and how to install it, whether it works on Windows (yes, via WSL2), how to use WSL2 Ubuntu, and a tailored walkthrough for building custom Pluto FPGA/HDL images. Four of eight walkthrough steps are done; Vivado install is next.

## Key takeaways

- **WSL2 is the right host for Pluto work.** Every SDR vendor's build flow expects a Linux environment; trying to hack around that with native-Windows GCC builds eventually hits autotools / POSIX-shell scripts. WSL2 sidesteps all of that with ~zero performance cost — provided sources live on ext4, not on `/mnt/c/`.
- **Three toolchains, one image.** The Pluto deliverable (`pluto.frm`) merges (1) Vivado-produced FPGA bitstream, (2) cross-compiled ARM userspace binary, (3) optional PetaLinux kernel/DT change. `plutosdr-fw` is the top-level glue.
- **`gcc-arm-linux-gnueabihf` is the canonical cross-compiler** for 32-bit ARM + Linux + hardware float (Cortex-A9 in the Zynq-7010). Not to be confused with `arm-none-eabi` (bare-metal, wrong for Pluto) or `aarch64-linux-gnu` (64-bit ARM, also wrong).
- **Vivado WebPACK is free** and covers XC7Z010 + the 128-pt Xilinx FFT IP we need. Heavy install (~30 GB web / 80 GB full), license via `account.amd.com`. Back up `~/.Xilinx/Xilinx.lic`.
- **The `CROSS_COMPILE=` Makefile idiom** (`make CROSS_COMPILE=arm-linux-gnueabihf- ARCH=arm`) is how every embedded Linux build flow hands the cross-toolchain to sub-builds — including our `aircomp-regret-pluto/firmware/Makefile`.

## Concepts introduced (new pages)
- [[cross-compilation]] — the general concept of host-on-x86, target-on-ARM builds
- [[gcc-arm-linux-gnueabihf]] — the specific toolchain, its naming conventions, install cheat sheet
- [[pluto-build-toolchain]] — the full Pluto build pipeline: Vivado + GCC + PetaLinux + `plutosdr-fw`
- [[wsl2-embedded-workflow]] — Windows host setup: `.wslconfig`, GUI, VS Code, USB passthrough, ext4-vs-NTFS performance

## Reinforced / cross-linked
- [[system-pipeline]] — the 7-stage AirComp pipeline this toolchain exists to build
- [[signal-design-gaps]] — the gap analysis that informs which HDL blocks we need
- `aircomp-regret-pluto/docs/build.md` — the project's short-form build doc (now cross-linked from the toolchain pages)

## Worked content kept in `raw/`, not duplicated in wiki

The `raw/daily/2026-04-23_Research_Questions.md` file contains complete step-by-step install commands, GUI installer selections, license-request URLs, and the verification script. This summary captures the **concepts**; the raw file carries the **procedure**. When actually running through Step 5 (Vivado install), open the raw file — see:
- `raw/daily/2026-04-23_Research_Questions.md` → Q5 Step 5 (Vivado 2022.2 install)
- `raw/daily/2026-04-23_Research_Questions.md` → Q5 Step 6 (WebPACK license)
- `raw/daily/2026-04-23_Research_Questions.md` → Q5 Step 7 (`plutosdr-fw` clone)
- `raw/daily/2026-04-23_Research_Questions.md` → Q5 verification script

The concept pages above distill the *why* and the *what to remember*; the raw file is the runbook.

## Open questions flagged
- **USB passthrough: `usbipd-win` or drag-drop flashing?** The raw file lists both. Drag-drop is simpler; `usbipd-win` is needed only if we ever need JTAG. For now, drag-drop is the default.
- **Vivado vs Vitis-bundled cross-compiler?** The raw file notes Vitis ships an alternate `arm-linux-gnueabi-` toolchain at `/tools/Xilinx/Vitis/2022.2/gnu/aarch32/lin/gcc-arm-linux-gnueabi/bin/`. We default to apt's `gcc-arm-linux-gnueabihf` (hard-float) — which matches Pluto — but Vitis's toolchain is a fallback if apt's is too old.
- **PetaLinux: skip until needed.** Not required for our current HDL-only iteration. Becomes necessary when we add a new UIO device node or kernel driver. Documented in [[pluto-build-toolchain]] § "order of installation."

## Related
- [[system-pipeline]] — what the toolchain is building
- [[signal-design-gaps]] — gap analysis that informs HDL block choices
- CLAUDE.md → "Implementation agent — 6G researcher persona" → hardware constraints + FPGA/ARM split
- `aircomp-regret-pluto/docs/build.md` — project's short-form build doc

## Sources
- `raw/daily/2026-04-23_Research_Questions.md` — the full Q&A log (Q1–Q5)
- ADI Pluto build guide: https://wiki.analog.com/university/tools/pluto/building_the_image
- `plutosdr-fw` repo: https://github.com/analogdevicesinc/plutosdr-fw
