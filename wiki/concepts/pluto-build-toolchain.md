---
title: Pluto Build Toolchain (Vivado + GCC + plutosdr-fw)
type: concept
course:
  - "[[research]]"
tags: [toolchain, pluto, vivado, petalinux, plutosdr-fw, build]
sources:
  - "[[daily-2026-04-23-sdr-toolchain-questions]]"
  - "[[daily-2026-04-23-pluto-deployment-and-regret-learning]]"
created: 2026-04-24
updated: 2026-05-06
---

# Pluto Build Toolchain

## In one line
To ship our custom HDL $+$ firmware onto the Pluto, we build three artifacts — FPGA bitstream (Vivado), ARM user-space binary (GCC cross-compiler), and optionally a kernel/DT update (PetaLinux) — and merge them into a single `pluto.frm` image via `analogdevicesinc/plutosdr-fw`.

## Example first — the three-artifact pipeline

```
  HDL (SystemVerilog)                C (firmware)
   in aircomp-regret-pluto/hdl/       in aircomp-regret-pluto/firmware/
          │                                   │
          ▼                                   ▼
     Vivado 2022.2             arm-linux-gnueabihf-gcc (11+)
     synth + impl                  cross-compile
          │                                   │
          ▼                                   ▼
     aircomp_core.bit              aircomp_ed, aircomp_es (ARM ELFs)
          │                                   │
          └───────────────┐     ┌─────────────┘
                          ▼     ▼
                 plutosdr-fw/ (analogdevicesinc)
                      top-level make
                          │
                          ▼
                     pluto.frm  ← flash onto Pluto
```

Three toolchains, one image. Each of the three artifacts lives in its own build system; `plutosdr-fw` stitches them.

## The four pieces you need installed

| Piece | Version | Purpose |
|---|---|---|
| **Vivado** | **2022.2** | HDL synthesis $+$ implementation $\to$ bitstream. Free WebPACK covers XC7Z010 for basic use. |
| **gcc-arm-linux-gnueabihf** | 11$+$ | Cross-compiles our C firmware. See [[gcc-arm-linux-gnueabihf]]. |
| **PetaLinux** | 2022.2 | **Only** needed if we change the kernel or device tree (new IP requires this). |
| **plutosdr-fw** | **tag v0.38** (or matching your device) | Top-level make target that merges all three into `pluto.frm`. |

**Pinning** matters — mismatched Vivado / PetaLinux / `plutosdr-fw` versions silently fail. ADI aligns their tags to Vivado versions.

## Order of installation

```
1. Host prep (Ubuntu 22.04 or WSL2 — see [[wsl2-embedded-workflow]])
2. Vivado 2022.2         <- heaviest (~80 GB full, ~30 GB downloaded via web installer)
3. Cross-compiler        <- seconds, via apt
4. PetaLinux 2022.2      <- optional (~30 GB)
5. Clone plutosdr-fw
6. Verify device firmware >= v0.34 on the Pluto
```

Vivado first because its Vitis component ships a fallback cross-compiler that PetaLinux can use if your distro's GCC is too old.

## Where each piece is used

| When we | We touch |
|---|---|
| Edit `aircomp-regret-pluto/hdl/**.sv` | Vivado (synth $+$ impl). $\sim 30$–$45$ min rebuild first time, incremental after. |
| Edit `aircomp-regret-pluto/firmware/**.c` | Cross-compiler (`make CROSS_COMPILE=arm-linux-gnueabihf-`). Seconds. |
| Change Linux device tree or kernel | PetaLinux. Rare. |
| Merge into final image | `plutosdr-fw` top-level `make`. $\sim 1$–$3$ hours first time (Buildroot), incremental after. |

See `aircomp-regret-pluto/docs/build.md` for exact commands.

## Disk + memory budget

| Item | Disk | RAM (peak during build) |
|---|---|---|
| Vivado | $\sim 80$ GB | $4$–$8$ GB for XC7Z010 synthesis |
| PetaLinux $+$ Buildroot sstate | $\sim 30$ GB | $2$–$4$ GB |
| plutosdr-fw build tree | $\sim 8$ GB | (uses above) |
| **Total** | **$\sim 120$ GB free recommended** | **$8$ GB RAM bare minimum, $16$ GB comfortable** |

On WSL2: raise the cap in `~/.wslconfig` (`memory=16GB`, `processors=8`). See [[wsl2-embedded-workflow]].

## License — Vivado WebPACK

Free. Covers XC7Z010 (the Pluto's Zynq device) for basic synthesis. Steps:

1. Create account at `account.amd.com`.
2. In Vivado: **Help $\to$ Manage License $\to$ Load License $\to$ Connect Now**.
3. Request **Vivado Design Suite: ML Standard** (free WebPACK tier).
4. Save the issued `.lic` to `~/.Xilinx/Xilinx.lic`.
5. **Back the file up.** A WSL reinstall wipes it; re-requesting is a pain.

**Caveat for our project:** the Xilinx FFT IP at $128$-pt (our numerology) is WebPACK-eligible. Larger FFT sizes need a paid license — but we don't use them ([[ofdm]] / system-pipeline's numerology 0).

