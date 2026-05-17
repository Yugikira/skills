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
paper_type: survey
---

# {Paper Title}

## One-Line Summary
{What the survey contributes in one sentence}

## Abstract Summary
{2-3 sentence paraphrase}

## Hypothesis
> **Optional**: Only if the survey develops theoretical hypotheses.
> Survey hypotheses require good theory to underpin causal relationships (Brown 1995).
> If no hypothesis: Write "No explicit hypothesis stated in this paper."

### Hypothesis Statement
{The survey's hypothesis or research question}

### Argument Structure
> Premises intended to support the hypothesis.

| Premise | Source | Type |
|---------|--------|------|
| {Premise 1} | {Literature/Theory} | {Assumption/Observation} |

### Reasoning Approach
- **Type**: [Deductive | Inductive]
- **Relation**: [Valid | Strong]

### Evaluation
- **Status**: [Sound | Unsound | Cogent | Uncogent]
- **Reason**: {why this evaluation}

## Claim Findings
> **3-5 KEY INTERPRETATIONS** - Authors' main interpretations of survey results.
>
> **Important**: Claims should correspond to Ground Truth findings below. Claim N should be supported by Ground Truth Finding N.

- Claim 1: {primary interpretation}
- Claim 2: {secondary interpretation}
- Claim 3: {third interpretation}

## Ground Truth Findings
> **3-5 KEY FINDINGS ONLY** - Most objective results from survey.
>
> **Correspondence**: The first N findings here should directly support the N claims above.

### Question-Based Results
{For surveys with direct question results}

- Finding 1: The survey Question {Q1-Q3} (grouped as {dimension name}) shows that {percentage/response pattern} of respondents {result description}.
- Finding 2: The survey Question {Q4-Q5} (grouped as {dimension name}) shows that {result description}.

### Statistical Analysis Results
{If survey conducts statistical analysis, describe as archival ground truth format}

- Finding 3: {Variable X} (defined as {formula}) has coefficient β=YYY (p<ZZ) in {model type} (n=XXXX).

## Concepts Defined
> **Survey concepts are easier to extract.**
> Often found in: research question, title, introduction.

| Concept | Definition | Survey Dimensions | Wiki Page |
|---------|------------|-------------------|-----------|
| {concept} | {definition} | {dimensions/questions measuring it} | [[concepts/{concept}]] |

## Measures/Variables
> **Survey variables = questions grouped by dimension.**
> One concept measured by several dimensions (groups of questions).
> One wiki page per dimension (NOT per individual question), marked `_survey`.
> Concepts follow standard naming (no `_survey` marker).

| Dimension | Concept | Questions Grouped | Response Type | Wiki Page |
|-----------|---------|--------------------|---------------|-----------|
| {dimension_name} | {concept} | Q1-Q3: {brief question summary} | {scalar/yes-no} | [[variables/{dimension}_survey]] |
| {dimension_name2} | {concept} | Q4-Q5: {brief question summary} | {scalar/yes-no} | [[variables/{dimension2}_survey]] |

**Wiki naming**:
- Concepts: Standard `[[concepts/{concept}]]` (no `_survey`)
- Variables: `{dimension}_survey` (grouped questions per dimension)

## Survey Design
> **Design details for non face-to-face surveys.**

### Survey Type
- [ ] Mail survey
- [ ] Telephone survey
- [ ] E-mail survey
- [ ] Internet platform survey
- [ ] Others: {custom type}

### Respondent Target
{Target population description, similar to experimental subjects}

### Response Categories
{What does the survey ask for?}
- [ ] Opinions
- [ ] Judgements
- [ ] Knowledge
- [ ] Others: {custom category}

### Question Sequence
{Order of questions: easiest to hardest, hardest to easiest, random, or logical flow}

### Survey Instrument
{Basic survey instrument used}
- **Instrument Type**: {self-reported performance, budgetary participation, tolerance of ambiguity, etc.}
- **Source**: {well-established instrument from previous research OR new instrument}
- If new instrument: Briefly summarize validity testing → Create [[methods/{instrument}_survey_instrument]]

### Non-Response Handling
{What does the paper do to encourage response? How does it address non-response issue?}

### Reliability Measures
{How does the paper address reliability?}
- [ ] Test-Retest reliability
- [ ] Split-half reliability coefficient
- [ ] Cronbach's Alpha Coefficient
- [ ] Others: {custom measure}
- **Values**: {report reliability coefficients}

## Face-to-Face Interview Details
> **Additional details for face-to-face interview surveys.**

### Interview Type
- [ ] Structured Interview
- [ ] Semi-Structured Interview
- [ ] Unstructured Interview

### Interviewee Selection
{How and why interviewees chosen to participate}

## Limitations
- {limitation 1: inability to assign subjects randomly, inability to rule out rival hypotheses}
- {limitation 2}

## Related Papers
| Authors | Year | Title | Relevance | Wiki Link |
|---------|------|-------|-----------|-----------|
| {Author} | {YYYY} | {Title} | {why related} | [[source/summary/{citekey}]] or [not in wiki] |