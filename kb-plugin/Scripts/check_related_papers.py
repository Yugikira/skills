#!/usr/bin/env python3
"""
Check if related papers are in wiki database and suggest links.

Usage:
    python Scripts/check_related_papers.py --summary source/summary/{citekey}_summary.md
    python Scripts/check_related_papers.py --summary source/summary/{citekey}_summary.md --update

This script:
    - Reads Related Papers table from summary (extracts Title column)
    - Scans all summaries in source/summary/ directory
    - Matches titles against frontmatter 'title' field (normalized comparison)
    - Returns wiki link if found, [not in wiki] otherwise
    - With --update flag: modifies the summary file to fill Wiki Link column

Matching strategy: Title-based (not citekey) because citekey formats vary.
"""

import os
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
SUMMARY_DIR = ROOT_DIR / "source" / "summary"


def normalize_title(title: str) -> str:
    """
    Normalize title for comparison.
    - Lowercase
    - Remove punctuation (except apostrophes in names)
    - Strip extra whitespace
    """
    # Lowercase
    title = title.lower()
    # Remove punctuation (keep apostrophes for names like "Oyer's")
    title = re.sub(r"[^\w\s']", "", title)
    # Normalize whitespace
    title = " ".join(title.split())
    return title


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}

    # Find the closing ---
    end_match = re.search(r"\n---\n", content[3:])
    if not end_match:
        return {}

    frontmatter_text = content[3:end_match.start() + 3]
    metadata = {}

    for line in frontmatter_text.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            # Handle list values like [item1, item2]
            if value.startswith("["):
                value = [v.strip().strip('"').strip("'")
                         for v in value[1:-1].split(",") if v.strip()]
            elif value.startswith('"') or value.startswith("'"):
                value = value[1:-1]
            metadata[key] = value

    return metadata


def build_title_index() -> dict:
    """
    Build index of all titles in wiki database.
    Returns: {normalized_title: citekey}
    """
    title_index = {}

    if not SUMMARY_DIR.exists():
        return title_index

    for summary_file in SUMMARY_DIR.glob("*_summary.md"):
        try:
            content = summary_file.read_text(encoding="utf-8")
            frontmatter = parse_frontmatter(content)

            if "title" in frontmatter:
                title = frontmatter["title"]
                normalized = normalize_title(title)
                # Extract citekey from filename: {citekey}_summary.md
                citekey = summary_file.stem.replace("_summary", "")
                title_index[normalized] = citekey

        except Exception as e:
            print(f"Warning: Could not read {summary_file}: {e}")

    return title_index


def extract_related_papers_table(content: str) -> list:
    """
    Extract Related Papers table from summary content.
    Returns list of dicts with: authors, year, title, relevance, wiki_link (original)
    """
    # Find the Related Papers section
    related_match = re.search(r"## Related Papers\n", content)
    if not related_match:
        return []

    # Extract table after the section
    table_start = related_match.end()
    table_content = content[table_start:]

    # Find table rows (lines starting with | after header)
    rows = []
    in_table = False
    header_found = False

    for line in table_content.split("\n"):
        if line.startswith("|") and not line.startswith("| >"):
            in_table = True
            if not header_found:
                # Skip header row and separator row
                header_found = True
                continue
            if re.match(r"\|[\s-]+\|", line):
                # Skip separator row
                continue

            # Parse row: | Authors | Year | Title | Relevance | Wiki Link |
            parts = [p.strip() for p in line.split("|")]
            # parts[0] is empty (before first |), parts[-1] is empty (after last |)
            if len(parts) >= 6:
                row = {
                    "authors": parts[1],
                    "year": parts[2],
                    "title": parts[3],
                    "relevance": parts[4],
                    "wiki_link": parts[5] if len(parts) > 5 else ""
                }
                rows.append(row)
        elif in_table and not line.startswith("|"):
            # End of table
            break

    return rows


def check_related_papers(summary_path: Path, title_index: dict) -> list:
    """
    Check each related paper against wiki database.
    Returns list of dicts with: original_row, matched_citekey, wiki_link
    """
    try:
        content = summary_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error: Could not read {summary_path}: {e}")
        return []

    rows = extract_related_papers_table(content)

    results = []
    for row in rows:
        title = row["title"]
        normalized = normalize_title(title)

        matched_citekey = None
        wiki_link = "[not in wiki]"

        # Try exact match first
        if normalized in title_index:
            matched_citekey = title_index[normalized]
            wiki_link = f"[[source/summary/{matched_citekey}_summary]]"
        else:
            # Try partial match (title might be truncated or slightly different)
            for indexed_title, citekey in title_index.items():
                if normalized in indexed_title or indexed_title in normalized:
                    matched_citekey = citekey
                    wiki_link = f"[[source/summary/{matched_citekey}_summary]]"
                    break

        results.append({
            "original_row": row,
            "matched_citekey": matched_citekey,
            "wiki_link": wiki_link
        })

    return results


def update_summary_wiki_links(summary_path: Path, results: list) -> None:
    """
    Update the Wiki Link column in the summary file.
    """
    try:
        content = summary_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error: Could not read {summary_path}: {e}")
        return

    # Find and replace each row's Wiki Link
    for result in results:
        row = result["original_row"]
        new_link = result["wiki_link"]

        # Build the old row pattern
        old_row = f"| {row['authors']} | {row['year']} | {row['title']} | {row['relevance']} | {row['wiki_link']} |"

        # Build the new row
        new_row = f"| {row['authors']} | {row['year']} | {row['title']} | {row['relevance']} | {new_link} |"

        content = content.replace(old_row, new_row)

    # Write back
    summary_path.write_text(content, encoding="utf-8")
    print(f"Updated: {summary_path}")


def main():
    summary_file = None
    update_mode = False

    for arg in sys.argv:
        if arg.startswith("--summary="):
            summary_file = arg.split("=", 1)[1]
        elif arg == "--summary" and len(sys.argv) > sys.argv.index(arg) + 1:
            summary_file = sys.argv[sys.argv.index(arg) + 1]
        elif arg == "--update":
            update_mode = True

    if not summary_file:
        print("Usage: python Scripts/check_related_papers.py --summary {summary_file} [--update]")
        print("Example: python Scripts/check_related_papers.py --summary source/summary/gao_2026_summary.md --update")
        sys.exit(1)

    summary_path = Path(summary_file)
    if not summary_path.exists():
        summary_path = ROOT_DIR / summary_file
        if not summary_path.exists():
            print(f"Error: Summary file not found: {summary_file}")
            sys.exit(1)

    # Build title index from all summaries
    print("Building title index from wiki database...")
    title_index = build_title_index()
    print(f"Found {len(title_index)} papers in wiki")

    # Check related papers
    print(f"\nChecking Related Papers in: {summary_path}")
    results = check_related_papers(summary_path, title_index)

    # Output results
    print("\n## Results")
    print("| Authors | Year | Title | Wiki Link |")
    print("|---------|------|-------|-----------|")

    matched_count = 0
    for result in results:
        row = result["original_row"]
        wiki_link = result["wiki_link"]
        matched = result["matched_citekey"]

        print(f"| {row['authors']} | {row['year']} | {row['title']} | {wiki_link} |")

        if matched:
            matched_count += 1

    print(f"\nMatched: {matched_count}/{len(results)} papers found in wiki")

    # Update if requested
    if update_mode and matched_count > 0:
        print("\nUpdating summary file...")
        update_summary_wiki_links(summary_path, results)


if __name__ == "__main__":
    main()
