# Progress

Task tracking for kb-plugin restructuring and ima-skill integration.

## Task 1: Restructuring kb-plugin into kb-skill

- **Status**: Completed
- **Started**: 2026-05-15
- **Finished**: 2026-05-15

### Final Structure:
```
kb-skill/
├── SKILL.md                    # Root dispatcher
├── meta.json                   # Python 3.8+ dependency
├── ingest/
│   ├── SKILL.md
│   ├── summary-agent.md
│   └── scripts/                # collision, linker, index scripts
├── extract/
│   ├── SKILL.md
│   └── templates/              # paper_summary.md
├── wiki/
│   ├── SKILL.md
│   ├── scripts/                # check_wiki_collision.py
│   └── templates/              # concept, variable, method, theory, construct
├── lint/
│   ├── SKILL.md
│   └── scripts/                # wikilinks, orphans
├── consolidate/SKILL.md
├── query/SKILL.md
└── verify/SKILL.md
```

Scripts/templates placed inside the sub-skill that directly uses them (ima-skill pattern).

---

## Task 2: Incorporate ima-skill into kb workflow

- **Status**: Completed
- **Started**: 2026-05-15
- **Finished**: 2026-05-15

### Changes Made:

1. **kb-skill/SKILL.md** - Added IMA KB integration section:
   - Required KB list (summary, conversation, concepts, variables, methods, constructs, theories)
   - KB directory check using `search_knowledge_base`
   - Fallback guidance when KBs not available

2. **kb-wiki/SKILL.md** - Updated Pre-Creation Semantic Check:
   - Step 0: IMA KB check
   - Step 1: Use `search_knowledge` for semantic duplicate detection
   - Fallback to file-based Glob/Read

3. **kb-ingest/SKILL.md** - Updated Phase 4.3 Collision Resolution:
   - Step 0: IMA KB check
   - Step 2: Use `search_knowledge` for collision detection
   - Fallback to `check_new_page_collision.py` script

4. **kb-query/SKILL.md** - Updated Query Process:
   - IMA KB check section
   - Use `search_knowledge` for querying KBs
   - Fallback to file-based Grep/Read

### Key Pattern:
All skills now follow: **IMA KB check → ima search → fallback to file-based**

---

## Task 2.5: Sync local wiki to IMA knowledge base after ingestion

- **Status**: Completed
- **Started**: 2026-05-15
- **Finished**: 2026-05-15

### Changes Made:

Added **Phase 7: IMA Knowledge Base Sync** to kb-ingest/SKILL.md:

