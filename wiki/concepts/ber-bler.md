---
title: BER and BLER
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - ber
  - bler
  - performance-metric
  - foundations
  - wireless
sources:
  - "[[article-2026-04-23-physical-layer-ml-roadmap]]"
created: 2026-05-01
updated: 2026-05-01
---

# Bit Error Rate (BER) and Block Error Rate (BLER)

## In one line
**BER = fraction of bits decoded wrong.** **BLER = fraction of code blocks (frames) decoded wrong** — even one wrong bit fails the block. The two canonical wireless-system performance metrics; PHY-ML papers report one or the other (usually BLER for 5G NR, BER for raw modulation).

## Example first

Send 100 codewords, each containing 50 bits. Decoder gets:
- 95 codewords completely correct.
- 4 codewords with 1 bit wrong each.
- 1 codeword with 5 bits wrong.

**BER:**
$$\text{BER} = \frac{4 \cdot 1 + 1 \cdot 5}{100 \cdot 50} = \frac{9}{5000} = 1.8 \times 10^{-3}.$$

**BLER:**
$$\text{BLER} = \frac{4 + 1}{100} = 0.05 = 5 \times 10^{-2}.$$

Note the ratio: BLER ≫ BER per block size. **One bit wrong = whole block fails.** This is why $10^{-5}$ BER → $\sim 10^{-2}$ BLER for 1000-bit blocks (rule of thumb).

## The idea

Wireless systems are evaluated at different abstraction layers:
- **BER** is the lowest-level metric — measures uncoded modulation/demodulation.
- **BLER** is what the protocol actually cares about — a single bit error inside an LDPC-decoded block triggers retransmission (HARQ).

In **AWGN** (Gaussian noise, no channel coding), BER for BPSK / QPSK is the exact Q-function:
$$\text{BER}_{\text{BPSK}} = Q\!\left(\sqrt{\frac{2 E_b}{N_0}}\right)$$
where $E_b/N_0$ is the SNR per bit. This is the reference curve every modulation gets compared to.

After **channel coding** (LDPC, polar, turbo), BER drops dramatically — and the relevant metric becomes BLER (the probability the decoded block contains at least one error).

### What "$10^{-2}$ BLER point" means
In 5G NR, the **$10^{-2}$ BLER point** is the standard operating point — the SNR at which 1% of blocks fail and HARQ kicks in. PHY-ML papers report "$X$ dB gain at $10^{-2}$ BLER" as the headline metric. NRX papers ([[paper-nrx-cammerer-2023]], [[paper-nrx-wiesmayr-2024]]) report 0.5–2 dB gain at this point — a meaningful operational improvement.

### Why $E_b/N_0$ instead of SNR
$E_b/N_0$ normalizes per **information bit** — apples-to-apples across modulation orders and code rates:
$$\frac{E_b}{N_0} = \frac{E_s/N_0}{R \cdot k}$$
where $R$ is code rate and $k = \log_2 M$ for $M$-ary modulation. BER curves use $E_b/N_0$ on the x-axis; BLER curves often use SNR (in dB) directly because they're for fixed-modulation, fixed-rate evaluation.

## Formal definition

For a transmission of $N$ blocks of $K$ bits each:
$$\text{BER} = \frac{1}{NK}\sum_{n=1}^{N} \sum_{i=1}^{K} \mathbb{1}\bigl[\hat b_{n,i} \neq b_{n,i}\bigr], \quad \text{BLER} = \frac{1}{N}\sum_{n=1}^{N} \mathbb{1}\bigl[\hat{\mathbf{b}}_n \neq \mathbf{b}_n\bigr].$$

Reported on **log-y, linear-x dB** axes. The headline figure of any PHY-ML paper.

## Why it matters

- **The headline metric.** Every modulation, channel-coding, or neural-receiver paper plots BER or BLER vs. SNR.
- **Operational point.** $10^{-2}$ BLER is the 5G design point; below this, HARQ retransmission rate becomes the bottleneck.
- **Sim-to-real check.** A real-world deployed receiver should hit similar BLER to the simulator; sim-only papers risk the "validated the simulator" critique.

## Common mistakes

- **Confusing $E_b/N_0$ and SNR.** They differ by $10\log_{10}(R\cdot k)$ dB.
- **Not enough Monte Carlo trials.** To estimate BER $= 10^{-5}$ accurately, you need at least $10^7$ bits → $10^4$ frame errors. Use **importance sampling** or **multi-SNR continuation** to speed this up.
- **Reporting BER when BLER matters.** A neural decoder might improve BER but worsen BLER (correlated errors → fewer total bit errors but block failures shift). Always report the metric the system cares about.
- **Comparing curves at different rates.** A $R=1/2$ code at SNR $X$ vs. a $R=3/4$ code at the same SNR — apples to oranges. Use $E_b/N_0$.

## Related
- [[qam-modulation]] — sets the modulation order $k$.
- [[ldpc-codes]] — sets the code rate $R$.
- [[neural-receiver]] — improves BLER over LMMSE.
- [[autoencoder-phy]] — reports BLER vs. AWGN baseline.
- [[python-ml-wireless]] — Phase 1 OFDM-from-scratch deliverable: "BER vs Eb/N0 vs theory" is the headline figure.

## Practice
- Plot BPSK BER vs. $E_b/N_0$ in AWGN; verify against $Q(\sqrt{2 E_b/N_0})$.
- Plot 16-QAM and 64-QAM BER on the same axes; verify the ~6 dB-per-doubling rule.
- For a $(7,4)$ Hamming code, plot BER vs. uncoded BER at fixed SNR; observe the **coding gain**.
