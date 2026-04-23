---
name: Analyst_Forecast_Error
measures: [[concepts/Analyst_Performance]]
domain: finance
first_used: [[source/summary/li_2026_allstar_award_affect_summary]]
---

# Analyst_Forecast_Error

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Analyst_Performance]]
- **Definition:** Standardized relative forecast error measuring the accuracy of analyst's earnings forecast relative to other analysts following the same firm.

## Computation
[AbsFE_ijt - min(AbsFE_jt)]/[max(AbsFE_jt) - min(AbsFE_jt)]

where:
- AbsFE_ijt = |Forecast EPS_ijt - Actual EPS_jt| / Price_jt (price at beginning of year t)
- min(AbsFE_jt) = smallest earnings forecast error among all analysts following firm j in year t
- max(AbsFE_jt) = largest earnings forecast error among all analysts following firm j in year t

Standardization ranges from 0 (most accurate) to 1 (least accurate).

## Data Sources
- CSMAR (China Stock Market & Accounting Research) - forecast EPS, actual EPS, stock prices
- I/B/E/S (for US studies) - forecast data

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Validity | Standardized to control for firm-year effects, enabling cross-firm comparison | [[source/summary/li_2026_allstar_award_affect_summary]] |
| Common Use | Clement and Tse (2005) standardization methodology | Standard approach in analyst literature |

## Alternative Variables for Same Concept
- [[variables/Cumulative_Abnormal_Returns]] - measures information content of recommendations

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | Primary performance measure in RDD | All-Star award improves AFE by 7.8% (coeff=-0.078, p<0.01) |
| Stickel (1992) | Association with star status | Stars have better accuracy |
| Clement and Tse (2005) | Herding behavior analysis | Standardization methodology |

## Interpretations
> **Selection Criteria**: Include only most valuable sources (max 5 total).

| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | CAR | 2026 | Lower AFE = better analyst performance; All-Star award causally improves |
| Clement and Tse | JF | 2005 | Standardized AFE enables cross-analyst, cross-firm comparison |
| Stickel | JF | 1992 | Star analysts have lower AFE than non-stars |
| Malloy | JF | 2005 | Geographic effects on AFE |