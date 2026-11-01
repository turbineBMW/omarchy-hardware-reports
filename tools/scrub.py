#!/usr/bin/env python3
"""Take the SoC serial number out of a report's ACPI tables.

  scrub.py reports/<maker>/<model>/<id>      # one report folder, in place

Qualcomm's DSDT declares Name (SOSN, ...) and the firmware fills it with the
chip's serial number at boot, which tells units of one model apart. The
installer blanks it since 1.0.1; ingest.py runs this over every report so
older ones arrive the same way. The value is zeroed where it sits and the
table's checksum put right, and the report's own record says it was done.
"""

import json
import re
import sys
from pathlib import Path

NAME_OP = 0x08
INTEGER_WIDTH = {0x0A: 1, 0x0B: 2, 0x0C: 4, 0x0E: 8}
STRING_PREFIX = 0x0D
SERIAL_NAMES = (b"SOSN",)
REDACTION = "SoC serial number in the ACPI tables (SOSN)"


def scrub_table(table):
    """The table with each serial-number Name's value zeroed, and the values
    it held; the same bytes and an empty list when it held none."""
    data = bytearray(table)
    found = []
    for name in SERIAL_NAMES:
        at = data.find(name, 1)
        while at > 0:
            v = at + len(name)
            if data[at - 1] == NAME_OP and v < len(data):
                width = INTEGER_WIDTH.get(data[v])
                if width and v + 1 + width <= len(data):
                    value = int.from_bytes(data[v + 1:v + 1 + width], "little")
                    if value:
                        found.append(f"{value:x}")
                        data[v + 1:v + 1 + width] = bytes(width)
                elif data[v] == STRING_PREFIX:
                    end = data.find(b"\0", v + 1)
                    if end > v + 1:
                        found.append(bytes(data[v + 1:end]).decode("ascii", "replace"))
                        data[v + 1:end] = bytes(end - v - 1)
            at = data.find(name, at + 1)
    if found and len(data) > 9:
        data[9] = 0
        data[9] = (-sum(data)) & 0xFF
    return bytes(data), found


def scrub_files(files):
    """files: {name: bytes} as ingest.py holds a report. Scrubs acpi/*.dat in
    place and notes it in report.json and summary.md. Returns the serials found."""
    found = []
    for name in sorted(files):
        if re.fullmatch(r"acpi/[a-z0-9_]+\.dat", name):
            files[name], values = scrub_table(files[name])
            found += values
    if found:
        # Edited as text, so the files keep their line endings and layout.
        text = files["report.json"].decode("utf-8")
        if REDACTION not in json.loads(text).get("redactions", []):
            nl = "\r\n" if "\r\n" in text else "\n"
            edited = re.sub(r'("redactions": \[)(.*?)(\r?\n\s*\])',
                            lambda m: f'{m.group(1)}{m.group(2)},{nl}    "{REDACTION}"{m.group(3)}', text, count=1, flags=re.DOTALL)
            if REDACTION in json.loads(edited).get("redactions", []):
                files["report.json"] = edited.encode("utf-8")
        summary = files.get("summary.md", b"").decode("utf-8", "replace")
        nl = "\r\n" if "\r\n" in summary else "\n"
        heading = f"## Left out for privacy{nl}{nl}"
        if REDACTION not in summary and heading in summary:
            files["summary.md"] = summary.replace(heading, f"{heading}- {REDACTION}{nl}", 1).encode("utf-8")
    return found


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    folder = Path(sys.argv[1])
    paths = [p for p in folder.rglob("*") if p.is_file()]
    files = {str(p.relative_to(folder)).replace("\\", "/"): p.read_bytes() for p in paths}
    before = dict(files)
    found = scrub_files(files)
    for name, content in files.items():
        if content != before[name]:
            (folder / name).write_bytes(content)
            print(f"rewrote {name}")
    print(f"{len(found)} serial number(s) blanked" if found else "nothing to blank")
    return 0


if __name__ == "__main__":
    sys.exit(main())
