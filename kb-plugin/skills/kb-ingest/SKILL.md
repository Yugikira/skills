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
- `/kb-ingest {citekey1} {citekey2} ...` - Batch process multiple papers in `raw/papers/`
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

**Step 0: Check for well-organized paper (skip extraction if possible)**

If the PDF is inside a subfolder of `raw/data/` (e.g., `raw/data/some_folder/paper.pdf`):
1. Run: `ls raw/data/{folder_name}/` to list directory contents
2. If the folder contains a `.bib` file alongside the PDF — paper is already well-organized:
   a. Run: `mv raw/data/{folder_name} raw/papers/` to move the entire folder
   b. Extract citekey from `.bib` filename or folder name
   c. **Skip directly to Phase 2: PDF Conversion**
3. If no `.bib` file or PDF is bare (not in a subfolder) — continue to Step 1

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

### Phase 3: Extraction & Wiki Drafting (Single Subagent)

**Token-efficient workflow**: ONE subagent handles all paper reading, summary creation, and wiki page drafting. No further sub-agents are dispatched.

For batch (multiple citekeys), process papers sequentially.

#### 3.1 Dispatch Extraction + Wiki Subagent

Dispatch a SINGLE subagent. **CRITICAL**: This agent must complete ALL work itself — it MUST NOT dispatch further sub-agents.

```
Agent prompt for extraction subagent:
---
You are extracting knowledge from an academic paper and creating wiki pages for the Knowledge Base.

Input files:
- Paper markdown: raw/papers/{citekey}/{citekey}.md
- Summary template: kb-plugin/templates/paper_summary.md
- Extraction guidance: kb-extract skill (what to extract, how to format)
- Wiki creation guidance: kb-wiki skill (how to create wiki pages, what to skip)

YOUR JOB (complete all steps yourself -- DO NOT dispatch sub-agents or invoke other skills):

STEP 1: READ the paper
- Read Introduction, Hypothesis Development, Literature Review, Results/Discussion, Variable Definitions, **Reference/References section**

STEP 2: CREATE summary at source/summary/{citekey}_summary.md
Follow kb-extract guidance and paper_summary.md template:
- 3-5 Claimed findings (authors' interpretations)
- 3-5 Ground Truth findings (empirical support, with correspondence to claims)
- Hypothesis section with argument structure analysis
- Concepts Defined table (abstract definitions + construct links)
- Measures/Variables table (Paper Variable → Wiki Name mapping + computational definitions)
- Methods section (note standard vs novel for wiki decision)
- **Related Papers table**: For each cited paper, extract full details (authors, year, title, journal) from the References section. Do NOT leave citations as bare citekeys.

STEP 2.5: SELF-VERIFY Ground Truth ↔ Claim correspondence
Before creating wiki pages, re-check each Ground Truth finding:
- Does GT Finding N actually support Claimed Finding N?
- Are the GT findings reproducible? (variable names match paper, formulas are exact, coefficients and p-values are correct)
- If any check fails: re-read the relevant paper section and fix the summary now
- This is a self-check — the paper is already in your context, no re-reading cost

STEP 3: RUN related papers linker
```bash
python Scripts/check_related_papers.py --summary source/summary/{citekey}_summary.md --update || \
python kb-plugin/Scripts/check_related_papers.py --summary source/summary/{citekey}_summary.md --update
```

STEP 4: CREATE wiki pages
Follow kb-wiki skill guidance:
- Use templates from templates/ (fallback kb-plugin/templates/)
- Concepts → wiki/concepts/{concept}.md (for concepts in Concepts Defined table)
- Variables → wiki/variables/{variable}.md (ONLY for directly measurable variables; skip derived/PCA/composite)
- Constructs → wiki/constructs/{construct}.md (for analytical model parameters)
- Methods → wiki/methods/{method}.md (ONLY for novel designs/models; skip standard methods)
- Theories → wiki/theories/{theory}.md (if paper contributes a theory)
- Use Obsidian [[filename]] linking
- Include first_used/first_defined linking back to summary

OUTPUT: Return the summary path and list of created wiki pages by category.
---
```

### Phase 4: Wiki Review & Merge (Orchestrator)

After subagent returns, **Orchestrator** reviews and finalizes everything. This is a lightweight quality check — fix only clear errors, don't re-read the full paper.

#### 4.1 Review Summary Quality

1. Read source/summary/{citekey}_summary.md
2. Quick check:
   - Claimed findings correspond to Ground Truth findings
   - Variable names in GT findings have computational definitions
   - Concepts Defined table entries have definitions (not empty)
   - Measures/Variables table has Paper Variable / Wiki Name mapping
