---
name: kb-wiki
description: Internal helper skill with wiki page creation, updating, and merging rules. Called by kb-ingest extraction subagent and orchestrator for wiki page management.
---

# kb-wiki - Wiki Creation & Update Helper

This skill provides wiki page creation rules for kb-ingest. Used by both the extraction subagent (Phase 3) to create initial pages and the orchestrator (Phase 4) to review and merge.

## Templates

Templates are in `templates/`:

### Concept/Theory/Construct (All Methodologies)
- `concept.md` - Concept wiki page template (domain-agnostic)
- `construct.md` - Construct wiki page template (for analytical models)
- `theory.md` - Theory wiki page template (domain-agnostic, general use)
- `theory_exp.md` - Experimental theory template (with Evidence Supporting/Contradicting tables)

### Variables (Methodology-Specific)
- `variable.md` - Variable wiki page template (archival/experimental - computational formula)
- `variable_survey.md` - Survey variable template (questions grouped by dimension, reliability measures)
- `variable_experimental.md` - Experimental variable template (manipulation/measurement details for replication)

### Methods (Methodology-Specific)
- `method.md` - Method wiki page template (archival - econometric, identification)
- `method_analytical.md` - Analytical model method template
- `method_experimental.md` - Experimental design template (treatment/control, randomization)
- `method_survey_instrument.md` - Survey instrument template (questionnaire, validity, reliability)

## Scripts

- `scripts/check_wiki_collision.py` - Semantic duplicate checker (pre-creation)

## Wiki Page Templates

### 1. Concepts → wiki/concepts/{concept}.md

Use `templates/concept.md` structure. Fill these sections from paper:

| Template Section | Source in Paper | Required? |
|------------------|-----------------|-----------|
| Definition | Introduction, Hypothesis Development, Lit Review | **YES** |
| Alternative Definitions | Literature Review (how others define it) | If available |
| Constructs & Variables | Measures/Variables table from summary | **YES** |
| Related Theories | Theory section mentions | If available |
| Determinants | What causes variation in concept | If discussed |
| Economic Consequences | What outcomes concept affects | If discussed |
| Identification Strategy | How paper identifies/causes concept | If discussed |
| Future Works | Limitations, future research section | If mentioned |

**Naming**: Use concept name from Concepts Defined table. Link first_used to summary.

### 2. Variables → wiki/variables/{variable}.md

**Methodology-specific templates**:

| Paper Type | Template | Key Differences |
|------------|----------|-----------------|
| **Archival/Experimental** | `variable.md` | Single computational formula, validity notes |
| **Survey** | `variable_survey.md` | Questions grouped by dimension, reliability measures, response scale |

#### Archival/Experimental Variables

Use `templates/variable.md` structure. Fill these sections:

| Template Section | Source | Required? |
|------------------|--------|-----------|
| What It Measures | Variables table: Concept + Definition | **YES** |
| Computation | Variables table: Computational Definition | **YES** |
| Data Sources | Methods section | If available |
| Validity Notes | Results/discussion of variable validity | If discussed |
| Alternative Variables | Other measures for same concept | If available |
| Papers Using | Link to summary | **YES** |
| Interpretations | How variable is interpreted | If discussed |

#### Survey Variables

Use `templates/variable_survey.md` structure. Fill these sections:

| Template Section | Source | Required? |
|------------------|--------|-----------|
| What It Measures | Variables table: Concept + Dimension | **YES** |
| Questions Relating to This Dimension | Variables table + Survey Design | **YES** |
| Studies Using This Dimension | Survey Design: Reliability/Validity + summary | **YES** |

**Multi-paper accumulation**:
- Questions table: One row per semantic question group (ONE precise excerpt, combine identical questions)
- Papers column: First + most recent from top journals
- Studies table: One row per paper with paper-specific reliability (α), validity, key findings (Sample removed - details in paper summary)

**Naming**: `{dimension}_survey` for survey variables (questions grouped by dimension).

#### Experimental Variables

Use `templates/variable_experimental.md` structure. Fill these sections:

| Template Section | Source | Required? |
|------------------|--------|-----------|
| What It Measures | Claim Findings: abstract concept level | **YES** |
| Experimental Operationalization (IV) | Manipulations table + Experimental Design | **YES** for manipulated IV |
| Experimental Operationalization (DV) | Measures/Variables + Experimental Design | **YES** for DV |
| Papers Using | Link to summary | **YES** |

