#!/usr/bin/env python3
"""
Find wiki pages not linked from any _index.md.

Usage:
    python scripts/list_orphans.py --wiki-dir=<path> [--verbose]
    python scripts/list_orphans.py --wiki-dir=../wiki --verbose

This script:
    - Lists all .md in wiki/*/ (excluding _index.md)
    - Checks if each file is referenced in its parent _index.md
    - Reports orphan pages with suggestions for inclusion

Note: --wiki-dir is REQUIRED. Points to the wiki directory containing category folders.
"""

import os
import re
import sys
from pathlib import Path

CATEGORIES = ["concepts", "theories", "proxies", "methods", "constructs", "variables"]

def get_index_links(index_file: Path) -> set:
    """Extract all wikilinks from an _index.md file."""
    if not index_file.exists():
        return set()

    content = index_file.read_text(encoding="utf-8")
    links = re.findall(r"\[\[([^\]]+)\]\]", content)

    # Extract just the filename part
    names = set()
    for link in links:
        name = link.split("|")[0]
        if "/" in name:
            name = name.split("/")[-1]
        names.add(name)

    return names

def find_orphans(wiki_dir: Path, verbose: bool = False):
    """Find all orphan wiki pages."""
    orphan_count = 0
    total_pages = 0

    print("# Orphan Pages Report")
    print()

    for category in CATEGORIES:
        category_dir = wiki_dir / category

        if not category_dir.exists():
            continue

        index_file = category_dir / "_index.md"
        indexed_names = get_index_links(index_file)

        orphan_pages = []

        for md_file in category_dir.glob("*.md"):
            if md_file.name == "_index.md":
                continue

            total_pages += 1
            page_name = md_file.stem

            if page_name not in indexed_names:
                orphan_pages.append(md_file)

        if orphan_pages:
            print(f"## {category}")
            print(f"Indexed: {len(indexed_names)}, Orphans: {len(orphan_pages)}")
            print()

            for orphan in orphan_pages:
                orphan_count += 1
                rel_path = orphan.relative_to(wiki_dir)

                if verbose:
                    print(f"- {rel_path}")
                    print(f"  Suggestion: Add [[{orphan.stem}]] to {category}/_index.md")
                    print()
                else:
                    print(f"- {rel_path}")

            print()

    print(f"## Summary")
    print(f"Total pages: {total_pages}")
    print(f"Orphan pages: {orphan_count}")

    return orphan_count

def main():
    wiki_dir = None
    verbose = False

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg.startswith("--wiki-dir="):
            wiki_dir = Path(arg.split("=", 1)[1])
        elif arg == "--wiki-dir" and i + 1 < len(sys.argv):
            wiki_dir = Path(sys.argv[i + 1])
            i += 1
        elif arg in ["--verbose", "-v"]:
            verbose = True
        i += 1

    if not wiki_dir:
        print("Usage: python scripts/list_orphans.py --wiki-dir=<path> [--verbose]")
        print("Example: python scripts/list_orphans.py --wiki-dir=../wiki --verbose")
        print("")
        print("ERROR: --wiki-dir is REQUIRED. Points to the wiki directory containing category folders.")
        sys.exit(1)

    if not wiki_dir.exists():
        print(f"ERROR: Wiki directory not found: {wiki_dir}")
        sys.exit(1)

    find_orphans(wiki_dir, verbose)

if __name__ == "__main__":
    main()
