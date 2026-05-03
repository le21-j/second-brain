---
title: Federated learning (FL)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - federated-learning
  - fedavg
  - distributed-ml
  - aircomp
  - phase-3
  - phase-4
sources:
  - "[[paper-aircomp-feel-demo]]"
  - "[[paper-experimental-ota-fl]]"
  - "[[paper-ncota-dgd]]"
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-05-01
updated: 2026-05-01
---

# Federated learning (FL)

## In one line
**Federated learning trains a global model across many decentralized devices that each hold private local data — devices send model updates (gradients or weights), never raw data, to a coordinator.** McMahan et al. 2017 (Google). **Jayden's AirComp project ([[system-pipeline]]) is FL — specifically Over-the-Air FL (OTA-FL), where the channel sums updates "for free" instead of transmitting them digitally.**

## Example first

**FedAvg on 100 phones training a next-word predictor (the original Google Gboard use case).**

Round $t$:
1. Server broadcasts current global weights $\boldsymbol\theta^{(t)}$.
2. Each phone $i$ trains for $E$ local SGD epochs on its private data → produces $\boldsymbol\theta_i^{(t+1)}$.
3. Phones upload local updates (or just the differences $\boldsymbol\theta_i^{(t+1)} - \boldsymbol\theta^{(t)}$).
4. Server **averages**: $\boldsymbol\theta^{(t+1)} = \frac{1}{N}\sum_i \boldsymbol\theta_i^{(t+1)}$ (or weighted by local-data size).
5. Repeat.

After many rounds, the global model approximates centralized training **without ever centralizing the data**.

For wireless: substitute "phones" → "edge devices (EDs)," "Gboard" → "any task you'd train centrally," and notice the **uplink bottleneck** — uploading $N$ models per round is bandwidth-heavy. **AirComp solves this** by sending all $N$ updates on the same channel and exploiting superposition: the channel sum **is** the average (modulo gain calibration).

## The idea — three families

| Family | What's averaged | Pros | Cons |
|---|---|---|---|
| **FedAvg** (McMahan 2017) | Local-trained weights | Simple, works | Data-heterogeneity can hurt convergence |
| **FedProx** (Li 2018) | Weights + proximal regularizer | Robust to heterogeneous data | Tuning |
| **OTA-FL / AirComp** | Gradients sent over the analog channel | **Bandwidth-free aggregation** | Needs synchronized power-control + channel inversion |

## Wireless specialization — Over-the-Air FL

OTA-FL is **the** wireless-AI research thread that connects Jayden's AirComp project to the 6G literature:

1. Each ED transmits its gradient as a complex baseband symbol; powers are aligned so the **channel-sum at the AP is the desired aggregate gradient** (modulo noise).
2. AP applies the aggregate as a global update; no per-ED message decoding needed — pure analog sum.
3. **Order-of-magnitude bandwidth savings** vs digital FL.

This is **exactly** the framework around which [[system-pipeline]] is designed. The Şahin & Yang AirComp survey ([[paper-aircomp-survey]]) is the canonical reference; [[paper-aircomp-feel-demo]] is the SDR demo of the same; [[paper-experimental-ota-fl]] is the first 5G-NR-compliant testbed (Pradhan 2025).

## Why it matters / where it sits in the roadmap

- **Phase 4 M11+ load-bearing.** Wi-Lab's V2V / DeepSense / LWM stack increasingly leans on federated learning (Morais alumni connection at NVIDIA reinforces this).
- **The single biggest cross-pollination between AirComp and the broader roadmap.** [[python-ml-wireless]] frames AirComp as "the first paper" — which only makes sense if the AirComp work is contextualized as OTA-FL, the wireless-FL flavor.
- **Cold-email leverage.** Mentioning OTA-FL as a "first paper" in the same sentence as [[paper-aircomp-survey]] + [[paper-experimental-ota-fl]] anchors the work in a literature both target labs (NVIDIA Sionna + Wi-Lab) actively engage with.
- **Adjacent to [[link-adaptation]] / [[harq]].** OTA-FL has its own retransmission and rate-adaptation literature; the same questions (when to retransmit? how to adapt to channel?) recur with different answers.

## Open challenges in OTA-FL

The challenges that make OTA-FL non-trivial — and the gaps Jayden's [[system-pipeline]] addresses:

| Challenge | What's hard | Status |
|---|---|---|
| **Channel inversion** | Need each ED to apply $1/h_i$ truncated power | [[truncated-channel-inversion]] (in [[robust-signaling]]) |
| **Synchronization** | Tx phase + frequency alignment across $N$ EDs | [[paper-experimental-ota-fl]] uses PTP + Octoclock |
| **Privacy** | Even gradients leak data | Differential-privacy variants |
| **Heterogeneous channels** | Some EDs see deep fades | Truncation, regret-based exclusion ([[regretful-learning]]) |
| **Non-IID data** | Local data distributions differ | FedProx, personalization layers |

## Common mistakes

- **Confusing FedAvg with synchronous-only.** FedAvg is the canonical synchronous version. Asynchronous variants exist; harder to analyze.
- **Ignoring system heterogeneity.** Real EDs have different compute / bandwidth / availability. FL papers that assume identical EDs are simulator-only.
- **Treating OTA-FL as just "wireless FedAvg."** It's an analog-aggregation technique that **needs the wireless channel to behave** — channel calibration, power control, and synchronization are all load-bearing.

## Related
- [[reinforcement-learning]] — adjacent decentralized-learning paradigm.
- [[regretful-learning]] — Hart-Mas-Colell regret matching is one OTA-FL exclusion mechanism (Jayden's existing AirComp anchor).
- [[system-pipeline]] — Jayden's literal OTA-FL implementation.
- [[paper-aircomp-survey]] — Şahin & Yang 2023 — comprehensive AirComp survey.
- [[paper-aircomp-feel-demo]] — Şahin 2022 — SDR OTA-FL demo (closest existing reproduction template).
- [[paper-ncota-dgd]] — non-coherent OTA decentralized GD.
- [[paper-experimental-ota-fl]] — first 5G-NR-compliant OTA-FL testbed.
- [[paper-deepsense-v2v-2024]] — V2V multi-modal data ripe for FL aggregation.
- [[python-ml-wireless]]

## Practice
- **TODO (Phase 4)** — Reproduce vanilla FedAvg on MNIST with $N=10$ simulated clients. Then add channel-inversion analog aggregation in NumPy → validate the AirComp framework end-to-end before any hardware deploy.
