---
name: kb-wiki
description: Internal helper skill with wiki page creation, updating, and merging rules. Called by kb-ingest extraction subagent and orchestrator for wiki page management.
---

# kb-wiki - Wiki Creation & Update Helper

This skill provides wiki page creation rules for kb-ingest. Used by both the extraction subagent (Phase 3) to create initial pages and the orchestrator (Phase 4) to review and merge.

## Template Path

Read templates from `templates/*.md` in kb-plugin root. If working from a subdirectory and path fails, use absolute path `kb-plugin/templates/*.md`.

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

## Cross-Linking Conventions

- All wiki pages use Obsidian [[filename]] links
- Concepts link to their constructs, variables, theories
- Variables link to their concept
- New pages include `first_used` or `first_defined` linking to summary
- When updating existing page: add paper to Papers Using section, merge any new content
