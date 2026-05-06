---
title: Pluto Experiment Lifecycle — Flash Once, Run Many
type: concept
course:
  - "[[research]]"
tags: [research, pluto, deployment, aircomp, experiment, tdma, sync, jitter, pcxo]
sources:
  - "[[daily-2026-04-23-pluto-deployment-and-regret-learning]]"
created: 2026-04-24
updated: 2026-05-06
---

# Pluto Experiment Lifecycle

## In one line
Running the AirComp + regret-learning experiment on 5 Plutos is two separate phases — **flash once** with a bundled `pluto.frm` image, then **launch a binary per Pluto** that coordinates over the air — with USB never in the real-time path.

## Example first — one epoch of the experiment

With 1 ES and 4 EDs already flashed and powered on, you SSH into each and launch `aircomp_es` / `aircomp_ed`. From that point, the binaries coordinate **wirelessly**:

```
ES: beacon                                  ──RF──▶  EDs (stage 1 DL)
EDs: per-ED CSI ACKs in assigned TDMA slots ──RF──▶  ES    (stage 2)
ES: training trigger beacon                 ──RF──▶  EDs   (stage 3)
EDs: AirComp superposition TX (all 4 sim.)  ──RF──▶  ES    (stage 4)
ES: computes MSE, broadcasts feedback       ──RF──▶  EDs   (stages 5+6)
EDs: ACK feedback                           ──RF──▶  ES    (stage 7)
EDs: update regret tables → pick P for epoch t+1        (local)
```

Host laptop sits idle after launch. You can **unplug USB from all 5 Plutos** — the experiment keeps running fine. At the end, `scp` `/var/log/aircomp.log` off the ES and you have the run.

## The two phases

### Phase 1 — Provisioning (once per Pluto, or when the firmware/bitstream changes)

Build `pluto.frm` on the dev machine (WSL2 Ubuntu → Vivado + `arm-linux-gnueabihf-gcc` + `plutosdr-fw`; see [[pluto-build-toolchain]]). The image is **monolithic** and bundles:

```
pluto.frm  =  u-boot  +  Linux kernel  +  device tree  +  FPGA bitstream  +  rootfs (with /usr/bin/aircomp_es, /usr/bin/aircomp_ed)
```

Drag-and-drop the `.frm` onto the Pluto's USB mass-storage mount. On eject, the Pluto auto-reflashes (u-boot notices the new image on next boot). Repeat on all 5 units.

### Phase 2 — Experiment (every run)

```
1. Power on all 5 Plutos.
2. SSH into each  (ssh root@plutoN.local   or wired IP).
3. Launch the ES first:           ed-laptop$ ssh pluto-es   → aircomp_es --config /etc/aircomp/es.yaml
4. Launch each ED:                ed-laptop$ ssh plutoN    → aircomp_ed --aid N  (×4 terminals)
5. ES blocks until ≥1 ED ACK arrives, then the FSM starts cycling epochs.
6. Experiment ends when ES decides converged (or on Ctrl-C). Logs written to /var/log/aircomp.log.
7. scp /var/log/aircomp.log off the ES. Done.
```

Launch order matters: **ES first**. If an ED comes up before the ES is broadcasting beacons, it retries and waits.

## The key architectural win — USB is out of the real-time path

In a laptop-GNURadio-over-USB setup, the sample stream crosses USB every $30$–$60\,\mu\text{s}$, and USB scheduling jitter (hundreds of $\mu\text{s}$ on a congested bus) lands directly in your RF timing. That kills any coherent AirComp scheme.

In our setup:

```
AD9363  →  FPGA  →  AXI-DMA  →  DDR  →  ARM userspace (via mmap)
[────────── all on-chip, one clock domain ──────────]
```

USB is used for:

| Purpose | Timing-critical? |
|---|---|
| Initial flashing of `pluto.frm` | No — one-time, minutes |
| Optional SSH for observability | No — pull at any pace |
| Post-run `scp` of log files | No — after the fact |

**Litmus test.** After launching `aircomp_es` and `aircomp_ed`, unplug USB. Experiment completes. If you still need USB, something is wrong.

## Remaining jitter sources (honest caveats)

Dropping USB is necessary, not sufficient. Two jitter sources remain and must be accounted for:

1. **Linux scheduling jitter on the ARM.** The FSM runs in userspace, not on an RTOS. Worst-case hundreds of $\mu\text{s}$ on a vanilla scheduler. Mitigation: `chrt -f 80` (SCHED_FIFO, real-time priority) and core-pinning the FSM to core 1 (CPU isolation via `isolcpus=1` kernel cmdline). Typically knocks tail latency below $50\,\mu\text{s}$, which is fine at epoch rate.
2. **Inter-Pluto TCXO drift.** Each Pluto has its own $40$ MHz TCXO with tens of ppm of free-running drift. Over a $100$-ms epoch that's microseconds of time and large phase walk at $2.4$ GHz. Current mitigation: Golay-32 **per-frame resync** inside each epoch. Not enough for strict phase coherence; enough for magnitude-alignment AirComp. Deferred upgrade: **PTP (IEEE 1588)** over Ethernet or **GPS-PPS / Octoclock shared $10$ MHz reference** — see [[paper-experimental-ota-fl]] for the validated recipe.

**Important:** TCXO drift affects **raw AirComp SNR** (phase misalignment $\to$ degraded magnitude sum) but not the **algorithmic validity** of the regret-learning results. The game-theoretic convergence proof holds regardless — you just measure a noisier MSE.

## Common mistakes

- **Treating flashing and running as one thing.** They are separate phases with separate failure modes. "I can't SSH into the Pluto" is a provisioning problem; "my feedback packets are CRC-failing" is a run-time problem. Diagnose accordingly.
- **Forgetting to rename the 4 EDs to unique hostnames.** Stock Pluto firmware boots with hostname `pluto.local`; four of them on the same subnet mDNS-collide. Fix with `fw_setenv hostname plutoN` and reboot.
- **Launching EDs before the ES.** EDs will sit and burn CPU retrying. Start the ES first, confirm beacons on a spectrum analyzer, then launch EDs.
- **Assuming zero USB latency implies zero jitter.** Clock drift and scheduling jitter still exist — see above.

## Related
- [[zynq-ps-pl-split]] — what each half of the Pluto is doing during an epoch
- [[pluto-build-toolchain]] — how `pluto.frm` gets built in Phase 1
- [[system-pipeline]] — the 7-stage AirComp protocol running inside each epoch
- [[pre-flash-test-pyramid]] — how to de-risk a flash before paying the reflash cost
- [[paper-experimental-ota-fl]] — PTP + Octoclock sync recipe for the deferred fine-sync upgrade

## Sources / further reading
- `aircomp-regret-pluto/docs/build.md` and `docs/architecture.md`
- ADI Pluto wiki — https://wiki.analog.com/university/tools/pluto
