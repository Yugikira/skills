---
title: Aggregated Compensation Peer Group Disclosure and Managerial Labor Market Competition: A Network Analysis
doi: 10.1111/1475-679X.70026
citekey: gao_2026_aggregated_compensation_peer
authors: [Ray Rui Gao, Yifei Lu]
year: 2026
journal: Journal of Accounting Research
keywords: [managerial labor market, managerial labor classifications, managerial labor competition measures, network analysis, compensation benchmarking peers]
processed: 2026-04-22
source: [[raw/papers/gao_2026_aggregated_compensation_peer/gao_2026_aggregated_compensation_peer.pdf]]
---

# Aggregated Compensation Peer Group Disclosure and Managerial Labor Market Competition: A Network Analysis

## One-Line Summary
Develops network-based managerial labor classifications and competition measures from compensation peer disclosures that capture multidimensional talent demand, validated by talent flow prediction and compensation contract responses.

## Abstract Summary
The authors construct compensation benchmarking networks from proxy statement disclosures to identify managerial labor market competitors and quantify competition intensity. Their classifications (Direct, Indirect, Louvain peers) strongly predict executive job-hopping, outperforming existing predictors. Competition measures (InDegree, Clustering, Eigenvector, Louvain Density/Size) are associated with retention-oriented compensation (higher equity pay, longer vesting). Applying these measures, the paper finds evidence supporting Oyer's [2004] theory on pay-for-luck and RPE, and Fama's [1980] tournament incentive theory.

## Claimed Findings
> **5 KEY INTERPRETATIONS** - Authors' main claims.
>
> **Important**: Claims should correspond to Ground Truth findings below. Claim N should be supported by Ground Truth Finding N.

- Claim 1: Managerial Labor Classifications (MLCs) effectively identify labor market competitors, outperforming conventional predictors (industry, size, location) in predicting talent flows.
- Claim 2: Competition measures capture outside opportunities and talent transferability, inducing firms to offer retention-oriented compensation (higher equity pay with longer vesting periods).
- Claim 3: Labor market competition explains controversial pay practices: firms pay more for luck and use less RPE when facing stronger competition, consistent with Oyer's [2004] theoretical model.
- Claim 4: Labor market provides external tournament incentives: larger tournament prizes (pay gap with potential employers) are associated with superior future firm performance.
- Claim 5: MLCs better capture the theoretical notion of tournament rivals than product industry classifications, enabling more powerful tests of labor theories.

## Ground Truth Findings
> **5 KEY FINDINGS ONLY** - Main empirical results with variable definitions.
>
> Format: "Variable X (defined as [formula]) has beta=YY (p<ZZ) in [model] (n=XXXX)"
>
> **Correspondence**: The first N findings here should directly support the N claims above.

- Finding 1: Selected Peer (defined as indicator=1 if focal firm i selects firm j as compensation peer in year t) has coefficient 2.787*** (z=13.565) in logistic regression predicting Talent Flow_{ijt+1} (n=15,823,862 pairs). Pseudo-R2 of MLC-only model (Column 4) is 9.7%, comparable to all Faulkender predictors combined (7.5%). Selected Peer's relative margin is 16.14, ranking 1st among 20+ predictors.
- Finding 2: InDegree (defined as count of firms selecting focal firm as compensation peer, standardized) has coefficient 0.105*** (t=7.363) in OLS regression on Ln(Total Pay) (n=9,798 firm-years). PCOMP1 coefficient 0.069*** on Ln(Total Pay) means one SD increase in competition = 6.9% higher pay. Equity Pay increases by 15.1% per SD increase in PCOMP1 (p<0.01). Pay Duration increases by 0.038 years per SD increase in PCOMP1 (p<0.05).
- Finding 3: Luck x PCOMP1 interaction has coefficient 0.088*** (t=2.624) in OLS regression on Ln(Total Pay), meaning firms pay 8.8% more for luck per one SD increase in competition (n=7,396). Ln(Return Peer) x PCOMP1 has coefficient 0.058** (t=1.986), reducing RPE sensitivity from -0.654 to -0.347 per one SD increase in competition (45.6% reduction).
- Finding 4: Ln(Louvain Peer Pay Gap) (defined as ln[1 + pay gap between focal CEO and second-highest-paid CEO among Louvain peers]) has coefficient 0.027*** (t=2.860) on Tobin's Q (n=8,108), meaning tournament prize predicts firm value. Ln(FF48 Pay Gap) coefficient 0.004 (insignificant); Ln(TNIC2 Pay Gap) coefficient 0.008 (insignificant), demonstrating MLCs better capture tournament rivals.
- Finding 5: Louvain Peer Same Product Industry (coefficient 1.748***, z=6.113) and Louvain Peer Diff Product Industry (coefficient 1.391***, z=6.134) both strongly predict Talent Flow, demonstrating MLCs capture multidimensional skills beyond industry. Direct Peer Diff Product Industry coefficient 3.279*** (z=15.156) is significantly larger than Direct Peer Same Product Industry (z=10.510).

