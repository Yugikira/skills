---
title: Aggregated Compensation Peer Group Disclosure and Managerial Labor Market Competition: A Network Analysis
doi: 10.1111/1475-679X.70026
citekey: gao_2026_aggregated_compensation_peer
authors: [Ray Rui Gao, Yifei Lu]
year: 2025
journal: Journal of Accounting Research
keywords: [managerial labor market, managerial labor classifications, managerial labor competition measures, network analysis, compensation benchmarking peers]
processed: 2026-04-22
source: [[raw/papers/gao_2026_aggregated_compensation_peer/gao_2026_aggregated_compensation_peer.pdf]]
---

# Aggregated Compensation Peer Group Disclosure and Managerial Labor Market Competition: A Network Analysis

## One-Line Summary
Develops novel network-based measures of managerial labor market classifications and competition using compensation peer group disclosures, demonstrating superior predictive power for executive moves and validating associations with retention tools and theoretical predictions.

## Abstract Summary
This paper constructs networks from compensation benchmarking peer disclosures to create Managerial Labor Classifications (MLCs) and competition measures. These classifications outperform existing predictors in predicting executive job moves, capturing multidimensional and dynamic talent competition features. Competition measures are associated with higher equity pay, longer vesting periods, and can explain controversial pay practices like pay for luck and reduced RPE use.

## Claimed Findings
> **3-5 KEY INTERPRETATIONS** - Authors' main claims.
>
> **Important**: Claims should correspond to Ground Truth findings below. Claim N should be supported by Ground Truth Finding N.

- Claim 1: MLCs strongly predict talent flows and outperform existing predictors (industry, size, location) in identifying labor market competitors.
- Claim 2: Competition measures are associated with retention tools - higher equity pay, longer pay duration - consistent with labor demand interpretation.
- Claim 3: Labor market competition explains controversial pay practices: firms pay more for luck and use less RPE when facing greater competition.
- Claim 4: External tournament incentives from labor market competition are associated with superior future firm performance.

## Ground Truth Findings
> **3-5 KEY FINDINGS ONLY** - Main empirical results with variable definitions.
>
> Format: "Variable X (defined as [formula]) has β=YY (p<ZZ) in [model] (n=XXXX)"

- Finding 1: InDegree (defined as number of firms selecting focal firm as compensation peer) and Clustering (defined as clustering coefficient in compensation peer network) have positive and significant coefficients (p<0.01) in logistic regression predicting Talent_Flow (n=various). MLCs have pseudo-R² comparable to all existing predictors combined.
- Finding 2: PCOMP1 (defined as first principal component of InDegree, Clustering, Louvain Density, Louvain Size, Eigenvector) has β=0.069 (p<0.001) in OLS regression on Ln(Total Pay) (n=9,798). PCOMP2 (second principal component) has β=0.070 (p<0.001). A one standard deviation increase in PCOMP1/PCOMP2 is associated with 6.9%/7.0% increase in CEO compensation.
- Finding 3: Equity Pay percentage increases with competition measures. InDegree, Clustering, Louvain Density, Louvain Size, and Eigenvector all have positive significant coefficients (p<0.01) on Equity_Pct. Pay Duration also increases significantly with competition measures.
- Finding 4: Luck x PCOMP1 and Luck x PCOMP2 have positive and significant coefficients (p<0.05) in regression on Ln(Total Pay), indicating firms pay more for luck when facing greater competition. Return_Peer x PCOMP1 and Return_Peer x PCOMP2 have positive significant coefficients in RPE tests, indicating less RPE filtering with greater competition.
- Finding 5: Ln(Potential Employer Pay Gap) (defined as pay gap between focal CEO and second-highest pay among MLC peers) has positive significant coefficient on Tobin Q (p<0.05), indicating external tournament incentives improve firm performance. Fitted Pay (competition-driven compensation) is associated with better future ROA and stock returns (p<0.05).

## Other Interpretations
> Alternative views from other papers.

- [Awaiting future papers]

## Concepts Defined
> **Concepts**: Abstract theoretical ideas (not directly observable).
> **Constructs**: Multi-item measures that operationalize concepts.

| Concept | Definition | Constructs | Wiki Page |
|---------|------------|------------|-----------|
| Outside Opportunities | The number of alternative employment options available to executives, affecting their reservation wage and poaching risk | InDegree, Louvain Size, PCOMP2 | [[concepts/Outside_Opportunities]] |
| Talent Transferability | The extent to which executive skills are suitable for potential employers, affecting poaching risk | Clustering, Louvain Density, Eigenvector, PCOMP1 | [[concepts/Talent_Transferability]] |
| Managerial Labor Market Competition | The intensity of competition for managerial talent among firms, encompassing both outside opportunities and talent transferability | PCOMP1, PCOMP2 | [[concepts/Managerial_Labor_Market_Competition]] |
| Managerial Labor Classifications (MLCs) | Network-based groupings of firms that compete for similar managerial talent | Direct Peer, Indirect Peer, Louvain Peer | [[concepts/Managerial_Labor_Classifications]] |

