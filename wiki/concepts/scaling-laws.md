---
title: Neural scaling laws
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - scaling-laws
  - foundation-models
  - lwm
  - chinchilla
  - kaplan
  - phase-4
sources:
  - "[[paper-lwm-2024]]"
  - "[[paper-lwm-spectro-2026]]"
  - "[[paper-lwm-temporal-2026]]"
created: 2026-05-01
updated: 2026-05-01
---

# Neural scaling laws

## In one line
**Empirical power-law relationships between model size $N$, dataset size $D$, compute $C$, and test loss $L$** — they predict that doubling either $N$ or $D$ (or compute) yields a precisely measurable, predictable loss reduction. The framework that justifies "build a bigger LWM and it will be better." Kaplan et al. 2020 (OpenAI) → Hoffmann et al. 2022 (Chinchilla, DeepMind).

## Example first

**Kaplan-style fit** for transformer language models:

$$L(N) \approx \left(\frac{N_c}{N}\right)^{\alpha_N} \quad \text{with} \quad \alpha_N \approx 0.076$$

Doubling $N$ from 100M to 200M parameters: $L$ drops by factor $2^{-0.076} \approx 0.95$ — a 5% loss reduction, every doubling.

For data:

$$L(D) \approx \left(\frac{D_c}{D}\right)^{\alpha_D} \quad \text{with} \quad \alpha_D \approx 0.095$$

For wireless foundation models like [[paper-lwm-2024|LWM]], the same power-law structure is empirically observed across DeepMIMO scenarios — though the constants $(\alpha_N, \alpha_D)$ are different from language models.

## The idea — Chinchilla's compute-optimal training

Hoffmann et al. 2022 ("Chinchilla") showed that **for a fixed compute budget $C$, the optimal $(N, D)$ balance is roughly $N \propto D$.** Kaplan-era models were severely under-trained — too big for their data. Chinchilla-era practice trains for ~20× more tokens per parameter.

For wireless: an LWM trained on 1M DeepMIMO channels with 100M params is **likely under-trained** by Chinchilla's heuristic. Either scale up data → 20M channels, or scale down model. **This is exactly the open question for LWM extensions.**

## Why it matters / where it sits in the roadmap

- **Phase 4 M11 — LWM extension.** Without scaling-laws intuition, a "bigger LWM" extension picks a random $(N, D)$ and may end up worse. The compute-optimal frontier is the right thing to target.
- **Cold-email talking point.** "I traced LWM's compute-optimal frontier across DeepMIMO and found it sits at $N \approx D / 20$" → a Wi-Lab cold-email-tier insight.
- **The "data more than model" wireless question.** Wireless data is **scarce** (real measurements) — scaling laws say $\alpha_D > \alpha_N$, so for wireless, **synthetic-channel data scaling** ([[deepmimo]] / [[paper-luo-dt-csi-feedback-2025|Luo digital-twin]]) is the bigger leverage point than model scaling.

## Common mistakes

- **Quoting Kaplan exponents for non-language tasks.** The constants $(\alpha_N, \alpha_D)$ depend heavily on the task / data distribution. Wireless exponents must be empirically measured, not assumed.
- **Conflating scaling with capability.** Scaling laws predict **loss**; emergent capabilities don't follow the same curves.
- **Ignoring the fixed-compute budget.** A "bigger model" claim without specifying compute equivalence is uninterpretable.

## Related

- [[paper-lwm-2024]], [[paper-lwm-spectro-2026]], [[paper-lwm-temporal-2026]] — the Wi-Lab foundation-model line where these laws would apply.
- [[transformer]] — architecture under study.
- [[large-wireless-model]] — the family that will benefit from explicit scaling-laws analysis.
- [[python-ml-wireless]]
