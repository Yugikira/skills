---
name: Forecast_Frequency_Per_Industry
measures: [[concepts/Analyst_Industry_Specialization]]
domain: finance
first_used: [[source/summary/li_2026_allstar_award_affect_summary]]
---

# Forecast_Frequency_Per_Industry

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Analyst_Industry_Specialization]]
- **Definition:** The average number of earnings forecasts an analyst issues per industry sector, measuring research activity intensity.

## Computation
FreqInd = Number of earnings forecasts issued / Number of CSRC industries followed

Higher FreqInd indicates more frequent updates within each covered industry.

## Data Sources
- CSMAR analyst forecast data
- Brokerage research reports

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Validity | Ratio captures timely feedback intensity | [[source/summary/li_2026_allstar_award_affect_summary]] |
| Investor Value | Timely feedback is valued by institutional investors | Groysberg et al. 2011 |

## Alternative Variables for Same Concept
- Industry_Coverage - measures breadth across industries
- Firm_Coverage_Per_Industry - measures firm depth

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | Post-award specialization measure | All-Star award increases FreqInd by 2.308 forecasts/industry (coeff=+2.308, p<0.10) |

## Interpretations
> **Selection Criteria**: Include only most valuable sources.

| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | CAR | 2026 | Higher FreqInd post-award indicates more frequent timely feedback; award induces activity increase |