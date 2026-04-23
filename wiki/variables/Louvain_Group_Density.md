---
name: Louvain_Group_Density
measures: [[concepts/Talent_Transferability]]
domain: accounting
first_used: [[source/summary/gao_2026_aggregated_compensation_peer_summary]]
---

# Louvain_Group_Density

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Talent_Transferability]]
- **Definition:** The density of connections within a Louvain group (community detected by Louvain algorithm). High density indicates firms within the group have similar talent demands, meaning talent is highly transferable across the group.

## Computation
Louvain Density = (Number of links within Louvain group) / (Maximum possible links within Louvain group)

Where:
- Links within group = count of peer selections among firms in same Louvain group
- Maximum possible = n(n-1)/2 where n = Louvain group size

## Data Sources
- ISS Incentive Lab (peer selections)
- Louvain algorithm community detection

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Scope alignment | Captures group-level transferability | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Empirical use | Component of competition measures | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |

## Alternative Variables for Same Concept
- [[variables/Peer_Clustering_Rate]] - local scope (direct peers only)
- [[variables/Network_Centrality]] - global scope (entire network)

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Competition measure (group scope) | Component of PCOMP1/PCOMP2; captures medium-breadth transferability |

## Interpretations
| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | JAR | 2026 | High Louvain density = tight skill cluster = talent transferable within group |
| Blondel et al. [2008] | J Stat Mech | 2008 | Louvain method detects network communities |