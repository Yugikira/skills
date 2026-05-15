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
Follow the Summary Agent instructions in `kb-skill/ingest/summary-agent.md` to extract this paper.

INPUT:
- citekey: {citekey}
- Paper: raw/papers/{citekey}/{citekey}.md
- Metadata: Read from raw/papers/{citekey}/{citekey}.bib
- Summary template: kb-skill/extract/templates/paper_summary.md
- Extraction guidance: kb-skill/extract/SKILL.md (what to extract, how to format)
- Wiki creation guidance: kb-skill/wiki/SKILL.md (how to create wiki pages, semantic duplicate check, what to skip)

Execute all 6 steps from the Summary Agent:
1. Read paper
2. Create summary at source/summary/{citekey}_summary.md
3. Self-verify GT ↔ Claim correspondence
4. Run related papers linker
5. Create wiki pages (follows kb-wiki: includes semantic duplicate check before creation)
6. Return output report

OUTPUT: Return summary path and list of wiki pages created/updated/skipped by category.
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

**Step 0: IMA Knowledge Base Check**

Before collision detection, verify IMA KBs exist:

1. Run: `ima_api "openapi/wiki/v1/search_knowledge_base" '{"query": "", "cursor": "", "limit": 20}'`
2. Check for KBs: `concepts`, `variables`, `methods`, `constructs`, `theories`

**If KBs missing**: Prompt user: "请在IMA桌面客户端创建以下知识库并上传对应文件: {missing_kbs}"

**Step 1: Collect New Pages from Subagent Output**

From the subagent's return value, collect all created wiki page names by category. For batch (multiple papers), collect all pages from all papers combined.

**Step 2: Collision Detection**

**Primary method (IMA KB available):**

For each new page in each category:
```bash
# Search for similar entries in category KB
ima_api "openapi/wiki/v1/search_knowledge" '{"query": "{page_name}", "knowledge_base_id": "{kb_id}", "cursor": ""}'
```

- Check `info_list` for exact matches or similar names
- Review `highlight_content` for definition snippets
- Cross-check across related categories (e.g., new variable vs existing concepts)

**Fallback (IMA KB not available):**

```bash
python scripts/check_new_page_collision.py --new-pages /tmp/new_pages_{citekey}.json --json
```

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
   python scripts/update_indexes.py
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

### Phase 7: IMA Knowledge Base Sync

Sync newly created files to IMA knowledge bases for semantic search capability.

**Step 1: Check IMA KB Availability**

```bash
ima_api "openapi/wiki/v1/search_knowledge_base" '{"query": "", "cursor": "", "limit": 20}'
```

Check returned KB names against required list:
- Required KBs: `summary`, `concepts`, `variables`, `methods`, `constructs`, `theories`
- Archive KB: `Archived` (for storing old versions before update)

**If KBs missing**: Prompt user: "请在IMA桌面客户端创建知识库: {missing_kb}，然后重试。"

**If `Archived` KB missing**: Prompt user: "请创建一个名为 'Archived' 的知识库用于存放旧版本文件，以便自动更新。"

**Step 2: Collect Files to Sync**

From Phase 4 subagent output, collect:
- `source/summary/{citekey}_summary.md` → sync to `summary` KB
- All created wiki pages by category → sync to corresponding KB

**Step 3: Check Duplicates in IMA KB**

For each file to sync:
```bash
ima_api "openapi/wiki/v1/search_knowledge" '{"query": "{filename}", "knowledge_base_id": "{kb_id}", "cursor": ""}'
```

- If `info_list` empty → file is NEW, proceed to upload
- If `info_list` has match → file EXISTS, record `media_id` for move operation

**Step 4: Handle Existing Files (Move to Archived)**

For files that already exist in IMA KB:

```bash
# Move old file to Archived KB (max 10 files per call)
ima_api "openapi/wiki/v1/move_knowledge" '{
  "src_knowledge_base_id": "{original_kb_id}",
  "dst_knowledge_base_id": "{archived_kb_id}",
  "infos": [{"media_id": "{old_media_id}"}]
}'
```

After successful move, the original KB slot is free for new upload.

**Step 5: Upload Files to IMA KB**

For all files (new or moved-old):

1. Run preflight check:
   ```bash
   node ima-skill/knowledge-base/scripts/preflight-check.cjs --file "{filepath}" --content-type "text/markdown"
   ```

2. Create media and get COS credentials:
   ```bash
   ima_api "openapi/wiki/v1/create_media" '{"file_name": "{filename}", "file_size": {size}, "content_type": "text/markdown", "knowledge_base_id": "{kb_id}", "file_ext": "md"}'
   ```

3. Upload to COS:
   ```bash
   node ima-skill/knowledge-base/scripts/cos-upload.cjs --file "{filepath}" --secret-id "{secret_id}" --secret-key "{secret_key}" --token "{token}" --bucket "{bucket}" --region "{region}" --cos-key "{cos_key}" --content-type "text/markdown" --start-time "{start_time}" --expired-time "{expired_time}"
   ```

4. Add to KB:
   ```bash
   ima_api "openapi/wiki/v1/add_knowledge" '{"media_type": 7, "media_id": "{media_id}", "title": "{filename}", "knowledge_base_id": "{kb_id}", "file_info": {"cos_key": "{cos_key}", "file_size": {size}, "file_name": "{filename"}}'
   ```

**Step 6: Log Sync Results**

```markdown
## IMA Sync Results
- Uploaded: {n} new files
- Updated: {m} files (moved old to Archived, uploaded new)
- KBs not available: {list (if any)}
```

**Step 7: Archived Cleanup Reminder**

```
💡 已将 {m} 个旧版本文件移至 'Archived' 知识库。
   请定期清理 Archived KB 中的文件（在IMA桌面客户端中删除）。
```

## Scripts

- `scripts/check_related_papers.py` - Wiki link checker
- `scripts/check_new_page_collision.py` - Post-ingest collision detection
- `scripts/update_indexes.py` - Index updater

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

IMA Sync:
- Uploaded: {n} new files
- Updated: {m} files (moved old to Archived)
- Archived KB cleanup needed: {list of moved files}
```
