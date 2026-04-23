# Knowledge Base Skills Changelog

All notable changes to the kb skills will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2026-04-23] - Analytical Model Support, Scanned PDF Handling, Constructs Category

### Added

- **Analytical Model Papers**: New extraction guidance for mathematical/theoretical papers
  - Recognition criteria: no empirical data, proofs/theorems, model parameters (symbols)
  - Ground Truth format: Theorem/Proposition style (NOT coefficient estimates)
  - Model Variations table: comparative statics + future paper updates
- **Constructs Category**: New `wiki/constructs/` for theoretical constructs
  - Model parameters (λ, σ_ε², etc.)
  - Definitional constructs (Informed Traders, Price Informativeness, etc.)
  - Top journal filtering: max 5 entries (oldest + newest)
- **templates/construct.md**: New template for theoretical constructs
- **templates/method_analytical.md**: Simplified template for analytical models
  - Basic setup section (3-5 bullet points)
  - Model Variations table (original + future updates)
- **Scanned PDF handling**: Phase 1 now handles scanned PDFs
  - First try: `--ai-extract` option
  - Fallback: pdftoppm + AI title extraction + `--with-title`
- **Cleanup instruction**: Remove temporary folders in `./raw/data/` after extraction

### Changed

- **kb-ingest Phase 1**: Updated Case C for scanned PDF handling with --ai-extract and image fallback
- **kb-ingest Phase 4**: Added constructs category and analytical model handling
- **kb-extract/SKILL.md**: Added "Analytical Model Papers" section with extraction rules
- **paper_summary.md**: Added "Model Parameters & Constructs" section for analytical models
- **CLAUDE.md**: Updated Wiki Structure and Templates sections (added constructs, method_analytical)

### Rationale

User feedback led to these changes:
1. Analytical model papers (e.g., Grossman & Stiglitz 1980) treated model parameters as "variables" incorrectly
2. Model parameters are theoretical constructs, NOT observable/measurable
3. Method template too complex for analytical models - need simplified version
4. Model Variations should include future paper updates, not just original comparative statics
5. Scanned PDFs failed with standard extraction - need --ai-extract and image fallback

### Test Case

Grossman & Stiglitz (1980) "On the Impossibility of Informationally Efficient Markets":
- Model parameters (λ, σ_ε², σ_θ², a, c) → wiki/constructs/ (NOT wiki/variables/)
- Model → wiki/methods/ using method_analytical.md template
- Model Variations table captures comparative statics

### Testing Results (2026-04-23)

Phase 1-2 tested with scanned PDF `ssrn-228054.pdf`:
- ✅ Cascade fallback works: `libby extract --format json` → `libby extract --ai-extract --format json` → `pdftoppm + MiniMax MCP`
- ✅ MiniMax MCP `understand_image` successfully extracted title
- ✅ Cleanup removes temp images
- 🔧 Additional fix: PDF stored in `~/.lib/papers/` - added copy step to `raw/papers/`
- 🔧 Additional fix: Markdown in `output/` subfolder - added move step

---

## [2026-04-22] - Hypothesis Section, Variable Naming, Methods Filtering

### Added

- **Hypothesis Section**: New section in paper summary template with argument structure analysis
  - Premises table with Source and Type columns
  - Reasoning approach: Deductive or Inductive classification
  - Evaluation: Sound/Unsound (deductive), Cogent/Uncogent (inductive)
- **kb-verify/SKILL.md**: New sub-skill for streamlined verification agent (YES/NO checks only)
- **Scripts/check_related_papers.py**: New script for title-based matching of related papers against wiki database

### Changed

- **Variable naming**: Renamed "proxy" → "variable" across all templates and skills
  - New table format: Paper Variable (exact name from paper) → Wiki Name (common-sense descriptive)
  - Ground Truth findings use paper's exact variable names (honest to source)
  - Wiki pages use descriptive names (e.g., InDegree → Peer_Selection_Count)
- **Variable wiki filtering**: Only create wiki pages for directly measurable variables
  - Create for: raw counts, indicators, ratios, network statistics
  - Skip for: PCA components, constructed indices, fitted values, standardized variables
- **Methods wiki filtering**: Skip standard econometric methods
  - Skip: OLS, FE, RE, 2SLS, GMM, DiD, Regression Discontinuity (standard versions)
  - Create: novel designs, analytical models, methodological contributions
- **Related Papers section**: Changed from simple links to structured table format
  - Columns: Authors, Year, Title, Relevance, Wiki Link
  - Links only to papers already in wiki database
- **kb-ingest workflow**: Updated Phase 3 to dispatch sub-agents
  - kb-verify for verification (separate skill)
  - Inline agents for hypothesis and references extraction
- **Proxy Interpretations**: Limited to most valuable sources
  - Max 5 interpretations total
  - Oldest + Newest from Top journals per domain
  - Top journals: Economics (AER, JPE, QJE, Econometrica, RES); Finance (JF, RFS, JFE, JFQA, RoF); Accounting (TAR, CAR, JAR, RAST, JAE)

### Removed

- **See Also sections**: Removed from theory.md, variable.md, and concept.md templates (not meaningful at this stage)

### Fixed

- **Wiki template guidance**: Added explicit template section mapping in kb-extract and kb-ingest
  - Specifies which template sections to fill for Concepts, Variables, Methods, Theories
  - Documents source in paper for each section
  - Marks required vs optional sections

### Updated Files

- `templates/paper_summary.md` - Added Hypothesis section, updated Variables table format, Related Papers table
- `templates/proxy.md` → `templates/variable.md` - Renamed, updated for directly measurable variables
- `templates/theory.md` - Removed See Also section
- `templates/concept.md` - Updated "Constructs & Measures" → "Constructs & Variables"
- `kb-extract/SKILL.md` - Added Hypothesis extraction, Methods filtering, Variable naming guidelines
- `kb-ingest/SKILL.md` - Updated workflow for sub-agent dispatch, variable/method wiki filtering
- `kb-lint/SKILL.md` - Updated "proxies" → "variables"
- `kb-verify/SKILL.md` - Created new verification skill
- `Scripts/update_indexes.py` - Changed "proxies" → "variables" category
- `Scripts/check_wikilinks.py` - Changed "proxies" → "variables" category
- `Scripts/check_related_papers.py` - Created new script

### Rationale

User feedback led to these changes:
1. Hypothesis analysis critical for academic work evaluation
2. Variable names should be honest to paper (Ground Truth uses exact names)
3. Wiki bloat from general methods and PCA components - now filtered
4. "See Also" sections were not providing value at this stage
5. Proxy Interpretations growing unbounded - limited to Top journal sources
6. kb-ingest/kb-extract too lengthy - modularized with kb-verify sub-skill

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
