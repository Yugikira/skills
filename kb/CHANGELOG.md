# Knowledge Base Skills Changelog

All notable changes to the kb skills will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2026-04-20] - Concept-Construct-Proxy Separation

### Changed
- **Concept extraction**: Now clearly separates Concepts (abstract ideas), Constructs (operationalizations), and Proxies (computational measures)
- **Two-table format**: Concepts Defined table now includes Definition + Constructs columns; Measures/Proxies table chains Measure → Construct → Concept
- **Section guidance**: Explicit instruction to find concept definitions in Introduction, Hypothesis Development, Literature Review sections
- **Undefined concepts**: Added `[common-sense]` marker for concepts without explicit paper definition

### Updated Files
- `kb-extract/SKILL.md` - Added concept extraction rules, two-table format with examples
- `templates/paper_summary.md` - New Concepts Defined and Measures/Proxies table structures
- `templates/concept.md` - Added Constructs section to show operationalization chain
- `kb-ingest/SKILL.md` - Added concept extraction sections to Phase 3

### Rationale
User feedback showed:
1. Previous extraction mixed definitions with constructions (e.g., "Managerial Labor Classifications" defined as its measures)
2. Key concepts like "Tournament Incentive" were missing
3. Undefined concepts lacked fallback handling

New approach mirrors academic methodology: Concept → Construct → Proxy chain for transparent operationalization.

---

## [2026-04-20] - Section Reordering & Claim-Ground Truth Correspondence

### Changed
- **Section ordering**: Claimed Findings now appears BEFORE Ground Truth Findings in all templates and skills. This establishes the interpretive framework first, then provides empirical support.
- **Correspondence requirement**: The first N Ground Truth findings should directly support the first N Claimed findings. Finding 1 supports Claim 1, Finding 2 supports Claim 2, etc.

### Updated Files
- `templates/paper_summary.md` - Reordered sections, added correspondence guidance
- `kb-extract/SKILL.md` - Updated extraction order and added correspondence requirement
- `kb-ingest/SKILL.md` - Updated summary creation instructions

### Rationale
Placing claims before evidence mirrors how scientific communication works - readers first understand *what* authors claim (the story), then verify *how* they support it (the data). The correspondence requirement creates a transparent chain from interpretation to empirical support.

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
