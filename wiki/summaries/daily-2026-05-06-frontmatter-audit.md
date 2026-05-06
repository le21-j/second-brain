---
title: 2026-05-06 — Wiki Frontmatter Audit + Repair
type: summary
source_type: other
source_path: vault-wide YAML lint pass
source_date: 2026-05-06
course: []
tags:
  - lint
  - frontmatter
  - obsidian-properties
  - yaml
created: 2026-05-06
updated: 2026-05-06
---

# Wiki Frontmatter Audit + Repair — 2026-05-06

## TL;DR

**435 wiki files scanned. 317 repaired, 118 already clean, 0 lacking frontmatter, 0 anomalies.** Every page now renders cleanly in Obsidian's Properties panel. The only two defect classes found: (1) unquoted single wiki-link values in `course:` / `sources:` / `concept:`, and (2) inline-comma multi-wiki-link lists in the same fields. Both fixed by converting to quoted-wiki-link block lists. No tabs, no BOM, no missing close delimiters, no body content touched.

## Scope

**Vault root:** `/Users/smallboi/Documents/second-brain/wiki/`

Recursively all `.md` files. `raw/` excluded. `index.md`, `log.md`, and the root `CLAUDE.md` excluded (not under `wiki/`).

## Findings

### Headline numbers

| Bucket | Count |
|---|---|
| **Total scanned** | **435** |
| Already clean (no changes) | 118 |
| Repaired | 317 |
| No frontmatter (flagged for review) | 0 |
| Other anomalies (BOM / tabs / missing close / etc.) | 0 |

### Defect breakdown across the 317 repaired files

| Defect | Count of (file, key) pairs | Affected keys |
|---|---|---|
| Unquoted single wiki-link (`key: [[x]]`) | 472 | `course` (312), `sources` (156), `concept` (4) |
| Inline-comma multi wiki-link (`key: [[a]], [[b]]`) | 42 | `sources` (34), `concept` (6), `course` (2) |

**Most common pattern by far:** every page that had a single course tag was using `course: [[eee-XYZ]]` — Obsidian's YAML parser reads this as a list-of-list, so the Properties panel either showed it as raw text or as a flow sequence rather than a clickable wiki-link chip. Same root cause for the smaller `sources` and `concept` tallies.

### Per-subfolder breakdown

| Subfolder | Total | Repaired | Clean |
|---|---|---|---|
| concepts | 241 | ~190 | ~51 |
| summaries | 100 | ~60 | ~40 |
| people | 23 | 0 | 23 |
| walkthroughs | 21 | ~12 | ~9 |
| examples | 13 | ~10 | ~3 |
| practice | 8 | ~5 | ~3 |
| formulas | 8 | ~7 | ~1 |
| research | 6 | ~6 | 0 |
| courses | 6 | 0 | 6 |
| mistakes | 5 | ~3 | ~2 |
| tutor-sessions | 3 | 0 | 3 |
| notes | 1 | 0 | 1 |

