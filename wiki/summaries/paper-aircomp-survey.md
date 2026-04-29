---
title: A Survey on Over-the-Air Computation (Şahin & Yang 2023)
type: summary
source_type: article
source_path: raw/articles/A_Survey_on_Over-the-Air_Computation.pdf
source_date: 2023
course: [[research]]
tags: [aircomp, survey, nomographic-functions, csi, synchronization]
created: 2026-04-21
updated: 2026-04-26
---

# A Survey on Over-the-Air Computation

**Authors:** Şahin & Yang. IEEE Commun. Surv. Tutorials 2023. 31 pp.

## TL;DR
Comprehensive survey of practical AirComp: what functions are computable (nomographic functions via Kolmogorov superposition), how schemes deal with fading (classified by CSIT/CSIR availability), encoding strategies (analog vs digital / nested lattice / balanced numerals), and the enabling mechanisms (synchronization, power control, channel estimation, security). Use this as the reference for background claims in the research design.

## Key takeaways
- **Computable functions:** any continuous function of $K$ variables can be represented as a superposition of at most $2K+1$ nomographic functions (Kolmogorov). Common cases — arithmetic mean, weighted sum, $p$-norm, max/min via binary-representation iterations, majority vote.
- **Classification by CSI availability** (Section III-B and Table II):
  - **CSIT available, CSIR not:** truncated channel inversion (TCI), phase correction, amplitude correction + energy estimation, MRT. Requires accurate + fresh CSIT; sensitive to synchronization.
  - **CSIT + CSIR:** ZF / MMSE coordination, RIS-assisted, diversity-oriented. Most flexible but highest overhead.
  - **CSIT not, CSIR available:** channel hardening (massive MIMO), advanced receivers.
  - **Neither:** orthogonal signaling (FSK-MV, CSK), energy-based non-coherent. Robust against sync errors and CFO.
- **Synchronization analysis (Sec IV-A):** timing errors cause a subcarrier-index-scaled phase rotation in OFDM; CFO causes inter-carrier interference. Sample-level sync is required for methods relying on phase alignment; non-coherent methods only need CP-level sync.
- **Power management (Sec IV-B):** receiver-side alignment (typically channel inversion), PAPR/OBO at transmitter side. Trade-off between cell size and back-off (Eq 43-44).
- **Encoding:**
  - Analog — linear (compression via sparsification, e.g., gradient), affine (energy-based), nonlinear (QAM pairing).
  - Digital — nested lattice codes (achieve information-theoretic rates), PAM-based, balanced number systems.
- **Demonstrations summary (Sec V-I):** Şahin 2022 demo (FSK-MV, 5 Adalm Pluto SDRs, 95% MNIST accuracy without CSI). Very relevant to Jayden's testbed considerations.
- **Protocols gap:** AirComp has never been standardized. Open directions include integration with 3GPP 5G/6G RACH-like procedures, synchronization, and security. Jayden's pipeline design falls exactly in this gap.

## Concepts introduced or reinforced
- [[aircomp-basics]] — generalized system model (Eq 8 in survey)
- [[truncated-channel-inversion]] — TCI as the dominant pre-equalization approach
- [[fsk-based-majority-vote]] — non-coherent alternative
- [[kolmogorov-superposition]] — theoretical underpinning
- [[aircomp-metrics]] — MSE, NMSE, outage, computation rate

## Questions this source raised
- Which CSI regime does Jayden's pipeline fall into? **CSIT at ED, no CSIR at ES** — each ED measures its own $|h_n|$ from the DL beacon. The ES broadcasts aggregate $g(|h_{n'}|)\sqrt{P_{n'}}$ sums for utility computation but doesn't need per-ED CSI for detection because the regret algorithm handles channel uncertainty.
- Standardization path: the survey names IEEE 802.11 AI/ML TIG and 3GPP 22.876 as potential homes. Jayden's WiFi-inspired protocol design is aligned with this trajectory.

## Related
- [[system-pipeline]] — the research design
- [[paper-unregrettable-hpsr]] — the specific algorithm being implemented
- [[paper-aircomp-feel-demo]] — the closest practical analog (SDR demonstration)
