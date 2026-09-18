#!/usr/bin/env python3
"""
Regenerate the comparison table in README.md from tools.yaml.

    python render_table.py            # print the table to stdout
    python render_table.py --write    # rewrite the block between the markers
    python render_table.py --check    # exit non-zero if README is out of sync
"""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

START = "<!-- TABLE:START -->"
END = "<!-- TABLE:END -->"


def linkify(provider: dict) -> str:
    name = provider.get("name", "")
    url = provider.get("url") or ""
    return f"[{name}]({url})" if url else name


COLUMNS = [
    ("name", "Provider", linkify),
    ("kyb_and_ubo", "KYB and UBO checks", lambda p: p.get("kyb_and_ubo", "")),
    ("aml_screening", "AML screening", lambda p: p.get("aml_screening", "")),
    ("billing_model", "Billing model", lambda p: p.get("billing_model", "")),
    ("best_for", "Best for", lambda p: p.get("best_for", "")),
]


def build_table(providers: list[dict]) -> str:
    header = "| " + " | ".join(label for _, label, _ in COLUMNS) + " |"
    divider = "| " + " | ".join("---" for _ in COLUMNS) + " |"
    rows = []
    for provider in providers:
        cells = [fn(provider) for _, _, fn in COLUMNS]
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, divider, *rows])


def main() -> int:
    ap = argparse.ArgumentParser()
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    ap.add_argument("--data", type=Path, default=Path("tools.yaml"))
    ap.add_argument("--readme", type=Path, default=Path("README.md"))
    args = ap.parse_args()

    providers = yaml.safe_load(args.data.read_text(encoding="utf-8"))["providers"]
    table = build_table(providers)

    if not args.write and not args.check:
        print(table)
        return 0

    text = args.readme.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit("README is missing the TABLE markers.")
    before = text.split(START)[0]
    after = text.split(END)[1]
    new = f"{before}{START}\n{table}\n{END}{after}"

    if args.check:
        if new != text:
            print("README table is out of sync with tools.yaml.")
            return 1
        print("README table matches tools.yaml.")
        return 0

    args.readme.write_text(new, encoding="utf-8")
    print(f"Updated table in {args.readme} ({len(providers)} providers).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
