---
name: kb-consolidate
description: Consolidate and clean wiki pages by merging similar concepts/variables, removing redundant entries, fixing misplaced items, and applying top-journal filtering criteria.
---

# kb-consolidate - Wiki Consolidation and Cleanup

Consolidate wiki pages to maintain quality as the knowledge base grows: merge similar concepts/variables, remove redundant entries, fix misplaced items, and apply top-journal filtering.

## Usage

```
/kb-consolidate                          # Full audit: all types, all sections
/kb-consolidate --concepts               # Audit only concept pages
/kb-consolidate --constructs             # Audit only construct pages
/kb-consolidate --variables              # Audit only variable pages
/kb-consolidate {name}                   # Audit specific wiki page
/kb-consolidate {name} --section {sec}   # Audit specific section in specific page
```

Valid sections for `--section`:
- concepts: `definition`, `variables`, `determinants`, `consequences`, `identification`
- constructs: `papers-defining`, `papers-using`
- variables: `interpretations`, `papers-using`

## Purpose

As papers accumulate, wiki pages develop structural issues:
- **Similar variables with different names** - `Ln(NVisit)`, `Visit_Num`, `Visit_freq` all measure visitor count
- **Incorrect categorization** - variables listed as proxies that don't measure the concept
- **Redundant entries** - same consequence with parenthetical qualifiers listed separately
- **Misplaced items** - moderators, behavioral responses, validity tests listed as consequences
- **Missing top-journal filtering** - >5 entries without oldest+newest criteria

## Top-Journal Filtering Criteria

Apply to all tables with paper references (max 5 entries):
- **Oldest from Top journals** - earliest seminal paper
- **Newest from Top journals** - latest usage

**Top Journals by Domain:**
- Economics: AER, JPE, QJE, Econometrica, RES
- Finance: JF, RFS, JFE, JFQA, RoF
- Accounting: TAR, CAR, JAR, RAST, JAE

---

## Verification Checklists

### Concepts

| Check | Section | Issue Pattern | Fix |
|-------|---------|---------------|-----|
| Duplicate definitions | Definition, Alternative Definitions | Same definition from different papers | Keep oldest + note variations |
| Similar variables | Constructs & Variables | Different names measuring same underlying phenomenon (count, log, capped, indicator variants) | Create canonical + cross-links with formula notes |
| Incorrect variables | Constructs & Variables | Variable not measuring concept | Remove or move to appropriate section |
| Duplicate determinants | Determinants | Same determinant with different measurement names | Consolidate with mechanism variations |
| Duplicate consequences | Economic Consequences | Same consequence with parenthetical qualifiers | Merge + add Heterogeneity note |
| Misplaced moderators | Economic Consequences | "X moderation", "who benefits more" | Move to Heterogeneity subsection |
| Misplaced behavioral responses | Economic Consequences | What subjects DO vs outcome | Move to Determinants |
| Misplaced validity tests | Economic Consequences | "validate", "confirm", "rule out" | Move to Validity Tests section |
| Top-journal filtering | All tables | >5 entries without filtering | Apply oldest + newest criteria |

### Constructs

| Check | Section | Issue Pattern | Fix |
|-------|---------|---------------|-----|
| Duplicate definitions | Papers Defining | Same construct defined differently | Keep oldest top-journal + note variations |
| Missing top-journal filter | Papers Defining/Using | >5 entries unfiltered | Keep oldest + newest from top journals |

### Variables

| Check | Section | Issue Pattern | Fix |
|-------|---------|---------------|-----|
| Similar computation | Computation | Different names measuring same underlying phenomenon (count, log, capped, indicator variants) | Create canonical + cross-links with formula notes |
| Duplicate interpretations | Interpretations | Same interpretation from different papers | Keep oldest + newest top-journal |
| Missing top-journal filter | Interpretations | >5 entries unfiltered | Apply oldest + newest criteria |

---

## Canonical + Cross-link Merge Strategy

When similar variables found (measuring same underlying phenomenon, different formulas):

1. **Identify canonical** - most commonly used name OR most precise formula (log preferred over capped, continuous preferred over indicator)
2. **Create canonical variable page** with combined sources
3. **Alternative names become cross-link pages**:
   ```markdown
   > **Canonical Variable**: [[variables/{canonical}]]
   > This is an alternative operationalization of {underlying_measurement}.
   > Formula: {alt_formula} (vs canonical's {canonical_formula})
   ```
