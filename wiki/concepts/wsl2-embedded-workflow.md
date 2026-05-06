---
title: WSL2 for Embedded / SDR Development
type: concept
course:
  - "[[research]]"
tags: [toolchain, wsl2, windows, linux, embedded, vivado, antivirus]
sources:
  - "[[daily-2026-04-23-sdr-toolchain-questions]]"
  - "[[daily-2026-04-23-pluto-deployment-and-regret-learning]]"
created: 2026-04-24
updated: 2026-05-06
---

# WSL2 for Embedded / SDR Development

## In one line
WSL2 (Windows Subsystem for Linux 2) runs a full Linux kernel as a lightweight VM inside Windows 11, giving you native-speed Linux tooling for the Pluto build pipeline without leaving Windows.

## Example first
```powershell
# PowerShell as admin (one-time)
wsl --install -d Ubuntu
```

Reboot, launch "Ubuntu" from the Start menu, set a UNIX username + password, then inside the Ubuntu shell:
```bash
sudo apt update
sudo apt install gcc-arm-linux-gnueabihf build-essential git cmake
arm-linux-gnueabihf-gcc --version   # 11.4.0 OK
```

At this point the exact `apt`-driven build flow in the ADI Pluto wiki works unmodified. You're done with "setup" — now it's just Linux.

## Why WSL2 over the alternatives

| Option | Verdict |
|---|---|
| **WSL2** | Works with every SDR vendor's build flow unchanged. Best I/O, kernel-level POSIX. |
| Native Ubuntu dual-boot | Only marginally better. Overkill unless you want to live in Linux. |
| VirtualBox / VMware Ubuntu | Works but sluggish; USB passthrough is flakier than WSL2 $+$ `usbipd-win`. |
| ARM prebuilt Windows GCC | Compiles single files but breaks on autotools / vendor scripts / forward-slash paths. |
| MSYS2 / Cygwin | Default packages target bare-metal (`arm-none-eabi`), not Linux (`-gnueabihf`). |
| Docker Desktop | Works for container-based flows, but Vivado install inside is painful. |

For the [[pluto-build-toolchain]] — WSL2 is the clear answer.

## The four things to set up

### 1. Install WSL2 + Ubuntu
```powershell
wsl --install -d Ubuntu
# Reboot if prompted
wsl -l -v    # confirm: Ubuntu (Running), Version 2
```
If already on WSL1: `wsl --set-version Ubuntu 2`.

### 2. Raise resource caps (critical for Vivado)

Vivado synthesis is RAM-hungry. WSL2 defaults to $50\%$ of host RAM — bump it. Create `C:\Users\<you>\.wslconfig` (Windows-side):
```ini
[wsl2]
memory=16GB
processors=8
swap=8GB
localhostForwarding=true
```
Apply: `wsl --shutdown` in PowerShell. Verify inside Ubuntu: `free -h`, `nproc`.

Target $\sim 75\%$ of physical RAM. $8$ GB minimum for Vivado on a small XC7Z010 project; $16$ GB comfortable.

### 3. GUI (for Vivado's block-design views)

