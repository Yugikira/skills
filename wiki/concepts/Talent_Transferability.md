---
name: Talent Transferability
domain: accounting
first_defined: [[source/summary/gao_2026_aggregated_compensation_peer_summary]]
---

# Talent Transferability

## Definition
The degree to which executive skills and human capital are applicable across different firms in the labor market. High transferability means executives can move to more potential employers; low transferability means skills are firm-specific or industry-specific.

> **Key Paper**: [[source/summary/gao_2026_aggregated_compensation_peer_summary]] - Gao & Lu (2026, JAR) operationalize via network clustering and centrality measures.

## Alternative Definitions
| Definition | Source | Note |
|------------|--------|------|
| "Firm-specific vs general human capital" | Lazear [2009] | Skill-weights approach; transferability depends on skill overlap |
| "Ability to perform at alternative employers" | Murphy & Zabojnik [2004, 2007] | Managerial capital theory; generalist CEOs more transferable |
| "Industry portability of skills" | Custodio et al. [2013] | Career experience diversity indicates transferability |

## Constructs & Variables
Three operationalizations capturing different scope levels:

| Construct | Variable | Computational Definition | Key Paper |
|----------|----------|--------------------------|-----------|
| Local Transferability | Peer_Clustering_Rate | Links between focal firm's peers divided by max possible links | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Group Transferability | Louvain_Group_Density | Links within Louvain group divided by max possible links | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Global Transferability | Network_Centrality (Eigenvector) | Eigenvector centrality from connection matrix | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |

## Related Theories
- [[theories/Skill_Weights_Theory]] - Lazear [2009]: transferability depends on skill weight overlap
- [[theories/Managerial_Capital]] - Murphy & Zabojnik [2004]: generalist skills more transferable

## Determinants of Talent Transferability
| Determinant | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| Industry specificity | Industry-specific skills less transferable | Fee & Hadlock [2003] | Cross-industry moves less common but higher pay |
| Executive experience | Diverse experience increases transferability | Custodio et al. [2013] | Generalist CEOs earn more |
| Firm complexity | Complex firms require more specific skills | Kaplan & Sorensen [2021] | CEO skill demands vary by firm type |

## Economic Consequences of Talent Transferability
| Consequence | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| Pay duration | Longer vesting when transferability high | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | PCOMP1 increases Pay Duration 0.27 years |
| Equity share | More equity when retention needed | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Clustering associated with equity pay |
| CEO pay level | Transferable executives command higher pay | Murphy & Zabojnik [2007] | Generalist premium in CEO pay |

## Identification Strategy
| Strategy | Assumption | Key Paper | Note |
|----------|------------|-----------|------|
| Clustering measure | Dense peer connections indicate similar skill demands | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Captures local skill similarity |
| Eigenvector centrality | Central firms face competition from all directions | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Global measure; may be noisy |

## Future Works
- **Skill decomposition**: Which specific skills drive transferability?
- **Industry boundaries**: How do industry walls affect transferability?
- **Career path analysis**: Do transferable executives follow predictable career paths?