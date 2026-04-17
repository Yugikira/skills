---
name: libby-fetch
description: Use when user needs to download academic PDFs, retrieve full-text papers, or mentions DOI with PDF request. Also trigger for 'download paper', 'get PDF', 'fetch article', 'full text', 'open access', 'paper library' - even if user doesn't explicitly say 'fetch'. Serpapi requires user confirmation before use.
---

# libby fetch

Download PDF by DOI with source cascade fallback.

## Quick Reference

| Input | Command |
|-------|---------|
| Single DOI | `libby fetch 10.1234/abc` |
| Batch DOIs | `libby fetch --batch dois.txt` |
| Pipeline | `cat dois.txt | libby fetch` |
| Check URL only | `libby fetch 10.1234/abc --dry-run` |
| Specific source | `libby fetch 10.1234/abc --source unpaywall` |

## Source Cascade

Order: **Crossref OA → Unpaywall → S2 → CORE → arXiv → PMC → bioRxiv → Sci-hub → Serpapi**

The cascade tries free/open sources first, then fallbacks. Serpapi is last because it costs quota.

| Source | Why use it |
|--------|------------|
| unpaywall | OA versions from publishers, requires EMAIL config |
| core | Institutional repositories worldwide, often has blocked papers |
| scihub | Shadow library, Selenium handles CAPTCHA/blocking |
| serpapi | Google Scholar search, uses quota, last resort |

## Serpapi Policy (Important)

**Serpapi uses API quota and costs money.**

Default `--serpapi deny` prevents accidental usage. Before using Serpapi:

1. **ALWAYS ask user for permission** first
2. Explain: "Serpapi may help find this PDF, but uses API quota"
3. Only proceed with `--serpapi auto` or `--source serpapi` after user confirms

**Never auto-retry with Serpapi without user consent.**

## Key Options

| Option | Purpose |
|--------|---------|
| `--dry-run` | Show PDF URL without downloading |
| `--source NAME` | Use single source only (skip cascade) |
| `--no-scihub` | Skip Sci-hub source |
| `--serpapi deny|ask|auto` | Serpapi usage policy (default: deny) |
| `--batch FILE` | File with DOIs (one per line) |
| `--output DIR` | Override papers directory |

## Output Structure

```
~/.lib/papers/{citekey}/{citekey}.pdf
~/.lib/papers/{citekey}/{citekey}.bib
```

Use `--output DIR` to override papers directory (unlike extract, fetch can directly specify output location).

On failure: `{citekey}_attempts.json` logs tried sources.

## Batch Failure Handling

Each failed DOI creates `{citekey}_attempts.json` in its directory:

```json
{
  "doi": "10.1234/abc",
  "citekey": "smith_2024_example",
  "attempts": [
    {"source": "unpaywall", "url": "https://...", "error": "403 Forbidden"},
    {"source": "core", "url": null, "error": "Not found"},
    {"source": "scihub", "url": "https://sci-hub.se/...", "error": "CAPTCHA"}
  ],
  "found_urls": [{"source": "unpaywall", "url": "https://..."}]
}
```

**Recovery steps:**

1. Check each `{citekey}_attempts.json` for failure details
2. Identify which sources found URLs but failed to download
3. Retry with specific source or alternative approach:

| Error Pattern | Recovery Approach |
|---------------|-------------------|
| URL found, 403 blocked | Try `--source core` or `--source scihub` |
| Sci-hub CAPTCHA | Ensure Chrome installed, retry manually |
| No URLs found | Paper may not be available OA; ask user about Serpapi |
| needs_serpapi | **Ask user first**, confirm → retry with `--serpapi auto` |

**Example recovery workflow:**
```bash
# After batch fails, check attempt logs
ls ~/.lib/papers/*/_attempts.json

# View specific failure details
cat ~/.lib/papers/smith_2024_example/smith_2024_example_attempts.json

# Retry with different source (URL was found but blocked)
libby fetch 10.1234/abc --source core

# If no URLs found, ask user about Serpapi
# "PDF not found in free sources. Serpapi may help but uses quota. Try Serpapi?"
# After user confirms:
libby fetch 10.1234/abc --serpapi auto
```

## Common Mistakes

| Issue | Fix |
|-------|-----|
| All sources fail | Check `{citekey}_attempts.json` for found URLs |
| URL found but blocked | Try `--source core` or `--source scihub` |
| Sci-hub CAPTCHA | Ensure Chrome browser available |
| No URLs in attempts | Paper may not be OA; ask user about Serpapi |
| Batch partial failure | BibTeX saved anyway; check each `_attempts.json` |
| Need Serpapi fallback | **Ask user first** → confirm → retry with `--serpapi auto` |
| Want different output | Use `--output DIR` (works directly, unlike extract) |

