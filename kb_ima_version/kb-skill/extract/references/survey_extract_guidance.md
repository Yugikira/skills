# Survey Paper Extraction Guidance

This reference provides detailed extraction guidance for survey research papers. Use this when processing papers that collect data through questionnaires (mail, telephone, e-mail, internet) or face-to-face interviews.

## Survey Paper Recognition

Paper is a survey if:
- Primary data collection via questionnaires or interviews
- No manipulation of variables (no treatment/control groups)
- Subjects/respondents report opinions, judgments, or knowledge
- Variables are responses to survey questions

## Survey vs Experimental

| Survey | Experimental |
|--------|--------------|
| No manipulation | Manipulated variables |
| Natural responses | Treatment/control groups |
| Opinions/judgments/knowledge | Observable behavior/outcomes |
| Random sampling (if possible) | Random assignment |
| External validity focus | Internal validity focus |

## Summary Requirements for Survey Papers

### Claim Findings: 3-5 Key Interpretations FIRST

Select the authors' **main interpretations** of survey results:
- What they conclude from the survey findings
- The story they tell about why results matter

**Write Claims BEFORE Ground Truth** - this establishes the interpretive framework first.

### Ground Truth Findings: 3-5 Key Findings SECOND

Select the **most objective** survey results:
- Primary question-based results (response patterns, percentages)
- Statistical analysis results (if regression/correlation conducted)
- Key dimensions with significant findings

**Correspondence Requirement**: The first N Ground Truth findings should directly support the N Claim findings above. Finding 1 supports Claim 1, Finding 2 supports Claim 2, etc.

DO NOT extract every finding. Quality over quantity.

## Ground Truth Format for Survey Papers

### Question-Based Results

For surveys with direct question results (most common):

```
The survey Question {Q1-Q3} (grouped as {dimension name}) shows that {percentage/response pattern} of respondents {result description}.
```

**Grouping rule**: If question text is too long (over 3 questions), group them with a short summary and indicate question numbers.

**Example**:
```
Finding 1: The survey Questions Q1-Q4 (grouped as "Budgetary Participation") shows that 65% of respondents report moderate participation in budget setting.
```

### Statistical Analysis Results

If survey conducts statistical analysis (regression, correlation):

Use archival ground truth format:
```
{Variable X} (defined as {formula}) has coefficient β=YYY (p<ZZ) in {model type} (n=XXXX).
```

## Concepts Extraction for Survey Papers

Survey concepts are **easier to extract** than archival papers:

**Where to find concepts**:
- **Research question**: Often directly stated
- **Title**: Paper title frequently indicates core concept
- **Introduction**: Concepts introduced with their importance

**Concept structure for surveys**:
- Each concept measured by **survey dimensions** (multiple questions)
- Dimension = grouping of related questions
- Record dimensions in Concepts table

## Variables Extraction for Survey Papers

### Survey Variables = Survey Questions

Survey variables differ from archival/experimental:
- **Archival/Experimental**: Variables = computational measures
- **Survey**: Variables = responses to questions (scalar/yes-no)

### Grouping Questions by Dimensions

One concept is typically measured by **several dimensions**, each dimension contains **multiple questions**.

**Grouping structure**:
```
Concept → Dimensions → Questions (grouped)
```

**Example**:
- Concept: "Budgetary Participation"
- Dimensions: Budget Setting, Budget Review
- Questions: Q1-Q3 (Budget Setting), Q4-Q5 (Budget Review)

**Key insight**: Questions are **GROUPED** by dimension. One variable wiki page = all questions measuring one dimension.

### Wiki Naming for Survey Variables

Survey wiki naming differs from archival/experimental:

| Category | Naming Rule | Marker |
|----------|-------------|--------|
| **Concepts** | Standard: `[[concepts/{concept}]]` | NO `_survey` |
| **Variables** | `{dimension}_survey` (grouped questions) | YES `_survey` |
| **Methods (instruments)** | `{instrument}_survey_instrument` | YES `_survey_instrument` |

**Variable naming**: One wiki page per dimension (NOT per individual question).

