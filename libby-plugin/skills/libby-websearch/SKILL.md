---
name: libby-websearch
description: Use when user needs literature search, academic papers by keywords, or mentions 'search papers', 'find articles', 'scholar', 'google scholar', 'semantic scholar', 'crossref', 'bibliography search', 'literature review'. Also trigger when user wants papers filtered by year/author/journal. Serpapi requires user confirmation before use.
---

# libby websearch

Search Crossref and Semantic Scholar (parallel), optionally Serpapi.

## Quick Reference

| Search | Command |
|--------|---------|
| Keywords | `libby websearch "machine learning"` |
| Year range | `libby websearch "AI" --year-from 2023 --year-to 2025` |
| Author | `libby websearch "governance" --author Smith` |
| Venue | `libby websearch "policy" --venue Nature` |
| JSON output | `libby websearch "quantum" --format json -o results.json` |
| Single source | `libby websearch "AI" --source s2` |
| No auto-save | `libby websearch "AI" --no-save` |

## Key Options

| Option | Purpose |
|--------|---------|
| `--year-from N` | Start year (default: current - 2) |
| `--year-to N` | End year |
| `--author NAME` | Author filter |
| `--venue NAME` | Journal/conference filter |
| `--issn ISSN` | ISSN filter |
| `--limit N` | Results per source (default: 50) |
| `--source NAME` | Single source: crossref, s2, serpapi |
| `--format json/bibtex` | Output format (default: bibtex) |
| `--output FILE` | Output file path |
| `--no-save` | Skip auto-save to file |
| `--serpapi deny|ask|auto` | Serpapi policy (default: deny) |

## Special Behavior

- DOI input triggers **fetch → extract** workflow instead of search
- Parallel execution: Crossref + S2 simultaneously
- Serpapi optional (uses quota)

## Serpapi Policy (Important)

**Serpapi uses API quota and costs money.**

Default `--serpapi deny` prevents accidental usage. Before using Serpapi:

1. **ALWAYS ask user for permission** first
2. Explain: "Serpapi may find more results, but uses API quota"
3. Only proceed with `--serpapi auto` or `--source serpapi` after user confirms

**Never auto-enable Serpapi without user consent.**

## Default Output

```
~/.lib/search_results/yymmdd_{keywords}.bib
```

Use `--output FILE` to specify custom location. Use `--no-save` to skip file output.

## Follow-up Workflow

Search results can feed into fetch/extract:

```bash
# Search → get DOI → fetch PDF
libby websearch "topic" --format json --no-save
# Then: libby fetch {doi_from_result}

# Search → save → use in paper
libby websearch "topic" -o results.bib
# Then import results.bib into reference manager
```

## Common Mistakes

| Issue | Fix |
|-------|-----|
| No results found | Try broader keywords; ask user about Serpapi |
| Too many results | Use `--year-from/--year-to` or `--venue` to narrow |
| Missing recent papers | Default year_from is 2 years back; set explicitly |
| Venue filter too strict | Use `--issn` for exact match, or relax venue |
| Need Serpapi results | **Ask user first** → confirm → use `--serpapi auto` |
| DOI input unexpected | DOIs trigger fetch workflow, not search |
| Want to fetch found papers | Use JSON output, extract DOI, then `libby fetch` |

