# Archival Paper Extraction Guidance

This reference provides detailed extraction guidance specific to archival/empirical papers. Use this when processing papers with existing data sources and observational methods.

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

## Methods Filtering for Archival Papers

### SKIP - Do NOT create wiki/methods/ page for:

**Standard econometric methods**:
- OLS, Fixed Effects, Random Effects
- Standard tests: t-tests, F-tests, Hausman tests, White tests

**Standard causal identification methods**:
- 2SLS (Two-stage least squares)
- GMM (Generalized method of moments)
- DiD (Difference-in-differences) exploiting new regulation/law as exogenous shock
- Regression Discontinuity - unless novel threshold/cutoff design

**Standard data methods**:
- Panel data construction, variable winsorization

### CREATE wiki/methods/ page for:

- **Novel identification designs**: Unique research design settings for causality (e.g., novel instrument, DiD with non-regulation shock, novel RD threshold)
- **Novel methodological contributions**: New measurement approaches, new estimators, new tests
- **Combined approaches**: Novel combinations of standard methods with unique twist

### Methods Section in Summary

**If using standard methods only**:
```markdown
## Methods
- **Standard Methods**: OLS with Industry×Year fixed effects (no wiki page created)
- **Data**: {data sources}, n={sample size}
```

**If novel design**:
```markdown
## Methods
- **Novel Design**: {description of what makes it novel}
- **Model**: {key equations or framework}
→ Create wiki/methods/{method_name}
```

## Summary Requirements for Archival Papers

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

### Ground Truth Format for Regression Results

Each finding must be **reproducible** - use the paper's actual variable names:

```
{Paper Variable Name} (defined as [exact formula from paper]) has coefficient β=YYY (p<ZZ) in [model type] (n=XXXX).
```

**Key rules**:
- Use **paper's exact variable names** (e.g., "PCOMP1", "InDegree") - be honest to the paper
- Include computational definition from paper (Results section, Variable Definitions)
- If a variable is defined once, subsequent findings can reference "see Finding N" or "see Variables table"
- The Variables table maps paper names to common-sense wiki names

## Measures/Variables for Archival Papers

### Wiki Page Criteria

**CREATE wiki/variables/ page for** (directly measurable/basic):
- **BE FOCUS**: Focus on variables central to the paper.
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
- **Control Variables**: **DO NOT** create wiki page for control variables not essential to the paper.

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