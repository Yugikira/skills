# Experimental Paper Extraction Guidance

Brief guidance for manipulation handling in experimental paper extraction. Complements the main `kb-extract/SKILL.md`.

## Manipulations Section Extraction

The `## Manipulations` section in experimental summaries consolidates manipulation info across studies.

### Extraction Rules

1. **One row per manipulation method**
   - Same variable can have multiple manipulation methods within a paper
   - Example: "Appeal Type - Science Mention" vs "Appeal Type - Science Necessity Salience"

2. **Studies column format**: `Study {number} (n={size} {pool})`
   - Example: "Study 1a (n=511 students), Study 3a (n=809 MTurk)"
   - Group studies using the same manipulation method
   - Order by study number

3. **Paper Variable naming**: `{variable_name} - {Method descriptor}`
   - Clear distinction between different manipulation methods
   - Wiki Page links to same variable page (different methods documented in that page)

4. **DV handling**: 
   - For dependent variables, show `{measured}` in Manipulation column
   - Or skip the row if not manipulated (purely measured outcome)

### Example

| Paper Variable | Manipulation | Studies | Wiki Page |
|----------------|--------------|---------|-----------|
| Appeal Type - Science Mention | Adding/removing science language in slogan | Study 1a (n=511 students), Study 3b (n=809 MTurk) | [[variables/Appeal_Type_exp]] |
| Appeal Type - Science Salience | Article manipulation (chemistry vs seasonality) | Study 5a (n=814 MTurk) | [[variables/Appeal_Type_exp]] |
| Purchase Intentions | {measured} | All studies | [[variables/Purchase_Intentions_exp]] |

## Wiki Variable Page Accumulation

Experimental variable pages (`{variable}_exp.md`) support multi-paper accumulation.

### For Manipulated IV Table

| Paper | Manipulation Method | Treatment Levels | Manipulation Check | Control Condition | Validity |

**Selection rule**: 
- Keep **first + most recent from top journals** for similar manipulation strategy
- Different manipulation strategies get separate rows
- Do NOT update for papers with similar manipulation (just link summary in Papers Using table)

### For DV Table

| Paper | Measurement Method | Scale/Units | Collection Procedure | Validity |

**Selection rule**:
- Keep **first + most recent from top journals** for similar measurement approach

### Papers Using Table

Simple accumulation: `| Paper | Key Findings |`
- Link all papers using this variable
- No manipulation detail in this table (that's in Operationalization tables)