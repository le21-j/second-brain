---
title: Generalization — Mistakes
type: mistake
course:
  - "[[python-ml-wireless]]"
tags:
  - mistakes
  - generalization
  - deep-learning
  - zhang-2017
concept:
  - "[[overfitting-bias-variance]]"
  - "[[regularization]]"
created: 2026-05-01
updated: 2026-05-01
---

# Generalization — Common Mistakes

Mistakes that surface when reasoning about *what makes a model "understand" rather than memorize* — the train-test gap, the difference between fitting and generalization, and the structural property of data that makes generalization possible. Anchored to the Zhang et al. 2017 random-labels experiment.

## Known gotchas (general)

- **"High training accuracy means the model understood the data."** Modern over-parameterized networks have enough capacity to memorize *anything*, including labels that are pure noise. Zhang et al. 2017 trained a standard CNN to $\sim 100\%$ training accuracy on MNIST with **randomly shuffled labels** — and the network learned them perfectly. Training accuracy alone tells you nothing about whether the network extracted any structure from the data; it tells you only whether the network's capacity was large enough to fit the empirical training pairs. **The diagnostic is the gap between training accuracy and test accuracy on data drawn from the same distribution, conditional on the model having fit the training set.** Train error is a fitting metric, not a generalization metric.

- **"Random-label test accuracy is 0%."** On a balanced $K$-class problem, predictions that are *uncorrelated* with the truth produce chance-level accuracy ($1/K$), not zero. Memorization of random training labels produces uncorrelated test predictions — the network has no information about the test images' true labels because the training labels were noise, so its outputs on test images are essentially random draws from the empirical label distribution. **To get $0\%$ accuracy, the network would have to be *anti-correlated* — it would need to *know* the correct label and systematically output anything but that.** That's informationally equivalent to perfect classification with a fixed label permutation, not random-label memorization. Distinguish *uncorrelated* (chance) from *anti-correlated* (zero) before reasoning about random-label outcomes.

## Jayden's personal log

- `2026-05-01` — *Predicted the Zhang 2017 random-labels six-number table in a 6-turn Socratic session.* See [[practice/generalization-set-01]] for the full attempt log. Got the load-bearing prediction right (S2 train $\sim 100\%$ — networks fit random labels just as well as real ones) without having read the paper. Got S2 test wrong: said $\sim 0\%$, actual is $\sim 10\%$ (chance level on a balanced 10-class problem). **Lesson: distinguish *uncorrelated* (gives chance, $1/K$) from *anti-correlated* (gives $0\%$). Memorization of random training pairs produces uncorrelated test predictions, never anti-correlated ones.** Articulated the difference cleanly once prompted: anti-correlation requires the network to "know the correct answer and output anything but that," which is qualitatively a different relationship between the network's output and the truth than mere ignorance. Also sharpened the diagnostic from "test accuracy" to "**the gap, train minus test, conditional on fitting**" — and learned the formal name for the property of structured data: **mutual information** $I(X; Y) > 0$ on the data-generating distribution, vs. $I(X; Y) = 0$ for random-label data. The synthesis was that the Zhang result is a *falsifiability test*: if the network's mechanism on real data were "just memorize," it would behave identically in both scenarios; the fact that it doesn't is empirical evidence the network is doing something more than memorization on structured data.

## Related

- [[practice/generalization-set-01]] — the practice problem this log was produced from
- [[overfitting-bias-variance]] — the classical decomposition that Zhang 2017 refined
- [[regularization]] — the umbrella for techniques that close the gap
- [[python-ml-wireless]] — Phase 1–2 foundations
