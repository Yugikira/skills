#!/usr/bin/env python3
"""
Check proposed wiki entries against existing entries for potential duplicates.

Usage:
    python Scripts/check_wiki_collision.py --summary source/summary/{citekey}_summary.md

This script:
    - Reads Concepts Defined and Measures/Variables tables from summary
    - Scans wiki/_index.md files in each category (concepts, variables, constructs, methods, theories)
    - Matches proposed entries against existing entries (normalized comparison)
    - Returns JSON collision report for each proposed entry

Output JSON:
{
    "concepts": [{"proposed": "...", "candidates": [...]}],
    "variables": [{"proposed": "...", "candidates": [...]}],
    "constructs": [...],
    "methods": [...],
    "theories": [...]
}

Matching strategy: Name-based (normalized) + definition keyword overlap scoring.
"""

import os
import re
import sys
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent.parent
WIKI_DIR = ROOT_DIR / "wiki"

CATEGORIES = ["concepts", "variables", "constructs", "methods", "theories"]


def normalize_name(name: str) -> str:
    """
    Normalize wiki name for comparison.
    - Lowercase
    - Remove punctuation
    - Replace underscores/hyphens with spaces
    - Strip extra whitespace
    """
    # Lowercase
    name = name.lower()
    # Remove wikilink syntax if present
    name = re.sub(r"\[\[.*?\/", "", name)  # Remove [[category/
    name = re.sub(r"\]\]", "", name)  # Remove ]]
    # Replace underscores and hyphens with spaces
    name = name.replace("_", " ").replace("-", " ")
    # Remove remaining punctuation (keep apostrophes)
    name = re.sub(r"[^\w\s']", "", name)
    # Normalize whitespace
    name = " ".join(name.split())
    return name


def parse_index_md(category: str) -> list:
    """
    Parse wiki/{category}/_index.md to get existing entries.
    Returns: [{name, title, domain, first_source}, ...]
    """
    index_path = WIKI_DIR / category / "_index.md"
    if not index_path.exists():
        return []

    try:
        content = index_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Warning: Could not read {index_path}: {e}")
        return []

    entries = []
    in_table = False
    header_found = False

    for line in content.split("\n"):
        if line.startswith("|") and not line.startswith("| >"):
            in_table = True
            if not header_found:
                # Skip header row
                header_found = True
                continue
            if re.match(r"\|[\s-]+\|", line):
                # Skip separator row
                continue

            # Parse row: | [[Name]] | Title | Domain | First Source |
            parts = [p.strip() for p in line.split("|")]
            # parts[0] is empty (before first |), parts[-1] is empty (after last |)
            if len(parts) >= 5:
                # Extract name from wikilink [[category/Name]] or [[Name]]
                name_link = parts[1]
                name_match = re.search(r"\[\[.*?\/?([^\[\]]+)\]\]", name_link)
                name = name_match.group(1) if name_match else name_link

                entry = {
                    "name": name,
                    "title": parts[2],
                    "domain": parts[3],
                    "first_source": parts[4] if len(parts) > 4 else ""
                }
                entries.append(entry)
        elif in_table and not line.startswith("|"):
            # End of table
            break

    return entries


def extract_keywords(text: str) -> set:
    """
    Extract keywords from text for similarity scoring.
    - Lowercase, remove punctuation
    - Split into words
    - Remove common stopwords
    """
    if not text:
        return set()

    # Lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)

    # Split into words
    words = text.split()

    # Remove stopwords (minimal set)
    stopwords = {"the", "a", "an", "is", "are", "of", "to", "in", "for", "and",
                 "or", "by", "with", "from", "as", "that", "this", "these", "those",
                 "which", "who", "what", "when", "where", "how", "why", "be", "been",
                 "being", "have", "has", "had", "do", "does", "did", "will", "would",
                 "could", "should", "may", "might", "must", "shall", "can", "need"}

    keywords = set(w for w in words if w not in stopwords and len(w) > 2)
    return keywords


def keyword_overlap_score(text1: str, text2: str) -> float:
    """
    Calculate keyword overlap score (Jaccard similarity).
    Returns: 0.0 to 1.0
    """
    kw1 = extract_keywords(text1)
    kw2 = extract_keywords(text2)

    if not kw1 or not kw2:
        return 0.0

    intersection = kw1 & kw2
    union = kw1 | kw2

    return len(intersection) / len(union) if union else 0.0