**Multi-paper accumulation**:
- For Manipulated IV table: One row per **Condition Type** (Treatment, Control, Hedonic, Utilitarian, etc.)
- **Condition Type column**: Each row = one condition type from one paper
- **Manipulation Method column**: Corresponds to the Condition Type in that row (no `|` separator needed)
- For DV table: One row per paper's measurement approach (Paper, Measurement Method, Scale/Units, Collection Procedure, Validity)
- Selection: First + most recent from top journals for similar manipulation/measurement strategy
- **Same variable stays in ONE page** across all condition types and papers

**Naming**: `{variable}_exp.md` for experimental variables.

**Why experimental needs separate template**:
- Dependent variable: How outcome is **measured** (not formula, but operationalization)
- Independent variable: How treatment is **manipulated** (not computed, but implemented)
- Enable replication: Document exact manipulation/measurement procedures
- Multi-paper: Track how different papers operationalize same variable

### 3. Methods → wiki/methods/{method}.md

**Methodology-specific templates**:

| Paper Type | Template | Key Differences |
|------------|----------|-----------------|
| **Archival** | `method.md` | Econometric models, identification strategies, steps |
| **Analytical** | `method_analytical.md` | Model setup, assumptions, derivations, proofs |
| **Experimental** | `method_experimental.md` | Treatment/control, randomization, counterbalancing |
| **Survey** | `method_survey_instrument.md` | Questionnaire structure, validity, reliability |

#### Archival Methods

Use `templates/method.md` structure. Only create for novel designs/models.

| Template Section | Source | Required? |
|------------------|--------|-----------|
| Description | Methods section overview | **YES** |
| Steps | Method procedure | **YES** |
| When To Use | When method is applicable | If discussed |
| Requirements | Data, tools, assumptions needed | If available |
| Limitations | What method cannot do | If discussed |
| Papers Using | Link to summary | **YES** |

#### Analytical Model Methods

Use `templates/method_analytical.md`. Fill:

| Template Section | Source | Required? |
|------------------|--------|-----------|
| Overview | Model Structure section | **YES** |
| Basic Setup | Key Equations table | **YES** |
| Model Variations | Comparative Statics | If available |
| Papers Using | Link to summary | **YES** |

#### Experimental Designs

Use `templates/method_experimental.md`. Fill:

| Template Section | Source | Required? |
|------------------|--------|-----------|
| Design Structure | Experimental Design: Design Type | **YES** |
| Key Features | Randomization, Control Group, Counterbalancing | **YES** |
| Procedure | Experimental Design: Procedure | **YES** |
| Subject Pool | Experimental Design: Subjects | **YES** |
| External Validity | The Context section | **YES** |
| Papers Using | Link to summary | **YES** |

#### Survey Instruments

Use `templates/method_survey_instrument.md`. Fill:

| Template Section | Source | Required? |
|------------------|--------|-----------|
| Instrument Structure | Measures/Variables table + Survey Design | **YES** |
| Development Process | Survey Design: Survey Instrument | If new instrument |
| Validity Testing | Survey Design section | If tested |
| Reliability Testing | Survey Design: Reliability Measures | **YES** |
| Administration Guidelines | Survey Design section | If available |
| Papers Using | Link to summary | **YES** |

**Naming**: `{instrument}_survey_instrument` for survey instruments.

### 4. Theories → wiki/theories/{theory}.md

Use `templates/theory.md` structure. Fill all sections from paper.

### 5. Constructs → wiki/constructs/{construct}.md

Use `templates/construct.md` structure. For analytical model papers:
- Model parameters (λ, σ_ε², etc.)
- Definitional constructs (Informed Traders, Price Informativeness, etc.)
- Top journal filtering: max 5 entries (oldest + newest)

| Template Section | Source | Required? |
|------------------|--------|-----------|
| Definition | Paper model section | **YES** |
| Role in Model | How construct is used | **YES** |
| Papers Using | Link to summary | **YES** |

**Note**: Mathematical notation varies by paper and is not core knowledge. Do not create "Mathematical Representation" section.

## What to Create vs Skip

### Methods Filtering (by Paper Type)

#### Archival Papers

