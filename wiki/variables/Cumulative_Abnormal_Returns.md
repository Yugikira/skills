---
name: Cumulative_Abnormal_Returns
measures: [[concepts/Analyst_Performance]]
domain: finance
first_used: [[source/summary/li_2026_allstar_award_affect_summary]]
---

# Cumulative_Abnormal_Returns

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Analyst_Performance]]
- **Definition:** Size-adjusted cumulative abnormal stock returns around analyst events (recommendations, forecasts), measuring market reaction to analyst information.

## Computation
CAR[-1,+1] = Sum of abnormal returns from day -1 to day +1 around event

Abnormal return = Actual return - Size-decile benchmark return

Higher CAR indicates stronger market reaction to analyst recommendation.

## Data Sources
- CRSP/CSMAR stock return data
- Size decile benchmarks

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Validity | Size adjustment controls for size-related return patterns | [[source/summary/li_2026_allstar_award_affect_summary]] |
| Window | 3-day window [-1,+1] captures immediate market reaction | Standard in event studies |

## Alternative Variables for Same Concept
- Analyst_Forecast_Error - measures forecast accuracy
- Trading volume reaction - alternative market response measure

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | Information content of recommendations | All-Star recommendations have stronger CAR for high-asymmetry firms (coeff=0.012, p<0.01 for low liquidity) |
| Gleason and Lee (2003) | Star recommendation impact | All-Star forecasts elicit stronger immediate response |

## Interpretations
> **Selection Criteria**: Include only most valuable sources (max 5 total).

| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | CAR | 2026 | Higher CAR indicates more valuable recommendation information content |
| Gleason and Lee | RFS | 2003 | All-Star CAR stronger but less subsequent drift |
| Loh and Stulz | RFS | 2011 | Influential recommendations identified by CAR threshold |