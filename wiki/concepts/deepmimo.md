---
title: DeepMIMO
type: concept
course: [[python-ml-wireless]]
tags: [dataset, ray-tracing, wi-lab, asu, channels, mimo]
sources: [[article-2026-04-23-physical-layer-ml-roadmap]]
created: 2026-04-23
updated: 2026-04-26
---

# DeepMIMO

## In one line
A public, ray-traced MIMO channel dataset from the ASU Wireless Intelligence Lab — you choose a scenario (city, mmWave band, antenna geometry), run `dm.compute_channels()`, and get a pile of frequency-response tensors ready to feed a neural network.

## Example first

```python
import deepmimo as dm

# Pick the ASU campus scenario at 3.5 GHz.
params = dm.default_params()
params["scenario"] = "asu_campus_3p5"
params["active_BS"] = [1]                         # which basestations
params["user_rows"] = [i for i in range(100)]     # which user rows
params["bs_antenna"]["shape"] = [1, 8, 4]         # 1x8x4 UPA at BS
params["ue_antenna"]["shape"] = [1, 1, 1]         # single-antenna UE

dataset = dm.generate(params)
# dataset[0]["user"]["channel"] -> complex channel tensor of shape
# (num_users, num_bs_ant, num_ue_ant, num_subcarriers)
```

That tensor **is** the channel — computed by a ray tracer from a 3D city model, for the exact BS+antenna geometry you specified. You can now train a CNN for channel estimation, a transformer for beam prediction, or pretrain a foundation model ([[large-wireless-model]]) on channels from a dozen scenarios.

## The idea

DeepMIMO was released in 2019 by Ahmed Alkhateeb as the first standardized ray-tracing-based MIMO channel dataset — before it, every wireless-ML paper rolled its own simulator and nothing was comparable. v4 (released 2024, on PyPI as `deepmimo`) is a full rewrite in modern Python, with:

- `dm.download()` — pulls scenarios from the cloud.
- `dm.load()` — loads a cached scenario.
- `dataset.compute_channels()` — computes frequency-response tensors on the fly given your antenna geometry.
- **`dm.convert()`** — **the critical interop feature.** Accepts Sionna RT, Wireless InSite, or NVIDIA AODT outputs and converts them into DeepMIMO format. This is how DeepMIMO becomes the integration glue between Sionna ray tracing and the Wi-Lab ecosystem.

### Scenarios

Most-used scenarios:
- **O1** — synthetic outdoor grid, 3.5 / 28 / 60 GHz, and a THz variant. Pedagogical default.
- **I1, I3** — indoor halls.
- **Boston5G_3p5, Boston5G_28** — Boston street layout.
- **asu_campus_3p5** — the Wi-Lab "home" scenario.
- **12 city scenarios** used to pretrain [[large-wireless-model]] — this is how LWM gets its diversity.

### What DeepMIMO gives you that a 3GPP TDL/CDL channel does not

A 3GPP TDL is a **statistical** channel: specific delays and gains, drawn from published tables, designed to be representative of a *class* of environments. A DeepMIMO channel is **deterministic for a specific location and geometry** — the multipath comes from bouncing rays off the actual buildings. Consequences:

- **Spatial consistency.** Moving the user $1$ m changes the channel smoothly, as it would in reality — not as an independent redraw.
- **Site-specific training.** You can train a beam predictor for a specific cell deployment, because the channels depend on the actual deployment.
- **Multi-user correlation.** Two users in the same environment share rays off the same buildings, so their channels are statistically coupled — crucial for massive-MIMO scheduling research.
- **Digital twin pretraining.** Ray-traced channels are what a [[wireless-digital-twin]] provides during pretraining — DeepMIMO is the file format.

## Formal definition

For a scenario with BS antenna array and user set, DeepMIMO computes the multipath channel as a sum of rays:

$$
h_{u,b}(f) \;=\; \sum_{\ell=1}^{L_{u,b}} \alpha_{u,b,\ell}\; e^{-j 2\pi f \tau_{u,b,\ell}}\; \mathbf{a}_b(\phi_{u,b,\ell}^{\text{AoD}}, \theta_{u,b,\ell}^{\text{AoD}})\;\mathbf{a}_u^{\text{H}}(\phi_{u,b,\ell}^{\text{AoA}}, \theta_{u,b,\ell}^{\text{AoA}})
$$

where $\alpha_\ell, \tau_\ell, \phi_\ell, \theta_\ell$ for each ray come from the ray tracer, and $\mathbf{a}$ are the antenna steering vectors. The ray tracer used in v4 is Wireless InSite for most scenarios; new scenarios can be generated with Sionna RT and imported via `dm.convert()`.

## Why it matters / when you use it

- **Benchmarking wireless ML.** Because thousands of papers now use DeepMIMO scenarios, your results are directly comparable to published work.
- **Foundation-model pretraining.** [[large-wireless-model]] was pretrained on 1M+ DeepMIMO channels across 15 scenarios — this is how you get a "generic" wireless-channel representation.
- **Sionna bridge.** When you want to train a neural receiver on a specific city, the workflow is: generate scene in Sionna RT $\to$ export $\to$ `dm.convert()` $\to$ train.

## Common mistakes

- **Treating DeepMIMO channels as i.i.d.** They are not — adjacent user positions have strongly correlated channels, which breaks most default CSI / beam-prediction pipelines' shuffled-batch assumptions. Use spatial splits for train/val/test.
- **Ignoring antenna geometry.** The same scenario with a $1\times 8$ ULA vs a $4\times 8$ UPA produces very different channels. Log the antenna config in every experiment.
- **Forgetting to version-pin.** `pip install --pre deepmimo` is the v4 release; v3 is still available under the old name. Mixing them is a common reproduction bug.

## Research ties

- **Paper:** Alkhateeb 2019 (arxiv:1902.06435).
- **Maintainer:** Umut Demirhan (Wi-Lab PhD, 2025).
- **Forum:** https://deepmimo.net/forum/ — direct line to Alkhateeb's team.
- **Sponsors:** NSF, Qualcomm, Meta Reality Labs, Nokia Bell Labs, InterDigital, Remcom, NVIDIA.

## The move for Jayden's portfolio
Three DeepMIMO projects compound well:
1. **Channel estimation** (Phase 3 M9) — CNN/U-Net vs LS vs LMMSE on `asu_campus_3p5`.
2. **Beam prediction** (Phase 3 M9) — DeepSense positions paired with DeepMIMO channels.
3. **LWM extension** (Phase 4 capstone) — fine-tune LWM on a new DeepMIMO scenario.

## Related
- [[sionna]] — interoperates via `dm.convert()`.
- [[deepsense-6g]] — real-world companion dataset.
- [[large-wireless-model]] — pretrained on DeepMIMO.
- [[wireless-digital-twin]] — DeepMIMO is the ground truth a digital twin is calibrated against.
- [[alkhateeb]] — creator.
- [[python-ml-wireless]].

## Practice
- Phase 3 M9: CNN channel-estimation repo on `asu_campus_3p5`.
