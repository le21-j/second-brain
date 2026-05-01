---
title: Bloom's Taxonomy
type: concept
course: []
tags: [learning-meta, study-skills, ai-tutoring, cognitive-hierarchy]
sources: [[article-2026-04-29-giles-oxford-ai-learning]], [[article-2026-04-29-sung-ai-learning-faster]]
created: 2026-04-29
updated: 2026-04-29
---

# Bloom's Taxonomy

## In one line

A six-level hierarchy of cognitive complexity used to design and evaluate learning activities — **the higher the level, the deeper the learning**. The top three (analyze, evaluate, create) is where deep understanding happens; the bottom three (remember, understand, apply) is where AI shines and human effort is increasingly low-leverage.

## Example first — the chain rule at every level

| Level | Activity | Output |
|---|---|---|
| **1. Remember** | Recite the chain rule | "$(f \circ g)' = f'(g(x)) \cdot g'(x)$" |
| **2. Understand (comprehend)** | Restate it in your own words | "Take the derivative of the outside, then multiply by the derivative of the inside" |
| **3. Apply** | Use it on a new function | $\frac{d}{dx}\sin(x^2) = \cos(x^2) \cdot 2x$ |
| **4. Analyze** | Compare with the product rule — when do you need each? | "Chain for composition $f(g(x))$; product for multiplication $f(x)\cdot g(x)$. Both can appear in the same problem — you decompose by structure" |
| **5. Evaluate** | Critique a solution: which differentiation rule fits this problem best, and why is the alternative worse? | "I'd use chain because the function is $\sin(x^2)$ — composition. Product would only apply if I rewrote as $\sin(x)\cdot\sin(x)$, which adds steps and creates a different problem" |
| **6. Create** | Construct an original problem that requires both chain and product | $\frac{d}{dx}\!\left[x^2 \sin(x^2)\right]$ — student designs, solves, and explains why the structure forces both rules |

Levels 1–3 are the **bottom 3** — what AI does well, fast, cheap. Levels 4–6 are the **top 3** — where human cognitive value concentrates and where AI is currently bad.

## The idea

Bloom's original 1956 framework (revised 2001 — Anderson & Krathwohl) ranks cognitive activities by depth. The hierarchy was originally meant for curriculum designers, but it has become the most-cited model of "what kind of thinking is this?"

The two YouTube videos that created this page both lean on Bloom's, but for different reasons:

- **[[article-2026-04-29-giles-oxford-ai-learning|Giles]]** uses it as a **practice-question generator**: ask AI to produce questions at each Bloom level so you drill the full ladder, not just memorize.
- **[[article-2026-04-29-sung-ai-learning-faster|Sung]]** uses it as a **gating decision**: bottom 3 → fair game for AI; top 3 → don't offload, get better at them yourself.

The two framings are complementary. *You* practice the top 3; you let *AI* drill you on the bottom 3.

## Formal definition

| Level | Original verb (1956) | Revised verb (2001) | Cognitive process |
|---|---|---|---|
| 1 | Knowledge | **Remember** | Recall facts, terms, basic concepts |
| 2 | Comprehension | **Understand** | Explain ideas; classify; summarize; paraphrase |
| 3 | Application | **Apply** | Use information in new situations; execute, implement |
| 4 | Analysis | **Analyze** | Break into parts; identify relationships; compare/contrast |
| 5 | Synthesis | **Evaluate** | Judge value; defend opinions; critique; prioritize |
| 6 | Evaluation | **Create** | Combine elements into new patterns; design; construct novel |

(The 2001 revision swapped synthesis and evaluation, making "create" the apex.)

## The Sung gating rule (the actionable version)

```
6. CREATE      ← do these yourself; AI is bad at them
5. EVALUATE    ← do these yourself; AI is bad at them
4. ANALYZE     ← do these yourself; AI is bad at them
─────────────────── the AI / human boundary ───
3. APPLY       ← AI is fine for these
2. UNDERSTAND  ← AI is fine for these
1. REMEMBER    ← AI is fine for these
```

When you find yourself studying, ask: *what level of thinking is this requiring of me?*

- If you're trying to **memorize** a formula → Bloom 1 → don't waste time; AI can recall this faster than you ever will. Use the formula sheet, link to [[formulas]] page, move on.
- If you're trying to **understand** a paragraph → Bloom 2 → AI can paraphrase. Don't dwell.
- If you're **applying** a known technique to a textbook problem → Bloom 3 → fine to use AI for help, but mostly to verify your attempt.
- If you're **comparing** two concepts and figuring out which fits a context → Bloom 4. *Don't ask AI which to use.* Work it out.
- If you're **evaluating** trade-offs in a design → Bloom 5. AI's "balanced view" is mush. Form your own.
- If you're **creating** something — a paper, a project, a novel solution → Bloom 6. AI's output here is consistently the worst. This is your job.

## Why it matters / when you use it

- **As a study-activity classifier.** Before doing 30 minutes of "studying," ask: *what Bloom level am I working at?* If the answer is 1–2, the activity is low-yield; up-level it.
- **As a practice-set difficulty ladder.** When generating practice problems (with AI or alone), explicitly tag each problem with its Bloom level. The wiki's `wiki/practice/` schema benefits from this.
- **As an AI-offload boundary.** This is the explicit operating rule of the [[teacher]] sub-agent — refuse to do top-3 work on the user's behalf.
- **As a career signal.** Sung's argument: jobs increasingly pay for top-3 work. Spending years building expertise that lives at level 3 (applying well-understood techniques to standard problems) is a career-fragility risk.

## Common mistakes

- **Confusing Bloom level 1 (memorize the *process*) with the outcome of *retention***. The process of trying-to-memorize doesn't reliably produce retention. Retention comes from analyze/evaluate/create work, where the information sticks because it's been *used*. (Sung's clearest argument.)
- **Treating Bloom 2 ("understand") as a process you can do.** You don't *do* understanding directly — you do analyze/evaluate/create work, and understanding emerges as a side-effect.
- **Stopping at Bloom 3 (apply) once you can solve textbook problems.** Most undergraduates plateau here. The students who differentiate themselves climb to 4–6.
- **Assigning AI a top-3 task and trusting the output.** AI's analyze/evaluate/create output is fluent and confident-sounding but typically of lower quality than a skilled human's. Use it as a sounding board, never as the answer.

## Related

- [[retrieval-practice]] — orthogonal to Bloom's; you can retrieve at any level. A retrieval-practice question can target Bloom 4 ("compare X and Y from memory") just as easily as Bloom 1.
- [[ai-learning-risk-complexity]] — Sung's other framework. The two compose: high complexity *and* top-3 cognition both push toward "do this yourself."
- [[teacher]] sub-agent — operationalizes the gating rule by escalating questions through the top three levels and refusing to perform them on the user's behalf.

## How to apply this week

For Exam 2 prep (Thursday 4/30):

- **Stop drilling memorization** of the formula sheet. The cheat sheet handles Bloom 1.
- **Drill analyze-level comparisons:** "Why does this problem call for FFT vs direct DFT? Why ROC matters here but not there? Why ReLU vs Sigmoid for this hidden layer?"
- **Drill evaluate-level judgment:** "Among Direct Form I, II, transposed — which would I implement on the STM32 and why?"
- **Drill create-level synthesis:** Take Exam 2 Practice P2 — given the same $H(z)$, design a *different* difference equation that produces the same impulse response (impossible — and figuring out why teaches the uniqueness of the transform).
