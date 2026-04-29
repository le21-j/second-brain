---
title: Asymptotics — Practice Set 01
type: practice
course: [[eee-350]]
tags: [practice, chebyshev, lln, clt]
concept: [[central-limit-theorem]], [[weak-law-of-large-numbers]]
difficulty: mixed
created: 2026-04-21
updated: 2026-04-26
---

# Asymptotics — Practice Set 01

**Scope:** decks 41–43. Chebyshev, convergence in probability, WLLN, CLT, binomial approximation. Attempt before peeking.

---

### 1. Chebyshev's bound [easy]
A RV has mean 50 and std 5. Give an upper bound on $P(|X - 50| \geq 20)$ using Chebyshev.

<details><summary>Solution</summary>

$P(|X - 50| \geq 20) = P(|X - 50| \geq 4\sigma) \leq 1/4^2 =$ **$1/16 \approx 0.0625$**.

For a Gaussian: actual $\approx 6.3\cdot 10^{-5}$. Chebyshev is loose but universal.

See [[chebyshev-inequality]].

</details>

---

### 2. Convergence in probability [easy–medium]
Let $X_n$ have $E[X_n] = 5 + 1/n$ and $\text{Var}(X_n) = 10/n$. Does $X_n$ converge in probability? If so, to what?

<details><summary>Solution</summary>

- $E[X_n] \to 5$ as $n \to \infty$.
- $\text{Var}(X_n) \to 0$ as $n \to \infty$.

By Chebyshev, $P(|X_n - E[X_n]| \geq \varepsilon) \leq (10/n)/\varepsilon^2 \to 0$. And $E[X_n] \to 5$.

So $X_n \to$ **5 in probability**.

See [[convergence-in-probability]], [[chebyshev-inequality]].

</details>

---

### 3. WLLN proof sketch [medium]
State why $\bar X_n \to \mu$ in probability when $X_i$ are i.i.d. with finite variance $\sigma^2$. Write a 2-line proof.

<details><summary>Solution</summary>

- $E[\bar X_n] = \mu$. $\text{Var}(\bar X_n) = \sigma^2/n$.
- By Chebyshev: $P(|\bar X_n - \mu| \geq \varepsilon) \leq \sigma^2/(n\varepsilon^2) \to 0$.

That's convergence in probability.

See [[weak-law-of-large-numbers]].

</details>

---

### 4. CLT direct application [medium]
$X_i$ i.i.d. with $\mu = 10$, $\sigma^2 = 4$. Use CLT to approximate $P(\bar X_{100} > 10.3)$.

<details><summary>Solution</summary>

$\bar X_{100} \approx N(10, 0.04)$. So:
$$P(\bar X_{100} > 10.3) \approx P\!\left(Z > \frac{10.3 - 10}{0.2}\right) = P(Z > 1.5) = 1 - \Phi(1.5) \approx 0.067$$

See [[central-limit-theorem]].

</details>

---

### 5. CLT + continuity correction [medium]
$\text{Binomial}(n = 100, p = 0.5)$. Find $P(X \geq 60)$ using normal approximation with continuity correction.

<details><summary>Solution</summary>

$X \approx N(50, 25)$, $\sigma = 5$.

With continuity correction: $P(X \geq 60) \approx P(Z \geq (59.5 - 50)/5) = P(Z \geq 1.9) =$ **$1 - \Phi(1.9) \approx 0.0287$**.

(Exact Binomial: $\approx 0.0284$. Near-perfect.)

Without continuity correction: $P(Z \geq 2) = 0.023$ — 5% off.

See [[binomial-via-clt]], [[continuity-correction]].

</details>

---

### 6. Polling sample size via CLT [medium]
How many voters do you need to poll to estimate $p$ within 2 percentage points with 99% confidence, worst-case?

<details><summary>Solution</summary>

$$n = \left(\frac{z_{0.005}}{\varepsilon}\right)^2\cdot p(1-p) \le \left(\frac{2.576}{0.02}\right)^2\cdot 0.25 = (128.8)^2 \cdot 0.25 \approx 4147$$

So **$n \approx 4150$**.

See [[polling-sample-size]].

</details>

---

### 7. Chebyshev vs. CLT [hard]
For $\text{Binomial}(n = 100, p = 0.5)$, give both a Chebyshev upper bound and a CLT approximation of $P(|X - 50| \geq 15)$. Compare.

<details><summary>Solution</summary>

$\text{Var}(X) = np(1-p) = 25$. $\sigma = 5$.

**Chebyshev:** $P(|X - 50| \geq 15) \leq 25/225 =$ **$1/9 \approx 0.111$**.

**CLT:** $|X - 50|/5 > 3$, so $\approx 2\cdot(1 - \Phi(3)) \approx$ **0.0027**.

Chebyshev overestimates by **$\sim 40\times$** here.

See [[chebyshev-inequality]], [[central-limit-theorem]].

</details>

---

### 8. Spot the LLN misuse [easy]
"I flipped 10 heads in a row on a fair coin. By the Law of Large Numbers, tails is more likely on the next flip." Is this right? Explain in one sentence.

<details><summary>Solution</summary>

**Wrong.** This is the [[gamblers-fallacy]]. WLLN says long-run **averages** stabilize around 0.5 — it says nothing about the next flip, which is still 50/50 by independence.

</details>

---

## Your attempts

_(Log attempts, date, what you missed, pattern to remember.)_
