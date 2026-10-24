# Omarchy hardware reports

Linux runs on Arm laptops through a device tree, written by hand for each model. Writing one takes what the laptop's firmware and Windows know about it: the ACPI tables, the SMBIOS strings its hardware IDs come from, which devices sit where, and which firmware the drivers load.

This repository collects that from as many Windows on Arm laptops as people will run the tool on, so the Omarchy Dragon team and anyone else writing device trees can work from it, and so people whose Windows is gone can find the firmware and drivers their model needs again.

## Sending a report

1. On the laptop, in Windows, run the Omarchy Windows tool and choose **Share a hardware report**.
2. It saves `hardware-report-….zip` in Downloads and opens this repository's form with the model and its hardware IDs filled in.
3. Drag the zip into the form and submit it. You need a free GitHub account.

An Action checks the zip and opens a pull request that adds it under `reports/<manufacturer>/<product>/<report id>/`. [MODELS.md](MODELS.md) lists every model so far.

## What a report holds

| File | What it is |
|---|---|
| `summary.md` | The model, its firmware, processor and panel, and its hardware IDs |
| `report.json` | The same, for scripts, with each ACPI table's OEM IDs |
| `acpi/*.dat` | Every ACPI table the firmware hands Windows; `iasl -d acpi/dsdt.dat` |
| `smbios/dmi.bin` | The SMBIOS table; `dmidecode --from-dump smbios/dmi.bin` |
| `hwids.json` | The CHIDs in systemd's `src/boot/hwids` format, ready once the device tree's compatible is known |
| `edid/*.bin` | The displays' EDID |
| `devices.json` | Every present device: hardware and compatible IDs, ACPI path, location, driver INF, version and problem code |
| `firmware.json` | The firmware files in each driver package, by name, size and SHA-256, with a Microsoft Update Catalog search for the package. The files themselves are not included: they are not ours to redistribute. |

## What a report leaves out

Serial numbers and asset tags, the system UUID, the Windows product key (the MSDM table), display serial numbers, USB serial numbers and MAC addresses in device IDs, and anything paired or plugged in: Bluetooth devices, printers, drives, volumes and audio endpoints. Everything left in describes the model, not the person or the one machine. Look inside the zip before sending it if you like; it is plain files.

## Checking a report by hand

```sh
python3 tools/ingest.py --zip hardware-report-….zip --check-only
python3 tools/ingest.py --zip hardware-report-….zip   # unpacks under reports/
python3 tools/index.py                                # rewrites MODELS.md
```