**SKIP** - NO wiki/methods/ page for:
- Standard econometric methods: OLS, Fixed Effects, Random Effects
- Standard causal identification: 2SLS, GMM, DiD exploiting new regulation/law as exogenous shock, Regression Discontinuity (unless novel threshold)
- Standard data methods: Panel data construction, variable winsorization

**CREATE** wiki/methods/{method}.md (using `method.md`) for:
- Novel identification designs: Unique research design settings for causality
- Novel methodological contributions: New measurement approaches, new estimators, new tests

#### Analytical Model Papers

**CREATE** wiki/methods/{baseline_model}.md (using `method_analytical.md`) for:
- **Baseline/classical model** that subsequent variations stem from
- The foundational model that defines the theoretical framework
- Example: `Noisy_Rational_Expectations_Model.md` for Grossman-Stiglitz (1980) baseline

**ADD TO VARIATIONS** (in baseline page's Model Variations table) for:
- Model variations with modified assumptions from baseline
- Extensions that generate **significant new insights** or **different predictions**
- Subsequent papers using same model family with modifications

**SKIP** - NO wiki/methods/ page for:
- Model variations without significant new insights
- Minor parameter adjustments
- Variations already documented in baseline page's Model Variations table

**Reference**: See `references/Noisy_Rational_Expectations_Model.md` for example of baseline + variations structure.

#### Experimental Papers

**SKIP** - NO wiki/methods/ page for:
- Standard designs: Simple post-test only control group, simple pre/post-test
- Standard factorial designs without methodological innovation

**CREATE** wiki/methods/{design}_experimental.md (using `method_experimental.md`) for:
- Novel experimental designs: Unique treatment structures, novel control mechanisms
- Complex factorial designs with innovative methodology
- Field experiments with unique settings

#### Survey Papers

**SKIP** - NO wiki/methods/ page for:
- Well-established instruments from prior research (already documented)
- Standard survey administration procedures

**CREATE** wiki/methods/{instrument}_survey_instrument.md (using `method_survey_instrument.md`) for:
- Novel survey instruments: New questionnaires with validity/reliability testing
- Modified established instruments with significant changes

### Variables Filtering (by Paper Type)

### Theories Filtering (Experimental Papers - Ground Theories)

**CRITICAL for Experimental Papers**: The summary's Ground Theories table links to `[[theories/{theory}]]`. These are theories **referenced from prior literature** (not necessarily novel theories contributed by the paper).

**ALWAYS CHECK FIRST, THEN CREATE OR UPDATE**:

1. **Pre-creation semantic check**: Follow Pre-Creation Semantic Check process
2. **If page exists**: Update existing page - add paper to Evidence Supporting/Contradicting tables
3. **If no page**: Create new page using `templates/theory_exp.md`

**Use template**: `templates/theory_exp.md` (experimental-specific with evidence tables)

**Evidence table selection criteria**:
- **Oldest 2** from top journals (earliest experimental tests)
- **Newest 3** from top journals (most recent experimental tests)
- Max 5 papers total per table (Evidence Supporting + Evidence Contradicting)

**Evidence Supporting table columns**: Paper, Journal, Year, Experimental Design, Key Finding, Support Type
**Evidence Contradicting table columns**: Paper, Journal, Year, Experimental Design, Contradictory Finding, Nature of Contradiction

**Theory Types**:
| Theory Type | Original Source | Wiki Content Focus |
|-------------|-----------------|---------------------|
| Referenced (prior literature) | Link to original paper [[source/summary/{citekey_origin}]] | Core propositions + how this paper tests/applies |
| Novel (paper's contribution) | Link to this paper | New theoretical framework introduced |

**Example**:
- Paper: "Warmth and Competence in Consumer Judgment" (2024)
- Ground Theories table: Stereotype Content Model → [[source/summary/cuddy2008_summary]]
- Action: Check if wiki/theories/Stereotype_Content_Model.md exists
- If exists: Add 2024 paper to Evidence Supporting table
- If not exists: CREATE using theory_exp.md, link to Cuddy 2008 as original source

#### Archival Papers

**CREATE** wiki/variables/{variable}.md (using `variable.md`) for (directly measurable):
- Raw counts: Number of items
- Indicators: Binary variables (0/1 flags)
- Ratios from raw data: Proportions, percentages
- Network statistics: Degree, clustering coefficient
- Observable measurements: Directly countable/measurable

**SKIP** - NO wiki page for (derived/composite):
- PCA components: Principal components
- Constructed indices: Variables combining multiple measures
- Standardized variables: Z-scores, normalized versions
- Fitted/predicted values: Outputs from regression models
- Generic names: Non-descriptive names applicable to any paper
- Control variables not essential to the paper

#### Experimental Papers

**CREATE** wiki/variables/{variable}_exp.md (using `variable_experimental.md`) for:
- **Dependent variables**: Measured outcome variables (how outcome is operationalized)
- **Manipulated independent variables**: Treatment variables (how manipulation is implemented)

**Key documentation for replication**:
- Measurement method for DV (scale, procedure, reliability)
- Manipulation method for IV (treatment levels, control condition, manipulation check)
- External validity factors (task complexity, incentives, location)

**SKIP** - NO wiki page for:
- Subject characteristics (background variables, not manipulated)
- Control variables not essential to experimental design

#### Survey Papers

**CREATE** wiki/variables/{dimension}_survey.md (using `variable_survey.md`) for:
- Question dimensions: Multiple questions measuring one aspect of concept
- With reliability measures: Cronbach's alpha, test-retest
- With response scale: Likert, scalar, yes-no

**SKIP** - NO wiki page for:
- Individual single questions (must be grouped by dimension)
- Derived survey indices (PCA from survey responses)

### Analytical Model Papers

Paper is an analytical model if:
- No empirical data or sample description
- Contains formal mathematical model with equations
- Results are proofs/theorems, NOT coefficient estimates
- "Variables" are model parameters (symbols like λ, σ²), not observable measures

For analytical models:
- **SKIP wiki/variables/** — model parameters are theoretical constructs
- **CREATE wiki/constructs/{innovative_construct}.md** ONLY for:
  - **Innovative theory constructs** that extend existing frameworks
  - New definitional constructs specific to this paper's contribution
  - Novel conceptual entities introduced by the paper
- **SKIP wiki/constructs/** for:
  - Standard constructs from classical models (already documented)
  - Model parameters from baseline models (documented in baseline method page)
  - Common constructs used across multiple existing papers (update existing page instead)
- **CREATE wiki/methods/{baseline_model}.md** using templates/method_analytical.md
- Ground Truth: Use Theorem/Proposition format

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
2. Use common terms understandable without context
3. Include measurement type if helpful (Count, Rate, Indicator, Ratio)
4. If no wiki page: Wiki Name = "[derived]" or "[composite]"

## Pre-Creation Semantic Check

**CRITICAL**: Before creating ANY new wiki page, you MUST check for semantic duplicates across ALL categories: concepts, variables, methods, constructs, theories.

### Step 0: IMA Knowledge Base Check

First, verify IMA knowledge bases are available:

1. Read `kb-skill/SKILL.md` for required KB list
2. Run: `ima_api "openapi/wiki/v1/search_knowledge_base" '{"query": "", "cursor": "", "limit": 20}'`
3. Check if KB `{category}` exists (e.g., `concepts`, `variables`, `methods`, `constructs`, `theories`)

**If KB missing**: Prompt user: "请在IMA桌面客户端创建知识库: {category}，并上传 wiki/{category}/ 目录下的所有 .md 文件。创建后重试。"

**If KB exists**: Proceed to Step 1 using ima search.

### Step 1: Search Existing Pages via IMA

For each page you plan to create:

**Primary method (IMA KB available):**
```bash
# Search within specific category KB
ima_api "openapi/wiki/v1/search_knowledge" '{"query": "{page_name}", "knowledge_base_id": "{kb_id}", "cursor": ""}'
```

- Use the page name as `query`
- Use `{category}` KB's ID (from Step 0)
- Review `highlight_content` in results for definition snippets
- Check both exact matches and similar-name entries

**Fallback (IMA KB not available):**
```bash
# File-based search
Glob wiki/{category}/*.md
Read wiki/{category}/{similar_name}.md
```

### Step 2: Category-Specific Semantic Rules

#### Concepts (wiki/concepts/)

**MERGE INTO EXISTING if:**

| Relationship Type | Example | Action |
|-------------------|---------|--------|
| **Mathematical reciprocal/transform** | Market-to-Book vs Book-to-Market | ONE page; note formula variants |
| **Specific case of general** | Announcement_Abnormal_Return ⊂ Cumulative_Abnormal_Returns | ONE page for general; note specific variant |
| **Prefix/suffix variation** | "Reporting_Conservatism" vs "Conservatism" | Merge into base if same phenomenon |
| **Synonym definitions** | "Earnings Informativeness" vs "ERC" (if same phenomenon) | Merge with alternative names section |
| **Same phenomenon, different wording** | Basu's conservatism vs Givoly-Hayn's conservatism | ONE page with alternative definitions table |

**KEEP SEPARATE if:**
- Different underlying phenomenon (e.g., Timeliness vs Asymmetric_Timeliness)
- One is cause, other is consequence (e.g., Conservatism → Asymmetric_Persistence)

#### Variables (wiki/variables/)

**MERGE INTO EXISTING if:**

| Relationship Type | Example | Action |
|-------------------|---------|--------|
| **Mathematical reciprocal** | Market/Book (M/B) vs Book/Market (B/M) | ONE page; note M/B = 1/B/M |
| **Log transformation** | ln(MarketCap) vs MarketCap | ONE page; note log variant in computation |
| **Same computation, different name** | "Annual_Return" vs "Stock_Return" (same formula) | ONE page with alternative names |
| **Same variable, different window** | 3-day CAR vs 5-day CAR vs announcement CAR | ONE page; note window variants |

**KEEP SEPARATE if:**
- Different formulas for purportedly same concept (cross-link but separate)
- Different data sources yield different measures (note distinction)

#### Methods (wiki/methods/)

**MERGE INTO EXISTING if:**

| Relationship Type | Example | Action |
|-------------------|---------|--------|
| **Same core procedure, different label** | "Basu Regression" vs "Asymmetric Timeliness Model" (same equation) | ONE page; note alternative names |
| **Minor variation of existing method** | Basu (1997) vs modified Basu with controls | ONE page; note variations in Model Variations table |
| **Same analytical model, different paper** | Multiple papers using same Kyle (1985) model | ONE method page; note each paper in Model Variations |

**KEEP SEPARATE if:**
- genuinely novel design (new identification strategy, new estimator)
- Different model structure (different equations, assumptions)

#### Constructs (wiki/constructs/)

**MERGE INTO EXISTING if:**

| Relationship Type | Example | Action |
|-------------------|---------|--------|
| **Same model parameter** | λ (informed trading intensity) across papers using same model | ONE page; note papers in "Papers Using" |
| **Same definitional construct** | "Informed Traders" across Kyle-model papers | ONE page; add each paper's context |
| **Same symbol, same role** | σ² (variance parameter) in same model family | ONE page |

**KEEP SEPARATE if:**
- Same symbol but different meaning in different models (cross-link with disambiguation)
- Different construct in different theoretical framework

#### Theories (wiki/theories/)

**MERGE INTO EXISTING if:**

| Relationship Type | Example | Action |
|-------------------|---------|--------|
| **Same theoretical framework** | "Contracting Theory" vs "Contract Theory" | ONE page; note alternative names |
| **Same core proposition** | Multiple papers deriving same proposition | ONE page; note papers |

**KEEP SEPARATE if:**
- Different theoretical frameworks (e.g., Agency Theory vs Signaling Theory)
- Competing explanations for same phenomenon

### Step 3: Definition Comparison

Compare definitions at the **phenomenon/mechanism level**:
- **Same underlying phenomenon/mechanism?** → Merge
- **Different phenomenon despite keyword overlap?** → Keep separate with cross-link
- **One is subset of the other?** → ONE page (general notes specific variants)

### Cross-Category Checks

Before creating a page in one category, check if it belongs in another:
- **Variable that's actually a concept?** → concepts/ not variables/
- **Method that's standard?** → SKIP (no wiki page)
- **Construct from empirical paper?** → May be concept/ not constructs/
- **Theory from single paper?** → May be concept/ not theories/

## Cross-Linking Conventions

- All wiki pages use Obsidian [[filename]] links
- Concepts link to their constructs, variables, theories
- Variables link to their concept
- New pages include `first_used` or `first_defined` linking to summary
- When updating existing page: add paper to Papers Using section, merge any new content
