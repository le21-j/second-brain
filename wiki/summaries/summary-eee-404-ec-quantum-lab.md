---
title: EEE 404 EC Lab — QFT vs DFT Speech Compression (J-DSP)
type: summary
source_type: lab
source_path: raw/labs/eee-404/ec-quantum-qft_dft_exercise.pdf
source_date: 2026-04-29
course:
  - "[[eee-404]]"
tags: [eee-404, lab, extra-credit, quantum-computing, qft, dft, speech, j-dsp, peak-picking]
created: 2026-04-29
---

# EC Lab — QFT vs DFT Speech Compression

**Source:** [`raw/labs/eee-404/ec-quantum-qft_dft_exercise.pdf`](../../raw/labs/eee-404/ec-quantum-qft_dft_exercise.pdf) (9 pages, by Aradhita Sharma + Andreas Spanias, ASU SenSIP)
**Table template:** `raw/labs/eee-404/ec-quantum-qft_dft_jdsp_simulation_table.docx`
**Platform:** [J-DSP web simulator](https://jdspwebsite.netlify.app/) (no installs).
**Due:** 2026-05-02 06:59 UTC. **Worth: 20 EC points.**

## TL;DR
Use J-DSP to compare classical FFT-based and quantum QFT-based speech compression via peak-picking. For each of 14 (qubit, $N$, $L$, noise-type) combinations, record the SNR using both "first $L$" and "largest $L$" peak-selection. Discuss trends: SNR vs $L$, classical vs quantum, first vs largest, effect of amplitude vs phase damping noise. **No coding** — drag-and-drop blocks in J-DSP.

## Key takeaways
- **QFT formula** $\text{QFT}|k\rangle = \tfrac{1}{\sqrt N} \sum_j e^{+j 2\pi jk/N} |j\rangle$ (note positive sign vs DFT's negative sign + a SWAP gate at the end of the circuit).
- **QFT complexity:** $O(n^2)$ on $n = \log_2 N$ qubits — exponential speedup over $O(N \log N)$ FFT, in the noise-free limit.
- **Peak-picking by largest $L$ wins by Parseval** (preserves most energy).
- **Quantum noise types tested:** amplitude damping ($\gamma = \sin^2\theta$, qubit $|1\rangle \to |0\rangle$ decay), phase damping ($\lambda = 1 - \cos^2\phi$, phase coherence loss). Amplitude noise hits magnitudes harder than phase noise → larger SNR drop for peak-picking.
- **Noise-free SNR:** classical and quantum should match (modulo numerical precision and bin swap).

## Concepts introduced or reinforced
- [[dft]], [[fft]], [[idft]] — classical
- [[parseval-theorem]] — justifies "largest L" peak-picking
- **QFT** (new — could become its own page if Jayden plans to do quantum-DSP research)
- **Quantum noise channels** — amplitude damping, phase damping, depolarising
- **Speech analysis-synthesis via peak-picking** — frame-by-frame compression

## Walkthrough produced
[[eee-404-ec-quantum-walkthrough]] — concept overview + 56-run J-DSP plan + report skeleton.

## Questions this source raised
- Does J-DSP's QFT block actually simulate a quantum circuit, or just compute the DFT and inject classical noise? (The lab implies the latter — Kraus operators applied as deterministic perturbations.)
- Could the same setup test other quantum algorithms (Grover, QPE) for DSP? (Probably not in J-DSP; would need Qiskit/Cirq.)
