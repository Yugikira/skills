# Review Paper Extraction Guidance

This reference provides extraction guidance for review papers. Review papers consolidate existing knowledge about a concept—they focus on updating wiki pages rather than creating a full summary.

## Review Paper Recognition

Paper is a review if:
- Surveys existing literature on a specific concept
- Synthesizes findings across multiple papers
- No new empirical data collection
- No hypothesis testing with new data
- Title often includes "Review", "Survey" (as literature survey), "Overview"

## Review Paper Workflow

Review papers have a **different workflow** from archival/experimental/survey papers:

```
Review → Check concept wiki → Create/Update concept wiki → NO full summary creation
```

### Step 1: Check Concept Page Existence

1. Identify the **core concept** the review paper is about
2. Check if wiki page exists for the concept:

   **If IMA_AVAILABLE=true (from kb-skill pre-flight):**
   ```bash
   ima_api "openapi/wiki/v1/search_knowledge" '{"query": "{concept_name}", "knowledge_base_id": "concepts_kb_id", "cursor": ""}'
   ```
   - If `info_list` contains match → EXISTS
   - If `info_list` empty → NOT EXISTS

   **If IMA_AVAILABLE=false (file-based fallback):**
   ```bash
   Grep "{concept_name}" wiki/concepts/_index.md
   ```
   - If output contains `[[{concept_name}]]` → EXISTS
   - If no output → NOT EXISTS, proceed to create

   **Why Grep instead of Read**: For existence check, we only need to know if the specific concept is in the index. Grep returns only matching rows (0-1), while Read returns entire index (50+ entries).

### Step 2: Create Concept Page (If Not Exists)

If no wiki page for the concept:

1. Read `kb-wiki/templates/concept.md` template
2. Fill in with information from the review paper
3. Use **concise sentences** to conclude main points
4. Source papers: Record **oldest 2 and nearest 3** papers only

**We don't want wiki pages growing as long as review papers.** Instruct readers to read the review if they need more information.

### Step 3: Update Concept Page (If Exists)

If wiki page already exists for the concept:

1. Compare existing content with review paper information
2. Update with new information from review
3. Maintain concise style
4. Add review paper to source papers (oldest 2 + nearest 3)

## What NOT to Create

**ONLY create concept page for the main concept.**

Do NOT create:
- Multiple concept pages (only main concept)
- New variable pages (review papers don't introduce new measures)
- New method pages (review papers don't introduce new methods)
- Full paper summary (review is consolidation, not extraction)

## Cross-Linking from Review Paper

For variables/methods/related concepts/theories mentioned in review:

1. Check existing wiki pages for these items
2. If exists: Establish correct links in concept page
3. If not exists: **Do NOT create**—wait for empirical papers to define them

## Concept Page Content from Review

### Definition
- Synthesize definition from review
- Note if multiple definitions exist (alternative definitions section)

### Constructs & Variables
- List measures discussed in review
- Link to existing variable pages
- Do NOT create new variable pages

### Related Theories
- List theories discussed in review
- Link to existing theory pages

### Economic Consequences
- Synthesize consequences discussed in review
- Cite oldest 2 + nearest 3 papers

### Future Works
- Extract future research directions from review
- These guide future paper ingestion

## Source Papers Management

Wiki pages should remain concise. Source papers:

**Pattern**: Oldest 2 papers + Nearest 3 papers

**Example**:
| Source Papers | Year | Contribution |
|---------------|------|--------------|
| [[source/summary/first_paper]] | 1990 | First definition |
| [[source/summary/second_paper]] | 1995 | Alternative definition |
| [[source/summary/review_paper]] | 2024 | Comprehensive review |
| [[source/summary/near_paper_1]] | 2023 | Recent finding |
| [[source/summary/near_paper_2]] | 2022 | Recent extension |

**Why this pattern**: 
- Oldest papers establish concept origin
- Nearest papers show current state
- Review paper synthesizes all

## Review Paper Summary (Minimal)

Review papers do NOT use the full summary template.

Create a minimal reference file instead:

```markdown
---
title: "{Review Title}"
citekey: {citekey}
paper_type: review
target_concept: {concept name}
---

# {Review Title}

## Core Concept
{concept reviewed}

## Wiki Update Action
- [Concept page created] or [Concept page updated]

## Key Contributions
{2-3 sentences on what the review adds to existing knowledge}

## Related Papers (for wiki cross-linking)
{Papers mentioned in review that should be linked}
```

Store minimal summary in `source/summary/{citekey}_review.md`.

## When to Create Full Summary

**Exception**: If review paper introduces novel theoretical framework:

1. Create full summary using `paper_summary_analytical.md` template
2. Treat as analytical model paper (theoretical contribution)
3. This is rare—most reviews consolidate existing knowledge

## Integration with kb-ingest

When ingesting a review paper:

1. **Phase 3**: Skip standard extraction
2. Use this review extraction guidance
3. **Phase 4**: Focus on wiki consolidation quality check
4. No collision resolution needed (only updating one concept page)

## Related Skills

- **kb-consolidate**: Wiki page consolidation and merging. May be relevant if review reveals multiple similar concept pages.