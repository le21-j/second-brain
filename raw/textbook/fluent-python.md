# Fluent Python (2nd ed.) — Luciano Ramalho

**Category:** Python intermediate / advanced
**Status:** paid book — not yet in repo
**Publisher:** O'Reilly, 2022
**Roadmap phase:** return to it in Month 2; keep as reference throughout

## Topic coverage
- Data model (Python's dunder protocol — `__len__`, `__iter__`, `__getitem__`, etc.)
- Sequences (list, tuple, array, deque, memoryview)
- Dicts, sets, and Unicode (hash tables, string internals)
- Functions as objects (decorators, first-class, closures)
- Object-oriented idioms (properties, `__slots__`, dataclasses, ABCs, protocols)
- Control flow (iterators, generators, coroutines, context managers, async/await)
- Metaprogramming (descriptors, class decorators, metaclasses)

## Why it's on the roadmap
This is the book that turns a Python user into a Python fluent speaker. For wireless+ML research, you don't need every chapter, but you **do** need the data model, decorators, generators, context managers, and dataclasses chapters — these show up constantly when reading Sionna, PyTorch, and Hugging Face code.

## High-priority chapters for this roadmap
1. Ch 1 (Python Data Model) — understand the dunder protocol.
2. Ch 3 (Dictionaries and Sets) — hashability pitfalls.
3. Ch 5 (Data class builders) — `@dataclass`, `attrs`, `pydantic`.
4. Ch 7 (Functions as First-Class Objects) and Ch 9 (Decorators and Closures).
5. Ch 17 (Iterators, Generators, Classic Coroutines) — data pipelines.
6. Ch 18 (`with`, `match`, `else`) — context managers.
7. Ch 21 (Asynchronous Programming) — only if doing data-loading in anger.

## Related wiki pages
- [[python-ml-wireless]]
- [[python-crash-course]]
- [[luciano-ramalho]]