4. **Concepts' "Constructs & Variables" table**:
   - Keep canonical entry only
   - Add note: "Also measured as: {alt1} ({formula_type1}), {alt2} ({formula_type2})"
   - Formula types: capped, indicator, log, raw count, ratio
   - Source oldest + newest top-journal papers for each variant

---

## Execution Phases

### Phase 1: Scope Detection

1. Parse user arguments: type filter, page filter, section filter
2. Glob relevant files:
   - `--concepts`: `wiki/concepts/*.md`
   - `--constructs`: `wiki/constructs/*.md`
   - `--variables`: `wiki/variables/*.md`
   - No filter: all three directories
3. If specific page: read that page only

### Phase 2: Issue Detection

For each wiki page in scope:
1. Read full page content
2. Apply checklist for wiki type
3. Flag issues with specific fixes:
   - Similar variables: compare computation column for identical formulas
   - Incorrect variables: check if variable measures the concept
   - Duplicate entries: compare base name ignoring parenthetical qualifiers
   - Misplaced items: check entry purpose (moderator/behavioral/test)
   - Top-journal filter: count entries, check journal rankings

### Phase 3: Similar Concepts Detection (Cross-File)

1. Build concept similarity matrix:
   - Definition text overlap (lemmatized keywords)
   - Shared variables >50%
   - Shared theories >50%
2. Flag high-similarity pairs (>70% threshold) for potential merge
3. Report to user for manual decision

### Phase 4: Report Generation

Output audit report:
```markdown
# Consolidation Audit Report

## Summary
- Pages audited: {n}
- Issues found: {m}
- By type: {similar vars: x, incorrect: y, duplicates: z, misplaced: w}

## {Page Name}

**Issues**: {count}

| Issue Type | Entry | Fix | Details |
|------------|-------|-----|---------|
| Similar variable | Visit_freq, Ln(NVisit), Visit_Num | Merge → canonical Ln_NVisit | All measure visitor count |
| Incorrect variable | ABN_ABSAR | Remove | Not a site visit proxy |
| Duplicate consequence | Stock price impact (info env) | Merge to Heterogeneity | Same base consequence |
| Misplaced moderator | Governance moderation | Move to Heterogeneity | Who benefits more |

**Recommended Structure**: {outline}
```

### Phase 5: User Approval

Present findings. Ask:
> "Apply these fixes? (Y/n)"
> - Y: Execute all recommended fixes
> - n: Skip, make manual edits later

### Phase 6: Execute Fixes

After user approval:
1. Apply fixes sequentially
2. For variable merges:
   - Create canonical variable page if needed
   - Create cross-link pages for alternatives
   - Update concept page table
3. For section moves:
   - Remove from incorrect section
   - Add to correct section
4. For top-journal filtering:
   - Identify oldest + newest top-journal papers
   - Keep only those entries
5. Maintain paper reference integrity (wikilinks)

### Phase 7: Output Summary

```markdown
✓ Consolidation Complete

Pages modified: {n}
Issues fixed: {m}

By type:
- Similar variables merged: {x} → canonical entries
- Incorrect variables removed: {y}
- Duplicate entries consolidated: {z}
- Misplaced items moved: {w}
- Top-journal filtering applied: {v} tables

Cross-links created:
- [[variables/{alt1}]] → [[variables/{canonical}]]
- [[variables/{alt2}]] → [[variables/{canonical}]]

Remaining for manual review:
- {concept pair} - 75% similarity, user decision required
```

---

## Detection Patterns

### Similar Variables

Two types of similarity to detect:

#### Type A: Identical Computation

**Pattern**: Same formula with different variable names

**Examples**:
```
| Ln(NVisit) | ln(1 + number of visits)          |  ← IDENTICAL to Visit_Num
| Visit_Num  | ln(1 + number of site visits)     |  ← IDENTICAL to Ln(NVisit)
```

**Detection**:
1. Normalize computation formulas (remove whitespace, standardize notation)
2. Compare normalized strings
3. Flag identical formulas (100% match after normalization)

#### Type B: Conceptually Similar (Same Underlying Measurement)

**Pattern**: Variables that measure the SAME underlying phenomenon but use different operationalization approaches (count, capped count, log, indicator, ratio, etc.)

