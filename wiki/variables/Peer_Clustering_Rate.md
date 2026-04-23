---
name: Peer_Clustering_Rate
measures: [[concepts/Talent_Transferability]]
domain: accounting
first_used: [[source/summary/gao_2026_aggregated_compensation_peer_summary]]
---

# Peer_Clustering_Rate

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Talent_Transferability]]
- **Definition:** The degree to which a firm's direct peers are connected to each other in the compensation benchmarking network. High clustering indicates peers have similar talent demands to each other, meaning focal firm's talent is transferable across multiple competitors.

## Computation
Clustering = (Number of links between focal firm's peers) / (Maximum possible links between focal firm's peers)

Where:
- Links between peers = count of peer selections among firms that select focal firm
- Maximum possible links = n(n-1)/2 where n = number of peers selecting focal firm

## Data Sources
- ISS Incentive Lab (peer selections)
- Network construction from focal-peer pairs

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Construct validity | Captures local talent similarity | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Empirical validation | Associated with equity pay and duration | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |

## Alternative Variables for Same Concept
- [[variables/Louvain_Group_Density]] - broader scope clustering
- [[variables/Network_Centrality]] - global transferability measure

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Competition measure (local) | Component of PCOMP1/PCOMP2; associated with retention pay |

## Interpretations
| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | JAR | 2026 | High clustering = talent transferable across nearby firms = need retention incentives |
| Hanneman & Riddle [2005] | Book | 2005 | Clustering coefficient standard network metric |