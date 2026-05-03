---
title: Link adaptation
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - 5g
  - mcs
  - olla
  - link-adaptation
  - phase-4
sources:
  - "[[paper-wiesmayr-salad-2025]]"
created: 2026-05-01
updated: 2026-05-01
---

# Link adaptation

## In one line
**Link adaptation chooses the modulation-and-coding-scheme (MCS) for each slot to maximize spectral efficiency subject to a target block-error-rate (BLER ≈ 10%).** The classical industry-standard algorithm is **outer-loop link adaptation (OLLA)**; modern ML alternatives like [[paper-wiesmayr-salad-2025|SALAD]] beat OLLA by ~15%.

## Example first

5G NR has 28 MCS indices (MCS Table 1). At each slot, the BS:
1. Reads the latest **CQI report** from UE (a wide-band SINR-proxy index 0–15).
2. Looks up "expected BLER for each MCS at this CQI" in a pre-computed table.
3. Picks the highest-rate MCS such that expected BLER ≤ τ (typically 10%).
4. Applies an **OLLA offset** Δ adjusted by ACK/NACK history: NACK → Δ ↓ (be more conservative); ACK → Δ ↑.

If τ is too aggressive: many retransmissions, bad TCP throughput. If τ is too conservative: wasted spectral efficiency. **MCS choice is the closed bottleneck for cellular throughput.**

## The idea

Link adaptation is a **closed-loop control problem**: SINR moves stochastically (fading, mobility, interference); MCS must track it; ACK/NACK is the feedback signal.

| Family | Method |
|---|---|
| **Sampling-based** | Auto Rate Fallback (ARF), Sample Rate (Wi-Fi) — pure trial-and-error |
| **Model-based (industry standard)** | OLLA — fixed-stepsize SINR offset adjustment |
| **ML-based (modern)** | [[paper-wiesmayr-salad-2025|SALAD]] — Bayesian SINR inference + hypothesis-test MCS selection |

## Why it matters / where it sits in the roadmap

- **Phase 4 M10 reading.** [[paper-wiesmayr-salad-2025]] is the canonical reproduction target.
- **The "outer controller" of any neural receiver.** A NRX picks symbols; link adaptation picks MCS. Both happen every slot; both are intern-relevant work.
- **NVIDIA Aerial intern flagship.** SALAD shipping on Sionna Research Kit is exactly the deliverable a BS-level intern would extend.

## Common mistakes
- **Treating OLLA as bandit-style.** OLLA is **not** a bandit — it tracks SINR via a *single* offset parameter, not a per-arm value.
- **Ignoring delay.** CQI reports are old by the time the BS uses them; in TDD they can lag by several slots.
- **Wrong stepsize.** Too small = slow convergence; too large = unstable. SALAD's contribution is making the stepsize adaptive.

## Related
- [[paper-wiesmayr-salad-2025]] — modern SALAD method.
- [[harq]] — provides the ACK/NACK feedback every link-adaptation algorithm consumes.
- [[ber-bler]] — direct dependency.
- [[neural-receiver]] — the per-symbol cousin.
- [[reinforcement-learning]] — SALAD is a Bayesian-RL method (online inference + hypothesis-test selection).
- [[bandit-regret]] — alternative framing: link adaptation as a contextual bandit.
- [[paper-sionna-research-kit-2025]] — testbed where SALAD is deployed.
- [[python-ml-wireless]]
