---
title: "Research Questions"
date: 2026-04-23
tags: [research, embedded, sdr, toolchain, arm, cross-compilation]
aliases: ["2026-04-23 Research Questions"]
status: in-progress
last_updated: 2026-04-23
resume_at: "Q5 Step 5 — Install full Vivado 2022.2"
---

# 2026-04-23 Research Questions

Running log of questions and answers for ingestion into the Obsidian second brain.

> [!todo] ⏸️ Resume here next session
> **Target:** PlutoSDR custom HDL build on WSL2 Ubuntu ([[#Q5 Tailored walkthrough — WSL2 Ubuntu + custom FPGA/HDL goal|see Q5]])
>
> **Completed:**
> - [x] Step 1 — WSL2 GUI prep
> - [x] Step 2 — `.wslconfig` memory/CPU bump
> - [x] Step 3 — Base packages installed
> - [x] Step 4 — `gcc-arm-linux-gnueabihf` installed
>
> **Next up:**
> - [ ] **Step 5 — Install full Vivado 2022.2** ← you are here
> - [ ] Step 6 — WebPACK license
> - [ ] Step 7 — Clone `plutosdr-fw` + submodules
> - [ ] Step 8 — First HDL build
>
> **Notes:** Vivado install is a 2–3 hour wall-clock event (~30 GB download via web installer). Plan to start it before a long break. Download the `Xilinx_Unified_2022.2_*_Lin64.bin` from `account.amd.com` → Downloads archive.

---

## Q1: What is `gcc-arm-linux-gnueabihf` and how do I install it to build ARM firmware for my SDR?

### Definition

`gcc-arm-linux-gnueabihf` is a **cross-compiler toolchain** — it runs on an x86/x64 host machine but produces binaries that execute on 32-bit ARM processors running Linux. It is the standard toolchain for compiling user-space applications and firmware for ARM-based Linux SDR platforms.

### Name breakdown

| Segment | Meaning |
|---|---|
| `gcc` | GNU Compiler Collection — the compiler |
| `arm` | Target architecture: 32-bit ARM |
| `linux` | Target operating system: Linux (links against glibc, assumes kernel present) |
| `gnueabi` | GNU Embedded Application Binary Interface |
| `hf` | **Hard Float** — uses hardware FPU/VFP instructions directly |

**Hard float vs soft float:** Hard-float emits ARM VFP instructions and passes floating-point arguments in FPU registers. Soft-float emulates FP math in integer code. Hard-float is significantly faster but requires the target CPU to have a VFP unit. Most modern SDR SoCs (Zynq-7000, i.MX6, etc.) support it.

### Related but different toolchains

- `gcc-arm-none-eabi` — bare-metal ARM, **no OS**. Use this for microcontrollers or RTOS targets.
- `gcc-aarch64-linux-gnu` — 64-bit ARM (ARMv8/AArch64). Use for Zynq UltraScale+, Raspberry Pi 4 64-bit, etc.
- `gcc-arm-linux-gnueabi` (no `hf`) — soft-float variant. Rare on modern hardware.

### Installation

**Debian / Ubuntu:**
```bash
sudo apt update
sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf
```

**Fedora / RHEL:**
```bash
sudo dnf install gcc-arm-linux-gnu
```

**Arch Linux (AUR):**
```bash
yay -S arm-linux-gnueabihf-gcc
```

**macOS (Homebrew + ARM prebuilt):**
```bash
brew install arm-linux-gnueabihf-binutils
# GCC itself: download from https://developer.arm.com/downloads/-/gnu-a
```

**Verify:**
```bash
arm-linux-gnueabihf-gcc --version
```

### Usage patterns

Quick sanity check:
```bash
arm-linux-gnueabihf-gcc hello.c -o hello_arm
file hello_arm
# Expect: ELF 32-bit LSB executable, ARM, EABI5
```

CMake-based SDR projects:
```bash
cmake -DCMAKE_C_COMPILER=arm-linux-gnueabihf-gcc \
      -DCMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++ \
      ..
```

Makefile / kernel-style projects (the convention most SDR firmware uses):
```bash
make CROSS_COMPILE=arm-linux-gnueabihf- ARCH=arm
```

The `CROSS_COMPILE=` prefix is the idiomatic pattern — the Makefile prepends it to `gcc`, `ld`, `objcopy`, etc., yielding `arm-linux-gnueabihf-gcc`, `arm-linux-gnueabihf-ld`, and so on. PlutoSDR, Analog Devices' HDL, and many Xilinx/Zynq SDR build flows all expect this exact prefix.

### When to use (SDR context)

Use `gcc-arm-linux-gnueabihf` when:
- Target SDR runs **embedded Linux** on an ARM SoC
- Building user-space apps, kernel modules, or firmware that sits on top of Linux
- Examples: PlutoSDR (Zynq-7000), USRP E310/E312, LimeSDR-QPCIe with ARM host, BladeRF 2.0 micro host tools

Do **not** use when:
- Target runs bare-metal or an RTOS → use `gcc-arm-none-eabi`
- Target is 64-bit ARM → use `gcc-aarch64-linux-gnu`
- Target is the FPGA fabric itself → use Vivado/Quartus toolchain, not GCC

### Common gotchas

- Always check the project README for the exact expected prefix. Some vendors ship their own toolchain with a slightly different tuple (e.g., `arm-xilinx-linux-gnueabi-`).
- Mismatched glibc versions between host toolchain and target rootfs cause runtime failures. When in doubt, use the toolchain shipped by the SDR vendor's BSP.
- If linking against target-side libraries, set `--sysroot=` to point at a copy of the target root filesystem.

### Sources / further reading

- Debian package: https://packages.debian.org/stable/gcc-arm-linux-gnueabihf
- ARM GNU Toolchain downloads: https://developer.arm.com/downloads/-/gnu-a
- PlutoSDR build guide: https://wiki.analog.com/university/tools/pluto/building_the_image

---

## Q2: Can I do this on Windows?

Yes — three approaches, WSL2 is the clear winner for SDR work.

### Option 1 — WSL2 (recommended)

Windows Subsystem for Linux 2 runs a real Linux kernel on Windows. Use the standard `apt` workflow identical to native Ubuntu.

```powershell
# PowerShell as admin
wsl --install -d Ubuntu
```

Inside the Ubuntu shell:
```bash
sudo apt update
sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf build-essential cmake git
arm-linux-gnueabihf-gcc --version
```

**Pros:**
- Works with every SDR vendor build flow (PlutoSDR, PetaLinux, Yocto, ADI HDL) unmodified
- Windows files accessible at `/mnt/c/...`; WSL files accessible from Windows at `\\wsl$\Ubuntu\...`
- Supports POSIX shell scripts, autotools, Make — everything Linux-native build systems expect

**Cons / gotchas:**
- USB passthrough for flashing requires [`usbipd-win`](https://github.com/dorssel/usbipd-win); many users just flash from Windows after building the binary in WSL
- First-time setup consumes ~2–4 GB disk

### Option 2 — ARM prebuilt Windows toolchain

ARM publishes native Windows binaries at [developer.arm.com/downloads/-/gnu-a](https://developer.arm.com/downloads/-/gnu-a). Download the `arm-gnu-toolchain-*-mingw-w64-i686-arm-none-linux-gnueabihf.zip` variant (the "linux-gnueabihf" one, **not** "none-eabi"). Extract it and add `bin/` to `PATH`. You get `arm-none-linux-gnueabihf-gcc.exe` and friends.

**Works for:** single-file compilation, small CMake projects using plain Windows tools.

**Breaks on:**
- Autotools and most vendor BSP build scripts (expect POSIX shell)
- Anything that shells out with backticks, `$()`, or uses forward-slash paths throughout
- Most real SDR firmware build flows

### Option 3 — MSYS2 / Cygwin

MSYS2 gives you a POSIX-ish environment with pacman. However, its default ARM packages skew toward `arm-none-eabi` (bare-metal). You can install a Linux-targeted toolchain manually, but at that level of effort WSL2 is simpler and more robust.

### Decision matrix

| Use case | Best option |
|---|---|
| Full SDR firmware build (PlutoSDR, PetaLinux, etc.) | **WSL2** |
| Compile a single C file / small test | ARM prebuilt Windows toolchain |
| Corporate machine with WSL2 blocked | ARM prebuilt or MSYS2 |
| Bare-metal / RTOS target (not Linux) | ARM `none-eabi` prebuilt, any host |

### Recommendation

Install WSL2 with Ubuntu. Treat it as your Linux build machine. Keep source code under the WSL filesystem (not `/mnt/c/...`) for significantly faster I/O during builds. Edit with VS Code's Remote-WSL extension if you want a Windows-native editor UI.

### Sources

- WSL install docs: https://learn.microsoft.com/en-us/windows/wsl/install
- usbipd-win (USB passthrough): https://github.com/dorssel/usbipd-win
- ARM GNU Toolchain (Windows builds): https://developer.arm.com/downloads/-/gnu-a

---

## Q3: How do I access my Ubuntu shell?

Multiple entry points to WSL2's Ubuntu shell, pick whichever fits the workflow.

### Launch methods

| Method | How | Best for |
|---|---|---|
| Start Menu | Type "Ubuntu", Enter | Quick ad-hoc shell |
| Windows Terminal | Install from MS Store, `⌵` dropdown → Ubuntu | Daily driver — best UX |
| PowerShell / CMD | Run `wsl` (or `wsl -d Ubuntu`) | Scripting, quick one-shots |
| File Explorer | Address bar → type `wsl` → Enter | Open shell at current folder |
| VS Code | "WSL" extension → `WSL: Connect to WSL` | Coding / SDR dev work |

### First-time setup

On first launch Ubuntu finishes installing and prompts for a **UNIX username and password**. These are independent of the Windows account. The password is what `sudo` will ask for.

### Sanity checks inside the shell

```bash
whoami            # WSL username
pwd               # usually /home/<user>
uname -a          # Linux kernel info
lsb_release -a    # Ubuntu version
ls /mnt/c/Users/  # confirms Windows filesystem is mounted
```

### Verifying WSL state from PowerShell

```powershell
wsl -l -v         # list distros with version
wsl --set-version Ubuntu 2   # upgrade if stuck on v1
wsl --shutdown    # hard-stop all WSL VMs (useful when something hangs)
```

If nothing is listed at all, `wsl --install -d Ubuntu` didn't complete — rerun it and reboot.

### Recommended setup for SDR work

1. Install **Windows Terminal** (Microsoft Store) → set Ubuntu as default profile.
2. Install **VS Code** + the **WSL extension** (`ms-vscode-remote.remote-wsl`).
3. Keep source code in `~/` (the WSL filesystem) rather than `/mnt/c/...` — I/O is ~10× faster for builds.
4. Use `code .` from inside WSL to open the current directory in VS Code with the remote backend attached.

### Sources

- WSL basic commands: https://learn.microsoft.com/en-us/windows/wsl/basic-commands
- Windows Terminal: https://learn.microsoft.com/en-us/windows/terminal/
- VS Code WSL guide: https://code.visualstudio.com/docs/remote/wsl

---

## Q4: Walk-through — installing the PlutoSDR firmware prerequisites

Prerequisite list being satisfied:
- Vivado 2022.2+
- `gcc-arm-linux-gnueabihf` (11+) or Vitis-bundled cross-compiler
- PetaLinux 2022.2 (only for kernel/DT changes)
- Clone of `analogdevicesinc/plutosdr-fw` at a pinned tag
- Pluto firmware v0.34+ on the device (for device tree overlay support)

### Order matters

1. Host prep → 2. Vivado → 3. Cross-compiler → 4. PetaLinux (optional) → 5. Clone repo → 6. Verify device firmware.

Vivado first because its Vitis component ships an alternate cross-compiler that PetaLinux can fall back to.

### 1. Host prep (WSL2 Ubuntu or native Ubuntu 22.04/24.04)

Budget **~120 GB** free disk (Vivado ~80 GB, PetaLinux ~30 GB with sstate cache).

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential git wget curl ca-certificates \
    libtinfo5 libncurses5 libssl-dev libstdc++6 \
    lib32z1 lib32stdc++6 \
    python3 python3-pip flex bison gawk texinfo \
    unzip zip xterm autoconf libtool
```

`libtinfo5` + `libncurses5` are the ones that silently kill Vivado on modern Ubuntu. Install them now.

**WSL2 only:** Vivado GUI needs X. Windows 11 has WSLg built-in (automatic). Windows 10 needs VcXsrv + `export DISPLAY=:0` in `~/.bashrc`.

### 2. Vivado 2022.2

**License:** Xilinx WebPACK (free) covers XC7Z010 for basic use. Full FFT IP at larger sizes requires a paid license. Stock Pluto firmware rebuilds work fine with WebPACK.

**Download:**
1. Create AMD/Xilinx account at `account.amd.com`.
2. Go to AMD downloads archive → **Vivado 2022.2** (version-pinned — ADI scripts expect this).
3. Grab the **Linux Self Extracting Web Installer** (~300 MB; full offline installer is ~80 GB).

**Install:**
```bash
chmod +x Xilinx_Unified_2022.2_*_Lin64.bin
./Xilinx_Unified_2022.2_*_Lin64.bin
```

During GUI install:
- Product: **Vivado** (add Vitis only if you want its cross-compiler)
- Devices: at minimum **7 Series** (XC7Z010 Zynq-7000)
- Cable drivers: yes

Source env every new shell (or `~/.bashrc`):
```bash
source /tools/Xilinx/Vivado/2022.2/settings64.sh
vivado -version   # expect "Vivado v2022.2"
```

### 3. Cross-compiler

```bash
sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf
arm-linux-gnueabihf-gcc --version   # need 11+
```

- Ubuntu 22.04 → GCC 11 ✓
- Ubuntu 24.04 → GCC 13 ✓
- Older distros → use `ubuntu-toolchain-r/test` PPA, or the Vitis-bundled toolchain at `/tools/Xilinx/Vitis/2022.2/gnu/aarch32/lin/gcc-arm-linux-gnueabi/bin/`.

### 4. PetaLinux 2022.2 (skip unless modifying kernel/DT)

```bash
mkdir -p ~/petalinux/2022.2
chmod +x petalinux-v2022.2-*-installer.run
./petalinux-v2022.2-*-installer.run --dir ~/petalinux/2022.2
```

Source on demand:
```bash
source ~/petalinux/2022.2/settings.sh
petalinux-util --webtalk off
```

**Do not source PetaLinux and Vivado in the same shell** unless doing a full build — env variables collide. Use separate terminals.

### 5. Clone `plutosdr-fw`

```bash
mkdir -p ~/sdr && cd ~/sdr
git clone --recursive https://github.com/analogdevicesinc/plutosdr-fw.git
cd plutosdr-fw
git tag
git checkout v0.38     # or desired stable tag
git submodule update --init --recursive
```

Checkpoints:
- `--recursive` is mandatory — submodules include `hdl`, `linux`, `u-boot-xlnx`, `buildroot`.
- Use a **tag**, not `main`. Match tag to the firmware version you want running.

### 6. Verify device firmware version (≥ v0.34)

```bash
ssh root@192.168.2.1     # default pw: analog
cat /opt/VERSIONS
fw_printenv | grep firmware_version
```

Upgrade path if older: drop the latest `plutosdr-fw-v*.frm` from GitHub Releases onto the Pluto's USB mass-storage mount point → flashes + reboots automatically.

### Verification script (run in fresh shell before first build)

```bash
source /tools/Xilinx/Vivado/2022.2/settings64.sh
vivado -version                        # v2022.2
arm-linux-gnueabihf-gcc --version      # 11+
cd ~/sdr/plutosdr-fw && git describe   # your tag
```

First full `make` run: 1–3 hours, mostly Buildroot.

### Gotchas worth remembering

- **WSL2 virtual disk never shrinks.** After failed builds: `wsl --shutdown`, then Windows `diskpart` / `Optimize-VHD` to reclaim.
- **Never clone into `/mnt/c/...` from WSL.** NTFS is case-insensitive → Buildroot breaks with cryptic errors. Keep source in `~/sdr/`.
- **Vivado licensing errors on WebPACK:** check that `XILINXD_LICENSE_FILE` is NOT pointing at a nonexistent file. Unset it if needed.
- **Submodule fetch failures:** `cd` into the failing submodule path and retry `git pull` manually.
- **Vivado + PetaLinux env conflict:** separate terminals, always.

### Sources

- ADI plutosdr-fw build guide: https://wiki.analog.com/university/tools/pluto/building_the_image
- AMD/Xilinx downloads: https://www.xilinx.com/support/download.html
- PetaLinux 2022.2 release notes: https://docs.amd.com/r/2022.2-English/ug1144-petalinux-tools-reference-guide
- plutosdr-fw repo: https://github.com/analogdevicesinc/plutosdr-fw

---

## Q5: Tailored walkthrough — WSL2 Ubuntu + custom FPGA/HDL goal

Specialized path for the combination: **Windows host + WSL2 Ubuntu + custom HDL changes** on PlutoSDR.

### What's different for this specific combination

- Need **full Vivado** install (not minimal).
- **GUI matters** — block design, IP integrator, waveform viewer used constantly. WSL2 X server is the #1 pain point.
- **PetaLinux unnecessary** unless new IP requires driver/DT changes — can add later.
- **Disk I/O is critical** — project on WSL ext4 vs `/mnt/c/` NTFS is 5–10× build time difference.

### Step 1 — WSL2 GUI prep

**Windows 11:** WSLg is built-in. Verify:
```bash
echo $DISPLAY       # expect :0 or similar
sudo apt install x11-apps -y
xeyes               # GUI window confirms X works
```

**Windows 10:** Install [VcXsrv](https://sourceforge.net/projects/vcxsrv/).
- Launch XLaunch → Multiple windows → Start no client → **check "Disable access control"**
- Add to `~/.bashrc`:
  ```bash
  export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
  export LIBGL_ALWAYS_INDIRECT=1
  ```

### Step 2 — Expand WSL2 resources

Default WSL2 caps memory at 50% of Windows RAM. Vivado synthesis is RAM-hungry — bump it.

Create `C:\Users\<you>\.wslconfig` (Windows side):
```ini
[wsl2]
memory=16GB
processors=8
swap=8GB
localhostForwarding=true
```
Target ~75% of physical RAM. Apply:
```powershell
wsl --shutdown
```
Verify in Ubuntu: `free -h`, `nproc`.

### Step 3 — Base packages (includes GUI extras)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential git wget curl ca-certificates \
    libtinfo5 libncurses5 libssl-dev libstdc++6 \
    lib32z1 lib32stdc++6 \
    python3 python3-pip flex bison gawk texinfo \
    unzip zip xterm autoconf libtool \
    locales x11-apps dbus-x11
sudo locale-gen en_US.UTF-8
```
`dbus-x11` and `locales` are the ones that cause Vivado Tcl console to crash on launch if missing.

### Step 4 — Cross-compiler

```bash
sudo apt install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf
arm-linux-gnueabihf-gcc --version
```

### Step 5 — Install full Vivado 2022.2

> [!attention] 📍 **RESUME HERE** — last session ended before starting this step (2026-04-23)

1. AMD/Xilinx account at `account.amd.com`.
2. Download **Unified Installer 2022.2 — Linux Self Extracting Web Installer** (~300 MB).
3. Move to WSL ext4 — don't run from `/mnt/c/`:
   ```bash
   mkdir -p ~/Downloads && cd ~/Downloads
   cp /mnt/c/Users/<you>/Downloads/Xilinx_Unified_2022.2_*_Lin64.bin .
   chmod +x Xilinx_Unified_2022.2_*_Lin64.bin
   ./Xilinx_Unified_2022.2_*_Lin64.bin
   ```

GUI installer selections:
- Product: **Vivado ML Standard**
- Devices: **7 Series** (must include Zynq-7000 / XC7Z010)
- Include default IP packs (FFT, DDS, FIR, AXI)
- Install path: `/tools/Xilinx` (default) or `~/Xilinx`
- Cable drivers: yes

Lazy-source alias in `~/.bashrc`:
```bash
alias vivado-env='source /tools/Xilinx/Vivado/2022.2/settings64.sh'
```
Usage:
```bash
vivado-env
vivado &
```

### Step 6 — WebPACK license

1. Vivado GUI: **Help → Manage License → Load License → Connect Now**
2. Log in → request **Vivado Design Suite: ML Standard** (free).
3. Save received `.lic` to `~/.Xilinx/Xilinx.lic`.
4. **Load License → Copy License** → point at file.
5. **Backup this file** — gets wiped if WSL is reinstalled.

### Step 7 — Clone plutosdr-fw with HDL submodule

```bash
mkdir -p ~/sdr && cd ~/sdr
git clone --recursive https://github.com/analogdevicesinc/plutosdr-fw.git
cd plutosdr-fw
git tag | tail -10
git checkout v0.38
git submodule update --init --recursive
```

HDL project lives at:
```bash
cd ~/sdr/plutosdr-fw/hdl/projects/pluto
# system_bd.tcl, system_constr.xdc, system_top.v, Makefile
```

Build FPGA bitstream:
```bash
vivado-env
make     # Tcl → synth → impl → system_top.xsa (~30–45 min first run)
```

### Step 8 — Skip PetaLinux for now

plutosdr-fw top-level Makefile wraps prebuilt kernel + rootfs. Only install PetaLinux when custom IP needs driver/DT work.

### Typical HDL iteration loop

```bash
# 1. Edit HDL
cd ~/sdr/plutosdr-fw/hdl/projects/pluto
# modify system_bd.tcl / system_top.v / add IP

# 2. Rebuild bitstream
vivado-env && make

# 3. Rebuild top-level firmware image
cd ~/sdr/plutosdr-fw && make

# 4. Flash: drag build/pluto.frm onto Pluto's USB mass-storage mount
```

### WSL2 + HDL gotchas

- **Never store project on `/mnt/c/...`** — 5–10× slower for HDL builds (NTFS 9P vs ext4).
- **First Vivado GUI launch is slow** — WSLg spins up lazily, second launch is fast.
- **JTAG flashing** needs `usbipd-win` for USB passthrough; mass-storage drag-drop is simpler.
- **Out-of-disk mid-synth**: WSL VHD bloats. `wsl --shutdown` → `Optimize-VHD` in PowerShell.
- **License file backup** — `~/.Xilinx/Xilinx.lic` lost if WSL is reinstalled.
- **Vivado + PetaLinux env collision** — separate terminals (relevant later if adding PetaLinux).

### Verification script `~/sdr/check-env.sh`

```bash
#!/usr/bin/env bash
set -e
echo "=== Host ==="
uname -a; free -h | head -2; df -h ~ | tail -1
echo "=== Cross-compiler ==="
arm-linux-gnueabihf-gcc --version | head -1
echo "=== Vivado ==="
source /tools/Xilinx/Vivado/2022.2/settings64.sh
vivado -version | head -1
echo "=== Repo ==="
cd ~/sdr/plutosdr-fw && git describe
git submodule status | awk '{print "  "$2" "$3}'
echo "=== GUI ==="
[ -n "$DISPLAY" ] && echo "DISPLAY=$DISPLAY OK" || echo "DISPLAY not set"
echo "=== All checks passed ==="
```

### Sources

- WSLg docs: https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps
- `.wslconfig` reference: https://learn.microsoft.com/en-us/windows/wsl/wsl-config
- ADI HDL repo (plutosdr-fw submodule): https://github.com/analogdevicesinc/hdl
- Pluto HDL project docs: https://wiki.analog.com/university/tools/pluto/devs/fpga

---

<!-- Append future questions below this line using the same ## Q<N>: heading pattern -->
