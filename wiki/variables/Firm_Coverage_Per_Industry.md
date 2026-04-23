---
name: Firm_Coverage_Per_Industry
measures: [[concepts/Analyst_Industry_Specialization]]
domain: finance
first_used: [[source/summary/li_2026_allstar_award_affect_summary]]
---

# Firm_Coverage_Per_Industry

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Analyst_Industry_Specialization]]
- **Definition:** The average number of firms an analyst covers within each industry sector, measuring coverage depth.

## Computation
NFirmInd = Number of firms covered / Number of CSRC industries followed

Higher NFirmInd indicates deeper coverage within each industry.

## Data Sources
- CSMAR analyst coverage data
- Brokerage research reports

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Validity | Ratio captures depth vs. breadth trade-off | [[source/summary/li_2026_allstar_award_affect_summary]] |
| Interpretation | Higher values = more concentrated expertise within industries | [[source/summary/li_2026_allstar_award_affect_summary]] |

## Alternative Variables for Same Concept
- Industry_Coverage - measures breadth across industries
- Forecast_Frequency_Per_Industry - measures activity intensity

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | Post-award specialization measure | All-Star award increases NFirmInd by 0.909 firms/industry (coeff=+0.909, p<0.05) |

## Interpretations
> **Selection Criteria**: Include only most valuable sources.

| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | CAR | 2026 | Higher NFirmInd post-award indicates deeper industry expertise; award induces concentration |