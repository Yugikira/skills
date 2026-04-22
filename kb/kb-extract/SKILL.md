---
name: kb-extract
description: Internal helper skill that extracts concepts, theories, variables from converted paper markdown. Called by kb-ingest, not invoked directly by user.
---

# kb-extract - Knowledge Extraction Helper

This skill is called by kb-ingest to extract structured knowledge from converted paper markdown files.

## Efficient Workflow

**Token-minimized approach**:
1. **Orchestrator** creates summary directly (reads paper once)
2. **kb-verify agent** provides simple YES/NO feedback (separate skill)
3. **Orchestrator** revises if needed

```
Orchestrator (read paper → create summary) → kb-verify (check) → Orchestrator (revision)
```

## Hypothesis Extraction

### Where to Find Hypotheses
- **Hypothesis Development section**: Explicit H1, H2 statements
- **Introduction**: Research questions that imply hypotheses
- **Theory section**: Propositions derived from theory

### If No Explicit Hypothesis
Write: "No explicit hypothesis stated in this paper. The paper is a {descriptive paper type: empirical exploration | descriptive analysis | methodological contribution}."

### Argument Structure Analysis
1. **Identify premises** (supporting evidence/claims for the hypothesis)
2. **Classify each premise source**:
   - Literature-based (prior findings)
   - Theory-based (logical derivation)
   - Assumption-based (taken as given)
   - Data-based (empirical observation)
3. **Determine reasoning approach**:
   - **Deductive**: Conclusion necessarily follows (mathematical/logical certainty)
   - **Inductive**: Conclusion probabilistically follows (empirical generalization)
4. **Evaluate**:
   - Deductive papers: **Sound** if valid AND all premises empirically true; **Unsound** otherwise
   - Inductive papers: **Cogent** if strong AND all premises empirically true; **Uncogent** otherwise

## Methods Filtering Criteria

### SKIP - Do NOT create wiki/methods/ page for:

**Standard econometric methods**:
- OLS, Fixed Effects, Random Effects
- Standard tests: t-tests, F-tests, Hausman tests, White tests

**Standard causal identification methods**:
- 2SLS (Two-stage least squares)
- GMM (Generalized method of moments)
- DiD (Difference-in-differences) - unless novel design setting
- Regression Discontinuity - unless novel threshold/cutoff design

**Standard data methods**:
- Panel data construction, variable winsorization

### CREATE wiki/methods/ page for:

- **Analytical/model papers**: Full model specifications, assumptions, derivations, proofs
- **Novel identification designs**: Unique research design settings for causality (e.g., novel instrument, novel DiD setting with special threshold)
- **Novel methodological contributions**: New measurement approaches, new estimators, new tests
- **Combined approaches**: Novel combinations of standard methods with unique twist

### Methods Section in Summary

**If using standard methods only**:
```markdown
## Methods
- **Standard Methods**: OLS with Industry×Year fixed effects (no wiki page created)
- **Data**: {data sources}, n={sample size}
```

**If novel design/model**:
```markdown
## Methods
- **Novel Design**: {description of what makes it novel}
- **Model**: {key equations or framework}
→ Create wiki/methods/{method_name}.md
```

## Where to Find Concepts

**Key sections for concept definitions**:
1. **Introduction** - Authors introduce concepts and their importance
2. **Hypothesis Development** - Explicit concept definitions for hypothesis testing
3. **Literature Review** - Background definitions from prior work

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

## Summary Requirements

### Claimed Findings: 3-5 Key Interpretations FIRST

Select the authors' **main theoretical claims**:
- What they conclude from the empirical results
- The story they tell about why results matter

**Write Claims BEFORE Ground Truth** - this establishes the interpretive framework first.

### Ground Truth Findings: 3-5 Key Findings SECOND

Select the **most important** empirical results:
- Main coefficients from primary regression tables
- Key novel variables/measures from the paper
- Statistically significant results (p<0.05 or better)

**Correspondence Requirement**: The first N Ground Truth findings should directly support the N Claimed findings above. Finding 1 supports Claim 1, Finding 2 supports Claim 2, etc.

