---
name: PCOMP Competition Measures
measures: [[concepts/managerial_labor_market_competition]]
domain: accounting
first_used: [[source/summary/gao_2026_aggregated_compensation_peer]]
---

# PCOMP Competition Measures (PCOMP1, PCOMP2)

## What It Measures
- **Target Concept:** [[concepts/managerial_labor_market_competition]]
- **Definition:** Principal components of five network-based competition measures (InDegree, Clustering, Louvain Density, Louvain Size, Eigenvector). Standardized proxies for overall labor market competition intensity.

## Methodology
1. Construct compensation benchmarking network from peer disclosures
2. Calculate 5 network measures per firm-year:
   - InDegree: # of times benchmarked by others
   - Clustering: density of connections among firm's peers
   - Louvain Density: density within Louvain community
   - Louvain Size: # firms in Louvain community
   - Eigenvector: centrality in network
3. Apply principal component analysis
4. PCOMP1 = first principal component, PCOMP2 = second principal component
5. Standardize for interpretation

## Data Sources
- ISS Incentive Lab (compensation peer disclosures)
- Execucomp (executive compensation)
- CRSP/Compustat (firm financials)

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Predicts talent flows | Strong predictive power for executive moves | [[source/summary/gao_2026_aggregated_compensation_peer]] Table 3 |
| Linked to retention tools | Higher PCOMP → higher equity pay, longer pay duration | [[source/summary/gao_2026_aggregated_compensation_peer]] Table 5 |
| Explains pay for luck | Luck × PCOMP positive, significant at 1% | [[source/summary/gao_2026_aggregated_compensation_peer]] Table 6 Panel A |
| Explains RPE puzzle | Ln(Return Peer) × PCOMP positive at 5% | [[source/summary/gao_2026_aggregated_compensation_peer]] Table 6 Panel B |

## Alternative Proxies for Same Concept
- Product market HHI - captures product competition, not validated for labor competition
- Industry-based measures - single dimension, weak predictive power for talent flows

## Papers Using This Proxy
| Paper | How Used | Ground Truth Findings |
|-------|----------|-----------------------|
| [[source/summary/gao_2026_aggregated_compensation_peer]] | Primary competition proxy in all analyses | 1 std dev increase in PCOMP1 → 15.1% increase in equity pay; explains pay for luck and RPE puzzle |

## Interpretations
> Different papers' interpretations of findings using this proxy

- [[source/summary/gao_2026_aggregated_compensation_peer]] interprets PCOMP as capturing labor demand (outside opportunities + talent transferability), validated by link to retention tools
- Competition measures may also capture aspects of talent supply; higher supply would reduce retention efforts, but empirical results show opposite pattern

## See Also
- [[proxies/indegree_competition]] - Component of PCOMP
- [[proxies/clustering_competition]] - Component of PCOMP
- [[concepts/outside_opportunities]] - Underlying construct
