# Progress

Task tracking for kb-plugin restructuring and ima-skill integration.

## Completed Tasks Summary

### Task 1: Restructuring kb-plugin into kb-skill (Completed 2026-05-15)

Created nested skill structure following ima-skill pattern:
- `kb-skill/SKILL.md` - Root dispatcher with decision table
- Sub-skills: ingest, query, lint, consolidate, verify, extract, wiki
- Scripts/templates placed inside sub-skills that use them

### Task 2: Incorporate ima-skill into kb workflow (Completed 2026-05-15)

Integrated IMA KB semantic search across all skills:
- kb-ingest, kb-query, kb-wiki now follow: IMA KB check → ima search → fallback to file-based
- Added Phase 7: IMA KB Sync with `move_knowledge` API for updates

### Task 3: Expanding domain scope (Completed 2026-05-15)

Extended from economics/finance/accounting to include management science/marketing:
- Created paper type templates: archival, experimental, survey, analytical (review uses minimal summary)
- Created type-specific extraction guidance files in extract/references/
- Created methodology-specific wiki templates: variable_survey.md, method_experimental.md, method_survey_instrument.md
- Established Claim-Ground Truth correspondence rules for all templates
- Added Hypothesis extraction guidance for all paper types with hypotheses

---

## Task 4: Fix experimental and analytical wiki guidance issues

- **Status**: Completed
- **Started**: 2026-05-16
- **Finished**: 2026-05-16

### Sub-task 4.1: Experimental variable wiki guidance (Completed)

**Issue**: No guidance for key variables from experimental research.

**Fixes**:
- Created `kb-skill/wiki/templates/variable_experimental.md` template
- Template documents: dependent variable measurement, manipulated independent variable operationalization
- Wiki naming: `{variable}_exp.md`
- Key sections: Measurement Method, Manipulation Method, Manipulation Check, Validity Notes
- Updated `kb-wiki/SKILL.md`: Added Experimental Variables section with template guidance

### Sub-task 4.2: Analytical method wiki criteria tightening (Completed)

**Issue**: Methods page creation too broad - creates pages for model variations.

**Fixes**:
- Updated `kb-wiki/SKILL.md` Methods Filtering section for analytical papers
- CREATE only for **baseline/classical model**
- ADD variations to Model Variations table in baseline page
- Only add if variation generates **significant new insights** or **different predictions**
- Reference: `references/Noisy_Rational_Expectations_Model.md` example

### Sub-task 4.3: Analytical variable/construct wiki criteria tightening (Completed)

**Issue**: Recording all constructs makes wiki pages explode.

**Fixes**:
- Updated `kb-wiki/SKILL.md` Variables Filtering section for analytical papers
- CREATE wiki/constructs/ ONLY for **innovative theory constructs**
- SKIP for: standard constructs from classical models, common constructs already documented
- Update existing page instead of creating new for common constructs

---

## Task 6: Fix experimental/survey wiki template issues from user testing

- **Status**: Completed
- **Started**: 2026-05-16
- **Finished**: 2026-05-16

### Problem Statement

User tested kb-skill with experimental paper extraction. Three feedback issues identified:

1. **Feedback 1**: Manipulations section creates separate variable pages with suffixes (treatment/control/Hedonic vs Utilitarian) - should use column to distinguish conditions, keep single variable page, and use `|` separator in wiki Manipulation Method column
2. **Feedback 2**: Ground Theories for experimental research always left un-created due to conflicting instructions (kb-extract says "create" but kb-wiki has no explicit rule for referenced theories)
3. **Feedback 3**: Survey variable page `Studies Using This Dimension` table's Sample column causes meaningless per-sample rows

### Design Decisions

#### Experimental Summary Template (Manipulations)
- Add `Condition Type` column (Treatment/Control/Hedonic/Utilitarian etc.)
- Keep single Paper Variable without suffixes
- Wiki Page links to single `{variable}_exp` page

#### Experimental Variable Template
- For Manipulated IV table: Add `Condition Type` column
- Use `|` separator in Manipulation Method cell for different conditions
- Remove standalone Manipulation Details section (content goes into Manipulation Method column)

