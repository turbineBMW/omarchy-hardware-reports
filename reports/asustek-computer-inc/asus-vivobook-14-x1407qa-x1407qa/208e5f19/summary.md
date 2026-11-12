# Hardware report: ASUSTeK COMPUTER INC. ASUS Vivobook 14 X1407QA_X1407QA

| | |
|---|---|
| Manufacturer | ASUSTeK COMPUTER INC. |
| Product | ASUS Vivobook 14 X1407QA_X1407QA |
| Family | ASUS Vivobook 14 |
| Version | 1.0 |
| Baseboard | ASUSTeK COMPUTER INC. X1407QA |
| Firmware | Insyde X1407QA.314 (05/22/2026) |
| Processor | Snapdragon(R) X - X126100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | BOE0A6A |
| Windows | Windows 11 Core 26H2 (build 26300.9711, Arm64) |
| Report | 208e5f19, 2026-11-12, tool 1.2.0 |

## Hardware IDs (CHIDs)

```
   1 MFP---BvRr-- 105faa04-183f-5b23-937e-adb02cd53073
   2 M-P---BvRr-- 16e5acf2-4955-596c-b41e-ce4362648b9f
   5 MFP--------- af52a449-f48c-58f4-a37d-ebe4d5492302
   8 M-P-mp------ 03001eb0-1ca9-5471-979a-3216030eb89c
   9 M-P--------- 87fde16f-5709-5135-8986-8079469adff8
  10 MF--mp------ c62de106-3b06-5f8d-b33c-843d24b00818
  11 MF---------- aac36ff8-1558-5d00-b637-36a524a4c4d7
  12 M---------e- 665276be-80c5-5e5d-929f-fa85d18e2d50
  13 M---mp------ 83542aec-9b0c-5b26-9431-41f0195b9059
  14 M----------- 65605ed1-09e2-57aa-bd0f-a26c1d35433f
ext0 MFP--------E db152867-7643-5677-809e-627f89a6c647
ext1 MF---------E 09436005-6cfd-502f-a908-e14522eb9068
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 17 ACPI tables (facp, dsdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 246 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 408 firmware files in 190 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 190 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3373 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- System serial number
- System UUID
- Baseboard serial number
- Baseboard asset tag
- Chassis serial number
- Chassis asset tag
- Processor serial number
- Memory serial numbers
- Memory asset tags
- Battery serial number
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 114 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 5 registry values and properties named as serial numbers, addresses or identifiers
