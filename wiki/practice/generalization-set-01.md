---
title: "Generalization — Practice Set 01: Random vs structured labels"
type: practice
course:
  - "[[python-ml-wireless]]"
tags:
  - practice
  - generalization
  - deep-learning
  - zhang-2017
concept:
  - "[[overfitting-bias-variance]]"
  - "[[regularization]]"
  - "[[cross-entropy-loss]]"
difficulty: hard
created: 2026-05-01
updated: 2026-05-01
---

# Generalization — Practice Set 01: Random vs structured labels

> Attempt before scrolling. This set is the synthesis output of a Socratic session on *what makes ML "understand" rather than memorize.* The headline experiment is Zhang et al. 2017 — the result that opened the modern study of generalization in deep learning. The mistake log this set produced is at [[mistakes/generalization]].

## Problems

### 1. Hard — Zhang 2017 random-labels prediction

You take a standard CNN (say, ResNet-18) with sufficient capacity to perfectly fit MNIST. You train it twice, both runs to convergence ($\sim 100\%$ training accuracy):

- **Scenario 1 — structured:** train on the real MNIST training set (60K images, correct labels in $\{0, 1, \ldots, 9\}$). Evaluate on the held-out MNIST test set (10K images, correct labels).
- **Scenario 2 — random:** before training, take the *same* 60K MNIST training images but **randomly shuffle every label** independently. The label of each image is now a uniform draw from $\{0, 1, \ldots, 9\}$. Train to convergence on this shuffled set. Evaluate on the original MNIST test set (real labels).

Predict the following six numbers, each as a percent. For each, write one sentence justifying your prediction:

| | Scenario 1 (structured) | Scenario 2 (random) |
|---|---|---|
| Training accuracy | ? | ? |
| Test accuracy | ? | ? |
| Gap (train − test) | ? | ? |

Then answer:

- **(b)** What is the diagnostic that separates "the network learned" from "the network memorized"? Why is *test accuracy alone* insufficient as a diagnostic in general?
- **(c)** What mathematical property does the structured data have on its data-generating distribution that the random-label data lacks? Name the formal quantity.

<details><summary>Solution</summary>

#### The six numbers

| | Scenario 1 (structured) | Scenario 2 (random) |
|---|---|---|
| Training accuracy | $\sim 100\%$ | $\sim 100\%$ |
| Test accuracy | $\sim 99\%$ | $\sim 10\%$ |
| Gap (train − test) | $\sim 1\%$ | $\sim 90\%$ |

#### Interpretation

**Training accuracy in both scenarios reaches $\sim 100\%$.** This is the load-bearing Zhang 2017 finding. Modern over-parameterized networks have enough capacity to memorize the empirical training pairs in *either* case — they do not need the labels to be structured to fit them. Capacity is what determines fittability; structure is what determines transfer.

**Scenario 1 test accuracy $\sim 99\%$.** Real MNIST is a well-structured dataset; the function $f^*: \text{image} \to \text{digit}$ exists, the network estimates it well from 60K samples, and the estimate transfers to held-out images drawn from the same distribution.

**Scenario 2 test accuracy $\sim 10\%$ (NOT $0\%$).** This is chance level on a balanced 10-class problem ($1/K = 1/10$). The network's predictions on test images are uncorrelated with the truth — *not* anti-correlated. To get $0\%$, the network would have to *know* the right answer and systematically avoid it, which is informationally identical to perfect classification with a label permutation. Memorization of random training pairs produces uncorrelated test predictions, so chance.

**Gap $\sim 90\%$ in Scenario 2.** This is the diagnostic signature of memorization without learning: high training accuracy, chance test accuracy, large gap.

#### (b) The diagnostic

**The diagnostic is the gap, train accuracy − test accuracy, given high training accuracy.** Test accuracy alone is insufficient because a network with $40\%$ training accuracy and $40\%$ test accuracy has a small gap but didn't generalize — it failed to *fit* in the first place; there's nothing to transfer. Generalization is the question "did the fit transfer?" — which only makes sense once the network has fit the data. So the proper diagnostic is **the gap, conditional on fitting.** In the Zhang setup, training accuracy is pinned at $\sim 100\%$ in both scenarios, so the gap reduces to a comparison of test accuracies — but that's a special case, not the general rule.

#### (c) The mathematical property

**Mutual information** between inputs and labels on the data-generating distribution:

$$I(X; Y) = \mathbb{E}_{X,Y}\!\left[\log \frac{P(X, Y)}{P(X)\, P(Y)}\right]$$

