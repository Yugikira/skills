---
name: Vote_Distance
measures: [[concepts/Award_Effect]]
domain: finance
first_used: [[source/summary/li_2026_allstar_award_affect_summary]]
---

# Vote_Distance

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Award_Effect]]
- **Definition:** The distance between an analyst's vote share and the cutoff vote share required to win All-Star award, centered at zero at the award threshold.

## Computation
Distance_i = VoteShare_i - Cutoff_VoteShare_i

where:
- VoteShare_i = analyst's vote share percentage
- Cutoff_VoteShare_i = vote share of analyst at cutoff ranking (3rd for <=20 analysts industries, 5th for >20 analysts industries)

Positive Distance = award recipient; Negative Distance = non-recipient.

## Data Sources
- New Fortune All-Star analyst voting data (proprietary)

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Validity | Centers running variable at threshold for RDD analysis | [[source/summary/li_2026_allstar_award_affect_summary]] |
| Manipulation Test | McCrary density test shows no discontinuity at zero | [[source/summary/li_2026_allstar_award_affect_summary]] |

## Alternative Variables for Same Concept
- Vote_Share - uncentered vote percentage
- All_Star_Indicator - binary treatment indicator

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | Running variable in RDD | Distance centered at zero enables treatment effect estimation |

## Interpretations
> **Selection Criteria**: Include only most valuable sources.

| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | CAR | 2026 | Distance > 0 = Star; Distance < 0 = Non-Star; threshold at Distance = 0 |