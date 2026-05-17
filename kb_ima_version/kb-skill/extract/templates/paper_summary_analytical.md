---
title: "{Paper Title}"
doi: {doi}
citekey: {citekey}
authors: [{Author 1}, {Author 2}, ...]
year: {YYYY}
journal: {Journal Name}
keywords: [{keyword1}, {keyword2}, ...]
processed: {YYYY-MM-DD}
source: [[raw/papers/{citekey}/{citekey}.pdf]]
paper_type: analytical
---

# {Paper Title}

## One-Line Summary
{What the analytical model contributes in one sentence}

## Abstract Summary
{2-3 sentence paraphrase}

## Claim Findings
> **3-5 KEY THEORETICAL IMPLICATIONS** - Implications of the model results.
>
> **Important**: Claims should correspond to Ground Truth findings below. Claim N should be supported by Ground Truth Finding N (Theorem/Proposition).

- Claim 1: {primary theoretical implication}
- Claim 2: {secondary implication}
- Claim 3: {third implication}

## Ground Truth Findings
> **3-5 KEY FINDINGS ONLY** - Use Theorem/Proposition format, NOT coefficient format.
>
> **Correspondence**: The first N findings here should directly support the N claims above.

- Finding 1: **Theorem/Proposition N** - {theorem statement with conditions}
- Finding 2: **Theorem/Proposition M** - {theorem statement}
- Finding 3: {additional result}

## Model Structure
> **Key equations and assumptions.**

### Core Model
{Brief description of model purpose and setting}

### Key Equations
| Equation | Description | Assumptions |
|----------|-------------|-------------|
| {equation} | {what it represents} | {required assumption} |

### Comparative Statics
{How results change with parameter variations}

## Model Parameters & Constructs
> **For analytical models: These are theoretical constructs.**
> Create wiki/constructs/ pages. NO wiki/variables/ pages.

| Construct | Symbol | Type | Definition | Wiki Page |
|-----------|--------|------|------------|-----------|
| {name} | λ | model_parameter | {definition} | [[constructs/{name}]] |
| {name} | - | definitional_construct | {definition} | [[constructs/{name}]] |

## Concepts Defined
> **Concepts**: Abstract theoretical ideas (not directly observable).

| Concept | Definition | Constructs | Wiki Page |
|---------|------------|------------|-----------|
| {concept} | {abstract theoretical definition} | {constructs} | [[concepts/{concept}]] |

## Methods
> **For analytical model papers: Create wiki/methods/{model}.md**
> Only for novel model contributions. Skip if standard model extension.

- **Model Name**: {name}
- **Key Innovation**: {what makes this model novel}
- **Assumptions**: {key assumptions}
- **Derivations**: {main mathematical derivations}
- → Create [[methods/{model_name}]] if novel

## Limitations
- {limitation 1: e.g., assumptions that may not hold empirically}
- {limitation 2}

## Related Papers
> **Include papers that adopt/extend this model.**

| Authors | Year | Title | Relevance | Wiki Link |
|---------|------|-------|-----------|-----------|
| {Author} | {YYYY} | {Title} | {adopts model / extends model / contrasts} | [[source/summary/{citekey}]] or [not in wiki] |