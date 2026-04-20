---
title: {Paper Title}
doi: {doi}
citekey: {citekey}
authors: [{Author 1}, {Author 2}, ...]
year: {YYYY}
journal: {Journal Name}
keywords: [{keyword1}, {keyword2}, ...]
processed: {YYYY-MM-DD}
source: [[raw/papers/{citekey}/{citekey}.pdf]]
---

# {Paper Title}

## One-Line Summary
{What the paper contributes in one sentence}

## Abstract Summary
{2-3 sentence paraphrase}

## Claimed Findings
> **3-5 KEY INTERPRETATIONS** - Authors' main claims.
>
> **Important**: Claims should correspond to Ground Truth findings below. Claim N should be supported by Ground Truth Finding N.

- Claim 1: {primary interpretation}
- Claim 2: {secondary interpretation}
- Claim 3: {third interpretation}

## Ground Truth Findings
> **3-5 KEY FINDINGS ONLY** - Main empirical results with variable definitions.
>
> Format: "Variable X (defined as [formula]) has β=YY (p<ZZ) in [model] (n=XXXX)"
>
> **Correspondence**: The first N findings here should directly support the N claims above.
>
> If a variable is defined in Measures table or earlier finding, can reference it.

- Finding 1: {key result supporting Claim 1 - with full definitions}
- Finding 2: {key result supporting Claim 2 - can reference Finding 1}
- Finding 3: {key result supporting Claim 3}
- Finding 4: {optional}
- Finding 5: {optional}

## Other Interpretations
> Alternative views from other papers.

- [Awaiting future papers]

## Concepts Defined
| Concept | Definition | Wiki Page |
|---------|------------|-----------|
| {concept} | {brief definition} | [[concepts/{concept}]] |

## Measures/Proxies
> **Computational Definition required** - Findings can reference this table.

| Measure | For Concept | Computational Definition | Wiki Page |
|---------|-------------|--------------------------|-----------|
| {proxy} | {concept} | {exact formula} | [[proxies/{proxy}]] |

## Methods
{Brief methodology, sample, data sources}

## Limitations
- {limitation 1}
- {limitation 2}

## Related Papers
- [[source/summary/{citekey}]] - {relevance}