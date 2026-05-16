---
name: kb-extract
description: Internal helper skill with extraction guidance for concepts, theories, variables from paper markdown. Wiki creation guidance moved to kb-wiki. Called by kb-ingest, not invoked directly by user.
---

# kb-extract - Knowledge Extraction Helper

This skill provides extraction guidance for kb-ingest's Phase 3 subagent. The subagent reads the paper, creates the summary, and drafts wiki pages — kb-extract defines what to extract and how to format it.

## Paper Type Detection

Select template based on paper type:

| Paper Type | Criteria | Template | Detailed Guidance |
|------------|----------|----------|-------------------|
| **Archival** | Existing data sources, observational | `templates/paper_summary_archival.md` | `references/archival_extract_guidance.md` |
| **Experimental** | Manipulated variables, treatment/control, subjects | `templates/paper_summary_experimental.md` | See Experimental Papers section |
| **Analytical** | No empirical data, mathematical model, proofs | `templates/paper_summary_analytical.md` | See Analytical Model Papers section |
| **Survey** | Questionnaires, interviews, opinions/judgments/knowledge | `templates/paper_summary_survey.md` | `references/survey_extract_guidance.md` |
| **Review** | Literature survey on specific concept, synthesizes findings | Minimal summary (wiki consolidation) | `references/review_extract_guidance.md` |

## Current Workflow

**Standard workflow** (archival, experimental, analytical, survey):
```
Subagent (read paper → create summary → self-verify → create wiki) → Orchestrator (review & merge)
```

**Review workflow** (different):
```
Subagent (check concept wiki → create/update concept wiki → minimal summary) → Orchestrator (quality check)
```

The subagent handles all heavy lifting. The orchestrator only does lightweight quality checks and collision resolution.

## Wiki Creation Trigger

**CRITICAL**: After completing the summary, you MUST create wiki pages for all entries with Wiki Page links.

### Trigger Tables

Check each summary table for Wiki Page column:

| Table | Wiki Page Column | Action |
|-------|-------------------|--------|
| Concepts Defined | `[[concepts/{name}]]` | Create if page doesn't exist |
| Measures/Variables | `[[variables/{name}]]` or `[no wiki]` | Create for `[[variables/{name}]]` entries |
| Ground Theories (experimental) | `[[theories/{name}]]` | **CHECK FIRST** - semantic duplicate check → create using theory_exp.md or update existing page with evidence |
| Model Parameters & Constructs (analytical) | `[[constructs/{name}]]` | Create if page doesn't exist |

### Survey-Specific Wiki Naming

Survey wiki naming differs from other types:

| Category | Naming | Marker |
|----------|--------|--------|
| Concepts | Standard `[[concepts/{concept}]]` | NO `_survey` |
| Variables (grouped) | `[[variables/{dimension}_survey]]` | YES `_survey` |
| Methods (instruments) | `[[methods/{instrument}_survey_instrument]]` | YES `_survey_instrument` |

**Key**: Variables = questions grouped by dimension (one page per dimension, NOT per question).

## Ground Truth Format by Paper Type

All paper types have Ground Truth Findings (most objective results), but **format differs by type**:

| Paper Type | Ground Truth Format | Example |
|------------|--------------------|---------|
| **Archival** | Regression coefficient: `Variable X (defined as [formula]) has β=YY (p<ZZ) in [model] (n=XXXX)` | `ROA (defined as net income/assets) has β=0.15 (p<0.01) in OLS (n=500)` |
| **Experimental** | Manipulated/dependent relationship: `With subjects from {background}, {X} is {relation} to {Y} (p=ZZ, n=XXXX)` | `With MBA students, manipulated incentive is positively related to effort (p<0.05, n=120)` |
| **Survey** | Question results: `Question {Q1-Q3} (grouped as {dimension}) shows {result}` | `Question Q1-Q3 (Budget Setting) shows 65% report moderate participation` |
| **Analytical** | Theorem/Proposition: `**Theorem N** - {statement with conditions}` | `**Theorem 5** - If σ_x² = 0, equilibrium does not exist if e^ac < √(1+n)` |
| **Review** | NO Ground Truth (consolidates existing findings) | — |