**Example**:
| Dimension | Concept | Questions Grouped | Wiki Page |
|-----------|---------|-------------------|-----------|
| Budget_Setting | Budgetary_Participation | Q1-Q3 | [[variables/Budget_Setting_survey]] |
| Budget_Review | Budgetary_Participation | Q4-Q5 | [[variables/Budget_Review_survey]] |

**Why grouped**: Multiple questions measuring same dimension share one wiki page. The wiki page summarizes what that dimension measures and lists the specific questions.

## Survey Design Extraction

### Survey Type
Identify delivery method:
- Mail survey
- Telephone survey
- E-mail survey
- Internet platform survey
- Face-to-face interview
- Custom type

### Respondent Target
Similar to experimental "subjects":
- Target population (managers, accountants, students, etc.)
- Sample size
- Sampling method (random, convenience, stratified)

### Response Categories
What does the survey ask for:
- **Opinions**: Subjective views (e.g., "I believe...")
- **Judgments**: Evaluations (e.g., "This is effective...")
- **Knowledge**: Factual recall (e.g., "What is...?")
- Custom categories

### Question Sequence
Order of questions:
- Easiest (shortest) to hardest
- Hardest to easiest
- Random order
- Logical flow (topic grouping)

### Survey Instrument

**Well-established instruments** (from previous research):
- Self-reported performance scales
- Budgetary participation instruments
- Tolerance of ambiguity scales
- etc.

**New instruments**:
- If paper develops new instrument
- Summarize validity testing (construct validity, content validity)
- **CREATE wiki/methods/{instrument}_survey_instrument.md**
- Wiki page marked as `_survey_instrument`

### Non-Response Handling
Extract how paper:
- Encourages response (incentives, reminders, etc.)
- Addresses non-response bias
- Calculates response rate

### Reliability Measures
Extract reliability testing:
- **Test-Retest reliability**: Same survey administered twice
- **Split-half reliability**: Correlation between halves of survey
- **Cronbach's Alpha**: Internal consistency
- Custom reliability measures

**Record coefficients**: Report actual reliability values (e.g., α = 0.85)

## Face-to-Face Interview Specifics

### Interview Type
Three types of interviews:
- **Structured Interview**: Fixed questions, fixed order
- **Semi-Structured Interview**: Core questions + flexible probing
- **Unstructured Interview**: Open-ended conversation

### Interviewee Selection
Extract:
- How interviewees chosen (random, purposive, convenience)
- Why chosen (expertise, position, experience)
- Selection acknowledgment in paper

## Hypothesis Extraction for Survey Papers

Survey papers CAN develop hypotheses when:
- Theory-driven causal predictions
- Testing relationships between concepts
- Brown (1995) emphasizes need for good theory to underpin causal relationships

### If Hypothesis Exists

Use archival guidance argument structure analysis:
1. Identify premises (supporting evidence for hypothesis)
2. Classify premise sources (literature, theory, assumption)
3. Determine reasoning approach (deductive/inductive)
4. Evaluate (sound/unsound/cogent/uncogent)

→ Refer to `archival_extract_guidance.md` for detailed argument structure analysis.

### If No Hypothesis
Write: "No explicit hypothesis stated in this paper. The survey is {descriptive study | exploratory study | knowledge assessment}."

## Survey Limitations

Common survey limitations to extract:
- **Internal validity**: Inability to assign subjects randomly, inability to rule out rival hypotheses
- **External validity**: Response bias, non-response bias, sample representativeness
- **Construct validity**: Question wording effects, social desirability bias
- **Reliability**: Measurement reliability concerns

## Wiki Pages for Survey Papers

### Concepts Wiki Pages
- Standard concept template
- Standard naming: `[[concepts/{concept}]]` (NO `_survey` marker)
- Include survey dimensions in "Constructs & Variables" section

### Variables Wiki Pages
- One wiki page per **dimension** (group of questions)
- Naming: `[[variables/{dimension}_survey]]`
- NOT per individual question (questions grouped by dimension)
- Wiki page summarizes what dimension measures, lists specific questions

### Methods Wiki Pages
- Only for **new survey instruments**
- Naming: `[[methods/{instrument}_survey_instrument]]`
- Skip standard instruments (existing validated scales)