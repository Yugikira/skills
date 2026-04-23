#!/usr/bin/env python3
"""
Regenerate all _index.md files from wiki directory structure.

Usage:
    python Scripts/update_indexes.py [--dry-run]

This script:
    - Scans wiki/concepts/, wiki/theories/, wiki/variables/, wiki/methods/
    - Reads YAML frontmatter from each .md file for metadata
    - Generates _index.md with one-line summaries from frontmatter
    - Updates wiki/_index.md master index
"""

import os
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
WIKI_DIR = SCRIPT_DIR.parent / "wiki"

def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}

    end_match = re.search(r"\n---\n", content[3:])
    if not end_match:
        return {}

    frontmatter_text = content[3:end_match.end() + 1]
    metadata = {}

    for line in frontmatter_text.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value.startswith("["):
                value = [v.strip().strip('"').strip("'")
                         for v in value[1:-1].split(",") if v.strip()]
            metadata[key] = value

    return metadata

def get_page_title(content: str, frontmatter: dict) -> str:
    """Get title from frontmatter or first heading."""
    if "name" in frontmatter:
        return frontmatter["name"]
    if "title" in frontmatter:
        return frontmatter["title"]

    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if match:
        return match.group(1)

    return "Untitled"

def scan_category(category_dir: Path) -> list:
    """Scan a category directory for all wiki pages."""
    pages = []

    if not category_dir.exists():
        return pages

    for md_file in category_dir.glob("*.md"):
        if md_file.name == "_index.md":
            continue

        try:
            content = md_file.read_text(encoding="utf-8")
            frontmatter = parse_frontmatter(content)
            title = get_page_title(content, frontmatter)

            pages.append({
                "file": md_file,
                "name": md_file.stem,
                "title": title,
                "frontmatter": frontmatter
            })
        except Exception as e:
            print(f"Warning: Could not read {md_file}: {e}")

    return sorted(pages, key=lambda p: p["name"])

def generate_category_index(category: str, pages: list) -> str:
    """Generate index content for a category."""
    category_names = {
        "concepts": "Concepts",
        "theories": "Theories",
        "variables": "Variables",
        "methods": "Methods"
    }

    lines = [
        f"# {category_names.get(category, category)} Index",
        "",
        f"{len(pages)} pages",
        "",
        "| Name | Title | Domain | First Source |",
        "|------|-------|--------|--------------|"
    ]

    for page in pages:
        name = page["name"]
        title = page["title"]
        domain = page["frontmatter"].get("domain", "unknown")
        first = page["frontmatter"].get("first_defined",
                                        page["frontmatter"].get("first_proposed",
                                        page["frontmatter"].get("first_used", "N/A")))

        lines.append(f"| [[{name}]] | {title} | {domain} | {first} |")

    return "\n".join(lines) + "\n"

def generate_master_index(stats: dict) -> str:
    """Generate master wiki/_index.md content."""
    lines = [
        "# Knowledge Base Index",
        "",
        "## Statistics",
        f"- Papers processed: See source/summary/ directory",
        f"- Concepts: {stats['concepts']}",
        f"- Theories: {stats['theories']}",
        f"- Variables: {stats['variables']}",
        f"- Methods: {stats['methods']}",
        "",
        "## Categories",
        "- [[concepts/_index]] - Concepts defined and used",
        "- [[theories/_index]] - Theoretical frameworks",
        "- [[variables/_index]] - Measures and variables",
        "- [[methods/_index]] - Research methodologies",
        "",
        "## Recent Activity",
        "See [[log]] for full history."
    ]

    return "\n".join(lines) + "\n"

def update_indexes(dry_run: bool = False):
    """Update all index files."""
    categories = ["concepts", "theories", "variables", "methods"]
    stats = {}

    for category in categories:
        category_dir = WIKI_DIR / category
        pages = scan_category(category_dir)
        stats[category] = len(pages)

        index_content = generate_category_index(category, pages)
        index_file = category_dir / "_index.md"

        if dry_run:
            print(f"\n=== {index_file} ===")
            print(index_content)
        else:
            category_dir.mkdir(parents=True, exist_ok=True)
            index_file.write_text(index_content, encoding="utf-8")
            print(f"Updated: {index_file}")

    master_content = generate_master_index(stats)
    master_file = WIKI_DIR / "_index.md"

    if dry_run:
        print(f"\n=== {master_file} ===")
        print(master_content)
    else:
        WIKI_DIR.mkdir(parents=True, exist_ok=True)
        master_file.write_text(master_content, encoding="utf-8")
        print(f"Updated: {master_file}")

def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("Dry run mode - showing generated indexes without writing")

    update_indexes(dry_run)

if __name__ == "__main__":
    main()