## Source layout after clone

```
~/sdr/plutosdr-fw/
├── hdl/                 <- submodule: analogdevicesinc/hdl (Vivado projects + IP)
│   └── projects/pluto/  <- default Pluto HDL (we'll slot our IP in here)
├── linux/               <- submodule: Xilinx Linux kernel fork
├── u-boot-xlnx/         <- submodule: U-Boot bootloader
├── buildroot/           <- submodule: Buildroot-based rootfs
├── scripts/
└── Makefile             <- top-level: builds everything, produces pluto.frm
```

**Crucial:** clone with `--recursive` and pin a tag (`v0.38`), not `main`.

```bash
git clone --recursive https://github.com/analogdevicesinc/plutosdr-fw.git
cd plutosdr-fw
git checkout v0.38
git submodule update --init --recursive
```

## The HDL project for our custom IP

`aircomp-regret-pluto/hdl/scripts/build_project.tcl` wires our `aircomp_core.sv` block between `axi_ad9361` and `axi_dma` in the Pluto Vivado project. This is the one place our HDL tree couples into ADI's. Keep `hdl/projects/pluto/system_bd.tcl` override-compatible.

## Typical iteration loop

```bash
# 1. Edit HDL
cd aircomp-regret-pluto/hdl
# change e.g. sync_detector.sv

# 2. Rebuild bitstream
source /tools/Xilinx/Vivado/2022.2/settings64.sh
vivado -mode batch -source scripts/build_project.tcl   # 30-45 min first time

# 3. Rebuild firmware (if C changed too)
cd ../firmware
make CROSS_COMPILE=arm-linux-gnueabihf-

# 4. Merge into pluto.frm via plutosdr-fw
cd ~/sdr/plutosdr-fw
make

# 5. Flash: drag build/pluto.frm onto Pluto's USB mass-storage mount
```

**Before paying step 1–5, drop to the [[pre-flash-test-pyramid]].** Layer 1 (`pytest python_reference/tests/`) and Layer 3 (WSL gcc + `test_regret_standalone`) catch most bugs in seconds rather than waiting on a 30-minute bitstream rebuild $\times\,5$ Plutos.

## Flashing vs running are two distinct phases

The toolchain above produces `pluto.frm` — that's the **provisioning** artifact. You drop it on each Pluto once (drag-drop onto USB mass-storage, auto-reflashes on eject). After flashing, launching the experiment is a separate phase: SSH into each Pluto, `aircomp_es` on the edge server, `aircomp_ed` on each of the 4 EDs, and the 5 devices coordinate over the air — USB entirely out of the real-time path. See [[pluto-experiment-lifecycle]] for the runtime side.

## Common gotchas

- **Vivado + PetaLinux env collision.** Both `source` scripts stomp on each other. **Use separate terminals.**
- **Don't clone onto `/mnt/c/...` (WSL).** NTFS's case-insensitivity breaks Buildroot; 9P I/O is $5$–$10\times$ slower than ext4. Keep everything in `~/sdr/`.
- **Device firmware $<$ v0.34.** Device-tree overlay support is required. Upgrade first (drop `plutosdr-fw-v0.38.frm` onto the Pluto's USB mass-storage $\to$ auto-flashes).
- **Submodule fetch failures.** Don't retry the whole clone; `cd` into the failing submodule directory and retry `git pull` there.
- **`XILINXD_LICENSE_FILE` pointing at a stale path.** Unsets itself between installs. `unset XILINXD_LICENSE_FILE` if WebPACK license loads but Vivado claims "no license."
- **WSL2 VHD never shrinks.** After a failed build with $40$ GB of orphaned Buildroot output: `wsl --shutdown`, then PowerShell `Optimize-VHD -Path <path> -Mode Full` to reclaim.

## Where this lives in our repo

- Build instructions (short form): `aircomp-regret-pluto/docs/build.md`
- Architecture / HDL-ARM split: `aircomp-regret-pluto/docs/architecture.md`
- AXI-Lite register map: `aircomp-regret-pluto/docs/registers.md`

## Related
- [[cross-compilation]] — general concept
- [[gcc-arm-linux-gnueabihf]] — the ARM cross-compiler
- [[wsl2-embedded-workflow]] — Windows host setup
- [[zynq-ps-pl-split]] — what each of the two artifacts targets on the chip
- [[pluto-experiment-lifecycle]] — what happens after the flash (the experiment phase)
- [[pre-flash-test-pyramid]] — the 6-layer dev loop that gates on reflash
- [[system-pipeline]] — the 7-stage AirComp pipeline this toolchain builds
- [[signal-design-gaps]] — gap analysis that informs what the HDL implements

## Sources / further reading
- ADI `plutosdr-fw` build guide: https://wiki.analog.com/university/tools/pluto/building_the_image
- AMD/Xilinx downloads: https://www.xilinx.com/support/download.html
- PetaLinux 2022.2 reference: https://docs.amd.com/r/2022.2-English/ug1144-petalinux-tools-reference-guide
- Pluto HDL project docs: https://wiki.analog.com/university/tools/pluto/devs/fpga
