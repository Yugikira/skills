# Knowledge Base Skills Changelog

All notable changes to the kb skills will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2026-04-17] - Token-Efficient Workflow & Simplified Ground Truth Protocol

### Changed
- **Workflow efficiency**: Orchestrator now creates summary directly (reads paper once) instead of dispatching a Summary Agent first. This significantly reduces token usage.
- **Verify Agent scope**: Simplified to simple YES/NO feedback with one-sentence reason for failures only. No longer provides lengthy corrected versions.
- **Ground Truth quantity**: Limited to 3-5 key findings only (not exhaustive extraction of all results).
- **Claimed Findings quantity**: Limited to 3-5 key interpretations only.
- **Reference relaxation rule**: Once a proxy/variable is fully defined in Measures table or earlier finding, subsequent findings can reference it without repeating definitions.

### Added
- `kb-extract/SKILL.md` - Internal helper skill with simplified protocol
- `kb-ingest/SKILL.md` - Main orchestration skill with new workflow
- `templates/paper_summary.md` - Paper summary template with 3-5 findings format

### Rationale
Previous test on `gao_2026_aggregated_compensation_peer` revealed:
1. Too token-consuming when orchestrator reads paper first then dispatches agent
2. Agent worked mechanically - extracting every finding unnecessarily
3. Verify Agent provided overly detailed corrections

New approach focuses on practical usage: quality over quantity, simple feedback loops.

---

## [Initial] - Project Setup

### Added
- Project structure: `kb-extract/`, `kb-ingest/`, `kb-lint/`, `kb-query/`
- Templates: `paper_summary.md`, `concept.md`, `proxy.md`, `method.md`, `theory.md`
- Scripts: `check_wikilinks.py`, `list_orphans.py`, `update_indexes.py`
- Domain focus: economics, finance, accounting
