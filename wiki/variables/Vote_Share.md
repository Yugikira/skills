---
name: Vote_Share
measures: [[concepts/Award_Effect]]
domain: finance
first_used: [[source/summary/li_2026_allstar_award_affect_summary]]
---

# Vote_Share

> **Wiki Criteria**: This page is for **directly measurable/basic variables**.
> - Raw counts, indicators, ratios computed from observable data
> - NOT derived/composite variables (PCA components, constructed indices)

## What It Measures
- **Target Concept:** [[concepts/Award_Effect]]
- **Definition:** The percentage of weighted votes received by an analyst relative to total votes for top 15 analysts in the industry.

## Computation
VoteShare_i = Votes received by analyst i / Total votes received by top 15 analysts in industry

Each vote is weighted by the net asset value of the fund managed by the voting fund manager.

## Data Sources
- New Fortune All-Star analyst voting data (proprietary, 2007-2016)
- Institutional Investor voting data (US equivalent)

## Validity Notes
| Aspect | Assessment | Source |
|--------|------------|--------|
| Validity | Weighted voting reflects influence of larger funds | [[source/summary/li_2026_allstar_award_affect_summary]] |
| Confidentiality | Vote counts kept confidential, reducing manipulation | [[source/summary/li_2026_allstar_award_affect_summary]] |

## Alternative Variables for Same Concept
- Vote_Distance - centered version relative to cutoff
- All_Star_Indicator - binary version based on ranking

## Papers Using This Variable
| Paper | How Used | Key Findings |
|-------|----------|--------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | Running variable in RDD (via Distance) | VoteShare determines All-Star status |
| Li et al. (2020) | Determinants of star status | Gender and beauty affect VoteShare |

## Interpretations
> **Selection Criteria**: Include only most valuable sources (max 5 total).

| Paper | Journal | Year | Interpretation |
|-------|---------|------|----------------|
| [[source/summary/li_2026_allstar_award_affect_summary]] | CAR | 2026 | Higher VoteShare = higher award probability; cutoff varies by industry |
| Li et al. | RAS | 2020 | VoteShare affected by analyst characteristics |
| Gu et al. | JAR | 2019 | Connected analysts receive more votes |