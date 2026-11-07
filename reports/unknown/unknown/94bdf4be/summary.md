# Hardware report: unknown computer

| | |
|---|---|
| Panel | LGD07CC |
| Windows | Windows 11 Professional 26H1 (build 28120.3454, Arm64) |
| Report | 94bdf4be, 2026-11-07, tool 1.0.1 |

## Hardware IDs (CHIDs)

```
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 19 ACPI tables (facp, dsdt, ssdt, apic, bert, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, rgrt, sdev, spcr, tpm2, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 313 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 469 firmware files in 239 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 239 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3973 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- System UUID
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 65 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- 15 registry values and properties named as serial numbers, addresses or identifiers

## Could not be read

- Windows lists 10 hardware IDs this report did not compute: b52d5be1-0a5d-5152-9894-2848d2b9e2f5, 3ce1d1e5-028f-5585-85be-793005feea93, 213fd4bd-bfcf-57d6-8a15-0838f4760a16, 924c9073-ff02-57f3-ac65-f96a58faace7, 8348d0ec-17f2-5356-9546-239c59fd9063, 90b52dd0-73fd-53e1-b8c8-014d6dfe15e2, c3f48d5e-195c-5740-9fca-676f7f26cd87, ca2e5189-1d32-509f-88a0-d4ebcc721899, aca387a9-183e-5da9-8f9d-f460c3f50f54, cc0aea32-ad2c-5013-8bed-cede6be8c9f4