**Detailed format guidance**: See type-specific reference files.

### Methods Creation Trigger

If summary Methods section contains:
- `→ Create wiki/methods/{method_name}` — Create wiki/methods/{method_name}.md
- "no wiki page created" — SKIP

### Wiki Creation Process

For each Wiki Page link `[[category/name]]` in tables:

1. **Semantic duplicate check**: Follow `kb-wiki` Pre-Creation Semantic Check
2. **If duplicate found**: Update existing page instead of creating new
3. **If no duplicate**: Create new page using `kb-wiki/templates/{category}.md`
4. **Fill template**: Use information from summary table row

**DO NOT skip wiki page creation** — this is essential for knowledge base structure.

## Paper-Type-Specific Guidance

### Archival Papers

For detailed archival extraction guidance (hypothesis argument structure, methods filtering, ground truth format), see:

→ **`references/archival_extract_guidance.md`**

Key archival-specific topics covered:
- Hypothesis extraction with argument structure analysis
- Methods filtering for econometric methods
- Claim-Ground Truth correspondence rules
- Regression coefficient format

### Survey Papers

For detailed survey extraction guidance (question grouping, survey design, wiki naming), see:

→ **`references/survey_extract_guidance.md`**

Key survey-specific topics covered:
- Ground truth format for question-based results
- Concepts extraction (easier than archival)
- Variables = survey questions (grouped by dimensions)
- Survey Design extraction (instrument, reliability, non-response)
- Face-to-face interview specifics
- Wiki naming with `_survey` marker

### Analytical Model Papers

Paper is an analytical model if:
- No empirical data or sample description
- Contains formal mathematical model with equations
- Results are proofs/theorems, NOT coefficient estimates
- "Variables" are model parameters (symbols like λ, σ²), not observable measures

**Summary Requirements for Analytical Papers**:

1. **Claim Findings FIRST**: 3-5 key theoretical implications
2. **Ground Truth Findings SECOND**: 3-5 theorems/propositions
3. **Correspondence**: Claim N should be supported by Theorem/Proposition N

**Extraction Rules for Analytical Models**:

1. **SKIP wiki/variables/** - Model parameters are theoretical constructs, NOT observable
2. **CREATE wiki/constructs/{construct}.md** for:
   - Model parameters (λ, σ_ε², a, c, etc.)
   - Definitional constructs (Informed Traders, Price Informativeness, etc.)
3. **CREATE wiki/methods/{model}.md** using kb-wiki/templates/method_analytical.md
4. **Ground Truth Findings**: Use Theorem/Proposition format
   ```
   Finding 1: **Theorem 5** - If σ_x² = 0 (no noise), equilibrium does not exist if e^ac < √(1+n).
   ```
5. **Model Variations Table**: Extract comparative statics

### Experimental Papers

Experimental papers differ from archival in structure:
- **Methods section**: Focus on experimental design, not econometric methods
- **Ground Truth format**: Manipulated/dependent variable relationship
- **Ground Theories**: Link to existing theories (experimental papers test pre-existing theories)

For detailed experimental extraction guidance (manipulation handling, wiki accumulation), see:

→ **`references/experimental_extract_guidance.md`**

**Summary Requirements for Experimental Papers**:

1. **Claim Findings FIRST**: 3-5 key interpretations with problem context
2. **Ground Truth Findings SECOND**: 3-5 objective results (manipulated/dependent relationship)
3. **Correspondence**: Claim N should be supported by Finding N

**Hypothesis in Experimental Papers**:
- Experimental papers CAN develop hypotheses (predicting manipulation effect)
- If hypothesis exists, use archival guidance argument structure analysis
- See template `paper_summary_experimental.md` for experimental-specific sections:
  - Ground Theories (link to existing theories)
  - Experimental Design (design type, control group, randomisation, counterbalancing)
  - Manipulations (manipulation methods overview across studies)
  - The Context (external validity factors)

### Review Papers

Review papers have a **different workflow**—they consolidate wiki pages, not extract full summaries.

→ **`references/review_extract_guidance.md`**

Key review workflow:
1. Check if concept wiki page exists
2. Create concept page if not exists
3. Update existing concept page if exists
4. Create minimal summary (not full template)
5. Only create page for main concept

**Review papers do NOT use full summary template.**

## Hypothesis Extraction (Multiple Paper Types)

**Papers that CAN develop hypotheses**:
- **Archival**: Most common—theoretical arguments with empirical testing
- **Survey**: Theory-driven causal predictions (Brown 1995: need good theory)
- **Experimental**: Predicting manipulation effect on dependent variable
- **Analytical**: Propositions derived from model assumptions

**Papers that typically DO NOT develop hypotheses**:
- **Review**: Consolidates existing hypotheses
- **Descriptive surveys**: No causal predictions

### Argument Structure Analysis

For all papers with hypotheses (archival, survey, experimental), use the argument structure analysis from:

→ **`references/archival_extract_guidance.md`** → "Hypothesis Extraction" section

This includes:
- Premise identification and classification
- Deductive vs Inductive reasoning approach
- Sound/Unsound/Cogent/Uncogent evaluation

## Where to Find Concepts

**Key sections for concept definitions** (applies to all paper types):
1. **Introduction** - Authors introduce concepts and their importance
2. **Hypothesis Development** - Explicit concept definitions for hypothesis testing
3. **Literature Review** - Background definitions from prior work

**Survey papers**: Concepts easier to extract—from research question, title, introduction.

**If no explicit definition found**:
- Provide a **common-sense definition** based on context
- Mark with `[common-sense definition, not explicitly defined in paper]`

## Concept Extraction Rules

### KEEP ONLY Main Concepts
- Focus on concepts central to the paper's hypotheses and findings
- NOT every mentioned term or peripheral concepts

### Separate Concepts from Constructs
- **Concepts**: Abstract theoretical ideas (not directly observable)
- **Constructs**: Multi-item measures that operationalize concepts
- **Proxies/Variables**: Single computational measures

**Example**:
- Concept: "Managerial Labor Classifications" = a market where managers share similar talents
- Constructs: Industry match, Compensation peer group match (measure if two managers are in same classification)
- Proxies: `SameIndustry` = 1 if both firms in same SIC code, `PeerGroupMatch` = 1 if both in compensation peer group

## Variable Naming Guidelines

**Paper Variable** = exact name from paper (use in Ground Truth findings)
**Wiki Name** = common-sense descriptive name (use in wiki page title)

| Paper Variable | Wiki Name | Wiki Created? | Reason |
|----------------|-----------|---------------|--------|
| InDegree | Peer_Selection_Count | YES | Describes what it counts |
| PCOMP1 | [derived] | NO | PCA component, not directly measurable |
| Talent_Flow | Executive_Move | YES | Describes the observable event |

**Wiki naming rules**:
1. Wiki Name should describe what the variable **directly measures**
2. Use common terms that a reader can understand without context
3. Include measurement type if helpful (Count, Rate, Indicator, Ratio)
4. If no wiki page: Wiki Name = "[derived]" or "[composite]"

**Variable wiki page criteria** (applies to archival, experimental, survey):
- CREATE for: raw counts, indicators, ratios from raw data, observable measurements
- SKIP for: PCA components, constructed indices, standardized variables, fitted values, control variables

## Related Skills

- **kb-wiki**: Wiki page creation, updating, filtering, and cross-linking conventions. Use kb-wiki for all wiki page creation/update rules and template mappings.

## Templates

Four paper summary templates based on paper type:

- `templates/paper_summary_archival.md` - Archival/empirical papers
- `templates/paper_summary_experimental.md` - Experimental papers
- `templates/paper_summary_analytical.md` - Analytical model papers
- `templates/paper_summary_survey.md` - Survey papers

**Review papers**: No full template—use minimal summary format per review guidance.

## References

- `references/archival_extract_guidance.md` - Archival paper detailed guidance
- `references/experimental_extract_guidance.md` - Experimental paper manipulation handling
- `references/survey_extract_guidance.md` - Survey paper detailed guidance
- `references/review_extract_guidance.md` - Review paper wiki consolidation workflow