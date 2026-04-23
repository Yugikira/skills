---
name: Award Effect
domain: finance
first_defined: [[source/summary/li_2026_allstar_award_affect_summary]]
---

# Award Effect

## Definition
The causal impact of receiving a prestigious recognition or award on the subsequent behavior, performance, and resource access of recipients in professional settings.

> **Key Paper**: [[source/summary/li_2026_allstar_award_affect_summary]] - Li et al. (2026) establish causal award effect on analyst performance using RDD.

## Alternative Definitions
Two competing theoretical views: positive effect (motivation/resource access) vs. negative effect (distraction/contentment).

| Definition | Source | Note |
|------------|--------|------|
| "Awards motivate recipients to maintain prestige and exert more effort" | Neckermann et al. 2014 | Positive view |
| "Awards enhance social status and bargaining power" | Frey and Gallus 2017 | Positive view - resources |
| "Awards may reduce motivation or distract from core responsibilities" | Malmendier and Tate 2009 | Negative view - superstar CEOs |

## Constructs & Variables
Award effect operationalized through treatment indicator and post-award outcome measures.

| Construct | Variable | Computational Definition | Key Paper |
|----------|----------|--------------------------|-----------|
| Award Treatment | All_Star_Indicator | =1 if ranked above cutoff threshold | [[source/summary/li_2026_allstar_award_affect_summary]] |
| Running Variable | Vote_Distance | VoteShare - cutoff VoteShare | [[source/summary/li_2026_allstar_award_affect_summary]] |

## Related Theories
- Matthew Effect (Merton 1973) - success breeds success through accumulated advantage
- Halo Effect - prestigious titles unlock resources

## Determinants of Award Effect Magnitude
Effect magnitude depends on institutional and cultural context.

| Determinant | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| Cultural Award Valuation | Higher status from awards in China | [[source/summary/li_2026_allstar_award_affect_summary]] | Halo effect more pronounced in China |
| Organizational Response | Brokerages allocate resources to stars | [[source/summary/li_2026_allstar_award_affect_summary]] | Larger teams, more site visits |

## Economic Consequences of Award Effect
Award effects cascade through labor market and organizational outcomes.

| Consequence | Mechanism | Key Paper | Finding |
|-------------|-----------|-----------|---------|
| Performance Improvement | Motivation and resource access | [[source/summary/li_2026_allstar_award_affect_summary]] | 7.8% better forecast accuracy |
| Career Opportunities | External recognition | Li et al. 2020 | Salary ~US 1 million for top star |
| Brokerage Commissions | Research quality perception | [[source/summary/li_2026_allstar_award_affect_summary]] | 400%+ commission increase |

## Identification Strategy
RDD around award threshold is primary causal identification approach.

| Strategy | Assumption | Key Paper | Note |
|----------|------------|-----------|------|
| RDD | Local random assignment near threshold | [[source/summary/li_2026_allstar_award_affect_summary]] | Unknown ex ante cutoff, large voter pool |

## Future Works
- Test competing positive vs. negative award effects in other professions
- Examine whether award effects persist or diminish over time
- Investigate heterogeneous effects by recipient characteristics
