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

**IMPORTANT: Do NOT use WebSearch or WebFetch. Follow these exact Bash/MCP tool steps:**

1. First attempt: Run `libby extract {pdf_path} --format json` and capture output
2. Check result:
   - If output contains citekey and metadata: SUCCESS, proceed to step 5
   - If output shows "Failed" or no citekey: FAIL, proceed to step 3
3. Second attempt (AI fallback): Run `libby extract {pdf_path} --ai-extract --format json`
4. Check result:
   - If output contains citekey: SUCCESS, proceed to step 5
   - If output shows "Failed" or "Cannot extract text": FAIL, proceed to pdftoppm fallback
5. **pdftoppm fallback** (for scanned PDFs when both above fail):
   a. Run Bash: `pdftoppm -png -f 1 -l 1 {pdf_path} raw/data/temp_page`
   b. Run MiniMax MCP tool `mcp__MiniMax__understand_image` with prompt "Extract paper title" on `raw/data/temp_page-01.png`
   c. Run Bash: `libby extract {pdf_path} --with-title "{extracted_title}" --format json`
6. After successful extraction:
   a. PDF is in `~/.lib/papers/{citekey}/` - copy to `raw/papers/{citekey}/`
   b. Run: `mkdir -p raw/papers/{citekey} && mv -r ~/.lib/papers/{citekey}/* raw/papers/{citekey}/`
7. Verify files in `raw/papers/{citekey}/`:
   - Should have: `{citekey}.pdf`, `{citekey}.bib`
   - If markdown in `output/` subfolder, move to parent: `mv raw/papers/{citekey}/output/{citekey}.md raw/papers/{citekey}/`
8. **Clean up**: 
   - Run: `rm -rf raw/data/temp_page*.png` (remove temp images)

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

#### 3.6 Wiki Collision Check

**Purpose**: Check existing wiki entries BEFORE creating new ones. Prevent duplicates and maintain knowledge base consistency.

**Step 1: Run Collision Detection Script**

```bash
python Scripts/check_wiki_collision.py --summary source/summary/{citekey}_summary.md --json
```

Output JSON identifies:
- `exact_match`: Existing entry with same name → decision: `update_existing`
- `candidates`: Similar entries for semantic comparison → dispatch agent for decision

**Step 2: Dispatch Parallel Subagents (Per Category)**

For each category with candidates (concepts, variables, constructs, methods, theories), dispatch an agent:

```
Agent prompt template (Concept Checker):
---
You are checking concept wiki collision for kb-ingest.

Input:
- Summary file: {path}
- Collision candidates: {JSON from script}

For each concept with similar existing entries:
1. Read wiki/concepts/{existing_name}.md
2. Read summary's Concepts Defined table for proposed definition
3. Compare definitions and decide:
   - Identical definition → "update_existing"
   - >70% keyword overlap → "update_existing"
   - Different concept, similar name → "rename_proposed" + suggest new name
   - <70% similarity → "create_new"

Output JSON:
{"decisions": [{"proposed": "...", "existing": "...", "decision": "...", "new_name": "..."}]}
---
```

**Decision Types**:

| Decision | When | Action |
|----------|------|--------|
| `update_existing` | Exact match or high similarity | Append paper source to existing page |
| `create_new` | No collision or marginal similarity | Create new wiki page |
| `create_crosslink` | Same measurement target, different formula | Alternative variable page linking to canonical |
| `rename_proposed` | Similar name, different concept | Disambiguate proposed name in summary |

**Step 3: Update Summary Wikilinks**

Orchestrator applies agent decisions:
- `update_existing`: Change wikilink to existing page name
- `rename_proposed`: Update proposed name in summary tables
- `create_crosslink`: Note alternative in concept table

**Step 4: Proceed to Phase 4**

Phase 4 now creates pages based on resolved collision decisions.

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
   - Skip for: analytical model parameters (these are constructs, NOT variables)
   - Use Wiki Names (common-sense, not paper abbreviations)

3. **Constructs** → for analytical model papers, create wiki/constructs/{construct}.md
   - Use templates/construct.md structure
   - Create for: model parameters (λ, σ², etc.) and definitional constructs
   - Fill: Definition, Mathematical Representation, Role in Model
   - Top journal filtering: max 5 entries (oldest + newest)

4. **Methods** → CHECK criteria before creating wiki/methods/{method}.md
   - For analytical models: use templates/method_analytical.md
   - For empirical designs: use templates/method.md
   - Create for: novel designs, analytical models
   - Skip for: standard methods (OLS, DiD, 2SLS, GMM, etc.)
   - Model Variations: include comparative statics + future paper updates

5. **Theories** → create wiki/theories/{theory}.md
   - Use templates/theory.md structure

Use templates from templates/. Use Obsidian [[filename]] linking.

### Phase 5: Index Updates

1. Run `python Scripts/update_indexes.py`
2. Updates all _index.md files

### Phase 6: Log Entry and Consolidation Trigger

1. Append to `wiki/log.md`:
```markdown
## [YYYY-MM-DD] ingest | {citekey} | {title}
- Created: wiki/concepts/{concept1}.md, ...
- Summary: source/summary/{citekey}_summary.md
```

2. **Consolidation Trigger (Batch mode only)**:
   - Count papers: `ls source/summary/*.md | wc -l` (or equivalent Glob count)
   - If count >= 10:
     - Output: "📚 {count} papers processed. Running kb-consolidate to maintain wiki quality."
     - Auto-invoke: `/kb-consolidate`
   - Note: Manual `/kb-consolidate` available for targeted audits anytime

## Dependencies

- libby-extract skill (../libby/extract/SKILL.md)
- libby-fetch skill (../libby/fetch/SKILL.md)
- paddle-pdf skill (../paddle-pdf/SKILL.md)
- kb-extract skill (kb-extract/SKILL.md) - extraction guidance
- kb-verify skill (kb-verify/SKILL.md) - verification agent
- Python Scripts/check_related_papers.py - wiki link checker
- Python Scripts/check_wiki_collision.py - collision detection (Phase 3.6)
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
