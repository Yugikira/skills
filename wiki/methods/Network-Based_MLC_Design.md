---
name: Network-Based MLC Design
domain: accounting
first_used: [[source/summary/gao_2026_aggregated_compensation_peer_summary]]
---

# Network-Based MLC Design

## Description
A novel methodology that constructs compensation benchmarking networks from proxy statement disclosures to identify managerial labor market competitors. The approach uses network analysis to aggregate firm-level peer choices into market-level classifications, overcoming limitations of single-dimension approximations (e.g., product industry).

## Steps

1. **Data Collection**: Extract compensation peer group disclosures from DEF 14A proxy statements (ISS Incentive Lab database)

2. **Network Construction**: Build directed network where:
   - Nodes = firms
   - Edges = peer selections (firm A selects firm B as compensation peer)

3. **MLC Classification**: Define three classification types:
   - **Direct Peer**: Firms that select or are selected by focal firm
   - **Indirect Peer**: Direct peers of focal firm's direct peers (transitive)
   - **Louvain Peer**: Firms in same Louvain group (community detection)

4. **Competition Measurement**: Compute five network metrics:
   - InDegree (local outside opportunities)
   - Clustering (local talent transferability)
   - Eigenvector (global talent transferability)
   - Louvain Density (group talent transferability)
   - Louvain Size (group outside opportunities)

5. **Validation**: Test classifications via talent flow prediction (logistic regression)

## When To Use
- Identifying managerial labor market competitors beyond product industry
- Measuring labor market competition intensity
- Testing labor theories requiring potential employer identification (tournament, outside options)
- Studies of executive compensation benchmarking

## Requirements
- Data: Compensation peer group disclosures (ISS Incentive Lab or proxy statements)
- Tools: Network analysis software (Python NetworkX, R igraph), Louvain algorithm implementation
- Assumptions: Peer selections reflect genuine talent demand; network aggregation mitigates opportunistic selection

## Limitations
- Sample limited to U.S. public firms with proxy disclosures
- Louvain algorithm parameters affect granularity (sensitivity to modularity threshold)
- Assumes peer choices reflect talent competition (may also reflect strategic benchmarking)
- Requires sufficient network density for community detection

## Variations
- Different classification granularities (Direct vs Indirect vs Louvain)
- Different competition measure combinations (individual vs PCA composite)
- Different validation outcomes (talent flow vs compensation response)

## Papers Using This Method
- [[source/summary/gao_2026_aggregated_compensation_peer_summary]] - Original development and validation

## See Also
- [[concepts/Managerial_Labor_Classifications]] - Concept operationalized by this method
- [[concepts/Outside_Opportunities]] - Construct measured via InDegree, Louvain Size
- [[concepts/Talent_Transferability]] - Construct measured via Clustering, Eigenvector, Louvain Density
- [[variables/Peer_Selection_Count]] - Primary network metric
- [[variables/Network_Centrality]] - Global transferability measure