def find_exact_match(proposed: str, existing: list) -> dict | None:
    """
    Find exact name match after normalization.
    Returns: matched entry or None
    """
    proposed_norm = normalize_name(proposed)

    for entry in existing:
        entry_norm = normalize_name(entry["name"])
        if proposed_norm == entry_norm:
            return entry

    # Also try matching against title
    for entry in existing:
        title_norm = normalize_name(entry["title"])
        if proposed_norm == title_norm:
            return entry

    return None


def find_similar_candidates(proposed: str, definition: str, existing: list, threshold: float = 0.3) -> list:
    """
    Find similar entries for LLM to evaluate.
    Uses: name similarity + definition keyword overlap

    Returns: [{name, title, similarity, reason}, ...]
    """
    proposed_norm = normalize_name(proposed)
    candidates = []

    for entry in existing:
        entry_norm = normalize_name(entry["name"])
        title_norm = normalize_name(entry["title"])

        # Calculate name similarity (partial match)
        name_sim = 0.0
        if proposed_norm in entry_norm or entry_norm in proposed_norm:
            name_sim = 0.8  # High similarity for substring match
        elif proposed_norm in title_norm or title_norm in proposed_norm:
            name_sim = 0.7

        # Calculate definition overlap (if definition provided)
        def_sim = keyword_overlap_score(definition, entry["title"]) if definition else 0.0

        # Combined score
        combined_sim = max(name_sim, def_sim)

        if combined_sim >= threshold:
            reason = "name_match" if name_sim >= threshold else "definition_overlap"
            candidates.append({
                "name": entry["name"],
                "title": entry["title"],
                "similarity": round(combined_sim, 2),
                "reason": reason
            })

    # Sort by similarity descending
    candidates.sort(key=lambda x: x["similarity"], reverse=True)

    return candidates


def extract_summary_tables(content: str) -> dict:
    """
    Extract Concepts Defined and Measures/Variables tables from summary.
    Returns: {concepts: [...], variables: [...]}
    """
    tables = {"concepts": [], "variables": []}

    # Find Concepts Defined section
    concepts_match = re.search(r"## Concepts Defined\n", content)
    if concepts_match:
        table_start = concepts_match.end()
        table_content = content[table_start:]

        # Parse table rows
        in_table = False
        header_found = False
        for line in table_content.split("\n"):
            if line.startswith("|") and not line.startswith("| >"):
                in_table = True
                if not header_found:
                    header_found = True
                    continue
                if re.match(r"\|[\s-]+\|", line):
                    continue

                # Parse row: | Concept | Definition | Constructs | Wiki Page |
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 5:
                    concept_name = parts[1]
                    definition = parts[2]
                    wiki_page = parts[4] if len(parts) > 4 else ""

                    # Extract wikilink name from Wiki Page column
                    # Format: [[concepts/Name]] or [[variables/Name]]
                    link_match = re.search(r"\[\[.*\/([^\[\]]+)\]\]", wiki_page)
                    wiki_name = link_match.group(1) if link_match else wiki_page.strip()

                    # Skip if no wiki page (implicit, not yet, skip, no wiki)
                    # Flexible matching: check for keywords anywhere in wiki_page
                    skip_keywords = ["not yet in wiki", "implicit", "no wiki", "skip", "common concept"]
                    if any(kw in wiki_page.lower() for kw in skip_keywords):
                        continue

                    tables["concepts"].append({
                        "concept": concept_name,
                        "definition": definition,
                        "wiki_name": wiki_name if wiki_name else concept_name.replace(" ", "_")
                    })
            elif in_table and not line.startswith("|"):
                break

    # Find Measures/Variables section
    measures_match = re.search(r"## Measures/Variables\n", content)
    if measures_match:
        table_start = measures_match.end()
        table_content = content[table_start:]

        in_table = False
        header_found = False
        for line in table_content.split("\n"):
            if line.startswith("|") and not line.startswith("| >"):
                in_table = True
                if not header_found:
                    header_found = True
                    continue
                if re.match(r"\|[\s-]+\|", line):
                    continue

                # Parse row: | Paper Variable | Wiki Name | Constructs | Concept | Computational Definition | Wiki Page |
                # Note: Computational Definition may contain | characters, breaking simple split
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 7:
                    wiki_name_col = parts[2]  # Wiki Name column (fixed position)
                    wiki_page = parts[-1] if parts[-1] else parts[-2]  # Last column (Wiki Page)
                    computation = parts[5] if len(parts) > 5 else ""

                    # Skip non-eligible variables (derived, skip, no wiki)
                    # Flexible matching: check for keywords anywhere in wiki_page
                    skip_keywords = ["derived", "skip", "no wiki", "composite", "hhi", "rolling"]
                    if any(kw in wiki_page.lower() for kw in skip_keywords):
                        continue
                    if wiki_name_col in ["[derived]", "[skip]", ""]:
                        continue

                    # Extract wikilink name from Wiki Page column
                    # Format: [[variables/Name]]
                    link_match = re.search(r"\[\[.*\/([^\[\]]+)\]\]", wiki_page)
                    proposed_name = link_match.group(1) if link_match else wiki_name_col.strip()

                    tables["variables"].append({
                        "variable": parts[1],
                        "computation": computation,
                        "wiki_name": proposed_name
                    })
            elif in_table and not line.startswith("|"):
                break

    return tables


