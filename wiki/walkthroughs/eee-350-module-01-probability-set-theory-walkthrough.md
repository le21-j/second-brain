---
title: "EEE 350 Module 1 — Set Theory, Probability Spaces, Conditional Probability Walkthrough"
type: walkthrough
course:
  - "[[eee-350]]"
tags:
  - eee-350
  - walkthrough
  - probability-axioms
  - conditional-probability
  - bayes-rule
  - counting
sources:
  - "raw/textbook/Probability and Stochastic Processes_ Third Ed copy.pdf"
created: 2026-05-06
updated: 2026-05-06
---

# EEE 350 Module 1 — Set Theory, Probability Axioms, Conditional Probability

> [!tip] **What this is.** Module 1 = the foundations: probability axioms, conditional probability, Bayes' rule, counting.

## Problem inventory

| Slot | 2nd ed | **3rd ed** | Topic |
|---|---|---|---|
| 1 | 1.5.2 | **1.4.2** | Conditional prob from die roll |
| 2 | 1.7.3 | **2.1.3** | Tree / law of total probability |
| 3 | 1.7.5 | **2.1.5** | Bayes' rule — HIV test |
| 4 | 1.8.6 | **2.2.12** | Counting — basketball lineup |
| 5 | 1.9.1 | **2.3.1** | Binomial as i.i.d. Bernoulli |

## Framework

> [!tip] **What to internalize.**
>
> 1. **Probability axioms.** $P(\Omega) = 1$, $P(A) \geq 0$, countable additivity. $P(A^c) = 1 - P(A)$, $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
> 2. **Conditional probability.** $P(A \mid B) = P(A \cap B)/P(B)$ for $P(B) > 0$.
> 3. **Total probability + Bayes.** $P(A) = \sum_i P(A \mid B_i)P(B_i)$ for partition $\{B_i\}$. $P(B_i \mid A) = P(A \mid B_i)P(B_i)/P(A)$.
> 4. **Counting:** combinations $\binom{n}{k} = n!/(k!(n-k)!)$, permutations $n!/(n-k)!$.

---

## Problem 1 (3rd-ed 1.4.2) — Conditional probability from die roll

> [!example] Six-sided die. $R_i$ = roll is $i$. $G_j$ = roll > $j$. $E$ = roll is even.
> (a) $P[R_3 \mid G_1]$. (b) $P[R_6 \mid G_3]$. (c) $P[G_3 \mid E]$. (d) $P[E \mid G_3]$.

### (a) $P[R_3 \mid G_1]$

$G_1$ = roll in $\{2,3,4,5,6\}$, prob $5/6$.

$R_3 \cap G_1 = R_3$ (since $3 > 1$), prob $1/6$.

$$P[R_3 \mid G_1] = \frac{1/6}{5/6} = 1/5.$$

### (b) $P[R_6 \mid G_3]$

$G_3 = \{4, 5, 6\}$, prob $1/2$. $R_6 \cap G_3 = R_6$, prob $1/6$.

$$P[R_6 \mid G_3] = \frac{1/6}{1/2} = 1/3.$$

### (c) $P[G_3 \mid E]$

$E = \{2, 4, 6\}$, prob $1/2$. $G_3 \cap E = \{4, 6\}$, prob $2/6 = 1/3$.

$$P[G_3 \mid E] = \frac{1/3}{1/2} = 2/3.$$

### (d) $P[E \mid G_3]$

$G_3 = \{4, 5, 6\}$. $E \cap G_3 = \{4, 6\}$, prob $1/3$.

$$P[E \mid G_3] = \frac{1/3}{1/2} = 2/3.$$

**Answer:** $1/5, 1/3, 2/3, 2/3$.

> [!tip] **Internalize.** Conditional probability formula: count favorable outcomes within the conditioning event, divide by size of conditioning event.

---

## Problem 2 (3rd-ed 2.1.3) — Free throws (total probability)

> [!example] First free throw: prob 1/2. If made, second prob 3/4. If missed, second prob 1/4. Probability game goes to overtime (exactly 1 made)?

### Tree

- Make 1st (1/2): then make 2nd (3/4) → both made, no OT. Miss 2nd (1/4) → 1 made, OT. Branch prob: $1/2 \cdot 1/4 = 1/8$.
- Miss 1st (1/2): then make 2nd (1/4) → 1 made, OT. Miss 2nd (3/4) → 0 made, no OT. Branch prob: $1/2 \cdot 1/4 = 1/8$.

$$P[\text{OT}] = 1/8 + 1/8 = 1/4.$$

**Answer:** $P[\text{OT}] = 1/4$.

> [!tip] **Internalize.** **Tree diagram first.** Sum branch probabilities of leaves where the event of interest occurs.

---

## Problem 3 (3rd-ed 2.1.5) — Bayes for HIV test