## Other Interpretations
> Alternative views from other papers.

- [Awaiting future papers]

## Concepts Defined
> **Concepts**: Abstract theoretical ideas (not directly observable).
> **Constructs**: Multi-item measures that operationalize concepts.
>
> **Where to find**: Introduction, Hypothesis Development, Literature Review sections.

| Concept | Definition | Constructs | Wiki Page |
|---------|------------|------------|-----------|
| Managerial Labor Classifications | Groupings of firms that compete for similar managerial talent, identifying potential employers for executives | Direct Peer, Indirect Peer, Louvain Peer | [[concepts/Managerial_Labor_Classifications]] |
| Outside Opportunities | The number and quality of alternative employment options available to executives in the managerial labor market | InDegree, Louvain Size | [[concepts/Outside_Opportunities]] |
| Talent Transferability | The degree to which executive skills and human capital are applicable across different firms in the labor market | Clustering, Eigenvector, Louvain Density | [[concepts/Talent_Transferability]] |
| Compensation Benchmarking Network | A directed graph linking firms based on peer selection choices, representing firms' relative positions in the managerial labor market | Network edges (peer selections), Louvain groups | [implicit - see Methods] |

## Measures/Variables
> **Paper Variable** = exact name from paper (use in Ground Truth findings)
> **Wiki Name** = common-sense name (only for directly measurable variables)
> **Wiki Creation**: Skip derived/composite (PCA, indices, fitted values)

| Paper Variable | Wiki Name | Constructs | Concept | Computational Definition | Wiki Page |
|----------------|-----------|------------|---------|--------------------------|-----------|
| InDegree | Peer_Selection_Count | Outside Opportunities | Outside Opportunities | Count of firms selecting focal firm as compensation peer in year t | [[variables/Peer_Selection_Count]] |
| Clustering | Peer_Clustering_Rate | Talent Transferability | Talent Transferability | Number of links between focal firm's peers divided by maximum possible links between peers | [[variables/Peer_Clustering_Rate]] |
| Eigenvector | Network_Centrality | Talent Transferability | Talent Transferability | Eigenvector centrality from connection matrix A, satisfying lambda*E = A*E | [[variables/Network_Centrality]] |
| Louvain Density | Louvain_Group_Density | Talent Transferability | Talent Transferability | Number of links in Louvain group divided by maximum possible links in group | [[variables/Louvain_Group_Density]] |
| Louvain Size | Louvain_Group_Size | Outside Opportunities | Outside Opportunities | Count of firms in each Louvain group | [[variables/Louvain_Group_Size]] |
| Talent Flow | Talent_Flow | [indicator] | Managerial Labor Competition | Indicator=1 if top 5 executive of firm i moves to top 5 position of firm j within 1 year | [[variables/Talent_Flow]] |
| Selected Peer | Selected_Peer | [indicator] | Managerial Labor Classification | Indicator=1 if focal firm i selects firm j as compensation peer in year t | [[variables/Selected_Peer]] |
| PCOMP1 | [derived] | Composite Competition | Labor Market Competition | First principal component of 5 competition measures (standardized) | [no wiki - derived] |
| PCOMP2 | [derived] | Composite Competition | Labor Market Competition | Second principal component of 5 competition measures (standardized) | [no wiki - derived] |
| Fitted Pay | [derived] | Predicted Pay | Labor Competition Effect | Fitted value from competition measures in total pay regression | [no wiki - derived] |

## Hypothesis
> If no explicit hypothesis: write "No explicit hypothesis stated in this paper."