def check_collisions(summary_path: Path) -> dict:
    """
    Check proposed wiki entries against existing entries.
    Returns: collision report dict
    """
    try:
        content = summary_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error: Could not read {summary_path}: {e}")
        return {}

    # Extract proposed entries from summary
    tables = extract_summary_tables(content)

    # Build collision report
    report = {}

    for category in CATEGORIES:
        existing = parse_index_md(category)
        proposed_list = []

        # Get proposed entries for this category
        if category == "concepts":
            proposed_items = tables.get("concepts", [])
        elif category == "variables":
            proposed_items = tables.get("variables", [])
        else:
            proposed_items = []  # constructs, methods, theories need different extraction

        for item in proposed_items:
            proposed_name = item.get("wiki_name") or item.get("concept") or item.get("variable")
            definition = item.get("definition") or item.get("computation") or ""

            # Check exact match
            exact_match = find_exact_match(proposed_name, existing)

            if exact_match:
                proposed_list.append({
                    "proposed": proposed_name,
                    "exact_match": exact_match["name"],
                    "candidates": []
                })
            else:
                # Find similar candidates
                candidates = find_similar_candidates(proposed_name, definition, existing)
                # Only include entries that need attention
                if candidates:
                    proposed_list.append({
                        "proposed": proposed_name,
                        "exact_match": None,
                        "candidates": candidates
                    })

        report[category] = proposed_list

    # Compute summary statistics
    total_checked = sum(len(items) for items in [tables.get("concepts", []), tables.get("variables", [])])
    total_in_report = sum(len(items) for items in report.values())
    exact_matches = sum(1 for items in report.values() for item in items if item["exact_match"])
    needs_review = total_in_report - exact_matches

    report["_summary"] = {
        "total_checked": total_checked,
        "exact_matches": exact_matches,
        "needs_agent_review": needs_review,
        "no_collision_skipped": total_checked - total_in_report
    }
    return report


def main():
    summary_file = None
    output_json = False

    for arg in sys.argv:
        if arg.startswith("--summary="):
            summary_file = arg.split("=", 1)[1]
        elif arg == "--summary" and len(sys.argv) > sys.argv.index(arg) + 1:
            summary_file = sys.argv[sys.argv.index(arg) + 1]
        elif arg == "--json":
            output_json = True

    if not summary_file:
        print("Usage: python Scripts/check_wiki_collision.py --summary {summary_file} [--json]")
        print("Example: python Scripts/check_wiki_collision.py --summary source/summary/gao_2026_summary.md --json")
        sys.exit(1)

    summary_path = Path(summary_file)
    if not summary_path.exists():
        summary_path = ROOT_DIR / summary_file
        if not summary_path.exists():
            print(f"Error: Summary file not found: {summary_file}")
            sys.exit(1)

    if not output_json:
        print(f"Checking wiki collisions for: {summary_path}")

    # Run collision check
    report = check_collisions(summary_path)

    # Output results
    if output_json:
        print(json.dumps(report, indent=2))
    else:
        print("\n## Collision Report")
        for category, items in report.items():
            if not items:
                continue

            print(f"\n### {category}")
            print("| Proposed | Exact Match | Similar Candidates |")
            print("|----------|-------------|--------------------|")

            for item in items:
                proposed = item["proposed"]
                exact = item["exact_match"] or "-"
                candidates = ", ".join(
                    f"{c['name']}({c['similarity']})"
                    for c in item["candidates"]
                ) or "-"

                print(f"| {proposed} | {exact} | {candidates} |")


if __name__ == "__main__":
    main()