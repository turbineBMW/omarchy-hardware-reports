#!/usr/bin/env python3
"""Check a hardware report zip and unpack it under reports/.

  ingest.py --zip report.zip                 # a local file
  ingest.py --issue-body body.md             # the zip linked from an issue

Only the files the Windows tool writes are accepted, each under a size
limit; anything else rejects the whole report. Prints the folder it wrote.
"""

import argparse
import io
import json
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ALLOWED = re.compile(
    r"^(report\.json|summary\.md|devices\.json|firmware\.json|hwids\.json|smbios/dmi\.bin"
    r"|acpi/[a-z0-9_]{1,8}[0-9]{0,3}\.dat|edid/[0-9]{1,2}-[A-Za-z0-9]{1,16}(-internal)?\.bin)$"
)
MAX_ZIP = 32 << 20
MAX_ENTRY = 16 << 20
MAX_TOTAL = 64 << 20
MAX_ENTRIES = 300
ATTACHMENT = re.compile(r"https://github\.com/user-attachments/files/\d+/[A-Za-z0-9._-]+\.zip")


class Rejected(Exception):
    pass


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s or "unknown"


def download(body):
    urls = ATTACHMENT.findall(body)
    if not urls:
        raise Rejected("no zip file is attached; drag the hardware-report zip into the issue")
    if len(set(urls)) > 1:
        raise Rejected("more than one zip is attached; attach only the report")
    request = urllib.request.Request(urls[0], headers={"User-Agent": "omarchy-hardware-reports"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read(MAX_ZIP + 1)
    if len(data) > MAX_ZIP:
        raise Rejected("the zip is larger than a report can be")
    return data


def check(data):
    try:
        archive = zipfile.ZipFile(io.BytesIO(data))
    except zipfile.BadZipFile:
        raise Rejected("the attachment is not a zip file")
    entries = archive.infolist()
    if len(entries) > MAX_ENTRIES:
        raise Rejected("the zip holds more files than a report does")
    total = 0
    files = {}
    for entry in entries:
        if entry.is_dir():
            continue
        if not ALLOWED.match(entry.filename):
            raise Rejected(f"the zip holds a file a report does not: {entry.filename!r}")
        if entry.file_size > MAX_ENTRY:
            raise Rejected(f"{entry.filename} is too large")
        total += entry.file_size
        if total > MAX_TOTAL:
            raise Rejected("the zip unpacks to more than a report can be")
        with archive.open(entry) as f:
            content = f.read(MAX_ENTRY + 1)
        if len(content) > MAX_ENTRY:
            raise Rejected(f"{entry.filename} is too large")
        files[entry.filename] = content
    if "report.json" not in files:
        raise Rejected("the zip has no report.json; is it the tool's report?")
    try:
        report = json.loads(files["report.json"])
    except ValueError:
        raise Rejected("report.json is not valid JSON")
    if report.get("format") != 1 or not re.fullmatch(r"[0-9a-f]{8}", str(report.get("id", ""))):
        raise Rejected("report.json is not from a version of the tool this repository knows")
    for name in ("devices.json", "firmware.json", "hwids.json"):
        if name in files:
            try:
                json.loads(files[name])
            except ValueError:
                raise Rejected(f"{name} is not valid JSON")
    return report, files


def unpack(report, files):
    identity = report.get("identity") or {}
    folder = ROOT / "reports" / slug(identity.get("manufacturer")) / slug(identity.get("productName")) / report["id"]
    if folder.exists():
        raise Rejected(f"report {report['id']} is already in the repository")
    for name, content in files.items():
        path = folder / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    return folder


def main():
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--zip", type=Path)
    source.add_argument("--issue-body", type=Path)
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    try:
        data = args.zip.read_bytes() if args.zip else download(args.issue_body.read_text())
        report, files = check(data)
        if args.check_only:
            print(report["id"])
            return 0
        print(unpack(report, files).relative_to(ROOT))
        return 0
    except Rejected as e:
        print(f"rejected: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
