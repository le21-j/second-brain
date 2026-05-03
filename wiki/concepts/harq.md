---
title: HARQ (Hybrid Automatic Repeat Request)
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - 5g
  - harq
  - retransmission
  - link-adaptation
  - phase-4
sources:
  - "[[paper-wiesmayr-salad-2025]]"
created: 2026-05-01
updated: 2026-05-01
---

# HARQ (Hybrid Automatic Repeat Request)

## In one line
**HARQ is 5G/LTE's retransmission protocol: the receiver decodes; if the CRC fails it sends NACK; the transmitter combines the failed and retransmitted copies to decode jointly — this is what generates the ACK/NACK feedback that drives [[link-adaptation]] and [[paper-wiesmayr-salad-2025|SALAD]].**

## Example first

**Slot 1:** BS transmits MCS-15 transport block. UE decodes; CRC check **fails** → UE sends NACK on PUCCH.

**Slot 2:** BS retransmits the **same** transport block (with possibly different redundancy version). UE combines the slot-1 received signal with slot-2 received signal — **chase combining** (just sum the soft LLRs) or **incremental redundancy** (each retransmission adds new parity bits). Decodes. CRC passes → ACK.

Maximum retransmission count: typically 4. After that, the transport block is dropped → upper-layer (RLC) handles it.

## The idea

Pure ARQ retransmits identical packets. **Hybrid ARQ** combines the received signal across retransmissions, exploiting **soft information** even from failed decodings. Two variants:

| Variant | What changes | Combining |
|---|---|---|
| **Chase combining (HARQ-CC)** | Identical retransmission | Sum LLRs |
| **Incremental redundancy (HARQ-IR)** | New parity bits per retransmission | Decoder uses larger codeword |

5G NR supports both; IR is more efficient at high SNR; CC is simpler.

## Why it matters / where it sits in the roadmap

- **Load-bearing for [[link-adaptation]].** Both classical OLLA and modern [[paper-wiesmayr-salad-2025|SALAD]] use ACK/NACK from HARQ as their **only** feedback signal. No HARQ → no link-adaptation.
- **Phase 4 reading prereq.** Reading SALAD without understanding HARQ is hopeless. The 10% BLER target is the per-attempt BLER **before** HARQ; effective post-HARQ BLER is much lower.
- **Effective BLER computation.** With max 4 retransmissions and per-attempt BLER $\tau$, post-HARQ residual error is **at most** $\tau^4$ in the **independent-attempts upper bound** (HARQ-CC with no soft-combining gain assumed). Real HARQ with chase-combining or incremental-redundancy makes residual *much* lower than $\tau^4$ — but the bound is what justifies $\tau \approx 10\%$ being acceptable: $0.1^4 = 10^{-4}$ residual upper-bound.

## Common mistakes
- **Confusing target BLER (per attempt) with residual BLER (post-HARQ).** Always specify which.
- **Ignoring HARQ in BER plots.** Pre-HARQ vs post-HARQ curves differ by orders of magnitude — must be labeled.
- **Forgetting RV cycling.** 5G NR cycles through 4 redundancy versions; SALAD must condition on RV.

## Related
- [[link-adaptation]] — primary consumer of HARQ feedback.
- [[ber-bler]] — per-attempt vs post-HARQ distinction.
- [[paper-wiesmayr-salad-2025]] — SALAD uses HARQ ACK/NACK as the only feedback.
- [[ldpc-codes]] — 5G NR data channel uses LDPC + HARQ.
- [[python-ml-wireless]]
