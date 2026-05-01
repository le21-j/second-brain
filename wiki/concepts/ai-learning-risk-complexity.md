---
title: AI-Learning Risk vs. Complexity
type: concept
course: []
tags: [learning-meta, ai-tutoring, study-skills, llm-limitations]
sources: [[article-2026-04-29-sung-ai-learning-faster]]
created: 2026-04-29
updated: 2026-04-29
---

# AI-Learning Risk vs. Complexity

## In one line

As topic complexity rises, LLM accuracy falls and the **risk of compounding 10% errors** in your understanding rises sharply — so make the *should I use AI for this* decision **upfront**, before sinking hours into AI-assisted study of something AI is fundamentally bad at.

## Example first — two questions, two zones

**Question A:** *"What's the formula for variance of a Bernoulli random variable?"*

- **Topic complexity:** very low. Single right answer, well-established, in every textbook the same way.
- **LLM accuracy:** ~100%. Hundreds of thousands of training examples agree on $p(1-p)$.
- **Risk of using AI:** essentially zero.
- **Verdict:** **Use AI freely.** It'll save you a lookup. The 5 seconds you save matter; the 0% chance of compounding error doesn't bother you.

**Question B:** *"What's the current state of the art in 2026 for neural-receiver design under realistic 5G NR pilot patterns, and which approach should I prioritize for my Phase 3 reproduction?"*

- **Topic complexity:** very high. Active research area; multiple competing groups (Hoydis at NVIDIA; Aït Aoudia; Cammerer; O'Shea); methodology disputes; benchmark choices contested.
- **LLM accuracy:** maybe 80–90%, but with 10–20% subtle errors that *sound exactly like the correct version* — wrong author, slightly-off architecture detail, conflated paper, outdated baseline. You won't know which 10% is wrong.
- **Risk of using AI:** **high and silent.** You'll build a research plan on a 10% incorrect foundation. The error compounds — wrong baseline → wrong comparison → wrong conclusion → wasted reproduction.
- **Verdict:** **Don't ask AI.** Read the original papers. Use AI only for low-complexity sub-questions ("how do I instantiate this Sionna block?") that arise during the reading.

The two questions feel similar (both are "research questions"). The risk profiles are completely different.

## The idea

LLMs (Claude, ChatGPT, Gemini, etc.) use the **transformer architecture** — at heart, they're probability-based word generators. Each output word is the most-probable next word given training data and your prompt. They have no concept of truth; they generate text that *sounds* like truth.

Two consequences:

1. **They cannot validate or prioritize sources.** When they "search the internet," they're folding in more text — but they have no machinery for "is this Reddit comment more or less reliable than this peer-reviewed paper?"
2. **They produce fluent, coherent text by design** — and humans interpret fluent+coherent text as correct. This is why hallucinations are dangerous: they *sound* right.

This is **not solvable** with the current architecture. It will not be fixed by GPT-5 or Claude 5 or larger context windows. It would require a new architectural breakthrough on the scale of "LLMs themselves were a breakthrough." That's years away, possibly decades.

So you don't try to make the LLM accurate on hard topics. You **route around the limitation**.

## Formal definition — Sung's two graphs

```
Risk of using LLM
       ▲
       │                                   ╱
       │                              ╱
       │                        ╱
       │                  ╱
       │            ╱
       │      ╱
       │ ╱
       └────────────────────────────────────►
       low                              high   Topic complexity

Usefulness of LLM
       ▲
       │ ╲
       │   ╲
       │     ╲
       │       ╲
       │         ╲
       │           ╲
       │             ╲
       │               ╲___________________
       └────────────────────────────────────►
       low                              high   Topic complexity
```

These are intuition curves, not measurements — but they capture the trade-off Sung argues you should *make explicitly* before each use.

### What "complexity" means here

- **Many moving parts.** Lots of interacting variables, sub-systems, edge cases.
- **Evolving information.** Active research front; consensus shifts year-to-year.
- **Competing opinions.** Multiple valid frameworks; differing schools of thought.
- **Lack of consensus.** No single authoritative answer.
- **Context-specific application.** General principle, but its application depends heavily on factors specific to the user's situation.

### What "low complexity" looks like

- Well-established textbook material.
- Single agreed-upon answer.
- Application is direct (one-to-one mapping from concept to use case).
- The application doesn't depend strongly on context.

## Why it matters / when you use it

**Make the gating decision upfront.** The mistake Sung sees most often: people don't classify the topic before starting. They spend 30 min, 2 hours, 3 weeks studying with AI on something AI is fundamentally bad at, and only realize at the end (or never realize) that the foundation was inaccurate.

The decision takes 15 seconds. *Is this topic well-understood and stable, or evolving and contested?* If contested → don't ask AI for the answer; ask AI for *help reading the source* (e.g., proposition extraction, key-term lists — see [[article-2026-04-29-giles-oxford-ai-learning|Giles' video]]). If stable → use AI freely as a tutor, drill partner, and lookup tool.