## Measures/Variables
> **Paper Variable** = exact name from paper (use in Ground Truth findings)
> **Wiki Name** = common-sense name (only for directly measurable variables)
> **Wiki Creation**: Skip derived/composite (PCA, indices, fitted values)

| Paper Variable | Wiki Name | Constructs | Concept | Computational Definition | Wiki Page |
|----------------|-----------|------------|---------|--------------------------|-----------|
| InDegree | Peer_Selection_Count | Network Position | Outside Opportunities | Number of firms selecting focal firm as compensation peer | [[variables/Peer_Selection_Count]] |
| Clustering | Peer_Clustering_Rate | Network Clustering | Talent Transferability | Clustering coefficient: number of links between peers divided by maximum possible links | [[variables/Peer_Clustering_Rate]] |
| Louvain Density | Louvain_Group_Density | Group Clustering | Talent Transferability | Density of links within Louvain group: links divided by maximum possible links | [[variables/Louvain_Group_Density]] |
| Louvain Size | Louvain_Group_Size | Group Size | Outside Opportunities | Number of firms in each Louvain group | [[variables/Louvain_Group_Size]] |
| Eigenvector | Network_Centrality | Network Position | Talent Transferability | Eigenvector centrality from compensation benchmarking network adjacency matrix | [[variables/Network_Centrality]] |
| PCOMP1 | [derived] | Talent Transferability Composite | Talent Transferability | First principal component of 5 network measures (35.06% variance) | [no wiki] |
| PCOMP2 | [derived] | Outside Opportunities Composite | Outside Opportunities | Second principal component of 5 network measures (28.11% variance) | [no wiki] |
| Talent_Flow | Executive_Move | Talent Mobility | Labor Competition | Indicator: 1 if top-5 executive moves to top-5 position at another firm within one year | [[variables/Executive_Move]] |
| Fitted Pay | [derived] | Competition-Driven Pay | Market Wage | Fitted value from regression of Total Pay on all competition measures | [no wiki] |

## Hypothesis
> If no explicit hypothesis: write "No explicit hypothesis stated in this paper."

### Hypothesis Statement
1. MLCs better identify labor market competitors than product industry classifications
2. Competition measures are positively associated with compensation level and retention tools
3. Labor market competition explains controversial pay practices (pay for luck, reduced RPE)
4. External tournament incentives from MLC peers are associated with superior performance

### Argument Structure
| Premise | Source | Type |
|---------|--------|------|
| Compensation peer selection reflects firms' demand for managerial talent | Institutional background (SEC disclosure, Equilar report) | Observation |
| Network position captures relative position in managerial labor market | Theory (Hotelling-like talent space) | Assumption |
| Outside opportunities increase poaching risk | Theory (Oyer 2004) | Claim |
| Talent transferability affects poaching risk | Theory (Murphy and Zabojnik 2004, 2007) | Claim |

### Reasoning Approach
- **Type**: Inductive - Empirical validation of theoretical constructs through network analysis
- **Relation**: Strong - Evidence supports probabilistic claims about labor market competition

### Evaluation
- **Status**: Cogent
- **Reason**: Strong empirical evidence from multiple tests (talent flow prediction, compensation validation, theoretical applications)

## Methods
- **Network Analysis**: Constructed directed compensation benchmarking networks from peer group disclosures (2006-2018, ISS Incentive Lab)
- **MLC Design**: Three classifications - Direct Peer (directly linked firms), Indirect Peer (transitive links), Louvain Peer (Louvain community detection algorithm)
- **Competition Measures**: Five network statistics (InDegree, Clustering, Louvain Density, Louvain Size, Eigenvector) + PCA to derive PCOMP1, PCOMP2
- **Validation Tests**: Logistic regression for talent flows; OLS for compensation components; interaction models for pay for luck and RPE

> **Wiki Creation**: Novel MLC design warrants wiki method page.

## Novel Methodology
> [[methods/Network_Based_MLC_Design]] - Novel approach for constructing managerial labor classifications using compensation peer networks

## Limitations
- Competition measures could capture talent supply (size/quality of talent pool) rather than demand
- Peer selection could be opportunistic (justify higher pay) rather than talent-driven
- Sample limited to firms with Execucomp data (large public firms)
- Network measures require sufficient peer disclosure coverage

## Related Papers
| Authors | Year | Title | Relevance | Wiki Link |
|---------|------|-------|-----------|-----------|
| Oyer | 2004 | Why do firms use incentives that are unrelated to worker performance? | Theory of outside opportunities and pay for luck | [not in wiki] |
| Murphy and Zabojnik | 2004, 2007 | Managerial capital and firm performance | Theory of talent transferability | [not in wiki] |
| Faulkender and Yang | 2010 | Inside the "Black Box" of compensation peer selection | Alternative view: opportunistic peer selection | [not in wiki] |
| Hoberg and Phillips | 2016 | Text-based network industries and endogenous product differentiation | Network-based market classification precedent | [not in wiki] |
| Fee and Hadlock | 2003 | Raids, recruiting, and the competition for managerial talent | Talent flow precedent | [not in wiki] |