### Hypothesis Statement
No single formal hypothesis stated. The paper tests multiple theoretical predictions:
1. **H1 (Implicit)**: MLCs predict talent flows better than conventional predictors.
2. **H2 (Implicit)**: Competition measures are positively associated with total pay and retention-oriented compensation structure.
3. **H3 (Oyer's Theory)**: Firms pay more for luck and use less RPE when facing stronger labor market competition.
4. **H4 (Fama/Tournament)**: Larger tournament prizes from potential employers induce superior future performance.

### Argument Structure
> Premises intended to support the hypothesis.

| Premise | Source | Type |
|---------|--------|------|
| Compensation peers reflect firms' talent demand across multiple dimensions (industry, size, location, operations) | Institutional Background (SEC disclosure, Equilar survey) | Observation |
| Network analysis extracts latent labor market structure from aggregated peer choices | Network Theory (Jaffe 1986, Hoberg & Phillips 2016) | Assumption |
| Boards possess private information about labor competitors unavailable to researchers | Brickley & Zimmerman [2010] | Assumption |
| Outside opportunities increase reservation wage; talent transferability expands potential employer set | Oyer [2004], Murphy & Zabojnik [2004, 2007] | Theory |
| Labor market provides tournament incentives through external employment opportunities | Fama [1980], Lazear & Rosen [1981] | Theory |

### Reasoning Approach
- **Type**: Inductive - The paper develops novel measures from data patterns and validates them empirically rather than deductively testing pre-specified hypotheses.
- **Relation**: Strong - The empirical evidence provides probabilistic support for the theoretical predictions, but causal interpretation relies on observational data and endogeneity controls.

### Evaluation
- **Status**: Cogent
- **Reason**: The measures are validated through multiple tests (talent flow prediction, compensation association, theoretical applications), but the observational nature limits causal claims. The predictions from established theories (Oyer, Fama) are confirmed, strengthening the interpretation.

## Methods
Network analysis of compensation peer disclosures to construct:
1. **MLCs**: Three classification types (Direct, Indirect, Louvain) using Louvain community detection algorithm
2. **Competition Measures**: Five network metrics (InDegree, Clustering, Eigenvector, Louvain Density, Louvain Size)
3. **Validation**: Logistic regression for talent flows; OLS for compensation; interaction models for pay-for-luck and RPE

Sample: 2006-2018, ISS Incentive Lab + Execucomp + CRSP + Compustat; 177,010 focal-peer pairs; 9,342 firm-years

> **Wiki Creation**: Network-Based MLC Design is novel methodology - CREATE wiki page. Standard OLS/logistic - SKIP.

## Limitations
- Observational data: endogeneity concerns despite extensive controls (reverse causality, omitted variables)
- Peer selection may reflect opportunistic benchmarking (though network aggregation mitigates this)
- Sample limited to U.S. public firms with proxy disclosures (excludes private firms, international)
- Talent flow measure limited to top 5 executives (may miss lateral moves)
- Louvain algorithm parameters affect classification granularity (sensitivity not tested)

## Related Papers
> **Process**: List key papers with relevance first. Enrich with full citations from paper's Reference section.
> **Linking**: Link only to papers already in wiki database.

| Authors | Year | Title | Relevance | Wiki Link |
|---------|------|-------|-----------|-----------|
| Oyer, P. | 2004 | Why Do Firms Use Incentives That Have No Incentive Effects? | Theory of outside opportunities explaining pay-for-luck and RPE puzzle | [not in wiki] |
| Fama, E.F. | 1980 | Agency Problems and the Theory of the Firm | Theory of labor market as incentive device | [not in wiki] |
| Faulkender, M. and Yang, J. | 2010 | Inside the Black Box: The Role and Composition of Compensation Peer Groups | Prior work on peer selection determinants | [not in wiki] |
| Albuquerque, A.M., De Franco, G. and Verdi, R.S. | 2013 | Peer Choice in CEO Compensation | Benchmarking literature foundation | [not in wiki] |
| Hoberg, G. and Phillips, G. | 2016 | Text-Based Network Industries and Endogenous Product Differentiation | Network analysis methodology precedent | [not in wiki] |
| Core, J.E., Holthausen, R.W. and Larcker, D.F. | 1999 | Corporate Governance, CEO Compensation, and Firm Performance | Research design for future performance tests | [not in wiki] |
| Daniel, N.D., Li, Y. and Naveen, L. | 2020 | Symmetry in Pay for Luck | Pay-for-luck measurement methodology | [not in wiki] |
| Murphy, K.J. and Zabojnik, J. | 2004 | CEO Pay and Appointments: A Market-Based Explanation for Recent Trends | Talent transferability theory | [not in wiki] |
| Lazear, E.P. and Rosen, S. | 1981 | Rank-Order Tournaments as Optimum Labor Contracts | Tournament theory foundation | [not in wiki] |
| Fee, C.E. and Hadlock, C.J. | 2003 | Raids, Rewards, and Reputations in the Market for Managerial Talent | Talent flow and executive mobility literature | [not in wiki] |