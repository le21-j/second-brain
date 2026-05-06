---
title: UAV-Assisted Over-the-Air Computation (Fu et al. 2021)
type: summary
source_type: article
source_path: raw/articles/UAV-Assisted_Over-the-Air_Computation.pdf
source_date: 2021
course:
  - "[[research]]"
tags: [aircomp, uav, trajectory-optimization, mse-minimization]
created: 2026-04-21
updated: 2026-05-06
---

# UAV-Assisted Over-the-Air Computation

**Authors:** Fu, Zhou, Shi, Wang, Chen. IEEE ICC 2021.

## TL;DR
Use a UAV as a mobile base station for AirComp to shorten transmission distances and exploit LoS channels. Jointly optimize UAV trajectory, denoising factor at UAV, and per-sensor transmit power to minimize time-averaged MSE. BCD + SCA algorithm. Mostly relevant as context, not a direct input to Jayden's pipeline.

## Key takeaways
- **System model (Sec II-B/C):** received signal $y = \sum b_k h_k s_k + n$, estimated function $\hat f = y / (K\sqrt{\eta})$. Identical form to HPSR.
- **MSE expression** matches HPSR's with path-loss-dependent channel gain.
- **Optimization problem:** non-convex, solved via block coordinate descent between three subproblems (denoising factor — closed form; power — QP; trajectory — SCA).
- **Result:** UAV adaptively balances distance to low-power vs high-power sensors; arc-shaped trajectories better than straight.

## Notes for Jayden's pipeline
- Not directly applicable (Jayden's ES is likely static). Interesting as a future extension: UAV could collect aggregated data in sparsely deployed testbeds.
- Confirms the MSE formulation used in HPSR is the community standard.

## Related
- [[paper-unregrettable-hpsr]]
- [[aircomp-basics]]
