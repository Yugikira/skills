---
name: Selected_Peer
measures: [[concepts/Managerial_Labor_Classifications]]
domain: accounting
first_used: [[source/summary/gao_2026_aggregated_compensation_peer_summary]]
---

# Selected_Peer

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Managerial_Labor_Classifications]]
- **Definition:** Indicator variable that takes value 1 if focal firm i explicitly selects firm j as its compensation benchmarking peer in year t, from proxy statement disclosure.

## Computation
Selected_Peer_{jt} = 1 if firm i discloses firm j as compensation peer in DEF 14A
                  = 0 otherwise

## Data Sources
- ISS Incentive Lab (primary source)
- Proxy statements (DEF 14A, Compensation Discussion & Analysis)

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Direct measurement | Explicit board choice documented | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Selection bias | May reflect opportunistic benchmarking | Faulkender & Yang [2010] |

## Alternative Variables for Same Concept
- [[variables/Peer_Selection_Count]] (InDegree) - reverse direction (selected by others)
- Industry peers - implicit, not board-selected

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Direct Peer classification | Selected peers are closest competitors; beta=2.787*** (z=13.565) on Talent Flow; relative margin 16.14 (ranked 1st) |
| Faulkender & Yang [2010] | Peer selection determinants | Size, industry, talent flows predict selection |
| Albuquerque et al. [2013] | Benchmarking effects | Selected peers affect CEO pay |

## Interpretations
| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | JAR | 2026 | Selected peer = self-identified talent competitor |
| Faulkender & Yang [2010] | JFE | 2010 | Selection reflects multiple firm characteristics |
| Albuquerque et al. [2013] | JFE | 2013 | Selection for benchmarking may be strategic |