---
title: Aggregated Compensation Peer Group Disclosure and Managerial Labor Market Competition: A Network Analysis
doi: 10.1111/1475-679X.70026
citekey: gao_2026_aggregated_compensation_peer
authors: [Ray Rui Gao, Yifei Lu]
year: 2025
journal: Journal of Accounting Research
keywords: [managerial labor market, managerial labor classifications, managerial labor competition measures, network analysis, compensation benchmarking peers]
processed: 2026-04-17
source: [[raw/papers/gao_2026_aggregated_compensation_peer/gao_2026_aggregated_compensation_peer.pdf]]
---

# Aggregated Compensation Peer Group Disclosure and Managerial Labor Market Competition: A Network Analysis

## One-Line Summary
Develops network-based measures of managerial labor market classification and competition from compensation peer group disclosures, demonstrating their predictive power for talent flows and application to compensation contract theories.

## Abstract Summary
The paper constructs managerial labor classifications (MLCs) and competition measures from compensation benchmarking peer networks disclosed in proxy statements. These measures predict executive talent flows better than conventional predictors and are associated with retention-focused compensation design (higher equity pay, longer vesting).

## Ground Truth Findings
> **3-5 KEY FINDINGS ONLY** - Main empirical results with variable definitions.
>
> **Note**: All measures are standardized (zero mean, unit variance). *** indicates p<0.01, ** indicates p<0.05.

- **Finding 1**: PCOMP1 (first principal component of [InDegree=13.80 mean, Clustering=0.32 mean, Louvain_Density=0.06 mean, Louvain_Size=159.38 mean, Eigenvector=0.02 mean], capturing talent transferability with factor loadings: Clustering=0.523, Louvain_Density=0.524) has coefficient β=0.069 (t=3.839, p<0.01) in OLS regression regressing Ln(Total Pay) on PCOMP1, PCOMP2, Ln(FF Peer Pay), FF Peer Num, and controls with Industry×Year fixed effects (n=9,798). This implies a one SD increase in PCOMP1 is associated with 6.9% higher total compensation.

- **Finding 2**: PCOMP2 (second principal component capturing outside opportunities with factor loadings: InDegree=0.531, Louvain_Size=0.537) has coefficient β=0.070 (t=3.182, p<0.01) in OLS regression regressing Ln(Total Pay) on PCOMP1, PCOMP2 and controls with Industry×Year fixed effects (n=9,798). This implies a one SD increase in PCOMP2 is associated with 7.0% higher total compensation.

- **Finding 3**: PCOMP1 (see Finding 1 for definition) has coefficient β=0.151 (t=2.656, p<0.01) in OLS regression regressing Ln(Equity Pay) on PCOMP1, PCOMP2 and controls with Industry and Year fixed effects (n=9,750). This implies a one SD increase in PCOMP1 is associated with 15.1% higher equity pay.

- **Finding 4**: Luck × PCOMP1 interaction term (Luck defined as annualized fitted value from FirmReturn regression on IndReturn and MktReturn; PCOMP1 see Finding 1) has coefficient β=0.088 (t=2.624, p<0.01) in OLS regression regressing Ln(Total Pay) on Luck, Skill, Luck×PCOMP1, Luck×PCOMP2 and controls (n=7,396). This indicates firms pay more for luck when facing higher competition.

- **Finding 5**: Ln(Return Peer) × PCOMP1 interaction term (Return Peer is equal-weighted TNIC3-size matched peer returns; PCOMP1 see Finding 1) has coefficient β=0.058 (t=1.986, p<0.05) in OLS regression regressing Ln(Total Pay) on Ln(Return Own), Ln(Return Peer), interaction terms and controls (n=8,564). This indicates firms use less RPE (less negative sensitivity to peer returns) when facing higher competition.

## Claimed Findings
> **3-5 KEY INTERPRETATIONS** - Authors' main claims.

- **Claim 1**: MLCs derived from compensation peer networks capture the multidimensional and dynamic nature of managerial labor competition better than static product industry classifications.

- **Claim 2**: Network-based competition measures predominantly capture labor demand (retention pressure) rather than talent supply, as evidenced by their association with retention tools (equity pay with longer vesting).

