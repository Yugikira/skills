---
name: Talent_Flow
measures: [[concepts/Managerial_Labor_Classifications]]
domain: accounting
first_used: [[source/summary/gao_2026_aggregated_compensation_peer_summary]]
---

# Talent_Flow

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Managerial_Labor_Classifications]]
- **Definition:** Indicator variable that takes value 1 if one of the top five executives of firm i moves to a top five executive position at firm j within a one-year window. Used to validate MLC predictions.

## Computation
Talent_Flow_{ij,t+1} = 1 if executive from firm i moves to firm j within t+1 to t+2
                    = 0 otherwise

Where top five executives identified from Execucomp database.

## Data Sources
- Execucomp (executive positions, firm affiliations)
- SEC filings (executive transitions)

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Outcome validity | Direct evidence of labor competition | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Measurement | Limited to top 5 executives; may miss lateral moves | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |

## Alternative Variables for Same Concept
- Executive turnover (broader, includes exits without destinations)
- Job change announcements (direct but incomplete)

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Validation outcome for MLCs | Selected Peer beta=2.787*** (z=13.565) predicts flow with relative margin 16.14 (ranked 1st) |
| Fee & Hadlock [2003] | Mobility and pay studies | Talent flow associated with pay increases |
| Gao, Luo & Tang [2015] | Labor market effects on pay | Job-hopping affects compensation structure |

## Interpretations
| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | JAR | 2026 | Flow to MLC peer validates classification as true competitor |
| Fee & Hadlock [2003] | RFS | 2003 | Talent flows reveal labor market structure |
