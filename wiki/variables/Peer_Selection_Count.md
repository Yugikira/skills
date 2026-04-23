---
name: Peer_Selection_Count
measures: [[concepts/Outside_Opportunities]]
domain: accounting
first_used: [[source/summary/gao_2026_aggregated_compensation_peer_summary]]
---

# Peer_Selection_Count

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Outside_Opportunities]]
- **Definition:** Count of firms that select the focal firm as their compensation benchmarking peer in a given year. Reflects the number of firms that view the focal firm's executives as comparable talent.

## Computation
InDegree = Count{firm j : firm j selects focal firm i as compensation peer in year t}

Data source: ISS Incentive Lab database, derived from DEF 14A proxy statement disclosures.

## Data Sources
- ISS Incentive Lab (primary)
- Proxy statements (DEF 14A, Compensation Discussion & Analysis section)

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Predictive validity | Strongly predicts talent flows | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Theoretical alignment | Captures revealed talent demand | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |

## Alternative Variables for Same Concept
- [[variables/Louvain_Group_Size]] - broader scope, captures wider labor market
- Industry mobility measures (Fee & Hadlock [2003]) - indirect proxy

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Main competition measure | Beta=0.061 (p<0.001) on Ln(Total Pay); predicts talent flows |
| Faulkender & Yang [2010] | Peer selection determinant | InDegree driven by size, industry similarity |

## Interpretations
| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | JAR | 2026 | Higher InDegree = more outside options = higher reservation wage |
| Faulkender & Yang [2010] | JFE | 2010 | Selection as peer indicates labor market relevance |