---
title: Aggregated Compensation Peer Group Disclosure and Managerial Labor Market Competition: A Network Analysis
doi: 10.1111/1475-679x.70026
citekey: gao_2026_aggregated_compensation_peer
authors: [GAO, RAY RUI, LU, YIFEI]
year: 2026
journal: Journal of Accounting Research
keywords: [managerial labor market, managerial labor classifications, managerial labor competition measures, network analysis, compensation benchmarking peers]
processed: 2026-04-15
source: [[raw/papers/gao_2026_aggregated_compensation_peer/gao_2026_aggregated_compensation_peer.pdf]]
---

# Aggregated Compensation Peer Group Disclosure and Managerial Labor Market Competition: A Network Analysis

## One-Line Summary
Develops network-based measures of managerial labor market classification and competition from compensation peer disclosures, demonstrating they outperform industry-based measures in predicting executive moves and explaining pay practices.

## Abstract Summary
The authors construct networks from compensation benchmarking peer disclosures to develop novel Managerial Labor Classifications (MLCs) and competition measures. These MLCs predict executive job moves better than existing predictors (industry, size, location). Competition measures are linked to retention tools (higher equity pay, longer vesting). The measures explain controversial pay practices (pay for luck, RPE puzzle) and demonstrate external tournament incentives.

## Ground Truth Findings
> Objective observations without interpretation. What the data/methods actually show.

