#!/usr/bin/env python3
"""
Check newly created wiki pages against PRE-EXISTING wiki entries for potential merges.

Unlike check_wiki_collision.py (which checks proposed entries from a summary before creation),
this script runs AFTER wiki pages are created. It excludes the newly created pages from the
"existing" pool so the orchestrator can find genuinely pre-existing pages that should be merged.

Usage:
    python Scripts/check_new_page_collision.py --new-pages new_pages.json --json

Input JSON format (new_pages.json):
{
    "concepts": ["Concept_Name_1", "Concept_Name_2"],
    "variables": ["Variable_Name_1"],
    "constructs": [],
    "methods": [],
    "theories": []
}

Output JSON:
{
    "concepts": [{"new_page": "Name", "exact_match": null, "candidates": [...]}],
    ...
    "_summary": {"total_new": N, "exact_matches": N, "needs_review": N, "no_collision": N}
}
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
    """Normalize wiki name for comparison."""
    name = name.lower()
    name = re.sub(r"\[\[.*?\/", "", name)
    name = re.sub(r"\]\]", "", name)
    name = name.replace("_", " ").replace("-", " ")
    name = re.sub(r"[^\w\s']", "", name)
    name = " ".join(name.split())
    return name


def extract_keywords(text: str) -> set:
    """Extract keywords from text for similarity scoring."""
    if not text:
        return set()
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    words = text.split()
    stopwords = {"the", "a", "an", "is", "are", "of", "to", "in", "for", "and",
                 "or", "by", "with", "from", "as", "that", "this", "these", "those",
                 "which", "who", "what", "when", "where", "how", "why", "be", "been",
                 "being", "have", "has", "had", "do", "does", "did", "will", "would",
                 "could", "should", "may", "might", "must", "shall", "can", "need"}
    return set(w for w in words if w not in stopwords and len(w) > 2)


def keyword_overlap_score(text1: str, text2: str) -> float:
    """Jaccard similarity of keywords."""
    kw1 = extract_keywords(text1)
    kw2 = extract_keywords(text2)
    if not kw1 or not kw2:
        return 0.0
    intersection = kw1 & kw2
    union = kw1 | kw2
    return len(intersection) / len(union) if union else 0.0


def parse_index_md(category: str) -> list:
    """Parse wiki/{category}/_index.md to get existing entries."""
    index_path = WIKI_DIR / category / "_index.md"
    if not index_path.exists():
        return []

    try:
        content = index_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Warning: Could not read {index_path}: {e}", file=sys.stderr)
        return []

    entries = []
    in_table = False
    header_found = False

    for line in content.split("\n"):
        if line.startswith("|") and not line.startswith("| >"):
            in_table = True
            if not header_found:
                header_found = True
                continue
            if re.match(r"\|[\s-]+\|", line):
                continue

            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 5:
                name_link = parts[1]
                name_match = re.search(r"\[\[.*?\/?([^\[\]]+)\]\]", name_link)
                name = name_match.group(1) if name_match else name_link

                entries.append({
                    "name": name,
                    "title": parts[2],
                    "domain": parts[3],
                    "first_source": parts[4] if len(parts) > 4 else ""
                })
        elif in_table and not line.startswith("|"):
            break

    return entries


def read_wiki_page_definition(category: str, page_name: str) -> str:
    """Read the Definition section from a wiki page."""
    page_path = WIKI_DIR / category / f"{page_name}.md"
    if not page_path.exists():
        return ""

    try:
        content = page_path.read_text(encoding="utf-8")
    except Exception:
        return ""

    # Extract the Definition or "What It Measures" section
    for pattern in [r"## Definition\n(.*?)(?:\n##|\Z)", r"## What It Measures\n(.*?)(?:\n##|\Z)"]:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return match.group(1).strip()[:500]

    return ""


def find_exact_match(proposed: str, existing: list) -> dict | None:
    """Find exact name match after normalization."""
    proposed_norm = normalize_name(proposed)
    for entry in existing:
        if normalize_name(entry["name"]) == proposed_norm:
            return entry
    for entry in existing:
        if normalize_name(entry["title"]) == proposed_norm:
            return entry
    return None


def find_similar_candidates(proposed: str, definition: str, existing: list, threshold: float = 0.35) -> list:
    """Find similar entries for semantic comparison."""
    proposed_norm = normalize_name(proposed)
    candidates = []

    for entry in existing:
        entry_norm = normalize_name(entry["name"])
        title_norm = normalize_name(entry["title"])

        name_sim = 0.0
        if proposed_norm in entry_norm or entry_norm in proposed_norm:
            name_sim = 0.8
        elif proposed_norm in title_norm or title_norm in proposed_norm:
            name_sim = 0.7

        def_sim = keyword_overlap_score(definition, entry["title"]) if definition else 0.0
        combined_sim = max(name_sim, def_sim)

        if combined_sim >= threshold:
            candidates.append({
                "name": entry["name"],
                "title": entry["title"],
                "similarity": round(combined_sim, 2),
                "reason": "name_match" if name_sim >= threshold else "definition_overlap"
            })

    candidates.sort(key=lambda x: x["similarity"], reverse=True)
    return candidates


def check_collisions(new_pages: dict) -> dict:
    """Check newly created pages against pre-existing entries (excluding the new ones)."""
    report = {}

    for category in CATEGORIES:
        new_names = new_pages.get(category, [])
        if not new_names:
            report[category] = []
            continue

        existing = parse_index_md(category)
        # Exclude newly created pages from existing pool
        new_norm = {normalize_name(n) for n in new_names}
        pre_existing = [e for e in existing if normalize_name(e["name"]) not in new_norm]

        category_results = []
        for page_name in new_names:
            definition = read_wiki_page_definition(category, page_name)
            exact_match = find_exact_match(page_name, pre_existing)

            if exact_match:
                category_results.append({
                    "new_page": page_name,
                    "exact_match": exact_match["name"],
                    "candidates": []
                })
            else:
                candidates = find_similar_candidates(page_name, definition, pre_existing)
                if candidates:
                    category_results.append({
                        "new_page": page_name,
                        "exact_match": None,
                        "candidates": candidates
                    })

        report[category] = category_results

    # Summary
    total_new = sum(len(new_pages.get(c, [])) for c in CATEGORIES)
    total_in_report = sum(len(items) for items in report.values())
    exact_matches = sum(1 for items in report.values() for item in items if item["exact_match"])
    needs_review = total_in_report - exact_matches

    report["_summary"] = {
        "total_new_pages": total_new,
        "exact_matches": exact_matches,
        "needs_semantic_review": needs_review,
        "no_collision": total_new - total_in_report
    }
    return report


def main():
    new_pages_file = None
    output_json = False

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg.startswith("--new-pages="):
            new_pages_file = arg.split("=", 1)[1]
        elif arg == "--new-pages":
            if i + 1 < len(sys.argv):
                new_pages_file = sys.argv[i + 1]
                i += 1
        elif arg == "--json":
            output_json = True
        i += 1

    if not new_pages_file:
        print("Usage: python Scripts/check_new_page_collision.py --new-pages <json_file> [--json]")
        print("Example: python Scripts/check_new_page_collision.py --new-pages new_pages.json --json")
        sys.exit(1)

    new_pages_path = Path(new_pages_file)
    if not new_pages_path.exists():
        new_pages_path = ROOT_DIR / new_pages_file
        if not new_pages_path.exists():
            print(f"Error: New pages JSON file not found: {new_pages_file}", file=sys.stderr)
            sys.exit(1)

    try:
        new_pages = json.loads(new_pages_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error: Could not parse JSON: {e}", file=sys.stderr)
        sys.exit(1)

    report = check_collisions(new_pages)

    if output_json:
        print(json.dumps(report, indent=2))
    else:
        print("\n## Post-Ingest Collision Report")
        for category, items in report.items():
            if category.startswith("_") or not items:
                continue
            print(f"\n### {category}")
            print("| New Page | Exact Match | Candidates |")
            print("|----------|-------------|------------|")
            for item in items:
                proposed = item["new_page"]
                exact = item["exact_match"] or "-"
                candidates = ", ".join(
                    f"{c['name']}({c['similarity']})"
                    for c in item.get("candidates", [])
                ) or "-"
                print(f"| {proposed} | {exact} | {candidates} |")
        s = report.get("_summary", {})
        print(f"\n*{s.get('total_new_pages', 0)} new pages checked. "
              f"{s.get('exact_matches', 0)} exact matches, "
              f"{s.get('needs_semantic_review', 0)} need semantic review, "
              f"{s.get('no_collision', 0)} clean.*")


if __name__ == "__main__":
    main()
