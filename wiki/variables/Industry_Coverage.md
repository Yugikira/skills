---
name: Industry_Coverage
measures: [[concepts/Analyst_Industry_Specialization]]
domain: finance
first_used: [[source/summary/li_2026_allstar_award_affect_summary]]
---

# Industry_Coverage

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Analyst_Industry_Specialization]]
- **Definition:** The number of industry sectors an analyst follows and covers with research reports, measuring coverage breadth.

## Computation
IndCovrg = ln(Number of CSRC industries analyst i follows between ceremony date of year t and ceremony date of year t+1)

CSRC = China Securities Regulatory Commission industry classification.

## Data Sources
- CSMAR analyst coverage data
- Brokerage research reports

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Validity | Log transformation captures diminishing marginal coverage | [[source/summary/li_2026_allstar_award_affect_summary]] |
| Timing | Measured between ceremony dates to capture post-award behavior | [[source/summary/li_2026_allstar_award_affect_summary]] |

## Alternative Variables for Same Concept
- Firm_Coverage_Per_Industry - measures depth within industries
- Forecast_Frequency_Per_Industry - measures activity intensity

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | Post-award specialization measure | All-Star award reduces IndCovrg by 31.6% (coeff=-0.316, p<0.01) |

## Interpretations
> **Selection Criteria**: Include only most valuable sources.

| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | CAR | 2026 | Lower IndCovrg post-award indicates industry concentration; award induces specialization |