1. Check IMA KB availability
2. Collect files to sync (summary + wiki pages)
3. Check duplicates in IMA KB using `search_knowledge`
4. Upload NEW files only (IMA doesn't support replace/update)
5. Log sync results with uploaded/skipped counts
6. Remind user to manually update existing files in IMA desktop client

---

## Task 2.5: Sync local wiki to IMA knowledge base after ingestion

- **Status**: Completed (Updated)
- **Started**: 2026-05-15
- **Finished**: 2026-05-15

### Changes Made:

Added **Phase 7: IMA Knowledge Base Sync** to kb-ingest/SKILL.md with **move_knowledge** API support:

1. Check IMA KB availability (including `Archived` KB)
2. Collect files to sync (summary + wiki pages)
3. Check duplicates in IMA KB using `search_knowledge`
4. **Move existing files to `Archived` KB** using `move_knowledge` API
5. Upload new files to original KB
6. Log sync results with uploaded/updated counts
7. Remind user to periodically clean `Archived` KB

### IMA API Update:
Added `move_knowledge` API to ima-skill documentation:
- `ima-skill/knowledge-base/SKILL.md` - Added to decision table
- `ima-skill/knowledge-base/references/api.md` - Added full API documentation

### Required KBs (Updated):
- `summary`, `conversation`, `concepts`, `variables`, `methods`, `constructs`, `theories`
- **`Archived`** - Required for auto-sync (stores old versions before update)

### Workflow:
```
Existing file → Move to Archived KB → Upload new file → User cleans Archived
```

---

## Task 3: Expanding domain scope

- **Status**: In Progress
- **Started**: 2026-05-15

### Sub-task 3.1: Experimental research template (Completed 2026-05-15)

Created three separate paper summary templates:
- `kb-skill/extract/templates/paper_summary_archival.md` - Archival/empirical papers
- `kb-skill/extract/templates/paper_summary_experimental.md` - Experimental papers
- `kb-skill/extract/templates/paper_summary_analytical.md` - Analytical model papers

Updated `kb-skill/extract/SKILL.md`:
- Added Paper Type Detection section at top
- Detection based on data source + methodology
- Template routing logic

Key changes per user feedback:
- `title` field quoted to handle colons
- Experimental template: Methods merged into Experimental Design section
- Experimental Design: Added "Others" option for custom designs
- Templates don't reference each other (self-contained)

### Remaining items:
- Survey paper extraction guidance (future task)
- Review paper handling clarification (future task)
- Marketing/management science domains (future task)

---

## Task 3.2: Template cleanup and wiki creation strengthening

- **Status**: Completed
- **Started**: 2026-05-15
- **Finished**: 2026-05-15

### Sub-task 3.2.1: Remove evidence supporting/contracting from experimental template (Completed)

Removed evidence supporting/contracting section from `paper_summary_experimental.md`:
- Deleted lines 30-33 (the "For each theory, note..." section)
- This content belongs to wiki/templates/theory.md, not summary template

### Sub-task 3.2.2: Strengthen wiki creation trigger (Completed)

Added explicit "Wiki Creation Trigger" section to `kb-skill/extract/SKILL.md`:
- Trigger Tables: Concepts, Variables, Theories, Constructs
- Methods Creation Trigger: Based on summary Methods section markers
- Wiki Creation Process: Semantic check → create/update → fill template
- Added "**DO NOT skip wiki page creation**" emphasis

This ensures agent creates wiki pages after completing summary tables.

### Sub-task 3.2.3: Move archival-specific instructions to reference file (Completed)

Created `kb-skill/extract/references/archival_extract_guidance.md` containing:
- Hypothesis extraction with argument structure analysis
- Methods filtering for econometric methods (OLS, DiD, 2SLS, etc.)
- Summary requirements (Claim-Ground Truth correspondence)
- Ground truth format for regression coefficients
- Measures/variables filtering for archival papers

Refactored `kb-skill/extract/SKILL.md` to be concise hub file:
- Paper-Type-Specific Guidance section with references
- Common content: Paper type detection, wiki triggers, concept extraction, variable naming
- Analytical and experimental papers get brief inline guidance
- Archival papers reference the detailed guidance file

**Archival guidance NOT valuable for other research types**:
- Experimental papers test pre-existing theories (no argument structure analysis needed)
- Experimental papers use different ground truth format (manipulated/dependent variable)
- Analytical papers use theorem/proposition format (not regression coefficients)

---

## Task 3.3: Survey and Review paper extraction guidance

- **Status**: Completed
- **Started**: 2026-05-15
- **Finished**: 2026-05-15

### Sub-task 3.3.1: Survey paper template and guidance (Completed)

Created survey paper template `templates/paper_summary_survey.md`:
- Hypothesis section (optional - theory-driven causal predictions)
- Claim Findings (interpreted results)
- Ground Truth Findings (question-based results format OR statistical analysis format)
- Concepts Defined (easier extraction - from research question, title, introduction)
- Measures/Variables (survey questions grouped by dimensions, wiki naming `{dimension}_{concept}_survey`)
- Survey Design section: survey type, respondent target, response categories, question sequence, survey instrument, non-response handling, reliability measures
- Face-to-Face Interview Details: interview type (structured/semi/unstructured), interviewee selection
- Wiki markers: variables `_survey`, methods `_survey_instrument`

Created `references/survey_extract_guidance.md`:
- Survey paper recognition criteria
- Survey vs Experimental comparison
- Ground truth format for question-based results (grouping questions by dimensions)
- Variables = survey questions grouping structure (Concept → Dimensions → Questions)
- Wiki naming for survey variables with `_survey` marker
- Survey Design extraction details
- Face-to-face interview specifics
- Hypothesis extraction reference to archival guidance

### Sub-task 3.3.2: Review paper guidance (Completed)

Created `references/review_extract_guidance.md`:
- Review paper recognition criteria
- Different workflow: wiki consolidation, NOT full summary extraction
- Step 1: Check concept page existence
- Step 2: Create concept page if not exists (fill template, oldest 2 + nearest 3 papers only)
- Step 3: Update concept page if exists
- Minimal summary format for review papers
- ONLY create concept page for main concept
- No new variable/method pages (review papers don't introduce new measures)

Key principle: Wiki pages should remain concise—don't grow as long as review papers. Instruct readers to read review for more details.

### Sub-task 3.3.3: Hypothesis section for survey/experimental templates (Completed)

Added Hypothesis section to experimental template:
- Optional: Only if experiment develops its own hypothesis
- If testing pre-existing theory without new hypothesis: Write "No explicit hypothesis developed"
- Argument structure table with reference to archival guidance for detailed analysis
- Reasoning approach and evaluation sections

Updated archival template Hypothesis section:
- Added reference to `archival_extract_guidance.md` for detailed premise classification

Updated kb-extract/SKILL.md:
- New section "Hypothesis Extraction (Multiple Paper Types)" explaining:
  - Archival: Most common (theoretical arguments with empirical testing)
  - Survey: Theory-driven causal predictions (Brown 1995 reference)
  - Experimental: Predicting manipulation effect on dependent variable
  - Analytical: Propositions from model assumptions
  - Review: Does NOT develop hypotheses (consolidates existing)
- All hypothesis papers reference archival guidance for argument structure analysis

### Updated Paper Type Detection Table

| Paper Type | Template | Guidance Reference |
|------------|----------|-------------------|
| Archival | full template | archival_extract_guidance.md |
| Experimental | full template | inline + archival (for hypothesis) |
| Analytical | full template | inline |
| Survey | full template | survey_extract_guidance.md |
| Review | minimal summary | review_extract_guidance.md |

---

## Task 3.4: Fix survey wiki naming and ground truth format

- **Status**: Completed
- **Started**: 2026-05-15
- **Finished**: 2026-05-15

### Issue 1: Survey Wiki Naming Incorrect

**Problem**: Initial survey wiki naming used `{dimension}_{concept}_survey` per question, which was incorrect.

**Correct understanding from reference**:
- Questions are **GROUPED** by dimension (multiple questions → one wiki page)
- Wiki naming: `{dimension}_survey` (one page per dimension group)
- Concepts: Standard naming `[[concepts/{concept}]]` (NO `_survey` marker)

**Fixes applied**:
- `templates/paper_summary_survey.md`: Variables table now shows one row per **dimension** (grouped questions), not per individual question
- `references/survey_extract_guidance.md`: Wiki naming section updated with correct grouping explanation
- `kb-skill/extract/SKILL.md`: Survey-Specific Wiki Naming table shows correct naming for concepts (no marker) vs variables (grouped with `_survey`)

### Issue 2: Ground Truth Format Consolidated

**Problem**: Ground Truth concept (most objective results) is common to all paper types, but format was scattered across templates and guidance files.

**Fix**: Added "Ground Truth Format by Paper Type" section to `kb-skill/extract/SKILL.md`:
- Table showing format for each paper type with examples
- Archival: Regression coefficient format
- Experimental: Manipulated/dependent relationship format
- Survey: Question results format (grouped by dimension)
- Analytical: Theorem/Proposition format
- Review: NO Ground Truth (consolidates existing)

**Reference pattern**: Centralized format overview in SKILL.md, detailed guidance in type-specific reference files.

---