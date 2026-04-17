---
name: Managerial Labor Classification (MLC)
domain: accounting
first_defined: [[source/summary/gao_2026_aggregated_compensation_peer]]
---

# Managerial Labor Classification (MLC)

## Definition
Network-based groupings of firms that compete for similar managerial talent, derived from compensation benchmarking peer disclosures. MLCs capture firms' relative positions in the managerial labor market based on aggregated benchmarking patterns.

Three granularity levels:
- **Direct Peer**: Firms that either benchmark against or are benchmarked by the focal firm (narrowest)
- **Indirect Peer**: Direct peers of a focal firm's direct peers, following transitive property (intermediate)
- **Louvain Peer**: All peers in the same cluster identified by Louvain community detection algorithm (broadest)

## Alternative Definitions
> How other papers define this concept differently

- Previous literature commonly used **product industry classifications** (SIC, Fama-French, TNIC) to approximate managerial labor market competitors. However, Gao & Lu (2026) show this captures only a single, static aspect of talent demand and fails to predict executive moves as well as MLCs.

## Related Theories
- [[theories/managerial_labor_market_competition]] - MLCs identify competitors in this framework
- [[theories/tournament_theory]] - MLCs define tournament competitors for external tournament incentives
- [[theories/participation_constraints]] - MLCs identify firms affecting outside opportunities

## Common Proxies/Measures
| Proxy | Description | Validity Notes | Papers Using |
|-------|-------------|----------------|--------------|
| Product industry (FF48, TNIC) | Single-dimension classification based on product market | Predicts talent flows weakly; coefficients insignificant when tested against tournament incentives | Prior literature |

## Papers Defining This Concept
- [[source/summary/gao_2026_aggregated_compensation_peer]] - Original definition and validation; demonstrates MLCs predict executive moves better than industry classifications

## Papers Using This Concept
- [[source/summary/gao_2026_aggregated_compensation_peer]] - Uses MLCs to: (1) predict talent flows, (2) identify tournament competitors, (3) demonstrate multidimensional/dynamic features

## See Also
- [[concepts/compensation_benchmarking_network]] - Network from which MLCs are derived
- [[concepts/managerial_labor_market_competition]] - What MLCs help measure