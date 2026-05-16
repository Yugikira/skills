---
name: {Dimension Name}_survey
measures: [[concepts/{concept}]]
domain: {management|marketing|economics|finance|accounting}
paper_type: survey
first_used: [[source/summary/{citekey}_summary]]
---

# {Dimension Name} (Survey)

> **Wiki Criteria**: This page is for **survey variables** - questions grouped by dimension.
> - Multiple questions measuring one dimension of a concept
> - Response scale (scalar, yes-no, Likert scale)
> - Reliability measures (Cronbach's alpha, test-retest)
> - Naming: `{dimension}_survey.md`

## What It Measures
- **Target Concept:** [[concepts/{concept}]]
- **Dimension:** {dimension name} - {what this dimension captures}

## Questions Relating to This Dimension
| Questions | Response Scale | Papers |
|-----------|----------------|--------|
| Q{1-3}: "{most precise question excerpt from semantic group}" | {Likert 5-point | Likert 7-point | Scalar | Yes/No} | [[source/summary/{first}_summary]] (first), [[source/summary/{recent}_summary]] (most recent) |

**Selection Rule**:
- **Retain ONLY ONE** question statement - the most precise wording from the semantic group
- Combine **semantic identical questions** (same meaning, different wording) into one row
- Papers: **first + most recent from top journals**

## Studies Using This Dimension
| Paper | Reliability (α) | Validity | Key Findings |
|-------|-----------------|----------|--------------|
| [[source/summary/{citekey}_summary]] | α={value} | {assessment} | {finding related to this dimension} |

**Reliability**: Per-study Cronbach's alpha varies by sample.
**Validity**: Per-study validity testing (construct, content).
**Note**: Sample details are in the paper's summary - no need to duplicate here.

## Alternative Dimensions for Same Concept
- [[variables/{dimension2}_survey]] - {comparison}

## Interpretations
> **Selection Criteria**: Include only most valuable sources (max 5 total).
> - Oldest from Top journals (earliest seminal survey using this dimension)
> - Newest from Top journals (latest survey using this dimension)
>
> **Top Journals by Domain**:
> - Management: AMJ, AMR, JOM, SMJ, OS
> - Marketing: JMR, JM, MS, JCR
> - Economics: AER, JPE, QJE
> - Finance: JF, RFS, JFE
> - Accounting: TAR, CAR, JAR

| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/{citekey}_summary]] | {journal} | {year} | {how dimension scores interpreted} |