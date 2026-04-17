---
name: kb-extract
description: Internal helper skill that extracts concepts, theories, proxies, and methods from converted paper markdown. Called by kb-ingest, not invoked directly by user.
---

# kb-extract - Knowledge Extraction Helper

This skill is called by kb-ingest to extract structured knowledge from converted paper markdown files.

## Efficient Workflow

**Token-minimized approach**:
1. **Orchestrator** creates summary directly (reads paper once)
2. **Verify Agent** provides simple yes/no feedback
3. **Orchestrator** revises if needed

```
Orchestrator (read paper → create summary) → Verify Agent (check) → Orchestrator (revision)
```

## Summary Requirements

### Ground Truth Findings: 3-5 Key Findings ONLY

Select the **most important** empirical results:
- Main coefficients from primary regression tables
- Key novel variables/measures from the paper
- Statistically significant results (p<0.05 or better)

DO NOT extract every finding. Quality over quantity.

### Ground Truth Format

Each finding must be **reproducible**:

```
Variable X (defined as [exact formula from paper context]) has coefficient β=YYY (p<ZZ) in [model type] regressing [dependent variable] on [independent variables] (n=XXXX).
```

**Key rules**:
- Use variable definitions from paper context (Results section, Variable Definitions, Model description)
- NOT just variable names like "PCOMP1" - must include what it measures
- If a proxy is defined once, subsequent findings can reference "see Finding N" or "see Measures table"

### Claimed Findings: 3-5 Key Interpretations ONLY

Select the authors' **main theoretical claims**:
- What they conclude from the empirical results
- The story they tell about why results matter

## Verify Agent Role

**Simple feedback format**:

```
Finding 1: YES
Finding 2: NO - uses abstract concept "competition" without computational definition
Finding 3: YES
Finding 4: NO - variable "MLCs" undefined, reader cannot verify
```

That's it. Just yes/no with one sentence reason for failures.

**What Verify Agent checks**:
1. Is this an objective statistical observation (coefficient, p-value, n)?
2. Are ALL variables defined with formulas (or referenced to earlier definition)?
3. Can a reader verify this without external sources?

**If referenced**: If Finding 2 says "PCOMP1 (see Finding 1)" and Finding 1 fully defines PCOMP1's components, that's YES.

## Orchestrator Revision

If Verify Agent says NO:
- Edit that finding directly
- Add the missing variable definition
- No interpretation changes, only operationalization clarity

## Measures/Proxies Table Requirement

The table MUST have computational definitions:

| Measure | For Concept | Computational Definition | Wiki Page |
|---------|-------------|--------------------------|-----------|
| PCOMP1 | Competition | First principal component of [InDegree, Clustering, Louvain_Density, Louvain_Size, Eigenvector] | [[proxies/PCOMP1]] |

Ground Truth findings can reference this table: "PCOMP1 (see Measures table) has β=..."

## Wiki Creation (Orchestrator's Job)

After summary finalized:
1. For Concepts table → create/update `wiki/concepts/{concept}.md`
2. For Measures table → create/update `wiki/proxies/{proxy}.md`
3. For Methods → create/update `wiki/methods/{method}.md`

Use templates from `templates/`. Use Obsidian [[filename]] links.