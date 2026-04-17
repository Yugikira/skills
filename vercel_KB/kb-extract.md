---
name: kb-extract
description: Internal helper skill that extracts concepts, theories, proxies, and methods from converted paper markdown. Called by kb-ingest, not invoked directly by user.
---

# kb-extract - Knowledge Extraction Helper

This skill is called by kb-ingest to extract structured knowledge from converted paper markdown files.

## Input Context

When invoked:
- **Paper markdown**: `raw/papers/{citekey}/{citekey}.md` (converted via paddle-pdf)
- **BibTeX metadata**: `raw/papers/{citekey}/{citekey}.bib`
- **Paper summary template**: `templates/paper_summary.md`

## Extraction Process

### Step 1: Read Paper Content

Read:
1. Converted markdown at `raw/papers/{citekey}/{citekey}.md`
2. BibTeX metadata at `raw/papers/{citekey}/{citekey}.bib`

### Step 2: Create Paper Summary

Create `source/summary/{citekey}_summary.md` using templates/paper_summary.md:

Fill in:
- YAML frontmatter from BibTeX (title, doi, citekey, authors, year, journal)
- One-Line Summary: Core contribution in one sentence
- Abstract Summary: 2-3 sentence paraphrase
- Ground Truth Findings: Raw observations without interpretation
- Claimed Findings: Authors' interpretations
- Concepts Defined: Extract concept definitions
- Measures/Proxies: Extract operationalizations
- Methods: Research methodology

### Step 3: Extract Concepts

For each concept defined/used:
1. Check if `wiki/concepts/{concept-name}.md` exists
2. If exists: Update page with new definition/usage
3. If not exists: Create using `templates/concept.md`

### Step 4: Extract Theories

For each theory referenced/proposed:
1. Check if `wiki/theories/{theory-name}.md` exists
2. Update with new evidence/criticism or create new

### Step 5: Extract Proxies

For each proxy/measure:
1. Check if `wiki/proxies/{proxy-name}.md` exists
2. Document usage, validity notes, interpretations

### Step 6: Extract Methods

For each research method:
1. Check if `wiki/methods/{method-name}.md` exists
2. Add usage details or create new page

### Step 7: Output Summary

Return structured summary:
```
EXTRACTION COMPLETE:
- Paper summary: source/summary/{citekey}_summary.md
- Concepts: {n} created, {n} updated
- Theories: {n} created, {n} updated
- Proxies: {n} created, {n} updated
- Methods: {n} created, {n} updated
```

## Important Notes

- Use Obsidian-style [[filename]] linking
- When updating existing pages, append (don't overwrite)
- Domain check: Concepts should relate to economics/finance/accounting
- Slugified filenames: lowercase with underscores