---
title: Example — Direct DFT on 5 Minutes of Speech
type: example
course: [[eee-404]]
tags: [dft, complexity]
sources: [[slides-fft-core-equations]]
created: 2026-04-21
updated: 2026-04-26
---

# Example — Direct DFT on 5 Minutes of Speech

## Setup
- $5$ minutes of speech sampled at $f_s = 8$ kHz
- $N = 5 \times 60 \times 8000 = $ **$2.4 \times 10^6$ samples**
- DSP at $168$ MHz, 1 instruction per cycle ($168$ MIPS)

## Direct DFT cost
$N^2$ complex MULTs $= 4N^2$ real MULTs (using [[complex-multiplication]]: $1$ CMULT $= 4$ MULTs).

Total $= 4 \times (2.4 \times 10^6)^2 = $ **$2.304 \times 10^{13}$ real MULTs**.

## Wall-clock time
Time $= 2.304 \times 10^{13} / (168 \times 10^6) \approx $ **$137{,}143$ seconds $\approx 38$ hours**.

## With FFT
$(N/2)\cdot\log_2 N$ complex MULTs. $\log_2(2.4 \times 10^6) \approx 21.2$, call it $22$ (nearest power of 2 is $N = 4M$). Total $\approx (2\cdot 10^6 \times 22) \times 4 \approx $ **$1.8 \times 10^8$ real MULTs**.

Time $\approx 1.8 \times 10^8 / (168 \times 10^6) \approx $ **$1.1$ seconds**.

## Takeaway
Same output. **$38$ hours vs. $1$ second.** That's why FFT exists.

## Related
- [[dft-computation-complexity]]
- [[fft]]
