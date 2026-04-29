---
title: Time-Division Multiplexing (TDM)
type: concept
course: [[eee-304]]
tags: [eee-304, communication, multiplexing, tdm, pam, sampling]
sources: [[homework-2026-04-26-eee-304-hw7]]
created: 2026-04-26
updated: 2026-04-26
---

# Time-Division Multiplexing (TDM)

## In one line
TDM lets $N$ independent signals share a single wire by **interleaving their samples in time** — each signal gets its own narrow time slot inside a repeating frame, and a sync slot tells the receiver where the frame boundary is.

## Example first

**HW7 problem 2:** $20$ audio signals, each bandlimited to $20$ kHz, multiplexed via PAM. What is the minimum PAM pulse rate?

Step-by-step:
- Each audio signal must be sampled at $f_s \geq 2B = 40$ kHz (Nyquist for $20$ kHz bandwidth).
- That means **one sample every $25\,\mu$s** per channel.
- In that $25\,\mu$s window, we must fit $20$ channel slots $+$ $1$ sync slot $= 21$ slots.
- Slot duration: $25\,\mu\text{s} / 21 \approx 1.19\,\mu\text{s}$.
- Pulse rate: $1 / 1.19\,\mu\text{s} \approx 840$ kHz.

==**Minimum PAM frequency:** $840$ kHz.==

The wire now carries $840{,}000$ pulses per second — but each individual audio channel is still sampled at exactly $40$ kHz, just spread across the 21-slot frame.

## The idea

A single wire has only one signal value at any instant. But if your signal of interest occupies only a small fraction of the time (because samples are short pulses), the wire is **idle** the rest of the time. TDM exploits that idle time by **slotting** other signals into it.

```
Frame layout (21 slots per frame, frame period = 25 μs):

|sync| ch1| ch2| ch3| ... |ch20|sync| ch1| ch2| ...
 ◄──── frame N (25 μs) ───► ◄──── frame N+1 ────►
```

Each channel only sees its own slot. The receiver uses the sync slot to align frame boundaries, then de-interleaves: samples landing in slot $k$ go to channel $k$.

> [!tip] **TDM vs FDM (frequency-division multiplexing).** TDM gives each user the **whole bandwidth for a slice of time**. FDM gives each user **a slice of bandwidth for all time**. AM broadcast is FDM (each station owns its own carrier frequency); telephone backbones are TDM (each call owns a $1/24$ slot in a T1 frame). Modern systems combine both (e.g., LTE OFDMA $=$ OFDM frequency slots $\times$ time slots).

## Formal definition

For $N$ PAM-modulated signals, each requiring sample rate $f_s \geq 2B$ per channel:

$$\text{slot period} = \frac{T_s}{N + N_{\text{sync}}}, \qquad \text{pulse rate} = (N + N_{\text{sync}}) \cdot f_s$$

where $N_{\text{sync}}$ is the number of sync slots per frame (typically $1$ for simple framing). For HW7 problem 2:

$$f_s = 40 \text{ kHz}, \quad T_s = 25\,\mu\text{s}, \quad N = 20, \quad N_{\text{sync}} = 1,$$

$$\text{slot period} = \frac{25\,\mu\text{s}}{21} \approx 1.19\,\mu\text{s}, \qquad \text{pulse rate} = 21 \cdot 40 \text{ kHz} = 840 \text{ kHz}.$$

==**Bandwidth scaling rule:** TDMing $N$ channels onto one wire requires at least $N \cdot f_s$ total pulse rate (or $(N+1) \cdot f_s$ with a sync slot). The wire's bandwidth must support the higher rate.==

## Why it matters / when you use it

- **Telephony.** T1 $=$ $24$ voice channels TDMed at $8$ kHz each $\to$ $1.544$ Mbps. The whole telecom backbone of the 1980s.
- **Stage 2 of [[system-pipeline]].** Per-ED CSI ACKs arrive in **TDMA slots** — each ED has its own assigned slot to report $|\hat h_n|$. Same TDM idea, applied wirelessly.
- **CPU time-sharing / OS scheduling.** Each process gets a slot of CPU time. Same principle, applied to a different shared resource.

## Common mistakes

- **Forgetting the sync slot.** Without a sync indication, the receiver has no way to know "this is slot $0$ of channel $1$." A naive $N \cdot f_s$ answer to HW7 problem 2 ($= 800$ kHz) is missing the sync overhead.
- **Sampling below Nyquist for some channel.** Every channel must be sampled at $\geq 2B$ of *that channel's* bandwidth. If one channel has wider bandwidth, its sample rate must be higher — and the frame structure has to accommodate.
- **Assuming the wire bandwidth is equal to per-channel bandwidth.** TDM trades wire bandwidth for per-channel rate. The wire must run $N+1$ times faster than any individual channel.
- **Confusing TDM with TDMA.** TDM is the multiplexing scheme (wired or wireless). TDMA is the access protocol on a shared *wireless* medium (multiple transmitters take turns on the same frequency). Same time-slotting idea; different setting.

## Related
- [[pulse-amplitude-modulation]] — the modulation TDM rides on
- [[amplitude-modulation]] — FDM's natural counterpart (different carrier per user)
- [[ofdm]] — frequency-domain analog of TDM (slot in frequency, not time)
- [[system-pipeline]] — Stage 2 (per-ED CSI ACKs in TDMA slots)
- [[paper-aircomp-feel-demo]] — practical TDMA-style coordination among SDRs

## Sources / further reading
- HW7 problem 2: `raw/homework/HW7.pdf` + `raw/homework/304_hw7_sample25.pdf`
- B.P. Lathi, *Modern Digital and Analog Communication Systems*, ch. 6
- Wikipedia: https://en.wikipedia.org/wiki/Time-division_multiplexing