- **Claim 3**: Greater labor market competition explains controversial pay practices—firms pay more for luck and use less RPE to retain talent when executives have more outside opportunities.

- **Claim 4**: External tournament incentives (measured using MLCs to identify potential employers) predict superior firm performance, validating the labor market as an incentive device.

## Other Interpretations
> Alternative views from other papers.

- [Awaiting future papers]

## Concepts Defined
| Concept | Definition | Wiki Page |
|---------|------------|-----------|
| Managerial Labor Classifications (MLCs) | Network-based groupings of firms that compete for similar managerial talent, derived from compensation benchmarking patterns | [[concepts/MLCs]] |
| Talent Transferability | The extent to which managerial skills are suitable for potential employers, captured by clustering and density of peer networks | [[concepts/talent_transferability]] |
| Outside Opportunities | The number of potential employers a manager could move to, captured by network centrality and Louvain group size | [[concepts/outside_opportunities]] |
| Pay for Luck | Compensation awarded for market/industry returns (luck) rather than firm-specific performance (skill) | [[concepts/pay_for_luck]] |
| Relative Performance Evaluation (RPE) | Filtering out peer performance from executive compensation evaluation | [[concepts/RPE]] |

## Measures/Proxies
> **Computational Definition required** - Findings can reference this table.

| Measure | For Concept | Computational Definition | Wiki Page |
|---------|-------------|--------------------------|-----------|
| PCOMP1 | Talent Transferability | First principal component of [InDegree, Clustering, Louvain_Density, Louvain_Size, Eigenvector]; factor loadings: Clustering(0.523), Louvain_Density(0.524), InDegree(0.438), Louvain_Size(-0.455), Eigenvector(0.232); standardized to mean=0, SD=1 | [[proxies/PCOMP1]] |
| PCOMP2 | Outside Opportunities | Second principal component of same variables; factor loadings: Louvain_Size(0.537), InDegree(0.531), Eigenvector(0.341), Clustering(0.327), Louvain_Density(-0.454); standardized to mean=0, SD=1 | [[proxies/PCOMP2]] |
| InDegree | Network Popularity | Number of firms that select focal firm as compensation peer | [[proxies/InDegree]] |
| Clustering | Local Density | Proportion of pairs of focal firm's direct peers that are also direct peers with each other | [[proxies/Clustering]] |
| Louvain_Density | Group Density | Density of links within the same Louvain group (community detected by Louvain algorithm) | [[proxies/Louvain_Density]] |
| Luck | Exogenous Returns | Annualized fitted value from FirmReturn_{i,t} = α_i + β_i·IndReturn_{j,t} + δ_i·MktReturn_t + ε_{i,t} | [[proxies/Luck]] |
| Skill | Firm-specific Returns | Annualized intercept plus residual from same regression (α_i + ε_{i,t}) | [[proxies/Skill]] |

## Methods
- **Data**: ISS Incentive Lab (compensation peers 2006-2018), Execucomp (executives), CRSP (stock prices), Compustat (financials); 177,010 focal-peer pairs, 1,247 unique focal firms
- **Network Construction**: Directed graph where link A→B formed if firm A selects firm B as compensation peer
- **MLC Methods**: Direct Peer (immediate links), Indirect Peer (transitive), Louvain Peer (community detection via Louvain algorithm maximizing intracluster density)
- **Competition Measures**: Five network measures → PCA → two principal components (PCOMP1, PCOMP2)
- **Validation**: Logistic regression predicting talent flows; OLS regression predicting compensation components

## Limitations
- Competition measures may also capture talent supply (size/quality of available talent pool); authors rely on validation tests to distinguish
- Peer selection may be opportunistic (inflating pay); authors find no correlation with governance proxies
- Sample limited to U.S. public firms with proxy disclosures (2006-2018)

## Related Papers
- [[source/summary/gao_2026]] - Source paper for this summary
- Oyer (2004) - Theory on outside opportunities and pay for luck
- Bertrand & Mullainathan (2001) - Pay for luck controversy
- Albuquerque (2009) - RPE specification
- Gabaix & Landier (2008), Terviö (2008) - Competition and compensation levels