- **Windows 11:** WSLg is built in. Verify: `sudo apt install -y x11-apps && xeyes` $\to$ GUI window appears. Done.
- **Windows 10:** Install [VcXsrv](https://sourceforge.net/projects/vcxsrv/). Launch with "Disable access control" checked. Add to `~/.bashrc`:
  ```bash
  export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
  export LIBGL_ALWAYS_INDIRECT=1
  ```

### 4. VS Code + WSL extension (daily driver)

Install VS Code on Windows, add the **WSL** extension (`ms-vscode-remote.remote-wsl`). From inside Ubuntu: `code .` opens a VS Code window attached to the WSL backend. File edits, git, terminal — everything feels Windows-native but runs Linux-native.

## Filesystem rule — where the source lives

**Keep the project on the Linux ext4 filesystem** (`~/sdr/...`), **not** `/mnt/c/...` (Windows NTFS mounted at 9P).

| Filesystem | Build time (typical Vivado $+$ Buildroot) |
|---|---|
| Linux ext4 (`/home/<user>/sdr/`) | baseline (e.g. $45$ min) |
| `/mnt/c/...` (via 9P to NTFS) | **$5$–$10\times$ slower** (e.g. $3$–$8$ hours) |

The 9P protocol has per-file overhead — fine for a handful of documents, brutal for tens of thousands of source + object files. **Always clone into `~/`.**

## USB passthrough (optional)

To program the Pluto over USB directly from WSL2 you need [`usbipd-win`](https://github.com/dorssel/usbipd-win). Install on Windows, then:
```powershell
# List USB devices
usbipd list

# Share the Pluto's USB bus to WSL (replace BUSID)
usbipd bind --busid 2-3
usbipd attach --wsl --busid 2-3
```
Inside Ubuntu: `lsusb` $\to$ Pluto should appear.

**Easier alternative:** skip USB passthrough. After building `pluto.frm` inside WSL, open Windows Explorer, drag the file onto the Pluto's mass-storage mount. The Pluto re-flashes on eject. Works fine for our iteration loop.

## Accessing files across the WSL $\leftrightarrow$ Windows boundary

```bash
# From WSL, access Windows files
cd /mnt/c/Users/jayden/Downloads
```
```powershell
# From Windows, access WSL files (File Explorer or PowerShell)
\\wsl$\Ubuntu\home\jayden\sdr
```

Use this to move installers (Vivado web installer downloaded in Windows $\to$ copy into `~/Downloads` in WSL before running).

## Common gotchas

- **VHD never shrinks.** After building $+$ deleting a $40$-GB Buildroot tree, the WSL2 disk file stays at $40$ GB. Reclaim: `wsl --shutdown`, then PowerShell `Optimize-VHD -Path <path-to-ext4.vhdx> -Mode Full`.
- **WSLg flaky on Windows 10.** If `xeyes` doesn't render, you're on Win 10 $\to$ install VcXsrv (see step 3 above).
- **First Vivado GUI launch takes $30$–$90$ s.** WSLg spins up lazily. Subsequent launches are fast.
- **Locale / dbus errors in Vivado Tcl console.** Install `locales dbus-x11`, run `sudo locale-gen en_US.UTF-8`. (Included in the install list in [[pluto-build-toolchain]].)
- **Cloned the repo under `/mnt/c/`.** Move it to `~/sdr/` immediately — build times and error rates drop dramatically.
- **License file lost on WSL reinstall.** Back up `~/.Xilinx/Xilinx.lic` to Windows side or cloud.

## Escape hatch — when Windows AV blocks unsigned compilers

On the ASU lab PC (and any managed endpoint with aggressive EDR), **MSYS2's `gcc.exe` launches fine, but the backend `cc1.exe` is silently killed the moment it spawns** — no error message, no quarantine popup, just `cc1` exits immediately. Root cause: endpoint security blocks unsigned binaries from executing. Ships a broken compiler that produces zero output.

WSL2 is the clean workaround — Linux kernel isolation means Windows AV can't inspect WSL subprocess execution. Ubuntu 24.04 + gcc 13.3.0 runs unimpeded, Windows drives mount at `/mnt/c/`, and the [[pre-flash-test-pyramid]] Layer 3 (C host compile + run) works the same as on a personal machine. Alternative if WSL is unavailable: GitHub Codespaces ($\sim 60$ free hours/month per user) or a Remote-SSH session to a home PC.

Note: VS Code is not itself a compiler; it invokes whatever external toolchain you configure. If the configured toolchain is blocked by AV, switching editors won't help.

## Verification script

Drop this at `~/sdr/check-env.sh`:
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
echo "=== GUI ==="
[ -n "$DISPLAY" ] && echo "DISPLAY=$DISPLAY OK" || echo "DISPLAY not set"
```
Run before every build session — catches $\sim 90\%$ of environment drift.

## Sources / further reading
- WSL install docs: https://learn.microsoft.com/en-us/windows/wsl/install
- `.wslconfig` reference: https://learn.microsoft.com/en-us/windows/wsl/wsl-config
- WSLg (GUI): https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps
- VS Code WSL: https://code.visualstudio.com/docs/remote/wsl
- `usbipd-win`: https://github.com/dorssel/usbipd-win

## Related
- [[cross-compilation]]
- [[gcc-arm-linux-gnueabihf]]
- [[pluto-build-toolchain]] — the overall Pluto build pipeline WSL2 supports
