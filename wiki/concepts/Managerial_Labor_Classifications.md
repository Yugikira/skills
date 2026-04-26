---
name: Managerial Labor Classifications
domain: accounting
first_defined: [[source/summary/gao_2026_aggregated_compensation_peer_summary]]
---

# Managerial Labor Classifications

## Definition
Groupings of firms that compete for similar managerial talent, identifying potential employers for executives. Unlike product market classifications, MLCs capture multidimensional skill demands including industry knowledge, operational complexity, firm size, geographic scope, and other factors that determine executive labor market competition.

> **Key Paper**: [[source/summary/gao_2026_aggregated_compensation_peer_summary]] - Gao & Lu (2026, JAR) introduce network-based MLCs from compensation peer disclosures.

## Alternative Definitions
| Definition | Source | Note |
|------------|--------|------|
| "Firms within same product industry" | Common practice in prior literature | Single-dimension approximation; fails to capture non-industry talent demand |
| "Firms selected as compensation peers" | Faulkender & Yang [2010] | Self-identified competitors only; misses potential employers |

## Constructs & Variables
Primary operationalization through three classification types with increasing scope:

| Construct | Variable | Computational Definition | Key Paper |
|----------|----------|--------------------------|-----------|
| Direct Peer | Selected_Peer, Direct Potential Peer | Firms that select or are selected by focal firm as compensation peer | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Indirect Peer | Indirect Potential Peer | Direct peers of focal firm's direct peers (transitive property) | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |
| Louvain Peer | Louvain Group Membership | Firms in same Louvain cluster from community detection algorithm | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] |

## Related Theories
- [[theories/Tournament_Theory]] - MLCs identify tournament rivals (potential employers with larger pay)

## Determinants of Managerial Labor Classifications
| Determinant | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| Compensation peer selection | Boards choose peers reflecting talent demand | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | 71.6% cite talent as peer selection criterion |
| Industry similarity | Common skill requirements within industry | Fee & Hadlock [2003] | External hires often from outside same industry |
| Firm size/complexity | Similar operational demands require similar skills | Faulkender & Yang [2010] | Market cap, revenue predict peer selection |

## Economic Consequences of Managerial Labor Classifications
| Consequence | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| Talent flows | Executives move to firms in same MLC | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Selected Peer beta=2.787*** (z=13.565) on Talent Flow; relative margin 16.14 |
| Tournament incentives | Pay gap with MLC peers creates external tournament | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Louvain Pay Gap beta=0.027*** (t=2.860) on Tobin's Q; FF48/TNIC2 insignificant |
| Compensation benchmarking | Peers set reservation wage reference | Albuquerque et al. [2013] | Peer pay affects CEO compensation |

## Identification Strategy
| Strategy | Assumption | Key Paper | Note |
|----------|------------|-----------|------|
| Network construction | Aggregated peer choices reveal latent structure | [[source/summary/gao_2026_aggregated_compensation_peer_summary]] | Mitigates opportunistic selection bias |
| Louvain algorithm | Communities emerge from connection patterns | Blondel et al. [2008] | Heuristic optimization; granularity varies |

## Future Works
- **Cross-country validation**: Do MLCs work for international labor markets?
- **Private firm extension**: How to classify competitors for private company executives?
- **Skill dimension analysis**: Which specific skills drive MLC membership?