- Finding 1: MLCs (Direct Peer, Indirect Peer, Louvain Peer) predict future talent flows (executive job moves) with explanatory power comparable to all existing predictors combined.
- Finding 2: Executives move to both selected peers (firms' self-identified compensation peers) and potential peers (firms in same MLC but not selected), indicating MLCs identify additional competitors beyond self-disclosed ones.
- Finding 3: Both peers within and outside same product industry predict talent flows, indicating MLCs capture multidimensional skill demand.
- Finding 4: Current peers have greater predictive power for talent flows than past/future peers, indicating dynamic feature of labor competition.
- Finding 5: CEOs facing higher competition (PCOMP1, PCOMP2) receive higher total pay, specifically higher equity pay percentage and longer pay duration.
- Finding 6: Firms pay more for luck (Luck × PCOMP coefficients positive, significant at 1%) when facing higher labor competition.
- Finding 7: Firms use less RPE (Ln(Return Peer) × PCOMP positive, significant at 5%) when facing higher competition.
- Finding 8: Tournament prize calculated from MLCs (Ln(Direct/Indirect/Louvain Peer Pay Gap)) positively predicts Tobin's Q (significant at 1%), while product industry-based gaps are insignificant.
- Finding 9: Fitted pay from competition measures positively predicts future ROA and stock returns over 1-3 year windows.

## Claimed Findings
> The paper's interpretations of the findings. How the authors explain the results.

- Claim 1: MLCs better capture managerial labor market competitors than product industry classifications because they reflect firms' multidimensional and dynamic talent demand.
- Claim 2: Compensation peer group disclosure contains rich information about labor market competition, as boards incorporate private information about competitors.
- Claim 3: Pay for luck and reduced RPE use are rational responses to labor market competition (supporting Oyer's 2004 theory), not evidence of rent extraction.
- Claim 4: External tournament incentives exist in the managerial labor market - CEOs strive to outperform labor competitors to win higher-paying positions.
- Claim 5: Higher pay induced by competition incentivizes better performance, ruling out rent-seeking interpretation of competition measures.

## Other Interpretations
> Alternative interpretations from other papers or later analysis. Updated as wiki evolves.

- (No alternative interpretations recorded yet)

## Concepts Defined
| Concept | Definition | Wiki Page |
|---------|------------|-----------|
| Managerial Labor Classification (MLC) | Network-based groupings of firms that compete for similar managerial talent, derived from compensation benchmarking disclosures. Three types: Direct Peer, Indirect Peer, Louvain Peer. | [[concepts/managerial_labor_classification]] |
| Managerial Labor Market Competition | The extent of competition a firm faces in hiring and retaining executive talent, measured by outside opportunities and talent transferability. | [[concepts/managerial_labor_market_competition]] |
| Compensation Benchmarking Network | Directed network where firms are linked if one cites another as compensation peer. Represents firms' relative positions in managerial talent space. | [[concepts/compensation_benchmarking_network]] |
| Outside Opportunities | Alternative employment options available to executives, which increase with labor market competition. (From Oyer 2004) | [[concepts/outside_opportunities]] |
| Talent Transferability | The degree to which executives' skills are suitable for potential employers beyond current firm. (From Murphy and Zabojnik 2004, 2007) | [[concepts/talent_transferability]] |
| Pay for Luck | Compensation awarded for firm performance attributable to external factors (market/industry returns) rather than managerial skill. | [[concepts/pay_for_luck]] |
| Relative Performance Evaluation (RPE) | Filtering out common shocks by benchmarking performance against peer firms. RPE puzzle: why firms don't use RPE extensively. | [[concepts/relative_performance_evaluation]] |
| External Tournament Incentives | Incentives for CEOs to outperform labor market competitors to win higher-paying positions (tournament prize). | [[concepts/external_tournament_incentives]] |

## Measures/Proxies
| Measure | For Concept | How Used | Wiki Page |
|---------|-------------|----------|-----------|
| PCOMP1, PCOMP2 | Managerial Labor Market Competition | Principal components of 5 network measures; standardized competition proxies. | [[proxies/pcomp_competition_measures]] |
| InDegree | Outside Opportunities | Number of times a firm is benchmarked by others; more benchmarked = more outside options. | [[proxies/indegree_competition]] |
| Clustering Coefficient | Talent Transferability | Density of connections among firm's peers; higher clustering = skills more transferable within cluster. | [[proxies/clustering_competition]] |
| Louvain Density | Competition Intensity | Density of connections within Louvain group; higher density = more intense competition. | [[proxies/louvain_density_competition]] |
| Louvain Size | Competition Scope | Number of firms in Louvain group; larger group = broader competition scope. | [[proxies/louvain_size_competition]] |
| Eigenvector Centrality | Competition Centrality | Importance in network based on connections to important firms; high centrality = central in talent market. | [[proxies/eigenvector_competition]] |
| Pay Duration | Retention Effort | Vesting period of pay components (Gopalan et al. 2014). Longer duration = stronger retention. | [[proxies/pay_duration]] |
| Luck/Skill Decomposition | Pay for Luck | Luck = fitted industry+market returns; Skill = intercept+residual (Daniel, Li, Naveen 2020). | [[proxies/luck_skill_decomposition]] |

## Methods
Network analysis using compensation peer disclosures (ISS Incentive Lab 2006-2018). Constructed directed network of focal-peer links. Applied Louvain algorithm for community detection. Five network-based competition measures (InDegree, Clustering, Louvain Density, Louvain Size, Eigenvector). Principal component analysis to derive PCOMP1/PCOMP2. Panel regressions with industry/year fixed effects.

Key empirical tests:
1. Talent flow prediction (logit models for executive moves)
2. Compensation components (OLS with competition measures)
3. Pay for luck (interaction: Luck × PCOMP)
4. RPE use (interaction: Ln(Return Peer) × PCOMP)
5. Tournament incentives (Tobin's Q on Pay Gap)
6. Future performance (Future ROA/Return on Fitted Pay)

## Limitations & Future Work
- Sample limited to U.S. public firms (2006-2018), may not generalize to private firms or other countries
- Compensation peer disclosure may reflect both retention motives and rent-seeking; cannot fully disentangle
- Network measures capture labor demand primarily; may also capture aspects of supply
- Cannot observe actual outside job offers; only observe realized moves

## Related Papers
- [[source/summary/oyer_2004]] - Theory: outside opportunities explain pay practices
- [[source/summary/murphy_zabojnik_2004]] - Theory: talent transferability affects compensation
- [[source/summary/fama_1980]] - Theory: labor market disciplines managers
- [[source/summary/lazear_rosen_1981]] - Tournament theory
- [[source/summary/bertrand_mullainathan_2001]] - Pay for luck as rent extraction
- [[source/summary/daniel_li_naveen_2020]] - Luck/Skill decomposition method
