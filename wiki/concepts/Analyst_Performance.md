---
name: Analyst Performance
domain: finance
first_defined: [[source/summary/li_2026_allstar_award_affect_summary]]
---

# Analyst Performance

## Definition
The quality of financial analyst's research outputs, encompassing the accuracy of earnings forecasts, the information content of stock recommendations, and the overall value of research services provided to institutional investors.

> **Key Paper**: [[source/summary/li_2026_allstar_award_affect_summary]] - Li et al. (2026) establish causal link between All-Star award and analyst performance using RDD.

## Alternative Definitions
Performance definitions vary across traditions: some focus on forecast accuracy alone, others include stock recommendation profitability and market impact.

| Definition | Source | Note |
|------------|--------|------|
| "Accuracy of earnings forecasts signals the quality of analysts' research" | [[source/summary/li_2026_allstar_award_affect_summary]] | Primary measure in Li et al. |
| "Information content measured by market reactions to recommendations" | [[source/summary/li_2026_allstar_award_affect_summary]] | Supplementary measure |
| "Timely feedback and industry knowledge valued by institutional investors" | Groysberg et al. 2011 | Service quality dimension |

## Constructs & Variables
Primary operationalization uses standardized forecast accuracy and market reaction measures.

| Construct | Variable | Computational Definition | Key Paper |
|----------|----------|--------------------------|-----------|
| Forecast Accuracy | Analyst_Forecast_Error | [AbsFE_ijt - min(AbsFE_jt)]/[max(AbsFE_jt) - min(AbsFE_jt)] | [[source/summary/li_2026_allstar_award_affect_summary]] |
| Information Content | Cumulative_Abnormal_Returns | 3-day size-adjusted CAR[-1,+1] around recommendations | [[source/summary/li_2026_allstar_award_affect_summary]] |

## Related Theories
- Award Effect Theory - awards causally improve subsequent performance
- Reputational Incentives Theory (Meng 2015) - star analysts have incentives to provide quality service

## Determinants of Analyst Performance
Main factors include awards, industry specialization, and resource access.

| Determinant | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| All-Star Award | Motivates effort, improves resource access | [[source/summary/li_2026_allstar_award_affect_summary]] | 7.8% better forecast accuracy |
| Industry Specialization | Concentrated expertise | [[source/summary/li_2026_allstar_award_affect_summary]] | Fewer industries, more firms per industry |
| Team Size | Delegated routine work | [[source/summary/li_2026_allstar_award_affect_summary]] | Larger teams post-award |

## Economic Consequences of Analyst Performance
Performance affects market efficiency and brokerage commissions.

| Consequence | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| Market Reaction | Information content in recommendations | [[source/summary/li_2026_allstar_award_affect_summary]] | Stronger CAR for high-asymmetry firms |
| Brokerage Commissions | Research quality valuation | Li et al. 2020 | All-Star acquisition increases commissions 400%+ |

## Identification Strategy
Regression discontinuity design around award threshold is primary causal approach.

| Strategy | Assumption | Key Paper | Note |
|----------|------------|-----------|------|
| RDD | Analysts near threshold cannot manipulate vote share | [[source/summary/li_2026_allstar_award_affect_summary]] | Large voter pool, confidential votes |

## Future Works
- Test award effects in US/European markets for generalizability
- Examine persistence of award effects over multiple years
- Investigate heterogeneous effects by analyst characteristics (experience, gender)