---
name: kb-lint
description: Health check for the Knowledge Base wiki. Finds broken wikilinks, orphan pages, missing cross-references, stale claims, and contradictions.
---

# kb-lint - Wiki Health Check

Run periodic health checks on the Knowledge Base wiki.

## Usage Patterns

- `/kb-lint` - Full health check (all checks)
- `/kb-lint --quick` - Quick check (wikilinks and orphans only)
- `/kb-lint --contradictions` - Focus on finding contradictions

## Check Types

### Check 1: Broken Wikilinks

Run: `python Scripts/check_wikilinks.py`

Scans all [[link]] references and verifies target files exist.

**Fix approach:**
- If target should exist: Create missing page
- If link is wrong: Update link to correct target
- If target removed: Remove the wikilink

### Check 2: Orphan Pages

Run: `python Scripts/list_orphans.py --verbose`

Finds wiki pages not referenced in any `_index.md`.

**Fix approach:**
- Add [[page]] to appropriate `_index.md`
- If page is duplicate/outdated: Delete or merge

### Check 3: Missing Cross-References

Scan paper summaries for concepts that have no wiki page.

Process:
1. Grep all `[[concepts/{name}]]` in `source/summary/*.md`
2. Check each concept has `wiki/concepts/{name}.md`
3. Report missing wiki pages

### Check 4: Stale Claims

Find paper summaries not updated in 6+ months.

Process:
1. Read YAML frontmatter `processed: {date}` from summaries
2. Calculate age from current date
3. Flag papers older than 6 months

### Check 5: Contradictions (--contradictions focus)

Find conflicting interpretations across papers using the same proxy.

Process:
1. Read all proxy pages in `wiki/proxies/`
2. For each proxy, examine Interpretations section
3. Look for conflicting claims about what the proxy measures

### Check 6: Unpopularized Ground Truth

Find ground truth findings without interpretations.

Process:
1. Scan `source/summary/*.md` for Ground Truth Findings
2. Check if Other Interpretations section is empty
3. Flag for review

## Full Check Output Format

```markdown
# Lint Report - {YYYY-MM-DD}

## Summary
- Broken wikilinks: {n}
- Orphan pages: {n}
- Missing cross-references: {n}
- Stale claims: {n}
- Contradictions flagged: {n}
- Unpopularized ground truth: {n}

[Details for each check]

## Suggested Actions
1. Create wiki/concepts/undefined_concept.md
2. Add orphan to _index.md
3. Review proxy for interpretation conflicts
```

## Post-Lint Actions

1. Fix broken wikilinks and orphan pages immediately
2. Schedule stale claims and contradictions for review
3. Log the lint in `wiki/log.md`

## Python Script Dependencies

- `Scripts/check_wikilinks.py`
- `Scripts/list_orphans.py`

## Recommended Schedule

- Quick lint: After each kb-ingest
- Full lint: Weekly or after batch ingestion
- Contradictions check: Monthly or before major synthesis