**The 80/90 rule.** *80–90% of people, 80–90% of the time, only need superficial knowledge of any given topic.* That's the LLM-friendly zone. Don't over-engineer your AI use for the 10% case unless your role specifically demands expert-level depth.

**Career relevance for Jayden specifically.** The [[python-ml-wireless]] roadmap has both modes:

| Phase activity | Complexity | AI's role |
|---|---|---|
| Reproducing a paper (Phase 3 M7 neural receiver) | Mostly low — the paper is the spec | Heavy AI use is fine — debugging, code generation, drilling |
| Choosing *which* paper to reproduce | High — strategic, judgment-laden | Don't ask AI to decide; read the [[python-ml-wireless]] page, ask Jayden's intuition, ask a human mentor |
| Implementing a Sionna block | Low to medium — well-documented API | AI is a great pair-programmer |
| Designing an *original* extension to an LWM | Very high — research-frontier | Do not let AI be the architect. Use AI for code, read the original Wi-Lab papers for the design |

## Common mistakes

- **Treating an LLM as an authority on a contested topic.** It will produce a confident, coherent answer that's wrong in subtle ways. You'll trust it because it sounds careful.
- **Spending hours building a knowledge base on AI-generated content** for a high-complexity topic. The 10% error compounds; you'll have to redo the work later, and worse — the wrong foundation will mislead your judgment in the meantime.
- **Confusing "AI got the simple part right, so it must be right about the hard part too."** AI is *especially* prone to bait-and-switch — opening a response with correct boilerplate to establish credibility, then subtly drifting into wrong territory.
- **"I'll just verify it later."** You won't. Verifying takes nearly as long as not using AI in the first place. Make the gating decision upfront, not after the fact.
- **Asking AI which approach is best when "best" depends on contested values.** AI gives you an averaged-opinion mush. *You* have priorities; *AI* doesn't. Make the call yourself.

## Related

- [[blooms-taxonomy]] — Sung's other framework. The two compose: **high topic complexity *and* top-3 Bloom levels** are the strongest "do this yourself" signal.
- [[retrieval-practice]] — works best on stable, low-complexity topics where there *is* a knowable answer to retrieve. On high-complexity topics, retrieval becomes "what did the source claim" rather than "what's true."
- [[teacher]] sub-agent — operationalizes the risk-vs-complexity gate (Operating Rule 2): refuses to be the authority on high-complexity questions, points to original sources instead.

## How to apply this week

Before any AI-assisted study session, run a 15-second classification:

| If your question is… | Then… |
|---|---|
| "What's the formula / definition / standard procedure for X?" | **Use AI freely.** Low complexity. |
| "How do I implement / debug / set up X?" | **Use AI freely.** Low-to-medium complexity, well-documented. |
| "How do I solve this textbook-style problem in a course I'm taking?" | **Use AI as a Socratic drill partner**, not an answer-giver — see [[teacher]]. Medium complexity but stable. |
| "What's the best approach to X among several competing methods?" | **Don't ask AI.** Read the canonical sources. Form your own view. High complexity. |
| "What's the SOTA for X in 2026?" | **Don't ask AI.** Go to arXiv, recent surveys, the relevant lab's GitHub. Very high risk of confidently-wrong AI output on bleeding-edge topics. |
