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