3. Fix minor issues directly

#### 4.2 Review Wiki Pages

1. Read each wiki page created by the subagent
2. Quick check:
   - Required sections are filled (Definition, Computation, etc.)
   - Obsidian [[filename]] links are correct
   - Variable naming follows kb-wiki conventions
   - Standard methods were correctly skipped
   - Derived/composite variables were correctly skipped
3. Fix minor issues directly

#### 4.3 Wiki Collision Resolution

**Purpose**: Check newly created pages against **pre-existing** wiki entries (from before this ingestion). The subagent already created the pages — now we check if any should be merged into older existing pages.

**Step 1: Collect New Pages from Subagent Output**

From the subagent's return value, collect all created wiki page names by category. For batch (multiple papers), collect all pages from all papers combined.

**Step 2: Run Post-Ingest Collision Script**

Write the new page list to a temp JSON file, then run the script:

```bash
# Write new pages list (example format)
# echo '{"concepts":["Name1"],"variables":["Var1"],...}' > /tmp/new_pages_{citekey}.json

python Scripts/check_new_page_collision.py --new-pages /tmp/new_pages_{citekey}.json --json || \
python kb-plugin/Scripts/check_new_page_collision.py --new-pages /tmp/new_pages_{citekey}.json --json
```

This script checks new pages against **pre-existing** entries only — it excludes the new pages themselves from the existing pool. Output:

- `exact_match`: A pre-existing page has the same normalized name → merge needed
- `candidates`: Pre-existing pages with similar names/definitions → semantic review needed
- Entries with no matches are silently skipped (no action needed)

The `_summary` key shows: `total_new_pages`, `exact_matches`, `needs_semantic_review`, `no_collision`.

**Step 3: Resolve Each Collision via Semantic Comparison**

For each entry in the collision report:

1. **If `exact_match` present**: Read the pre-existing page. If the new page's definition truly duplicates it → `merge_into_existing`. If same name but different concept → `rename_new_page`.

2. **If `candidates` non-empty**: For each candidate, **read `wiki/{category}/{candidate_name}.md`** fully. Compare definitions at the **phenomenon level**:
   - **Same underlying phenomenon?** Both describe the same causal mechanism, theoretical scope, and domain → `merge_into_existing`
   - **Different phenomenon despite keyword overlap?** Definitions describe different things → `keep_new`
   - **Subset relationship?** New page is a narrower case of existing → `merge_into_existing` (append as sub-case)
   - **Superset relationship?** New page is broader → `keep_new` + add cross-reference from existing page
   - **Same name, different concept?** → `rename_new_page` + suggest disambiguated name

**CRITICAL**: Do NOT use keyword overlap percentage to decide. Read the actual definition text and reason about whether the phenomena are genuinely the same.

**Decision Types**:

| Decision | When | Action |
|----------|------|--------|
| `merge_into_existing` | Same underlying phenomenon | Merge new page content into existing page; delete the new page; update wikilinks |
| `keep_new` | Different phenomenon | Keep new page as-is |
| `create_crosslink` | Same measurement target, different formula | Add cross-link between pages |
| `rename_new_page` | Similar name, different concept | Rename new page file, update all wikilinks |

#### 4.4 Apply Collision Decisions

- `merge_into_existing`: Copy new content from the new page into the pre-existing page (add paper to Papers Using, merge determinants/consequences/etc.), then **delete the new page file**. Update all wikilinks pointing to the new page to point to the existing page instead.
- `rename_new_page`: Rename the new wiki page file, update all wikilinks in the summary and other pages.
- `create_crosslink`: Add cross-link between the two pages, note formula/definition difference.
- `keep_new`: Keep new page as-is — it's genuinely distinct.

#### 4.5 Finalize

After all checks pass, proceed to Phase 5.

### Phase 5: Index Updates

1. Run index updater with fallback:
   ```bash
   python Scripts/update_indexes.py || python kb-plugin/Scripts/update_indexes.py
   ```
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
- kb-wiki skill (kb-wiki/SKILL.md) - wiki creation guidance
- Python kb-plugin/Scripts/check_related_papers.py - wiki link checker
- Python kb-plugin/Scripts/check_new_page_collision.py - post-ingest collision detection (Phase 4.3)
- Python kb-plugin/Scripts/update_indexes.py - index updater
- **Note**: Scripts run from wiki root; use fallback `kb-plugin/Scripts/` if path fails

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
