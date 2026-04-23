---
title: Does the All-Star Award Affect Chinese Analysts' Performance? Evidence From a Regression Discontinuity Design and the Field
doi: 10.1111/1911-3846.70038
citekey: li_2026_allstar_award_affect
authors: [Congcong Li, Shaokun Li, Hai Lu]
year: 2026
journal: Contemporary Accounting Research
keywords: [analysts, awards, Chinese markets, labor market, regression discontinuity design]
processed: 2026-04-22
source: [[raw/papers/li_2026_allstar_award_affect/li_2026_allstar_award_affect.pdf]]
---

# Does the All-Star Award Affect Chinese Analysts' Performance? Evidence From a Regression Discontinuity Design and the Field

## One-Line Summary
All-Star award causally improves Chinese analysts' performance through enhanced forecast accuracy, concentrated industry coverage, and increased access to internal/external resources.

## Abstract Summary
Using proprietary voting data from New Fortune (2007-2016) and regression discontinuity design, the paper finds that All-Star award recipients exhibit 7.8% better forecast accuracy than non-recipients near the threshold. Award winners concentrate on fewer industries while covering more firms per industry, issue more frequent forecasts, lead larger teams, and conduct more site visits. Survey evidence from analysts and institutional investors corroborates the archival findings.

## Claimed Findings
> **5 KEY INTERPRETATIONS** - Authors' main claims.
>
> **Important**: Claims should correspond to Ground Truth findings below. Claim N should be supported by Ground Truth Finding N.

- Claim 1: All-Star award causally improves analysts' earnings forecast accuracy in fundamental analysis.
- Claim 2: All-Star award enhances the information content of stock recommendations for firms with higher information asymmetry (smaller, less liquid firms).
- Claim 3: All-Star award induces analysts to reallocate effort by concentrating on fewer industries, covering more firms per industry, and issuing more frequent forecasts.
- Claim 4: All-Star award improves analysts' access to internal resources (larger teams) and external resources (more site visits).
- Claim 5: All-Star award reduces forecast bias and increases analyst independence from affiliation pressures.

## Ground Truth Findings
> **5 KEY FINDINGS ONLY** - Main empirical results with variable definitions.
>
> Format: "Variable X (defined as [formula]) has beta=YY (p<ZZ) in [model] (n=XXXX)"
>
> **Correspondence**: The first N findings here should directly support the N claims above.

- Finding 1: Star indicator (defined as =1 if analyst ranked top 3 or 5 by New Fortune in year t) has coefficient -0.078 (p<0.01) in nonparametric local linear regression on AFE (defined as standardized relative forecast error) (n=13,163 forecasts), representing 7.8% better accuracy or 14.2% of sample mean (Table 4, Panel B).
- Finding 2: Star indicator has coefficient 0.012 (p<0.01) on CAR[-1,+1] (defined as 3-day size-adjusted abnormal returns around strong buy recommendations) for low liquidity subsample (Table 5, Panel B); coefficient 0.008 (p<0.10) for small firm subsample.
- Finding 3: Star indicator has coefficient -0.316 (p<0.01) on IndCovrg (defined as ln(number of CSRC industries followed)) representing 31.6% fewer industries; coefficient +0.909 (p<0.05) on NFirmInd (defined as firms per industry); coefficient +2.308 (p<0.10) on FreqInd (defined as forecasts per industry) (Table 6).
- Finding 4: Star indicator has coefficient +0.187 (p<0.10) on Number of Team Members (defined as ln(team size)) (Table 7, Panel A); coefficient +0.751 (p<0.10) on Number of Site Visits (Table 7, Panel B).
- Finding 5: Star indicator has marginally significant negative effect on forecast bias (coefficients not tabulated, p<0.10), indicating award recipients are less biased than non-recipients in earnings forecasts (Section 6.1).

## Other Interpretations
> Alternative views from other papers.

- Emery and Li (2009) argue All-Star rankings are largely based on visibility rather than quality, suggesting awards may not reflect actual performance differences.
- Malmendier and Tate (2009) find superstar CEO awards can distract attention from core responsibilities, potentially reducing performance - competing view to positive award effects.

