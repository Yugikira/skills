# Object

This `kb_ima_version` project is to transfer the `../kb-plugin` into a standard nested skill (`kb-skill`) and incorporate the ima skill into several processes with ima-skill, especially the knowledge base skill.

# Preparation

- Always read the Progress.md before you start any task, if the task is not in Progress.md, add it.

    - If the new task is a follow-up task from previous task list, append it to the end.

    - If the new task is with higher priority, insert it before the current un-finished task.

    - If the new task would require a revision of finished tasks, restructure the Prgoress.md

# kb-skill Structure Reference

The kb-skill follows the ima-skill nested pattern. Reference this instead of reading ima-skill/SKILL.md repeatedly.

## Module Decision Table

| User Intent | Module | Read |
|-------------|--------|------|
| Ingest paper by DOI, title, or citekey | ingest | `kb-skill/ingest/SKILL.md` |
| Query the knowledge base, find papers, deep dive on concept | query | `kb-skill/query/SKILL.md` |
| Health check wiki - broken wikilinks, orphan pages | lint | `kb-skill/lint/SKILL.md` |
| Consolidate wiki pages - merge similar, fix structure | consolidate | `kb-skill/consolidate/SKILL.md` |
| Verify summary ground truth findings (internal) | verify | `kb-skill/verify/SKILL.md` |
| Extraction guidance (internal, called by ingest subagent) | extract | `kb-skill/extract/SKILL.md` |
| Wiki creation/update guidance (internal, called by ingest) | wiki | `kb-skill/wiki/SKILL.md` |

## Key Files

- `kb-skill/SKILL.md` - Root dispatcher with decision table
- `kb-skill/meta.json` - Version and dependencies (Python 3.8+)
- `kb-skill/scripts/` - Python utility scripts
- `kb-skill/templates/` - Wiki page templates

## Domain Scope

Primary: **economics, finance, accounting, management science, marketing**
Related: econometrics, behavioral economics, financial mathematics, accounting regulation, organizational behavior, consumer behavior, strategic management

The skill now supports multiple research methodologies:
- **Archival/empirical** - Existing data, observational studies (economics, finance, accounting)
- **Experimental** - Manipulated variables, treatment/control (behavioral economics, marketing, organizational behavior)
- **Survey** - Questionnaires, interviews (management, marketing, organizational research)
- **Analytical** - Mathematical models, proofs (financial mathematics, economic theory)
- **Review** - Literature synthesis (all domains)

# Constraints

- **ONLY** use standard libraries with `python` scripts.

- Write a test for the scripts before you write python scripts.

- The `ima-skill` could not work in this PC, ignore the testing of its functionality.

# Others

- **DO NOT** test the skills, ask the user to test for you.