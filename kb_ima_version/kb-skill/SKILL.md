---
name: kb-skill
description: |
  Unified Knowledge Base skill for academic paper management. Use when user mentions
  "ingest paper", "extract concepts", "create wiki", "query knowledge base", "kb-consolidate",
  "kb-lint", "kb-verify", or asks about concepts, theories, variables, methods from papers.
homepage: https://github.com/anthropics/claude-code
metadata:
  openclaw:
    emoji: 📚
---

# kb-skill - Knowledge Base Management

Unified skill for managing academic paper knowledge bases. Currently supports: **ingest**, **query**, **lint**, **consolidate**, **verify**, plus internal helpers **extract** and **wiki**.

## Module Decision Table

| User Intent | Module | Read |
|-------------|--------|------|
| Ingest paper by DOI, title, or citekey | ingest | `ingest/SKILL.md` |
| Query the knowledge base, find papers, deep dive on concept | query | `query/SKILL.md` |
| Health check wiki - broken wikilinks, orphan pages | lint | `lint/SKILL.md` |
| Consolidate wiki pages - merge similar, fix structure | consolidate | `consolidate/SKILL.md` |
| Verify summary ground truth findings (internal) | verify | `verify/SKILL.md` |
| Extraction guidance (internal, called by ingest subagent) | extract | `extract/SKILL.md` |
| Wiki creation/update guidance (internal, called by ingest) | wiki | `wiki/SKILL.md` |

## Domain Scope

Primary domains: **economics, finance, accounting, management science, marketing**
Related fields: econometrics, behavioral economics, financial mathematics, accounting regulation, organizational behavior, consumer behavior, strategic management

### Supported Research Methodologies

| Methodology | Typical Domains | Template |
|-------------|-----------------|----------|
| **Archival/Empirical** | Economics, finance, accounting | `paper_summary_archival.md` |
| **Experimental** | Behavioral economics, marketing, organizational behavior | `paper_summary_experimental.md` |
| **Survey** | Management science, marketing, organizational research | `paper_summary_survey.md` |
| **Analytical** | Financial mathematics, economic theory, accounting theory | `paper_summary_analytical.md` |
| **Review** | All domains | Minimal summary (wiki consolidation) |

Papers outside these domains will prompt for user confirmation.

## Structure

Each module contains its own resources:

| Module | Contains |
|--------|----------|
| `ingest/` | scripts/ (collision, linker, index), templates/ (paper_summary) |
| `wiki/` | templates/ (concept, variable, method, theory, construct) |
| `lint/` | scripts/ (wikilinks, orphans) |
| `extract/` | SKILL.md only |
| `consolidate/` | SKILL.md only |
| `query/` | SKILL.md only |
| `verify/` | SKILL.md only |

## Dependency Check

Requires Python 3.8+. Verify before use:
```bash
python --version
```

## IMA Knowledge Base Integration

This skill uses **ima-skill** for semantic search. Before searching wiki content, verify the required IMA knowledge bases exist.

### Required Knowledge Bases

| KB Name | Maps To | Purpose |
|---------|---------|---------|
| `summary` | `source/summary/` | Paper summaries |
| `conversation` | `source/conversation/` | Q&A records |
| `concepts` | `wiki/concepts/` | Concept definitions |
| `variables` | `wiki/variables/` | Variable definitions |
| `methods` | `wiki/methods/` | Method descriptions |
| `constructs` | `wiki/constructs/` | Model constructs |
| `theories` | `wiki/theories/` | Theory frameworks |
| `Archived` | — | Archive old versions before update (required for auto-sync) |

### KB Directory Check

Run before any ima search operation:
```bash
# Invoke ima-skill to list all knowledge bases
# Use search_knowledge_base with empty query to get all KBs
ima_api "openapi/wiki/v1/search_knowledge_base" '{"query": "", "cursor": "", "limit": 20}'
```

Check returned KB names against required list. If missing:
1. **ima-skill does NOT provide KB creation** - users must create KBs manually in IMA desktop client
2. Guide user: "请在IMA桌面客户端创建知识库: {missing_kb_name}"
3. After KB created, upload corresponding files (markdown) to that KB

### When KBs Not Available

If IMA KBs are not set up, fall back to file-based search:
- `Glob wiki/{category}/*.md` to list existing pages
- `Read wiki/{category}/{name}.md` to compare definitions

This fallback is slower but ensures functionality without IMA.

## Key Workflows

### Paper Ingestion Pipeline

When user wants to add a paper to the knowledge base:

1. Read `ingest/SKILL.md` for full pipeline
2. Pipeline phases: Acquisition → Conversion → Extraction → Review → Index Update
3. Uses `extract/SKILL.md` and `wiki/SKILL.md` as internal helpers

### Wiki Quality Maintenance

When user wants to check or clean the wiki:

- `/kb-lint` → Read `lint/SKILL.md` - broken wikilinks, orphan pages
- `/kb-consolidate` → Read `consolidate/SKILL.md` - merge similar, fix structure

### Knowledge Query

When user asks a question about the knowledge base:

- `/kb-query "{question}"` → Read `query/SKILL.md`

## Cross-Module Tasks

Certain tasks require reading multiple modules:

| User Request | Actual Flow | Read Order |
|--------------|-------------|------------|
| Ingest paper | ingest orchestrates → extract/wiki helpers | `ingest/SKILL.md` first |
| Fix wiki after ingest | lint → consolidate | `lint/SKILL.md` → `consolidate/SKILL.md` |

## Module Resources

Scripts and templates are located inside each sub-skill:

### ingest/
- scripts/: `check_new_page_collision.py`, `check_related_papers.py`, `update_indexes.py`

### extract/
- templates/: `paper_summary.md`

### wiki/
- scripts/: `check_wiki_collision.py`
- templates/: `concept.md`, `construct.md`, `theory.md`, `variable.md`, `variable_survey.md`, `method.md`, `method_analytical.md`, `method_experimental.md`, `method_survey_instrument.md`

### lint/
- scripts/: `check_wikilinks.py`, `list_orphans.py`

## Important Notes

- Internal helpers (extract, wiki, verify) are NOT invoked directly by users
- Skills assume working directory is wiki root (contains `source/`, `wiki/`, `raw/`)
- Run scripts as `python scripts/*.py` from within each sub-skill context