**Examples**:
```
| Visit      | Indicator=1 if visited, 0 otherwise    | ← All measure VISITOR COUNT
| Visit_freq | 2 if ≥2 visits, 1 if 1, 0 if none      | ← All measure VISITOR COUNT  
| Ln(NVisit) | ln(1 + number of visits)               | ← All measure VISITOR COUNT
| Visit_Num  | ln(1 + number of site visits)          | ← All measure VISITOR COUNT
```

**Detection**:
1. Extract the underlying measurement target from computation:
   - What is being counted/measured? (e.g., "number of visits", "number of visitors")
   - What data source? (e.g., "brokerage firm", "analyst", "investors")
2. Group variables by underlying measurement target
3. Flag all variables measuring same target (even with different formulas)

**Key insight**: A capped count, a log transform, and a raw indicator of the same underlying phenomenon are ALTERNATIVE OPERATIONALIZATIONS, not different variables. They should be consolidated.

**Consolidation approach**:
- **Canonical**: Choose most commonly used OR most precise formula
- **Cross-links**: Alternative operationalizations point to canonical with note about formula difference
- **Concept table note**: "Also measured as: {alt1} (capped), {alt2} (indicator), {alt3} (log)"

### Incorrect Variables (Not Measuring Concept)

**Pattern**: Variable's computational definition doesn't measure the concept

**Example**: Corporate Site Visit concept should have visit occurrence/frequency proxies, NOT:
```
| ABN_ABSAR | (ABSAR_event - MEAN) / STD | ← INCORRECT - measures stock returns, not visits
```

**Detection**:
1. Parse concept definition keywords
2. Check if variable computation contains relevant measurement terms
3. Flag variables that measure different outcomes

### Duplicate Consequences (Parenthetical Qualifiers)

**Pattern**: Same base consequence listed multiple times with qualifiers

**Examples**:
```
| Stock price impact (overall)        | ← Base consequence
| Stock price impact (info env)       | ← DUPLICATE - move to Heterogeneity
| Stock price impact (manufacturing)  | ← DUPLICATE - move to Heterogeneity
```

**Detection**:
1. Extract base consequence name (remove parenthetical)
2. Count occurrences of same base name
3. Flag duplicates (>1 entry with same base)

### Misplaced Moderators

**Pattern**: Entries describing heterogeneity conditions

**Keywords**: "moderation", "who benefits", "when effect stronger", "X amplifies", "heterogeneity"

**Fix**: Move to **Heterogeneity** subsection under main consequence

### Misplaced Behavioral Responses

**Pattern**: What subjects DO in response to concept

**Keywords**: "decisions", "choices", "behavior", "response", "adjustment"

**Distinction**:
- **Consequence**: Outcome HAPPENS TO subject/world (forecast accuracy improves)
- **Behavioral Response**: Subject DOES something (analysts choose to visit)

**Fix**: Move to **Determinants** section (if explaining why concept varies) or add **Behavioral Response** subsection

### Misplaced Validity Tests

**Pattern**: Tests confirming consequence is "real"

**Keywords**: "validate", "confirm", "rule out", "falsification", "robustness", "alternative explanation"

**Fix**: Move to **Validity Tests** section

---

## Proper Structure Template (Concepts)

```markdown
## Economic Consequences of {Concept}

{Concept} generates {N} primary outcomes: {outcome1}, {outcome2}.

### {Outcome Category 1}

| Consequence | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| {Main consequence} | {Mechanism} | [[source]] | {Key statistic} |

**Heterogeneity**: Effects stronger for {condition1}, {condition2}; weaker for {condition3}.

### {Outcome Category 2}

| Consequence | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| {Main consequence} | {Mechanism} | [[source]] | {Key statistic} |

**Heterogeneity**: {Who benefits more / when effect stronger}.

## Validity Tests

| Test | Purpose | Key Paper | Finding |
|------|---------|-----------|---------|
| {Falsification test} | Rule out {alternative} | [[source]] | {Result} |
```

---

## Examples

### Corporate_Site_Visit (Before/After)

**Before**: 16 entries in Economic Consequences including duplicates, moderators, incorrect variable
**After**: 3 categories with Heterogeneity notes, Validity Tests section

**Constructs & Variables Fix**:
- `Ln(NVisit)` + `Visit_Num` → canonical `Ln_NVisit`, cross-links created
- `Visit_freq` → cross-link to `Ln_NVisit` (similar but capped formula)
- `ABN_ABSAR` → removed (not a site visit proxy)

### Information_Acquisition (Before/After)

**Before**: Duplicate determinants, misplaced behavioral response
**After**: Consolidated determinants + Behavioral Response subsection