---
name: kb-wiki
description: Internal helper skill with wiki page creation, updating, and merging rules. Called by kb-ingest extraction subagent and orchestrator for wiki page management.
---

# kb-wiki - Wiki Creation & Update Helper

This skill provides wiki page creation rules for kb-ingest. Used by both the extraction subagent (Phase 3) to create initial pages and the orchestrator (Phase 4) to review and merge.

## Templates

Templates are in `templates/`:

- `concept.md` - Concept wiki page template
- `construct.md` - Construct wiki page template (for analytical models)
- `method.md` - Method wiki page template
- `method_analytical.md` - Analytical model method template
- `theory.md` - Theory wiki page template
- `variable.md` - Variable wiki page template

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

### 3. Methods → wiki/methods/{method}.md

Use `templates/method.md` structure. Only create for novel designs/models.

| Template Section | Source | Required? |
|------------------|--------|-----------|
| Description | Methods section overview | **YES** |
| Steps | Method procedure | **YES** |
| When To Use | When method is applicable | If discussed |
| Requirements | Data, tools, assumptions needed | If available |
| Limitations | What method cannot do | If discussed |
| Papers Using | Link to summary | **YES** |

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
| Mathematical Representation | Model equations | **YES** |
| Role in Model | How construct is used | **YES** |
| Papers Using | Link to summary | **YES** |

## What to Create vs Skip

### Methods Filtering

**SKIP** - NO wiki/methods/ page for:
- Standard econometric methods: OLS, Fixed Effects, Random Effects
- Standard causal identification: 2SLS, GMM, DiD exploiting new regulation/law as exogenous shock, Regression Discontinuity (unless novel threshold)
- Standard data methods: Panel data construction, variable winsorization

**CREATE** wiki/methods/ page for:
- Analytical/model papers: Full model specifications, assumptions, derivations, proofs
- Novel identification designs: Unique research design settings for causality
- Novel methodological contributions: New measurement approaches, new estimators, new tests

### Variables Filtering

**CREATE** wiki/variables/ page for (directly measurable):
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

### Analytical Model Papers

Paper is an analytical model if:
- No empirical data or sample description
- Contains formal mathematical model with equations
- Results are proofs/theorems, NOT coefficient estimates
- "Variables" are model parameters (symbols like λ, σ²), not observable measures

For analytical models:
- **SKIP wiki/variables/** — model parameters are theoretical constructs
- **CREATE wiki/constructs/{construct}.md** for model parameters and definitional constructs
- **CREATE wiki/methods/{model}.md** using templates/method_analytical.md
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
