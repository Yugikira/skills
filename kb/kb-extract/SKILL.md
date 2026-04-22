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

Each finding must be **reproducible**:

```
Variable X (defined as [exact formula from paper context]) has coefficient β=YYY (p<ZZ) in [model type] regressing [dependent variable] on [independent variables] (n=XXXX).
```

**Key rules**:
- Use variable definitions from paper context (Results section, Variable Definitions, Model description)
- NOT just variable names like "PCOMP1" - must include what it measures
- If a proxy is defined once, subsequent findings can reference "see Finding N" or "see Measures table"

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

## Table Requirements

### Concepts Defined Table

Link concepts to their constructs (operationalizations):

| Concept | Definition | Constructs | Wiki Page |
|---------|------------|------------|-----------|
| Managerial Labor Classifications | A market where managers share similar talents | Industry match, Compensation peer group match | [[concepts/Managerial_Labor_Classifications]] |
| Tournament Incentive | Outside employment opportunity incentives | Job change events, External compensation offers | [[concepts/Tournament_Incentive]] |

**Rules**:
- Definition should be the **abstract theoretical idea**, NOT the measure
- Constructs are multi-item measures that operationalize the concept
- If paper lacks explicit definition, provide common-sense definition with `[common-sense]` marker

### Measures/Proxies Table

Link proxies to constructs and concepts with computational definitions:

| Measure | Constructs | Concept | Computational Definition | Wiki Page |
|---------|------------|---------|--------------------------|-----------|
| SameIndustry | Industry match | Managerial Labor Classifications | 1 if both firms in same 4-digit SIC code | [[proxies/SameIndustry]] |
| PeerGroupMatch | Compensation peer group match | Managerial Labor Classifications | 1 if both firms appear in same compensation peer group | [[proxies/PeerGroupMatch]] |

**Rules**:
- Computational Definition must be **exact formula or operational rule** from paper
- Link measure → construct → concept to show the operationalization chain

Ground Truth findings can reference this table: "SameIndustry (see Measures table) has β=..."

## Wiki Creation (Orchestrator's Job)

After summary finalized:
1. For Concepts table → create/update `wiki/concepts/{concept}.md` (include Constructs section)
2. For Measures table → create/update `wiki/proxies/{proxy}.md`
3. For Methods → create/update `wiki/methods/{method}.md`

Use templates from `templates/`. Use Obsidian [[filename]] links.