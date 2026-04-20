---
name: kb-ingest
description: Main skill for ingesting academic papers into the Knowledge Base. Orchestrates paper acquisition, conversion, extraction, and index updates.
---

# kb-ingest - Paper Ingestion Pipeline

Ingest academic papers into the Knowledge Base, extracting concepts, theories, proxies, and methods.

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

### Phase 3: Summary Creation (Orchestrator Directly)

**Token-efficient**: Orchestrator creates summary, then Verify Agent checks.

1. **Orchestrator creates summary** (read paper key sections directly):
   - Read: **Introduction, Hypothesis Development, Literature Review** (for concept definitions)
   - Read: Abstract, Results tables, Variable Definitions (in context or appendix)
   - Create `source/summary/{citekey}_summary.md` using template
   - Include **3-5 key Claimed findings** FIRST (authors' interpretations)
   - Include **3-5 key Ground Truth findings** SECOND (empirical support)
   - **Correspondence**: Ground Truth Finding N should support Claim N
   - Fill **Concepts Defined table** with:
     - Abstract theoretical definitions (NOT operationalizations)
     - Link to constructs that operationalize each concept
     - Mark undefined concepts with `[common-sense]`
   - Fill **Measures/Proxies table** with:
     - Computational definitions
     - Chain: Measure → Construct → Concept

2. **Dispatch Verify Agent** (Agent tool, general-purpose):
   - Agent reads summary only (not full paper)
   - Checks each finding: YES/NO with one-sentence reason
   - Simple output format

3. **Orchestrator revises** (if any NO):
   - Edit failing findings directly
   - Add missing definitions
   - No new interpretations

### Phase 4: Wiki Update (Orchestrator)

After summary is finalized, **Orchestrator** (you) creates/updates wiki pages:

1. Read finalized `source/summary/{citekey}_summary.md`
2. For "Concepts Defined" table entries → create/update `wiki/concepts/{concept}.md`
3. For "Measures/Proxies" table entries → create/update `wiki/proxies/{proxy}.md`
4. For "Methods" section → create/update `wiki/methods/{method}.md`
5. For theories mentioned → create/update `wiki/theories/{theory}.md`

Use templates from `templates/` directory. Use Obsidian [[filename]] linking.

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
- kb-extract skill (kb-extract.md)
- Python Scripts/update_indexes.py

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
- wiki/proxies/{proxy}.md ({n} pages)
- wiki/methods/{method}.md ({n} pages)

Indexes updated. See wiki/_index.md for overview.
```