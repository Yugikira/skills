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
paper_type: experimental
---

# {Paper Title}

## One-Line Summary
{What the paper contributes in one sentence}

## Abstract Summary
{2-3 sentence paraphrase}

## Ground Theories
> **Experimental papers typically state grounding theories explicitly.**
> Link to the paper that first proposed the theory.

| Theory | Original Source | Key Propositions | Wiki Page |
|--------|-----------------|------------------|-----------|
| {theory name} | [[source/summary/{citekey_origin}]] | {brief proposition} | [[theories/{theory}]] |

## Hypothesis
> **Optional**: Only if the experiment develops its own hypothesis predicting manipulation effect.
> If testing pre-existing theory without new hypothesis: Write "No explicit hypothesis developed in this paper. The experiment tests pre-existing theory from [[theories/{theory}]]."

### Hypothesis Statement
{The experiment's hypothesis predicting how manipulated variable affects dependent variable}

### Argument Structure
> Premises intended to support the hypothesis.
> For detailed argument analysis, refer to `kb-extract/references/archival_extract_guidance.md`.

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
> **Problem statement + interpretation of experiment results.**
> This is NOT just findings interpretation - include the problem context.

- Claim 1: {problem context + main interpretation}
- Claim 2: {secondary interpretation}
- Claim 3: {third interpretation}

## Ground Truth Findings
> **Most objective results.**
> Format: "With subjects from {background}, participating in {study}. The manipulated variable {X} is {relationship} to dependent variable {Y}."

- Finding 1: With subjects from {brief subject background}, participating in {study name/design}. The manipulated variable {X} is positively/negatively related to the dependent variable {Y} (p<ZZ, n=XXXX).
- Finding 2: {additional finding}
- Finding 3: {additional finding}

## The Context
> **Context factors that affect external validity.**
> Summarize: task complexity, location, time constraints, incentives, subject pool.

| Context Factor | Value/Description | Threat to Validity |
|----------------|-------------------|-------------------|
| Task Complexity | {high/medium/low, description} | {how it may affect results} |
| Location | {lab/field/online} | {validity concern} |
| Time Constraints | {time limit if any} | {pressure effect} |
| Incentives | {payment scheme} | {motivation effect} |
| Subject Pool | {student/professional/...} | {generalizability concern} |

## Experimental Design
> **Categorize and document the design. Includes methodology.**

### Design Type
- [ ] Post-test only control group design
- [ ] Pre-test/post-test control group design
- [ ] Factorial design - between subjects
- [ ] Factorial design - within subjects (repeated measures)
- [ ] Others: {custom design description}

### Design Summary
{Brief summary of the study/studies design in 2-3 sentences}

### Control Group
{Is it a clean control group? All other conditions same except manipulated variable?}

### Randomisation
{How subjects assigned to treatments? Is distribution equal across conditions?}

### Counterbalancing
{For within-subjects designs: How order effects mitigated?}

### Procedure
{Experimental procedure: what subjects do, sequence of events, materials used}

### Data Sources
{If any additional data collected beyond experimental procedure}

## Concepts Defined
> **Concepts**: Abstract theoretical ideas (not directly observable).
> **Constructs**: Multi-item measures that operationalize concepts.

| Concept | Definition | Constructs | Wiki Page |
|---------|------------|------------|-----------|
| {concept} | {definition} | {constructs} | [[concepts/{concept}]] |

## Measures/Variables
> **Note**: Dependent and independent variables in experiments are often abstract concepts.
> **Paper Variable** = exact name from paper (use in Ground Truth findings)
> **Wiki Name** = common-sense name (only for directly measurable variables)

| Paper Variable | Wiki Name | Constructs | Concept | Computational Definition | Wiki Page |
|----------------|-----------|------------|---------|--------------------------|-----------|
| {paper_name} | {wiki_name} | {construct} | {concept} | {formula} | [[variables/{wiki_name}]] or [no wiki] |

## Limitations
- {limitation 1}
- {limitation 2}

## Related Papers
| Authors | Year | Title | Relevance | Wiki Link |
|---------|------|-------|-----------|-----------|
| {Author} | {YYYY} | {Title} | {why related} | [[source/summary/{citekey}]] or [not in wiki] |