- **Structured data:** $I(X; Y) > 0$ on the data-generating distribution. There exists a function $f^*: \mathcal{X} \to \mathcal{Y}$ such that $P(Y \mid X)$ is non-uniform, and crucially the same distribution governs train and test (i.i.d. assumption). Finite samples can estimate $f^*$, and the estimate transfers.
- **Random-label data:** $I(X; Y) = 0$. Labels are independent of inputs on the data-generating distribution. The network can still memorize the *empirical* training pairs $(x_i, \tilde y_i)$ — but those pairs do not appear at test time, and the underlying $P(Y \mid X) = 1/K$ has nothing to extract.

The same architecture, trained with the same algorithm, produces dramatically different test behavior in the two scenarios — purely because of the mutual-information structure of the labeling, not the mechanism of training. This is the empirical evidence that, on structured data, neural networks are doing something more than memorization: they're estimating $P(Y \mid X)$.

#### Connection to bias-variance

This experiment is exactly the failure mode that the bias-variance decomposition (see [[overfitting-bias-variance]]) warns about. High-capacity models can drive training error to zero while test error stays arbitrarily high. Zhang 2017's contribution was demonstrating that this failure mode is not pathological — it's available to any sufficiently-large network on any dataset, including ones with no learnable structure at all. **Train error is a fitting metric, not a generalization metric.** Generalization lives in the gap.

#### Reference

Zhang, C., Bengio, S., Hardt, M., Recht, B., Vinyals, O. (2017). *Understanding deep learning requires rethinking generalization.* ICLR 2017. arXiv:1611.03530.

</details>

## Jayden's attempts

- `2026-05-01` — **Predicted the six numbers in a 6-turn Socratic session.** What he predicted vs. what's correct:

  | | S1 train | S1 test | S1 gap | S2 train | S2 test | S2 gap |
  |---|---|---|---|---|---|---|
  | Predicted | $\sim 100\%$ | "low" (muddled) | $\sim 0\%$ | $\sim 100\%$ | $\sim 0\%$ | $\sim 100\%$ |
  | Correct | $\sim 100\%$ | $\sim 99\%$ | $\sim 1\%$ | $\sim 100\%$ | $\sim 10\%$ | $\sim 90\%$ |

  **What he got right:**
  - **S1 train ($\sim 100\%$)** — straightforward, expected.
  - **S1 gap ($\sim 0\%$)** — predicted the network would generalize on real labels.
  - **S2 train ($\sim 100\%$) — the non-obvious one.** This is the load-bearing Zhang 2017 finding: networks fit random labels just as well as real ones, given enough capacity. Predicting this correctly without having seen the paper is the moment that justifies the entire session — it means he understood that fitting and generalization are independent properties.
  - **S2 gap ($\sim 100\%$, in spirit)** — directionally right (huge gap), magnitude off because of the S2 test prediction below.

  **What he got wrong:**
  - **S1 test** — said "low" then revised to "high" mid-answer; muddled wording but the underlying intuition (real labels → good test accuracy) was right.
  - **S2 test = $0\%$.** The actual answer is $\sim 10\%$ — chance level on a balanced 10-class problem, not zero. He corrected himself in Part B of the dialogue once prompted.

  **What clicked:**
  - **The difference between *uncorrelated* (gives chance, $1/K$) and *anti-correlated* (gives $0\%$).** "For a network to get $0\%$ it would have to be anti-correlated meaning everytime it guesses something it is completely wrong, which in a sense it knows the correct answer has to output anything but that." Clean articulation, better than most graduate students.
  - **The gap as the diagnostic, not test accuracy alone.** Initially said "test accuracy of the neural network" was the diagnostic; the sharpening was that test accuracy is only sufficient when training accuracy is pinned (the Zhang setup), and the proper diagnostic is the gap conditional on fitting.
  - **Mutual information $I(X; Y)$ as the formalization of "structure."** He reached for "correlation between labels and the dataset" — directionally right, then upgraded to MI: structured data has $I(X; Y) > 0$ on the data-generating distribution; random-label data has $I(X; Y) = 0$.

## Related

- [[mistakes/generalization]] — mistake log produced by this session
- [[overfitting-bias-variance]] — the classical decomposition this experiment refines
- [[regularization]] — the umbrella for cures to the gap
- [[python-ml-wireless]] — Phase 1–2 foundations
- [[textbook-prince-understanding-deep-learning]] — Ch 8 covers generalization theory
