#!/usr/bin/env python3
"""
Find broken [[filename]] wikilinks across all markdown files.

Usage:
    python scripts/check_wikilinks.py --root-dir=<path> [--report broken_links.txt]
    python scripts/check_wikilinks.py --root-dir=.. --report broken_links.txt

This script:
    - Scans all .md files in wiki/, source/summary/, source/conversations/
    - Extracts all [[link]] patterns
    - Checks if target file exists
    - Reports broken links with source file and line number

Note: --root-dir is REQUIRED. Points to the directory containing source/ and wiki/.
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

# Fix Windows console encoding issue
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


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

def resolve_link_target(link: str, source_file: Path, root_dir: Path) -> Path:
    """Resolve a wikilink target to an actual file path."""
    # Remove any display text after | if present
    target = link.split("|")[0]

    # Handle relative paths with slashes
    if "/" in target:
        # Path like "concepts/market_efficiency" - resolve from wiki/
        return root_dir / "wiki" / f"{target}.md"
    elif target.startswith("raw/"):
        return root_dir / f"{target}"
    elif target.startswith("source/"):
        return root_dir / f"{target}.md"
    else:
        # Bare link like "market_efficiency" - check wiki categories
        for category in ["concepts", "theories", "variables", "methods"]:
            candidate = root_dir / "wiki" / category / f"{target}.md"
            if candidate.exists():
                return candidate

        # Also check wiki root
        return root_dir / "wiki" / f"{target}.md"

def check_wikilinks(root_dir: Path, report_file: str = None):
    """Check all wikilinks and report broken ones."""

    # Directories to scan for markdown files
    scan_dirs = [
        root_dir / "wiki",
        root_dir / "source" / "summary",
        root_dir / "source" / "conversations"
    ]

    broken_links = defaultdict(list)
    total_links = 0
    broken_count = 0

    for scan_dir in scan_dirs:
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
                    target_path = resolve_link_target(link_info["target"], md_file, root_dir)

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
            rel_path = source_file.relative_to(root_dir)
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
    root_dir = None
    report_file = None

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg.startswith("--root-dir="):
            root_dir = Path(arg.split("=", 1)[1])
        elif arg == "--root-dir" and i + 1 < len(sys.argv):
            root_dir = Path(sys.argv[i + 1])
            i += 1
        elif arg.startswith("--report="):
            report_file = arg.split("=", 1)[1]
        elif arg == "--report" and i + 1 < len(sys.argv):
            report_file = sys.argv[i + 1]
            i += 1
        i += 1

    if not root_dir:
        print("Usage: python scripts/check_wikilinks.py --root-dir=<path> [--report <file>]")
        print("Example: python scripts/check_wikilinks.py --root-dir=.. --report broken_links.txt")
        print("")
        print("ERROR: --root-dir is REQUIRED. Points to directory containing source/ and wiki/.")
        sys.exit(1)

    if not root_dir.exists():
        print(f"ERROR: Root directory not found: {root_dir}")
        sys.exit(1)

    check_wikilinks(root_dir, report_file)

if __name__ == "__main__":
    main()
