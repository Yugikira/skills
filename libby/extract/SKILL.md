---
name: libby-extract
description: Use when user needs citation metadata, BibTeX, citekeys, or mentions DOI/title/PDF extraction. Also trigger for keywords like 'bibtex', 'bibliography', 'citation', 'reference', 'organize papers', 'paper library', 'metadata from PDF' - even if user doesn't explicitly say 'extract'. Serpapi requires user confirmation before use.
---

# libby extract

Extract BibTeX/JSON metadata from DOI, title, or PDF.

## Quick Reference

| Input | Command |
|-------|---------|
| DOI | `libby extract 10.1234/abc --format json` |
| Title | `libby extract "paper title here"` |
| PDF | `libby extract paper.pdf` |
| PDF + DOI | `libby extract scanned.pdf --with-doi 10.1234/abc` |
| PDF + Title | `libby extract scanned.pdf --with-title "Title Here"` |
| Batch PDFs | `libby extract --batch-dir ./papers/` |

## Key Options

| Option | Purpose |
|--------|---------|
| `--format json` | Machine-readable output (default: bibtex) |
| `--ai-extract` | Use AI to extract DOI/title from PDF |
| `--with-doi DOI` | Provide DOI for scanned PDF |
| `--with-title TITLE` | Provide title for scanned PDF |
| `--batch-dir DIR` | Process all PDFs in directory |
| `--batch FILE` | File with `pdf|doi` or `pdf|title` pairs |
| `--copy` | Copy PDF instead of moving |
| `--fetch` | Also download PDF for DOI inputs |

## Serpapi Policy (Important)

**Serpapi uses API quota and costs money.**

Default `--serpapi deny` prevents accidental usage. Before using Serpapi:

1. **ALWAYS ask user for permission** first
2. Explain: "Serpapi may help find this paper, but uses API quota"
3. Only proceed with `--serpapi auto` or `--source serpapi` after user confirms

**Never auto-retry with Serpapi without user consent.**

## Source Cascade (Title Search)

Crossref → Semantic Scholar → Serpapi

Free sources (Crossref, S2) are tried first to avoid quota usage. Serpapi is last resort because it queries Google Scholar, which costs API credits.

## Output Structure

PDFs always stored to `~/.lib/papers/{citekey}/` (configured by `lib_dir`).

`--output FILE` only controls BibTeX/JSON file location, **not PDF directory**.

**To change PDF output location:**

| Method | How |
|--------|-----|
| Permanent | Edit `~/.libby/config.yaml`: set `lib_dir: /your/path` |
| Per command | Use `--config` with custom config file |
| After extract | Move with bash: `mv ~/.lib/papers/{citekey} /target/path` |

**Example workflow for custom output:**
```bash
# Extract DOI -> get metadata
libby extract 10.1234/abc --format json -o metadata.json

# PDF already in ~/.lib/papers/{citekey}/ - move if needed
mv ~/.lib/papers/{citekey} ~/my_project/papers/
```

## Batch Failure Handling

Failed tasks saved to `~/.lib/extract_task/failed_tasks.json`:

```json
[
  {
    "input": "scanned.pdf",
    "error": "Cannot extract DOI/title from PDF",
    "needs_serpapi": false
  },
  {
    "input": "obscure_title.pdf",
    "error": "Title not found in Crossref or S2",
    "needs_serpapi": true
  }
]
```

**Recovery steps:**

1. Check failed_tasks.json for each failure
2. Identify cause from `error` field
3. Retry individually with appropriate fix:

| Error Type | Recovery Command |
|------------|-----------------|
| Cannot extract DOI/title | `libby extract scanned.pdf --with-doi 10.xxx` or `--with-title "Title"` |
| needs_serpapi: true | **Ask user first**, then `--serpapi auto` or `--source serpapi` |
| Other errors | Check error message, may need manual intervention |

**Example batch recovery:**
```bash
# After batch fails, check log
cat ~/.lib/extract_task/failed_tasks.json

# Retry scanned PDF with manually provided DOI
libby extract scanned.pdf --with-doi 10.1234/example

# For needs_serpapi errors - ASK USER FIRST
# "Serpapi can help but uses API quota. Proceed?"
# After user confirms:
libby extract "Obscure Paper Title" --serpapi auto

# Or batch retry with pairs file (ask user about Serpapi)
libby extract --batch pairs.txt --serpapi auto
```

## Common Mistakes

| Issue | Fix |
|-------|-----|
| Scanned PDF fails | Use `--with-doi` or `--with-title` |
| Title not found | Ask user → confirm Serpapi → retry with `--serpapi` |
| Batch fails silently | Check `~/.lib/extract_task/failed_tasks.json` |
| Wrong citekey format | Edit `~/.libby/config.yaml` citekey section |
| Need different PDF location | Move after extract or edit lib_dir in config |
| `--output` doesn't affect PDF | Use bash mv or edit lib_dir in config |

