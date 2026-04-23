---
name: All_Star_Indicator
measures: [[concepts/Award_Effect]]
domain: finance
first_used: [[source/summary/li_2026_allstar_award_affect_summary]]
---

# All_Star_Indicator

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Award_Effect]]
- **Definition:** Binary indicator identifying whether an analyst received All-Star award status from New Fortune magazine in a given year.

## Computation
Star = 1 if analyst is ranked in top 3 (for industries with <=20 analysts) or top 5 (for industries with >20 analysts) by New Fortune in year t

Star = 0 otherwise (non-recipient analysts)

## Data Sources
- New Fortune All-Star analyst voting data (proprietary)
- Institutional Investor (US equivalent)

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Validity | Clear award threshold defined by ranking rules | [[source/summary/li_2026_allstar_award_affect_summary]] |
| Context | Chinese award system, different from US Institutional Investor | [[source/summary/li_2026_allstar_award_affect_summary]] |

## Alternative Variables for Same Concept
- Institutional Investor All-Star (US market equivalent)
- Vote_Share - continuous measure of award likelihood

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | Treatment indicator in RDD | Award causally improves analyst performance |
| Stickel (1992) | Association analysis | Stars have better accuracy |
| Emery and Li (2009) | Association analysis | Stars may not differ in performance |

## Interpretations
> **Selection Criteria**: Include only most valuable sources (max 5 total).

| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | CAR | 2026 | All-Star status causally improves performance via RDD |
| Gleason and Lee | RFS | 2003 | All-Star forecasts elicit stronger market response |
| Emery and Li | JEF | 2009 | All-Star may reflect visibility rather than quality |
| Stickel | JF | 1992 | All-Star associated with better accuracy |