## Concepts Defined
> **Concepts**: Abstract theoretical ideas (not directly observable).
> **Constructs**: Multi-item measures that operationalize concepts.
>
> **Where to find**: Introduction, Hypothesis Development, Literature Review sections.

| Concept | Definition | Constructs | Wiki Page |
|---------|------------|------------|-----------|
| Analyst Performance | The quality of financial analyst's research outputs, including accuracy of earnings forecasts and information content of stock recommendations | AFE, CAR | [[concepts/Analyst_Performance]] |
| Award Effect | The causal impact of receiving a prestigious recognition on subsequent behavior and performance of recipients | Star indicator, post-award outcomes | [[concepts/Award_Effect]] |
| Analyst Industry Specialization | The degree to which analysts concentrate their coverage and expertise on specific industries | IndCovrg, NFirmInd | [[concepts/Analyst_Industry_Specialization]] |
| Analyst Resource Access | The ability of analysts to obtain internal support (team members, budgets) and external access (management meetings, site visits) | Team size, Site visits | [[concepts/Analyst_Resource_Access]] |
| Information Asymmetry | The degree to which information about a firm is unevenly distributed, creating differential value for analyst research | Firm size, Liquidity | [common concept - no wiki] |

## Measures/Variables
> **Paper Variable** = exact name from paper (use in Ground Truth findings)
> **Wiki Name** = common-sense name (only for directly measurable variables)
> **Wiki Creation**: Skip derived/composite (PCA, indices, fitted values)

| Paper Variable | Wiki Name | Constructs | Concept | Computational Definition | Wiki Page |
|----------------|-----------|------------|---------|--------------------------|-----------|
| AFE | Analyst_Forecast_Error | Analyst Performance | Analyst Performance | [AbsFE_ijt - min(AbsFE_jt)]/[max(AbsFE_jt) - min(AbsFE_jt)], where AbsFE = |forecast EPS - actual EPS|/price | [[variables/Analyst_Forecast_Error]] |
| Star | All_Star_Indicator | Award Effect | Award Effect | =1 if analyst ranked top 3 or 5 by New Fortune in year t | [[variables/All_Star_Indicator]] |
| VoteShare | Vote_Share | [ranking criterion] | Award Selection | Votes received / total votes of top 15 analysts in industry | [[variables/Vote_Share]] |
| Distance | Vote_Distance | [running variable] | Award Effect | VoteShare_i - VoteShare of analyst at cutoff ranking | [[variables/Vote_Distance]] |
| IndCovrg | Industry_Coverage | Analyst Industry Specialization | Analyst Industry Specialization | ln(number of CSRC industries followed between ceremony dates) | [[variables/Industry_Coverage]] |
| NFirmInd | Firm_Coverage_Per_Industry | Analyst Industry Specialization | Analyst Industry Specialization | Number of firms / number of industries followed | [[variables/Firm_Coverage_Per_Industry]] |
| FreqInd | Forecast_Frequency_Per_Industry | Analyst Industry Specialization | Analyst Industry Specialization | Number of forecasts / number of industries followed | [[variables/Forecast_Frequency_Per_Industry]] |
| CAR | Cumulative_Abnormal_Returns | Analyst Performance | Analyst Performance | 3-day size-adjusted abnormal returns [-1,+1] | [[variables/Cumulative_Abnormal_Returns]] |
| BSize | Brokerage_Size | Analyst Resource Access | Analyst Resource Access | ln(number of analysts in brokerage firm) | [[variables/Brokerage_Size]] |

## Hypothesis
> If no explicit hypothesis: write "No explicit hypothesis stated in this paper."

### Hypothesis Statement
**Hypothesis**: All-Star award recipients just above the award threshold perform better in fundamental analysis than non-recipients just below the award threshold during the post-award period.

### Argument Structure
> Premises intended to support the hypothesis.

