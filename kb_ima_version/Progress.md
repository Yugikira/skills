# Progress

Task tracking for kb-plugin restructuring and ima-skill integration.

## Completed Tasks Summary

### Task 1: Restructuring kb-plugin into kb-skill (2026-05-15)

Created nested skill structure: kb-skill/SKILL.md as root dispatcher, sub-skills (ingest, query, lint, consolidate, verify, extract, wiki), scripts/templates placed inside sub-skills.

### Task 2: Incorporate ima-skill into kb workflow (2026-05-15)

Integrated IMA KB semantic search: kb-ingest/query/wiki follow IMA KB check → ima search → fallback. Added Phase 7: IMA KB Sync with move_knowledge API.

### Task 3: Expanding domain scope (2026-05-15)

Extended to management science/marketing. Created paper type templates (archival, experimental, survey, analytical), type-specific extraction guidance, methodology-specific wiki templates. Established Claim-Ground Truth correspondence rules.

### Task 4: Fix experimental and analytical wiki guidance issues (2026-05-16)

- **4.1**: Created variable_experimental.md template for manipulated IV/dv measurement. Wiki naming: {variable}_exp.md.
- **4.2**: Tightened analytical methods criteria - CREATE only for baseline/classical model, variations go to table.
- **4.3**: Tightened analytical construct criteria - CREATE only for innovative constructs, SKIP standard ones.

### Task 5: Fix experimental/survey wiki template multi-paper issues (2026-05-16)

- **Experimental summary**: Added Manipulations section with Studies format `Study {n} (size={x} pool)`.
- **Experimental variable**: Removed construct content, focus on manipulation/measurement operationalization.
- **Survey variable**: Questions table with one excerpt per semantic group, Papers column first+recent.
- **Analytical construct**: Removed Mathematical Representation section.

### Task 6: Fix experimental/survey wiki template issues (2026-05-16)

- **Manipulations**: Added Condition Type column, single variable page with `|` separator for conditions.
- **Ground Theories**: CHECK FIRST pattern, created theory_exp.md template with evidence tables.
- **Survey variable**: Removed Sample column from Studies Using This Dimension table.

### Task 7: Fix orchestrator context rot and add fallback methods (2026-05-17)

- **Orchestrator restrictions**: Added Role Division table, ORCHESTRATOR RESTRICTIONS box with ❌/✅ markers. Orchestrator CAN read templates for verification only. Subagent reads .bib, determines paper type. Phase 4 hybrid review.
- **Fallbacks**: Missing libby → skip Phase 1, move PDF directly. Missing minimax → multimodal LLM fallback. Missing paddle-pdf → any pdf convert tool. Missing .bib → subagent fills from paper.

## Files Modified in Task 7

- `kb-skill/ingest/SKILL.md` - Role Division (lines 10-17), ORCHESTRATOR RESTRICTIONS, Agent Prompt restructure, Phase 4 hybrid review, Phase 1/2 fallbacks
- `kb-skill/extract/SKILL.md` - WHO DETERMINES TYPE note (subagent determines)

### Task 8: Streamline IMA integration with single pre-flight check (2026-05-18)

Based on user feedback that agents skip IMA steps without verifying tool availability.

**Root cause**: Each integration point (Phase 7, Phase 4.3, kb-wiki Pre-Creation, kb-query) had redundant IMA checks, leading to 4+ checks per ingestion.

**Solution**: Single pre-flight check at root dispatcher (`kb-skill/SKILL.md`), pass status to all downstream modules.

**Implementation**:
1. Add Pre-Flight Check to `kb-skill/SKILL.md` - actual `ima_api` call to verify functionality
2. Update `kb-skill/ingest/SKILL.md` - pass IMA_AVAILABLE flag to subagent; Phase 4, 7 use passed flag
3. Update `kb-skill/wiki/SKILL.md` - remove standalone tool check, use passed flag
4. Update `kb-skill/query/SKILL.md` - use passed flag from dispatcher
5. Fix all scripts to accept required `--wiki-dir` or `--root-dir` parameters (no default paths)

## Files Modified in Task 8

- `kb-skill/SKILL.md` - Added Pre-Flight Check section with ima_api call test, decision flow diagram
- `kb-skill/ingest/SKILL.md` - Added IMA_AVAILABLE context flag to subagent prompt; Phase 4.3 and Phase 7 use passed flag
- `kb-skill/wiki/SKILL.md` - Removed standalone tool check, added Step 0 for using passed flag; fixed fallback logic to index-first approach (Read entire index for semantic check)
- `kb-skill/query/SKILL.md` - Removed standalone IMA check, uses passed flag; fixed fallback logic to Grep-first approach for keyword search
- `kb-skill/extract/references/review_extract_guidance.md` - Fixed concept existence check to use Grep (token-efficient for single concept lookup)
- `kb-skill/ingest/scripts/update_indexes.py` - Added required `--wiki-dir` parameter
- `kb-skill/ingest/scripts/check_new_page_collision.py` - Added required `--wiki-dir` parameter
- `kb-skill/ingest/scripts/check_related_papers.py` - Added required `--root-dir` parameter
- `kb-skill/wiki/scripts/check_wiki_collision.py` - Added required `--wiki-dir` parameter
- `kb-skill/lint/scripts/check_wikilinks.py` - Added required `--root-dir` parameter
- `kb-skill/lint/scripts/list_orphans.py` - Added required `--wiki-dir` parameter
- `kb-skill/lint/SKILL.md` - Updated script call syntax with required parameters

**Note on fallback logic fix**: Original design reads `_index.md` first to get structured entry list, then reads specific candidate pages. Initial edits simplified this to Glob/Read directly - now corrected to follow index-first approach.

**Refined by use case**:
- **Semantic duplicate check (kb-wiki)**: Read entire `_index.md` (need ALL entries for comparison) ✓
- **Keyword query (kb-query)**: Grep `_index.md` first (need only matching entries) - more token-efficient ✓
- **Existence check (review_extract)**: Grep for specific concept name (only need yes/no answer) ✓