#### Ground Theories Wiki Guidance
- **CHECK FIRST, THEN CREATE OR UPDATE** pattern (not "always create")
- Add explicit section in kb-wiki/SKILL.md for experimental ground theories
- CREATE wiki/theories/{theory}.md for BOTH:
  - Referenced theories from prior literature (e.g., Stereotype Content Model from Cuddy 2008)
  - Novel theories contributed by the paper
- Link to original source paper's summary
- **New template**: `theory_exp.md` with structured evidence tables
- **Evidence Supporting table**: Paper, Journal, Year, Experimental Design, Key Finding, Support Type
- **Evidence Contradicting table**: Paper, Journal, Year, Experimental Design, Contradictory Finding, Nature of Contradiction
- **Selection**: Oldest 2 + Newest 3 from top journals (max 5)

#### Survey Variable Template
- Remove `Sample` column from `Studies Using This Dimension` table
- Keep: Paper, Reliability (α), Validity, Key Findings

### Implementation Plan

1. Update `kb-skill/extract/templates/paper_summary_experimental.md` - add Condition Type column to Manipulations
2. Update `kb-skill/wiki/templates/variable_experimental.md` - add Condition Type column, restructure for multi-paper
3. Update `kb-skill/wiki/templates/variable_survey.md` - remove Sample column
4. Create `kb-skill/wiki/templates/theory_exp.md` - experimental theory template with evidence tables
5. Update `kb-skill/wiki/SKILL.md` - add explicit Ground Theories section, reference theory_exp.md
6. Update `kb-skill/extract/SKILL.md` - clarify Ground Theories check-first pattern

---

## Task 5: Fix experimental, survey, and analytical wiki template issues

- **Status**: Completed
- **Started**: 2026-05-16
- **Finished**: 2026-05-16

### Problem Statement

User tested kb-skill with experimental paper extraction. Three feedback issues identified:

1. **Feedback 1**: Experimental summary lacks explicit Manipulations section - manipulation info scattered across variable pages
2. **Feedback 2**: Experimental variable page missing construct/computational definition (later clarified: remove construct content entirely, focus on manipulation/measurement)
3. **Feedback 3**: Variable templates only support single-paper extraction, not multi-paper accumulation (experimental, survey, analytical all affected)

### Design Decisions

#### Experimental Summary Template
- Add `## Manipulations` section after `Measures/Variables`
- One row per **manipulation method** (same variable can have multiple methods)
- Columns: Paper Variable, Manipulation, Studies, Wiki Page
- Studies format: `Study {number} (n={size} {pool})` - e.g., "Study 1a (n=511 students)"

#### Experimental Variable Template
- Remove construct-related content entirely
- Focus on manipulation/measurement operationalization only
- For Manipulated IV table: Paper, Manipulation Method, Treatment Levels, Manipulation Check, Control Condition, Validity
- Selection: First + most recent from top journals for similar manipulation strategy
- Papers Using table: Paper, Key Findings (simple accumulation)

#### Survey Variable Template
- Questions Relating to This Dimension table: Questions, Response Scale, Papers
- ONE precise question excerpt per semantic group (not multiple variants)
- Papers column: first + most recent from top journals
- Studies Using This Dimension table: Paper, Sample, Reliability (α), Validity, Key Findings

#### Analytical Construct Template
- Remove `## Mathematical Representation` section (notation is not knowledge)
- Keep Definition, Role in Model, Papers Defining/Using tables

### Implementation Plan

1. Update `kb-skill/extract/templates/paper_summary_experimental.md` - add Manipulations section
2. Update `kb-skill/wiki/templates/variable_experimental.md` - restructure for multi-paper
3. Update `kb-skill/wiki/templates/variable_survey.md` - restructure for multi-paper
4. Update `kb-skill/wiki/templates/construct.md` - remove Mathematical Representation
5. Create `references/experimental_extract_guidance.md` - brief manipulation handling guidance
6. Update `kb-skill/wiki/SKILL.md` - update Experimental Variables section guidance
7. Update `kb-skill/extract/SKILL.md` - reference new experimental guidance
