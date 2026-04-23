---
name: kb-ingest
description: Main skill for ingesting academic papers into the Knowledge Base. Orchestrates paper acquisition, conversion, extraction, and index updates.
---

# kb-ingest - Paper Ingestion Pipeline

Ingest academic papers into the Knowledge Base, extracting concepts, theories, variables, and methods.

## Usage Patterns

- `/kb-ingest {doi}` - Ingest paper by DOI (e.g., `/kb-ingest 10.1234/example`)
- `/kb-ingest "{title}"` - Ingest paper by title
- `/kb-ingest {citekey}` - Process existing paper in `raw/papers/{citekey}/`
- `/kb-ingest --batch` - Process all unprocessed PDFs in `raw/data/`

## Domain Scope

Primary domains: **economics, finance, accounting**
Related fields accepted: econometrics, behavioral economics, financial mathematics, accounting regulation

Papers outside these domains will prompt for user confirmation.

## Ingestion Pipeline

### Phase 1: Paper Acquisition

**Case A: DOI provided**
1. Invoke libby-fetch: `/libby fetch {doi}`
2. Wait for PDF download to `raw/papers/{citekey}/`

**Case B: Title provided**
1. Invoke libby-extract: `/libby extract "{title}"`
2. Get DOI from extraction result
3. Invoke libby-fetch: `/libby fetch {doi}`

**Case C: Local PDF in raw/data/**
1. Invoke libby-extract: `/libby extract {pdf_path}`
2. This organizes PDF to `raw/papers/{citekey}/`

**Case D: Existing citekey**
1. Skip acquisition, use existing files

**Case E: Batch mode (--batch)**
1. List PDFs in `raw/data/` using Glob
2. For each PDF, run Case C pipeline

### Phase 2: PDF Conversion

For each paper:
1. Check if markdown exists: `raw/papers/{citekey}/{citekey}.md`
2. If not, invoke paddle-pdf: `/paddle-pdf convert raw/papers/{citekey}/{citekey}.pdf -o raw/papers/{citekey}/`
3. Verify output exists. Note: paddle-pdf automatically names output as `{citekey}.md` (not `output.md`)

### Phase 3: Summary Creation (Orchestrator + Sub-agents)

**Token-efficient workflow**: Orchestrator creates summary, sub-agents verify and enrich.

#### 3.1 Orchestrator Creates Initial Summary

Read paper key sections directly:
- Read: **Introduction, Hypothesis Development, Literature Review** (for concept definitions)
- Read: Abstract, Results tables, Variable Definitions (in context or appendix)
- Create `source/summary/{citekey}_summary.md` using template

Include:
- **3-5 key Claimed findings** FIRST (authors' interpretations)
- **3-5 key Ground Truth findings** SECOND (empirical support)
- **Correspondence**: Ground Truth Finding N should support Claim N
- **Hypothesis section**: Analyze argument structure (see kb-extract guidance)
- **Concepts Defined table**: Abstract definitions + construct links
- **Measures/Variables table**: Computational definitions + wiki name mapping
- **Methods section**: Note if standard vs novel (for wiki decision)

#### 3.2 Dispatch Hypothesis Agent (inline)

If hypothesis is complex, dispatch general-purpose agent:
```
Agent prompt: "Read raw/papers/{citekey}/{citekey}.md Hypothesis Development section.
Analyze: 1) Hypothesis statement, 2) Premises and sources, 3) Deductive/Inductive approach.
Return structured Hypothesis section content."
```

#### 3.3 Dispatch References Agent (inline)

After creating Related Papers table, dispatch agent to enrich citations:
```
Agent prompt: "Grep raw/papers/{citekey}/{citekey}.md for Reference/References section.
Match citations in Related Papers table to full entries.
Return: for each citation, extract authors, year, title."
```

#### 3.4 Dispatch kb-verify Agent

Invoke kb-verify skill to check Ground Truth findings:
- kb-verify returns YES/NO for each finding
- If any NO: Orchestrator edits failing findings directly
- Add missing definitions, no new interpretations

#### 3.5 Link Related Papers

Run script to check wiki links:
```bash
python Scripts/check_related_papers.py --summary source/summary/{citekey}_summary.md --update
```

### Phase 4: Wiki Update (Orchestrator)

After summary finalized, **Orchestrator** creates/updates wiki pages **following templates exactly** (see kb-extract for detailed template guidance):

1. **Concepts** → create wiki/concepts/{concept}.md
   - Use templates/concept.md structure
   - Fill: Definition, Constructs & Variables (required)
   - Fill optional: Alternative Definitions, Determinants, Consequences, etc.

2. **Variables** → CHECK criteria before creating wiki/variables/{variable}.md
   - Use templates/variable.md structure
   - Create for: directly measurable (raw counts, indicators, ratios, network stats)
   - Skip for: derived/composite (PCA components, indices, fitted values)
   - Use Wiki Names (common-sense, not paper abbreviations)

3. **Methods** → CHECK criteria before creating wiki/methods/{method}.md
   - Use templates/method.md structure
   - Create for: novel designs, analytical models
   - Skip for: standard methods (OLS, DiD, 2SLS, GMM, etc.)

4. **Theories** → create wiki/theories/{theory}.md
   - Use templates/theory.md structure

Use templates from templates/. Use Obsidian [[filename]] linking.

### Phase 5: Index Updates

1. Run `python Scripts/update_indexes.py`
2. Updates all _index.md files

### Phase 6: Log Entry

Append to `wiki/log.md`:
```markdown
## [YYYY-MM-DD] ingest | {citekey} | {title}
- Created: wiki/concepts/{concept1}.md, ...
- Summary: source/summary/{citekey}_summary.md
```

## Dependencies

- libby-extract skill (../libby/extract/SKILL.md)
- libby-fetch skill (../libby/fetch/SKILL.md)
- paddle-pdf skill (../paddle-pdf/SKILL.md)
- kb-extract skill (kb-extract/SKILL.md) - extraction guidance
- kb-verify skill (kb-verify/SKILL.md) - verification agent
- Python Scripts/check_related_papers.py - wiki link checker
- Python Scripts/update_indexes.py - index updater

## Error Handling

- **PDF not found**: Ask user to provide PDF
- **Conversion fails**: Check paddle-pdf output
- **Domain mismatch**: Prompt confirmation

## Output Format

After ingestion:
```
✓ Knowledge Base Updated

Paper: {title}
DOI: {doi}
Citekey: {citekey}

Created:
- source/summary/{citekey}_summary.md
- wiki/concepts/{concept}.md ({n} pages)
- wiki/theories/{theory}.md ({n} pages)
- wiki/variables/{variable}.md ({n} pages)
- wiki/methods/{method}.md ({n} pages)

Indexes updated. See wiki/_index.md for overview.
```