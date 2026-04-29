---
title: Andrej Karpathy
type: person
tags: [teaching, dl, openai, tesla, nano-gpt, zero-to-hero]
course: [[python-ml-wireless]]
created: 2026-04-23
updated: 2026-04-23
---

# Andrej Karpathy

**Current:** founder of Eureka Labs (education-focused AI startup); previously Senior Director of AI at Tesla; founding member of OpenAI.
**Teaching outputs:** the single most effective DL pedagogy on the internet.

## Why he matters to Jayden

**Best-in-class teacher of deep-learning internals.** The roadmap calls his **Neural Networks: Zero to Hero** playlist and **"Let's build GPT"** video "the highest-ROI deep-learning content anywhere — do the entire playlist." There is no more efficient 20 hours of ML video anywhere.

## Required content (per the roadmap)

- **Neural Networks: Zero to Hero** — https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ. 10 videos. Watch all.
  - The `micrograd` video alone is worth 2x a textbook chapter on backprop.
  - `makemore` series progressively builds a character-level language model with every common architecture.
- **"Let's build GPT from scratch, in code, spelled out"** — https://www.youtube.com/watch?v=kCc8FmEb1nY.
- **nanoGPT** — https://github.com/karpathy/nanoGPT. The reference implementation of clean, minimal LLM training.
- **The Annotated Transformer** — http://nlp.seas.harvard.edu/annotated-transformer/ (not authored by Karpathy but he routinely recommends it).

## What to imitate in your own code

- **Minimal, flat file layout** — `nanoGPT`'s `train.py` is ~300 lines. Every production repo has this; no mystery framework magic.
- **Written as a tutorial.** Comments explain the why, not the what. Every variable name is honest.
- **Reproducibility as a first-class design goal.** Every repo shows a loss curve + one-command reproduction.

## Tone to internalize

Karpathy's pedagogy is honest about what's hard:
- "I'll keep making mistakes because this is the learning process."
- "Don't memorize; rebuild."
- "Study the gradients."

If Jayden can explain one of his own models the way Karpathy explains nanoGPT, he is ready for any research interview.

## Related
- [[transformer]]
- [[backpropagation]]
- [[autograd]]
- [[pytorch]]
- [[python-ml-wireless]]