| Premise | Source | Type |
|---------|--------|------|
| Awards motivate recipients to maintain prestige and exert more effort | Neckermann et al. 2014; Gallus and Frey 2016 | Theory |
| Awards enhance social status and bargaining power, improving access to resources | Frey and Gallus 2017; Merton 1973 (Matthew Effect) | Theory |
| Chinese culture values awards across sectors, creating halo effect | Fisman et al. 2018; Li et al. 2023 | Observation |
| All-Star titles give analysts control over tasks and flexibility to reallocate effort | Meng 2015 | Theory |
| Institutional investors value industry knowledge and timely feedback most | Groysberg et al. 2011; Bradshaw 2012 | Observation |

### Reasoning Approach
- **Type**: Deductive - The hypothesis is derived from established theories on award effects and institutional background.
- **Relation**: Valid - The conclusion necessarily follows if the premises are true: awards provide motivation and resources, which should improve performance.

### Evaluation
- **Status**: Sound
- **Reason**: The deductive argument is valid, and the premises have strong theoretical and empirical support from prior literature. The RDD design tests whether the premises lead to the predicted outcome near the award threshold.

## Methods
Regression discontinuity design (RDD) leveraging New Fortune All-Star voting data:
- **Running variable**: Distance (vote share minus cutoff vote share)
- **Treatment**: Star status (above vs. below threshold)
- **Estimation**: Global polynomial regressions (cubic/quartic) and nonparametric local linear regressions with triangular kernel and optimal bandwidth (Calonico et al. 2014)
- **Validation**: McCrary density test for manipulation; pre-award covariate balance tests
- **Sample**: 2007-2016, 13,163 forecasts, 495 unique analysts within 4% symmetric window around cutoff

Survey methodology: 102 analysts and 385 institutional investors surveyed in 2020 on post-award behavior changes.

> **Wiki Creation**: RDD with vote share threshold is standard method - SKIP wiki page. Survey augmentation is supplementary - SKIP.

## Limitations
- Chinese institutional setting may not generalize to US/European markets
- RDD only identifies local treatment effect near threshold (not average effect for all stars)
- Survey responses may reflect perception rather than actual behavior changes
- Sample restricted to analysts within 4% of cutoff (excludes far-from-threshold cases)
- Pre-award validation shows balance but cannot prove perfect randomness
- Information content of recommendations only significant for high-asymmetry subsample

## Related Papers
> **Process**: List key papers with relevance first. Enrich with full citations from paper's Reference section.
> **Linking**: Link only to papers already in wiki database.

| Authors | Year | Title | Relevance | Wiki Link |
|---------|------|-------|-----------|-----------|
| Stickel, S.E. | 1992 | Reputation and Performance Among Security Analysts | Prior association between All-Star status and performance | [not in wiki] |
| Malmendier, U. and Tate, G. | 2009 | Superstar CEOs | Award distraction effect - competing view | [not in wiki] |
| Gleason, C. and Lee, B. | 2003 | The Price Response to Earnings Forecast Revisions | All-Star market impact precedent | [not in wiki] |
| Guan, Y. et al. | 2019 | Star Analyst Departures and Brokerages | All-Star importance in market | [not in wiki] |
| Li, C., Lin, A., and Lu, H. | 2023 | The Effect of Social Skills on Analyst Performance | Same authors' prior work on analyst determinants | [not in wiki] |
| Li, C. et al. | 2020 | Gender and Beauty in the Financial Analyst Profession | Chinese All-Star determinants | [not in wiki] |
| Meng, X. | 2015 | Analyst Reputation, Communication, and Information Acquisition | Reputational incentives theory | [not in wiki] |
| Malloy, C.J. | 2005 | The Geography of Equity Analysis | Star analyst geographic effects | [not in wiki] |
| Lee, D.S. and Lemieux, T. | 2010 | Regression Discontinuity Designs in Economics | RDD methodology reference | [not in wiki] |
| Calonico, S. et al. | 2014 | Robust Nonparametric Confidence Intervals for RDD | RDD estimation methodology | [not in wiki] |