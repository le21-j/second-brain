# Datasets catalog — Physical-Layer ML Roadmap

Canonical datasets for physical-layer ML. Use these for every repro project.

## DeepMIMO v4

- **URL:** https://www.deepmimo.net/
- **Install:** `pip install --pre deepmimo`
- **Paper:** Alkhateeb 2019 (arxiv:1902.06435)
- **GitHub:** https://github.com/DeepMIMO/DeepMIMO
- **Maintainer:** Umut Demirhan (Wi-Lab PhD, graduated 2025)
- **Main scenarios:**
  - **O1** — outdoor grid, 3.5 / 28 / 60 GHz, THz available.
  - **I1 / I3** — indoor scenarios.
  - **Boston5G_3p5**, **Boston5G_28** — city scenarios.
  - **asu_campus_3p5** — ASU campus (the Wi-Lab home scenario).
  - 12 additional city scenarios used for LWM pretraining.
- **Key v4 feature:** `dm.download()`, `dm.load()`, `dataset.compute_channels()`, and **`dm.convert()`** which accepts Sionna RT, Wireless InSite, or NVIDIA AODT outputs.
- See [[deepmimo]] for concept page.

## DeepSense 6G

- **URL:** https://www.deepsense6g.net/
- **Paper:** Alkhateeb et al. 2023 (arxiv:2211.09769)
- **Baselines:** https://github.com/DeepSense6G
- **Scope:** 1M+ synchronized real-world samples across 40+ scenarios.
- **Modalities:** mmWave 60 GHz phased array + RGB/360° cameras + 32-channel LiDAR + 77 GHz FMCW radar + RTK GPS + sub-6 channels.
- **Past challenges:**
  - Multi-Modal Beam Prediction 2022 (scenario 31 is the held-out test).
  - LiDAR-Aided 2023.
  - Multi-Modal V2V 2023.
- See [[deepsense-6g]] for concept page.

## DeepVerse 6G

- **URL:** https://deepverse6g.net/
- Synthetic digital-twin companion to DeepSense.

## RadioML 2016.10a / 2018.01A

- **URL:** https://www.deepsig.ai/datasets/
- **Paper:** O'Shea, Roy, Clancy 2018 (arxiv:1712.04578)
- **Use:** Automatic modulation classification benchmark. Required Phase 2 reproduction.
- **Modulations:** 11 analog+digital (2016), 24 digital+analog (2018).

## COST2100 preprocessed

- Used in CsiNet et al. papers.
- Reference implementations: https://github.com/sydney222/Python_CsiNet, https://github.com/Kylin9511/CRNet, https://github.com/SIJIEJI/CLNet.

## Related wiki pages
- [[python-ml-wireless]]
- [[deepmimo]]
- [[deepsense-6g]]
