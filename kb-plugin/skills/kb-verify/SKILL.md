---
name: kb-verify
description: Verify agent that checks ground truth findings for reproducibility. Called by kb-ingest during summary creation phase.
---

# kb-verify - Summary Verification

This skill is called by kb-ingest to verify the ground truth findings in a paper summary.

## Input

The orchestrator passes:
- Summary file path: `source/summary/{citekey}_summary.md`

## Verification Checklist

For each **Ground Truth finding**, check:

1. **Is this an objective statistical observation?**
   - Must have: coefficient, p-value, sample size (n)
   - Format: "Variable X has β=YYY (p<ZZ) in [model] (n=XXXX)"

2. **Are ALL variables defined with computational formulas?**
   - Each variable must have exact definition (not just name)
   - Can reference earlier finding or Measures table if defined there
   - No abstract concepts without operationalization

3. **Can a reader verify without external sources?**
   - All information needed to understand the result is in the summary
   - No assumed knowledge of paper context

## Output Format

**Simple YES/NO with one-sentence reason for failures only:**

```
Finding 1: YES
Finding 2: NO - uses abstract concept "competition" without computational definition
Finding 3: YES
Finding 4: NO - variable "MLCs" undefined, reader cannot verify without paper context
Finding 5: YES
```

**NO reasoning examples:**
- "NO - coefficient reported but no p-value"
- "NO - variable X mentioned but formula not provided"
- "NO - model type not specified"
- "NO - sample size missing"

## What NOT to Check

Do NOT check:
- Whether the finding is correct (that's the paper's job)
- Theoretical interpretation (that's Claimed Findings)
- Whether the hypothesis is valid
- Paper quality or methodology soundness

**Your job**: Ensure the finding is **reproducible** from the summary alone.

## Handling References

If Finding 2 says "Variable X (see Finding 1)" and Finding 1 fully defines Variable X:
- **YES** - reference is valid

If Finding 3 says "Variable Y (see Measures table)" and Measures table defines Variable Y:
- **YES** - reference is valid

If reference target is missing or incomplete:
- **NO** - referenced definition not found or incomplete

## Workflow

```
1. Read summary file
2. Focus on Ground Truth Findings section
3. Check each finding against verification criteria
4. Return simple YES/NO output
5. Orchestrator revises based on NO feedback
```

## Example

**Input summary excerpt:**
```
## Ground Truth Findings
- Finding 1: SameIndustry (1 if both firms in same 4-digit SIC code) has β=0.052 (p<0.01) in OLS regression (n=12,340)
- Finding 2: PeerGroupMatch (see Finding 1) has β=0.031 (p<0.05)
```

**Output:**
```
Finding 1: YES
Finding 2: NO - references Finding 1 for PeerGroupMatch, but Finding 1 only defines SameIndustry
```

## Token Efficiency

- Keep output minimal: YES/NO only
- One sentence for NO reasons
- No explanations for YES
- No suggestions for fixes (orchestrator handles revision)