> [!example] $P[H] = 1/5000$. Test correct 99/100 of time. Find $P[-\mid H]$ and $P[H \mid +]$.

### Decode "test correct 99% of time"

Means $P[+\mid H] = 0.99 = P[-\mid H^c]$. (Sensitivity = specificity = 0.99.)

### $P[-\mid H]$

$P[-\mid H] = 1 - P[+\mid H] = 1 - 0.99 = 0.01$.

### $P[H \mid +]$ — Bayes

$$P[H \mid +] = \frac{P[+\mid H]P[H]}{P[+\mid H]P[H] + P[+\mid H^c]P[H^c]}.$$

$P[H] = 1/5000 = 0.0002$, $P[H^c] = 0.9998$.
$P[+\mid H] = 0.99$, $P[+\mid H^c] = 0.01$.

Numerator: $0.99 \cdot 0.0002 = 0.000198$.
Denominator: $0.000198 + 0.01 \cdot 0.9998 = 0.000198 + 0.009998 = 0.010196$.

$$P[H \mid +] = \frac{0.000198}{0.010196} \approx 0.0194.$$

**Answer:** $P[-\mid H] = 0.01$. $P[H \mid +] \approx 0.0194$, i.e. about **1.94%** of positive testers actually have HIV.

> [!warning] **Gotcha — base-rate fallacy.** A 99%-accurate test on a 1-in-5000 population gives a positive predictive value of only 2%. **The rare-disease prior dominates** when the false-positive rate is comparable to disease prevalence.

> [!tip] **Internalize.** Bayes intuition: **prior × likelihood / evidence.** Don't confuse $P[H \mid +]$ (what you want) with $P[+ \mid H]$ (sensitivity).

---

## Problem 4 (3rd-ed 2.2.12) — Counting basketball lineup

> [!example] 3 pure centers, 4 pure forwards, 4 pure guards, 1 swingman (can play F or G). Lineup: 1 C, 2 F, 2 G. Count lineups.

### Case-split by swingman role

**Case 1: Swingman not in lineup.** 1 center from 3, 2 forwards from 4, 2 guards from 4: $\binom{3}{1}\binom{4}{2}\binom{4}{2} = 3 \cdot 6 \cdot 6 = 108$.

**Case 2: Swingman plays forward.** Center from 3, 1 more forward from 4, 2 guards from 4: $\binom{3}{1}\binom{4}{1}\binom{4}{2} = 3 \cdot 4 \cdot 6 = 72$.

**Case 3: Swingman plays guard.** Center from 3, 2 forwards from 4, 1 more guard from 4: $\binom{3}{1}\binom{4}{2}\binom{4}{1} = 3 \cdot 6 \cdot 4 = 72$.

Total: $108 + 72 + 72 = 252$.

**Answer:** **252 possible lineups.**

> [!tip] **Internalize.** **When a flexible element exists, partition by where it goes.** Sum the disjoint cases. Don't try to "count it once" — that double-counts or under-counts.

---

## Problem 5 (3rd-ed 2.3.1) — Binary codeword (independent Bernoulli)

> [!example] 5-bit codeword, each bit 0 with prob 0.8 (independent).
> (a) $P[\text{codeword} = 00111]$. (b) $P[\text{exactly 3 ones}]$.

### (a) Specific codeword 00111

$P = 0.8 \cdot 0.8 \cdot 0.2 \cdot 0.2 \cdot 0.2 = (0.8)^2(0.2)^3 = 0.64 \cdot 0.008 = 0.00512$.

### (b) $P[\text{3 ones}]$

Number of codewords with 3 ones: $\binom{5}{3} = 10$. Each has prob $(0.2)^3 (0.8)^2 = 0.00512$:

$$P[\text{3 ones}] = 10 \cdot 0.00512 = 0.0512.$$

This is just $\text{Bin}(5, 0.2)$ at $k = 3$.

**Answer:** $P[00111] = 0.00512$. $P[\text{3 ones}] = 0.0512$.

> [!tip] **Internalize.** **Specific sequence vs. count.** $P[\text{specific 3-ones sequence}] = (0.2)^3(0.8)^2$. $P[\text{any 3-ones sequence}] = \binom{5}{3}(0.2)^3(0.8)^2$. The factor $\binom{5}{3}$ is the **binomial coefficient** counting sequences with $k$ ones.

---

## Cross-references

- **Course page:** [[eee-350]]
- **Master review:** [[eee-350-final-walkthrough]]
- **Adjacent walkthroughs:** [[eee-350-module-02-discrete-rvs-walkthrough]] (binomial in problem 5 here is the bridge).
- **Concept pages:** [[probability-axioms]], [[conditional-probability]], [[bayes-rule]], [[law-of-total-probability]], [[counting]], [[binomial-distribution]].

