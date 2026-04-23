---
name: Louvain_Group_Size
measures: [[concepts/Outside_Opportunities]]
domain: accounting
first_used: [[source/summary/gao_2026_aggregated_compensation_peer_summary]]
---

# Louvain_Group_Size

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Outside_Opportunities]]
- **Definition:** Count of firms within each Louvain group (community cluster detected by Louvain algorithm). Captures the number of potential employers within a broader definition of labor market competitors.

## Computation
Louvain Size = Count{firm j : firm j belongs to same Louvain group as focal firm i}

Louvain groups identified via Louvain method optimization algorithm (Blondel et al. [2008]) that maximizes intra-cluster links and minimizes inter-cluster links.

## Data Sources
- ISS Incentive Lab (peer selections)
- Louvain algorithm community detection

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Scope alignment | Broader than InDegree | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Empirical use | Component of competition measures | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |

## Alternative Variables for Same Concept
- [[variables/Peer_Selection_Count]] (InDegree) - narrower scope (direct selections)
- Industry size measures - product market approximation

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Competition measure (broad scope) | Component of PCOMP1/PCOMP2; captures broad outside options |

## Interpretations
| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | JAR | 2026 | Large Louvain group = many potential employers in skill cluster |
| Blondel et al. [2008] | J Stat Mech | 2008 | Louvain groups represent network communities |