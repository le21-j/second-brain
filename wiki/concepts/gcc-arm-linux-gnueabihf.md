---
title: gcc-arm-linux-gnueabihf (Pluto Cross-Compiler)
type: concept
course:
  - "[[research]]"
tags: [toolchain, gcc, arm, pluto, embedded]
sources:
  - "[[daily-2026-04-23-sdr-toolchain-questions]]"
created: 2026-04-24
updated: 2026-05-06
---

# gcc-arm-linux-gnueabihf

## In one line
The **canonical cross-compiler** for building user-space ARM-Linux binaries — runs on x86-64, emits code for the 32-bit ARM Cortex-A9 in the Pluto SDR's Zynq-7010.

## Example first
```bash
# Install on Ubuntu / Debian / WSL2
sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf

# Verify
arm-linux-gnueabihf-gcc --version
# gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

# Compile a test program
arm-linux-gnueabihf-gcc hello.c -o hello_arm
file hello_arm
# ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), ...

# Scp to Pluto and run
scp hello_arm root@192.168.2.1:/tmp/
ssh root@192.168.2.1 /tmp/hello_arm
# Hello from ARM
```

Same C source, different binary — and the ARM binary simply does not execute on x86-64 (`./hello_arm` $\to$ "cannot execute binary file: Exec format error"). That's the proof it worked.

## Name breakdown

| Segment | Meaning |
|---|---|
| `gcc` | The GNU compiler |
| `arm` | Target: 32-bit ARM |
| `linux` | Target OS: Linux (expects glibc + kernel) |
| `gnueabi` | GNU Embedded ABI |
| `hf` | **Hard-float** — FPU used directly |

See [[cross-compilation]] for the general idea; this page is about the specific Pluto-compatible variant.

## When to use (and when not to)

Use `arm-linux-gnueabihf-*` for:
- Pluto SDR user-space firmware (our `aircomp-regret-pluto/firmware/`)
- PlutoSDR `plutosdr-fw` build tree
- USRP E310 / E312 (also Zynq-7000 class)
- Any ARMv7-A Linux target with VFP

**Don't** use it for:
- Microcontrollers (STM32, nRF52, etc.) $\to$ use `gcc-arm-none-eabi` instead
- 64-bit ARM SoCs (Zynq UltraScale$+$, RPi 4 64-bit) $\to$ use `gcc-aarch64-linux-gnu`
- FPGA fabric itself $\to$ that's Vivado's job, see [[pluto-build-toolchain]]

## Version required for Pluto

Stock Pluto v0.38 firmware was built against **GCC 11**. GCC 13 (Ubuntu 24.04) works fine. Pre-11 → some newer libstdc++ features aren't available; older firmware sometimes needs GCC 8 / 9.

| Distro | Default GCC version |
|---|---|
| Ubuntu 22.04 | 11 |
| Ubuntu 24.04 | 13 |
| Debian 12 | 12 |
| Older | Use `ubuntu-toolchain-r/test` PPA or the Vitis-bundled toolchain at `/tools/Xilinx/Vitis/2022.2/gnu/aarch32/lin/gcc-arm-linux-gnueabi/bin/` |

## Usage patterns

**Single-file:**
```bash
arm-linux-gnueabihf-gcc foo.c -o foo_arm
```

**With CMake (firmware projects):**
```bash
cmake -DCMAKE_C_COMPILER=arm-linux-gnueabihf-gcc \
      -DCMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++ \
      ..
```

**With Make / kernel / `plutosdr-fw` (the idiomatic pattern):**
```bash
make CROSS_COMPILE=arm-linux-gnueabihf- ARCH=arm
```
Makefile prepends the prefix to every tool name.

**Our project** — see `aircomp-regret-pluto/firmware/Makefile`:
```bash
make CROSS_COMPILE=arm-linux-gnueabihf- TARGET=ed   # edge device
make CROSS_COMPILE=arm-linux-gnueabihf- TARGET=es   # edge server
```

## Linking against target-side libraries

The Pluto ships `libiio.so.0` on the device. To link against it at build time you need the Pluto's headers + a stub library. Simplest approach: clone `analogdevicesinc/libiio`, build it for ARM with the same cross-compiler, and point `-I`/`-L` at the build output. Or use `--sysroot=` to pin against a copy of the Pluto's rootfs.

## Installation cheat sheet

```bash
# Debian / Ubuntu / WSL2 Ubuntu
sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf

# Fedora / RHEL
sudo dnf install gcc-arm-linux-gnu

# Arch (AUR)
yay -S arm-linux-gnueabihf-gcc

# macOS (Homebrew — binutils only; download GCC from developer.arm.com)
brew install arm-linux-gnueabihf-binutils

# Windows native — easiest via WSL2, see [[wsl2-embedded-workflow]]
```

## Common gotchas
- **`arm-none-eabi-gcc` vs `arm-linux-gnueabihf-gcc`.** None-eabi is bare-metal (microcontrollers); never use it for Pluto.
- **Hard-float / soft-float ABI mismatch.** Mixing hf and non-hf object files silently corrupts FP args. Stay on hf for Pluto.
- **Vendor prefix drift.** Some BSPs ship `arm-xilinx-linux-gnueabi-`. Check the project's README — it usually hardcodes the expected prefix.
- **glibc mismatch.** If a binary links but crashes on the Pluto with `GLIBC_2.xx not found`, your toolchain was built against a newer glibc than the Pluto's rootfs carries.

## Sources / further reading
- Debian package: https://packages.debian.org/stable/gcc-arm-linux-gnueabihf
- ARM GNU Toolchain downloads: https://developer.arm.com/downloads/-/gnu-a
- Pluto build guide: https://wiki.analog.com/university/tools/pluto/building_the_image

## Related
- [[cross-compilation]] — the general concept
- [[pluto-build-toolchain]] — the full Pluto build pipeline
- [[wsl2-embedded-workflow]] — Windows host setup
