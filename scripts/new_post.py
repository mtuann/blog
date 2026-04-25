#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
DOCS = ROOT / "docs"

SECTION_CHOICES = [
    "ml",
    "genai",
    "ai-systems",
    "efficient-ai",
    "trustworthy-ai",
    "research-notes",
    "paper-reviews",
    "cuda",
]

KIND_CONFIG = {
    "evergreen": {
        "template": "evergreen-overview.md",
        "needs_section": True,
        "default_series": "",
    },
    "series-note": {
        "template": "series-note.md",
        "needs_section": True,
        "default_series": "",
    },
    "paper-review": {
        "template": "paper-review.md",
        "needs_section": False,
        "default_series": "paper-reviews",
    },
    "roundup": {
        "template": "monthly-roundup.md",
        "needs_section": False,
        "default_series": "monthly-roundups",
    },
    "reading-map": {
        "template": "reading-map.md",
        "needs_section": False,
        "default_series": "reading-maps",
    },
}


def slugify(value: str) -> str:
    slug = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "untitled-note"


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scaffold a new blog post from a local template."
    )
    parser.add_argument(
        "--kind",
        required=True,
        choices=sorted(KIND_CONFIG),
        help="Template type to use.",
    )
    parser.add_argument("--title", required=True, help="Title for the new note.")
    parser.add_argument(
        "--section",
        choices=SECTION_CHOICES,
        help="Docs subdirectory for evergreen or series-note content.",
    )
    parser.add_argument("--slug", help="Optional filename slug.")
    parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="Publishing date in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--summary",
        default="",
        help="Optional summary to insert into the front matter.",
    )
    parser.add_argument(
        "--series",
        default=None,
        help="Optional series override. Defaults depend on --kind.",
    )
    parser.add_argument(
        "--tags",
        default="",
        help="Comma-separated tags to insert into front matter.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the target path without writing a file.",
    )
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    config = KIND_CONFIG[args.kind]
    if config["needs_section"] and not args.section:
        raise SystemExit(f"--section is required for kind '{args.kind}'.")
    if not config["needs_section"] and args.section:
        raise SystemExit(f"--section is not used for kind '{args.kind}'.")


def render_tags(raw_tags: str) -> str:
    tags = [tag.strip() for tag in raw_tags.split(",") if tag.strip()]
    if not tags:
        return " []"
    rendered = "\n" + "\n".join(f"  - {tag}" for tag in tags)
    return rendered


def destination_for(args: argparse.Namespace, slug: str) -> Path:
    if args.kind == "paper-review":
        return DOCS / "paper-reviews" / f"{slug}.md"
    if args.kind == "roundup":
        year_month = args.date[:7]
        return DOCS / "research-notes" / "roundups" / f"{year_month}-{slug}.md"
    if args.kind == "reading-map":
        return DOCS / "research-notes" / "reading-maps" / f"{slug}.md"
    return DOCS / args.section / f"{slug}.md"


def render_template(template_path: Path, args: argparse.Namespace) -> str:
    text = template_path.read_text(encoding="utf-8")
    text = text.replace('title: ""', f"title: {yaml_quote(args.title)}")
    text = text.replace("date: 2026-04-24", f"date: {args.date}")
    text = text.replace("updated: 2026-04-24", f"updated: {args.date}")
    text = text.replace('summary: ""', f"summary: {yaml_quote(args.summary)}")
    text = text.replace("tags: []", f"tags:{render_tags(args.tags)}")

    series = args.series
    if series is None:
        series = KIND_CONFIG[args.kind]["default_series"]
    text = text.replace('series: ""', f'series: "{series}"')
    text = text.replace('series: "paper-reviews"', f'series: "{series}"')
    text = text.replace('series: "monthly-roundups"', f'series: "{series}"')
    text = text.replace('series: "reading-maps"', f'series: "{series}"')

    heading_replaced = False
    lines = []
    for line in text.splitlines():
        if not heading_replaced and line.strip() == "# Title":
            lines.append(f"# {args.title}")
            heading_replaced = True
        else:
            lines.append(line)
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    validate_args(args)

    slug = args.slug or slugify(args.title)
    config = KIND_CONFIG[args.kind]
    template_path = TEMPLATES / config["template"]
    target = destination_for(args, slug)

    if args.dry_run:
        print(target)
        return 0

    if target.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {target}")

    target.parent.mkdir(parents=True, exist_ok=True)
    rendered = render_template(template_path, args)
    target.write_text(rendered, encoding="utf-8")
    print(target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
