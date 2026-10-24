#!/usr/bin/env python3
"""Write MODELS.md: one row per model, from every reports/*/*/*/report.json."""

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def cell(text):
    return (text or "").replace("|", "\\|").strip()


def main():
    models = defaultdict(list)
    for path in sorted((ROOT / "reports").glob("*/*/*/report.json")):
        report = json.loads(path.read_text())
        models[path.parent.parent].append(report)

    lines = [
        "# Models",
        "",
        "Every model a hardware report has come in for. Written by `tools/index.py`; do not edit by hand.",
        "",
        "| Manufacturer | Product | SKUs | Processor | Panels | Reports | ACPI tables |",
        "|---|---|---|---|---|---|---|",
    ]
    for folder, reports in sorted(models.items(), key=lambda m: str(m[0]).lower()):
        first = reports[0].get("identity") or {}
        skus = sorted({(r.get("identity") or {}).get("sku") or "" for r in reports} - {""})
        panels = sorted({r.get("panel") or "" for r in reports} - {""})
        processors = sorted({r.get("processor") or "" for r in reports} - {""})
        acpi = max(len(r.get("acpi") or []) for r in reports)
        link = folder.relative_to(ROOT).as_posix()
        lines.append(
            f"| {cell(first.get('manufacturer'))} | [{cell(first.get('productName'))}]({link}) | {cell(', '.join(skus))} "
            f"| {cell(', '.join(processors))} | {cell(', '.join(panels))} | {len(reports)} | {acpi} |"
        )
    if not models:
        lines.append("| | No reports yet | | | | | |")
    (ROOT / "MODELS.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
