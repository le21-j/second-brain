---
title: SARSA
type: concept
course:
  - "[[python-ml-wireless]]"
tags:
  - rl
  - on-policy
  - tabular
  - bellman
  - phase-3
sources:
  - "[[textbook-sutton-barto-rl]]"
created: 2026-05-01
updated: 2026-05-01
---

# SARSA

## In one line
**SARSA is the on-policy TD analogue of [[q-learning]]: it updates $Q(s,a)$ toward the actual next action's value, not the optimal one.** Safer than Q-learning when exploration is dangerous; named after the 5-tuple $(s, a, r, s', a')$ used in each update.

## Example first

**Cliff-walking ([[textbook-sutton-barto-rl]] Ex 6.6).** A grid where the bottom row is a cliff (reward $-100$, return to start). Goal is bottom-right.

- **Q-learning** finds the **optimal** path — walks right along the cliff edge, but with $\epsilon$-greedy exploration occasionally falls off → high variance reward.
- **SARSA** learns a **safer** path one step away from the cliff — its updates account for the actual exploratory $a'$, so it learns the cliff is risky **with the current behavior policy**.

Same Q-table size, same learning rate, **different update rule** → different policy.

## The idea

SARSA's update uses the **actually-chosen** next action $a'$ from the behavior policy:

$$Q(s,a) \leftarrow Q(s,a) + \alpha\bigl[r + \gamma Q(s', a') - Q(s,a)\bigr]$$

Compare to Q-learning's $\max_{a'} Q(s',a')$. SARSA evaluates the policy it's executing; Q-learning evaluates a different (greedy) policy.

## Why it matters / when you use it

- **Sutton-Barto Ch 6** — paired with [[q-learning]] as the on-policy/off-policy contrast.
- **Wireless safety-critical setting.** When the cost of catastrophic actions is high (e.g., dropping a call to learn power-control limits), on-policy methods like SARSA reduce risk during training.

## Common mistakes
- **Confusing on-policy with online.** SARSA is *on-policy*: target uses the behavior policy's action. Online means updated per-step (both Q-learning and SARSA do this).
- **Comparing SARSA / Q-learning at the same $\epsilon$** without noting that the optimal policies differ when exploration is irreversible.

## Related
- [[q-learning]] — off-policy cousin.
- [[reinforcement-learning]]
- [[textbook-sutton-barto-rl]] — Ch 6.
- [[python-ml-wireless]]
