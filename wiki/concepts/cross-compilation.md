---
title: Cross-Compilation
type: concept
course: [[research]]
tags: [toolchain, embedded, arm, gcc, build]
sources: [[daily-2026-04-23-sdr-toolchain-questions]]
created: 2026-04-24
updated: 2026-04-26
---

# Cross-Compilation

## In one line
Building binaries on one architecture (the *host*, usually x86-64 Linux or macOS) that will run on a different architecture (the *target*, for us the 32-bit ARM Cortex-A9 inside the Pluto SDR's Zynq-7010).

## Example first
On an Ubuntu laptop (x86-64), you want a "hello world" that will run on the Pluto's ARM CPU:

```bash
# Install the cross-toolchain
sudo apt install gcc-arm-linux-gnueabihf

# Compile for ARM from x86-64
arm-linux-gnueabihf-gcc hello.c -o hello_arm

# Verify the binary is ARM, not x86
file hello_arm
# ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), ...
```

Run `./hello_arm` on your laptop $\to$ "Exec format error" (it's not an x86 binary). Copy it to the Pluto (`scp hello_arm root@192.168.2.1:/tmp/`) and run it there $\to$ it works.

That's the whole idea: a separate *cross* compiler emits code for an architecture the host can't natively execute.

## Why we can't just compile on the Pluto
- The Pluto's ARM A9 running at $\sim 667$ MHz with $512$ MB RAM would take hours to compile anything nontrivial.
- It doesn't carry a full build environment in its stripped-down rootfs.
- Reproducibility — a laptop with a pinned toolchain version beats whatever accidentally-installed binaries the device has.

So we do the slow part (compile) off-device and ship only the binary.

## Anatomy of a cross-toolchain name

Example: `arm-linux-gnueabihf-gcc`

| Segment | Meaning |
|---|---|
| `arm` | Target CPU architecture — 32-bit ARM |
| `linux` | Target OS — expects a Linux kernel + glibc at runtime |
| `gnueabi` | ABI — GNU Embedded Application Binary Interface |
| `hf` | **Hard-float** — uses the hardware FPU (VFP) directly |

So `arm-linux-gnueabihf-gcc` compiles C for "32-bit ARM, Linux userspace, GNU ABI, hardware floating-point." The full toolchain adds matching `arm-linux-gnueabihf-{ld, as, objcopy, objdump, ...}`.

See [[gcc-arm-linux-gnueabihf]] for the Pluto-specific details.

## The four-ish ARM toolchain variants

| Toolchain | Target | Use case |
|---|---|---|
| `arm-linux-gnueabihf-*` | 32-bit ARM $+$ Linux $+$ hardware FP | **Pluto, most modern SDR SoCs** |
| `arm-linux-gnueabi-*` | 32-bit ARM $+$ Linux $+$ soft FP | Older or FPU-less ARM Linux boxes |
| `arm-none-eabi-*` | 32-bit ARM, **no OS** | Bare-metal / RTOS (STM32, nRF52, etc.) |
| `aarch64-linux-gnu-*` | 64-bit ARM $+$ Linux | Zynq UltraScale$+$, RPi 4 64-bit, Jetson |

Picking the wrong one is the most common install-time mistake. For Pluto $\to$ always `arm-linux-gnueabihf-`.

## The `CROSS_COMPILE=` idiom
Kernel / embedded Makefiles uniformly use:
```bash
make CROSS_COMPILE=arm-linux-gnueabihf- ARCH=arm
```
The Makefile prepends `$(CROSS_COMPILE)` to every tool name — `$(CROSS_COMPILE)gcc` becomes `arm-linux-gnueabihf-gcc`, etc. This is exactly what `plutosdr-fw`, Buildroot, PetaLinux, and the Linux kernel all expect. See [[pluto-build-toolchain]].

Our own ARM firmware in `aircomp-regret-pluto/firmware/Makefile` follows the same convention.

## Hard-float vs soft-float — why it matters
- **Hard-float** (`hf`) emits ARM VFP instructions (`vmul.f32`, `vadd.f64`, …) and passes floats in FPU registers. Fast.
- **Soft-float** emulates FP math in integer code. Slow ($\sim 10\times$ for heavy FP) but works without an FPU.

The Zynq-7010's Cortex-A9 has VFPv3, so we use hard-float. **Linking soft-float code into a hard-float binary (or vice versa) silently corrupts floating-point values** — the calling convention differs. Stay on one variant.

## What goes wrong in practice
- **Wrong prefix.** Using `arm-none-eabi-gcc` (bare-metal) on a Linux target $\to$ missing `libc` symbols at link time.
- **Host / target glibc mismatch.** Toolchain built against newer glibc than the target has $\to$ binaries crash on exotic symbols. Pin the toolchain to a version the Pluto's rootfs supports (GCC 11 is safe for stock Pluto v0.38).
- **Sysroot not set.** Linking against target-side libraries without `--sysroot=` $\to$ build picks up host headers, runs broken on target.
- **Missing `-marm` / `-mthumb` flag.** Some toolchains default to Thumb mode where ARM mode is expected. Specify explicitly if linker errors mention unknown relocations.

## Related
- [[gcc-arm-linux-gnueabihf]] — the specific toolchain we use for Pluto
- [[pluto-build-toolchain]] — the full Pluto build pipeline that depends on this
- [[wsl2-embedded-workflow]] — how to run cross-compilation from a Windows host
