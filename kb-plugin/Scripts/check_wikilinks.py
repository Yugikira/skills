#!/usr/bin/env python3
"""
Find broken [[filename]] wikilinks across all markdown files.

Usage:
    python Scripts/check_wikilinks.py [--report broken_links.txt]

This script:
    - Scans all .md files in wiki/, source/summary/, source/conversations/
    - Extracts all [[link]] patterns
    - Checks if target file exists
    - Reports broken links with source file and line number
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent.parent

# Directories to scan for markdown files
SCAN_DIRS = [
    ROOT_DIR / "wiki",
    ROOT_DIR / "source" / "summary",
    ROOT_DIR / "source" / "conversations"
]

def find_wikilinks(content: str) -> list:
    """Extract all [[link]] patterns from content with line numbers."""
    links = []
    lines = content.split("\n")

    for line_num, line in enumerate(lines, 1):
        # Find all [[...]] patterns
        matches = re.findall(r"\[\[([^\]]+)\]\]", line)
        for match in matches:
            links.append({
                "target": match,
                "line": line_num,
                "text": line.strip()
            })

    return links

def resolve_link_target(link: str, source_file: Path) -> Path:
    """Resolve a wikilink target to an actual file path."""
    # Remove any display text after | if present
    target = link.split("|")[0]

    # Handle relative paths with slashes
    if "/" in target:
        # Path like "concepts/market_efficiency" - resolve from wiki/
        return ROOT_DIR / "wiki" / f"{target}.md"
    elif target.startswith("raw/"):
        return ROOT_DIR / f"{target}"
    elif target.startswith("source/"):
        return ROOT_DIR / f"{target}.md"
    else:
        # Bare link like "market_efficiency" - check wiki categories
        for category in ["concepts", "theories", "variables", "methods"]:
            candidate = ROOT_DIR / "wiki" / category / f"{target}.md"
            if candidate.exists():
                return candidate

        # Also check wiki root
        return ROOT_DIR / "wiki" / f"{target}.md"

def check_wikilinks(report_file: str = None):
    """Check all wikilinks and report broken ones."""
    broken_links = defaultdict(list)
    total_links = 0
    broken_count = 0

    for scan_dir in SCAN_DIRS:
        if not scan_dir.exists():
            continue

        for md_file in scan_dir.rglob("*.md"):
            if md_file.name.startswith("_index"):
                continue

            try:
                content = md_file.read_text(encoding="utf-8")
                links = find_wikilinks(content)

                for link_info in links:
                    total_links += 1
                    target_path = resolve_link_target(link_info["target"], md_file)

                    if not target_path.exists():
                        broken_count += 1
                        broken_links[md_file].append(link_info)

            except Exception as e:
                print(f"Warning: Could not read {md_file}: {e}")

    # Output results
    output_lines = []
    output_lines.append(f"# Wikilink Check Report")
    output_lines.append(f"")
    output_lines.append(f"Total wikilinks: {total_links}")
    output_lines.append(f"Broken wikilinks: {broken_count}")
    output_lines.append(f"")

    if broken_count > 0:
        output_lines.append("## Broken Links by Source File")
        output_lines.append("")

        for source_file, links in sorted(broken_links.items()):
            rel_path = source_file.relative_to(ROOT_DIR)
            output_lines.append(f"### {rel_path}")

            for link in links:
                output_lines.append(f"  - Line {link['line']}: [[{link['target']}]]")
                output_lines.append(f"    Context: {link['text'][:80]}...")

            output_lines.append("")

    report_text = "\n".join(output_lines)

    if report_file:
        Path(report_file).write_text(report_text, encoding="utf-8")
        print(f"Report written to: {report_file}")
    else:
        print(report_text)

    return broken_count

def main():
    report_file = None

    for arg in sys.argv:
        if arg.startswith("--report="):
            report_file = arg.split("=", 1)[1]
        elif arg == "--report" and len(sys.argv) > sys.argv.index(arg) + 1:
            report_file = sys.argv[sys.argv.index(arg) + 1]

    check_wikilinks(report_file)

if __name__ == "__main__":
    main()
