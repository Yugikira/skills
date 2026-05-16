---
name: {Variable Name}
measures: [[concepts/{concept}]]
domain: {economics|finance|accounting|management|marketing}
first_used: [[source/summary/{citekey}_summary]]
type: {dependent|independent_manipulated}
---

# {Variable Name}

> **Wiki Criteria**: This page is for **experimental variables**.
> - Dependent variables: How the outcome is measured
> - Manipulated independent variables: How the treatment is operationalized
> - Naming: `{variable}_exp.md`

## What It Measures
- **Target Concept:** [[concepts/{concept}]]
- **Type:** {dependent|independent_manipulated}
- **Definition:** {What the variable measures in experimental context}

## Experimental Operationalization

### For Manipulated Independent Variables
| Paper | Condition Type | Manipulation Method | Treatment Levels | Manipulation Check | Control Condition | Validity |
|-------|----------------|---------------------|------------------|--------------------|--------------------|----------|
| [[source/summary/{citekey}_summary]] | Treatment | {how treatment operationalized} | {levels/conditions} | {verification method} | {baseline description} | {assessment} |
| [[source/summary/{citekey}_summary]] | Control | {how control condition implemented} | {control level} | {verification method} | — | {assessment} |

**Selection Rule**: Keep **first + most recent from top journals** for similar manipulation strategy.
- Each row corresponds to one **Condition Type** (Treatment, Control, Hedonic, Utilitarian, etc.)
- Different Condition Types get **separate rows** within the same paper
- Different manipulation strategies from different papers get separate rows

**Multi-paper accumulation**: Add new papers to the table with their manipulation details per condition type.

### For Dependent Variables
| Paper | Measurement Method | Scale/Units | Collection Procedure | Validity |
|-------|--------------------|-------------|----------------------|----------|
| [[source/summary/{citekey}_summary]] | {how outcome measured} | {scale - e.g., Likert 1-7} | {when/how collected} | {reliability if multi-item} |

**Selection Rule**: Keep **first + most recent from top journals** for similar measurement approach.

## Alternative Operationalizations
- {different manipulation/measurement approaches for same concept}

## Papers Using This Variable
| Paper | Key Findings |
|-------|--------------|
| [[source/summary/{citekey}_summary]] | {brief finding related to this variable} |

## Interpretations
> **Selection Criteria**: Include only most valuable sources (max 5 total).
> - **Oldest from Top journals**: earliest seminal paper
> - **Newest from Top journals**: latest paper using this variable
>
> **Top Journals by Domain**:
> - Economics: AER, JPE, QJE, Econometrica, Review of Economic Studies
> - Finance: JF, RFS, JFE, JFQA, RoF
> - Accounting: TAR, CAR, JAR, RAST, JAE
> - Management: AMJ, AMR, SMJ, Organization Science
> - Marketing: JMR, JM, Marketing Science

| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/{citekey}_summary]] | {journal} | {year} | {how variable values interpreted} |