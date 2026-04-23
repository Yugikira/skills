---
name: Brokerage_Size
measures: [[concepts/Analyst_Resource_Access]]
domain: finance
first_used: [[source/summary/li_2026_allstar_award_affect_summary]]
---

# Brokerage_Size

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Analyst_Resource_Access]]
- **Definition:** The number of analysts employed by a brokerage firm, measuring organizational resources available to analysts.

## Computation
BSize = ln(Number of analysts employed by brokerage firm in year t+1)

Log transformation captures diminishing marginal size effects.

## Data Sources
- CSMAR brokerage firm data
- Industry directories

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Validity | Brokerage size affects analyst resources and capabilities | [[source/summary/li_2026_allstar_award_affect_summary]] |
| Control | Used as pre-award covariate in RDD balance tests | [[source/summary/li_2026_allstar_award_affect_summary]] |

## Alternative Variables for Same Concept
- Team_Size - analyst's specific team size
- Site_Visits - external resource access measure

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | Pre-award covariate balance test | BSize balanced at threshold (no significant discontinuity) |

## Interpretations
> **Selection Criteria**: Include only most valuable sources.

| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | CAR | 2026 | Larger brokerages provide more potential resources; balanced at RDD threshold |