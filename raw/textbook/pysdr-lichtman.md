# PySDR: A Guide to SDR and DSP using Python — Marc Lichtman

**Category:** Wireless / SDR / DSP (the single most wireless-relevant free resource)
**Status:** FREE online textbook
**URL:** https://pysdr.org/
**GitHub (source):** https://github.com/777arc/PySDR
**License:** CC BY-NC-SA 4.0
**Author:** Marc Lichtman (UMD research scientist)
**Roadmap phase:** Phase 1 (week 4) onward; referenced through Phase 3

## Topic coverage (chapters)
1. Intro to SDR
2. Frequency-domain basics (FFT interpretation — overlaps with our [[dft]] arc)
3. IQ sampling
4. Digital modulation (BPSK/QPSK/QAM constellations, pulse shaping)
5. PlutoSDR in Python (relevant to Jayden's 4× Pluto AirComp build!)
6. USRP in Python
7. Noise and dB
8. Filters (FIR/IIR, design, windowing)
9. Link budgets
10. Channel coding
11. Frequency-hopping spread spectrum
12. OFDM — **the single most important chapter for this roadmap**
13. Pulse shaping
14. Synchronization (timing, frequency, phase recovery)
15. Cyclostationary processing
16. Machine learning for RF — introductory treatment, good bridge to the DL-for-PHY literature

## Why it's on the roadmap
The roadmap calls it "the single most wireless-relevant free resource anywhere." It sits exactly at the Python + DSP + wireless intersection that Jayden's target research lives at. Chapter 12 (OFDM) is the starting point for the **OFDM-from-scratch project** (Phase 1 Month 2), and Chapter 16 (ML for RF) is the gentle on-ramp to the O'Shea / Hoydis literature.

## Cross-links to existing vault content
PySDR's FFT chapter overlaps our existing coverage in [[eee-404]] — use it to reinforce bin mapping and windowing, especially the interactive plots.
PySDR's Pluto chapter is directly useful for the AirComp implementation ([[system-pipeline]]).

## Concepts this book anchors
- [[ofdm]]
- [[iq-sampling]]
- [[pulse-shaping]]
- [[synchronization-timing]]
- [[channel-coding]]

## Related wiki pages
- [[python-ml-wireless]]
- [[marc-lichtman]]
- [[system-pipeline]] — the existing AirComp pipeline