DO NOT extract every finding. Quality over quantity.

### Ground Truth Format

Each finding must be **reproducible** - use the paper's actual variable names:

```
{Paper Variable Name} (defined as [exact formula from paper]) has coefficient β=YYY (p<ZZ) in [model type] (n=XXXX).
```

**Key rules**:
- Use **paper's exact variable names** (e.g., "PCOMP1", "InDegree") - be honest to the paper
- Include computational definition from paper (Results section, Variable Definitions)
- If a variable is defined once, subsequent findings can reference "see Finding N" or "see Variables table"
- The Variables table maps paper names to common-sense wiki names

## Measures/Variables Filtering Criteria

### Wiki Page Criteria

**CREATE wiki/variables/ page for** (directly measurable/basic):
- **Raw counts**: Number of items (e.g., peer selections, employees, transactions)
- **Indicators**: Binary variables (0/1 flags for observable events)
- **Ratios from raw data**: Computable from observable inputs (e.g., proportions, percentages)
- **Network statistics**: Directly computed from network structure (e.g., degree, clustering coefficient)
- **Observable measurements**: Variables that can be directly counted/measured

**SKIP - NO wiki page for** (derived/composite):
- **PCA components**: Principal components (e.g., PCOMP1, PCOMP2) - these are constructed indices
- **Constructed indices**: Variables combining multiple measures through mathematical transformation
- **Standardized variables**: Z-scores, normalized versions of other variables
- **Fitted/predicted values**: Outputs from regression models (e.g., "Fitted Pay")
- **Generic names**: Variables with non-descriptive names that could apply to any paper

### Variable Naming Guidelines

**Paper Variable** = exact name from paper (use in Ground Truth findings)
**Wiki Name** = common-sense descriptive name (use in wiki page title)

| Paper Variable | Wiki Name | Wiki Created? | Reason |
|----------------|-----------|---------------|--------|
| InDegree | Peer_Selection_Count | YES | Describes what it counts |
| PCOMP1 | [derived] | NO | PCA component, not directly measurable |
| Talent_Flow | Executive_Move | YES | Describes the observable event |
| Eigenvector | Network_Centrality | YES | More descriptive of what it captures |
| Clustering | Peer_Clustering_Rate | YES | Describes the ratio |

**Wiki naming rules**:
1. Wiki Name should describe what the variable **directly measures**
2. Use common terms that a reader can understand without context
3. Include measurement type if helpful (Count, Rate, Indicator, Ratio)
4. If no wiki page: Wiki Name = "[derived]" or "[composite]"

### Measures/Variables Table

Map paper variable names to wiki names with computational definitions:

| Paper Variable | Wiki Name | Constructs | Concept | Computational Definition | Wiki Page |
|----------------|-----------|------------|---------|--------------------------|-----------|
| InDegree | Peer_Selection_Count | Network position | Outside Opportunities | Number of firms selecting focal firm as peer | [[variables/Peer_Selection_Count]] |
| PCOMP1 | [derived] | Talent Transferability | Competition | First principal component of 5 measures | [no wiki] |

**Columns explained**:
- **Paper Variable**: Exact name used in the paper (honest to source) - use this in Ground Truth findings
- **Wiki Name**: Common-sense descriptive name (if wiki page created) or "[derived]" if no wiki
- **Wiki Page**: Link if directly measurable, "[no wiki]" if composite/constructed

**Rules**:
- Computational Definition must be **exact formula or operational rule**
- Ground Truth findings use **Paper Variable** names; wiki pages use **Wiki Name**

Ground Truth findings reference paper names: "InDegree (see Variables table) has β=..." → wiki maps to Peer_Selection_Count

## Wiki Creation (Orchestrator's Job)

After summary finalized, create wiki pages **following templates exactly**:

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

**Wiki Criteria**: Only for directly measurable variables. Skip PCA, indices, fitted values.

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

**Skip**: Standard methods (OLS, DiD, 2SLS, GMM, etc.)

### 4. Theories → wiki/theories/{theory}.md

Use `templates/theory.md` structure. Fill all sections from paper.

Use templates from templates/. Use Obsidian [[filename]] links.