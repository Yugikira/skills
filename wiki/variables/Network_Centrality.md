---
name: Network_Centrality
measures: [[concepts/Talent_Transferability]]
domain: accounting
first_used: [[source/summary/gao_2026_aggregated_compensation_peer_summary]]
---

# Network_Centrality

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Talent_Transferability]]
- **Definition:** Eigenvector centrality of a firm in the compensation benchmarking network. Measures the average closeness with all other firms in the network. Central firms face competition from all kinds of firms; peripheral firms compete only with local market.

## Computation
Eigenvector centrality E is solved from: lambda * E = A * E

Where:
- A = adjacency matrix of compensation benchmarking connections (directed)
- E = eigenvector associated with principal eigenvalue lambda*
- Eigenvector_i = element of E corresponding to firm i

## Data Sources
- ISS Incentive Lab (peer selections)
- Network matrix construction

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Theoretical alignment | Captures global market position | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Empirical use | Component of competition measures | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |

## Alternative Variables for Same Concept
- [[variables/Peer_Selection_Count]] (InDegree) - local scope only
- [[variables/Peer_Clustering_Rate]] - intermediate scope

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Competition measure (global) | Component of PCOMP1/PCOMP2; captures broadest transferability |

## Interpretations
| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | JAR | 2026 | High centrality = talent applicable to many firm types = global competition |
| El-Khatib et al. [2015] | JFE | 2015 | CEO network centrality affects merger performance |
| Hanneman & Riddle [2005] | Book | 2005 | Eigenvector centrality standard network measure |