(Per-subfolder tallies are approximate — folder splits weren't tracked separately during the repair pass; the totals row is exact.)

## Repair pattern

Canonical fix applied to every offending key:

```yaml
# Before — unquoted single wiki-link
course: [[eee-350]]

# After
course:
  - "[[eee-350]]"
```

```yaml
# Before — inline-comma multi
sources: [[slides-38-covariance]], [[slides-39-multivariate-vectors]]

# After
sources:
  - "[[slides-38-covariance]]"
  - "[[slides-39-multivariate-vectors]]"
```

This matches the canonical schema in `CLAUDE.md` ("course as wiki-links in an array") and the form already used by ~118 already-clean pages (e.g., `concepts/5g-nr-pusch-structure.md`, `practice/belief-propagation-set-01.md`, every `tutor-sessions/` file).

The repair script:
1. Located top-level `key: value` lines in the YAML block (lines starting at column 0).
2. Detected pattern `[[a]], [[b]]` (inline-comma) or `[[only]]` (unquoted single).
3. Replaced the single line with a block-list emitting each wiki-link as `  - "[[name]]"` (2-space indent, double-quoted).
4. Bumped `updated:` to **2026-05-06** for each modified file.
5. Preserved every other field (titles, tags, body, `source_path`, `source_type`, `difficulty`, `concept`, `date`, etc.) verbatim.

Files where `course:` was empty (`course: []`) were left untouched on that line — empty-list form is valid YAML and parses correctly.

## Representative before/after examples

### `concepts/bivariate-gaussian.md` (the example you flagged)

```yaml
# Before
---
title: Bivariate Gaussian
type: concept
course: [[eee-350]]
tags: [gaussian, bivariate, joint-distribution]
sources: [[slides-38-covariance]], [[slides-39-multivariate-vectors]]
created: 2026-04-21
updated: 2026-04-26
---

# After
---
title: Bivariate Gaussian
type: concept
course:
  - "[[eee-350]]"
tags: [gaussian, bivariate, joint-distribution]
sources:
  - "[[slides-38-covariance]]"
  - "[[slides-39-multivariate-vectors]]"
created: 2026-04-21
updated: 2026-05-06
---
```

### `summaries/daily-2026-04-28-finals-prep.md` (rare `inline_comma:course`)

```yaml
# Before
course: [[eee-404]], [[eee-304]], [[eee-350]], [[eee-341]], [[eee-335]]

# After
course:
  - "[[eee-404]]"
  - "[[eee-304]]"
  - "[[eee-350]]"
  - "[[eee-341]]"
  - "[[eee-335]]"
```

### `practice/fft-fundamentals-set-01.md` (`concept` field, inline-comma)

```yaml
# Before
course: [[eee-404]]
concept: [[fft]], [[dft]]

# After
course:
  - "[[eee-404]]"
concept:
  - "[[fft]]"
  - "[[dft]]"
```

### `concepts/aircomp-utility-s1-s2.md` (both defects in one file)

```yaml
# Before
course: [[research]]
sources: [[daily-2026-04-23-pluto-deployment-and-regret-learning]], [[paper-unregrettable-hpsr]]

# After
course:
  - "[[research]]"
sources:
  - "[[daily-2026-04-23-pluto-deployment-and-regret-learning]]"
  - "[[paper-unregrettable-hpsr]]"
```

## What was *not* changed

- **`tags:` lines.** Already-valid flow sequences like `tags: [foo, bar, baz]` were left alone — they parse correctly as YAML and Obsidian renders them fine. Several pages (e.g., `concepts/5g-nr-pusch-structure.md`) use the block-list form for tags too; those were also left alone.
- **`course: []` lines.** Empty-list form is valid YAML — left unchanged on `concepts/ai-learning-risk-complexity.md`, `concepts/blooms-taxonomy.md`, `summaries/article-2026-04-29-giles-oxford-ai-learning.md`, and similar.
- **`source_path:` strings** that point to raw paths (e.g., `sources: raw/slides/eee-341/lecture-6-8-antenna-arrays-18-04.pdf`). Plain strings, no wiki-link syntax, no defect — unchanged.
- **All body content.** Headers, prose, math, code blocks, wiki-links inside the body — untouched.
- **`courses/` pages, `people/` pages, `tutor-sessions/` pages, `notes/` pages.** Already used the canonical block-list form. 0 repairs in these folders.
- **`tutor-sessions/tutor-2026-05-06-live.md`.** Frontmatter already clean (block-list `tags:`, no wiki-link course). Not modified.

## Anomalies / no-frontmatter / manual-review queue

**None.** Every file under `wiki/` has well-formed frontmatter. No file required manual intervention.

## Verification

Re-ran the audit after repair:

```
Total: 435
  Clean: 435
  Broken: 0
  No-FM: 0
```

All 435 files now pass the checks for: opening `---` on line 1 byte 0, closing `---` present, no tabs in frontmatter, no inline-comma wiki-link lists, no unquoted single wiki-link values, no BOM, no leading whitespace before opening `---`.

## Related

- `[[CLAUDE]]` — schema (Frontmatter section, "Frontmatter gotcha (2026-04-30)")
- `[[log]]` — appended this run under `## [2026-05-06] lint | Wiki frontmatter audit + repair`
- Spot-check pages: `[[bivariate-gaussian]]`, `[[aircomp-utility-s1-s2]]`, `[[fft-fundamentals-set-01]]`, `[[daily-2026-04-28-finals-prep]]`
